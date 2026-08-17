from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from generate_ontology import CanonicalSchemaValidator, humanize, slugify

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "content"
DEFAULT_SCHEMA = ROOT / "canonical_content_schema.json"

CORE_KEYS = {
    "definicion",
    "descripcion",
    "descripcion_general",
    "nombre",
    "nombre_completo",
    "nombre_doctrinal",
    "estado_teorico",
    "estado_ontologico",
}


def value_type(value: object) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return "number"
    if isinstance(value, str):
        return "text"
    return "json"


def field_role(key: str) -> str:
    lowered = slugify(key)
    if lowered.startswith("tesis"):
        return "thesis"
    if lowered.startswith("pregunta"):
        return "question"
    if lowered.startswith("relacion_con"):
        return "relation"
    if lowered in CORE_KEYS:
        return "core"
    return "attribute"


def collection_kind(key: str) -> str:
    lowered = slugify(key)
    if "axioma" in lowered:
        return "axiom"
    if "pregunta" in lowered:
        return "question"
    return "collection_item"


def make_field(key: str, value: object, source_path: str) -> dict:
    return {
        "key": key,
        "label": humanize(key),
        "role": field_role(key),
        "value_type": value_type(value),
        "value": value,
        "source_path": source_path,
    }


def make_collection(domain_id: str, key: str, values: list, source_path: str) -> dict:
    return {
        "id": slugify(f"{domain_id}_{source_path}"),
        "key": key,
        "label": humanize(key),
        "source_path": source_path,
        "item_kind_hint": collection_kind(key),
        "items": [
            {
                "order_index": index,
                "value_type": value_type(item),
                "value": item,
            }
            for index, item in enumerate(values, start=1)
        ],
    }


def make_node(
    domain_id: str,
    key: str,
    mapping: dict,
    source_path: str,
    *,
    root: bool = False,
) -> dict:
    node_id = domain_id if root else slugify(f"{domain_id}_{source_path}")
    kind = "system" if root and key == "sistema_filosofico" else ("concept" if root else "section")
    node = {
        "id": node_id,
        "key": key,
        "label": humanize(key),
        "kind": kind,
        "source_path": source_path,
        "canonical_id": node_id,
        "fields": [],
        "collections": [],
        "children": [],
    }

    for child_key, value in mapping.items():
        child_path = f"{source_path}.{child_key}"
        if isinstance(value, dict):
            node["children"].append(
                make_node(domain_id, child_key, value, child_path)
            )
        elif isinstance(value, list):
            node["collections"].append(
                make_collection(domain_id, child_key, value, child_path)
            )
        else:
            node["fields"].append(make_field(child_key, value, child_path))
    return node


def canonicalize_legacy_payload(payload: dict, source_file: str) -> dict:
    if not isinstance(payload, dict) or not payload:
        raise ValueError(f"{source_file}: legacy payload must be a non-empty JSON object")

    domain_id = slugify(Path(source_file).stem)
    if len(payload) == 1:
        root_key, root_value = next(iter(payload.items()))
        if isinstance(root_value, dict):
            root_mapping = root_value
        elif isinstance(root_value, list):
            root_mapping = {root_key: root_value}
        else:
            root_mapping = {"value": root_value}
    else:
        root_key = Path(source_file).stem
        root_mapping = payload

    return {
        "schema_version": 2,
        "source_format": "legacy-normalized",
        "domain": {
            "id": domain_id,
            "key": root_key,
            "label": humanize(root_key),
            "source_file": source_file,
        },
        "root": make_node(domain_id, root_key, root_mapping, root_key, root=True),
    }


def is_canonical(payload: object) -> bool:
    return (
        isinstance(payload, dict)
        and payload.get("schema_version") == 2
        and isinstance(payload.get("domain"), dict)
        and isinstance(payload.get("root"), dict)
    )


def canonicalize_path(path: Path, validator: CanonicalSchemaValidator) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    canonical = payload if is_canonical(payload) else canonicalize_legacy_payload(payload, path.name)
    validator.validate_payload(canonical, path.name)
    return canonical


def export_canonical_content(input_dir: Path, output_dir: Path, schema_path: Path = DEFAULT_SCHEMA) -> None:
    validator = CanonicalSchemaValidator(schema_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(input_dir.glob("*.json")):
        canonical = canonicalize_path(path, validator)
        target = output_dir / path.name
        target.write_text(json.dumps(canonical, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Validate/copy canonical v2 content or conservatively import legacy JSON into "
            "the canonical Exergism content schema. The legacy importer preserves source "
            "content but deliberately avoids semantic identity-merging heuristics."
        )
    )
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--domain", help="Process only <domain>.json")
    parser.add_argument("--stdout", action="store_true", help="Write one canonical payload to stdout")
    args = parser.parse_args()

    validator = CanonicalSchemaValidator(DEFAULT_SCHEMA)
    paths = [args.input_dir / f"{args.domain}.json"] if args.domain else sorted(args.input_dir.glob("*.json"))
    if not paths:
        raise SystemExit("No JSON content files found")

    if args.stdout:
        if len(paths) != 1:
            raise SystemExit("--stdout requires --domain (or an input directory containing one JSON file)")
        canonical = canonicalize_path(paths[0], validator)
        print(json.dumps(canonical, ensure_ascii=False, indent=2))
        return

    if args.output_dir is None:
        raise SystemExit("--output-dir is required unless --stdout is used")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for path in paths:
        canonical = canonicalize_path(path, validator)
        target = args.output_dir / path.name
        target.write_text(json.dumps(canonical, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {target}")


if __name__ == "__main__":
    main()
