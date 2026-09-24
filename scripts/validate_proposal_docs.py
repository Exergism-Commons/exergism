# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

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
MARKDOWN = (
    MarkdownIt("commonmark", {"html": True})
    .enable("table")
    .use(
        dollarmath_plugin,
        allow_blank_lines=True,
    )
)

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

CANONICAL_REGIME_GENERATED = r"""\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)
\land
x_i\in C_i
]."""

CANONICAL_REGIME_TOTAL = r"""\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
:\Longleftrightarrow
\operatorname{GeneBasis}_i(\mathfrak G_i)
\land
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\Longleftrightarrow
\operatorname{Real}_i(x_i)
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
].
}"""

CANONICAL_GENE_FAMILY = r"""\boxed{
\begin{aligned}
\operatorname{GeneFamily}_i(\mathfrak G_i)
:\Longleftrightarrow\;&
A\neq_{\mathsf M}\varnothing\\
&\land
\forall^{\mathsf M}\alpha\in A\;
\operatorname{GeneUnit}_i(
\mathcal O_{\alpha,i},
C_{\alpha,i}
)\\
&\land
\forall^{\mathsf M}\alpha,\beta\in A[
\alpha\neq_{\mathsf M}\beta
\land
\operatorname{GeneOverlap}_i(
G_{\alpha,i},
G_{\beta,i}
)
\Rightarrow
\operatorname{OverlapCoherence}_i(
G_{\alpha,i},
G_{\beta,i}
)
].
\end{aligned}
}"""

CANONICAL_REGIME_CLOSURE = r"""\boxed{
\begin{aligned}
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)
:\Longleftrightarrow
\exists B_i[
&\operatorname{FamilyBase}_i(\mathfrak G_i,B_i)
\land
B_i\preceq C_i
\land
\Gamma_i(C_i)=C_i\\
&\land
\forall Y_i[
B_i\preceq Y_i
\land
\Gamma_i(Y_i)=Y_i
\Rightarrow
C_i\preceq Y_i
]
].
\end{aligned}
}"""

CANONICAL_GENE_BASIS = r"""\boxed{
\operatorname{GeneBasis}_i(\mathfrak G_i)
:\Longleftrightarrow
\operatorname{GeneFamily}_i(\mathfrak G_i)
\land
\mathrm{RGCExists}_i(\mathfrak G_i)
\land
\mathrm{FamilyIrredundant}_i(\mathfrak G_i).
}"""

DISTINCT_OVERLAP_FRAGMENT = (
    "\\alpha\\neq_{\\mathsf M}\\beta\n"
    "\\land\n"
    "\\operatorname{GeneOverlap}_i"
)

