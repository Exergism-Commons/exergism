# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import unittest

from pylatexenc.latexwalker import LatexWalker

from scripts.validate_proposal_docs import (
    CONTEXT_INDEX_NAMES,
    MarkdownDocument,
    NORMATIVE,
    tex_nodes_text,
    validate_archive,
    validate_index_typing,
)


class PylatexencShapeDiagnostics(unittest.TestCase):
    def test_shapes(self) -> None:
        payload = []
        for tex in (
            r"\exists^{X} i\;P_i",
            r"\forall_{q} i\;P_i",
            r"i\ne j",
        ):
            nodes, _, _ = LatexWalker(tex).get_latex_nodes()
            payload.append(
                {
                    "tex": tex,
                    "nodes": repr(nodes),
                    "rendered": tex_nodes_text(list(nodes)),
                }
            )
        self.fail(repr(payload))


class IndexTypingGuardTests(unittest.TestCase):
    def assert_rejected(self, tex: str) -> None:
        document = MarkdownDocument(f"$" + tex + "$")
        with self.assertRaises(AssertionError):
            validate_index_typing(NORMATIVE, document, 0, len(document.lines))

    def assert_allowed(self, tex: str) -> None:
        document = MarkdownDocument(f"$" + tex + "$")
        validate_index_typing(NORMATIVE, document, 0, len(document.lines))

    def test_rejects_bare_index_quantifier_spellings(self) -> None:
        for tex in (
            r"\exists i\;P_i",
            r"\exists\,i\;P_i",
            r"\exists\ i\;P_i",
            r"\exists{\,i}\;P_i",
            r"\forall\quad i\;P_i",
            r"\exists\mathrm{i}\;P_i",
            r"\forall\mathbf{i}\;P_i",
            r"{\exists} i\;P_i",
            r"{{\forall}} i\;P_i",
            r"\mathop{\exists} i\;P_i",
            r"\mathop{\forall} i\;P_i",
            r"\exists! i\;P_i",
            r"\nexists i\;P_i",
            r"\exists^{X} i\;P_i",
            r"\forall_{q} i\;P_i",
        ):
            with self.subTest(tex=tex):
                self.assert_rejected(tex)

    def test_rejects_every_declared_context_index_as_object_quantifier(self) -> None:
        for name in sorted(CONTEXT_INDEX_NAMES):
            for tex in (
                rf"\exists {name}\;P_{name}",
                rf"\forall {name}\;P_{name}",
                rf"\exists\mathrm{{{name}}}\;P_{name}",
                rf"{{\forall}} {name}\;P_{name}",
            ):
                with self.subTest(name=name, tex=tex):
                    self.assert_rejected(tex)

    def test_allows_metalinguistic_and_indexed_object_quantifiers(self) -> None:
        for tex in (
            r"\exists^{\mathsf M} i",
            r"\exists x_i\;P(x_i)",
            r"\forall x_i\;P(x_i)",
        ):
            with self.subTest(tex=tex):
                self.assert_allowed(tex)

    def test_rejects_other_ext02_notation(self) -> None:
        for tex in (
            r"i\,\neq\,j",
            r"j\neq i",
            r"i\in I",
            r"\mathrm{i}\neq\mathrm{j}",
            r"\mathit{i}\in\mathrm{I}",
            r"i{\neq}j",
            r"i{\in}I",
            r"i\mathrel{\neq}j",
            r"i\mathrel{\in}I",
            r"i\ne j",
            r"\operatorname{Real}(x)",
            r"\operatorname{Real}_x(x)",
            r"\operatorname{Real}_{\phantom{i}}(x)",
            r"\operatorname{Real}_{\hphantom{i}}(x)",
            r"\operatorname{Real}_{}(x)",
        ):
            with self.subTest(tex=tex):
                self.assert_rejected(tex)

    def test_rejects_relations_for_every_declared_context_index(self) -> None:
        names = sorted(CONTEXT_INDEX_NAMES)
        for left in names:
            self.assert_rejected(rf"{left}\in I")
            for right in names:
                if left == right:
                    continue
                with self.subTest(left=left, right=right):
                    self.assert_rejected(rf"{left}\neq {right}")

    def test_allows_indexed_real(self) -> None:
        for tex in (
            r"\operatorname{Real}_i(x_i)",
            r"\operatorname{Real}_j(x_i)",
            r"\operatorname{Real}_k(x_i)",
            r"\operatorname{Real}_{\mathrm{i}}(x_i)",
        ):
            with self.subTest(tex=tex):
                self.assert_allowed(tex)


class ProseProjectionTests(unittest.TestCase):
    def test_inline_math_cannot_satisfy_prose_terms(self) -> None:
        document = MarkdownDocument(
            "visible $\\phantom{SharedOntSpace GeneFamily/GeneBasis RegimeClosure RegimeTotal}$ prose"
        )
        projected = document.prose_text(0, len(document.lines))
        for term in ("SharedOntSpace", "GeneFamily/GeneBasis", "RegimeClosure", "RegimeTotal"):
            with self.subTest(term=term):
                self.assertNotIn(term, projected)

    def test_visible_prose_terms_are_preserved(self) -> None:
        document = MarkdownDocument(
            "SharedOntSpace GeneFamily/GeneBasis RegimeClosure RegimeTotal"
        )
        projected = document.prose_text(0, len(document.lines))
        for term in ("SharedOntSpace", "GeneFamily/GeneBasis", "RegimeClosure", "RegimeTotal"):
            with self.subTest(term=term):
                self.assertIn(term, projected)


class ArchiveContractTests(unittest.TestCase):
    def test_keywords_without_canonical_polarity_do_not_satisfy_banner(self) -> None:
        document = MarkdownDocument(
            "> This archive is NOT SUPERSEDED and is not actually no normativo.\n"
        )
        with self.assertRaises(AssertionError):
            validate_archive(document)


class RawHtmlGuardTests(unittest.TestCase):
    def test_rejects_html_block(self) -> None:
        document = MarkdownDocument("<p>REV-24d = PARTIAL</p>\n")
        with self.assertRaises(AssertionError):
            document.reject_raw_html(NORMATIVE)

    def test_rejects_inline_html(self) -> None:
        document = MarkdownDocument("visible <!-- hidden doctrine --> text")
        with self.assertRaises(AssertionError):
            document.reject_raw_html(NORMATIVE)

    def test_allows_plain_markdown(self) -> None:
        document = MarkdownDocument("plain **CommonMark** text")
        document.reject_raw_html(NORMATIVE)


if __name__ == "__main__":
    unittest.main()
