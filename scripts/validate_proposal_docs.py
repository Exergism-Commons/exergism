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

MAX_NORMATIVE_LINES = 2850
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
        if fence_char is None:
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if opening:
                marker = opening.group(1)
                info_string = opening.group(2)
                if marker[0] != "`" or "`" not in info_string:
                    fence_char = marker[0]
                    fence_len = len(marker)
                    continue

            result.append((index, line))
            continue

        closing = re.fullmatch(
            rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*$",
            line,
        )
        if closing:
            fence_char = None
            fence_len = 0

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


def markdown_heading(line: str) -> tuple[int, str] | None:
    match = re.match(r"^ {0,3}(#{1,6})(?:[ \t]+|$)(.*)$", line)
    if not match:
        return None

    title = match.group(2).strip()
    closing = re.match(r"^(.*?)[ \t]+#+[ \t]*$", title)
    if closing:
        title = closing.group(1).rstrip()

    return len(match.group(1)), title


def markdown_section(text: str, heading: str) -> str:
    target = markdown_heading(heading)
    if target is None:
        fail(f"Invalid Markdown heading passed to markdown_section: {heading}")
    target_level, target_title = target

    outside = markdown_lines_outside_fences(text)
    matches = [
        position
        for position, (_, line) in enumerate(outside)
        if markdown_heading(line) == (target_level, target_title)
    ]
    if not matches:
        fail(f"Missing required section heading outside Markdown fences: {heading}")
    if len(matches) != 1:
        fail(f"Section heading must occur exactly once outside Markdown fences: {heading}")

    section: list[str] = []
    for _, line in outside[matches[0] :]:
        next_heading = markdown_heading(line)
        if section and next_heading and next_heading[0] <= target_level:
            break
        section.append(line)

    return "\n".join(section)


def display_math_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] | None = None

    for line in text.splitlines():
        delimiter = re.fullmatch(r"^ {0,3}\$\$[ \t]*$", line)
        if delimiter:
            if current is None:
                current = []
            else:
                blocks.append("\n".join(current))
                current = None
            continue

        if current is not None:
            current.append(line)

    if current is not None:
        fail("Unclosed display-math block inside validated Markdown section")

    return blocks


def first_display_math_after(text: str, marker: str) -> str:
    if marker not in text:
        fail(f"Missing required marker before display-math contract: {marker}")
    tail = text.split(marker, 1)[1]
    blocks = display_math_blocks(tail)
    if not blocks:
        fail(f"Missing display-math block after marker: {marker}")
    return blocks[0]


def split_top_level_tex_conjuncts(text: str) -> list[str]:
    parts: list[str] = []
    start = 0
    brace_depth = 0
    paren_depth = 0
    index = 0

    while index < len(text):
        char = text[index]
        if char == "{":
            brace_depth += 1
        elif char == "}":
            brace_depth = max(0, brace_depth - 1)
        elif char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth = max(0, paren_depth - 1)

        if brace_depth == 0 and paren_depth == 0:
            if char in "+,":
                parts.append(text[start:index].strip())
                start = index + 1
            else:
                connective = next(
                    (
                        token
                        for token in (r"\land", r"\wedge")
                        if text.startswith(token, index)
                        and (
                            index + len(token) == len(text)
                            or not text[index + len(token)].isalpha()
                        )
                    ),
                    None,
                )
                if connective is not None:
                    parts.append(text[start:index].strip())
                    index += len(connective) - 1
                    start = index + 1
        index += 1

    parts.append(text[start:].strip())
    return [part for part in parts if part]


