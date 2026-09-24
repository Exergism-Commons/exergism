# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt

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
HIDDEN_BLOCK_BOUNDARY = "\u241e"

# Structural Markdown semantics are delegated to a standards-conformant CommonMark parser.
# Do not reintroduce regex/state-machine parsing for fences, indented code, HTML blocks or comments.
MARKDOWN = MarkdownIt("commonmark", {"html": True})

# Critical TeX is a canonical source contract, not a LaTeX-equivalence problem. Semantically
# equivalent TeX spellings intentionally fail until the canonical contract itself is changed.
# This keeps CI deterministic and prevents validate_proposal_docs.py from becoming a TeX parser.
CANONICAL_EXISTSR = r"""\boxed{
\operatorname{ExistsR}
:\Longleftrightarrow
\exists^{\mathsf M} i\;
\bigl(
\exists\mathfrak G_i\exists R_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\bigr).
}"""

CANONICAL_XP_RGC_EXISTS = r"""\mathrm{RGCExists}_k(\mathfrak G_k),"""

CANONICAL_XP_CLOSURE = r"""\operatorname{RegimeClosure}_k(\mathfrak G_k,C_k)."""

CANONICAL_XP_STRICT_INCLUSION = r"""\boxed{
\bigcup_\alpha C_{\alpha,k}
\subsetneq
C_k
}"""

CANONICAL_PRESENTATION = r"""\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i)."""

DISTINCT_OVERLAP_FRAGMENT = (
    "\\alpha\\neq_{\\mathsf M}\\beta\n"
    "\\land\n"
    "\\operatorname{GeneOverlap}_i"
)

PLURAL_STATUS_LINE = (
    "> **Status contract:** `REV-24d = UNCHANGED`; "
    "`scope realization owner = REV-07/RegimeTotal`; "
    "`Actual/CoReal plural route = NON-DISCHARGING for RegimeGenerated*`."
)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Required proposal document missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def normalize_source(text: str) -> str:
    # markdown-it/CommonMark treats CRLF, CR and LF as source line endings. Normalize them once and
    # use split("\n") everywhere so Python never invents extra lines for Unicode separators.
    return text.replace("\r\n", "\n").replace("\r", "\n")


def inline_plain_text(token: Any) -> str:
    if token.children:
        return "".join(
            child.content
            for child in token.children
            if child.type in {"text", "code_inline"}
        ).strip()
    return token.content.strip()


class MarkdownDocument:
    def __init__(self, text: str) -> None:
        self.text = normalize_source(text)
        self.lines = self.text.split("\n")
        self.tokens = MARKDOWN.parse(self.text)
        self.hidden_lines: set[int] = set()

        # These token types are not active Markdown prose/contracts. Their source ranges are
        # authoritative CommonMark parser output, including all raw-HTML block families.
        for token in self.tokens:
            if token.type not in {"fence", "code_block", "html_block"} or token.map is None:
                continue
            start, end = token.map
            self.hidden_lines.update(range(start, end))

    def active_text(self, start: int = 0, end: int | None = None) -> str:
        if end is None:
            end = len(self.lines)
        return "\n".join(
            HIDDEN_BLOCK_BOUNDARY if line_no in self.hidden_lines else self.lines[line_no]
            for line_no in range(start, end)
        )

    def headings(self) -> list[tuple[int, str, int]]:
        result: list[tuple[int, str, int]] = []
        for index, token in enumerate(self.tokens):
            if token.type != "heading_open" or token.level != 0 or token.map is None:
                continue
            if index + 1 >= len(self.tokens) or self.tokens[index + 1].type != "inline":
                continue
            level = int(token.tag[1:])
            title = inline_plain_text(self.tokens[index + 1])
            result.append((level, title, token.map[0]))
        return result

    def reject_inline_html(self, path: Path) -> None:
        for token in self.tokens:
            if token.type != "inline" or not token.children:
                continue
            if any(child.type == "html_inline" for child in token.children):
                location = ""
                if token.map is not None:
                    location = f" near line {token.map[0] + 1}"
                fail(
                    f"{path.relative_to(ROOT)} contains active inline raw HTML/comment{location}; "
                    "proposal contracts use CommonMark prose/blocks only"
                )

    def section(self, level: int, title: str) -> str:
        headings = self.headings()
        matches = [
            (position, line_no)
            for position, (heading_level, heading_title, line_no) in enumerate(headings)
            if heading_level == level and heading_title == title
        ]
        if not matches:
            fail(f"Missing required active CommonMark heading h{level}: {title}")
        if len(matches) != 1:
            fail(f"Required active CommonMark heading must occur exactly once h{level}: {title}")

        position, start = matches[0]
        end = len(self.lines)
        for next_level, _, next_line in headings[position + 1 :]:
            if next_level <= level:
                end = next_line
                break
        return self.active_text(start, end)


