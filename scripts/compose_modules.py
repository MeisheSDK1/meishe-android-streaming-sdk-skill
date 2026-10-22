#!/usr/bin/env python3
"""Compose Meishe Android Streaming SDK modules from the skill registry.

This script is for skill use time. It reads only files bundled in the skill.
It must not read the external SdkDemo or doxygen folders.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

GENERIC_QUERY_TERMS = frozenset(
    {
        "android",
        "app",
        "application",
        "project",
        "feature",
        "features",
        "应用",
        "项目",
        "功能",
    }
)
COMPLETE_REQUEST_MARKERS = (
    "complete",
    "full",
    "all",
    "all features",
    "all capabilities",
    "完整",
    "全量",
    "全部",
    "全功能",
    "所有功能",
)
EDITOR_INTENT_MARKERS = (
    "video editor",
    "video editing",
    "editor",
    "editing",
    "edit",
    "编辑器",
    "编辑",
    "剪辑",
)
CAPTURE_INTENT_MARKERS = (
    "camera",
    "capture",
    "recording",
    "record",
    "相机",
    "拍摄",
    "录制",
    "录像",
)
MULTIPLE_BLUEPRINT_MARKERS = (
    "both",
    "multiple blueprints",
    "two blueprints",
    "both blueprints",
    "分别",
    "多个蓝图",
    "两个蓝图",
    "同时生成",
    "都生成",
)
FULL_CAPTURE_MODULE_IDS = (
    "capture-camera",
    "capture-filter",
    "capture-scene",
    "beauty-camera",
    "makeup-service",
    "ar-scene",
    "segmentation-keying",
)
EDITOR_INTENT_MODULE_IDS = frozenset(
    {
        "app-runtime",
        "permission-gates",
        "asset-package-service",
        "asset-center-service",
        "media-import",
        "app-repository",
        "timeline-state-store",
        "timeline-preview",
        "export-compile",
        "feature-hub",
        "editor-shell",
        "editor-ui-shell",
        "clip-editor",
        "filter-editor",
        "caption-editor",
        "compound-caption-editor",
        "sticker-editor",
        "transition-editor",
        "music-editor",
        "voiceover-editor",
        "mask-editor",
        "background-editor",
        "watermark-editor",
        "animation-editor",
        "particle-effects",
        "flip-caption",
        "cover-maker",
        "livephoto-editor",
        "audio-equalizer",
        "timeline-ui",
        "still-image-export",
        "effect-parameter-models",
    }
)
CAPTURE_INTENT_MODULE_IDS = frozenset(
    {
        "app-runtime",
        "permission-gates",
        "asset-package-service",
        "asset-center-service",
        "feature-hub",
        *FULL_CAPTURE_MODULE_IDS,
        "glitter-effects",
    }
)

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="", help="Natural-language feature/app request.")
    parser.add_argument("--modules", default="", help="Comma/space-separated module ids to compose.")
    parser.add_argument("--blueprint", default="", help="Comma/space-separated app blueprint ids.")
    parser.add_argument(
        "--mode",
        default="new-app",
        choices=["new-app", "incremental", "api-only"],
        help="Composition mode.",
    )
    parser.add_argument("--limit", type=int, default=8, help="Maximum query matches to use per kind.")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--list", action="store_true", dest="list_items")
    parser.add_argument("--compact", action="store_true", help="Omit long simple-code id and call-order listings; keep routing fields.")
    return parser.parse_args()

def skill_dir():
    return Path(__file__).resolve().parents[1]

@lru_cache(maxsize=None)
def load_json(relative_path):
    with (skill_dir() / relative_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)

def split_names(value):
    return [item for item in re.split(r"[\s,\uFF0C\u3001;|]+", value.strip()) if item]

def normalize(value):
    return str(value).casefold()


def phrase_in_query(query, phrase):
    normalized_query = normalize(query)
    normalized_phrase = normalize(phrase).strip()
    if not normalized_phrase:
        return False
    if re.search(r"[\u3400-\u9fff]", normalized_phrase):
        return normalized_phrase in normalized_query
    return (
        re.search(
            rf"(?<![\w]){re.escape(normalized_phrase)}(?![\w])",
            normalized_query,
        )
        is not None
    )


def has_any_phrase(query, phrases):
    return any(phrase_in_query(query, phrase) for phrase in phrases)


def broad_product_intent(query):
    if not query or not has_any_phrase(query, COMPLETE_REQUEST_MARKERS):
        return ""
    has_editor_intent = has_any_phrase(query, EDITOR_INTENT_MARKERS)
    has_capture_intent = has_any_phrase(query, CAPTURE_INTENT_MARKERS)
    if has_editor_intent and has_capture_intent:
        return "capture-editor"
    if has_editor_intent:
        return "editor"
    if has_capture_intent:
        return "capture"
    return ""


def query_named_blueprints(query, blueprints):
    named_ids = []
    for blueprint in blueprints:
        names = [blueprint.get("id", ""), *blueprint.get("aliases", [])]
        if any(phrase_in_query(query, name) for name in names if name):
            named_ids.append(blueprint["id"])
    return named_ids


def explicitly_requests_multiple_blueprints(query):
    return has_any_phrase(query, MULTIPLE_BLUEPRINT_MARKERS)


def blueprint_supports_mode(blueprint, mode):
    integration_modes = blueprint.get("integration_modes", [])
    return not integration_modes or mode in integration_modes


def select_blueprints(
    query,
    mode,
    explicit_blueprints,
    blueprints,
    lookup_candidates,
    registry_candidates,
    product_intent,
):
    blueprint_index = index_by_id(blueprints)
    if mode == "incremental":
        return ["incremental-integration"]
    if explicit_blueprints:
        return ordered_unique(explicit_blueprints)
    if mode == "api-only":
        return []

    named_blueprints = [
        blueprint_id
        for blueprint_id in query_named_blueprints(query, blueprints)
        if blueprint_id in blueprint_index
        and blueprint_supports_mode(blueprint_index[blueprint_id], mode)
    ]
    if named_blueprints:
        named_blueprints = ordered_unique(named_blueprints)
        if len(named_blueprints) > 1 and explicitly_requests_multiple_blueprints(
            query
        ):
            return named_blueprints
        return named_blueprints[:1]

    intent_blueprints = {
        "editor": "short-video-editor",
        "capture": "beauty-camera",
        "capture-editor": "camera-plus-editor",
    }
    intent_blueprint = intent_blueprints.get(product_intent)
    if intent_blueprint:
        return [intent_blueprint]

    candidate_scores = {}
    for score, blueprint_id in [*lookup_candidates, *registry_candidates]:
        blueprint = blueprint_index.get(blueprint_id)
        if blueprint is None or not blueprint_supports_mode(blueprint, mode):
            continue
        candidate_scores[blueprint_id] = max(
            score, candidate_scores.get(blueprint_id, 0)
        )
    if not candidate_scores:
        return []
    primary_blueprint = min(
        candidate_scores,
        key=lambda blueprint_id: (-candidate_scores[blueprint_id], blueprint_id),
    )
    return [primary_blueprint]


def constrain_inferred_modules(module_ids, product_intent):
    if product_intent == "editor":
        allowed_module_ids = EDITOR_INTENT_MODULE_IDS
    elif product_intent == "capture":
        allowed_module_ids = CAPTURE_INTENT_MODULE_IDS
    elif product_intent == "capture-editor":
        allowed_module_ids = EDITOR_INTENT_MODULE_IDS | CAPTURE_INTENT_MODULE_IDS
    else:
        return module_ids
    return [
        module_id for module_id in module_ids if module_id in allowed_module_ids
    ]


def text_fields(item):
    fields = [item.get("id", ""), item.get("title", ""), item.get("category", "")]
    fields.extend(item.get("aliases", []))
    fields.extend(item.get("resources", []))
    fields.extend(item.get("template_features", []))
    fields.extend(item.get("simple_code_refs", []))
    fields.extend(item.get("simple_code_ids", []))
    fields.extend(item.get("api_recipes", []))
    return [normalize(field) for field in fields if field]

def split_query(query):
    return [
        term.casefold()
        for term in re.split(r"[\s,，、|;:：()\[\]{}<>]+", query)
        if term.strip()
    ]

def score_item(query, item):
    query = normalize(query.strip())
    terms = [
        term for term in split_query(query) if term not in GENERIC_QUERY_TERMS
    ]
    fields = text_fields(item)
    joined = " ".join(fields)
    score = 0
    if query and query not in GENERIC_QUERY_TERMS and query in joined:
        score += 60
    for term in terms:
        for field in fields:
            if term == field:
                score += 24
            elif term in field:
                score += 10
            elif field in term and len(field) > 1:
                score += 24
    return score

def split_query(query):
    return [
        term.casefold()
        for term in re.split(r"[\s,\uFF0C\u3001|;:\uFF1A()\uFF08\uFF09\[\]{}<>]+", query)
        if term.strip()
    ]

def index_by_id(items):
    return {item["id"]: item for item in items}

def ordered_unique(values):
    result = []
    seen = set()
    for value in values:
        if value and value not in seen:
            result.append(value)
            seen.add(value)
    return result

def expand_and_sort_units(unit_ids, unit_index, warnings):
    selected = []
    selected_ids = set()

    def add_with_dependencies(unit_id):
        if unit_id in selected_ids:
            return
        unit = unit_index.get(unit_id)
        if unit is None:
            warnings.append(f"Unknown simple code id: {unit_id}")
            return
        for dependency_id in unit.get("compose_after_units", []):
            if dependency_id not in unit_index:
                warnings.append(f"Dangling compose_after_units reference: {unit_id} -> {dependency_id}")
                continue
            add_with_dependencies(dependency_id)
        selected_ids.add(unit_id)
        selected.append(unit)

    for unit_id in ordered_unique(unit_ids):
        add_with_dependencies(unit_id)

    ordered = []
    permanent = set()
    active = []

    def visit(unit):
        unit_id = unit["id"]
        if unit_id in permanent:
            return
        if unit_id in active:
            cycle = active[active.index(unit_id):] + [unit_id]
            warnings.append("Cyclic compose_after_units dependency: " + " -> ".join(cycle))
            return
        active.append(unit_id)
        for dependency_id in unit.get("compose_after_units", []):
            dependency = unit_index.get(dependency_id)
            if dependency is None:
                warnings.append(f"Dangling compose_after_units reference: {unit_id} -> {dependency_id}")
                continue
            if dependency_id in selected_ids:
                visit(dependency)
        active.pop()
        permanent.add(unit_id)
        ordered.append(unit)

    for unit in selected:
        visit(unit)
    return ordered

def load_lookup_entries():
    path = skill_dir() / "references" / "skill-lookup-index.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle).get("entries", [])

def lookup_matches(query, limit):
    if not query:
        return []
    entries = load_lookup_entries()
    scored = [(score_item(query, entry), entry) for entry in entries]
    scored = [(score, entry) for score, entry in scored if score > 0]
    scored.sort(key=lambda value: (-value[0], value[1]["id"]))
    return scored[:limit]

def registry_matches(query, items, limit):
    if not query:
        return []
    scored = [(score_item(query, item), item) for item in items]
    scored = [(score, item) for score, item in scored if score > 0]
    scored.sort(key=lambda value: (-value[0], value[1]["id"]))
    return scored[:limit]

@lru_cache(maxsize=None)
def _member_boundary_pattern(member):
    return re.compile(rf"(?<![\w.]){re.escape(member)}(?![\w.])")


def api_matches(query, limit):
    if not query:
        return []
    api_map = load_json("references/demo-api-simple-code-map.json")
    normalized_query = normalize(query)
    terms = [
        term for term in split_query(query) if term not in GENERIC_QUERY_TERMS
    ]
    matches = []
    exact_matches = []
    for api in api_map.get("api_members", []):
        member = normalize(api.get("member", ""))
        stable_id = normalize(api.get("stable_id", ""))
        owner = member.split(".", 1)[0]
        score = 0
        if stable_id and normalized_query == stable_id:
            score = 120
            exact_matches.append((score, api))
        elif member and (
            normalized_query == member
            or _member_boundary_pattern(member).search(normalized_query) is not None
        ):
            score = 100
            exact_matches.append((score, api))
        elif owner and owner in normalized_query:
            score = 55
        elif any(len(term) >= 3 and term in member for term in terms):
            score = 35
        if score:
            matches.append((score, api))
    if exact_matches:
        exact_matches.sort(
            key=lambda value: (-value[0], value[1].get("stable_id", value[1]["member"]))
        )
        return exact_matches[:limit]
    matches.sort(key=lambda value: (-value[0], value[1]["member"]))
    return matches[:limit]

def direct_api_unit_ids(api, simple_unit_index, exact_api_only=False):
    unit_ids = api.get("simple_code_ids", [])
    if not exact_api_only:
        return unit_ids

    member = api.get("member", "")
    stable_id = api.get("stable_id", "")
    signature_unit_ids = [
        unit_id
        for unit_id in unit_ids
        if simple_unit_index.get(unit_id, {}).get("kind") == "java_unit"
        and stable_id
        and stable_id in simple_unit_index.get(unit_id, {}).get("api_signatures", [])
    ]
    if signature_unit_ids:
        return signature_unit_ids

    java_unit_ids = [
        unit_id
        for unit_id in unit_ids
        if simple_unit_index.get(unit_id, {}).get("kind") == "java_unit"
        and member in simple_unit_index.get(unit_id, {}).get("api_members", [])
    ]
    if java_unit_ids:
        return java_unit_ids

    recipe_unit_ids = [
        unit_id
        for unit_id in unit_ids
        if not unit_id.startswith("recipe.feature.")
        and member in simple_unit_index.get(unit_id, {}).get("api_members", [])
    ]
    if recipe_unit_ids:
        return recipe_unit_ids

    return unit_ids

def compose_request(query="", modules="", blueprint="", mode="new-app", limit=8):
    lookup_blueprint_score_min = 20
    lookup_module_score_min = 30
    registry_blueprint_score_min = 20
    registry_module_score_min = 24
    registry = load_json("references/sdk-module-registry.json")
    simple_registry = load_json("references/simple-code-registry.json")
    module_index = index_by_id(registry.get("modules", []))
    recipe_index = index_by_id(registry.get("api_recipes", []))
    blueprint_index = index_by_id(registry.get("blueprints", []))
    simple_unit_index = index_by_id(simple_registry.get("units", []))

    explicit_blueprints = split_names(blueprint)
    explicit_modules = split_names(modules)
    inferred_modules = []
    match_report = {"lookup": [], "apis": [], "blueprints": [], "modules": []}
    lookup_blueprint_candidates = []
    registry_blueprint_candidates = []
    matched_simple_code_ids = []
    matched_apis = api_matches(query, limit)
    product_intent = broad_product_intent(query)
    is_exact_api_only = mode == "api-only" and any(
        score >= 100 for score, _ in matched_apis
    )

    for score, entry in ([] if is_exact_api_only else lookup_matches(query, limit)):
        match_report["lookup"].append({"id": entry["id"], "score": score})
        if score >= lookup_blueprint_score_min:
            for blueprint_id in entry.get("blueprint_ids", []):
                lookup_blueprint_candidates.append((score, blueprint_id))
        if score >= lookup_module_score_min:
            inferred_modules.extend(entry.get("module_ids", []))
        matched_simple_code_ids.extend(entry.get("simple_code_ids", []))

    for score, api in matched_apis:
        match_report["apis"].append(
            {
                "member": api["member"],
                "score": score,
                "coverage_status": api.get("coverage_status", ""),
            }
        )
        api_module_ids = [
            module_id
            for module_id in api.get("module_ids", [])
            if module_id in module_index
        ]
        if is_exact_api_only:
            # Exact API-only requests should stay at member-level scope.
            # The required call chain is recovered from compose_after_units below.
            pass
        else:
            inferred_modules.extend(api_module_ids)
        matched_simple_code_ids.extend(
            direct_api_unit_ids(api, simple_unit_index, is_exact_api_only)
        )

    for score, item in (
        [] if is_exact_api_only else registry_matches(query, registry.get("blueprints", []), limit)
    ):
        match_report["blueprints"].append({"id": item["id"], "score": score})
        if score >= registry_blueprint_score_min:
            registry_blueprint_candidates.append((score, item["id"]))

    for score, item in (
        [] if is_exact_api_only else registry_matches(query, registry.get("modules", []), limit)
    ):
        match_report["modules"].append({"id": item["id"], "score": score})
        if score >= registry_module_score_min:
            inferred_modules.append(item["id"])

    selected_blueprints = select_blueprints(
        query=query,
        mode=mode,
        explicit_blueprints=explicit_blueprints,
        blueprints=registry.get("blueprints", []),
        lookup_candidates=lookup_blueprint_candidates,
        registry_candidates=registry_blueprint_candidates,
        product_intent=product_intent,
    )
    if product_intent in {"capture", "capture-editor"}:
        inferred_modules.extend(FULL_CAPTURE_MODULE_IDS)
    selected_modules = [
        *explicit_modules,
        *constrain_inferred_modules(inferred_modules, product_intent),
    ]

    if not selected_blueprints and not selected_modules and not is_exact_api_only:
        selected_modules.append("app-runtime")

    selected_blueprints = ordered_unique(selected_blueprints)
    selected_modules = ordered_unique(selected_modules)
    warnings = []
    resolved_modules = []
    visiting = set()
    visited = set()

    def add_module(module_id):
        if module_id in visited:
            return
        if module_id in visiting:
            warnings.append(f"Cyclic dependency ignored at module: {module_id}")
            return
        module = module_index.get(module_id)
        if module is None:
            warnings.append(f"Unknown module id: {module_id}")
            return
        visiting.add(module_id)
        for required in module.get("requires", []):
            add_module(required)
        for recipe_id in module.get("api_recipes", []):
            recipe = recipe_index.get(recipe_id)
            if recipe is None:
                continue
            for required in recipe.get("requires", []):
                if required != module_id and required in module_index:
                    add_module(required)
        visiting.remove(module_id)
        visited.add(module_id)
        resolved_modules.append(module)

    resolved_blueprints = []
    for blueprint_id in selected_blueprints:
        blueprint_item = blueprint_index.get(blueprint_id)
        if blueprint_item is None:
            warnings.append(f"Unknown blueprint id: {blueprint_id}")
            continue
        resolved_blueprints.append(blueprint_item)
        for module_id in blueprint_item.get("modules", []):
            add_module(module_id)

    for module_id in selected_modules:
        add_module(module_id)

    recipes = []
    recipe_ids = []
    resources = []
    permissions = []
    template_features = []
    app_templates = []
    simple_code_refs = []
    simple_code_ids = list(matched_simple_code_ids)
    guards = []
    conflicts = []
    demo_evidence = []
    lifecycle = []

    for blueprint_item in resolved_blueprints:
        resources.extend(blueprint_item.get("resources", []))
        template_features.extend(blueprint_item.get("template_features", []))
        if blueprint_item.get("app_template"):
            app_templates.append(blueprint_item["app_template"])
        lifecycle.extend(blueprint_item.get("lifecycle", []))

    for module in resolved_modules:
        resources.extend(module.get("resources", []))
        permissions.extend(module.get("permissions", []))
        template_features.extend(module.get("template_features", []))
        simple_code_refs.extend(module.get("simple_code_refs", []))
        simple_code_ids.extend(
            module.get("render_units", module.get("simple_code_ids", []))
        )
        guards.extend(module.get("guards", []))
        conflicts.extend(module.get("conflicts", []))
        demo_evidence.extend(module.get("demo_evidence", []))
        lifecycle.extend(module.get("lifecycle", []))
        if mode not in module.get("integration_modes", []):
            warnings.append(f"Module {module['id']} does not explicitly support mode {mode}")
        recipe_ids.extend(module.get("api_recipes", []))

    recipe_ids = ordered_unique(recipe_ids)
    for recipe_id in recipe_ids:
        recipe = recipe_index.get(recipe_id)
        if recipe is None:
            warnings.append(f"Unknown API recipe id: {recipe_id}")
            continue
        recipes.append(recipe)
        resources.extend(recipe.get("resources", []))
        simple_code_refs.extend(recipe.get("simple_code_refs", []))
        simple_code_ids.extend(recipe.get("simple_code_ids", []))
        guards.extend(recipe.get("guards", []))
        conflicts.extend(recipe.get("conflicts", []))
        lifecycle.extend(recipe.get("lifecycle", []))

    resolved_simple_units = expand_and_sort_units(simple_code_ids, simple_unit_index, warnings)

    composition = {
        "query": query,
        "mode": mode,
        "independence": registry.get("independence", {}),
        "matches": match_report,
        "explicit_blueprints": explicit_blueprints,
        "explicit_modules": explicit_modules,
        "requested_blueprints": selected_blueprints,
        "requested_modules": selected_modules,
        "blueprints": [item["id"] for item in resolved_blueprints],
        "resolved_modules": [module["id"] for module in resolved_modules],
        "modules": [
            {
                "id": module["id"],
                "title": module.get("title", ""),
                "level": module.get("level", ""),
                "priority": module.get("priority", ""),
                "category": module.get("category", ""),
                "requires": module.get("requires", []),
            }
            for module in resolved_modules
        ],
        "api_recipes": [
            {
                "id": recipe["id"],
                "provides": recipe.get("provides", []),
                "requires": recipe.get("requires", []),
            }
            for recipe in recipes
        ],
        "resource_keys": ordered_unique(resources),
        "permissions": ordered_unique(permissions),
        "template_features": ordered_unique(template_features),
        "app_templates": ordered_unique(app_templates),
        "simple_code_refs": ordered_unique(simple_code_refs),
        "simple_code_ids": [unit["id"] for unit in resolved_simple_units],
        "simple_code_units": [
            {
                "id": unit["id"],
                "kind": unit.get("kind", ""),
                "implementation_state": unit.get("implementation_state", ""),
                "feature": unit.get("feature", ""),
                "api_members": unit.get("api_members", []),
                "api_signatures": unit.get("api_signatures", []),
                "requires": unit.get("requires", []),
                "requires_modules": unit.get("requires_modules", []),
                "requires_capabilities": unit.get("requires_capabilities", []),
                "provides": unit.get("provides", []),
                "compose_after": unit.get("compose_after", []),
                "compose_after_units": unit.get("compose_after_units", []),
                "lifecycle_hook": unit.get("lifecycle_hook", ""),
                "threading": unit.get("threading", ""),
                "guards": unit.get("guards", []),
                "failure": unit.get("failure", ""),
                "template_source": unit.get("template_source", ""),
                "source_symbol": unit.get("source_symbol", ""),
            }
            for unit in resolved_simple_units
        ],
        "call_order": [
            {
                "step": index,
                "simple_code_id": unit["id"],
                "compose_after": unit.get("compose_after", []),
                "compose_after_units": unit.get("compose_after_units", []),
                "implementation_state": unit.get("implementation_state", ""),
                "api_members": unit.get("api_members", []),
                "api_signatures": unit.get("api_signatures", []),
            }
            for index, unit in enumerate(resolved_simple_units, start=1)
        ],
        "lifecycle": ordered_unique(lifecycle),
        "failure_handling": ordered_unique(
            unit.get("failure", "")
            for unit in resolved_simple_units
            if unit.get("failure")
        ),
        "guards": ordered_unique(guards),
        "conflicts": ordered_unique([value for value in conflicts if value]),
        "demo_evidence": ordered_unique(demo_evidence),
        "warnings": ordered_unique(warnings),
    }
    return composition

def print_list():
    registry = load_json("references/sdk-module-registry.json")
    print("Blueprints:")
    for blueprint in registry.get("blueprints", []):
        print(f"- {blueprint['id']}: {blueprint.get('title', '')}")
    print()
    print("Modules:")
    for module in registry.get("modules", []):
        print(f"- {module['id']} [{module.get('level', '')}/{module.get('priority', '')}]: {module.get('title', '')}")

def compact_composition(composition):
    compact = dict(composition)
    compact["simple_code_ids"] = composition["simple_code_ids"][:20]
    compact["simple_code_ids_total"] = len(composition["simple_code_ids"])
    compact.pop("simple_code_units", None)
    compact["simple_code_units_count"] = len(composition["simple_code_units"])
    compact.pop("call_order", None)
    compact["call_order_count"] = len(composition["call_order"])
    return compact


def print_text(composition, compact=False):
    print(f"Mode: {composition['mode']}")
    if composition.get("query"):
        print(f"Query: {composition['query']}")
    independence = composition.get("independence", {})
    print(f"External Demo required at use time: {independence.get('external_demo_required', False)}")
    print(f"External Doxygen required at use time: {independence.get('external_doxygen_required', False)}")
    if composition.get("requested_blueprints"):
        print("Requested blueprints: " + ", ".join(composition["requested_blueprints"]))
    if composition.get("requested_modules"):
        print("Requested modules: " + ", ".join(composition["requested_modules"]))
    if composition["blueprints"]:
        print("Blueprints: " + ", ".join(composition["blueprints"]))
    print("Modules:")
    for index, module in enumerate(composition["modules"], start=1):
        print(f"{index}. {module['id']} [{module['priority']}/{module['level']}] - {module['title']}")
    print("API recipes: " + (", ".join(recipe["id"] for recipe in composition["api_recipes"]) or "-"))
    print("Resource keys: " + (", ".join(composition["resource_keys"]) or "-"))
    print("Permissions: " + (", ".join(composition["permissions"]) or "-"))
    print("Template features: " + (", ".join(composition["template_features"]) or "-"))
    print("App templates: " + (", ".join(composition.get("app_templates", [])) or "-"))
    print("Simple code refs: " + (", ".join(composition["simple_code_refs"]) or "-"))
    if compact:
        print(f"Simple code ids: {len(composition['simple_code_ids'])} total (rerun without --compact to list)")
    else:
        print("Simple code ids: " + (", ".join(composition["simple_code_ids"]) or "-"))
    if compact and composition["call_order"]:
        print(f"Call order steps: {len(composition['call_order'])} (rerun without --compact to list)")
    elif composition["call_order"]:
        print("Call order:")
        for item in composition["call_order"]:
            members = ", ".join(item["api_members"]) or "workflow contract"
            print(f"{item['step']}. {item['simple_code_id']}: {members}")
    if composition["conflicts"]:
        print("Conflicts/sequence guards: " + "; ".join(composition["conflicts"]))
    if composition["warnings"]:
        print("Warnings:")
        for warning in composition["warnings"]:
            print(f"- {warning}")

def main():
    args = parse_args()
    if args.list_items:
        print_list()
        return
    composition = compose_request(
        query=args.query,
        modules=args.modules,
        blueprint=args.blueprint,
        mode=args.mode,
        limit=args.limit,
    )
    if args.as_json:
        if args.compact:
            composition = compact_composition(composition)
        print(json.dumps(composition, ensure_ascii=False, indent=2))
    else:
        print_text(composition, compact=args.compact)

if __name__ == "__main__":
    main()
