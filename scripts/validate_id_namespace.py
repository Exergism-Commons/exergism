#!/usr/bin/env python3
"""Validate the Exergism v0.2 identifier migration candidate.

This preserves the v0.1 corpus/model checks while validating the next generated
semantic projection under id.exergism.org. It does not modify historical v0.1
release artifacts.
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET

import generate_id_ontology
import generate_ontology
import validate_repository as legacy


VOCABULARY_NAMESPACE = generate_id_ontology.VOCABULARY_NAMESPACE
ONTOLOGY_IRI = generate_id_ontology.ONTOLOGY_IRI
HISTORICAL_NAMESPACE = "http://www.exergia.org/ns/"
EXPECTED_VERSION = "0.2.0"
EXPECTED_TAG = "v0.2.0"


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_manifest_v02() -> dict:
    manifest = json.loads((legacy.ROOT / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("manifest_version") != 2:
        fail("manifest_version must be 2")
    release = manifest.get("release") or {}
    if release.get("version") != EXPECTED_VERSION or release.get("tag") != EXPECTED_TAG:
        fail("unexpected v0.2 release identity")
    if release.get("status") != "candidate":
        fail("v0.2 migration must remain candidate until reviewed")

    identifiers = manifest.get("semantic_identifiers") or {}
    if identifiers.get("vocabulary_namespace") != VOCABULARY_NAMESPACE:
        fail("manifest vocabulary namespace mismatch")
    if identifiers.get("ontology_iri") != ONTOLOGY_IRI:
        fail("manifest ontology IRI mismatch")
    if identifiers.get("previous_vocabulary_namespace") != HISTORICAL_NAMESPACE:
        fail("historical namespace boundary missing")
    migration = identifiers.get("migration")
    if migration != "docs/id-namespace-migration-v0.2.md" or not (legacy.ROOT / migration).is_file():
        fail("namespace migration document missing")

    ordered = manifest["philosophical_corpus"]["order"]
    actual = sorted(path.name for path in legacy.CONTENT_DIR.glob("*.json"))
    if sorted(ordered) != actual:
        fail("manifest/content mismatch")
    for key in ("books", "formal_exergic_analysis", "derived_ontology", "symbol"):
        if not (legacy.ROOT / manifest[key]).exists():
            fail(f"manifest target does not exist: {manifest[key]}")
    return manifest


def validate_formal_variable_projection(root: ET.Element) -> None:
    rdf_about = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
    rdf_resource = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
    rdf_type = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type"
    owl_named_individual = "{http://www.w3.org/2002/07/owl#}NamedIndividual"

    expected_class = VOCABULARY_NAMESPACE + "ExergicVariable"
    individuals: dict[str, ET.Element] = {}
    for node in root.findall(owl_named_individual):
        iri = node.attrib.get(rdf_about)
        if iri:
            individuals[iri] = node

    for symbol in generate_id_ontology.FORMAL_VARIABLES:
        iri = VOCABULARY_NAMESPACE + symbol
        node = individuals.get(iri)
        if node is None:
            fail(f"formal variable IRI is absent from v0.2 ontology: {iri}")
        type_nodes = node.findall(rdf_type)
        if not any(child.attrib.get(rdf_resource) == expected_class for child in type_nodes):
            fail(f"formal variable {symbol} is not typed as ExergicVariable")

    for historical_local in ("P", "A", "V_ep", "L", "O", "U", "C", "S", "R", "Ecol"):
        historical_iri = "urn:ecl:" + historical_local
        if historical_iri in ET.tostring(root, encoding="unicode"):
            fail(f"Exergism ontology must never mint ECL variable identity {historical_iri}")


def legacy_iri_occurrences(root: ET.Element) -> list[str]:
    """Return precise RDF/XML locations that still carry the historical namespace."""
    occurrences: list[str] = []
    for element in root.iter():
        for attribute, value in element.attrib.items():
            if HISTORICAL_NAMESPACE in value:
                occurrences.append(f"{element.tag} {attribute}={value}")
        if element.text and HISTORICAL_NAMESPACE in element.text:
            occurrences.append(f"{element.tag} text={element.text.strip()}")
    return occurrences


def validate_migrated_ontology() -> None:
    checked_in = generate_ontology.ONTOLOGY_PATH.read_text(encoding="utf-8")
    try:
        root = ET.fromstring(checked_in)
    except ET.ParseError as exc:
        raise AssertionError(f"ontology.owl is not well-formed XML: {exc}") from exc

    expected = generate_id_ontology.render_migrated_projection()
    if checked_in != expected:
        fail("ontology.owl is stale; run python scripts/generate_id_ontology.py")
    if f'xml:base="{VOCABULARY_NAMESPACE}"' not in checked_in:
        fail("ontology vocabulary base is not the id.exergism.org namespace")
    if f'<owl:Ontology rdf:about="{ONTOLOGY_IRI}"/>' not in checked_in:
        fail("ontology document IRI is not canonical")

    legacy_occurrences = legacy_iri_occurrences(root)
    if legacy_occurrences:
        preview = "\n  - ".join(legacy_occurrences[:25])
        suffix = "" if len(legacy_occurrences) <= 25 else f"\n  ... and {len(legacy_occurrences) - 25} more"
        fail(
            "new ontology projection reintroduced the historical namespace at:\n"
            f"  - {preview}{suffix}"
        )

    for term in legacy.FORBIDDEN_ONTOLOGY_TERMS:
        if term in checked_in:
            fail(f"derived ontology contains downstream legal/governance term: {term}")

    validate_formal_variable_projection(root)


def main() -> None:
    legacy.validate_project_contract()
    manifest = validate_manifest_v02()
    legacy.validate_canonical_content()
    legacy.validate_books(legacy.ROOT / manifest["books"])
    legacy.validate_formal_model(legacy.ROOT / manifest["formal_exergic_analysis"])
    legacy.validate_examples()
    validate_migrated_ontology()
    print("Exergism v0.2 identifier migration validation passed")
    print(f"Vocabulary: {VOCABULARY_NAMESPACE}")
    print(f"Ontology: {ONTOLOGY_IRI}")
    print(f"Formal variables: {', '.join(generate_id_ontology.FORMAL_VARIABLES)}")


if __name__ == "__main__":
    main()
