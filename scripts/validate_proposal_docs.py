# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from pylatexenc.latex2text import LatexNodes2Text, MacroTextSpec, get_default_latex_context_db
from pylatexenc.latexwalker import (
    LatexEnvironmentNode,
    LatexGroupNode,
    LatexMacroNode,
    LatexMathNode,
    LatexWalker,
)

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
HIDDEN_BLOCK_BOUNDARY = "\u241e"
CONTEXT_INDEX_NAMES = frozenset({"i", "j", "k"})
INVISIBLE_TEX_MACROS = frozenset({"phantom", "hphantom", "vphantom"})
DYNAMIC_TEX_MACROS = frozenset(
    {
        "newcommand",
        "renewcommand",
        "providecommand",
        "def",
        "gdef",
        "edef",
        "xdef",
        "let",
        "futurelet",
        "csname",
        "endcsname",
        "expandafter",
        "DeclareMathOperator",
    }
)
FORBIDDEN_TEX_MACROS = INVISIBLE_TEX_MACROS | DYNAMIC_TEX_MACROS

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

CANONICAL_R_FORM = r"""\boxed{
\frac{
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\qquad
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)
}{
\vdash^{\mathsf M} R_i:\mathsf{OntScope}_i
}
\quad(\mathrm{R\text{-}FORM})
}"""

