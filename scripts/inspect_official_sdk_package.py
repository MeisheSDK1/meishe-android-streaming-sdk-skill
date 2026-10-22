#!/usr/bin/env python3
"""Resolve skill resource requirements against an extracted official SDK package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sys
for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]

def resource_map() -> dict:
    path = skill_dir() / "references/official-sdk-download-resource-map.json"
    return json.loads(path.read_text(encoding="utf-8"))

def split_values(value: str) -> set[str]:
    return {item.strip() for item in value.replace(",", " ").split() if item.strip()}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-root", type=Path, required=True)
    parser.add_argument(
        "--resource-keys",
        default="",
        help="Optional comma/space-separated R keys, for example R0,R8,R9.",
    )
    parser.add_argument(
        "--modules",
        default="",
        help="Optional comma/space-separated module ids.",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args()

def record_selected(record: dict, keys: set[str], modules: set[str]) -> bool:
    if keys and not keys.intersection(record.get("resource_keys", [])):
        return False
    if modules and not modules.intersection(record.get("module_ids", [])):
        return False
    return True

def path_result(root: Path, relative_path: str, expected_kind: str) -> dict:
    resolved = root.joinpath(*relative_path.split("/"))
    exists = resolved.is_file() if expected_kind == "file" else resolved.is_dir()
    return {
        "relative_path": relative_path,
        "kind": expected_kind,
        "exists": exists,
        "resolved_path": str(resolved),
    }

def inspect(root: Path, keys: set[str], modules: set[str]) -> dict:
    manifest = resource_map()
    root = root.resolve()
    marker_results = [
        path_result(root, relative_path, "directory" if "." not in Path(relative_path).name else "file")
        for relative_path in manifest["observed_package"]["required_root_markers"]
    ]
    groups = []
    for group in manifest.get("resource_groups", []):
        if not record_selected(group, keys, modules):
            continue
        paths = [
            path_result(root, relative_path, "file")
            for relative_path in group.get("relative_files", [])
        ]
        paths.extend(
            path_result(root, relative_path, "directory")
            for relative_path in group.get("relative_directories", [])
        )
        groups.append(
            {
                "id": group["id"],
                "availability": group["availability"],
                "resource_keys": group.get("resource_keys", []),
                "module_ids": group.get("module_ids", []),
                "paths": paths,
                "copy_guidance": group.get("copy_guidance", []),
                "passed": all(item["exists"] for item in paths),
            }
        )
    families = []
    for family in manifest.get("asset_families", []):
        if not record_selected(family, keys, modules):
            continue
        result = path_result(root, family["relative_directory"], "directory")
        families.append(
            {
                "family": family["family"],
                "resource_keys": family.get("resource_keys", []),
                "module_ids": family.get("module_ids", []),
                **result,
            }
        )
    marker_passed = all(item["exists"] for item in marker_results)
    selected_paths_passed = all(group["passed"] for group in groups) and all(
        family["exists"] for family in families
    )
    return {
        "sdk_root": str(root),
        "official_download": manifest["official_download"],
        "resource_key_filter": sorted(keys),
        "module_filter": sorted(modules),
        "root_markers": marker_results,
        "resource_groups": groups,
        "asset_families": families,
        "not_present_in_observed_package": manifest.get(
            "not_present_in_observed_package", []
        ),
        "marker_passed": marker_passed,
        "selected_paths_passed": selected_paths_passed,
        "passed": marker_passed and selected_paths_passed,
    }

def print_text(result: dict) -> None:
    print(f"SDK root: {result['sdk_root']}")
    print(f"Official package markers: {'PASS' if result['marker_passed'] else 'FAIL'}")
    for group in result["resource_groups"]:
        print(f"[{group['id']}] {'PASS' if group['passed'] else 'FAIL'}")
        for item in group["paths"]:
            state = "found" if item["exists"] else "missing"
            print(f"  - {state}: {item['relative_path']}")
    for family in result["asset_families"]:
        state = "found" if family["exists"] else "missing"
        print(f"[asset:{family['family']}] {state}: {family['relative_path']}")
    if result["not_present_in_observed_package"]:
        print("Known package exclusions:")
        for item in result["not_present_in_observed_package"]:
            print(f"  - {item['resource']}: {item['scan_result']}")

def main() -> int:
    args = parse_args()
    result = inspect(
        args.sdk_root,
        split_values(args.resource_keys),
        split_values(args.modules),
    )
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)
    return 1 if args.strict and not result["passed"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
