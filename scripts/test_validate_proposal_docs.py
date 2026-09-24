# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import unittest

from scripts.validate_proposal_docs import MarkdownDocument, validate_index_typing


class IndexTypingGuardTests(unittest.TestCase):
    def assert_rejected(self, tex: str) -> None:
        document = MarkdownDocument(f"$" + tex + "$")
        with self.assertRaises(AssertionError):
            validate_index_typing(document, 0, len(document.lines))

    def assert_allowed(self, tex: str) -> None:
        document = MarkdownDocument(f"$" + tex + "$")
        validate_index_typing(document, 0, len(document.lines))

    def test_rejects_bare_index_quantifier_spellings(self) -> None:
        for tex in (
            r"\exists i\;P_i",
            r"\exists\,i\;P_i",
            r"\exists\ i\;P_i",
            r"\exists{\,i}\;P_i",
            r"\forall\quad i\;P_i",
        ):
            with self.subTest(tex=tex):
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
            r"\operatorname{Real}(x)",
        ):
            with self.subTest(tex=tex):
                self.assert_rejected(tex)

    def test_allows_indexed_real(self) -> None:
        self.assert_allowed(r"\operatorname{Real}_i(x_i)")


if __name__ == "__main__":
    unittest.main()
