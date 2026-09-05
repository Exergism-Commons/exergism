#!/usr/bin/env python3
"""Generate the next Exergism ontology projection under id.exergism.org.

This entrypoint deliberately leaves the historical generator implementation and
released artifacts untouched. It reuses the canonical corpus generator, selects
the vocabulary namespace for the next canonical Exergism release, gives the
ontology document its own IRI, and projects the canonical formal variables from
`formal/sistema_analitico_exergico.json`.
"""

from __future__ import annotations

import json
from xml.sax.saxutils import escape, quoteattr

import generate_ontology


VOCABULARY_NAMESPACE = "https://id.exergism.org/exergism#"
ONTOLOGY_IRI = "https://id.exergism.org/ontology/exergism"
FORMAL_MODEL_PATH = generate_ontology.ROOT / "formal" / "sistema_analitico_exergico.json"
FORMAL_VARIABLES = (
    "P",
    "A",
    "V_ep",
    "L",
    "O",
    "C",
    "S",
    "R",
    "Ecol",
    "U",
    "D_p",
    "D_a",
    "I",
    "Lz",
    "G",
)


def load_formal_variables() -> dict[str, dict]:
    payload = json.loads(FORMAL_MODEL_PATH.read_text(encoding="utf-8"))
    try:
        variables = payload["sistema_matematico_exergico"]["variables_principales"]
    except (KeyError, TypeError) as exc:
        raise SystemExit("formal model does not expose variables_principales") from exc

    if not isinstance(variables, dict):
        raise SystemExit("formal variables_principales must be an object")

    actual = tuple(variables)
    if actual != FORMAL_VARIABLES:
        raise SystemExit(
            "formal variable set/order changed; review semantic identities before regenerating: "
            f"expected {FORMAL_VARIABLES!r}, got {actual!r}"
        )

    for symbol, record in variables.items():
        if not isinstance(record, dict):
            raise SystemExit(f"formal variable {symbol} must be an object")
        for field in ("nombre", "dominio", "definicion"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise SystemExit(f"formal variable {symbol} requires non-empty {field}")
    return variables


def formal_variable_rdfxml() -> str:
    variables = load_formal_variables()
    lines = [
        "",
        "  <!-- Canonical formal exergic-analysis variables (v0.2 projection). -->",
        f"  <owl:Class rdf:about={quoteattr(VOCABULARY_NAMESPACE + 'ExergicVariable')}>",
        '    <rdfs:label xml:lang="en">Exergic variable</rdfs:label>',
        '    <rdfs:comment xml:lang="en">A named variable from the canonical Exergism formal exergic-analysis model.</rdfs:comment>',
        "  </owl:Class>",
        "",
    ]

    for symbol in FORMAL_VARIABLES:
        record = variables[symbol]
        iri = VOCABULARY_NAMESPACE + symbol
        label = escape(record["nombre"])
        definition = escape(record["definicion"])
        domain = escape(record["dominio"])
        lines.extend(
            [
                f"  <owl:NamedIndividual rdf:about={quoteattr(iri)}>",
                f"    <rdf:type rdf:resource={quoteattr(VOCABULARY_NAMESPACE + 'ExergicVariable')}/>",
                f'    <rdfs:label xml:lang="es">{label}</rdfs:label>',
                f'    <rdfs:comment xml:lang="es">{definition}</rdfs:comment>',
                f'    <rdfs:comment xml:lang="en">Formal symbol {escape(symbol)}; canonical normalized domain {domain}.</rdfs:comment>',
                "  </owl:NamedIndividual>",
                "",
            ]
        )
    return "\n".join(lines)


def render_migrated_projection() -> str:
    generate_ontology.BASE_IRI = VOCABULARY_NAMESPACE
    builder = generate_ontology.OntologyBuilder()
    builder.build()
    text = builder.render()

    old_ontology = f'<owl:Ontology rdf:about="{VOCABULARY_NAMESPACE}"/>'
    new_ontology = f'<owl:Ontology rdf:about="{ONTOLOGY_IRI}"/>'
    if text.count(old_ontology) != 1:
        raise SystemExit(
            "id namespace migration failure: expected exactly one generated ontology declaration"
        )
    text = text.replace(old_ontology, new_ontology, 1)

    closing = "</rdf:RDF>"
    if text.count(closing) != 1:
        raise SystemExit("id namespace migration failure: expected exactly one RDF root closing tag")
    return text.replace(closing, formal_variable_rdfxml() + "\n" + closing, 1)


def main() -> None:
    generate_ontology.ONTOLOGY_PATH.write_text(render_migrated_projection(), encoding="utf-8")


if __name__ == "__main__":
    main()