PLURAL_STATUS_TEXT = (
    "Status contract: REV-24d = UNCHANGED; "
    "scope realization owner = REV-07/RegimeTotal; "
    "Actual/CoReal plural route = NON-DISCHARGING for RegimeGenerated*."
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


def visible_inline_text(token: Any) -> str:
    if not token.children:
        return token.content.strip()

    parts: list[str] = []
    transparent = {
        "em_open",
        "em_close",
        "strong_open",
        "strong_close",
        "link_open",
        "link_close",
    }

    for child in token.children:
        if child.type in {"text", "code_inline"}:
            parts.append(child.content)
        elif child.type == "math_inline":
            markup = child.markup or "$"
            parts.append(f"{markup}{child.content}{markup}")
        elif child.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
        elif child.type in transparent:
            continue
        elif child.type in {"image", "html_inline"}:
            parts.append(HIDDEN_BLOCK_BOUNDARY)
        else:
            # Unknown visible inline nodes must never disappear from semantic identity.
            parts.append(HIDDEN_BLOCK_BOUNDARY)

    return "".join(parts).strip()


class MarkdownDocument:
    def __init__(self, text: str) -> None:
        self.text = normalize_source(text)
        self.lines = self.text.split("\n")
        self.env: dict[str, Any] = {}
        self.tokens = MARKDOWN.parse(self.text, self.env)
        self.hidden_lines: set[int] = set()

        # Non-prose source ranges come directly from parser tokens. Math remains available
        # semantically through math_block tokens, but its raw source must never satisfy prose,
        # table, ledger, or other source-structural guards.
        for token in self.tokens:
            if token.type in {
                "fence",
                "code_block",
                "html_block",
                "math_block",
                "math_block_label",
            } and token.map is not None:
                start, end = token.map
                self.hidden_lines.update(range(start, end))

        # CommonMark reference definitions are parser-consumed source and do not render. markdown-it
        # records their exact source ranges in env["references"]; hide those ranges directly rather
        # than inferring non-rendered lines from gaps between token maps.
        for reference in self.env.get("references", {}).values():
            mapping = reference.get("map")
            if mapping is None:
                continue
            start, end = mapping
            self.hidden_lines.update(range(start, end))

        for duplicate in self.env.get("duplicate_refs", []):
            mapping = duplicate.get("map")
            if mapping is None:
                continue
            start, end = mapping
            self.hidden_lines.update(range(start, end))

    def active_text(self, start: int = 0, end: int | None = None) -> str:
        if end is None:
            end = len(self.lines)
        return "\n".join(
            HIDDEN_BLOCK_BOUNDARY if line_no in self.hidden_lines else self.lines[line_no]
            for line_no in range(start, end)
        )

    def semantic_text(self, start: int = 0, end: int | None = None) -> str:
        if end is None:
            end = len(self.lines)

        parts: list[str] = []
        for token in self.tokens:
            if token.map is None:
                continue
            if not (start <= token.map[0] and token.map[1] <= end):
                continue

            if token.type == "inline":
                parts.append(visible_inline_text(token))
            elif token.type in {"math_block", "math_block_label"}:
                parts.append(token.content.strip())

        return "\n".join(part for part in parts if part)

    def parsed_math_lines(self) -> set[int]:
        result: set[int] = set()
        for token in self.tokens:
            if token.type not in {"math_block", "math_block_label"} or token.map is None:
                continue
            start, end = token.map
            result.update(range(start, end))
        return result

    def headings(self) -> list[tuple[int, str, int]]:
        result: list[tuple[int, str, int]] = []
        for index, token in enumerate(self.tokens):
            if token.type != "heading_open" or token.level != 0 or token.map is None:
                continue
            if index + 1 >= len(self.tokens) or self.tokens[index + 1].type != "inline":
                continue
            level = int(token.tag[1:])
            title = visible_inline_text(self.tokens[index + 1])
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

    def section_bounds(self, level: int, title: str) -> tuple[int, int]:
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
        return start, end

    def section(self, level: int, title: str) -> str:
        start, end = self.section_bounds(level, title)
        return self.active_text(start, end)

    def heading_start(self, level: int, title: str) -> int:
        start, _ = self.section_bounds(level, title)
        return start

    def math_blocks(self, start: int, end: int) -> list[Any]:
        return [
            token
            for token in self.tokens
            if token.type == "math_block"
            and token.level == 0
            and token.map is not None
            and start <= token.map[0]
            and token.map[1] <= end
        ]

    def marker_inline_tokens(self, start: int, end: int, marker: str) -> list[tuple[int, Any]]:
        matches: list[tuple[int, Any]] = []
        for index, token in enumerate(self.tokens):
            if token.type != "inline" or token.map is None:
                continue
            if not (start <= token.map[0] and token.map[1] <= end):
                continue

            # A doctrinal marker is a complete root paragraph, not a substring inside
            # a disclaimer, quotation, list item, blockquote, or larger sentence.
            if (
                index == 0
                or self.tokens[index - 1].type != "paragraph_open"
                or self.tokens[index - 1].level != 0
            ):
                continue
            if visible_inline_text(token) == marker:
                matches.append((index, token))
        return matches

    def root_blocks_after(self, token_index: int, line_no: int, end: int) -> list[Any]:
        return [
            token
            for token in self.tokens[token_index + 1 :]
            if token.level == 0
            and token.map is not None
            and line_no <= token.map[0] < end
        ]

    def table_body_rows(
        self,
        start: int,
        end: int,
        description: str,
    ) -> list[list[str]]:
        table_indices = [
            index
            for index, token in enumerate(self.tokens)
            if token.type == "table_open"
            and token.map is not None
            and start <= token.map[0]
            and token.map[1] <= end
        ]
        if len(table_indices) != 1:
            fail(
                f"{description} must contain exactly one parsed table "
                f"(found {len(table_indices)})"
            )

        table_index = table_indices[0]
        rows: list[list[str]] = []
        in_tbody = False
        index = table_index + 1

        while index < len(self.tokens):
            token = self.tokens[index]
            if token.type == "table_close":
                break
            if token.type == "tbody_open":
                in_tbody = True
                index += 1
                continue
            if token.type == "tbody_close":
                in_tbody = False
                index += 1
                continue

            if in_tbody and token.type == "tr_open":
                cells: list[str] = []
                cursor = index + 1
                while cursor < len(self.tokens) and self.tokens[cursor].type != "tr_close":
                    child = self.tokens[cursor]
                    if child.type == "inline":
                        cells.append(visible_inline_text(child))
                    cursor += 1
                rows.append(cells)
                index = cursor + 1
                continue

            index += 1

        if index >= len(self.tokens) or self.tokens[index].type != "table_close":
            fail(f"{description} parsed table is not structurally closed")
        if not rows:
            fail(f"{description} parsed table body is empty")

        return rows

    def parsed_blockquote_texts(self, start: int, end: int) -> list[str]:
        results: list[str] = []
        index = 0
        while index < len(self.tokens):
            token = self.tokens[index]
            if (
                token.type != "blockquote_open"
                or token.level != 0
                or token.map is None
                or not (start <= token.map[0] and token.map[1] <= end)
            ):
                index += 1
                continue

            depth = 1
            inline_parts: list[str] = []
            cursor = index + 1
            while cursor < len(self.tokens) and depth:
                child = self.tokens[cursor]
                if child.type == "blockquote_open":
                    depth += 1
                elif child.type == "blockquote_close":
                    depth -= 1
                    if depth == 0:
                        break
                elif depth == 1 and child.type == "inline":
                    inline_parts.append(visible_inline_text(child))
                cursor += 1

            results.append("\n".join(inline_parts).strip())
            index = cursor + 1
        return results


def require_canonical_display(
    document: MarkdownDocument,
    bounds: tuple[int, int],
    expected: str,
    description: str,
) -> None:
    start, end = bounds
    matches = [
        token
        for token in document.math_blocks(start, end)
        if token.content.strip() == expected
    ]
    if len(matches) != 1:
        fail(
            f"{description} must occur exactly once as a parsed canonical math_block "
            "inside the designated definition section"
        )


def require_canonical_display_after(
    document: MarkdownDocument,
    bounds: tuple[int, int],
    marker: str,
    expected: str,
    description: str,
) -> None:
    start, end = bounds
    markers = document.marker_inline_tokens(start, end, marker)
    if len(markers) != 1:
        fail(f"{description} must have exactly one parsed doctrinal marker: {marker}")

    marker_index, marker_token = markers[0]
    if marker_token.map is None:
        fail(f"{description} marker has no parser source map")

    next_blocks = document.root_blocks_after(marker_index, marker_token.map[1], end)
    if not next_blocks or next_blocks[0].type != "math_block":
        fail(
            f"{description} must be the first parsed block after its doctrinal marker"
        )

    math_token = next_blocks[0]
    if math_token.content.strip() != expected:
        fail(
            f"{description} must use the canonical TeX content in the parsed math_block "
            "immediately after its marker"
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
    headings = document.headings()
    if sum(
        1
        for level, title, _ in headings
        if level == 1 and title == "Ledger de revisión — autodescripción, realidad y distinción"
    ) != 1:
        fail("Review ledger must contain exactly one parsed top-level ledger title")

    if sum(
        1
        for level, title, _ in headings
        if level == 2 and title == "Estados"
    ) != 1:
        fail("Review ledger must contain exactly one parsed 'Estados' section")

    priority_bounds = document.section_bounds(2, "Prioridad de trabajo")
    body_rows = document.table_body_rows(
        *priority_bounds,
        description="Review ledger Prioridad de trabajo section",
    )

    if sum(1 for row in body_rows if row and row[0] == "FORM-02") != 1:
        fail("Review ledger must contain exactly one parsed FORM-02 table row")

    if sum(1 for row in body_rows if row and row[0] == "REV-07f") != 1:
        fail("REV-07f regression: review ledger must contain exactly one parsed REV-07f table row")

    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for row_number, row in enumerate(body_rows, start=1):
        if not row:
            continue
        identifier = row[0].strip()
        if not PRIMARY_LEDGER_ID.fullmatch(identifier):
            continue
        if identifier in seen:
            duplicates.append(
                f"{identifier} (parsed rows {seen[identifier]} and {row_number})"
            )
        else:
            seen[identifier] = row_number

    if duplicates:
        fail("Duplicate primary ledger identifiers: " + "; ".join(duplicates))


def validate_archive(document: MarkdownDocument) -> None:
    first_visible = document.semantic_text(0, min(8, len(document.lines)))
    if "SUPERSEDED" not in first_visible or "no normativo" not in first_visible:
        fail("Historical pre-consolidation archive must carry a visible SUPERSEDED/non-normative banner")


def validate_index_typing(current: str) -> None:
    tex_gap = r"(?:\s|\\[,;:!]|\\(?:quad|qquad)|\{\s*\})*"
    index_i = r"(?:i\b|\{\s*i\s*\})"
    checks = {
        rf"\\exists!?{tex_gap}{index_i}": "object-level existential quantification over index metavariable i",
        rf"\\forall{tex_gap}{index_i}": "object-level universal quantification over index metavariable i",
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
    totalization_bounds = normative.section_bounds(
        3,
        "1.6. $R_i$ — totalización genealógica mono- y multigeneal",
    )
    require_canonical_display(
        normative,
        totalization_bounds,
        CANONICAL_REGIME_GENERATED,
        "REV-07f RegimeGenerated* definition",
    )
    require_canonical_display(
        normative,
        totalization_bounds,
        CANONICAL_REGIME_TOTAL,
        "REV-07f RegimeTotal definition",
    )

    genealogy_bounds = normative.section_bounds(
        3,
        "5.1. Criterio primario: origen unificado + generación independiente",
    )
    require_canonical_display(
        normative,
        genealogy_bounds,
        CANONICAL_GENE_FAMILY,
        "REV-07f GeneFamily definition",
    )
    require_canonical_display(
        normative,
        genealogy_bounds,
        CANONICAL_REGIME_CLOSURE,
        "REV-07f RegimeClosure definition",
    )
    require_canonical_display(
        normative,
        genealogy_bounds,
        CANONICAL_GENE_BASIS,
        "REV-07f GeneBasis definition",
    )

    technical_genealogy_bounds = technical.section_bounds(
        3,
        "0.10a. REV-07f — RegimeTotal multigeneal",
    )
    require_canonical_display(
        technical,
        technical_genealogy_bounds,
        CANONICAL_GENE_FAMILY,
        "REV-07f technical GeneFamily definition",
    )

    existsr_bounds = normative.section_bounds(
        3,
        "1.9. ExistsR es una metasentencia, no un cuantificador sobre índices",
    )
    require_canonical_display_after(
        normative,
        existsr_bounds,
        "El target doctrinal se escribe ahora:",
        CANONICAL_EXISTSR,
        "REV-07f active normative ExistsR formula",
    )

    for level, heading in (
        (4, "RT-07-MG — Multigeneal Reality Test"),
        (4, "RT-07-XP — Transversal Production Test"),
        (4, "RT-07-MG-TRIV — Singleton-per-token attack"),
    ):
        technical.section(level, heading)

    xp_bounds = technical.section_bounds(4, "RT-07-XP — Transversal Production Test")
    require_canonical_display_after(
        technical,
        xp_bounds,
        "puede ocurrir, porque ningún cierre local dispone de ambos antecedentes. Supongamos ahora explícitamente:",
        CANONICAL_XP_RGC_EXISTS,
        "RT-07-XP affirmative RGCExists premise",
    )
    require_canonical_display_after(
        technical,
        xp_bounds,
        "y fijemos un testigo $C_k$ tal que:",
        CANONICAL_XP_CLOSURE,
        "RT-07-XP explicit RegimeClosure witness",
    )
    require_canonical_display_after(
        technical,
        xp_bounds,
        "Por tanto:",
        CANONICAL_XP_STRICT_INCLUSION,
        "RT-07-XP strict transversal-growth conclusion",
    )

    presentation_bounds = technical.section_bounds(4, "8.5. ExistsR como metasentencia")
    require_canonical_display_after(
        technical,
        presentation_bounds,
        "y una presentación semántica produce únicamente:",
        CANONICAL_PRESENTATION,
        "REV-07f §8.5 presentation implication",
    )

    pure_relation_bounds = technical.section_bounds(
        4,
        "0.4.6. Stress test mixto: relación–genealogía–relación",
    )
    pure_relation_section = technical.semantic_text(*pure_relation_bounds)
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

    plural_route_bounds = technical.section_bounds(5, "Ruta plural")
    plural_route_section = technical.semantic_text(*plural_route_bounds)
    status_quotes = [
        text
        for text in technical.parsed_blockquote_texts(*plural_route_bounds)
        if text == PLURAL_STATUS_TEXT
    ]
    if len(status_quotes) != 1:
        fail(
            "REV-07f regression: plural-route status must appear exactly once as "
            "a parsed top-level blockquote with the canonical contract"
        )
    if re.search(r"REV-24d[^\n]{0,120}\bPARTIAL\b", plural_route_section):
        fail(
            "REV-07f regression: plural route again assigns PARTIAL status to REV-24d"
        )

    historical_bounds = technical.section_bounds(
        4,
        "0.11.3. HISTORICAL — dilema monogeneal pre-REV-07f",
    )
    historical_dilemma = technical.semantic_text(*historical_bounds)
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


def validate_normative_size(document: MarkdownDocument) -> None:
    line_count = len(document.lines)
    if line_count > MAX_NORMATIVE_LINES:
        fail(
            f"Normative proposal grew to {line_count} lines; limit is {MAX_NORMATIVE_LINES}. "
            "Move technical derivations to docs/proposals/work/."
        )

    section4_start, section4_end = document.section_bounds(
        2,
        "4. Núcleo formal vigente",
    )
    section4_lines = section4_end - section4_start
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

    archive_document.reject_inline_html(ARCHIVE)

    validate_ledger(documents[LEDGER])
    validate_archive(archive_document)

    history_start = documents[NORMATIVE].heading_start(
        1,
        "II. Historia cronológica de la propuesta",
    )
    current_normative = documents[NORMATIVE].semantic_text(0, history_start)
    validate_index_typing(current_normative)

    validate_regime_total_contract(
        documents[NORMATIVE],
        documents[LEDGER],
        documents[TECHNICAL],
    )
    validate_normative_size(documents[NORMATIVE])

    print("Proposal document validation passed")
    print(f"Normative lines: {len(normalize_source(contents[NORMATIVE]).split(chr(10)))}")
    print("CommonMark structure: parsed by markdown-it-py")
    print("Critical REV-07f TeX: canonical source contracts preserved")
    print("Ledger identifiers: unique")
    print("Critical REV-07f math: parser-classified canonical blocks")
    print("Historical archive: explicitly superseded")
    print("REV-07f RegimeTotal contract: preserved")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