def display_math_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] | None = None

    for line in text.split("\n"):
        delimiter = re.fullmatch(r" {0,3}\$\$[ \t]*", line)
        if delimiter:
            if current is None:
                current = []
            else:
                blocks.append("\n".join(current).strip())
                current = None
            continue

        if current is not None:
            current.append(line)

    if current is not None:
        fail("Unclosed active display-math block inside validated Markdown")
    return blocks


def require_canonical_display_after(
    section: str,
    marker: str,
    expected: str,
    description: str,
) -> None:
    if section.count(marker) != 1:
        fail(f"{description} must have exactly one canonical doctrinal marker: {marker}")

    tail = section.split(marker, 1)[1]
    lines = tail.split("\n")
    index = 0
    while index < len(lines) and re.fullmatch(r"[ \t]*", lines[index]):
        index += 1

    if index >= len(lines) or not re.fullmatch(r" {0,3}\$\$[ \t]*", lines[index]):
        fail(
            f"{description} must begin at the first active block after its doctrinal marker"
        )

    index += 1
    block: list[str] = []
    while index < len(lines) and not re.fullmatch(r" {0,3}\$\$[ \t]*", lines[index]):
        block.append(lines[index])
        index += 1

    if index >= len(lines):
        fail(f"{description} has an unclosed canonical display after its marker")

    actual = "\n".join(block).strip()
    if actual != expected:
        fail(
            f"{description} must use the canonical TeX source immediately after its marker; "
            "equivalent TeX reformatting is intentionally not accepted by CI"
        )


def validate_display_math(path: Path, document: MarkdownDocument) -> None:
    active = document.active_text()
    lines = active.split("\n")

    lone_dollar = [
        index
        for index, line in enumerate(lines, start=1)
        if re.fullmatch(r" {0,3}\$[ \t]*", line)
    ]
    if lone_dollar:
        fail(
            f"{path.relative_to(ROOT)} contains active standalone '$' display delimiters at lines "
            + ", ".join(map(str, lone_dollar[:10]))
        )

    display_delimiters = sum(
        1
        for line in lines
        if re.fullmatch(r" {0,3}\$\$[ \t]*", line)
    )
    if display_delimiters % 2:
        fail(
            f"{path.relative_to(ROOT)} has an odd number of active '$$' display delimiters: "
            f"{display_delimiters}"
        )


def validate_markdown_table_blocks(path: Path, document: MarkdownDocument) -> None:
    lines = document.active_text().split("\n")

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


def validate_ledger(document: MarkdownDocument) -> None:
    lines = document.active_text().split("\n")

    if sum(line.startswith("# Ledger de revisión") for line in lines) != 1:
        fail("Review ledger must contain exactly one active top-level ledger title")
    if sum(line == "## Estados" for line in lines) != 1:
        fail("Review ledger must contain exactly one active '## Estados' section")
    if sum(line.startswith("| FORM-02 |") for line in lines) != 1:
        fail("Review ledger must contain exactly one active FORM-02 row")

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


def validate_archive(document: MarkdownDocument) -> None:
    first_lines = "\n".join(document.active_text().split("\n")[:8])
    if "SUPERSEDED" not in first_lines or "no normativo" not in first_lines:
        fail("Historical pre-consolidation archive must carry a visible SUPERSEDED/non-normative banner")


def validate_index_typing(current: str) -> None:
    checks = {
        r"\\exists!?\s*i\b": "object-level existential quantification over index metavariable i",
        r"\\forall\s*i\b": "object-level universal quantification over index metavariable i",
        r"i\s*\\neq\s*j|j\s*\\neq\s*i": "ordinary i\\neq j index relation",
        r"i\s*\\in\s*I\b": "membership of index metavariable i in an index domain I",
        r"\\operatorname\{Real\}\(x\)": "unindexed Real(x) predicate",
    }

    for pattern, description in checks.items():
        match = re.search(pattern, current)
        if match:
            line = current.count("\n", 0, match.start()) + 1
            fail(
                f"{NORMATIVE.relative_to(ROOT)} reintroduces {description} at active line {line}; "
                "indices are meta-level type parameters (EXT-02)"
            )


