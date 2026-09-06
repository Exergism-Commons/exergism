#!/usr/bin/env python3
"""Materialize the Exergism pre-1.0 semantic namespace migration.

Historical releases are intentionally untouched. The active ontology generator
is moved from the legacy exergia.org namespace to the Exergism Commons
persistent identifier authority, then ontology.owl is deterministically
regenerated from the canonical corpus.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_ontology.py"
ONTOLOGY = ROOT / "ontology.owl"
OLD = 'BASE_IRI = "http://www.exergia.org/ns/"'
NEW = 'BASE_IRI = "https://id.exergism.org/exergism#"'


def main() -> int:
    text = GENERATOR.read_text(encoding="utf-8")
    old_count = text.count(OLD)
    new_count = text.count(NEW)
    if old_count == 1 and new_count == 0:
        GENERATOR.write_text(text.replace(OLD, NEW), encoding="utf-8")
    elif old_count == 0 and new_count == 1:
        pass
    else:
        raise SystemExit(
            f"unexpected BASE_IRI state: old={old_count}, new={new_count}; refusing ambiguous rewrite"
        )

    subprocess.run([sys.executable, str(GENERATOR)], cwd=ROOT, check=True)

    rendered = ONTOLOGY.read_text(encoding="utf-8")
    if not rendered.strip():
        raise SystemExit("ontology.owl is empty after regeneration")
    if "http://www.exergia.org/ns/" in rendered:
        raise SystemExit("legacy exergia.org namespace remains in generated ontology")
    if "https://id.exergism.org/exergism#" not in rendered:
        raise SystemExit("new Exergism namespace missing from generated ontology")

    print("Exergism semantic namespace materialized successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
