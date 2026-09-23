# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NORMATIVE = ROOT / "docs/proposals/autodescripcion-realidad-distincion.md"
LEDGER = ROOT / "docs/proposals/autodescripcion-realidad-distincion-review-ledger.md"
REFERENCES = ROOT / "docs/proposals/autodescripcion-realidad-distincion-references.md"
TECHNICAL = ROOT / "docs/proposals/work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md"
ARCHIVE = ROOT / "docs/proposals/archive/autodescripcion-realidad-distincion-pre-consolidacion-2026-09-22.md"

ACTIVE_DOCS = (NORMATIVE, LEDGER, REFERENCES, TECHNICAL)

MAX_NORMATIVE_LINES = 2700
MAX_SECTION4_LINES = 400

PRIMARY_LEDGER_ID = re.compile(r"^(REV-\d+[a-z]?|DOC-\d+|FORM-\d+)$")
UNESCAPED_PIPE = re.compile(r"(?<!\\)\|")


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Required proposal document missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def markdown_lines_outside_fences(text: str) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_len = 0

    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        match = re.match(r"^(`{3,}|~{3,})", stripped)

        if match:
            marker = match.group(1)
            marker_char = marker[0]
            if fence_char is None:
                fence_char = marker_char
                fence_len = len(marker)
            elif marker_char == fence_char and len(marker) >= fence_len:
                fence_char = None
                fence_len = 0
            continue

        if fence_char is None:
            result.append((index, line))

    return result


def validate_display_math(path: Path, text: str) -> None:
    lines = markdown_lines_outside_fences(text)
    lone_dollar = [index for index, line in lines if line.strip() == "$"]
    if lone_dollar:
        fail(
            f"{path.relative_to(ROOT)} contains standalone '$' display delimiters at lines "
            + ", ".join(map(str, lone_dollar[:10]))
        )

    display_delimiters = sum(1 for _, line in lines if line.strip() == "$$")
    if display_delimiters % 2:
        fail(
            f"{path.relative_to(ROOT)} has an odd number of standalone '$$' display delimiters: "
            f"{display_delimiters}"
        )


def validate_markdown_table_blocks(path: Path, text: str) -> None:
    lines = text.splitlines()

    for index in range(1, len(lines) - 1):
        if (
            lines[index].strip() == ""
            and lines[index - 1].lstrip().startswith("|")
            and lines[index + 1].lstrip().startswith("|")
        ):
            fail(
                f"{path.relative_to(ROOT)} has a blank line splitting adjacent Markdown table rows "
                f"at line {index + 1}"
            )

    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|"):
            index += 1
            continue

        start = index
        block: list[str] = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            block.append(lines[index])
            index += 1

        if len(block) < 2:
            continue

        pipe_counts = [len(UNESCAPED_PIPE.findall(line)) for line in block]
        expected = pipe_counts[0]
        mismatches = [
            start + offset + 1
            for offset, count in enumerate(pipe_counts)
            if count != expected
        ]
        if mismatches:
            fail(
                f"{path.relative_to(ROOT)} has inconsistent Markdown table column structure "
                f"near lines {start + 1}-{start + len(block)}; mismatches at "
                + ", ".join(map(str, mismatches[:10]))
            )


def validate_ledger(text: str) -> None:
    lines = text.splitlines()

    if sum(line.startswith("# Ledger de revisión") for line in lines) != 1:
        fail("Review ledger must contain exactly one top-level ledger title")
    if sum(line == "## Estados" for line in lines) != 1:
        fail("Review ledger must contain exactly one '## Estados' section")
    if sum(line.startswith("| FORM-02 |") for line in lines) != 1:
        fail("Review ledger must contain exactly one FORM-02 row")

    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        identifier = cells[0]
        if not PRIMARY_LEDGER_ID.fullmatch(identifier):
            continue
        if identifier in seen:
            duplicates.append(f"{identifier} (lines {seen[identifier]} and {line_number})")
        else:
            seen[identifier] = line_number

    if duplicates:
        fail("Duplicate primary ledger identifiers: " + "; ".join(duplicates))


def validate_archive(text: str) -> None:
    first_lines = "\n".join(text.splitlines()[:8])
    if "SUPERSEDED" not in first_lines or "no normativo" not in first_lines:
        fail("Historical pre-consolidation archive must carry a visible SUPERSEDED/non-normative banner")


def validate_index_typing(text: str) -> None:
    checks = {
        r"\\exists!?\s*i\b": "object-level quantification over index metavariable i",
        r"i\s*\\neq\s*j|j\s*\\neq\s*i": "ordinary i\\neq j index relation",
        r"\\operatorname\{Real\}\(x\)": "unindexed Real(x) predicate",
    }

    for pattern, description in checks.items():
        match = re.search(pattern, text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            fail(
                f"{NORMATIVE.relative_to(ROOT)} reintroduces {description} at line {line}; "
                "indices are meta-level type parameters (EXT-02)"
            )


def validate_normative_size(text: str) -> None:
    lines = text.splitlines()
    if len(lines) > MAX_NORMATIVE_LINES:
        fail(
            f"Normative proposal grew to {len(lines)} lines; limit is {MAX_NORMATIVE_LINES}. "
            "Move technical derivations to docs/proposals/work/."
        )

    section4_start = next(
        (index for index, line in enumerate(lines) if line.startswith("## 4.")),
        None,
    )
    if section4_start is None:
        fail("Normative proposal is missing section 4")

    section5_start = next(
        (
            index
            for index, line in enumerate(lines[section4_start + 1 :], start=section4_start + 1)
            if line.startswith("## 5.")
        ),
        None,
    )
    if section5_start is None:
        fail("Normative proposal is missing section 5 after section 4")

    section4_lines = section5_start - section4_start
    if section4_lines > MAX_SECTION4_LINES:
        fail(
            f"Normative section 4 grew to {section4_lines} lines; limit is {MAX_SECTION4_LINES}. "
            "Keep proofs/stress tests in docs/proposals/work/."
        )


def main() -> None:
    contents = {path: read(path) for path in ACTIVE_DOCS}
    archive = read(ARCHIVE)

    for path, text in contents.items():
        validate_display_math(path, text)

    validate_markdown_table_blocks(LEDGER, contents[LEDGER])
    validate_ledger(contents[LEDGER])
    validate_archive(archive)
    validate_index_typing(contents[NORMATIVE])
    validate_normative_size(contents[NORMATIVE])

    print("Proposal document validation passed")
    print(f"Normative lines: {len(contents[NORMATIVE].splitlines())}")
    print("Ledger identifiers: unique")
    print("Display math delimiters: structurally valid")
    print("Historical archive: explicitly superseded")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