CANONICAL_CI_RT_BRIDGE = r"""\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\land
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)
\land
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{OntTotal}_i(R_i)
\land
\operatorname{ExistsR}.
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

CANONICAL_HISTORICAL_REGIME_TOTAL = r"""\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i),"""

PLURAL_STATUS_TEXT = (
    "Status contract: REV-24d = UNCHANGED; "
    "scope realization owner = REV-07/RegimeTotal; "
    "Actual/CoReal plural route = NON-DISCHARGING for RegimeGenerated*."
)

CANONICAL_ARCHIVE_BANNER = (
    "SUPERSEDED — archivo histórico, no normativo. "
    "Esta instantánea conserva deliberadamente formulaciones anteriores a REV-24 "
    "en las que máximos formales/semánticos fueron denominados $R_i$ "
    "(incluidos $R_i^{\\mathrm{proc}}$ y $R_i^A(t)$). "
    "Esas promociones están retiradas. "
    "La formulación vigente distingue $S_i$ como máximo semántico de $R_i$ "
    "como alcance ontológico y exige un puente independiente REV-24/$\\mathrm{OTB}_i$. "
    "Véase ../autodescripcion-realidad-distincion.md. "
    "No debe usarse este archivo para establecer el estado actual de la propuesta."
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


def visible_prose_text(token: Any) -> str:
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
        elif child.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
        elif child.type in transparent:
            continue
        else:
            # Math, images, HTML, and unknown inline nodes cannot satisfy prose-only
            # semantic guards. Preserve a nonzero boundary so adjacent prose never joins.
            parts.append(HIDDEN_BLOCK_BOUNDARY)

    return "".join(parts).strip()


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
        self.tokens = MARKDOWN.parse(self.text)

    def prose_text(self, start: int = 0, end: int | None = None) -> str:
        if end is None:
            end = len(self.lines)

        parts = [
            visible_prose_text(token)
            for token in self.tokens
            if token.type == "inline"
            and token.map is not None
            and start <= token.map[0]
            and token.map[1] <= end
        ]
        return "\n".join(part for part in parts if part)

    def math_fragments(self, start: int, end: int) -> list[tuple[int, str]]:
        fragments: list[tuple[int, str]] = []
        for token in self.tokens:
            if token.map is None or not (start <= token.map[0] and token.map[1] <= end):
                continue

            if token.type in {"math_block", "math_block_label"}:
                fragments.append((token.map[0] + 1, token.content))
                continue

            if token.type == "inline":
                for child in token.children or []:
                    if child.type in {"math_inline", "math_inline_double"}:
                        fragments.append((token.map[0] + 1, child.content))

        return fragments

    def inline_texts(self, start: int, end: int) -> list[str]:
        return [
            visible_inline_text(token)
            for token in self.tokens
            if token.type == "inline"
            and token.map is not None
            and start <= token.map[0]
            and token.map[1] <= end
        ]

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

    def reject_raw_html(self, path: Path) -> None:
        for token in self.tokens:
            if token.type == "html_block":
                location = ""
                if token.map is not None:
                    location = f" near line {token.map[0] + 1}"
                fail(
                    f"{path.relative_to(ROOT)} contains active raw HTML block{location}; "
                    "proposal contracts use CommonMark prose/blocks only"
                )

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
            and token.level == 0
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

    def root_blockquote_paragraph_texts(self, start: int, end: int) -> list[str]:
        results: list[str] = []
        for index in range(len(self.tokens) - 4):
            window = self.tokens[index : index + 5]
            if [token.type for token in window] != [
                "blockquote_open",
                "paragraph_open",
                "inline",
                "paragraph_close",
                "blockquote_close",
            ]:
                continue

            quote_open, paragraph_open, inline, _, quote_close = window
            if (
                quote_open.level != 0
                or quote_open.map is None
                or paragraph_open.level != 1
                or not (start <= quote_open.map[0] and quote_open.map[1] <= end)
            ):
                continue
            if quote_close.level != 0:
                continue

            results.append(visible_inline_text(inline))
        return results


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
    banners = document.root_blockquote_paragraph_texts(
        0,
        min(8, len(document.lines)),
    )
    if banners != [CANONICAL_ARCHIVE_BANNER]:
        fail(
            "Historical pre-consolidation archive must carry exactly the canonical "
            "parsed top-level SUPERSEDED/non-normative banner near the top"
        )


LATEX2TEXT_CONTEXT = get_default_latex_context_db()
LATEX2TEXT_CONTEXT.add_context_category(
    "proposal-semantic-aliases",
    prepend=True,
    macros=[
        MacroTextSpec("ne", simplify_repl="≠"),
        MacroTextSpec("neq", simplify_repl="≠"),
        MacroTextSpec("in", simplify_repl="∈"),
        MacroTextSpec("notin", simplify_repl="∉"),
    ],
)
LATEX_TO_TEXT = LatexNodes2Text(latex_context=LATEX2TEXT_CONTEXT)


def tex_nodes_text(nodes: list[Any]) -> str:
    rendered = LATEX_TO_TEXT.nodelist_to_text(nodes)
    return unicodedata.normalize("NFKC", rendered)


def bare_context_pattern(name: str) -> str:
    return rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])"


def rendered_quantifier_violation(rendered: str) -> str | None:
    indices = "|".join(
        re.escape(name)
        for name in sorted(CONTEXT_INDEX_NAMES, key=len, reverse=True)
    )
    pattern = re.compile(
        rf"(?P<quantifier>[∃∀∄])"
        rf"(?P<decoration>\s*(?:(?:!\s*)|(?:[\^_]\s*[^\s]+\s*))*)"
        rf"(?<![A-Za-z0-9_])(?P<index>{indices})(?![A-Za-z0-9_])"
    )

    for match in pattern.finditer(rendered):
        quantifier = match.group("quantifier")
        decoration = re.sub(r"\s+", "", match.group("decoration"))

        if quantifier in {"∃", "∀"} and decoration == "^M":
            continue

        if quantifier == "∀":
            return "object-level universal quantification over context metavariable"
        return "object-level existential quantification over context metavariable"

    return None


def rendered_relation_violation(rendered: str) -> str | None:
    for left in sorted(CONTEXT_INDEX_NAMES):
        left_pattern = bare_context_pattern(left)

        if re.search(
            rf"{left_pattern}\s*[∈∉]\s*(?<![A-Za-z0-9_])I(?![A-Za-z0-9_])",
            rendered,
        ):
            return "membership of context metavariable in an index domain I"

        for right in sorted(CONTEXT_INDEX_NAMES):
            if re.search(
                rf"{left_pattern}\s*≠\s*{bare_context_pattern(right)}",
                rendered,
            ):
                return "ordinary inequality relation between context metavariables"

    return None


def tex_child_nodelists(node: Any) -> list[list[Any]]:
    children: list[list[Any]] = []

    nodelist = getattr(node, "nodelist", None)
    if nodelist is not None:
        children.append(list(nodelist))

    nodeargd = getattr(node, "nodeargd", None)
    for argument in getattr(nodeargd, "argnlist", []) or []:
        if argument is None:
            continue
        argument_nodes = getattr(argument, "nodelist", None)
        if argument_nodes is not None:
            children.append(list(argument_nodes))

    return children


def find_forbidden_tex_macro(nodes: list[Any]) -> str | None:
    for node in nodes:
        if isinstance(node, LatexMacroNode) and node.macroname in FORBIDDEN_TEX_MACROS:
            return node.macroname

        for child_nodes in tex_child_nodelists(node):
            forbidden = find_forbidden_tex_macro(child_nodes)
            if forbidden is not None:
                return forbidden

    return None


def rendered_text_has_invalid_real_index(rendered: str) -> bool:
    allowed = "".join(sorted(CONTEXT_INDEX_NAMES))
    pattern = re.compile(
        rf"^_\s*([{re.escape(allowed)}])(?![A-Za-z0-9_])"
    )

    for match in re.finditer(r"(?<![A-Za-z0-9])Real(?![A-Za-z0-9])", rendered):
        suffix = rendered[match.end() :].lstrip()
        if pattern.match(suffix) is None:
            return True

    return False

def validate_index_typing(
    path: Path,
    document: MarkdownDocument,
    start: int,
    end: int,
) -> None:
    for line_number, fragment in document.math_fragments(start, end):
        try:
            nodes, _, _ = LatexWalker(fragment).get_latex_nodes()
        except Exception as exc:
            fail(
                f"{path.relative_to(ROOT)} contains TeX that pylatexenc cannot parse "
                f"near active line {line_number}: {exc}"
            )

        parsed_nodes = list(nodes)
        forbidden_macro = find_forbidden_tex_macro(parsed_nodes)
        if forbidden_macro is not None:
            fail(
                f"{path.relative_to(ROOT)} uses forbidden TeX macro \\{forbidden_macro} "
                f"near active line {line_number}; active proposal math must remain statically auditable"
            )

        rendered = tex_nodes_text(parsed_nodes)

        if rendered_text_has_invalid_real_index(rendered):
            fail(
                f"{path.relative_to(ROOT)} reintroduces Real with a missing or invalid context index "
                f"near active line {line_number}; allowed context metavariables are "
                f"{', '.join(sorted(CONTEXT_INDEX_NAMES))} (EXT-02)"
            )

        quantifier_violation = rendered_quantifier_violation(rendered)
        if quantifier_violation is not None:
            fail(
                f"{path.relative_to(ROOT)} reintroduces {quantifier_violation} "
                f"near active line {line_number}; indices are meta-level type parameters (EXT-02)"
            )

        relation_violation = rendered_relation_violation(rendered)
        if relation_violation is not None:
            fail(
                f"{path.relative_to(ROOT)} reintroduces {relation_violation} "
                f"near active line {line_number}; indices are meta-level type parameters (EXT-02)"
            )

def validate_regime_total_contract(
    normative: MarkdownDocument,
    technical: MarkdownDocument,
) -> None:
    individuation_bounds = normative.section_bounds(
        3,
        "1.3. El índice es un parámetro de tipo, no una entidad",
    )
    require_canonical_display_after(
        normative,
        individuation_bounds,
        "Puente de formación hacia R_i. IndexAdmission no crea una realidad ni demuestra su totalidad; solo licencia el sort contextual y la formación de un candidato de scope:",
        CANONICAL_R_FORM,
        "REV-07g R-FORM bridge",
    )

    totalization_bounds = normative.section_bounds(
        3,
        "1.6. $R_i$ — totalización genealógica mono- y multigeneal",
    )
    require_canonical_display_after(
        normative,
        totalization_bounds,
        r"Para una familia metateóricamente parametrizada $\mathfrak G_i$ de GeneUnit ya tipadas en el mismo contexto, §5.1 define GeneBasis, FamilyBase, RegimeClosure y:",
        CANONICAL_REGIME_GENERATED,
        "REV-07f RegimeGenerated* definition",
    )
    require_canonical_display_after(
        normative,
        totalization_bounds,
        "La totalización general es:",
        CANONICAL_REGIME_TOTAL,
        "REV-07f RegimeTotal definition",
    )

    genealogy_bounds = normative.section_bounds(
        3,
        "5.1. Criterio primario: origen unificado + generación independiente",
    )
    require_canonical_display_after(
        normative,
        genealogy_bounds,
        "Formalmente:",
        CANONICAL_GENE_FAMILY,
        "REV-07f GeneFamily definition",
    )
    require_canonical_display_after(
        normative,
        genealogy_bounds,
        "La closure del régimen no es esa unión. Debe volver a cerrar el mismo operador generativo para recoger producción transversal:",
        CANONICAL_REGIME_CLOSURE,
        "REV-07f RegimeClosure definition",
    )
    require_canonical_display_after(
        normative,
        genealogy_bounds,
        "Finalmente:",
        CANONICAL_GENE_BASIS,
        "REV-07f GeneBasis definition",
    )

    technical_genealogy_bounds = technical.section_bounds(
        3,
        "0.10a. REV-07f — RegimeTotal multigeneal",
    )
    require_canonical_display_after(
        technical,
        technical_genealogy_bounds,
        "Definimos GeneFamily:",
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
    require_canonical_display_after(
        normative,
        existsr_bounds,
        "Con la semántica anterior, el puente completo puede mostrarse sin colapsar sus etapas:",
        CANONICAL_CI_RT_BRIDGE,
        "REV-07g ContextIndividuation-RegimeTotal bridge",
    )

    for level, heading in (
        (4, "RT-07-MG — Multigeneal Reality Test"),
        (4, "RT-07-XP — Transversal Production Test"),
        (4, "RT-07-MG-TRIV — Singleton-per-token attack"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-c. RC-T1 — unresolved rival-cut theorem"),
        (4, "0.11.91r-d. No-Free-Promotion: el target es el witness, no prohibir contextos abundantes"),
        (4, "0.11.91r-g. NFP-T4 — contextual abundance theorem"),
        (4, "0.11.91r-h. RC-X — particiones cruzadas bajo simetría"),
        (4, "0.11.91r-j. Resultado doctrinal: unidad, escala y dimensión se desacoplan"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-k. Protocolo de robustez cross-domain"),
        (4, "0.11.91r-l. SW-A — software: servicio KV realizado frente a API puramente nominal"),
        (4, "0.11.91r-m. BIO-A — célula: boundary material + organización mantenida"),
        (4, "0.11.91r-n. PHY-A — termostato/control: el diagrama de bloques no es todavía ontología física"),
        (4, "0.11.91r-o. DR-T1 — resultado de portabilidad de criterio, no de identidad de mecanismo"),
        (4, "0.11.91r-p. Asimetría empírica entre dominios"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-q. Evidencia externa no es todavía ContextIndividuation"),
        (4, "0.11.91r-r. EMP-SW-REDIS — Redis Open Source como candidatura software concreta"),
        (4, "0.11.91r-s. EMP-BIO-ECOLI — E. coli como candidatura biológica concreta"),
        (4, "0.11.91r-t. EMP-PHY-NEST — Nest Thermostat + Heat Link como lazo físico concreto"),
        (4, "0.11.91r-u. EMP-T1 — qué ha sido realmente descargado"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-v. IA0 se descompone: realidad estructural no es todavía unidad contextual"),
        (4, "0.11.91r-w. UnitGroundAdequate — qué falta para IA0-U"),
        (4, "0.11.91r-x. Countermodels contra la promoción de estructura real a contexto"),
        (4, "0.11.91r-y. Resultado adversarial sobre RSP y epsilon-RSP"),
        (4, "0.11.91r-z. Consecuencia para Cellular Reality y XR-epsilon"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-aa. UGAudit — PASS, PARTIAL y FAIL son estados epistémicos de descarga"),
        (4, "0.11.91r-ab. UG-XR1 — auditoría del witness ejecutable"),
        (4, "0.11.91r-ac. UG-REDIS — proceso/estado/protocolo como ground candidato"),
        (4, "0.11.91r-ad. UG-ECOLI — organización mantenida como ground candidato"),
        (4, "0.11.91r-ae. UG-NEST — closed-loop control como ground candidato"),
        (4, "0.11.91r-af. UG-COMP — comparación sin ranking ontológico"),
        (4, "0.11.91r-ag. UG-T1 — ninguna descarga completa todavía"),
    ):
        technical.section_bounds(level, heading)

    for level, heading in (
        (4, "0.11.91r-ah. UnitProfileBreak — sensibilidad constitutiva sin presuponer reindividuación"),
        (4, "0.11.91r-ai. CIT — Constitutive Intervention Test"),
        (4, "0.11.91r-aj. CIT-XR1 — XR-1 sí descarga UG4"),
        (4, "0.11.91r-am. XR1FiniteRivalClass — clase adversarial pre-indexada"),
        (4, "0.11.91r-an. XR1-RC-T1 — cierre exhaustivo dentro de la clase finita"),
        (4, "0.11.91r-ao. RivalClassCompleteness — lo que falta para convertir FR1–FR4 en UG6 completo"),
        (4, "0.11.91r-ap. DTS-UG6 finding — un DTS desnudo no demuestra RivalClassCompleteness"),
    ):
        technical.section_bounds(level, heading)

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
    pure_relation_section = technical.prose_text(*pure_relation_bounds)
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
    status_quotes = [
        text
        for text in technical.root_blockquote_paragraph_texts(*plural_route_bounds)
        if text == PLURAL_STATUS_TEXT
    ]
    if len(status_quotes) != 1:
        fail(
            "REV-07f regression: plural-route status must appear exactly once as "
            "a parsed top-level blockquote with the canonical contract"
        )
    if any(
        "REV-24d" in paragraph and "PARTIAL" in paragraph
        for paragraph in technical.inline_texts(*plural_route_bounds)
    ):
        fail(
            "REV-07f regression: plural route again assigns PARTIAL status to REV-24d"
        )

    historical_bounds = technical.section_bounds(
        4,
        "0.11.3. HISTORICAL — dilema monogeneal pre-REV-07f",
    )
    require_canonical_display_after(
        technical,
        historical_bounds,
        "REV-07f retira la inferencia de que esto obliga a buscar un único origen común. En la arquitectura vigente, si ambas genealogías ya están justificadamente tipadas en el mismo SharedOntSpace, pueden formar una GeneFamily y la totalidad se expresa mediante:",
        CANONICAL_HISTORICAL_REGIME_TOTAL,
        "REV-07f historical current RegimeTotal architecture",
    )
    historical_dilemma = technical.prose_text(*historical_bounds)
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
        document.reject_raw_html(path)

    archive_document.reject_raw_html(ARCHIVE)

    validate_ledger(documents[LEDGER])
    validate_archive(archive_document)

    history_start = documents[NORMATIVE].heading_start(
        1,
        "II. Historia cronológica de la propuesta",
    )
    validate_index_typing(
        NORMATIVE,
        documents[NORMATIVE],
        0,
        history_start,
    )

    validate_regime_total_contract(
        documents[NORMATIVE],
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
