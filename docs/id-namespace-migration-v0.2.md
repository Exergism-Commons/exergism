# Exergism v0.2 identifier migration

Status: **release-candidate architecture**

Exergism v0.2 migrates the generated semantic projection from the historical namespace:

`http://www.exergia.org/ns/`

to the persistent EC identifier authority:

`https://id.exergism.org/exergism#`

The ontology document IRI is independently:

`https://id.exergism.org/ontology/exergism`

## Historical boundary

Exergism v0.1.0 remains an immutable historical release. Its semantic artifacts are not rewritten merely because v0.2 adopts a different identifier authority.

The migration therefore changes the next generated projection, not the bytes or asserted identifiers of v0.1.0.

## Canonical ownership

`Exergism-Commons/exergism` remains the semantic authority for the philosophical corpus and formal exergic-analysis model. `id.exergism.org` dereferences the adopted identifiers but does not become the source of their meaning.

## Formal variables

The Exergism formal model is the canonical home for the exergic variables, including:

- `P`
- `A`
- `V_ep`
- `L`
- `O`
- `U`
- `C`
- `S`
- `R`
- `Ecol`

Downstream EC projects such as ECL must reuse these identities when they mean the same variables, or define explicitly mapped domain-specific concepts when they intentionally narrow or operationalize them.

## Generation

The historical generator implementation remains available as `scripts/generate_ontology.py`. The v0.2 release candidate uses `scripts/generate_id_ontology.py`, which reuses the same canonical corpus and generator logic while selecting the new vocabulary namespace and distinct ontology IRI.

This prevents namespace migration from silently changing the philosophical source model.

## Compatibility

Because the v0.2 identifiers are being designed before their stable release, their exact mapping remains reviewable until v0.2 is adopted. Once a v0.2 IRI is declared stable, the EC persistent-identifier policy applies: it is not reassigned or silently repurposed.

Where a v0.1.0 term and a v0.2 term are semantically identical, compatibility mappings may be published by the canonical Exergism release process. Such mappings must not be guessed merely from local-name equality.
