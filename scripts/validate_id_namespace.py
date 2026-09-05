#!/usr/bin/env python3
"""Validate the Exergism v0.2 identifier migration candidate.

This preserves the v0.1 corpus/model checks while validating the next generated
semantic projection under id.exergism.org. It does not modify historical v0.1
release artifacts.
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET

import generate_ontology
import validate_repository as legacy


VOCABULARY_NAMESPACE = "https://id.exergism.org/exergism#"
ONTOLOGY_IRI = "https://id.exergism.org/ontology/exergism"
EXPECTED_VERSION = "0.2.0"
EXPECTED_TAG = "v0.2.0"


def fail(message: str) -> None:
    raise AssertionError(message)


def migrated_render() -> str:
    generate_ontology.BASE_IRI = VOCABULARY_NAMESPACE
    builder = generate_ontology.OntologyBuilder()
    builder.build()
    text = builder.render()
    old = f'<owl:Ontology rdf:about="{VOCABULARY_NAMESPACE}"/>'
    new = f'<owl:Ontology rdf:about="{ONTOLOGY_IRI}"/>'
    if text.count(old) != 1:
        fail("expected exactly one generated ontology declaration")
    return text.replace(old, new, 1)


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
    if identifiers.get("previous_vocabulary_namespace") != "http://www.exergia.org/ns/":
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


def validate_migrated_ontology() -> None:
    checked_in = generate_ontology.ONTOLOGY_PATH.read_text(encoding="utf-8")
    try:
        ET.fromstring(checked_in)
    except ET.ParseError as exc:
        raise AssertionError(f"ontology.owl is not well-formed XML: {exc}") from exc

    expected = migrated_render()
    if checked_in != expected:
        fail("ontology.owl is stale; run python scripts/generate_id_ontology.py")
    if f'xml:base="{VOCABULARY_NAMESPACE}"' not in checked_in:
        fail("ontology vocabulary base is not the id.exergism.org namespace")
    if f'<owl:Ontology rdf:about="{ONTOLOGY_IRI}"/>' not in checked_in:
        fail("ontology document IRI is not canonical")
    if "http://www.exergia.org/ns/" in checked_in:
        fail("new ontology projection reintroduced the historical namespace")
    for term in legacy.FORBIDDEN_ONTOLOGY_TERMS:
        if term in checked_in:
            fail(f"derived ontology contains downstream legal/governance term: {term}")


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


if __name__ == "__main__":
    main()
