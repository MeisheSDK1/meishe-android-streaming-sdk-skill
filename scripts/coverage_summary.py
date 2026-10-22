#!/usr/bin/env python3
"""Generate and validate the skill's current coverage summary."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from reference_markdown import render_markdown_contents

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

CURRENT_MARKER_START = "<!-- BEGIN GENERATED CURRENT COVERAGE -->"
CURRENT_MARKER_END = "<!-- END GENERATED CURRENT COVERAGE -->"
CAPABILITY_MARKER_START = "<!-- BEGIN GENERATED CAPABILITY COVERAGE -->"
CAPABILITY_MARKER_END = "<!-- END GENERATED CAPABILITY COVERAGE -->"
LEGACY_METRIC_LITERALS = ("99/99", "377/377", "1491")
LEGACY_METRIC_FILES = {"SKILL.md", "demo-coverage-audit.md"}

def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def build_coverage_summary(root: Path) -> dict:
    references = root / "references"
    api_map = load_json(references / "demo-api-simple-code-map.json")
    simple_registry = load_json(references / "simple-code-registry.json")
    feature_map = load_json(references / "demo-feature-simple-code-map.json")
    module_registry = load_json(references / "sdk-module-registry.json")
    runtime_matrix = load_json(references / "runtime-verification-matrix.json")
    build_matrix = load_json(references / "build-verification-matrix.json")
    p3_processing = load_json(references / "p3-api-processing.json")

    api_members = api_map.get("api_members", [])
    units = simple_registry.get("units", [])
    runtime_runs = runtime_matrix.get("runs", [])
    runtime_result_counts = Counter(run.get("runtime_result") for run in runtime_runs)
    evidence_runs = [
        run for run in runtime_runs if run.get("runtime_result") in {"passed", "partial"}
    ]
    passed_blueprints = {
        run.get("blueprint_id")
        for run in runtime_runs
        if run.get("runtime_result") == "passed" and run.get("blueprint_id")
    }
    evidence_blueprints = {
        run.get("blueprint_id") for run in evidence_runs if run.get("blueprint_id")
    }

    def verified_ids(field: str) -> set[str]:
        return {
            item
            for run in evidence_runs
            for item in run.get(field, [])
            if item
        }

    build_runs = build_matrix.get("runs", [])
    passed_build_runs = [run for run in build_runs if run.get("result") == "passed"]
    build_blueprints = {
        blueprint_id
        for run in passed_build_runs
        for blueprint_id in run.get("blueprint_ids", [])
        if blueprint_id
    }

    return {
        "schema_version": 1,
        "description": (
            "Generated current coverage summary. Historical Demo token and evidence-fragment "
            "counts are intentionally excluded from implementation coverage."
        ),
        "sources": [
            "references/demo-api-simple-code-map.json",
            "references/simple-code-registry.json",
            "references/demo-feature-simple-code-map.json",
            "references/sdk-module-registry.json",
            "references/runtime-verification-matrix.json",
            "references/build-verification-matrix.json",
            "references/p3-api-processing.json",
        ],
        "api": {
            "type_count": api_map.get("type_count", 0),
            "member_count": api_map.get("member_count", len(api_members)),
            "observed_method_count": api_map.get("observed_method_count", 0),
            "coverage": dict(
                sorted(Counter(row.get("coverage_status") for row in api_members).items())
            ),
        },
        "simple_code": {
            "unit_count": len(units),
            "kinds": dict(sorted(Counter(unit.get("kind") for unit in units).items())),
            "implementation_states": dict(
                sorted(Counter(unit.get("implementation_state") for unit in units).items())
            ),
        },
        "p3_processing": {
            "target_count": p3_processing.get("target_count", 0),
            "processed_count": p3_processing.get("processed_count", 0),
            "upgraded_count": p3_processing.get("upgraded_count", 0),
            "retained_evidence_count": p3_processing.get(
                "retained_evidence_count", 0
            ),
            "coverage_counts": p3_processing.get("coverage_counts", {}),
            "domain_counts": p3_processing.get("domain_counts", {}),
            "reason_code_counts": p3_processing.get("reason_code_counts", {}),
            "unclassified_count": p3_processing.get("unclassified_count", 0),
            "missing_module_count": p3_processing.get("missing_module_count", 0),
            "generic_reason_count": p3_processing.get("generic_reason_count", 0),
        },
        "composition": {
            "feature_count": len(feature_map.get("features", [])),
            "module_count": len(module_registry.get("modules", [])),
            "blueprint_count": len(module_registry.get("blueprints", [])),
        },
        "runtime": {
            "run_count": len(runtime_runs),
            "result_counts": dict(sorted(runtime_result_counts.items())),
            "blueprints_with_evidence_count": len(evidence_blueprints),
            "blueprints_with_passed_run_count": len(passed_blueprints),
            "blueprints_with_partial_only_count": len(evidence_blueprints - passed_blueprints),
            "verified_module_count": len(verified_ids("verified_modules")),
            "verified_feature_count": len(verified_ids("verified_features")),
            "verified_unit_count": len(verified_ids("verified_units")),
            "verified_api_count": len(verified_ids("verified_api_ids")),
        },
        "build": {
            "run_count": len(build_runs),
            "passed_run_count": len(passed_build_runs),
            "verified_blueprint_count": len(build_blueprints),
        },
    }

def render_current_coverage(summary: dict) -> str:
    api = summary["api"]
    coverage = api["coverage"]
    simple = summary["simple_code"]
    composition = summary["composition"]
    runtime = summary["runtime"]
    build = summary["build"]
    p3 = summary["p3_processing"]
    return "\n".join(
        [
            CURRENT_MARKER_START,
            "| Surface | Metric | Current result | Coverage meaning |",
            "| --- | --- | ---: | --- |",
            f"| API v2 | SDK types | {api['type_count']} | Exact owners from the bundled SDK signature map. |",
            f"| API v2 | Exact members | {api['member_count']} | Fields, constructors, methods, and overload descriptors. |",
            f"| API v2 | Demo-observed methods | {api['observed_method_count']} | Methods associated with retained Demo evidence. |",
            f"| API implementation | `compiled_unit` | {coverage.get('compiled_unit', 0)} | Exact member has a compilable skill-owned unit. |",
            f"| API implementation | `contract_only` | {coverage.get('contract_only', 0)} | Exact contract exists, but no exact compilable unit exists yet. |",
            f"| API implementation | `evidence_only` | {coverage.get('evidence_only', 0)} | Demo evidence exists; it is not counted as generated implementation. |",
            f"| Low-frequency P3 processing | Upgraded / retained | {p3['upgraded_count']} / {p3['retained_evidence_count']} | Frozen {p3['target_count']}-member scope; retained members have member-level domains, modules, recipes, constraints, and explicit reasons. |",
            f"| Simple Code v2 | Semantic units | {simple['unit_count']} | {simple['kinds'].get('java_unit', 0)} `java_unit` and {simple['kinds'].get('recipe', 0)} `recipe` entries. |",
            f"| Composition | Demo features | {composition['feature_count']} | Features have dedicated recipes and module mappings. |",
            f"| Composition | Modules / blueprints | {composition['module_count']} / {composition['blueprint_count']} | Dependency-closed modules and application shells. |",
            f"| Runtime evidence | Device runs | {runtime['run_count']} | {runtime['result_counts'].get('passed', 0)} passed and {runtime['result_counts'].get('partial', 0)} partial runs. |",
            f"| Runtime evidence | Blueprints with evidence | {runtime['blueprints_with_evidence_count']} | {runtime['blueprints_with_passed_run_count']} have a passed run; {runtime['blueprints_with_partial_only_count']} have partial-only evidence. |",
            f"| Runtime evidence | Modules / features / units / APIs | {runtime['verified_module_count']} / {runtime['verified_feature_count']} / {runtime['verified_unit_count']} / {runtime['verified_api_count']} | Applies only to exact recorded flows and resources. |",
            f"| Build evidence | Runs / blueprints | {build['run_count']} / {build['verified_blueprint_count']} | Build evidence never implies physical-device behavior. |",
            CURRENT_MARKER_END,
        ]
    )

def render_capability_coverage(summary: dict) -> str:
    api = summary["api"]
    coverage = api["coverage"]
    simple = summary["simple_code"]
    composition = summary["composition"]
    runtime = summary["runtime"]
    p3 = summary["p3_processing"]
    return "\n".join(
        [
            CAPABILITY_MARKER_START,
            "| Area | Current skill coverage | Boundary |",
            "| --- | --- | --- |",
            f"| Demo features | {composition['feature_count']} feature recipes mapped into {composition['module_count']} modules. | A recipe or mapping is not automatically a generated or device-verified implementation. |",
            f"| Exact API contracts | {api['type_count']} SDK types, {api['member_count']} exact members, and {api['observed_method_count']} Demo-observed methods. | SDK surfaces absent from both Demo and bundled official references remain out of scope. |",
            f"| API implementation | {coverage.get('compiled_unit', 0)} compiled, {coverage.get('contract_only', 0)} contract-only, and {coverage.get('evidence_only', 0)} evidence-only members. | Contract/evidence states must not be reported as generated implementation. |",
            f"| Low-frequency P3 APIs | {p3['upgraded_count']} of the frozen {p3['target_count']} members now have exact compiled units; {p3['retained_evidence_count']} retain explicit member-level reasons. | Constants, callbacks, diagnostic getters, value objects, and owned lifecycle operations are not promoted with meaningless wrapper code. |",
            f"| Simple Code | {simple['unit_count']} semantic units: {simple['kinds'].get('java_unit', 0)} compilable Java units and {simple['kinds'].get('recipe', 0)} recipes. | Historical evidence fragments prove Demo usage only. |",
            f"| Application generation | {composition['blueprint_count']} blueprints with dependency-closed module plans. | Product depth varies by blueprint and resource gate. |",
            f"| Physical-device evidence | {runtime['run_count']} runs across {runtime['blueprints_with_evidence_count']} blueprints; {runtime['blueprints_with_passed_run_count']} blueprints have passed runs and {runtime['blueprints_with_partial_only_count']} are partial-only. | Read the runtime matrix before making any runtime claim. |",
            CAPABILITY_MARKER_END,
        ]
    )

def render_p3_processing(summary: dict) -> str:
    p3 = summary["p3_processing"]
    domain_rows = [
        f"| `{domain_id}` | {count} |"
        for domain_id, count in sorted(p3["domain_counts"].items())
    ]
    reason_rows = [
        f"| `{reason_code}` | {count} |"
        for reason_code, count in sorted(p3["reason_code_counts"].items())
    ]
    return "\n".join(
        [
            "# Low-Frequency P3 API Processing",
            "",
            "This file is generated from `p3-api-processing.json`. The frozen scope contains "
            f"{p3['target_count']} Demo-observed P3 members with fewer than 10 occurrences.",
            "",
            "## Result",
            "",
            "| Metric | Count |",
            "| --- | ---: |",
            f"| Processed | {p3['processed_count']} |",
            f"| Upgraded to exact compiled units | {p3['upgraded_count']} |",
            f"| Retained as evidence with explicit reasons | {p3['retained_evidence_count']} |",
            f"| Unclassified | {p3['unclassified_count']} |",
            f"| Missing module mapping | {p3['missing_module_count']} |",
            f"| Generic retention reasons | {p3['generic_reason_count']} |",
            "",
            "An upgraded member must reference a real `java_unit`. A retained member keeps its exact jar signature, Demo evidence, member-level domains, modules, related recipes, constraints, and a specific reason. Constants, callbacks, diagnostic getters, value objects, OpenGL operations, and caller-owned lifecycle operations are not promoted with empty wrapper code.",
            "",
            "## Domain Mapping",
            "",
            "| Domain | Frozen members |",
            "| --- | ---: |",
            *domain_rows,
            "",
            "## Retention Reasons",
            "",
            "| Reason code | Retained members |",
            "| --- | ---: |",
            *reason_rows,
            "",
            "Use `p3-api-processing-scope.json` for the immutable member list and `p3-api-processing.json` for per-member status. These files are skill-owned runtime knowledge and do not require the external Demo or Doxygen tree.",
            "",
        ]
    )

def replace_generated_section(text: str, start: str, end: str, replacement: str) -> str:
    start_index = text.find(start)
    end_index = text.find(end)
    if start_index < 0 or end_index < start_index:
        raise ValueError(f"missing generated markers: {start} ... {end}")
    end_index += len(end)
    return text[:start_index] + replacement + text[end_index:]

def expected_artifacts(root: Path, summary: dict) -> dict[Path, str]:
    references = root / "references"
    summary_path = references / "coverage-summary.json"
    p3_processing_path = references / "p3-api-processing.md"
    coverage_path = references / "demo-feature-api-simple-coverage.md"
    capability_path = references / "capability-catalog.md"
    coverage_text = coverage_path.read_text(encoding="utf-8")
    capability_text = capability_path.read_text(encoding="utf-8")
    artifacts = {
        summary_path: json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        p3_processing_path: render_p3_processing(summary),
        coverage_path: replace_generated_section(
            coverage_text,
            CURRENT_MARKER_START,
            CURRENT_MARKER_END,
            render_current_coverage(summary),
        ),
        capability_path: replace_generated_section(
            capability_text,
            CAPABILITY_MARKER_START,
            CAPABILITY_MARKER_END,
            render_capability_coverage(summary),
        ),
    }
    return {
        path: (
            render_markdown_contents(content)
            if path.suffix == ".md"
            else content
        )
        for path, content in artifacts.items()
    }

def coverage_artifact_gaps(root: Path) -> list[dict]:
    summary = build_coverage_summary(root)
    gaps = []
    try:
        artifacts = expected_artifacts(root, summary)
    except (OSError, ValueError) as error:
        return [{"kind": "coverage_artifact", "reason": str(error)}]
    for path, expected in artifacts.items():
        if not path.is_file():
            gaps.append({"kind": "coverage_artifact", "file": path.name, "reason": "missing"})
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected:
            gaps.append(
                {
                    "kind": "coverage_artifact",
                    "file": path.name,
                    "reason": "generated coverage content is stale",
                }
            )

    for path in [root / "SKILL.md", *(root / "references").glob("*.md")]:
        text = path.read_text(encoding="utf-8")
        found = [literal for literal in LEGACY_METRIC_LITERALS if literal in text]
        if found and path.name not in LEGACY_METRIC_FILES:
            gaps.append(
                {
                    "kind": "legacy_metric",
                    "file": path.name,
                    "values": found,
                    "reason": "historical evidence metrics appear outside an approved legacy section",
                }
            )
    legacy_audit = (root / "references" / "demo-coverage-audit.md").read_text(
        encoding="utf-8"
    )
    if "Historical Evidence-Layer Coverage Audit" not in legacy_audit:
        gaps.append(
            {
                "kind": "legacy_metric",
                "file": "demo-coverage-audit.md",
                "reason": "historical metrics are not explicitly labeled",
            }
        )
    return gaps

def write_coverage_artifacts(root: Path) -> None:
    summary = build_coverage_summary(root)
    for path, content in expected_artifacts(root, summary).items():
        path.write_text(content, encoding="utf-8")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Refresh generated artifacts.")
    parser.add_argument("--check", action="store_true", help="Fail when artifacts are stale.")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    root = skill_dir()
    if args.write:
        write_coverage_artifacts(root)
    gaps = coverage_artifact_gaps(root) if args.check else []
    result = {"summary": build_coverage_summary(root), "gaps": gaps}
    if args.as_json or not args.write:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.check and gaps:
        sys.exit(1)

if __name__ == "__main__":
    main()
