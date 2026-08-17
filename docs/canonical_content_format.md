# Canonical Content Format

`content/*.json` is the canonical, machine-readable philosophical corpus of the
**Metafísica emergentista de la liberación (Exergism)**.

The canonical layer makes the philosophical structure explicit while keeping
wording and source paths inspectable. It exists so that ontology generation,
validation, search and future publication tooling do not have to rediscover
semantics from ad-hoc JSON nesting on every run.

## Canonical file shape

Each canonical domain has four top-level blocks:

1. `schema_version`
2. `source_format`
3. `domain`
4. `root`

Minimal schema-valid example:

```json
{
  "schema_version": 2,
  "source_format": "legacy-normalized",
  "domain": {
    "id": "ontologia",
    "key": "ontologia",
    "label": "Ontologia",
    "source_file": "ontologia.json"
  },
  "root": {
    "id": "ontologia",
    "key": "ontologia",
    "label": "Ontologia",
    "kind": "concept",
    "source_path": "ontologia",
    "canonical_id": "ontologia",
    "fields": [],
    "collections": [],
    "children": []
  }
}
```

The normative structural contract is `canonical_content_schema.json`.

## Node model

Every node declares:

- `id`: stable scoped identifier;
- exactly one of `canonical_id` or `concept_ref`;
- `key`: source key;
- `label`: human-readable label;
- `kind`: `concept`, `section` or `system`;
- `source_path`: location in the pre-canonical source model;
- `fields`: scalar statements;
- `collections`: ordered collections;
- `children`: nested nodes.

`concept_ref` is used where a structural occurrence points back to an already
canonical conceptual identity instead of creating a new one.

## Field roles

Scalar statements use one of these explicit roles:

- `core`: definition, description, name, theoretical/ontological status, etc.;
- `relation`: relationship statement;
- `thesis`: thesis statement;
- `question`: explicit question;
- `attribute`: other scalar metadata/content.

## Collections

Ordered source lists are explicit collections. `item_kind_hint` is one of:

- `collection_item`;
- `axiom`;
- `question`.

Each item retains order with `order_index`.

## Authoring and migration

The checked-in `content/` directory is already canonical v2 and is the source
of truth for normal repository work. Do **not** regenerate it from a legacy
snapshot as part of routine builds.

`scripts/canonicalize_content.py` exists for two narrower purposes:

1. validate and copy canonical v2 files into another directory; or
2. conservatively import an older legacy JSON corpus.

The legacy importer is deliberately content-preserving and conservative. It
does not attempt the richer concept-merging/identity decisions already encoded
in the checked-in corpus; imported output therefore requires semantic review
before replacing canonical content.

Validate/copy all canonical content:

```bash
python scripts/canonicalize_content.py \
  --input-dir content \
  --output-dir /tmp/exergism-canonical
```

Preview one domain:

```bash
python scripts/canonicalize_content.py \
  --input-dir content \
  --domain ontologia \
  --stdout
```

Import a legacy directory into a review directory:

```bash
python scripts/canonicalize_content.py \
  --input-dir /path/to/legacy/content \
  --output-dir /tmp/exergism-import-review
```

## Ontology generation

`ontology.owl` is derived from the canonical philosophical corpus:

```bash
python scripts/generate_ontology.py
```

The generated OWL is a semantic projection of the corpus, not a replacement
for the canonical JSON and not an independent source of doctrine.
