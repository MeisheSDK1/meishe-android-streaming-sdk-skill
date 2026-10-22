#!/usr/bin/env python3
"""Strict standalone knowledge and module audit for the Meishe Android skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from coverage_summary import build_coverage_summary, coverage_artifact_gaps

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

UNIT_FIELDS = {
    "schema_version",
    "id",
    "kind",
    "implementation_state",
    "priority",
    "feature",
    "source_label",
    "scenario",
    "api_classes",
    "api_members",
    "api_signatures",
    "requires",
    "inputs",
    "provides",
    "resources",
    "threading",
    "guards",
    "failure",
    "compose_after",
    "compose_after_units",
    "compose_into",
    "requires_modules",
    "requires_capabilities",
    "lifecycle_hook",
    "evidence_refs",
    "code",
    "template_source",
    "source_symbol",
    "steps",
}
CONTRACT_FIELDS = {
    "id",
    "title",
    "level",
    "priority",
    "category",
    "requires",
    "provides",
    "api_recipes",
    "simple_code_refs",
    "resources",
    "permissions",
    "template_features",
    "guards",
    "conflicts",
    "lifecycle",
    "integration_modes",
    "demo_evidence",
}
ALLOWED_UNIT_KINDS = {"java_unit", "recipe", "pseudocode", "evidence_fragment"}
ALLOWED_COVERAGE_STATES = {
    "evidence_only",
    "contract_only",
    "compiled_unit",
    "generated_module",
    "runtime_verified",
}
ALLOWED_LIFECYCLE_HOOKS = {
    "sdk_init",
    "activity_create",
    "timeline_created",
    "live_window_bound",
    "asset_installed",
    "before_structural_mutation",
    "after_mutation_refresh",
    "destroy",
}
API_CONTRACT_FIELDS = {
    "parameter_types",
    "return_type",
    "modifiers",
    "is_static",
    "is_final",
    "constant_value",
    "overload_ids",
    "declared_owner",
    "official_doc_refs",
    "threading",
    "lifecycle",
    "state_conflicts",
    "return_handling",
    "failure_paths",
}
RUNTIME_MATRIX_FIELDS = {
    "schema_version",
    "sdk_version",
    "verification_date",
    "scope",
    "devices",
    "runs",
    "unverified_scope",
}
RUNTIME_DEVICE_FIELDS = {
    "id",
    "manufacturer",
    "model",
    "android_api",
    "abi",
    "build_fingerprint",
}
RUNTIME_RUN_FIELDS = {
    "id",
    "blueprint_id",
    "device_id",
    "mode",
    "package_label",
    "build_result",
    "install_result",
    "runtime_result",
    "verified_modules",
    "verified_features",
    "verified_units",
    "verified_api_ids",
    "flows",
    "limitations",
}
RUNTIME_FLOW_FIELDS = {"id", "result", "assertions"}
ALLOWED_RUNTIME_RESULTS = {"passed", "partial", "failed"}
ALLOWED_INTEGRATION_MODES = {"new-app", "incremental", "api-only"}
BUILD_MATRIX_FIELDS = {
    "schema_version",
    "sdk_version",
    "verification_date",
    "scope",
    "toolchain",
    "runs",
    "warnings",
}
BUILD_RUN_FIELDS = {
    "id",
    "kind",
    "result",
    "isolated",
    "blueprint_ids",
    "assertions",
}
PRODUCTION_RESOURCE_MATRIX_FIELDS = {
    "schema_version",
    "updated_at",
    "scope",
    "policy",
    "external_catalog",
    "verification_runs",
    "external_requirements",
    "device_matrix",
}
REQUIRED_LOCAL_MATERIAL_POLICY = {
    "remote_material_service": "not_embedded",
    "service_request_code": "forbidden",
    "service_interface_questions": "contact_meishe_business",
    "license_acquisition_questions": "contact_meishe_business",
}
REQUIRED_EXTERNAL_MATERIAL_FAMILIES = {
    "filter",
    "transition",
    "captionstyle",
    "compoundcaption",
    "captionbubble",
    "captionrichword",
    "captionanimation",
    "customsticker",
    "stickeranimation",
    "animation",
    "particle",
    "picinpic",
    "capturescene",
    "arface",
    "beauty",
    "theme",
    "font",
}
OFFICIAL_RESOURCE_MAP_FIELDS = {
    "schema_version",
    "updated_at",
    "official_download",
    "observed_package",
    "policy",
    "resource_groups",
    "asset_families",
    "workflow_source_roots",
    "not_present_in_observed_package",
}
REQUIRED_OFFICIAL_RESOURCE_GROUPS = {
    "streaming-sdk-runtime",
    "effect-sdk-runtime",
    "optional-sdk-helpers",
    "streaming-demo-license",
    "effect-kit-demo-license",
    "streaming-human-detection-models",
    "effect-kit-reference-assets",
}
FORBIDDEN_MATERIAL_RUNTIME_TOKENS = {
    "MeisheAssetCenterClient",
    "MeisheMaterialDownloadManager",
    "MeisheMaterialService",
    "MeisheAuthHeaderProvider",
    "MeisheDemoMaterialCatalog",
    "DEFAULT_SERVICE_BASE_URL",
    "EXTRA_BASE_URL",
    "EXTRA_DEMO_MODE",
    "HttpURLConnection",
    "api/sdkdemo",
    "mall.meishesdk",
}
WINDOWS_ABSOLUTE_PATH_RE = re.compile(r"(?i)(?<![A-Z])[A-Z]:[\\/]")
JVM_DESCRIPTOR_TYPE_RE = re.compile(r"^(?:[BCDFIJSZV]|\[+|L.+;)$")
MIN_FEATURE_COUNT = 62
MIN_API_TYPE_COUNT = 283
MIN_API_MEMBER_COUNT = 739
MIN_OBSERVED_METHOD_COUNT = 515
MIN_SIMPLE_CODE_UNIT_COUNT = 200
GENERIC_EVIDENCE_REASON_FRAGMENTS = {
    "no exact compiled/generated unit",
    "has no exact compiled/generated unit",
    "no matching public jar signature and no exact unit",
}

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--sdk-jar", type=Path)
    parser.add_argument("--android-jar", type=Path)
    parser.add_argument(
        "--require-java-compile",
        action="store_true",
        help="Fail unless every java_unit is compiled against the supplied jars.",
    )
    return parser.parse_args()

def skill_dir():
    return Path(__file__).resolve().parents[1]

def load_json(relative_path):
    with (skill_dir() / relative_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)

def path_is_file(path):
    if os.name == "nt":
        return os.path.isfile("\\\\?\\" + str(path.resolve()))
    return path.is_file()

def production_resource_matrix_gaps(matrix):
    gaps = []
    missing_root_fields = sorted(PRODUCTION_RESOURCE_MATRIX_FIELDS - set(matrix))
    if missing_root_fields:
        gaps.append(
            {
                "kind": "production_resource_matrix",
                "id": "<root>",
                "fields": missing_root_fields,
            }
        )

    policy = matrix.get("policy", {})
    invalid_policy = {
        key: {"expected": expected, "actual": policy.get(key)}
        for key, expected in REQUIRED_LOCAL_MATERIAL_POLICY.items()
        if policy.get(key) != expected
    }
    if invalid_policy:
        gaps.append(
            {
                "kind": "local_material_policy",
                "id": "<root>",
                "reason": "local-only material boundary is incomplete",
                "entries": invalid_policy,
            }
        )

    external_catalog = matrix.get("external_catalog", {})
    external_families = set(external_catalog.get("families", []))
    missing_families = sorted(REQUIRED_EXTERNAL_MATERIAL_FAMILIES - external_families)
    if missing_families:
        gaps.append(
            {
                "kind": "local_material_catalog",
                "id": "<root>",
                "reason": "required external material families are missing",
                "missing": missing_families,
            }
        )
    for key in ("activity", "catalog", "asset_constants"):
        relative_path = external_catalog.get(key)
        if not relative_path or not path_is_file(skill_dir() / relative_path):
            gaps.append(
                {
                    "kind": "local_material_catalog",
                    "id": key,
                    "reason": "catalog implementation path is missing",
                    "path": relative_path,
                }
            )

    verification_runs = matrix.get("verification_runs", [])
    run_ids = [run.get("id") for run in verification_runs if run.get("id")]
    duplicate_run_ids = sorted(
        run_id for run_id, count in Counter(run_ids).items() if count > 1
    )
    if duplicate_run_ids:
        gaps.append(
            {
                "kind": "production_resource_run",
                "id": "<root>",
                "reason": "duplicate verification run ids",
                "ids": duplicate_run_ids,
            }
        )
    if not any(
        run.get("id", "").startswith("local-material-policy-")
        and run.get("result") == "passed"
        for run in verification_runs
    ):
        gaps.append(
            {
                "kind": "production_resource_run",
                "id": "local-material-policy",
                "reason": "passing local-material policy validation is missing",
            }
        )

    runtime_root = skill_dir() / "assets/android-feature-templates/asset-center"
    for path in runtime_root.rglob("*"):
        if not path.is_file() or path.suffix not in {".java", ".xml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_MATERIAL_RUNTIME_TOKENS:
            if token in text:
                gaps.append(
                    {
                        "kind": "local_material_network_boundary",
                        "id": str(path.relative_to(skill_dir())),
                        "reason": "forbidden material-service runtime token",
                        "token": token,
                    }
                )
    return gaps

def official_sdk_resource_map_gaps(resource_map, module_ids):
    gaps = []
    missing_root_fields = sorted(OFFICIAL_RESOURCE_MAP_FIELDS - set(resource_map))
    if missing_root_fields:
        gaps.append(
            {
                "kind": "official_sdk_resource_map",
                "id": "<root>",
                "fields": missing_root_fields,
            }
        )

    download = resource_map.get("official_download", {})
    expected_download = {
        "url": "https://www.meishesdk.com/downloads",
        "page_section": "SDK下载及开发文档",
        "platform": "Android",
        "release_line": "LTS",
        "button_label": "下载SDK人脸版本",
    }
    invalid_download = {
        key: {"expected": expected, "actual": download.get(key)}
        for key, expected in expected_download.items()
        if download.get(key) != expected
    }
    if invalid_download:
        gaps.append(
            {
                "kind": "official_sdk_download_route",
                "id": "<root>",
                "entries": invalid_download,
            }
        )

    groups = resource_map.get("resource_groups", [])
    group_ids = [group.get("id") for group in groups if group.get("id")]
    missing_groups = sorted(REQUIRED_OFFICIAL_RESOURCE_GROUPS - set(group_ids))
    duplicate_groups = sorted(
        group_id for group_id, count in Counter(group_ids).items() if count > 1
    )
    if missing_groups or duplicate_groups:
        gaps.append(
            {
                "kind": "official_sdk_resource_groups",
                "id": "<root>",
                "missing": missing_groups,
                "duplicates": duplicate_groups,
            }
        )

    families = resource_map.get("asset_families", [])
    family_ids = [family.get("family") for family in families if family.get("family")]
    duplicate_families = sorted(
        family_id for family_id, count in Counter(family_ids).items() if count > 1
    )
    if len(family_ids) != 34 or duplicate_families:
        gaps.append(
            {
                "kind": "official_sdk_asset_families",
                "id": "<root>",
                "expected_count": 34,
                "actual_count": len(family_ids),
                "duplicates": duplicate_families,
            }
        )

    referenced_modules = {
        module_id
        for item in [*groups, *families]
        for module_id in item.get("module_ids", [])
    }
    invalid_modules = sorted(referenced_modules - set(module_ids))
    if invalid_modules:
        gaps.append(
            {
                "kind": "official_sdk_resource_modules",
                "id": "<root>",
                "invalid": invalid_modules,
            }
        )

    relative_paths = []
    relative_paths.extend(
        resource_map.get("observed_package", {}).get("required_root_markers", [])
    )
    for group in groups:
        relative_paths.extend(group.get("relative_files", []))
        relative_paths.extend(group.get("relative_directories", []))
    relative_paths.extend(
        family.get("relative_directory", "") for family in families
    )
    relative_paths.extend(
        item.get("relative_path", "")
        for item in resource_map.get("workflow_source_roots", [])
    )
    invalid_paths = sorted(
        {
            path
            for path in relative_paths
            if not path
            or WINDOWS_ABSOLUTE_PATH_RE.search(path)
            or path.startswith(("/", "\\"))
            or ".." in Path(path.replace("\\", "/")).parts
        }
    )
    if invalid_paths:
        gaps.append(
            {
                "kind": "official_sdk_resource_paths",
                "id": "<root>",
                "invalid": invalid_paths,
            }
        )

    serialized = json.dumps(resource_map, ensure_ascii=False).casefold()
    if "mall.meishesdk" in serialized or "api/sdkdemo" in serialized:
        gaps.append(
            {
                "kind": "official_sdk_resource_network_boundary",
                "id": "<root>",
                "reason": "material-service route is retained in the local resource map",
            }
        )
    return gaps

def missing_fields(items, fields, kind):
    gaps = []
    for item in items:
        missing = sorted(fields - set(item))
        if missing:
            gaps.append({"kind": kind, "id": item.get("id", "<missing>"), "fields": missing})
    return gaps

def duplicate_ids(items, kind):
    counts = Counter(item.get("id") for item in items)
    return [
        {"kind": kind, "id": item_id, "count": count}
        for item_id, count in counts.items()
        if item_id and count > 1
    ]

def braces_are_balanced(code):
    depth = 0
    quote = ""
    escaped = False
    line_comment = False
    block_comment = False
    index = 0
    while index < len(code):
        character = code[index]
        next_character = code[index + 1] if index + 1 < len(code) else ""
        if line_comment:
            if character == "\n":
                line_comment = False
            index += 1
            continue
        if block_comment:
            if character == "*" and next_character == "/":
                block_comment = False
                index += 2
            else:
                index += 1
            continue
        if quote:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                quote = ""
            index += 1
            continue
        if character == "/" and next_character == "/":
            line_comment = True
            index += 2
            continue
        if character == "/" and next_character == "*":
            block_comment = True
            index += 2
            continue
        if character in {'"', "'"}:
            quote = character
        elif character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth < 0:
                return False
        index += 1
    return depth == 0 and not quote and not block_comment

def dependency_cycles(modules):
    module_index = {item["id"]: item for item in modules}
    cycles = []
    visited = set()
    active = []

    def visit(module_id):
        if module_id in active:
            start = active.index(module_id)
            cycle = active[start:] + [module_id]
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if module_id in visited or module_id not in module_index:
            return
        active.append(module_id)
        for required in module_index[module_id].get("requires", []):
            visit(required)
        active.pop()
        visited.add(module_id)

    for module_id in module_index:
        visit(module_id)
    return cycles

def unit_dependency_gaps(units):
    unit_index = {unit["id"]: unit for unit in units}
    missing = []
    cycles = []
    visited = set()
    active = []

    def visit(unit_id):
        if unit_id in active:
            cycle = active[active.index(unit_id):] + [unit_id]
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if unit_id in visited:
            return
        unit = unit_index.get(unit_id)
        if unit is None:
            return
        active.append(unit_id)
        for dependency_id in unit.get("compose_after_units", []):
            if dependency_id not in unit_index:
                missing.append({"unit": unit_id, "compose_after_unit": dependency_id})
                continue
            visit(dependency_id)
        active.pop()
        visited.add(unit_id)

    for unit_id in unit_index:
        visit(unit_id)
    return missing, cycles

def unit_order_gaps(units):
    unit_index = {unit["id"]: unit for unit in units}
    gaps = []

    def has_ancestor(unit_id, expected_ancestor):
        visited = set()

        def visit(current_id):
            if current_id in visited:
                return False
            visited.add(current_id)
            unit = unit_index.get(current_id)
            if unit is None:
                return False
            for dependency_id in unit.get("compose_after_units", []):
                if dependency_id == expected_ancestor or visit(dependency_id):
                    return True
            return False

        return visit(unit_id)

    required_orders = [
        ("java.timeline.create", "java.timeline.append-clip", "timeline_before_clip"),
        (
            "java.timeline.create",
            "java.timeline.append-trimmed-clip",
            "timeline_before_trimmed_clip",
        ),
        ("java.preview.connect", "java.preview.play", "live_window_before_play"),
        (
            "java.preview.connect",
            "java.preview.play-with-fps",
            "live_window_before_play_with_fps",
        ),
        ("java.engine.stop", "java.export.configure", "stop_before_export_config"),
        ("java.engine.stop", "java.export.compile", "stop_before_export"),
    ]
    structural_units = {
        unit["id"]
        for unit in units
        if unit.get("kind") == "java_unit"
        and unit.get("lifecycle_hook") == "before_structural_mutation"
        and unit["id"] not in {"java.engine.stop", "java.engine.stop-with-flags"}
    }
    required_orders.extend(
        ("java.engine.stop", unit_id, "stop_before_structural_mutation")
        for unit_id in sorted(structural_units)
    )
    for predecessor_id, successor_id, rule in required_orders:
        if predecessor_id not in unit_index or successor_id not in unit_index:
            gaps.append(
                {
                    "rule": rule,
                    "predecessor": predecessor_id,
                    "successor": successor_id,
                    "reason": "unit missing",
                }
            )
        elif not has_ancestor(successor_id, predecessor_id):
            gaps.append(
                {
                    "rule": rule,
                    "predecessor": predecessor_id,
                    "successor": successor_id,
                    "reason": "predecessor is not in dependency closure",
                }
            )
    return gaps

def module_dependency_closure(module_index, module_ids):
    resolved = set()

    def visit(module_id):
        if module_id in resolved or module_id not in module_index:
            return
        resolved.add(module_id)
        for required in module_index[module_id].get("requires", []):
            visit(required)

    for module_id in module_ids:
        visit(module_id)
    return resolved

def p3_processing_gaps(
    scope,
    report,
    api_rows,
    api_map,
    unit_index,
    module_index,
    recipe_index,
):
    gaps = []
    target_ids = scope.get("target_stable_ids", [])
    target_set = set(target_ids)
    report_items = report.get("items", [])
    report_ids = [item.get("stable_id") for item in report_items]
    report_set = set(report_ids)
    api_index = {row.get("stable_id"): row for row in api_rows}
    valid_domains = {
        contract.get("id")
        for contract in api_map.get("domain_contracts", [])
        if contract.get("id")
    }
    valid_recipes = set(recipe_index) | {
        unit_id
        for unit_id, unit in unit_index.items()
        if unit.get("kind") == "recipe"
    }

    if len(target_ids) != scope.get("target_count") or len(target_ids) != len(target_set):
        gaps.append(
            {
                "kind": "frozen_scope",
                "reason": "target_count or target IDs are inconsistent",
            }
        )
    if report.get("target_count") != scope.get("target_count"):
        gaps.append(
            {
                "kind": "processing_report",
                "reason": "report target_count differs from frozen scope",
            }
        )
    if len(report_ids) != report.get("processed_count") or len(report_ids) != len(report_set):
        gaps.append(
            {
                "kind": "processing_report",
                "reason": "processed_count or report IDs are inconsistent",
            }
        )
    for stable_id in sorted(target_set - report_set):
        gaps.append({"kind": "missing_report_item", "api": stable_id})
    for stable_id in sorted(report_set - target_set):
        gaps.append({"kind": "out_of_scope_report_item", "api": stable_id})

    coverage_counts = Counter()
    for item in report_items:
        stable_id = item.get("stable_id")
        row = api_index.get(stable_id)
        if row is None:
            gaps.append({"kind": "missing_api_member", "api": stable_id})
            continue
        coverage_status = item.get("coverage_status")
        coverage_counts[coverage_status] += 1
        if coverage_status != row.get("coverage_status"):
            gaps.append(
                {
                    "kind": "coverage_mismatch",
                    "api": stable_id,
                    "report": coverage_status,
                    "api_map": row.get("coverage_status"),
                }
            )
        if item.get("processing_disposition") != coverage_status:
            gaps.append({"kind": "invalid_disposition", "api": stable_id})

        domain_ids = item.get("domain_ids", [])
        module_ids = item.get("module_ids", [])
        recipe_ids = item.get("related_recipe_ids", [])
        simple_code_ids = item.get("simple_code_ids", [])
        if not domain_ids:
            gaps.append({"kind": "unclassified_api", "api": stable_id})
        for domain_id in domain_ids:
            if domain_id not in valid_domains:
                gaps.append(
                    {"kind": "invalid_domain", "api": stable_id, "domain": domain_id}
                )
        if not module_ids:
            gaps.append({"kind": "missing_module", "api": stable_id})
        for module_id in module_ids:
            if module_id not in module_index:
                gaps.append(
                    {"kind": "invalid_module", "api": stable_id, "module": module_id}
                )
        for recipe_id in recipe_ids:
            if recipe_id not in valid_recipes:
                gaps.append(
                    {"kind": "invalid_recipe", "api": stable_id, "recipe": recipe_id}
                )
        for unit_id in simple_code_ids:
            if unit_id not in unit_index:
                gaps.append(
                    {"kind": "invalid_simple_code", "api": stable_id, "unit": unit_id}
                )

        if coverage_status == "evidence_only":
            reason_code = item.get("evidence_only_reason_code", "")
            reason = item.get("evidence_only_reason", "")
            if not reason_code or not reason:
                gaps.append({"kind": "missing_retention_reason", "api": stable_id})
            if any(fragment in reason.lower() for fragment in GENERIC_EVIDENCE_REASON_FRAGMENTS):
                gaps.append({"kind": "generic_retention_reason", "api": stable_id})
            if reason_code in {"generic", "evidence_only.generic"}:
                gaps.append({"kind": "generic_retention_code", "api": stable_id})
        elif coverage_status in {"compiled_unit", "generated_module", "runtime_verified"}:
            java_units = [
                unit_id
                for unit_id in simple_code_ids
                if unit_index.get(unit_id, {}).get("kind") == "java_unit"
            ]
            if not java_units:
                gaps.append({"kind": "upgraded_without_java_unit", "api": stable_id})
            if item.get("evidence_only_reason") or item.get("evidence_only_reason_code"):
                gaps.append({"kind": "stale_retention_reason", "api": stable_id})

    if dict(sorted(coverage_counts.items())) != report.get("coverage_counts", {}):
        gaps.append(
            {
                "kind": "coverage_count_mismatch",
                "expected": dict(sorted(coverage_counts.items())),
                "actual": report.get("coverage_counts", {}),
            }
        )
    upgraded_count = sum(
        count for state, count in coverage_counts.items() if state != "evidence_only"
    )
    if upgraded_count != report.get("upgraded_count"):
        gaps.append({"kind": "upgraded_count_mismatch"})
    if coverage_counts.get("evidence_only", 0) != report.get("retained_evidence_count"):
        gaps.append({"kind": "retained_count_mismatch"})
    for field in ("unclassified_count", "missing_module_count", "generic_reason_count"):
        if report.get(field) != 0:
            gaps.append({"kind": "nonzero_report_gap", "field": field, "count": report.get(field)})
    return gaps

def compile_java_units(units, sdk_jar, android_jar):
    java_units = [unit for unit in units if unit["kind"] == "java_unit"]
    if not sdk_jar or not android_jar:
        return [], [], "SDK jar and Android platform jar were not both supplied"
    if not sdk_jar.is_file() or not android_jar.is_file():
        return [], [
            {
                "id": "<classpath>",
                "error": "Missing SDK jar or Android platform jar",
            }
        ], ""
    javac = shutil.which("javac")
    if not javac:
        return [], [{"id": "<javac>", "error": "javac not found"}], ""
    compiled = []
    failures = []
    classpath = f"{sdk_jar}{';' if sys.platform == 'win32' else ':'}{android_jar}"
    with tempfile.TemporaryDirectory(prefix="meishe-unit-compile-") as temp_dir:
        temp_root = Path(temp_dir)
        for index, unit in enumerate(java_units):
            class_name = f"UnitCompileCheck{index}"
            source_path = temp_root / f"{class_name}.java"
            face_occlusion_stub = (
                ""
                if "void enableAIFaceOcclusionIfHighPower" in unit["code"]
                else "  void enableAIFaceOcclusionIfHighPower(NvsFx arSceneFx) { }"
            )
            source = "\n".join(
                [
                    "import com.meicam.sdk.*;",
                    "import com.meicam.effect.sdk.*;",
                    "import android.content.Context;",
                    "import android.graphics.Bitmap;",
                    "import android.graphics.PointF;",
                    "import android.graphics.RectF;",
                    "import android.database.Cursor;",
                    "import android.net.Uri;",
                    "import android.os.Handler;",
                    "import android.provider.OpenableColumns;",
                    "import org.json.*;",
                    "import java.io.*;",
                    "import java.nio.charset.StandardCharsets;",
                    "import java.security.*;",
                    "import java.util.*;",
                    "import java.util.zip.*;",
                    f"final class {class_name} {{",
                    "  private NvsStreamingContext streamingContext;",
                    "  private NvsTimeline timeline;",
                    "  private NvsAssetPackageManager packageManager;",
                    "  private NvsLiveWindow liveWindow;",
                    "  private final NvsMediaFileConvertor convertor = new NvsMediaFileConvertor();",
                    "  private android.content.Context appContext;",
                    "  private static final String TAG = \"unit\";",
                    "  private static final String AR_SCENE = \"AR Scene\";",
                    "  private static final String AI_FACE_OCCLUSION_ENABLED = \"AI Face Occlusion Enabled\";",
                    "  private static final String MAX_FACES_RESPECT_MIN = \"Max Faces Respect Min\";",
                    "  private static final String SINGLE_BUFFER_MODE = \"Single Buffer Mode\";",
                    "  private static final long US_PER_MS = 1_000L;",
                    "  private static final int MAX_ARCHIVE_ENTRIES = 2_048;",
                    "  private static final long MAX_EXTRACTED_BYTES = 256L * 1024L * 1024L;",
                    "  static final class MediaProbe {",
                    "    MediaProbe(long durationUs, NvsSize size, int rotation) { }",
                    "  }",
                    "  interface InstallCallback {",
                    "    void onComplete(InstallResult result);",
                    "  }",
                    "  static final class InstallResult {",
                    "    final String packageId;",
                    "    final int errorCode;",
                    "    InstallResult(String packageId, String filePath, int packageType, int errorCode) {",
                    "      this.packageId = packageId == null ? \"\" : packageId;",
                    "      this.errorCode = errorCode;",
                    "    }",
                    "    boolean isSuccess() {",
                    "      return errorCode == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR",
                    "          || errorCode == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED;",
                    "    }",
                    "  }",
                    "  static final class MeisheAssetInstaller {",
                    "    interface InstallCallback { void onComplete(InstallResult result); }",
                    "    static final class InstallResult {",
                    "      final String packageId = \"\";",
                    "      boolean isSuccess() { return true; }",
                    "    }",
                    "    int installAsynchronously(String packagePath, String licensePath,",
                    "        int packageType, InstallCallback callback) { return 0; }",
                    "    String installOrUpgrade(String packagePath, String licensePath,",
                    "        int packageType) { return \"\"; }",
                    "  }",
                    "  private final MeisheAssetInstaller assetInstaller = new MeisheAssetInstaller();",
                    "  static final class ShotSpec {",
                    "    final int index;",
                    "    final long durationUs;",
                    "    final String sourceName;",
                    "    final String filterId;",
                    "    final String transitionId;",
                    "    final String compoundCaptionId;",
                    "    ShotSpec(int index, long durationUs, String sourceName, String filterId,",
                    "        String transitionId, String compoundCaptionId) {",
                    "      this.index = index;",
                    "      this.durationUs = durationUs;",
                    "      this.sourceName = sourceName;",
                    "      this.filterId = filterId;",
                    "      this.transitionId = transitionId;",
                    "      this.compoundCaptionId = compoundCaptionId;",
                    "    }",
                    "  }",
                    "  static final class MimoSpec {",
                    "    final String id;",
                    "    final String aspectRatio;",
                    "    final String musicFileName;",
                    "    final long musicDurationUs;",
                    "    final String timelineFilterId;",
                    "    final String endingFilterId;",
                    "    final long endingFilterDurationUs;",
                    "    final List<ShotSpec> shots;",
                    "    MimoSpec(String id, String aspectRatio, String musicFileName,",
                    "        long musicDurationUs, String timelineFilterId, String endingFilterId,",
                    "        long endingFilterDurationUs, List<ShotSpec> shots) {",
                    "      this.id = id;",
                    "      this.aspectRatio = aspectRatio;",
                    "      this.musicFileName = musicFileName;",
                    "      this.musicDurationUs = musicDurationUs;",
                    "      this.timelineFilterId = timelineFilterId;",
                    "      this.endingFilterId = endingFilterId;",
                    "      this.endingFilterDurationUs = endingFilterDurationUs;",
                    "      this.shots = shots;",
                    "    }",
                    "  }",
                    "  static final class BuildResult {",
                    "    BuildResult(NvsTimeline timeline, int clips, int effects, int captions,",
                    "        List<String> failures) { }",
                    "  }",
                    "  static final class ExtractedMimoPackage {",
                    "    ExtractedMimoPackage(File rootDirectory, File infoFile) { }",
                    "  }",
                    "  static final class AssetInstallResult {",
                    "    AssetInstallResult(int attempted, int installed, List<String> failures) { }",
                    "  }",
                    "  private static int packageTypeForName(String name) {",
                    "    if (name == null) { return -1; }",
                    "    String lower = name.toLowerCase(Locale.ROOT);",
                    "    if (lower.endsWith(\".videofx\")) {",
                    "      return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;",
                    "    }",
                    "    if (lower.endsWith(\".videotransition\")) {",
                    "      return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;",
                    "    }",
                    "    if (lower.endsWith(\".compoundcaption\")) {",
                    "      return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;",
                    "    }",
                    "    return -1;",
                    "  }",
                    face_occlusion_stub,
                    "  static final class MeisheThreading {",
                    "    static void requireMainThread(String operation) { }",
                    "  }",
                    "  static final class Log {",
                    "    static int e(String tag, String message) { return 0; }",
                    "  }",
                    unit["code"],
                    "}",
                ]
            )
            source_path.write_text(source, encoding="utf-8")
            result = subprocess.run(
                [
                    javac,
                    "-proc:none",
                    "-encoding",
                    "UTF-8",
                    "-cp",
                    classpath,
                    "-d",
                    str(temp_root / "classes"),
                    str(source_path),
                ],
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                check=False,
            )
            if result.returncode:
                failures.append(
                    {
                        "id": unit["id"],
                        "error": result.stderr.strip()[-2000:],
                    }
                )
            else:
                compiled.append(unit["id"])
    return compiled, failures, ""

def audit(args):
    root = skill_dir()
    registry = load_json("references/sdk-module-registry.json")
    simple_registry = load_json("references/simple-code-registry.json")
    api_map = load_json("references/demo-api-simple-code-map.json")
    feature_map = load_json("references/demo-feature-simple-code-map.json")
    lookup = load_json("references/skill-lookup-index.json")
    sdk_signatures = load_json("references/sdk-signature-map.json")
    runtime_matrix = load_json("references/runtime-verification-matrix.json")
    build_matrix = load_json("references/build-verification-matrix.json")
    production_resource_matrix = load_json(
        "references/production-resource-verification-matrix.json"
    )
    official_sdk_resource_map = load_json(
        "references/official-sdk-download-resource-map.json"
    )
    p3_scope = load_json("references/p3-api-processing-scope.json")
    p3_report = load_json("references/p3-api-processing.json")

    bricks = registry.get("api_bricks", [])
    recipes = registry.get("api_recipes", [])
    modules = registry.get("modules", [])
    blueprints = registry.get("blueprints", [])
    units = simple_registry.get("units", [])
    unit_index = {unit["id"]: unit for unit in units}
    module_index = {module["id"]: module for module in modules}
    recipe_index = {recipe["id"]: recipe for recipe in recipes}
    blueprint_index = {blueprint["id"]: blueprint for blueprint in blueprints}

    contract_field_gaps = []
    for kind, items in (
        ("api_brick", bricks),
        ("api_recipe", recipes),
        ("module", modules),
        ("blueprint", blueprints),
    ):
        contract_field_gaps.extend(missing_fields(items, CONTRACT_FIELDS, kind))
    unit_field_gaps = missing_fields(units, UNIT_FIELDS, "simple_code_unit")
    duplicates = []
    for kind, items in (
        ("api_brick", bricks),
        ("api_recipe", recipes),
        ("module", modules),
        ("blueprint", blueprints),
        ("simple_code_unit", units),
    ):
        duplicates.extend(duplicate_ids(items, kind))

    invalid_unit_kinds = [
        {"id": unit["id"], "kind": unit.get("kind")}
        for unit in units
        if unit.get("kind") not in ALLOWED_UNIT_KINDS
    ]
    invalid_implementation_states = [
        {"id": unit["id"], "implementation_state": unit.get("implementation_state")}
        for unit in units
        if unit.get("implementation_state") not in ALLOWED_COVERAGE_STATES
    ]
    invalid_lifecycle_hooks = [
        {"id": unit["id"], "lifecycle_hook": unit.get("lifecycle_hook")}
        for unit in units
        if unit.get("lifecycle_hook") not in ALLOWED_LIFECYCLE_HOOKS
    ]
    invalid_java_units = []
    for unit in units:
        if unit.get("kind") != "java_unit":
            continue
        if not unit.get("code") or not braces_are_balanced(unit["code"]):
            invalid_java_units.append({"id": unit["id"], "reason": "missing/unbalanced code"})
            continue
        template_source = root / unit.get("template_source", "")
        if not template_source.is_file():
            invalid_java_units.append({"id": unit["id"], "reason": "missing template source"})
        elif unit.get("source_symbol", "") not in template_source.read_text(encoding="utf-8"):
            invalid_java_units.append({"id": unit["id"], "reason": "template symbol not found"})

    missing_module_dependencies = [
        {"module": module["id"], "requires": required}
        for module in modules
        for required in module.get("requires", [])
        if required not in module_index
    ]
    missing_recipe_dependencies = [
        {"recipe": recipe["id"], "requires": required}
        for recipe in recipes
        for required in recipe.get("requires", [])
        if required not in module_index and required not in recipe_index
    ]
    missing_recipe_refs = [
        {"module": module["id"], "recipe": recipe_id}
        for module in modules
        for recipe_id in module.get("api_recipes", [])
        if recipe_id not in recipe_index
    ]
    missing_unit_refs = []
    for kind, items in (
        ("module", modules),
        ("recipe", recipes),
        ("blueprint", blueprints),
        ("feature", feature_map.get("features", [])),
    ):
        for item in items:
            for unit_id in item.get("simple_code_ids", []):
                if unit_id not in unit_index:
                    missing_unit_refs.append(
                        {"kind": kind, "id": item.get("id", item.get("feature")), "unit": unit_id}
                    )

    modules_without_java_units = [
        module["id"]
        for module in modules
        if module.get("level") in {"small_module", "big_module"}
        and not any(
            unit_index.get(unit_id, {}).get("kind") == "java_unit"
            for unit_id in module.get("render_units", module.get("simple_code_ids", []))
        )
    ]

    missing_unit_dependencies, unit_dependency_cycles = unit_dependency_gaps(units)
    unit_order_gaps_found = unit_order_gaps(units)
    unsatisfied_unit_capabilities = []
    for unit in units:
        dependency_module_ids = module_dependency_closure(
            module_index,
            unit.get("requires_modules", []),
        )
        provided_capabilities = {
            capability
            for module_id in dependency_module_ids
            for capability in module_index[module_id].get("provides", [])
        }
        for capability in unit.get("requires_capabilities", []):
            if capability not in provided_capabilities:
                unsatisfied_unit_capabilities.append(
                    {"unit": unit["id"], "capability": capability}
                )
    feature_rows = feature_map.get("features", [])
    uncovered_features = [
        row["feature"]
        for row in feature_rows
        if not row.get("simple_code_ids")
        or row.get("coverage_status") not in ALLOWED_COVERAGE_STATES
    ]
    p0_p1_without_compiled_units = [
        row["feature"]
        for row in feature_rows
        if row.get("priority") in {"P0", "P1"}
        and row.get("coverage_status") not in {"compiled_unit", "runtime_verified"}
    ]
    contract_only_features = [
        row["feature"]
        for row in feature_rows
        if row.get("coverage_status") == "contract_only"
    ]
    feature_recipe_count = sum(
        1 for unit in units if unit["id"].startswith("recipe.feature.")
    )
    features_without_dedicated_recipe = [
        row["feature"]
        for row in feature_rows
        if not row.get("feature_recipe_id")
        or row.get("feature_recipe_id") not in unit_index
    ]
    api_rows = api_map.get("api_members", [])
    api_contract_field_gaps = missing_fields(
        api_rows,
        API_CONTRACT_FIELDS,
        "api_member",
    )
    descriptor_java_types = []
    for row in api_rows:
        types = list(row.get("parameter_types", [])) + [row.get("return_type", "")]
        types.extend(
            parameter.get("java_type", "")
            for parameter in row.get("parameters", [])
        )
        types.append(row.get("returns", {}).get("java_type", ""))
        invalid_types = sorted(
            {
                java_type
                for java_type in types
                if java_type and JVM_DESCRIPTOR_TYPE_RE.match(java_type)
            }
        )
        if invalid_types:
            descriptor_java_types.append(
                {
                    "api": row.get("stable_id", row["member"]),
                    "types": invalid_types,
                }
            )
    signature_index = {
        row["stable_id"]: row
        for row in sdk_signatures.get("members", [])
    }
    signature_contract_mismatches = []
    for row in api_rows:
        if not row.get("jar_signature"):
            continue
        signature = signature_index.get(row.get("stable_id"))
        if not signature:
            signature_contract_mismatches.append(
                {"api": row.get("stable_id"), "field": "signature", "actual": "missing"}
            )
            continue
        for field in (
            "parameter_types",
            "return_type",
            "modifiers",
            "is_static",
            "is_final",
            "constant_value",
            "overload_ids",
            "declared_owner",
        ):
            if row.get(field) != signature.get(field):
                signature_contract_mismatches.append(
                    {
                        "api": row.get("stable_id"),
                        "field": field,
                        "expected": signature.get(field),
                        "actual": row.get(field),
                    }
                )
    invalid_api_coverage = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if row.get("coverage_status") not in ALLOWED_COVERAGE_STATES
    ]
    high_priority_evidence_only = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if row.get("priority") in {"P0", "P1"}
        and row.get("coverage_status") == "evidence_only"
    ]
    p2_evidence_only = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if row.get("priority") == "P2"
        and row.get("coverage_status") == "evidence_only"
    ]
    frequent_p3_evidence_only = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if row.get("priority") == "P3"
        and row.get("coverage_status") == "evidence_only"
        and int(row.get("occurrences", 0)) >= 10
    ]
    observed_without_jar_signature = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if row.get("observed_in_demo") and not row.get("jar_signature")
    ]
    placeholder_returns = [
        row.get("stable_id", row["member"])
        for row in api_rows
        if isinstance(row.get("returns"), str)
        and "SDK-defined; inspect bundled official references or SDK jar signature" in row["returns"]
    ]
    class_fallback_unit_refs = [
        unit["id"]
        for unit in units
        if unit["id"].startswith("module.")
    ]
    dangling_api_units = [
        {"member": row["member"], "unit": unit_id}
        for row in api_rows
        for unit_id in row.get("simple_code_ids", [])
        if unit_id not in unit_index
    ]
    invalid_api_module_refs = [
        {"member": row["member"], "module": module_id}
        for row in api_rows
        for module_id in row.get("module_ids", [])
        if module_id not in module_index
    ]
    p3_gaps = p3_processing_gaps(
        p3_scope,
        p3_report,
        api_rows,
        api_map,
        unit_index,
        module_index,
        recipe_index,
    )

    missing_blueprint_templates = []
    template_root = root / "assets" / "android-blueprint-templates"
    for blueprint in blueprints:
        app_template = blueprint.get("app_template")
        if not app_template:
            continue
        template_dir = template_root / app_template
        for relative in (
            Path("app/src/main/AndroidManifest.xml"),
            Path("app/src/main/java/{{PACKAGE_PATH}}/MainActivity.java"),
        ):
            if not (template_dir / relative).is_file():
                missing_blueprint_templates.append(
                    {"blueprint": blueprint["id"], "file": relative.as_posix()}
                )

    runtime_template_gaps = []
    assets_root = root / "assets"
    for path in assets_root.rglob("*.xml"):
        text = path.read_text(encoding="utf-8")
        if "<com.meicam.sdk.NvsLiveWindow" in text:
            runtime_template_gaps.append(
                {
                    "file": path.relative_to(root).as_posix(),
                    "reason": "NvsLiveWindow must be created after SDK initialization, not inflated from XML",
                }
            )
    for path in assets_root.rglob("*.java"):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        applies_system_bar_insets = any(
            call in text
            for call in (
                "MeisheAppSupport.applySystemBarInsets(this);",
                "MeisheAppSupport.applySystemBarInsets(activity);",
            )
        )
        if "setContentView(" in text and not applies_system_bar_insets:
            runtime_template_gaps.append(
                {
                    "file": relative,
                    "reason": "Activity does not apply system-bar insets",
                }
            )
        live_window_index = text.find("new NvsLiveWindow(")
        if live_window_index >= 0:
            initialize_index = text.find(".initialize()")
            if initialize_index < 0 or initialize_index > live_window_index:
                runtime_template_gaps.append(
                    {
                        "file": relative,
                        "reason": "NvsLiveWindow is constructed before SDK initialization",
                    }
                )
        if (
            "requestPermissions(CAPTURE_PERMISSIONS" in text
            and "permissionRequestInFlight" not in text
        ):
                runtime_template_gaps.append(
                    {
                        "file": relative,
                        "reason": "Capture permission flow has no in-flight reentry guard",
                    }
                )

    blueprint_template_root = assets_root / "android-blueprint-templates"
    for layout_path in blueprint_template_root.glob(
        "*/app/src/main/res/layout/activity_main.xml"
    ):
        main_activity = (
            layout_path.parents[2]
            / "java"
            / "{{PACKAGE_PATH}}"
            / "MainActivity.java"
        )
        if not main_activity.is_file():
            continue
        layout_text = layout_path.read_text(encoding="utf-8")
        java_text = main_activity.read_text(encoding="utf-8")
        for button_id in sorted(set(re.findall(r"@\+id/([A-Za-z0-9_]*Button)", layout_text))):
            direct_listener = re.search(
                rf"R\.id\.{re.escape(button_id)}\)\.setOnClickListener\s*\(",
                java_text,
            )
            assignment = re.search(
                rf"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*findViewById\(R\.id\.{re.escape(button_id)}\)",
                java_text,
            )
            assigned_listener = bool(
                assignment
                and re.search(
                    rf"\b{re.escape(assignment.group(1))}\.setOnClickListener\s*\(",
                    java_text,
                )
            )
            if not direct_listener and not assigned_listener:
                runtime_template_gaps.append(
                    {
                        "file": main_activity.relative_to(root).as_posix(),
                        "reason": f"Blueprint button {button_id} has no click listener",
                    }
                )

    runtime_verification_gaps = []
    missing_runtime_matrix_fields = sorted(RUNTIME_MATRIX_FIELDS - set(runtime_matrix))
    if missing_runtime_matrix_fields:
        runtime_verification_gaps.append(
            {
                "kind": "runtime_matrix",
                "id": "<root>",
                "fields": missing_runtime_matrix_fields,
            }
        )
    runtime_devices = runtime_matrix.get("devices", [])
    runtime_runs = runtime_matrix.get("runs", [])
    runtime_verification_gaps.extend(
        missing_fields(runtime_devices, RUNTIME_DEVICE_FIELDS, "runtime_device")
    )
    runtime_verification_gaps.extend(
        missing_fields(runtime_runs, RUNTIME_RUN_FIELDS, "runtime_run")
    )
    runtime_verification_gaps.extend(duplicate_ids(runtime_devices, "runtime_device"))
    runtime_verification_gaps.extend(duplicate_ids(runtime_runs, "runtime_run"))
    runtime_device_index = {
        device.get("id"): device
        for device in runtime_devices
        if device.get("id")
    }
    feature_ids = {row.get("feature") for row in feature_rows}
    api_ids = {
        row.get("stable_id", row.get("id"))
        for row in api_rows
    }
    runtime_verified_blueprints = set()
    runtime_verified_modules = set()
    runtime_verified_features = set()
    runtime_verified_units = set()
    runtime_verified_apis = set()
    passed_runtime_blueprints = set()
    partial_runtime_blueprints = set()
    for run in runtime_runs:
        run_id = run.get("id", "<missing>")
        if run.get("blueprint_id") not in blueprint_index:
            runtime_verification_gaps.append(
                {
                    "kind": "runtime_run",
                    "id": run_id,
                    "reason": f"unknown blueprint {run.get('blueprint_id')}",
                }
            )
        if run.get("device_id") not in runtime_device_index:
            runtime_verification_gaps.append(
                {
                    "kind": "runtime_run",
                    "id": run_id,
                    "reason": f"unknown device {run.get('device_id')}",
                }
            )
        if run.get("mode") not in ALLOWED_INTEGRATION_MODES:
            runtime_verification_gaps.append(
                {
                    "kind": "runtime_run",
                    "id": run_id,
                    "reason": f"invalid mode {run.get('mode')}",
                }
            )
        for result_field in ("build_result", "install_result", "runtime_result"):
            if run.get(result_field) not in ALLOWED_RUNTIME_RESULTS:
                runtime_verification_gaps.append(
                    {
                        "kind": "runtime_run",
                        "id": run_id,
                        "reason": f"invalid {result_field} {run.get(result_field)}",
                    }
                )
        reference_groups = (
            ("module", "verified_modules", module_index),
            ("feature", "verified_features", feature_ids),
            ("unit", "verified_units", unit_index),
            ("api", "verified_api_ids", api_ids),
        )
        for kind, field, target in reference_groups:
            references = run.get(field, [])
            if not isinstance(references, list):
                runtime_verification_gaps.append(
                    {
                        "kind": "runtime_run",
                        "id": run_id,
                        "reason": f"{field} must be a list",
                    }
                )
                continue
            duplicate_references = [
                reference
                for reference, count in Counter(references).items()
                if count > 1
            ]
            for reference in duplicate_references:
                runtime_verification_gaps.append(
                    {
                        "kind": "runtime_run",
                        "id": run_id,
                        "reason": f"duplicate {kind} reference {reference}",
                    }
                )
            for reference in references:
                if reference not in target:
                    runtime_verification_gaps.append(
                        {
                            "kind": "runtime_run",
                            "id": run_id,
                            "reason": f"unknown {kind} reference {reference}",
                        }
                    )
        flows = run.get("flows", [])
        if not flows:
            runtime_verification_gaps.append(
                {
                    "kind": "runtime_run",
                    "id": run_id,
                    "reason": "flows must contain at least one verified workflow",
                }
            )
        runtime_verification_gaps.extend(
            missing_fields(flows, RUNTIME_FLOW_FIELDS, f"runtime_flow:{run_id}")
        )
        runtime_verification_gaps.extend(
            duplicate_ids(flows, f"runtime_flow:{run_id}")
        )
        for flow in flows:
            if flow.get("result") not in ALLOWED_RUNTIME_RESULTS:
                runtime_verification_gaps.append(
                    {
                        "kind": "runtime_flow",
                        "id": flow.get("id", "<missing>"),
                        "reason": f"invalid result {flow.get('result')}",
                    }
                )
            if not isinstance(flow.get("assertions"), list) or not flow.get("assertions"):
                runtime_verification_gaps.append(
                    {
                        "kind": "runtime_flow",
                        "id": flow.get("id", "<missing>"),
                        "reason": "assertions must contain at least one runtime observation",
                    }
                )
        if run.get("runtime_result") == "failed" and any(
            run.get(field)
            for field in (
                "verified_modules",
                "verified_features",
                "verified_units",
                "verified_api_ids",
            )
        ):
            runtime_verification_gaps.append(
                {
                    "kind": "runtime_run",
                    "id": run_id,
                    "reason": "failed run cannot contribute runtime_verified references",
                }
            )
        if run.get("runtime_result") in {"passed", "partial"}:
            runtime_verified_blueprints.add(run.get("blueprint_id"))
            runtime_verified_modules.update(run.get("verified_modules", []))
            runtime_verified_features.update(run.get("verified_features", []))
            runtime_verified_units.update(run.get("verified_units", []))
            runtime_verified_apis.update(run.get("verified_api_ids", []))
        if run.get("runtime_result") == "passed":
            passed_runtime_blueprints.add(run.get("blueprint_id"))
        elif run.get("runtime_result") == "partial":
            partial_runtime_blueprints.add(run.get("blueprint_id"))

    build_verification_gaps = []
    missing_build_matrix_fields = sorted(BUILD_MATRIX_FIELDS - set(build_matrix))
    if missing_build_matrix_fields:
        build_verification_gaps.append(
            {
                "kind": "build_matrix",
                "id": "<root>",
                "fields": missing_build_matrix_fields,
            }
        )
    build_runs = build_matrix.get("runs", [])
    build_verification_gaps.extend(
        missing_fields(build_runs, BUILD_RUN_FIELDS, "build_run")
    )
    build_verification_gaps.extend(duplicate_ids(build_runs, "build_run"))
    all_blueprint_ids = set(blueprint_index)
    passing_workspace_blueprints = set()
    passing_isolated_blueprints = set()
    passing_incremental_variants = set()
    passing_knowledge_validation = False
    for run in build_runs:
        run_id = run.get("id", "<missing>")
        if run.get("result") not in ALLOWED_RUNTIME_RESULTS:
            build_verification_gaps.append(
                {
                    "kind": "build_run",
                    "id": run_id,
                    "reason": f"invalid result {run.get('result')}",
                }
            )
        blueprint_ids = run.get("blueprint_ids", [])
        if not isinstance(blueprint_ids, list):
            build_verification_gaps.append(
                {
                    "kind": "build_run",
                    "id": run_id,
                    "reason": "blueprint_ids must be a list",
                }
            )
            blueprint_ids = []
        for blueprint_id in blueprint_ids:
            if blueprint_id not in blueprint_index:
                build_verification_gaps.append(
                    {
                        "kind": "build_run",
                        "id": run_id,
                        "reason": f"unknown blueprint {blueprint_id}",
                    }
                )
        if not isinstance(run.get("assertions"), list) or not run.get("assertions"):
            build_verification_gaps.append(
                {
                    "kind": "build_run",
                    "id": run_id,
                    "reason": "assertions must contain at least one build observation",
                }
            )
        if run.get("result") != "passed":
            continue
        if run.get("kind") == "blueprint_build" and not run.get("isolated"):
            passing_workspace_blueprints.update(blueprint_ids)
        if run.get("kind") == "standalone_blueprint_build" and run.get("isolated"):
            passing_isolated_blueprints.update(blueprint_ids)
            if not run.get("fixture_contents"):
                build_verification_gaps.append(
                    {
                        "kind": "build_run",
                        "id": run_id,
                        "reason": "isolated build must declare its neutral fixture contents",
                    }
                )
        if run.get("kind") == "incremental_build":
            passing_incremental_variants.update(run.get("variants", []))
        if run.get("kind") == "knowledge_validation" and run.get("isolated"):
            passing_knowledge_validation = True
    if passing_workspace_blueprints != all_blueprint_ids:
        build_verification_gaps.append(
            {
                "kind": "build_matrix",
                "id": "<root>",
                "reason": "passing workspace build does not cover all registered blueprints",
                "missing": sorted(all_blueprint_ids - passing_workspace_blueprints),
            }
        )
    if passing_isolated_blueprints != all_blueprint_ids:
        build_verification_gaps.append(
            {
                "kind": "build_matrix",
                "id": "<root>",
                "reason": "passing isolated build does not cover all registered blueprints",
                "missing": sorted(all_blueprint_ids - passing_isolated_blueprints),
            }
        )
    expected_incremental_variants = {
        "java-groovy",
        "java-kts",
        "kotlin-groovy",
        "kotlin-kts",
    }
    if passing_incremental_variants != expected_incremental_variants:
        build_verification_gaps.append(
            {
                "kind": "build_matrix",
                "id": "<root>",
                "reason": "passing incremental build does not cover all host variants",
                "missing": sorted(expected_incremental_variants - passing_incremental_variants),
            }
        )
    if not passing_knowledge_validation:
        build_verification_gaps.append(
            {
                "kind": "build_matrix",
                "id": "<root>",
                "reason": "missing passing isolated knowledge validation",
            }
        )

    missing_lookup_units = [
        {"entry": entry["id"], "unit": unit_id}
        for entry in lookup.get("entries", [])
        for unit_id in entry.get("simple_code_ids", [])
        if unit_id not in unit_index
    ]
    cycles = dependency_cycles(modules)
    compiled_units, compile_failures, compile_skipped_reason = compile_java_units(
        units,
        args.sdk_jar.resolve() if args.sdk_jar else None,
        args.android_jar.resolve() if args.android_jar else None,
    )
    compile_requirement_gap = (
        args.require_java_compile
        and len(compiled_units) != sum(unit["kind"] == "java_unit" for unit in units)
    )

    independence = registry.get("independence", {})
    independence_gaps = []
    if independence.get("external_demo_required", True):
        independence_gaps.append("external_demo_required is true")
    if independence.get("external_doxygen_required", True):
        independence_gaps.append("external_doxygen_required is true")
    for path in (
        root / "references" / "simple-code-registry.json",
        root / "references" / "demo-api-simple-code-map.json",
        root / "references" / "demo-feature-simple-code-map.json",
        root / "references" / "sdk-module-registry.json",
        root / "references" / "skill-lookup-index.json",
        root / "references" / "official-sdk-download-resource-map.json",
    ):
        if WINDOWS_ABSOLUTE_PATH_RE.search(path.read_text(encoding="utf-8")):
            independence_gaps.append(f"absolute Windows path in {path.name}")

    metric_gaps = []
    if len(feature_rows) < MIN_FEATURE_COUNT:
        metric_gaps.append(
            f"feature_count={len(feature_rows)} expected>={MIN_FEATURE_COUNT}"
        )
    if api_map.get("type_count", 0) < MIN_API_TYPE_COUNT:
        metric_gaps.append(
            f"api_type_count={api_map.get('type_count', 0)} expected>={MIN_API_TYPE_COUNT}"
        )
    if api_map.get("member_count", 0) < MIN_API_MEMBER_COUNT:
        metric_gaps.append(
            f"api_member_count={api_map.get('member_count', 0)} expected>={MIN_API_MEMBER_COUNT}"
        )
    if api_map.get("observed_method_count", 0) < MIN_OBSERVED_METHOD_COUNT:
        metric_gaps.append(
            "observed_method_count="
            f"{api_map.get('observed_method_count', 0)} expected>={MIN_OBSERVED_METHOD_COUNT}"
        )
    if len(units) < MIN_SIMPLE_CODE_UNIT_COUNT:
        metric_gaps.append(
            f"simple_code_unit_count={len(units)} expected>={MIN_SIMPLE_CODE_UNIT_COUNT}"
        )
    coverage_doc_gaps = coverage_artifact_gaps(root)
    coverage_summary = build_coverage_summary(root)
    production_resource_gaps = production_resource_matrix_gaps(
        production_resource_matrix
    )
    official_sdk_resource_gaps = official_sdk_resource_map_gaps(
        official_sdk_resource_map,
        module_index,
    )

    gap_groups = {
        "contract_field_gaps": contract_field_gaps,
        "unit_field_gaps": unit_field_gaps,
        "duplicate_ids": duplicates,
        "invalid_unit_kinds": invalid_unit_kinds,
        "invalid_implementation_states": invalid_implementation_states,
        "invalid_lifecycle_hooks": invalid_lifecycle_hooks,
        "invalid_java_units": invalid_java_units,
        "compile_failures": compile_failures,
        "missing_module_dependencies": missing_module_dependencies,
        "missing_recipe_dependencies": missing_recipe_dependencies,
        "missing_recipe_refs": missing_recipe_refs,
        "missing_unit_refs": missing_unit_refs,
        "modules_without_java_units": modules_without_java_units,
        "missing_unit_dependencies": missing_unit_dependencies,
        "unit_dependency_cycles": unit_dependency_cycles,
        "unit_order_gaps": unit_order_gaps_found,
        "unsatisfied_unit_capabilities": unsatisfied_unit_capabilities,
        "uncovered_features": uncovered_features,
        "features_without_dedicated_recipe": features_without_dedicated_recipe,
        "p0_p1_without_compiled_units": p0_p1_without_compiled_units,
        "contract_only_features": contract_only_features,
        "api_contract_field_gaps": api_contract_field_gaps,
        "descriptor_java_types": descriptor_java_types,
        "signature_contract_mismatches": signature_contract_mismatches,
        "invalid_api_coverage": invalid_api_coverage,
        "high_priority_evidence_only": high_priority_evidence_only,
        "p2_evidence_only": p2_evidence_only,
        "frequent_p3_evidence_only": frequent_p3_evidence_only,
        "observed_without_jar_signature": observed_without_jar_signature,
        "placeholder_returns": placeholder_returns,
        "class_fallback_unit_refs": class_fallback_unit_refs,
        "dangling_api_units": dangling_api_units,
        "invalid_api_module_refs": invalid_api_module_refs,
        "p3_processing_gaps": p3_gaps,
        "missing_blueprint_templates": missing_blueprint_templates,
        "runtime_template_gaps": runtime_template_gaps,
        "runtime_verification_gaps": runtime_verification_gaps,
        "build_verification_gaps": build_verification_gaps,
        "production_resource_gaps": production_resource_gaps,
        "official_sdk_resource_gaps": official_sdk_resource_gaps,
        "missing_lookup_units": missing_lookup_units,
        "dependency_cycles": cycles,
        "independence_gaps": independence_gaps,
        "metric_gaps": metric_gaps,
        "coverage_doc_gaps": coverage_doc_gaps,
    }
    total_gaps = sum(len(value) for value in gap_groups.values())
    if compile_requirement_gap:
        total_gaps += 1
    return {
        "standalone": not independence_gaps,
        "api_brick_count": len(bricks),
        "api_recipe_count": len(recipes),
        "module_count": len(modules),
        "blueprint_count": len(blueprints),
        "simple_code_unit_count": len(units),
        "simple_code_kinds": dict(Counter(unit["kind"] for unit in units)),
        "simple_code_states": dict(Counter(unit.get("implementation_state") for unit in units)),
        "feature_recipe_count": feature_recipe_count,
        "demo_feature_count": len(feature_rows),
        "api_type_count": api_map.get("type_count", 0),
        "api_member_count": api_map.get("member_count", 0),
        "observed_method_count": api_map.get("observed_method_count", 0),
        "api_coverage": dict(Counter(row.get("coverage_status") for row in api_rows)),
        "placeholder_return_count": len(placeholder_returns),
        "class_fallback_coverage_count": len(class_fallback_unit_refs),
        "observed_without_jar_signature_count": len(observed_without_jar_signature),
        "p3_processing_target_count": p3_report.get("target_count", 0),
        "p3_processing_upgraded_count": p3_report.get("upgraded_count", 0),
        "p3_processing_retained_evidence_count": p3_report.get(
            "retained_evidence_count", 0
        ),
        "compiled_java_unit_count": len(compiled_units),
        "runtime_verification_run_count": len(runtime_runs),
        "runtime_verification_device_count": len(runtime_devices),
        "runtime_verified_blueprint_count": len(runtime_verified_blueprints),
        "runtime_passed_blueprint_count": len(passed_runtime_blueprints),
        "runtime_partial_only_blueprint_count": len(
            partial_runtime_blueprints - passed_runtime_blueprints
        ),
        "runtime_verified_module_count": len(runtime_verified_modules),
        "runtime_verified_feature_count": len(runtime_verified_features),
        "runtime_verified_unit_count": len(runtime_verified_units),
        "runtime_verified_api_count": len(runtime_verified_apis),
        "runtime_verified_blueprints": sorted(runtime_verified_blueprints),
        "coverage_summary": coverage_summary,
        "build_verification_run_count": len(build_runs),
        "production_resource_verification_run_count": len(
            production_resource_matrix.get("verification_runs", [])
        ),
        "production_resource_device_target_count": len(
            production_resource_matrix.get("device_matrix", [])
        ),
        "build_verified_blueprint_count": len(passing_workspace_blueprints),
        "isolated_build_verified_blueprint_count": len(passing_isolated_blueprints),
        "incremental_build_variant_count": len(passing_incremental_variants),
        "compile_skipped_reason": compile_skipped_reason,
        "compile_requirement_gap": compile_requirement_gap,
        "gap_groups": gap_groups,
        "structural_gap_count": total_gaps,
    }

def print_text(result):
    print("Meishe Android SDK standalone knowledge audit")
    print(f"Standalone: {result['standalone']}")
    print(
        "Contracts: "
        f"{result['api_brick_count']} bricks, "
        f"{result['api_recipe_count']} recipes, "
        f"{result['module_count']} modules, "
        f"{result['blueprint_count']} blueprints"
    )
    print(
        f"Simple code: {result['simple_code_unit_count']} units "
        f"{result['simple_code_kinds']}"
    )
    print(f"Simple code states: {result['simple_code_states']}")
    print(f"Feature recipes: {result['feature_recipe_count']}")
    print(
        f"Coverage: {result['demo_feature_count']} features, "
        f"{result['api_type_count']} API types, "
        f"{result['api_member_count']} API members, "
        f"{result['observed_method_count']} observed methods"
    )
    print(f"API coverage states: {result['api_coverage']}")
    print(
        "Frozen low-frequency P3 processing: "
        f"{result['p3_processing_target_count']} targets, "
        f"{result['p3_processing_upgraded_count']} upgraded, "
        f"{result['p3_processing_retained_evidence_count']} retained as evidence"
    )
    print(f"Placeholder returns: {result['placeholder_return_count']}")
    print(f"Class fallback coverage units: {result['class_fallback_coverage_count']}")
    print(f"Observed APIs without jar signature: {result['observed_without_jar_signature_count']}")
    print(f"Compiled java units: {result['compiled_java_unit_count']}")
    print(
        "Runtime verification: "
        f"{result['runtime_verification_run_count']} runs on "
        f"{result['runtime_verification_device_count']} device; "
        f"{result['runtime_verified_blueprint_count']} blueprints with evidence "
        f"({result['runtime_passed_blueprint_count']} passed, "
        f"{result['runtime_partial_only_blueprint_count']} partial-only), "
        f"{result['runtime_verified_module_count']} modules, "
        f"{result['runtime_verified_feature_count']} features, "
        f"{result['runtime_verified_unit_count']} units, "
        f"{result['runtime_verified_api_count']} APIs"
    )
    print(
        "Build verification: "
        f"{result['build_verification_run_count']} runs; "
        f"{result['build_verified_blueprint_count']} workspace blueprints, "
        f"{result['isolated_build_verified_blueprint_count']} isolated blueprints, "
        f"{result['incremental_build_variant_count']} incremental host variants"
    )
    if result["compile_skipped_reason"]:
        print(f"Compile note: {result['compile_skipped_reason']}")
    print(f"Structural gaps: {result['structural_gap_count']}")
    for name, gaps in result["gap_groups"].items():
        if gaps:
            print(f"{name}: {len(gaps)}")
            for gap in gaps[:10]:
                print(f"- {gap}")

def main():
    args = parse_args()
    result = audit(args)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)
    if args.strict and result["structural_gap_count"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