def validate_index_typing(text: str) -> None:
    checks = {
        r"\\exists!?\s*i\b": "object-level existential quantification over index metavariable i",
        r"\\forall\s*i\b": "object-level universal quantification over index metavariable i",
        r"i\s*\\neq\s*j|j\s*\\neq\s*i": "ordinary i\\neq j index relation",
        r"i\s*\\in\s*I\b": "membership of index metavariable i in an index domain I",
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


def validate_regime_total_contract(normative: str, ledger: str, technical: str) -> None:
    current = normative.split("# II. Historia cronológica", 1)[0]

    required_current = {
        r"\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)": "RegimeTotal totality target",
        r"\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)": "RegimeClosure definition",
        r"\operatorname{GeneFamily}_i(\mathfrak G_i)": "explicit GeneFamily contract",
        r"\operatorname{GeneBasis}_i(\mathfrak G_i)": "GeneBasis guard",
        r"\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)": "RegimeGenerated membership",
        "\\exists\\mathfrak G_i\\exists R_i\\;" + "\n" + "\\operatorname{RegimeTotal}_i(\\mathfrak G_i,R_i)": "ExistsR RegimeTotal witness",
    }
    for snippet, description in required_current.items():
        if snippet not in current:
            fail(f"REV-07f regression: normative proposal is missing {description}")

    old_exists_witness = (
        "\\exists\\mathcal O_i\\exists R_i\\;" + "\n"
        + "\\operatorname{GeneTotal}_i(\\mathcal O_i,R_i)"
    )
    if old_exists_witness in current:
        fail(
            "REV-07f regression: active normative text again uses GeneTotal as the "
            "general ExistsR witness; total existence must range over RegimeTotal"
        )

    if sum(line.startswith("| REV-07f |") for line in ledger.splitlines()) != 1:
        fail("REV-07f regression: review ledger must contain exactly one REV-07f row")

    for heading in (
        "#### RT-07-MG — Multigeneal Reality Test",
        "#### RT-07-XP — Transversal Production Test",
        "#### RT-07-MG-TRIV — Singleton-per-token attack",
    ):
        markdown_section(technical, heading)

    distinct_overlap_guard = (
        "\\alpha\\neq_{\\mathsf M}\\beta" + "\n"
        + "\\land" + "\n"
        + "\\operatorname{GeneOverlap}_i"
    )
    if distinct_overlap_guard not in current or distinct_overlap_guard not in technical:
        fail(
            "REV-07f regression: GeneFamily must require OverlapCoherence only "
            "between distinct family members"
        )

    xp_section = markdown_section(
        technical,
        "#### RT-07-XP — Transversal Production Test",
    )

    rgc_pattern = (
        r"\\mathrm\s*\{RGCExists\}_k\s*\(\s*"
        r"\\mathfrak(?:\s*\{G\}|\s+G)_k\s*\)\s*,?"
    )
    rgc_formula = first_display_math_after(
        xp_section,
        "Supongamos ahora explícitamente:",
    )
    if not re.fullmatch(rgc_pattern, rgc_formula, flags=re.MULTILINE):
        fail(
            "REV-07f regression: RT-07-XP must assert an affirmative RGCExists "
            "premise in the first display block after its assumption marker"
        )

    closure_pattern = (
        r"\\operatorname\s*\{RegimeClosure\}_k\s*\(\s*"
        r"\\mathfrak(?:\s*\{G\}|\s+G)_k\s*,\s*C_k\s*\)\s*\.?"
    )
    closure_formula = first_display_math_after(
        xp_section,
        "y fijemos un testigo $C_k$ tal que:",
    )
    if not re.fullmatch(closure_pattern, closure_formula, flags=re.MULTILINE):
        fail(
            "REV-07f regression: RT-07-XP must bind an affirmative explicit "
            "RegimeClosure witness in its witness display block"
        )

    strict_formula = first_display_math_after(
        xp_section,
        "Por tanto:",
    )
    strict_pattern = (
        r"\s*\\boxed\s*\{\s*"
        r"\\bigcup\s*_\s*(?:\{\\alpha\}|\\alpha)\s+"
        r"C_\{\\alpha,k\}\s*"
        r"\\subsetneq\s*C_k\s*"
        r"\}\s*\.?"
    )
    if not re.fullmatch(strict_pattern, strict_formula, flags=re.MULTILINE):
        fail(
            "REV-07f regression: RT-07-XP must affirm, at top level, the boxed "
            "strict inclusion of the local-closure union in C_k"
        )

    if re.search(
        r"\\operatorname\s*\{RegimeClosure\}_k\s*\(\s*"
        r"\\mathfrak(?:\s*\{G\}|\s+G)_k\s*\)\s*\.",
        xp_section,
        flags=re.MULTILINE,
    ):
        fail(
            "REV-07f regression: RT-07-XP again treats RegimeClosure as a unary "
            "carrier-valued term"
        )

    presentation_section = markdown_section(
        technical,
        "#### 8.5. `ExistsR` como metasentencia",
    )
    presentation_marker = "y una presentación semántica produce únicamente:"
    presentation_formula = first_display_math_after(
        presentation_section,
        presentation_marker,
    )

    if presentation_formula.count(r"\Rightarrow") != 1:
        fail(
            "REV-07f regression: active §8.5 presentation contract must contain "
            "exactly one forward \\Rightarrow implication"
        )
    if r"\Leftarrow" in presentation_formula or r"\Leftrightarrow" in presentation_formula:
        fail(
            "REV-07f regression: active §8.5 presentation contract has the wrong "
            "implication direction"
        )

    antecedent, consequent = presentation_formula.split(r"\Rightarrow", 1)
    antecedent_parts = split_top_level_tex_conjuncts(antecedent)

    premise_patterns = (
        (
            r"\\operatorname\s*\{RegimeTotal\}_i\s*\(\s*"
            r"\\mathfrak(?:\s*\{G\}|\s+G)_i\s*,\s*R_i\s*\)",
            "RegimeTotal premise",
        ),
        (
            r"\\operatorname\s*\{SemTotal\}_i\s*\(\s*S_i\s*\)",
            "SemTotal premise",
        ),
        (r"\\mathrm\s*\{OTB\}_i", "OTB bridge premise"),
    )
    if len(antecedent_parts) != len(premise_patterns):
        fail(
            "REV-07f regression: §8.5 presentation antecedent must contain exactly "
            "RegimeTotal, SemTotal, and OTB as top-level premises"
        )

    unmatched = antecedent_parts.copy()
    for pattern, description in premise_patterns:
        match_index = next(
            (
                index
                for index, part in enumerate(unmatched)
                if re.fullmatch(pattern, part, flags=re.MULTILINE)
            ),
            None,
        )
        if match_index is None:
            fail(
                "REV-07f regression: active §8.5 presentation antecedent is missing "
                f"an affirmative {description}"
            )
        unmatched.pop(match_index)

    if not re.fullmatch(
        r"\\operatorname\s*\{Presents\}_i\s*\(\s*S_i\s*,\s*R_i\s*\)\s*\.?",
        consequent.strip(),
        flags=re.MULTILINE,
    ):
        fail(
            "REV-07f regression: active §8.5 presentation implication must conclude "
            "exactly Presents_i(S_i,R_i)"
        )

    if re.search(r"\\operatorname\s*\{GeneTotal\}_i", presentation_formula):
        fail(
            "REV-07f regression: active §8.5 presentation bridge again requires "
            "GeneTotal instead of RegimeTotal"
        )

    pure_relation_section = markdown_section(
        technical,
        "#### 0.4.6. Stress test mixto: relación–genealogía–relación",
    )
    if "ensamblaje de GeneTotal" in pure_relation_section:
        fail(
            "REV-07f regression: active pure-relation assembly discussion again "
            "targets GeneTotal instead of the RegimeTotal architecture"
        )
    for term in ("SharedOntSpace", "GeneFamily/GeneBasis", "RegimeClosure", "RegimeTotal"):
        if term not in pure_relation_section:
            fail(
                "REV-07f regression: active pure-relation assembly discussion is "
                f"missing current regime-level term {term}"
            )

    historical_dilemma = markdown_section(
        technical,
        "#### 0.11.3. HISTORICAL — dilema monogeneal pre-REV-07f",
    )
    if "\\operatorname{RegimeTotal}_i(\\mathfrak G_i,R_i)" not in historical_dilemma:
        fail(
            "REV-07f regression: historical single-origin dilemma no longer records "
            "RegimeTotal as the current general architecture"
        )
    if "la arquitectura vigente de:" in historical_dilemma:
        fail(
            "REV-07f regression: historical §0.11.3 again labels the single-origin "
            "GeneTotal architecture as current"
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
    validate_regime_total_contract(
        contents[NORMATIVE],
        contents[LEDGER],
        contents[TECHNICAL],
    )
    validate_normative_size(contents[NORMATIVE])

    print("Proposal document validation passed")
    print(f"Normative lines: {len(contents[NORMATIVE].splitlines())}")
    print("Ledger identifiers: unique")
    print("Display math delimiters: structurally valid")
    print("Historical archive: explicitly superseded")
    print("REV-07f RegimeTotal contract: preserved")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
