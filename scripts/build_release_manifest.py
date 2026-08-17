# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_paths() -> list[Path]:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    paths: list[Path] = [
        ROOT / manifest["canonical_content_schema"],
        ROOT / manifest["books"],
        ROOT / manifest["formal_exergic_analysis"],
        ROOT / manifest["derived_ontology"],
        ROOT / manifest["symbol"],
    ]
    paths.extend(ROOT / "content" / name for name in manifest["philosophical_corpus"]["order"])
    for directory in manifest.get("examples", []):
        paths.extend(sorted(path for path in (ROOT / directory).rglob("*") if path.is_file()))
    return sorted(set(paths), key=lambda path: path.relative_to(ROOT).as_posix())


def build(version: str, git_commit: str) -> dict:
    entries = []
    aggregate = hashlib.sha256()
    for path in canonical_paths():
        relative = path.relative_to(ROOT).as_posix()
        size = path.stat().st_size
        digest = sha256(path)
        entries.append({"path": relative, "bytes": size, "sha256": digest})
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\0")
        aggregate.update(str(size).encode("ascii"))
        aggregate.update(b"\n")

    return {
        "manifest_version": 1,
        "project": "Exergism",
        "formal_name": "Metafisica emergentista de la liberacion",
        "release": version,
        "git_commit": git_commit,
        "canonical_digest_algorithm": "sha256(path\\0sha256\\0bytes\\n)",
        "canonical_digest": aggregate.hexdigest(),
        "artifacts": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an immutable Exergism release manifest")
    parser.add_argument("--version", required=True)
    parser.add_argument("--git-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = build(args.version, args.git_commit)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
