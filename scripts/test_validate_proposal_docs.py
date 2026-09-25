# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import unittest

from scripts.validate_proposal_docs import (
    CANONICAL_CI_RT_BRIDGE,
    CANONICAL_R_FORM,
    CONTEXT_INDEX_NAMES,
    MarkdownDocument,
    NORMATIVE,
    TECHNICAL,
    validate_archive,
    validate_architecture_archaeology,
    validate_current_theory_invariants,
    validate_index_typing,
    validate_regime_total_contract,
)


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
            r"\exists^X i\;P_i",
            r"\forall_q i\;P_i",
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
            r"\exists^{\mathsf M} j",
            r"\forall^{\mathsf M} k",
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
            r"i\mathrel{\ne}j",
            r"i\notin I",
            r"i≠j",
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
            self.assert_rejected(rf"{left}\notin I")
            for right in names:
                with self.subTest(left=left, right=right):
                    self.assert_rejected(rf"{left}\neq {right}")
                    self.assert_rejected(rf"{left}\ne {right}")

    def test_rejects_dynamic_tex_definitions(self) -> None:
        for tex in (
            r"\newcommand{\Q}{\exists}\Q i",
            r"\def\Q{\exists}\Q i",
            r"\let\Q\exists\Q i",
            r"\csname exists\endcsname i",
        ):
            with self.subTest(tex=tex):
                self.assert_rejected(tex)

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


class ContextRealityContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.normative_source = NORMATIVE.read_text(encoding="utf-8")
        self.normative = MarkdownDocument(self.normative_source)
        self.technical_source = TECHNICAL.read_text(encoding="utf-8")
        self.technical = MarkdownDocument(self.technical_source)

    def assert_contract_rejected(self, source: str) -> None:
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                MarkdownDocument(source),
                self.technical,
            )

    def test_rejects_missing_r_form_bridge(self) -> None:
        mutated = self.normative_source.replace(
            CANONICAL_R_FORM,
            r"\boxed{\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)}",
            1,
        )
        self.assert_contract_rejected(mutated)

    def test_rejects_missing_ci_rt_bridge(self) -> None:
        mutated = self.normative_source.replace(
            CANONICAL_CI_RT_BRIDGE,
            r"\boxed{\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)}",
            1,
        )
        self.assert_contract_rejected(mutated)

    def test_rejects_missing_rival_cut_contract(self) -> None:
        heading = "#### 0.11.91r-c. RC-T1 — unresolved rival-cut theorem"
        mutated = self.technical_source.replace(
            heading,
            "#### removed rival-cut theorem",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_no_free_promotion_contract(self) -> None:
        heading = (
            "#### 0.11.91r-d. No-Free-Promotion: el target es el witness, "
            "no prohibir contextos abundantes"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed no-free-promotion contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_cross_domain_portability_contract(self) -> None:
        heading = (
            "#### 0.11.91r-o. DR-T1 — resultado de portabilidad de criterio, "
            "no de identidad de mecanismo"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed cross-domain portability contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_empirical_non_promotion_contract(self) -> None:
        heading = "#### 0.11.91r-u. EMP-T1 — qué ha sido realmente descargado"
        mutated = self.technical_source.replace(
            heading,
            "#### removed empirical non-promotion contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_unit_ground_contract(self) -> None:
        heading = "#### 0.11.91r-w. UnitGroundAdequate — qué falta para IA0-U"
        mutated = self.technical_source.replace(
            heading,
            "#### removed unit-ground contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_ia0_adversarial_result(self) -> None:
        heading = "#### 0.11.91r-y. Resultado adversarial sobre RSP y epsilon-RSP"
        mutated = self.technical_source.replace(
            heading,
            "#### removed IA0 adversarial result",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_unit_ground_cross_case_audit(self) -> None:
        heading = "#### 0.11.91r-af. UG-COMP — comparación sin ranking ontológico"
        mutated = self.technical_source.replace(
            heading,
            "#### removed unit-ground cross-case audit",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_constitutive_intervention_contract(self) -> None:
        heading = "#### 0.11.91r-ai. CIT — Constitutive Intervention Test"
        mutated = self.technical_source.replace(
            heading,
            "#### removed constitutive intervention contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_rival_class_completeness_finding(self) -> None:
        heading = (
            "#### 0.11.91r-ap. DTS-UG6 finding — un DTS desnudo "
            "no demuestra RivalClassCompleteness"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed rival-class completeness finding",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_xr2_open_component_result(self) -> None:
        heading = "#### 0.11.91r-aw. XR2-E — ejecución efectiva del componente abierto"
        mutated = self.technical_source.replace(
            heading,
            "#### removed XR-2 open-component result",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_realization_envelope_contract(self) -> None:
        heading = "#### 0.11.91r-ba. UG5 no exige aislamiento físico absoluto: RealizationEnvelope"
        mutated = self.technical_source.replace(
            heading,
            "#### removed realization envelope",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_realizer_coverage_contract(self) -> None:
        heading = "#### 0.11.91r-bj. RCAAudit — vista derivada, no nuevo criterio"
        mutated = self.technical_source.replace(
            heading,
            "#### removed realizer coverage contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_finite_test_countermodel(self) -> None:
        heading = (
            "#### 0.11.91r-bn. RCA-X1 — límite de baterías finitas "
            "dentro de un contrato"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed finite-test countermodel",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_host_projection_contract(self) -> None:
        heading = (
            "#### 0.11.91r-bo. RCA-T1 — SUPERSEDED como teoría "
            "host autónoma"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed host projection contract",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_xr2_host_attack_result(self) -> None:
        heading = "#### 0.11.91r-bu. HOST-T1 — resultado adversarial reinterpretado"
        mutated = self.technical_source.replace(
            heading,
            "#### removed XR-2 host attack result",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_hmp_projection_result(self) -> None:
        heading = (
            "#### 0.11.91r-bw. HMP-T1 — completitud de clasificación "
            "sobre la gramática diagnóstica"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed HMP projection result",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )


    def test_rejects_missing_superseded_host_x1_correction(self) -> None:
        heading = (
            "#### 0.11.91r-by. HOST-X1 — SUPERSEDED: mecanismo omitido "
            "no implica constituyente omitido"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed superseded HOST-X1 correction",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_hta_redundancy_correction(self) -> None:
        heading = (
            "#### 0.11.91r-ca. HTA-X1 — REDUNDANT con RCA-X1; "
            "no crea un nuevo blocker"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed HTA redundancy correction",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )

    def test_rejects_missing_parallel_host_contract_rejection(self) -> None:
        heading = (
            "#### 0.11.91r-cb. HTA-K — SUPERSEDED: "
            "no crear un contrato host paralelo"
        )
        mutated = self.technical_source.replace(
            heading,
            "#### removed parallel host contract rejection",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_regime_total_contract(
                self.normative,
                MarkdownDocument(mutated),
            )
class CurrentTheoryInvariantTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = TECHNICAL.read_text(encoding="utf-8")

    def test_current_technical_architecture_passes(self) -> None:
        validate_current_theory_invariants(MarkdownDocument(self.source))

    def test_rejects_witness_as_context_individuation_argument(self) -> None:
        mutated = self.source + (
            "\\n\\n$\\operatorname{ContextIndividuation}^{\\mathsf M}"
            "(C;\\chi)$\\n"
        )
        with self.assertRaises(AssertionError):
            validate_current_theory_invariants(MarkdownDocument(mutated))

    def test_rejects_old_mcadequate_bundle(self) -> None:
        mutated = self.source + (
            "\\ncomo MC1–MC10 más los CI1–CI14/IA0–IA10 aplicables.\\n"
        )
        with self.assertRaises(AssertionError):
            validate_current_theory_invariants(MarkdownDocument(mutated))


class ArchitectureArchaeologyTests(unittest.TestCase):
    def setUp(self) -> None:
        from scripts.validate_proposal_docs import ARCHAEOLOGY
        self.source = ARCHAEOLOGY.read_text(encoding="utf-8")

    def test_current_architecture_map_passes(self) -> None:
        validate_architecture_archaeology(MarkdownDocument(self.source))

    def test_rejects_bake_to_continuation_regression(self) -> None:
        mutated = self.source.replace(
            "ContinuationProfile no se deriva de Bake",
            "ContinuationProfile se deriva de Bake",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_architecture_archaeology(MarkdownDocument(mutated))

    def test_rejects_embedding_generation_regression(self) -> None:
        mutated = self.source.replace(
            "ContextEmbedding por sí solo no crea CtxParent ni aumenta generación.",
            "ContextEmbedding puede aumentar generación.",
            1,
        )
        with self.assertRaises(AssertionError):
            validate_architecture_archaeology(MarkdownDocument(mutated))


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
