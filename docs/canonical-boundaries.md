# Canonical boundaries

This repository deliberately separates five layers that must not be conflated.

## 1. Canonical philosophical wording

`content/*.json` contains the canonical machine-readable philosophical corpus. Its statements, definitions, theses, questions and relations are the primary source for the corresponding philosophical wording.

## 2. Book architecture

`books/libros.json` defines the four-book editorial architecture. It organizes exposition; it does not silently override contradictory canonical philosophical wording.

## 3. Formal exergic analysis

`formal/sistema_analitico_exergico.json` contains the recovered formal analytical model. Numerical outputs are analytical aids, not automatic truth, moral verdicts, legal classifications or ECL outcomes.

The model includes contextual parameters and unresolved/provisional surfaces. Consumers must expose parameter choices and uncertainty rather than fill gaps silently. See `formal/FORMAL-MODEL-STATUS.md`.

## 4. Derived ontology

`ontology.owl` is generated from the canonical philosophical corpus. It exists for semantic navigation and machine processing.

OWL representation is **not** an independent doctrinal source. The generator must not introduce legal classifications or hidden normative inference absent from canonical sources.

## 5. Applied examples and downstream systems

`examples/` preserves applied analytical artifacts. Missing original generators mean some recovered examples are not fully reproducible pipelines.

Downstream projects, including ECL, are applications. Their legal or governance state is not inferred by this repository. They should bind to immutable Exergism releases when they need a stable conceptual/formal upstream.

## Conflict rule

When a derived or organizational layer conflicts with canonical philosophical wording, the conflict must be surfaced for review rather than silently resolving doctrine through tooling.
