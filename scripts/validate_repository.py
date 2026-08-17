# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from generate_ontology import (
    CANONICAL_SCHEMA_PATH,
    CONTENT_DIR,
    ONTOLOGY_PATH,
    CanonicalSchemaValidator,
    OntologyBuilder,
)

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_VARIABLES = {"P", "A", "V_ep", "L", "O", "U", "C", "S", "R", "Ecol"}
REQUIRED_FORMULA_SYMBOLS = {"Ex_b", "Ex_r", "E_i", "X_h", "B_0", "P_atr", "E_i_adj"}
REQUIRED_TEMPORAL_SYMBOLS = {"B_acc", "D_acc", "N_t"}
REQUIRED_PROJECT_FILES = {
    "LICENSE.md",
    "LICENSES/CC-BY-SA-4.0.txt",
    "LICENSES/Apache-2.0.txt",
    "NOTICE",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "docs/canonical-boundaries.md",
    "docs/release-process.md",
    "formal/FORMAL-MODEL-STATUS.md",
    "reviews/2026-08-17-v0.1.0-adversarial-review.md",
}

FORBIDDEN_ONTOLOGY_TERMS = {
    "RestrictedParty",
    "GovernanceDecision",
    "ECLCriterion",
    "ScheduleEntry",
}

EXPECTED_BOOKS = {
    1: ("Carcel del Mundo", "World Jail"),
    2: ("Luz Condenada", "Doomed Light"),
    3: ("Romper el Ciclo", "Break the Cycle"),
    4: ("Razon Exergica", "Exergic Reason"),
}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise AssertionError(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc


def validate_project_contract() -> None:
    for relative in sorted(REQUIRED_PROJECT_FILES):
        if not (ROOT / relative).is_file():
            fail(f"Required project contract file missing: {relative}")

    licensing = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    for marker in ("CC BY-SA 4.0", "Apache-2.0", "No ECL inheritance"):
        if marker not in licensing:
            fail(f"LICENSE.md missing required boundary marker: {marker}")


def validate_manifest() -> dict:
    manifest = load_json(ROOT / "manifest.json")
    if manifest.get("manifest_version") != 2:
        fail("manifest_version must be 2")
    if manifest.get("name") != "Metafisica emergentista de la liberacion":
        fail("Unexpected canonical system name")
    release = manifest.get("release")
    if not isinstance(release, dict):
        fail("manifest.release must be an object")
    if release.get("version") != "0.1.0" or release.get("tag") != "v0.1.0":
        fail("Unexpected v0.1.0 release identity")
    if release.get("status") not in {"candidate", "ready"}:
        fail("release.status must be candidate or ready")

    ordered = manifest["philosophical_corpus"]["order"]
    actual = sorted(path.name for path in CONTENT_DIR.glob("*.json"))
    if sorted(ordered) != actual:
        fail(f"Manifest/content mismatch: ordered={sorted(ordered)!r}, actual={actual!r}")

    for key in ("books", "formal_exergic_analysis", "derived_ontology", "symbol"):
        target = ROOT / manifest[key]
        if not target.exists():
            fail(f"Manifest target does not exist: {manifest[key]}")

    for directory in manifest.get("examples", []):
        target = ROOT / directory
        if not target.is_dir() or not any(target.iterdir()):
            fail(f"Example directory missing or empty: {directory}")
    return manifest


def validate_canonical_content() -> None:
    validator = CanonicalSchemaValidator(CANONICAL_SCHEMA_PATH)
    seen_domain_ids: set[str] = set()
    seen_node_ids: set[str] = set()
    canonical_ids: set[str] = set()
    concept_refs: list[tuple[str, str]] = []
    source_paths: dict[str, set[str]] = {}

    def walk(node: dict, source_name: str) -> None:
        node_id = node["id"]
        if node_id in seen_node_ids:
            fail(f"Duplicate node id: {node_id}")
        seen_node_ids.add(node_id)
        source_path = node["source_path"]
        paths_for_source = source_paths.setdefault(source_name, set())
        if source_path in paths_for_source:
            fail(f"Duplicate source_path in {source_name}: {source_path}")
        paths_for_source.add(source_path)
        if "canonical_id" in node:
            canonical_id = node["canonical_id"]
            if canonical_id in canonical_ids:
                fail(f"Duplicate canonical_id: {canonical_id}")
            canonical_ids.add(canonical_id)
        if "concept_ref" in node:
            concept_refs.append((node["concept_ref"], f"{source_name}:{node['source_path']}"))
        for child in node.get("children", []):
            walk(child, source_name)

    for path in sorted(CONTENT_DIR.glob("*.json")):
        payload = load_json(path)
        validator.validate_payload(payload, path.name)
        domain_id = payload["domain"]["id"]
        if domain_id in seen_domain_ids:
            fail(f"Duplicate domain id: {domain_id}")
        seen_domain_ids.add(domain_id)
        if payload["domain"]["source_file"] != path.name:
            fail(f"domain.source_file mismatch in {path.name}")
        walk(payload["root"], path.name)

    unresolved = [(ref, source) for ref, source in concept_refs if ref not in canonical_ids]
    if unresolved:
        fail(f"Unresolved concept_ref entries: {unresolved[:5]}")


def validate_books(path: Path) -> None:
    payload = load_json(path)
    if not isinstance(payload.get("serie"), dict):
        fail("books/libros.json must contain serie")
    books = payload.get("libros")
    if not isinstance(books, list) or len(books) != 4:
        fail("books/libros.json must define exactly four books")
    by_number = {book.get("numero"): book for book in books}
    if set(by_number) != set(EXPECTED_BOOKS):
        fail("Book numbering must be exactly 1..4")
    for number, (es, en) in EXPECTED_BOOKS.items():
        book = by_number[number]
        if book.get("titulo_es") != es or book.get("titulo_en") != en:
            fail(f"Unexpected title for book {number}")


def validate_formal_model(path: Path) -> None:
    payload = load_json(path)
    model = payload.get("sistema_matematico_exergico")
    if not isinstance(model, dict):
        fail("formal model must contain sistema_matematico_exergico")

    variables = model.get("variables_principales")
    if not isinstance(variables, dict):
        fail("formal model lacks variables_principales")
    missing_variables = REQUIRED_VARIABLES - set(variables)
    if missing_variables:
        fail(f"formal model missing variables: {sorted(missing_variables)}")

    formulas = model.get("formulas_principales")
    if not isinstance(formulas, dict):
        fail("formal model lacks formulas_principales")
    symbols = {entry.get("simbolo") for entry in formulas.values() if isinstance(entry, dict)}
    missing_symbols = REQUIRED_FORMULA_SYMBOLS - symbols
    if missing_symbols:
        fail(f"formal model missing formula symbols: {sorted(missing_symbols)}")

    contextual = model.get("modulacion_por_contexto")
    if not isinstance(contextual, dict):
        fail("formal model lacks modulacion_por_contexto")
    transition_weights = contextual.get("transicion", {}).get("pesos", {})
    if not isinstance(transition_weights, dict):
        fail("formal model lacks recovered transition weights")
    recovered_a_sum = sum(float(transition_weights[f"a{i}"]) for i in range(1, 6))
    if abs(recovered_a_sum - 0.90) > 1e-12:
        fail("Recovered transition a1..a5 weights changed; resolve doctrinally before altering the v0.1.0 baseline")

    formal_status = (ROOT / "formal/FORMAL-MODEL-STATUS.md").read_text(encoding="utf-8")
    for marker in ("0.90", "`z1`", "`z2`", "MUST NOT"):
        if marker not in formal_status:
            fail(f"Formal-model status does not expose known ambiguity: {marker}")

    macro = model.get("composicion_jerarquica_de_eventos", {}).get("agregacion_por_fase_y_macroevento", {})
    macro_formulas = "\n".join(
        value.get("formula", "") for value in macro.values() if isinstance(value, dict)
    )
    for symbol in ("z1", "z2"):
        if symbol not in macro_formulas:
            fail(f"Expected recovered open macroevent parameter missing: {symbol}")

    temporal = model.get("integracion_temporal")
    if not isinstance(temporal, dict) or not isinstance(temporal.get("formulas_temporales"), dict):
        fail("formal model lacks temporal integration formulas")
    temporal_symbols = {
        entry.get("simbolo")
        for entry in temporal["formulas_temporales"].values()
        if isinstance(entry, dict)
    }
    missing_temporal = REQUIRED_TEMPORAL_SYMBOLS - temporal_symbols
    if missing_temporal:
        fail(f"formal model missing temporal symbols: {sorted(missing_temporal)}")


def validate_examples() -> None:
    iran = ROOT / "examples/exergic-analysis/iran"
    kabul = ROOT / "examples/exergic-analysis/toma-de-kabul"
    if len(list(iran.glob("*.csv"))) < 3 or len(list(iran.glob("*.png"))) < 1:
        fail("Iran example is incomplete")
    if len(list(kabul.glob("*.png"))) < 1:
        fail("Toma de Kabul example is incomplete")


def validate_ontology_reproducibility() -> None:
    try:
        ET.parse(ONTOLOGY_PATH)
    except ET.ParseError as exc:
        raise AssertionError(f"ontology.owl is not well-formed XML: {exc}") from exc

    builder = OntologyBuilder()
    builder.build()
    rendered = builder.render()
    checked_in = ONTOLOGY_PATH.read_text(encoding="utf-8")
    if rendered != checked_in:
        fail("ontology.owl is stale; run python scripts/generate_ontology.py")
    for term in FORBIDDEN_ONTOLOGY_TERMS:
        if term in checked_in:
            fail(f"Derived ontology contains downstream legal/governance term: {term}")


def main() -> None:
    validate_project_contract()
    manifest = validate_manifest()
    validate_canonical_content()
    validate_books(ROOT / manifest["books"])
    validate_formal_model(ROOT / manifest["formal_exergic_analysis"])
    validate_examples()
    validate_ontology_reproducibility()
    print("Repository validation passed")
    print(f"Canonical philosophical domains: {len(list(CONTENT_DIR.glob('*.json')))}")
    print("Books: 4")
    print(f"Required exergic variables present: {', '.join(sorted(REQUIRED_VARIABLES))}")
    print("ontology.owl: valid and reproducible")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
