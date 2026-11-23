from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape


BASE_IRI = "https://id.exergism.org/exergism#"
ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
ONTOLOGY_PATH = ROOT / "ontology.owl"
CANONICAL_SCHEMA_PATH = ROOT / "canonical_content_schema.json"

PASS_THROUGH_SECTION_KEYS = {
    "tipos",
    "niveles",
    "formas",
    "formas_posibles",
    "mecanismos",
    "modalidades",
    "fases",
    "etapas",
    "pasos",
    "dominios",
    "potencial",
    "distincion_clave",
    "ejemplos",
    "rasgos_estructurales",
    "grados_de_demiurgicidad",
    "filtros_de_discernimiento",
    "capas_del_metodo",
    "medios_de_liberacion",
    "tipos_de_exergia",
    "tipos_de_conocimiento",
}

SCALAR_NODE_PARENT_KEYS = {
    "tipos",
    "niveles",
    "modalidades",
    "dimensiones",
    "formas",
    "formas_posibles",
    "etapas",
    "pasos",
    "fases",
    "distincion_clave",
    "tipos_de_exergia",
    "fuentes_del_conocimiento",
    "reacciones_basicas",
    "responsabilidad_moral",
}

SCALAR_NODE_SCOPED_PARENT_KEYS = {
    "etapas",
    "pasos",
    "fases",
    "distincion_clave",
}

SEQUENTIAL_PARENT_KEYS = {
    "etapas",
    "pasos",
    "fases",
}

SPECIAL_SECTION_CONCEPT_ANCHORS = {
    "tipos_de_exergia": "exergia",
}

SEMANTIC_ENTITY_ALIASES = {
    "conciencia": (
        "conciencia",
        "conciencias",
        "consciente",
        "conscientes",
        "ser consciente",
        "seres conscientes",
    ),
    "materia": (
        "materia",
        "material",
        "materiales",
    ),
    "vida": (
        "vida",
        "ser vivo",
        "seres vivos",
        "viviente",
        "vivientes",
        "biologico",
        "biologica",
    ),
    "ser_humano": (
        "ser humano",
        "seres humanos",
        "humano",
        "humanos",
        "humanidad",
    ),
    "realidad": (
        "realidad",
        "lo real",
    ),
    "universo": (
        "universo",
    ),
    "espiritu": (
        "espiritu",
    ),
    "espiritu_humano": (
        "espiritu humano",
    ),
    "demiurgo": (
        "demiurgo",
    ),
    "alma": (
        "alma",
    ),
    "verdad_absoluta": (
        "verdad absoluta",
    ),
    "exergia": (
        "exergia",
        "exergico",
        "exergica",
    ),
    "autonomia": (
        "autonomia",
        "autonomo",
        "autonoma",
    ),
}

PATH_SEMANTIC_ANCHORS = {
    "procesos_basales_conscientes": ("conciencia",),
    "procesos_de_elaboracion_consciente": ("conciencia",),
    "procesos_secundarios_conscientes": ("conciencia",),
    "emociones_reactivas": ("conciencia",),
    "naturaleza_humana": ("ser_humano", "conciencia"),
}

PATH_SCOPED_DUPLICATE_KEYS = {
    "distincion_clave",
    "mecanismos",
    "niveles",
    "tipos",
    "durante_la_sociedad_liberada",
    "durante_la_transicion",
    "funciones",
    "limites",
    "miedo",
    "relacion_con_la_exergia",
    "relacion_con_la_verdad_absoluta",
    "guia_intercivilizatoria",
}

MERGED_DUPLICATE_KEYS = {
    "carcel_del_mundo",
    "demiurgo",
    "justicia",
}

CORE_FIELD_MAP = {
    "definicion": "hasDefinition",
    "descripcion": "hasDescription",
    "descripcion_general": "hasDescription",
    "nombre": "hasName",
    "estado_teorico": "hasTheoreticalStatus",
    "estado_ontologico": "hasOntologicalStatus",
}

RELATION_PREFIXES = (
    "relacion_con_la_",
    "relacion_con_el_",
    "relacion_con_las_",
    "relacion_con_los_",
    "relacion_con_",
)

CLASS_PRIORITIES = {
    "Domain": 0,
    "System": 1,
    "ConceptLevel": 2,
    "ConceptSubtype": 3,
    "Concept": 4,
    "Section": 5,
    "Thesis": 6,
    "Axiom": 7,
    "Question": 8,
    "Collection": 9,
    "CollectionItem": 10,
}

FORCED_CONCEPT_KEYS = {
    "estructura_de_lo_real",
    "fundamento_ultimo",
    "realidad_manifestada",
    "niveles_emergentes",
    "dominio_humano_y_clausura",
    "limites_de_la_individualidad",
    "procesos_basales_conscientes",
    "emociones_reactivas",
    "procesos_de_elaboracion_consciente",
    "procesos_secundarios_conscientes",
    "naturaleza_humana",
    "gnosticismo_antropologico",
}


class CanonicalSchemaValidationError(ValueError):
    """Raised when a canonical content file does not satisfy the expected schema."""


