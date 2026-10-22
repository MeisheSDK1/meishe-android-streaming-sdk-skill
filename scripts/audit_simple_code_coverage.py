#!/usr/bin/env python3
"""Audit simple-code and module coverage for the Meishe Android SDK skill.

This script is self-contained and reads only bundled skill references.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on structural gaps.")
    return parser.parse_args()

def skill_dir():
    return Path(__file__).resolve().parents[1]

def load_json(relative_path):
    with (skill_dir() / relative_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)

def count_api_family_rows():
    path = skill_dir() / "references" / "demo-api-simple-code-map.md"
    if not path.exists():
        return 0
    count = 0
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| API family / class |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            if line.startswith("| ---"):
                continue
            count += 1
    return count

def audit():
    root = skill_dir()
    registry = load_json("references/sdk-module-registry.json")
    modules = {module["id"]: module for module in registry.get("modules", [])}
    blueprints = {blueprint["id"]: blueprint for blueprint in registry.get("blueprints", [])}
    recipes = {recipe["id"]: recipe for recipe in registry.get("api_recipes", [])}
    features = registry.get("demo_feature_coverage", [])

    missing_modules = []
    missing_recipe_refs = []
    missing_blueprint_modules = []
    missing_dependency_refs = []
    missing_recipe_dependency_refs = []
    missing_blueprint_template_dirs = []
    missing_blueprint_template_files = []
    blueprint_template_root = root / "assets" / "android-blueprint-templates"

    for feature in features:
        module_id = feature.get("module_id")
        if module_id and module_id not in modules:
            missing_modules.append({"feature": feature.get("feature"), "module_id": module_id})

    for module in modules.values():
        for required in module.get("requires", []):
            if required not in modules:
                missing_dependency_refs.append({"module": module["id"], "requires": required})
        for recipe_id in module.get("api_recipes", []):
            if recipe_id not in recipes:
                missing_recipe_refs.append({"module": module["id"], "api_recipe": recipe_id})

    for recipe in recipes.values():
        for required in recipe.get("requires", []):
            if required not in modules and required not in recipes:
                missing_recipe_dependency_refs.append({"api_recipe": recipe["id"], "requires": required})

    for blueprint in blueprints.values():
        for module_id in blueprint.get("modules", []):
            if module_id not in modules:
                missing_blueprint_modules.append({"blueprint": blueprint["id"], "module_id": module_id})
        app_template = blueprint.get("app_template")
        if not app_template:
            continue
        template_dir = blueprint_template_root / app_template
        if not template_dir.is_dir():
            missing_blueprint_template_dirs.append({
                "blueprint": blueprint["id"],
                "app_template": app_template,
            })
            continue
        required_files = (
            Path("app/src/main/AndroidManifest.xml"),
            Path("app/src/main/java/{{PACKAGE_PATH}}/MainActivity.java"),
        )
        for relative_path in required_files:
            if not (template_dir / relative_path).is_file():
                missing_blueprint_template_files.append({
                    "blueprint": blueprint["id"],
                    "file": str(relative_path).replace("\\", "/"),
                })

    base_template_root = root / "assets" / "android-template"
    required_base_template_files = (
        Path("build.gradle"),
        Path("settings.gradle"),
        Path("gradlew"),
        Path("gradlew.bat"),
        Path("gradle/wrapper/gradle-wrapper.jar"),
        Path("gradle/wrapper/gradle-wrapper.properties"),
        Path("app/build.gradle"),
        Path("app/src/main/AndroidManifest.xml"),
    )
    missing_base_template_files = [
        str(relative_path).replace("\\", "/")
        for relative_path in required_base_template_files
        if not (base_template_root / relative_path).is_file()
    ]

    coverage_counts = Counter(feature.get("coverage", "unknown") for feature in features)
    no_simple_refs = [
        feature.get("feature")
        for feature in features
        if not feature.get("simple_code_refs") and feature.get("coverage") != "workflow-only"
    ]
    snippet_groups = set()
    for module in modules.values():
        snippet_groups.update(module.get("simple_code_refs", []))
    for recipe in recipes.values():
        snippet_groups.update(recipe.get("simple_code_refs", []))

    structural_gaps = (
        missing_modules
        + missing_recipe_refs
        + missing_blueprint_modules
        + missing_dependency_refs
        + missing_recipe_dependency_refs
        + missing_blueprint_template_dirs
        + missing_blueprint_template_files
        + missing_base_template_files
    )
    result = {
        "external_demo_required_at_use_time": registry.get("independence", {}).get("external_demo_required", True),
        "external_doxygen_required_at_use_time": registry.get("independence", {}).get("external_doxygen_required", True),
        "module_count": len(modules),
        "blueprint_count": len(blueprints),
        "api_recipe_count": len(recipes),
        "demo_feature_total": len(features),
        "demo_feature_coverage": dict(sorted(coverage_counts.items())),
        "api_family_rows": count_api_family_rows(),
        "simple_code_ref_count": len(snippet_groups),
        "features_without_simple_refs": no_simple_refs,
        "missing_feature_module_refs": missing_modules,
        "missing_module_dependency_refs": missing_dependency_refs,
        "missing_recipe_dependency_refs": missing_recipe_dependency_refs,
        "missing_module_recipe_refs": missing_recipe_refs,
        "missing_blueprint_module_refs": missing_blueprint_modules,
        "missing_blueprint_template_dirs": missing_blueprint_template_dirs,
        "missing_blueprint_template_files": missing_blueprint_template_files,
        "missing_base_template_files": missing_base_template_files,
        "structural_gap_count": len(structural_gaps),
    }
    return result

def print_text(result):
    print("Meishe Android SDK skill simple-code coverage audit")
    print(f"External Demo required at use time: {result['external_demo_required_at_use_time']}")
    print(f"External Doxygen required at use time: {result['external_doxygen_required_at_use_time']}")
    print(f"Modules: {result['module_count']}")
    print(f"Blueprints: {result['blueprint_count']}")
    print(f"API recipes: {result['api_recipe_count']}")
    print(f"Demo features: {result['demo_feature_total']}")
    print("Demo feature coverage:")
    for key, value in result["demo_feature_coverage"].items():
        print(f"- {key}: {value}")
    print(f"API family rows: {result['api_family_rows']}")
    print(f"Unique simple code refs: {result['simple_code_ref_count']}")
    print(f"Structural gaps: {result['structural_gap_count']}")
    for key in (
        "missing_feature_module_refs",
        "missing_module_dependency_refs",
        "missing_recipe_dependency_refs",
        "missing_module_recipe_refs",
        "missing_blueprint_module_refs",
        "missing_blueprint_template_dirs",
        "missing_blueprint_template_files",
        "missing_base_template_files",
    ):
        if result[key]:
            print(f"{key}:")
            for item in result[key]:
                print(f"- {item}")

def main():
    args = parse_args()
    result = audit()
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)
    if args.strict and result["structural_gap_count"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
