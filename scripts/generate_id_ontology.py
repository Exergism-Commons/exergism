#!/usr/bin/env python3
"""Generate the next Exergism ontology projection under id.exergism.org.

This entrypoint deliberately leaves the historical generator implementation and
released artifacts untouched. It reuses the canonical generator with the
vocabulary namespace selected for the next canonical Exergism release, then
sets the ontology document IRI independently from the term namespace.
"""

from __future__ import annotations

import generate_ontology


VOCABULARY_NAMESPACE = "https://id.exergism.org/exergism#"
ONTOLOGY_IRI = "https://id.exergism.org/ontology/exergism"


def main() -> None:
    generate_ontology.BASE_IRI = VOCABULARY_NAMESPACE
    generate_ontology.main()

    path = generate_ontology.ONTOLOGY_PATH
    text = path.read_text(encoding="utf-8")
    old = f'<owl:Ontology rdf:about="{VOCABULARY_NAMESPACE}"/>'
    new = f'<owl:Ontology rdf:about="{ONTOLOGY_IRI}"/>'
    if text.count(old) != 1:
        raise SystemExit(
            "id namespace migration failure: expected exactly one generated ontology declaration"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


if __name__ == "__main__":
    main()
