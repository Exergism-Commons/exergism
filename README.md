# Exergism

**Metafísica emergentista de la liberación** (*Exergismo / Exergism*) is a
philosophical system centered on emergence, truth, consciousness, autonomy,
exergy, capture, liberation and the possibility of breaking recurrent cycles
of domination.

This repository is the canonical working corpus of the system. It keeps the
philosophical source, its formal exergic-analysis model, the four-book
architecture, applied examples and a generated OWL projection in one
version-controlled tree.

## Repository map

- `content/` — canonical philosophical corpus (JSON, schema v2).
- `formal/sistema_analitico_exergico.json` — formal exergic-analysis system,
  including variables, formulas, uncertainty, temporal integration and
  non-compensatory rules.
- `books/libros.json` — architecture of the four-book series:
  1. **Cárcel del Mundo / World Jail**
  2. **Luz Condenada / Doomed Light**
  3. **Romper el Ciclo / Break the Cycle**
  4. **Razón Exérgica / Exergic Reason**
- `examples/exergic-analysis/` — preserved applied-analysis datasets and
  visualizations.
- `ontology.owl` — generated semantic projection of the canonical
  philosophical corpus.
- `canonical_content_schema.json` — structural contract for `content/*.json`.
- `scripts/` — validation, migration and ontology-generation tooling.
- `manifest.json` — inventory and canonical reading order.

## Canonicality

`content/*.json`, `books/libros.json` and
`formal/sistema_analitico_exergico.json` are source artifacts. `ontology.owl`
is derived and MUST be reproducible from the checked-in canonical corpus.

The OWL projection does not supersede philosophical wording, and numerical
formalism does not silently convert philosophical claims into legal or
institutional conclusions.

## Validate

```bash
python scripts/validate_repository.py
```

Regenerate the ontology:

```bash
python scripts/generate_ontology.py
```

See `docs/canonical_content_format.md` for the content model and legacy-import
workflow.

## Relationship to ECL

The Exergic Commons License (ECL) is an application built using concepts and a
formal analytical lineage from Exergism. ECL is not the canonical home of the
philosophical system. Legal restrictions, Schedule designations and governance
outcomes belong to ECL and are not inferred merely from this repository.

## Development status

The corpus remains under active development. `manifest.json` identifies this
state as a canonicalization candidate rather than a philosophical 1.0 release.

## Licensing

No public-content license is selected by this repository state. A license for
the philosophical corpus, data and tooling must be chosen explicitly before a
public release; it must not be inferred from ECL merely because ECL derives
from Exergism.