class CanonicalSchemaValidator:
    def __init__(self, schema_path: Path) -> None:
        self.schema_path = schema_path
        self.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.native_validator = self._build_native_validator()

        defs = self.schema["$defs"]
        self.top_required = set(self.schema["required"])
        self.top_allowed = set(self.schema["properties"])
        self.domain_required = set(defs["domain"]["required"])
        self.domain_allowed = set(defs["domain"]["properties"])
        self.node_required = set(defs["node_base"]["required"])
        self.node_allowed = set(defs["node_base"]["properties"])
        self.field_required = set(defs["field"]["required"])
        self.field_allowed = set(defs["field"]["properties"])
        self.collection_required = set(defs["collection"]["required"])
        self.collection_allowed = set(defs["collection"]["properties"])
        self.collection_item_required = set(defs["collection_item"]["required"])
        self.collection_item_allowed = set(defs["collection_item"]["properties"])
        self.expected_schema_version = self.schema["properties"]["schema_version"]["const"]
        self.allowed_source_formats = set(self.schema["properties"]["source_format"]["enum"])
        self.allowed_node_kinds = set(defs["node_base"]["properties"]["kind"]["enum"])
        self.allowed_field_roles = set(defs["field"]["properties"]["role"]["enum"])
        self.allowed_field_value_types = set(defs["field"]["properties"]["value_type"]["enum"])
        self.allowed_collection_item_value_types = set(defs["collection_item"]["properties"]["value_type"]["enum"])
        self.allowed_collection_item_kinds = set(defs["collection"]["properties"]["item_kind_hint"]["enum"])

    def _build_native_validator(self):
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            return None
        return Draft202012Validator(self.schema)

    def validate_payload(self, payload: dict, source_name: str) -> None:
        if self.native_validator is not None:
            errors = sorted(self.native_validator.iter_errors(payload), key=lambda err: list(err.path))
            if errors:
                error = errors[0]
                path = ".".join(str(part) for part in error.path) or "<root>"
                raise CanonicalSchemaValidationError(f"{source_name}:{path}: {error.message}")
            return
        self._validate_payload_fallback(payload, source_name)

    def _validate_payload_fallback(self, payload: dict, source_name: str) -> None:
        self._validate_object(payload, source_name, self.top_required, self.top_allowed)
        self._require(
            payload["schema_version"] == self.expected_schema_version,
            f"schema_version must be {self.expected_schema_version}, got {payload['schema_version']!r}",
            f"{source_name}.schema_version",
        )
        self._require(
            payload["source_format"] in self.allowed_source_formats,
            f"source_format must be one of {sorted(self.allowed_source_formats)}, got {payload['source_format']!r}",
            f"{source_name}.source_format",
        )
        self._validate_domain(payload["domain"], f"{source_name}.domain")
        self._validate_node(payload["root"], f"{source_name}.root")

    def _validate_domain(self, domain: object, path: str) -> None:
        self._validate_object(domain, path, self.domain_required, self.domain_allowed)
        assert isinstance(domain, dict)
        for key in self.domain_allowed:
            self._require(isinstance(domain[key], str), f"{key} must be a string", f"{path}.{key}")

    def _validate_node(self, node: object, path: str) -> None:
        self._validate_object(node, path, self.node_required, self.node_allowed)
        assert isinstance(node, dict)

        for key in ("id", "key", "label", "source_path"):
            self._require(isinstance(node[key], str), f"{key} must be a string", f"{path}.{key}")

        self._require(
            node["kind"] in self.allowed_node_kinds,
            f"kind must be one of {sorted(self.allowed_node_kinds)}, got {node['kind']!r}",
            f"{path}.kind",
        )

        has_canonical_id = "canonical_id" in node
        has_concept_ref = "concept_ref" in node
        self._require(
            has_canonical_id != has_concept_ref,
            "node must define exactly one of canonical_id or concept_ref",
            path,
        )
        if has_canonical_id:
            self._require(
                isinstance(node["canonical_id"], str),
                "canonical_id must be a string",
                f"{path}.canonical_id",
            )
        if has_concept_ref:
            self._require(
                isinstance(node["concept_ref"], str),
                "concept_ref must be a string",
                f"{path}.concept_ref",
            )

        aliases = node.get("aliases")
        if aliases is not None:
            self._validate_string_array(aliases, f"{path}.aliases")

        self._validate_array(node["fields"], f"{path}.fields")
        for index, field in enumerate(node["fields"]):
            self._validate_field(field, f"{path}.fields[{index}]")

        self._validate_array(node["collections"], f"{path}.collections")
        for index, collection in enumerate(node["collections"]):
            self._validate_collection(collection, f"{path}.collections[{index}]")

        self._validate_array(node["children"], f"{path}.children")
        for index, child in enumerate(node["children"]):
            self._validate_node(child, f"{path}.children[{index}]")

    def _validate_field(self, field: object, path: str) -> None:
        self._validate_object(field, path, self.field_required, self.field_allowed)
        assert isinstance(field, dict)

        for key in ("key", "label", "source_path"):
            self._require(isinstance(field[key], str), f"{key} must be a string", f"{path}.{key}")

        self._require(
            field["role"] in self.allowed_field_roles,
            f"role must be one of {sorted(self.allowed_field_roles)}, got {field['role']!r}",
            f"{path}.role",
        )
        self._require(
            field["value_type"] in self.allowed_field_value_types,
            f"value_type must be one of {sorted(self.allowed_field_value_types)}, got {field['value_type']!r}",
            f"{path}.value_type",
        )

        target_hints = field.get("target_hints")
        if target_hints is not None:
            self._validate_string_array(target_hints, f"{path}.target_hints")

        target_ids = field.get("target_ids")
        if target_ids is not None:
            self._validate_string_array(target_ids, f"{path}.target_ids")

    def _validate_collection(self, collection: object, path: str) -> None:
        self._validate_object(collection, path, self.collection_required, self.collection_allowed)
        assert isinstance(collection, dict)

        for key in ("id", "key", "label", "source_path"):
            self._require(isinstance(collection[key], str), f"{key} must be a string", f"{path}.{key}")

        self._require(
            collection["item_kind_hint"] in self.allowed_collection_item_kinds,
            f"item_kind_hint must be one of {sorted(self.allowed_collection_item_kinds)}, got {collection['item_kind_hint']!r}",
            f"{path}.item_kind_hint",
        )

        self._validate_array(collection["items"], f"{path}.items")
        for index, item in enumerate(collection["items"]):
            self._validate_collection_item(item, f"{path}.items[{index}]")

    def _validate_collection_item(self, item: object, path: str) -> None:
        self._validate_object(item, path, self.collection_item_required, self.collection_item_allowed)
        assert isinstance(item, dict)

        self._require(
            isinstance(item["order_index"], int) and not isinstance(item["order_index"], bool) and item["order_index"] >= 1,
            "order_index must be an integer >= 1",
            f"{path}.order_index",
        )
        self._require(
            item["value_type"] in self.allowed_collection_item_value_types,
            f"value_type must be one of {sorted(self.allowed_collection_item_value_types)}, got {item['value_type']!r}",
            f"{path}.value_type",
        )

    def _validate_object(self, value: object, path: str, required_keys: set[str], allowed_keys: set[str]) -> None:
        self._require(isinstance(value, dict), "must be an object", path)
        assert isinstance(value, dict)
        missing = required_keys - set(value)
        self._require(not missing, f"missing required keys: {sorted(missing)}", path)
        extra = set(value) - allowed_keys
        self._require(not extra, f"unexpected keys: {sorted(extra)}", path)

    def _validate_array(self, value: object, path: str) -> None:
        self._require(isinstance(value, list), "must be an array", path)

    def _validate_string_array(self, value: object, path: str) -> None:
        self._validate_array(value, path)
        assert isinstance(value, list)
        for index, item in enumerate(value):
            self._require(isinstance(item, str), "must contain only strings", f"{path}[{index}]")

    def _require(self, condition: bool, message: str, path: str) -> None:
        if not condition:
            raise CanonicalSchemaValidationError(f"{path}: {message}")


