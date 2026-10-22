import argparse
import json
from collections import Counter
from pathlib import Path
import sys

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")



SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_API_MAP = SKILL_DIR / "references" / "demo-api-simple-code-map.json"
DEFAULT_OUTPUT = SKILL_DIR / "references" / "p3-api-processing-scope.json"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Freeze the low-frequency P3 evidence-only API scope for staged processing."
    )
    parser.add_argument("--api-map", type=Path, default=DEFAULT_API_MAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--freeze-date", default="2026-08-04")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing frozen scope. Omit during normal validation.",
    )
    return parser.parse_args()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def frozen_rows(api_map):
    return sorted(
        (
            row
            for row in api_map.get("api_members", [])
            if row.get("priority") == "P3"
            and row.get("coverage_status") == "evidence_only"
            and int(row.get("occurrences", 0)) < 10
        ),
        key=lambda row: row["stable_id"],
    )


def build_scope(api_map, freeze_date):
    rows = frozen_rows(api_map)
    owner_counts = Counter(row["owner"] for row in rows)
    return {
        "schema_version": 1,
        "frozen_at": freeze_date,
        "description": (
            "Stage 9 immutable target set: low-frequency Demo-observed P3 members that "
            "were evidence_only when processing began."
        ),
        "filters": {
            "priority": "P3",
            "coverage_status": "evidence_only",
            "maximum_demo_occurrences_exclusive": 10,
            "requires_demo_evidence": True,
            "requires_jar_signature": True,
        },
        "target_count": len(rows),
        "kind_counts": dict(sorted(Counter(row["kind"] for row in rows).items())),
        "owner_counts": dict(sorted(owner_counts.items())),
        "target_stable_ids": [row["stable_id"] for row in rows],
    }


def main():
    args = parse_args()
    api_map = load_json(args.api_map.resolve())
    scope = build_scope(api_map, args.freeze_date)
    output = args.output.resolve()
    if output.exists() and not args.force:
        existing = load_json(output)
        if existing != scope:
            raise SystemExit(
                "Frozen P3 API scope differs from the current baseline. "
                "Use --force only when intentionally starting a new processing stage."
            )
        print(json.dumps({"status": "unchanged", "target_count": scope["target_count"]}, indent=2))
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(scope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "frozen", "target_count": scope["target_count"]}, indent=2))


if __name__ == "__main__":
    main()
