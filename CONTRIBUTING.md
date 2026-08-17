# Contributing to Exergism

Contributions are welcome as criticism, corrections, formal analysis, ontology/schema improvements, documentation and proposed philosophical development.

## Before opening a pull request

Run:

```bash
python scripts/validate_repository.py
```

If canonical philosophical content changes, also regenerate and include the derived ontology:

```bash
python scripts/generate_ontology.py
python scripts/validate_repository.py
```

## Describe semantic effect

Classify the change using `GOVERNANCE.md` as mechanical/editorial, structural/semantic-preserving, or doctrinal/formal.

Doctrinal/formal changes must state the semantic delta, rationale, serious counterarguments and affected downstream concepts. Do not hide substantive edits inside a bulk migration or generated file.

## Licensing of contributions

By intentionally submitting a contribution for inclusion, you license that contribution under the license already governing the target material as described in `LICENSE.md`:

- corpus/documentation contributions: `CC-BY-SA-4.0`;
- software/tooling contributions: `Apache-2.0`.

You retain copyright in your contribution. This repository does not require copyright assignment merely to contribute.

Do not submit material you are not authorized to license on those terms. Clearly identify third-party material and its license before inclusion.

## Generated artifacts

`ontology.owl` is derived from the canonical corpus. Do not edit it as an independent source of doctrine. Update canonical sources and regenerate it.

Recovered examples under `examples/exergic-analysis/` are preserved evidence of historical use of the formal model; see their README before claiming reproducibility.