def validate_content_corpus(content_dir: Path = CONTENT_DIR, schema_path: Path = CANONICAL_SCHEMA_PATH) -> None:
    validator = CanonicalSchemaValidator(schema_path)
    for path in sorted(content_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        validator.validate_payload(payload, path.name)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", ascii_text).strip("_").lower()
    if not slug:
        return "unnamed"
    if slug[0].isdigit():
        return f"n_{slug}"
    return slug


def humanize(value: str) -> str:
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", value)
    text = text.replace("_", " ").strip()
    if not text:
        return value
    return text[0].upper() + text[1:]


def truncate_label(text: str, limit: int = 96) -> str:
    compact = re.sub(r"\s+", " ", text.strip())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


def ttl_lang(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\r", "").replace("\n", "\\n")
    return f'"{escaped}"@es'


def ttl_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\r", "").replace("\n", "\\n")
    return f'"{escaped}"^^xsd:string'


def ttl_int(value: int) -> str:
    return f'"{value}"^^xsd:integer'


def xml_text(value: str) -> str:
    return escape(value, {'"': "&quot;"})


def xml_resource_uri(value: str, default_base: str = BASE_IRI) -> str:
    if value == "owl:Thing":
        return "http://www.w3.org/2002/07/owl#Thing"
    if value == "rdf:langString":
        return "http://www.w3.org/1999/02/22-rdf-syntax-ns#langString"
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return f"{default_base}{value}"


def append_unique(items: list, value) -> None:
    if value not in items:
        items.append(value)


@dataclass
class Individual:
    identifier: str
    types: list[str] = field(default_factory=list)
    object_props: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    data_props: dict[str, list[tuple[str, object]]] = field(default_factory=lambda: defaultdict(list))
    label: str | None = None

    def add_type(self, class_name: str) -> None:
        append_unique(self.types, class_name)

    def add_obj(self, prop: str, target: str) -> None:
        append_unique(self.object_props[prop], target)

    def add_data(self, prop: str, kind: str, value: object) -> None:
        append_unique(self.data_props[prop], (kind, value))


class OntologyBuilder:
    def __init__(self) -> None:
        self.individuals: dict[str, Individual] = {}
        self.dynamic_datatype_properties: dict[str, str] = {}
        self.object_occurrences: dict[str, list[tuple[str, tuple[str, ...], dict]]] = defaultdict(list)
        self.old_primary_domains: dict[str, str] = {}
        self.old_enrichments: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
        self.primary_domain_assigned: dict[str, str] = {}
        self.alias_to_id: dict[str, str] = {}

    def load_payload(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def is_canonical_payload(self, payload: dict) -> bool:
        return (
            isinstance(payload, dict)
            and payload.get("schema_version") in {1, 2}
            and isinstance(payload.get("domain"), dict)
            and isinstance(payload.get("root"), dict)
        )

    def canonical_path_parts(self, source_path: str) -> tuple[str, ...]:
        return tuple(part for part in source_path.split(".") if part)

    def canonical_string_value(self, value) -> str:
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False)
        return str(value)

    def canonical_field_entry(self, node: dict | None, key: str) -> dict | None:
        if not node:
            return None
        for field in node.get("fields", []):
            if field.get("key") == key:
                return field
        return None

    def canonical_child_entry(self, node: dict | None, key: str) -> dict | None:
        if not node:
            return None
        for child in node.get("children", []):
            if child.get("key") == key:
                return child
        return None

    def ensure(self, identifier: str, *types: str) -> Individual:
        node = self.individuals.get(identifier)
        if node is None:
            node = Individual(identifier=identifier)
            self.individuals[identifier] = node
        for class_name in types:
            node.add_type(class_name)
        return node

    def register_aliases(self, identifier: str, *aliases: str) -> None:
        for alias in aliases:
            if not alias:
                continue
            slug = slugify(alias)
            if slug and slug not in self.alias_to_id:
                self.alias_to_id[slug] = identifier

    def resolve_identifier(self, raw_identifier: str) -> str | None:
        slug = slugify(raw_identifier)
        if slug in self.individuals:
            return slug
        return self.alias_to_id.get(slug)

    def ensure_concept_anchor(self, identifier: str, label: str | None = None) -> str:
        node = self.ensure(identifier, "Concept")
        if label and not node.label:
            self.set_label(identifier, label)
            self.add_lang(identifier, "hasName", label)
        self.register_aliases(identifier, identifier, label or "")
        return identifier

    def set_label(self, identifier: str, label: str) -> None:
        if label:
            self.ensure(identifier).label = label

    def add_obj(self, subject: str, prop: str, target: str) -> None:
        self.ensure(subject).add_obj(prop, target)

    def add_data(self, subject: str, prop: str, kind: str, value: object) -> None:
        self.ensure(subject).add_data(prop, kind, value)

    def add_lang(self, subject: str, prop: str, value: str) -> None:
        if value:
            self.add_data(subject, prop, "lang", value)

    def add_string(self, subject: str, prop: str, value: str) -> None:
        if value:
            self.add_data(subject, prop, "string", value)

    def add_int(self, subject: str, prop: str, value: int) -> None:
        self.add_data(subject, prop, "int", value)

    def add_field_text(self, subject: str, key: str, value: str) -> None:
        prop = f"field_{slugify(key)}"
        self.dynamic_datatype_properties[prop] = humanize(key)
        self.add_lang(subject, prop, value)

    def scoped_id(self, domain_id: str, path_parts: tuple[str, ...], suffix: str | None = None) -> str:
        parts = list(path_parts)
        if parts and slugify(parts[0]) == domain_id:
            parts = parts[1:]
        if suffix:
            parts.append(suffix)
        return slugify("_".join([domain_id] + parts))

    def register_domain_membership(self, identifier: str, domain_id: str, source_file: str, source_path: str) -> None:
        self.add_obj(identifier, "appearsIn", domain_id)
        if identifier in self.old_primary_domains:
            self.add_obj(identifier, "belongsToDomain", self.old_primary_domains[identifier])
        elif identifier not in self.primary_domain_assigned:
            self.primary_domain_assigned[identifier] = domain_id
            self.add_obj(identifier, "belongsToDomain", domain_id)
        if "Concept" in self.ensure(identifier).types and identifier != domain_id:
            self.add_obj(domain_id, "hasConcept", identifier)
        self.add_string(identifier, "hasSourceFile", source_file)
        self.add_string(identifier, "hasSourcePath", source_path)

    def scan_existing_ontology(self) -> None:
        if not ONTOLOGY_PATH.exists():
            return

        text = ONTOLOGY_PATH.read_text(encoding="utf-8")

        selected_props = {
            "belongsToDomain",
            "hasLevel",
            "hasSubtype",
        }

        blocks = [block for block in re.split(r"\n\s*\n", text) if block.strip()]
        for block in blocks:
            lines = [line.rstrip() for line in block.splitlines() if line.strip()]
            if not lines:
                continue
            first = lines[0].strip()
            if not first.startswith(":") or "owl:NamedIndividual" not in first:
                continue

            subject = slugify(first.split()[0][1:])
            for line in lines[1:]:
                stripped = line.strip()
                if not stripped.startswith(":"):
                    continue
                prop = stripped[1:].split()[0]
                if prop not in selected_props:
                    continue
                tail = stripped.split(None, 1)[1]
                targets = [slugify(match) for match in re.findall(r":([A-Za-z_][A-Za-z0-9_]*)", tail)]
                for target in targets:
                    append_unique(self.old_enrichments[subject][prop], target)
                if prop == "belongsToDomain" and targets and subject not in self.old_primary_domains:
                    self.old_primary_domains[subject] = targets[0]

    def scan_object_occurrences(self) -> None:
        for path in sorted(CONTENT_DIR.glob("*.json")):
            data = self.load_payload(path)
            if self.is_canonical_payload(data):
                continue
            domain_key = next(iter(data))
            self._scan_value(domain_key, tuple(), data[domain_key])

    def _scan_value(self, domain_key: str, path_parts: tuple[str, ...], value) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if isinstance(child, dict):
                    self.object_occurrences[slugify(key)].append((domain_key, path_parts + (key,), child))
                self._scan_value(domain_key, path_parts + (key,), child)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                self._scan_value(domain_key, path_parts + (f"[{index}]",), item)

    def choose_node_id(self, domain_key: str, path_parts: tuple[str, ...], value: dict) -> str:
        key = path_parts[-1]
        key_slug = slugify(key)
        repeated = len(self.object_occurrences[key_slug]) > 1

        if key_slug in MERGED_DUPLICATE_KEYS:
            return key_slug
        if repeated and key_slug in PATH_SCOPED_DUPLICATE_KEYS:
            return self.scoped_id(domain_key, path_parts)
        if not repeated:
            return key_slug
        if self.is_concept_like(key, value):
            return key_slug
        return self.scoped_id(domain_key, path_parts)

    def is_concept_like(self, key: str, value: dict) -> bool:
        key_slug = slugify(key)
        if key_slug in FORCED_CONCEPT_KEYS:
            return True

        markers = {
            "definicion",
            "nombre",
            "tesis_central",
            "tesis_general",
            "tesis",
            "estado_ontologico",
            "estado_teorico",
            "tipo",
        }
        if any(marker in value for marker in markers):
            return True

        return False

    def infer_related_targets(self, field_key: str, explicit_targets: list[str] | None = None) -> list[str]:
        if explicit_targets:
            resolved_targets: list[str] = []
            for target in explicit_targets:
                resolved = self.resolve_identifier(target)
                if resolved is None:
                    resolved = self.ensure_concept_anchor(slugify(target), humanize(target))
                append_unique(resolved_targets, resolved)
            return resolved_targets
        for prefix in RELATION_PREFIXES:
            if field_key.startswith(prefix):
                remainder = slugify(field_key[len(prefix) :])
                resolved = self.resolve_identifier(remainder)
                if resolved:
                    return [resolved]
                split_targets = []
                for part in re.split(r"_(?:y|e)_", remainder):
                    resolved_part = self.resolve_identifier(part)
                    if resolved_part:
                        split_targets.append(resolved_part)
                return split_targets
        return []

    def infer_textual_targets(self, text: str) -> list[str]:
        normalized = slugify(text).replace("_", " ")
        targets: list[str] = []
        for identifier in SEMANTIC_ENTITY_ALIASES:
            for variant in self.entity_variants(identifier):
                if " " in variant:
                    if variant in normalized:
                        append_unique(targets, identifier)
                        break
                elif re.search(rf"\b{re.escape(variant)}\b", normalized):
                    append_unique(targets, identifier)
                    break
        return targets

    def should_materialize_scalar_node(self, parent_key: str, key: str, value: str) -> bool:
        parent_slug = slugify(parent_key)
        key_slug = slugify(key)
        if parent_slug not in SCALAR_NODE_PARENT_KEYS:
            return False
        if key_slug in CORE_FIELD_MAP:
            return False
        if key.startswith("relacion_") or key.startswith("tesis") or key.startswith("pregunta"):
            return False
        words = len(value.split())
        return words >= 2

    def choose_scalar_node_id(self, domain_id: str, path_parts: tuple[str, ...], key: str) -> str:
        parent_slug = slugify(path_parts[-1]) if path_parts else ""
        key_slug = slugify(key)
        if parent_slug in SCALAR_NODE_SCOPED_PARENT_KEYS:
            return self.scoped_id(domain_id, path_parts + (key,))
        if key_slug in self.individuals:
            return self.scoped_id(domain_id, path_parts + (key,))
        return key_slug

    def apply_contextual_semantics(self, node_id: str, path_parts: tuple[str, ...], concept_anchor: str | None) -> None:
        node = self.ensure(node_id)
        if "Concept" not in node.types:
            return

        path_slugs = [slugify(part) for part in path_parts]
        parent_slug = path_slugs[-2] if len(path_slugs) >= 2 else ""
        current_slug = path_slugs[-1] if path_slugs else ""

        if concept_anchor is not None:
            anchor = self.ensure(concept_anchor)
            if "hasLevel" in anchor.object_props and "hasLevel" not in node.object_props:
                for target in anchor.object_props["hasLevel"]:
                    self.add_obj(node_id, "hasLevel", target)
            if concept_anchor != node_id:
                self.add_obj(node_id, "relatedTo", concept_anchor)

        if "hasSubtype" not in node.object_props:
            if parent_slug == "niveles" or re.match(r"^nivel_\d+", current_slug):
                self.add_obj(node_id, "hasSubtype", "level_subtype")
            elif parent_slug in {"tipos", "modalidades", "dimensiones", "formas", "formas_posibles", "reacciones_basicas", "responsabilidad_moral", "fuentes_del_conocimiento", "distincion_clave"}:
                self.add_obj(node_id, "hasSubtype", "type_subtype")
            elif parent_slug in {"etapas", "pasos", "fases"}:
                self.add_obj(node_id, "hasSubtype", "process")
            elif "mecanismos" in path_slugs:
                self.add_obj(node_id, "hasSubtype", "mechanism")

        for part in path_slugs:
            for target in PATH_SEMANTIC_ANCHORS.get(part, ()):
                if target != node_id:
                    self.add_obj(node_id, "relatedTo", target)

    def entity_variants(self, identifier: str) -> list[str]:
        node = self.ensure(identifier)
        variants = {slugify(identifier).replace("_", " ")}
        if node.label:
            variants.add(slugify(node.label).replace("_", " "))
        for alias in SEMANTIC_ENTITY_ALIASES.get(identifier, ()):
            variants.add(slugify(alias).replace("_", " "))
        return sorted(variants, key=len, reverse=True)

    def contains_any_cue(self, normalized: str, cues: tuple[str, ...]) -> bool:
        for cue in cues:
            if " " in cue:
                if cue in normalized:
                    return True
                continue
            if re.search(rf"\b{re.escape(cue)}\b", normalized):
                return True
        return False

    def leading_entity(self, text: str, owner: str, target: str) -> str | None:
        normalized = slugify(text).replace("_", " ")
        articles = ("", "el ", "la ", "los ", "las ", "lo ", "un ", "una ")
        for candidate, role in ((target, "target"), (owner, "owner")):
            for variant in self.entity_variants(candidate):
                for article in articles:
                    if normalized.startswith(article + variant):
                        return role
        return None

    def infer_specific_relation(self, owner: str, target: str, field_key: str, text: str) -> tuple[str, str, str]:
        normalized = slugify(text).replace("_", " ")
        leading = self.leading_entity(text, owner, target)
        relation_slug = slugify(field_key)
        owner_variants = self.entity_variants(owner)

        if self.contains_any_cue(normalized, ("opuesto", "opuesta", "contrario", "contraria", "se opone")):
            return ("opposes", owner, target)

        grounding_cues = (
            "condicion de posibilidad",
            "fundamento",
            "base practica",
            "base de",
            "horizonte",
        )
        if self.contains_any_cue(normalized, grounding_cues):
            return ("grounds", owner, target)

        dependency_cues = (
            "se apoya en",
            "se apoya sobre",
            "apoyado en",
            "apoyada en",
            "depende de",
            "depende del",
            "depende de la",
            "solo puede entenderse dentro de",
            "debe someterse plenamente a",
            "subordinada a",
            "subordinado a",
            "requiere",
            "descansa sobre",
        )
        if self.contains_any_cue(normalized, dependency_cues):
            return ("grounds", target, owner)

        emergence_cues = (
            "surge de",
            "surgen de",
            "surgir de",
            "surge cuando",
            "surgen cuando",
            "emerge de",
            "emergen de",
            "nace de",
            "nacen de",
            "nacer de",
            "resultado de",
            "producto de",
            "forma emergente de",
            "una de sus manifestaciones",
            "caso particular de",
            "caso particular del",
            "depende de la integracion",
        )
        if self.contains_any_cue(normalized, emergence_cues):
            if leading == "target":
                return ("emergesFrom", target, owner)
            return ("emergesFrom", owner, target)

        expressive_emergence_cues = (
            "es una expresion",
            "es una manifestacion",
            "es una forma parcial",
            "son manifestaciones",
            "son expresiones",
        )
        if leading == "target" and self.contains_any_cue(normalized, expressive_emergence_cues):
            if any(variant in normalized for variant in owner_variants):
                return ("emergesFrom", target, owner)

        development_cues = (
            "desarrolla",
            "desarrollan",
            "desarrollarse",
            "profundizacion",
            "amplia",
            "articula",
            "elaboracion mas compleja",
            "contribuye a la formacion",
            "contribuyen a la formacion",
            "se organiza como",
            "integra",
            "integran",
            "reorganiza",
            "refuerza",
            "estabiliza",
            "permite",
        )
        if self.contains_any_cue(normalized, development_cues):
            if leading == "target":
                return ("develops", target, owner)
            return ("develops", owner, target)

        if relation_slug in {
            "relacion_con_la_opresion",
            "relacion_con_el_cambio_social",
            "relacion_con_la_sociedad_liberada",
            "relacion_con_la_autodefensa_frente_a_la_recaptura",
        }:
            return ("develops", owner, target)

        if relation_slug == "relacion_con_el_poder_simbolico":
            return ("grounds", target, owner)

        return ("relatedTo", owner, target)

    def add_semantic_relations_from_field(self, owner: str, field_key: str, text: str, explicit_targets: list[str] | None = None) -> None:
        for target in self.infer_related_targets(field_key, explicit_targets):
            if target == owner:
                continue
            prop, source, destination = self.infer_specific_relation(owner, target, field_key, text)
            self.add_obj(source, prop, destination)

    def add_semantic_relations_from_text(self, owner: str, field_key: str, text: str) -> None:
        ignored_keys = {"nombre", "tipo", "estado_ontologico", "estado_teorico"}
        if field_key in ignored_keys:
            return

        for target in self.infer_textual_targets(text):
            if target == owner:
                continue
            prop, source, destination = self.infer_specific_relation(owner, target, field_key, text)
            self.add_obj(source, prop, destination)

    def link_sequence_children(self, container_key: str, child_ids: list[str]) -> None:
        container_slug = slugify(container_key)
        if container_slug in SEQUENTIAL_PARENT_KEYS and len(child_ids) > 1:
            for left, right in zip(child_ids, child_ids[1:]):
                self.add_obj(left, "develops", right)
            return

        numbered = []
        for child_id in child_ids:
            match = re.match(r"nivel_(\d+)", child_id)
            if match:
                numbered.append((int(match.group(1)), child_id))
        if len(numbered) > 1:
            ordered = [child_id for _, child_id in sorted(numbered)]
            for left, right in zip(ordered, ordered[1:]):
                self.add_obj(left, "develops", right)

    def initialize_schema(self) -> None:
        level_names = {
            "fundamental": "Fundamental",
            "medio": "Medio",
            "aplicado": "Aplicado",
            "meta": "Meta",
        }
        subtype_names = {
            "entity": "Entidad",
            "process": "Proceso",
            "mechanism": "Mecanismo",
            "state": "Estado",
            "capacity": "Capacidad",
            "structure": "Estructura",
            "principle": "Principio",
            "method_subtype": "Metodo",
            "horizon": "Horizonte",
            "type_subtype": "Tipo",
            "level_subtype": "Nivel",
        }

        for identifier, name in level_names.items():
            self.ensure(identifier, "ConceptLevel")
            self.set_label(identifier, name)
            self.add_lang(identifier, "hasName", name)

        for identifier, name in subtype_names.items():
            self.ensure(identifier, "ConceptSubtype")
            self.set_label(identifier, name)
            self.add_lang(identifier, "hasName", name)

    def initialize_domains(self) -> None:
        for path in sorted(CONTENT_DIR.glob("*.json")):
            payload = self.load_payload(path)
            if self.is_canonical_payload(payload):
                domain_key = slugify(payload["domain"].get("id") or path.stem)
                domain_label = payload["domain"].get("label") or humanize(path.stem)
                json_key = payload["domain"].get("key") or path.stem
                source_path = payload["root"].get("source_path") or json_key
            else:
                domain_key = slugify(path.stem)
                domain_label = humanize(path.stem)
                json_key = path.stem
                source_path = path.stem
            self.ensure(domain_key, "Domain")
            self.set_label(domain_key, domain_label)
            self.add_lang(domain_key, "hasName", domain_label)
            self.add_string(domain_key, "jsonKey", json_key)
            self.add_string(domain_key, "hasSourceFile", path.name)
            self.add_string(domain_key, "hasSourcePath", source_path)
            self.register_aliases(domain_key, domain_key, domain_label, json_key)

    def build(self) -> None:
        self.scan_existing_ontology()
        self.scan_object_occurrences()
        self.initialize_schema()
        self.initialize_domains()

        for path in sorted(CONTENT_DIR.glob("*.json")):
            payload = self.load_payload(path)

            if self.is_canonical_payload(payload):
                domain_key = slugify(payload["domain"].get("id") or path.stem)
                self._process_canonical_root(
                    root=payload["root"],
                    domain_id=domain_key,
                    source_file=path.name,
                )
                continue

            domain_key = slugify(path.stem)
            root_key = next(iter(payload))
            root_value = payload[root_key]

            if isinstance(root_value, dict):
                self._process_mapping(
                    mapping=root_value,
                    domain_id=domain_key,
                    source_file=path.name,
                    path_parts=(root_key,),
                    structural_parent=domain_key,
                    concept_anchor=None,
                )
            elif isinstance(root_value, list):
                self._process_array(
                    key=root_key,
                    values=root_value,
                    domain_id=domain_key,
                    source_file=path.name,
                    path_parts=(root_key,),
                    structural_parent=domain_key,
                    concept_anchor=None,
                )

        self._build_system_individuals()
        self._apply_legacy_enrichment()

    def _build_system_individuals(self) -> None:
        path = CONTENT_DIR / "sistema_filosofico.json"
        if not path.exists():
            return

        payload = self.load_payload(path)
        if self.is_canonical_payload(payload):
            root = payload["root"]
            nombre_completo_field = self.canonical_field_entry(root, "nombre_completo")
            nombre_doctrinal_field = self.canonical_field_entry(root, "nombre_doctrinal")
            descripcion_general_field = self.canonical_field_entry(root, "descripcion_general")
            estado_de_desarrollo_field = self.canonical_field_entry(root, "estado_de_desarrollo")

            nombre_completo = nombre_completo_field["value"]
            nombre_doctrinal = nombre_doctrinal_field["value"]
            descripcion_general = descripcion_general_field["value"] if descripcion_general_field else ""
            estado_de_desarrollo = estado_de_desarrollo_field["value"] if estado_de_desarrollo_field else ""
            system_source_path = root.get("source_path", "sistema_filosofico")
            doctrine_source_path = (
                nombre_doctrinal_field["source_path"]
                if nombre_doctrinal_field
                else "sistema_filosofico.nombre_doctrinal"
            )
        else:
            data = payload["sistema_filosofico"]
            nombre_completo = data["nombre_completo"]
            nombre_doctrinal = data["nombre_doctrinal"]
            descripcion_general = data.get("descripcion_general", "")
            estado_de_desarrollo = data.get("estado_de_desarrollo", "")
            system_source_path = "sistema_filosofico"
            doctrine_source_path = "sistema_filosofico.nombre_doctrinal"

        system_id = slugify(nombre_completo)
        doctrine_id = slugify(nombre_doctrinal)

        self.ensure(system_id, "System")
        self.set_label(system_id, nombre_completo)
        self.add_lang(system_id, "hasName", nombre_completo)
        self.add_lang(system_id, "hasDescription", descripcion_general)
        self.add_field_text(system_id, "estado_de_desarrollo", str(estado_de_desarrollo))
        self.register_domain_membership(system_id, "sistema_filosofico", path.name, system_source_path)
        self.add_obj("sistema_filosofico", "hasPart", system_id)
        self.add_obj(system_id, "partOf", "sistema_filosofico")

        self.ensure(doctrine_id, "Concept")
        self.set_label(doctrine_id, nombre_doctrinal)
        self.add_lang(doctrine_id, "hasName", nombre_doctrinal)
        self.add_lang(doctrine_id, "hasDescription", descripcion_general)
        self.register_domain_membership(doctrine_id, "sistema_filosofico", path.name, doctrine_source_path)
        self.add_obj(system_id, "hasPart", doctrine_id)
        self.add_obj(system_id, "hasConcept", doctrine_id)
        self.add_obj(doctrine_id, "partOf", system_id)

        exergia_path = CONTENT_DIR / "teoria_de_la_exergia.json"
        if exergia_path.exists():
            exergia_payload = self.load_payload(exergia_path)
            if self.is_canonical_payload(exergia_payload):
                exergia_root = exergia_payload["root"]
                family = self.canonical_child_entry(exergia_root, "familia_lexica")
                definition_field = self.canonical_field_entry(family, "definicion_del_exergismo")
                definition = definition_field["value"] if definition_field else None
                definition_source_path = (
                    definition_field["source_path"]
                    if definition_field
                    else "teoria_de_la_exergia.familia_lexica.definicion_del_exergismo"
                )

                definicion_general = self.canonical_child_entry(exergia_root, "definicion_general")
                definicion_filosofica_field = self.canonical_field_entry(definicion_general, "definicion_filosofica")
                funcion_en_el_sistema_field = self.canonical_field_entry(definicion_general, "funcion_en_el_sistema")
                exergia_definition = definicion_filosofica_field["value"] if definicion_filosofica_field else ""
                exergia_description = funcion_en_el_sistema_field["value"] if funcion_en_el_sistema_field else ""
                exergia_source_path = (
                    definicion_general.get("source_path")
                    if definicion_general
                    else "teoria_de_la_exergia.definicion_general"
                )
            else:
                exergia_data = exergia_payload["teoria_de_la_exergia"]
                family = exergia_data.get("familia_lexica", {})
                definition = family.get("definicion_del_exergismo")
                definition_source_path = "teoria_de_la_exergia.familia_lexica.definicion_del_exergismo"
                exergia_definition = exergia_data["definicion_general"].get("definicion_filosofica", "")
                exergia_description = exergia_data["definicion_general"].get("funcion_en_el_sistema", "")
                exergia_source_path = "teoria_de_la_exergia.definicion_general"

            if definition:
                self.add_lang(doctrine_id, "hasDefinition", definition)
                self.add_field_text(doctrine_id, "definicion_del_exergismo", definition)
                self.register_domain_membership(
                    doctrine_id,
                    "teoria_de_la_exergia",
                    exergia_path.name,
                    definition_source_path,
                )

            exergia_concept = self.ensure("exergia", "Concept")
            self.set_label("exergia", "Exergia")
            self.add_lang("exergia", "hasName", "Exergia")
            self.add_lang("exergia", "hasDefinition", exergia_definition)
            self.add_lang("exergia", "hasDescription", exergia_description)
            self.register_domain_membership("exergia", "teoria_de_la_exergia", exergia_path.name, exergia_source_path)

    def _process_canonical_root(self, root: dict, domain_id: str, source_file: str) -> None:
        root_key = root.get("key", domain_id)
        root_kind = root.get("kind")
        root_id = domain_id
        structural_parent = domain_id
        concept_anchor = None

        if root_kind == "concept":
            root_id = slugify(root.get("canonical_id") or root.get("id") or domain_id)
            self.ensure(root_id, "Concept")
            self.set_label(root_id, root.get("label") or humanize(root_key))
            self.add_lang(root_id, "hasName", root.get("label") or humanize(root_key))
            self.add_string(root_id, "jsonKey", root_key)
            self.register_domain_membership(root_id, domain_id, source_file, root.get("source_path", root_key))
            self.register_aliases(root_id, root.get("canonical_id", ""), root.get("label", ""), root_key, *(root.get("aliases", []) or []))
            if root_id != domain_id:
                self.add_obj(domain_id, "hasPart", root_id)
                self.add_obj(root_id, "partOf", domain_id)
            structural_parent = root_id
            concept_anchor = root_id
        elif root_kind == "system":
            root_id = slugify(root.get("canonical_id") or root.get("id") or domain_id)
            self.ensure(root_id, "System")
            self.set_label(root_id, root.get("label") or humanize(root_key))
            self.add_lang(root_id, "hasName", root.get("label") or humanize(root_key))
            self.add_string(root_id, "jsonKey", root_key)
            self.register_domain_membership(root_id, domain_id, source_file, root.get("source_path", root_key))
            self.register_aliases(root_id, root.get("canonical_id", ""), root.get("label", ""), root_key, *(root.get("aliases", []) or []))
            if root_id != domain_id:
                self.add_obj(domain_id, "hasPart", root_id)
                self.add_obj(root_id, "partOf", domain_id)
            structural_parent = root_id

        child_nodes: list[str] = []

        for child in root.get("children", []):
            child_id = self._process_canonical_node(
                node=child,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=structural_parent,
                concept_anchor=concept_anchor,
            )
            child_nodes.append(child_id)

        for collection in root.get("collections", []):
            self._process_canonical_collection(
                collection=collection,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=structural_parent,
                concept_anchor=concept_anchor,
            )

        for field in root.get("fields", []):
            self._process_canonical_field(
                field=field,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=structural_parent,
                concept_anchor=concept_anchor,
            )

        self.link_sequence_children(root_key, child_nodes)

    def _process_canonical_node(
        self,
        node: dict,
        domain_id: str,
        source_file: str,
        structural_parent: str,
        concept_anchor: str | None,
    ) -> str:
        path_parts = self.canonical_path_parts(node.get("source_path", ""))
        node_key = node["key"]
        is_concept = node.get("kind") == "concept"
        node_id = slugify(node.get("canonical_id") or node["id"])
        node_types = ["Concept"] if is_concept else ["Section"]

        self.ensure(node_id, *node_types)
        self.set_label(node_id, node.get("label") or humanize(node_key))
        self.add_lang(node_id, "hasName", node.get("label") or humanize(node_key))
        self.add_string(node_id, "jsonKey", node_key)
        self.register_domain_membership(node_id, domain_id, source_file, node.get("source_path", ""))
        self.register_aliases(
            node_id,
            node.get("canonical_id", ""),
            node.get("label", ""),
            node_key,
            *(node.get("aliases", []) or []),
        )

        self.add_obj(structural_parent, "hasPart", node_id)
        self.add_obj(node_id, "partOf", structural_parent)

        next_anchor = concept_anchor
        if is_concept:
            concept_ref = node.get("concept_ref")
            if concept_ref:
                canonical_target = self.resolve_identifier(concept_ref) or self.ensure_concept_anchor(
                    slugify(concept_ref),
                    humanize(concept_ref),
                )
                if canonical_target != node_id:
                    self.add_obj(node_id, "belongsToConcept", canonical_target)
                    self.add_obj(canonical_target, "hasConcept", node_id)
            if concept_anchor is not None and concept_anchor != node_id:
                self.add_obj(node_id, "belongsToConcept", concept_anchor)
                self.add_obj(concept_anchor, "hasConcept", node_id)
            next_anchor = node_id
        elif node_key not in PASS_THROUGH_SECTION_KEYS:
            next_anchor = concept_anchor

        special_anchor = SPECIAL_SECTION_CONCEPT_ANCHORS.get(slugify(node_key))
        if special_anchor:
            next_anchor = special_anchor

        self.apply_contextual_semantics(node_id, path_parts, concept_anchor)

        child_nodes: list[str] = []
        for child in node.get("children", []):
            child_id = self._process_canonical_node(
                node=child,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=node_id,
                concept_anchor=next_anchor,
            )
            child_nodes.append(child_id)

        for collection in node.get("collections", []):
            self._process_canonical_collection(
                collection=collection,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=node_id,
                concept_anchor=next_anchor,
            )

        for field in node.get("fields", []):
            self._process_canonical_field(
                field=field,
                domain_id=domain_id,
                source_file=source_file,
                structural_parent=node_id,
                concept_anchor=next_anchor,
            )

        self.link_sequence_children(path_parts[-1] if path_parts else "", child_nodes)
        return node_id

    def _process_canonical_field(
        self,
        field: dict,
        domain_id: str,
        source_file: str,
        structural_parent: str,
        concept_anchor: str | None,
    ) -> None:
        path_parts = self.canonical_path_parts(field.get("source_path", field["key"]))
        self._process_scalar(
            key=field["key"],
            value=self.canonical_string_value(field.get("value")),
            domain_id=domain_id,
            source_file=source_file,
            path_parts=path_parts,
            structural_parent=structural_parent,
            concept_anchor=concept_anchor,
            explicit_targets=[str(target) for target in field.get("target_ids", [])],
        )

    def _process_canonical_collection(
        self,
        collection: dict,
        domain_id: str,
        source_file: str,
        structural_parent: str,
        concept_anchor: str | None,
    ) -> None:
        path_parts = self.canonical_path_parts(collection.get("source_path", collection["key"]))
        values = [
            item.get("value")
            for item in sorted(collection.get("items", []), key=lambda entry: entry.get("order_index", 0))
        ]
        self._process_array(
            key=collection["key"],
            values=values,
            domain_id=domain_id,
            source_file=source_file,
            path_parts=path_parts,
            structural_parent=structural_parent,
            concept_anchor=concept_anchor,
        )

    def _apply_legacy_enrichment(self) -> None:
        for subject, predicates in self.old_enrichments.items():
            if subject not in self.individuals:
                continue
            for prop, targets in predicates.items():
                for target in targets:
                    if target in self.individuals:
                        self.add_obj(subject, prop, target)

    def _process_mapping(
        self,
        mapping: dict,
        domain_id: str,
        source_file: str,
        path_parts: tuple[str, ...],
        structural_parent: str,
        concept_anchor: str | None,
    ) -> None:
        child_nodes: list[str] = []
        for key, value in mapping.items():
            current_path = path_parts + (key,)
            current_source_path = ".".join(current_path)

            if isinstance(value, dict):
                node_id = self.choose_node_id(domain_id, current_path, value)
                node_types = ["Concept"] if self.is_concept_like(key, value) else ["Section"]
                self.ensure(node_id, *node_types)
                self.set_label(node_id, humanize(key))
                self.add_lang(node_id, "hasName", humanize(key))
                self.add_string(node_id, "jsonKey", key)
                self.register_domain_membership(node_id, domain_id, source_file, current_source_path)

                self.add_obj(structural_parent, "hasPart", node_id)
                self.add_obj(node_id, "partOf", structural_parent)

                next_anchor = concept_anchor
                if "Concept" in self.ensure(node_id).types:
                    if concept_anchor is not None and concept_anchor != node_id:
                        self.add_obj(node_id, "belongsToConcept", concept_anchor)
                        self.add_obj(concept_anchor, "hasConcept", node_id)
                    next_anchor = node_id
                elif key not in PASS_THROUGH_SECTION_KEYS:
                    next_anchor = concept_anchor

                special_anchor = SPECIAL_SECTION_CONCEPT_ANCHORS.get(slugify(key))
                if special_anchor:
                    next_anchor = special_anchor

                self.apply_contextual_semantics(node_id, current_path, concept_anchor)
                child_nodes.append(node_id)

                self._process_mapping(
                    mapping=value,
                    domain_id=domain_id,
                    source_file=source_file,
                    path_parts=current_path,
                    structural_parent=node_id,
                    concept_anchor=next_anchor,
                )
                continue

            if isinstance(value, list):
                self._process_array(
                    key=key,
                    values=value,
                    domain_id=domain_id,
                    source_file=source_file,
                    path_parts=current_path,
                    structural_parent=structural_parent,
                    concept_anchor=concept_anchor,
                )
                continue

            parent_key = path_parts[-1] if path_parts else ""
            if self.should_materialize_scalar_node(parent_key, key, str(value)):
                node_id = self.choose_scalar_node_id(domain_id, path_parts, key)
                self.ensure(node_id, "Concept")
                self.set_label(node_id, humanize(key))
                self.add_lang(node_id, "hasName", humanize(key))
                self.add_lang(node_id, "hasDefinition", str(value))
                self.add_string(node_id, "jsonKey", key)
                self.register_domain_membership(node_id, domain_id, source_file, current_source_path)
                self.add_obj(structural_parent, "hasPart", node_id)
                self.add_obj(node_id, "partOf", structural_parent)
                if concept_anchor is not None:
                    self.add_obj(node_id, "belongsToConcept", concept_anchor)
                    self.add_obj(concept_anchor, "hasConcept", node_id)
                self.apply_contextual_semantics(node_id, current_path, concept_anchor)
                child_nodes.append(node_id)
                continue

            self._process_scalar(
                key=key,
                value=str(value),
                domain_id=domain_id,
                source_file=source_file,
                path_parts=current_path,
                structural_parent=structural_parent,
                concept_anchor=concept_anchor,
            )

        self.link_sequence_children(path_parts[-1] if path_parts else "", child_nodes)

    def _process_scalar(
        self,
        key: str,
        value: str,
        domain_id: str,
        source_file: str,
        path_parts: tuple[str, ...],
        structural_parent: str,
        concept_anchor: str | None,
        explicit_targets: list[str] | None = None,
    ) -> None:
        source_path = ".".join(path_parts)
        owner = structural_parent

        if key.startswith("tesis"):
            thesis_id = self.scoped_id(domain_id, path_parts)
            self.ensure(thesis_id, "Thesis")
            self.set_label(thesis_id, humanize(key))
            self.add_lang(thesis_id, "hasName", humanize(key))
            self.add_lang(thesis_id, "hasText", value)
            self.add_string(thesis_id, "jsonKey", key)
            self.register_domain_membership(thesis_id, domain_id, source_file, source_path)
            self.add_obj(owner, "hasThesis", thesis_id)
            self.add_obj(owner, "hasPart", thesis_id)
            self.add_obj(thesis_id, "partOf", owner)
            if concept_anchor is not None:
                self.add_obj(thesis_id, "grounds", concept_anchor)
            return

        if key.startswith("pregunta"):
            question_id = self.scoped_id(domain_id, path_parts)
            self.ensure(question_id, "Question")
            self.set_label(question_id, humanize(key))
            self.add_lang(question_id, "hasName", humanize(key))
            self.add_lang(question_id, "hasText", value)
            self.add_string(question_id, "jsonKey", key)
            self.register_domain_membership(question_id, domain_id, source_file, source_path)
            self.add_obj(owner, "hasQuestion", question_id)
            self.add_obj(owner, "hasPart", question_id)
            self.add_obj(question_id, "partOf", owner)
            return

        core_prop = CORE_FIELD_MAP.get(key)
        if core_prop:
            self.add_lang(owner, core_prop, value)
            self.add_field_text(owner, key, value)
            if key == "nombre":
                self.set_label(owner, value)
        else:
            self.add_field_text(owner, key, value)

        self.add_semantic_relations_from_field(owner, key, value, explicit_targets)
        self.add_semantic_relations_from_text(owner, key, value)

    def _process_array(
        self,
        key: str,
        values: list,
        domain_id: str,
        source_file: str,
        path_parts: tuple[str, ...],
        structural_parent: str,
        concept_anchor: str | None,
    ) -> None:
        source_path = ".".join(path_parts)
        lower_key = slugify(key)

        if source_path == "axiomas_provisionales":
            for index, item in enumerate(values, start=1):
                axiom_id = f"axioma_provisional_{index:02d}"
                self.ensure(axiom_id, "Axiom")
                self.set_label(axiom_id, f"Axioma provisional {index:02d}")
                self.add_lang(axiom_id, "hasName", f"Axioma provisional {index:02d}")
                self.add_lang(axiom_id, "hasText", str(item))
                self.add_int(axiom_id, "orderIndex", index)
                self.add_string(axiom_id, "jsonKey", "axiomas_provisionales")
                self.register_domain_membership(axiom_id, domain_id, source_file, f"{source_path}[{index - 1}]")
                self.add_obj(domain_id, "hasAxiom", axiom_id)
                self.add_obj(domain_id, "hasPart", axiom_id)
                self.add_obj(axiom_id, "partOf", domain_id)
            return

        if source_path == "preguntas_abiertas":
            for index, item in enumerate(values, start=1):
                question_id = f"pregunta_abierta_{index:02d}"
                self.ensure(question_id, "Question")
                self.set_label(question_id, f"Pregunta abierta {index:02d}")
                self.add_lang(question_id, "hasName", f"Pregunta abierta {index:02d}")
                self.add_lang(question_id, "hasText", str(item))
                self.add_int(question_id, "orderIndex", index)
                self.add_string(question_id, "jsonKey", "preguntas_abiertas")
                self.register_domain_membership(question_id, domain_id, source_file, f"{source_path}[{index - 1}]")
                self.add_obj(domain_id, "hasQuestion", question_id)
                self.add_obj(domain_id, "hasPart", question_id)
                self.add_obj(question_id, "partOf", domain_id)
            return

        collection_id = self.scoped_id(domain_id, path_parts, "collection")
        self.ensure(collection_id, "Collection")
        self.set_label(collection_id, humanize(key))
        self.add_lang(collection_id, "hasName", humanize(key))
        self.add_string(collection_id, "jsonKey", key)
        self.register_domain_membership(collection_id, domain_id, source_file, source_path)
        self.add_obj(structural_parent, "hasPart", collection_id)
        self.add_obj(collection_id, "partOf", structural_parent)

        item_class = "CollectionItem"
        link_prop = "hasCollectionItem"
        if "axioma" in lower_key:
            item_class = "Axiom"
            link_prop = "hasAxiom"
        elif "pregunta" in lower_key:
            item_class = "Question"
            link_prop = "hasQuestion"

        for index, item in enumerate(values, start=1):
            item_id = self.scoped_id(domain_id, path_parts, f"item_{index:02d}")
            self.ensure(item_id, item_class)
            self.set_label(item_id, truncate_label(str(item)))
            self.add_lang(item_id, "hasText", str(item))
            self.add_int(item_id, "orderIndex", index)
            self.add_string(item_id, "jsonKey", key)
            self.register_domain_membership(item_id, domain_id, source_file, f"{source_path}[{index - 1}]")
            self.add_obj(collection_id, link_prop, item_id)
            self.add_obj(collection_id, "hasPart", item_id)
            self.add_obj(item_id, "partOf", collection_id)

    def render(self) -> str:
        return self.render_rdfxml()

    def render_rdfxml(self) -> str:
        object_properties = [
            ("hasPart", "owl:Thing", "owl:Thing"),
            ("partOf", "owl:Thing", "owl:Thing"),
            ("hasConcept", "owl:Thing", "Concept"),
            ("belongsToConcept", "owl:Thing", "Concept"),
            ("hasDomain", "owl:Thing", "Domain"),
            ("belongsToDomain", "owl:Thing", "Domain"),
            ("appearsIn", "owl:Thing", "Domain"),
            ("hasThesis", "owl:Thing", "Thesis"),
            ("hasAxiom", "owl:Thing", "Axiom"),
            ("hasQuestion", "owl:Thing", "Question"),
            ("hasCollectionItem", "Collection", "CollectionItem"),
            ("hasLevel", "Concept", "ConceptLevel"),
            ("hasSubtype", "Concept", "ConceptSubtype"),
            ("relatedTo", "owl:Thing", "owl:Thing"),
            ("emergesFrom", "owl:Thing", "owl:Thing"),
            ("grounds", "owl:Thing", "owl:Thing"),
            ("opposes", "owl:Thing", "owl:Thing"),
            ("develops", "owl:Thing", "owl:Thing"),
        ]

        core_datatype_properties = [
            ("hasName", "owl:Thing", "rdf:langString"),
            ("hasDefinition", "owl:Thing", "rdf:langString"),
            ("hasDescription", "owl:Thing", "rdf:langString"),
            ("hasText", "owl:Thing", "rdf:langString"),
            ("hasTheoreticalStatus", "owl:Thing", "rdf:langString"),
            ("hasOntologicalStatus", "owl:Thing", "rdf:langString"),
            ("jsonKey", "owl:Thing", "xsd:string"),
            ("hasSourceFile", "owl:Thing", "xsd:string"),
            ("hasSourcePath", "owl:Thing", "xsd:string"),
            ("orderIndex", "owl:Thing", "xsd:integer"),
        ]

        lines = [
            '<?xml version="1.0"?>',
            '<rdf:RDF',
            f'  xml:base="{BASE_IRI}"',
            f'  xmlns="{BASE_IRI}"',
            '  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"',
            '  xmlns:owl="http://www.w3.org/2002/07/owl#"',
            '  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"',
            '  xmlns:xsd="http://www.w3.org/2001/XMLSchema#">',
            "",
            f'  <owl:Ontology rdf:about="{BASE_IRI}"/>',
            "",
        ]

        for prop, domain, range_name in object_properties:
            lines.extend(
                [
                    f'  <owl:ObjectProperty rdf:about="{BASE_IRI}{prop}">',
                    f'    <rdfs:label xml:lang="es">{xml_text(humanize(prop))}</rdfs:label>',
                    f'    <rdfs:domain rdf:resource="{xml_resource_uri(domain)}"/>',
                    f'    <rdfs:range rdf:resource="{xml_resource_uri(range_name)}"/>',
                    "  </owl:ObjectProperty>",
                    "",
                ]
            )

        lines.extend(
            [
                f'  <owl:ObjectProperty rdf:about="{BASE_IRI}hasPart">',
                f'    <owl:inverseOf rdf:resource="{BASE_IRI}partOf"/>',
                "  </owl:ObjectProperty>",
                "",
            ]
        )

        for prop, domain, range_name in core_datatype_properties:
            lines.extend(
                [
                    f'  <owl:DatatypeProperty rdf:about="{BASE_IRI}{prop}">',
                    f'    <rdfs:label xml:lang="es">{xml_text(humanize(prop))}</rdfs:label>',
                    f'    <rdfs:domain rdf:resource="{xml_resource_uri(domain)}"/>',
                    f'    <rdfs:range rdf:resource="{xml_resource_uri(range_name, default_base="")}"/>',
                    "  </owl:DatatypeProperty>",
                    "",
                ]
            )

        for prop, label in sorted(self.dynamic_datatype_properties.items()):
            lines.extend(
                [
                    f'  <owl:DatatypeProperty rdf:about="{BASE_IRI}{prop}">',
                    f'    <rdfs:label xml:lang="es">{xml_text(label)}</rdfs:label>',
                    '    <rdfs:domain rdf:resource="http://www.w3.org/2002/07/owl#Thing"/>',
                    '    <rdfs:range rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#langString"/>',
                    "  </owl:DatatypeProperty>",
                    "",
                ]
            )

        for class_name in [
            "OntologyNode",
            "Domain",
            "System",
            "Concept",
            "Section",
            "Thesis",
            "Axiom",
            "Question",
            "Collection",
            "CollectionItem",
            "ConceptLevel",
            "ConceptSubtype",
        ]:
            lines.extend(
                [
                    f'  <owl:Class rdf:about="{BASE_IRI}{class_name}"/>',
                    "",
                ]
            )

        subclass_pairs = [
            ("Domain", "OntologyNode"),
            ("System", "OntologyNode"),
            ("Concept", "OntologyNode"),
            ("Section", "OntologyNode"),
            ("Thesis", "OntologyNode"),
            ("Axiom", "OntologyNode"),
            ("Question", "OntologyNode"),
            ("Collection", "OntologyNode"),
            ("CollectionItem", "OntologyNode"),
            ("ConceptLevel", "Concept"),
            ("ConceptSubtype", "Concept"),
        ]

        for child, parent in subclass_pairs:
            lines.extend(
                [
                    f'  <owl:Class rdf:about="{BASE_IRI}{child}">',
                    f'    <rdfs:subClassOf rdf:resource="{BASE_IRI}{parent}"/>',
                    "  </owl:Class>",
                    "",
                ]
            )

        for identifier in self.sorted_individual_ids():
            node = self.individuals[identifier]
            lines.append(f'  <owl:NamedIndividual rdf:about="{BASE_IRI}{identifier}">')
            lines.append('    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>')
            for class_name in node.types:
                lines.append(f'    <rdf:type rdf:resource="{BASE_IRI}{class_name}"/>')
            if node.label:
                lines.append(f'    <rdfs:label xml:lang="es">{xml_text(node.label)}</rdfs:label>')

            for prop, targets in sorted(node.object_props.items()):
                for target in targets:
                    lines.append(f'    <{prop} rdf:resource="{BASE_IRI}{target}"/>')

            for prop, values in sorted(node.data_props.items()):
                for kind, value in values:
                    if kind == "lang":
                        lines.append(f'    <{prop} xml:lang="es">{xml_text(str(value))}</{prop}>')
                    elif kind == "string":
                        lines.append(f'    <{prop} rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{xml_text(str(value))}</{prop}>')
                    elif kind == "int":
                        lines.append(f'    <{prop} rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{int(value)}</{prop}>')

            lines.append("  </owl:NamedIndividual>")
            lines.append("")

        lines.append("</rdf:RDF>")
        return "\n".join(lines).rstrip() + "\n"

    def sorted_individual_ids(self) -> list[str]:
        def sort_key(identifier: str) -> tuple[int, str]:
            node = self.individuals[identifier]
            priority = min(CLASS_PRIORITIES.get(class_name, 99) for class_name in node.types) if node.types else 99
            return (priority, identifier)

        return sorted(self.individuals, key=sort_key)


def main() -> None:
    cli = argparse.ArgumentParser(description="Generate ontology.owl from the philosophical JSON corpus.")
    cli.add_argument(
        "--export-canonical-dir",
        type=Path,
        help="Optional directory where the canonical JSON projection of content/ will be written before OWL generation.",
    )
    args = cli.parse_args()

    if args.export_canonical_dir is not None:
        from canonicalize_content import export_canonical_content

        export_canonical_content(CONTENT_DIR, args.export_canonical_dir)

    validate_content_corpus()

    builder = OntologyBuilder()
    builder.build()
    ONTOLOGY_PATH.write_text(builder.render(), encoding="utf-8")

    counts = Counter()
    for node in builder.individuals.values():
        for class_name in node.types:
            counts[class_name] += 1

    print(f"Wrote {ONTOLOGY_PATH}")
    for class_name in sorted(counts):
        print(f"{class_name}: {counts[class_name]}")
    print(f"Dynamic datatype properties: {len(builder.dynamic_datatype_properties)}")


if __name__ == "__main__":
    main()