def validate_regime_total_contract(
    normative: MarkdownDocument,
    ledger: MarkdownDocument,
    technical: MarkdownDocument,
) -> None:
    current = normative.active_text().split("# II. Historia cronológica", 1)[0]
    visible_ledger = ledger.active_text()
    visible_technical = technical.active_text()

    required_current = {
        r"\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)": "RegimeTotal totality target",
        r"\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)": "RegimeClosure definition",
        r"\operatorname{GeneFamily}_i(\mathfrak G_i)": "explicit GeneFamily contract",
        r"\operatorname{GeneBasis}_i(\mathfrak G_i)": "GeneBasis guard",
        r"\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)": "RegimeGenerated membership",
    }
    for snippet, description in required_current.items():
        if snippet not in current:
            fail(
                f"REV-07f regression: normative proposal is missing canonical {description}"
            )

    existsr_section = normative.section(
        3,
        "1.9. ExistsR es una metasentencia, no un cuantificador sobre índices",
    )
    require_canonical_display_after(
        existsr_section,
        "El target doctrinal se escribe ahora:",
        CANONICAL_EXISTSR,
        "REV-07f active normative ExistsR formula",
    )

    if sum(line.startswith("| REV-07f |") for line in visible_ledger.split("\n")) != 1:
        fail("REV-07f regression: review ledger must contain exactly one active REV-07f row")

    for level, heading in (
        (4, "RT-07-MG — Multigeneal Reality Test"),
        (4, "RT-07-XP — Transversal Production Test"),
        (4, "RT-07-MG-TRIV — Singleton-per-token attack"),
    ):
        technical.section(level, heading)

    if DISTINCT_OVERLAP_FRAGMENT not in current or DISTINCT_OVERLAP_FRAGMENT not in visible_technical:
        fail(
            "REV-07f regression: GeneFamily must retain the canonical distinct-member "
            "OverlapCoherence guard in both active documents"
        )

    xp_section = technical.section(4, "RT-07-XP — Transversal Production Test")
    require_canonical_display_after(
        xp_section,
        "Supongamos ahora explícitamente:",
        CANONICAL_XP_RGC_EXISTS,
        "RT-07-XP affirmative RGCExists premise",
    )
    require_canonical_display_after(
        xp_section,
        "y fijemos un testigo $C_k$ tal que:",
        CANONICAL_XP_CLOSURE,
        "RT-07-XP explicit RegimeClosure witness",
    )
    require_canonical_display_after(
        xp_section,
        "Por tanto:",
        CANONICAL_XP_STRICT_INCLUSION,
        "RT-07-XP strict transversal-growth conclusion",
    )

    presentation_section = technical.section(4, "8.5. ExistsR como metasentencia")
    require_canonical_display_after(
        presentation_section,
        "y una presentación semántica produce únicamente:",
        CANONICAL_PRESENTATION,
        "REV-07f §8.5 presentation implication",
    )

    pure_relation_section = technical.section(
        4,
        "0.4.6. Stress test mixto: relación–genealogía–relación",
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

    plural_route_section = technical.section(5, "Ruta plural")
    active_status_lines = [
        line
        for line in plural_route_section.split("\n")
        if re.fullmatch(r" {0,3}" + re.escape(PLURAL_STATUS_LINE), line)
    ]
    if len(active_status_lines) != 1:
        fail(
            "REV-07f regression: plural-route status must appear exactly once as "
            "the canonical active top-level blockquote contract"
        )
    if re.search(r"REV-24d[^\n]{0,120}\bPARTIAL\b", plural_route_section):
        fail(
            "REV-07f regression: plural route again assigns PARTIAL status to REV-24d"
        )

    historical_dilemma = technical.section(
        4,
        "0.11.3. HISTORICAL — dilema monogeneal pre-REV-07f",
    )
    if r"\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)" not in historical_dilemma:
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
    lines = normalize_source(text).split("\n")
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
    documents = {path: MarkdownDocument(text) for path, text in contents.items()}
    archive_text = read(ARCHIVE)
    archive_document = MarkdownDocument(archive_text)

    for path, document in documents.items():
        document.reject_inline_html(path)
        validate_display_math(path, document)

    validate_markdown_table_blocks(LEDGER, documents[LEDGER])
    validate_ledger(documents[LEDGER])
    validate_archive(archive_document)

    current_normative = documents[NORMATIVE].active_text().split(
        "# II. Historia cronológica", 1
    )[0]
    validate_index_typing(current_normative)

    validate_regime_total_contract(
        documents[NORMATIVE],
        documents[LEDGER],
        documents[TECHNICAL],
    )
    validate_normative_size(contents[NORMATIVE])

    print("Proposal document validation passed")
    print(f"Normative lines: {len(normalize_source(contents[NORMATIVE]).split(chr(10)))}")
    print("CommonMark structure: parsed by markdown-it-py")
    print("Critical REV-07f TeX: canonical source contracts preserved")
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
