# Simple Code Extraction Rules

Use this reference when expanding the Meishe Android Streaming SDK API skill from the official demo. The official demo and Doxygen folders are build-time learning sources only. A finished skill must work after those external folders are removed.

## Independence Boundary

- Do not require `SdkDemo` or `doxygen` at skill use time.
- Do not bundle the full demo source tree, full demo assets, signing configs, analytics keys, private package names, release tasks, debug servers, or large model directories.
- Keep only compact simple code, source labels, call-order knowledge, module contracts, resource checklists, lightweight sample assets, templates, and user-provided resource hooks.
- Source paths and line numbers are provenance labels. They are evidence, not runtime dependencies.

## Simple Code Unit

Each reusable simple code unit should include:

The machine-readable source of truth is `simple-code-registry.json`. Legacy
`demo-simple-snippets-*.md` blocks are retained as `evidence_fragment` records;
their ids remain stable, but incomplete context blocks must not be emitted as
generated Android code.

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier, usually `<capability>-<sequence>` or an existing snippet id such as `timeline-editing-001`. |
| `feature` | User-facing function or demo module using the code. |
| `source_label` | Demo source path and line number label only. |
| `scenario` | Demo scene that proves the code path. |
| `api_classes` | SDK classes touched by the snippet. |
| `api_signatures` | Exact `Owner#member(JVMDescriptor)` or `Owner#field:JVMDescriptor` ids implemented by a semantic unit. |
| `requires` | Objects/state that must exist before the snippet runs. |
| `inputs` | Parameters, resources, permissions, files, package ids, or user choices consumed by the snippet. |
| `provides` | SDK object, state mutation, package id, output file, or UI state produced by the snippet. |
| `resources` | `R*` resource keys from `resource-requirements-index.md`. |
| `threading` | UI thread, GL thread, background thread, or callback gate. |
| `guards` | Null checks, boolean result checks, package status checks, time-range checks, model gates, or state conflicts. |
| `failure` | Observable failure handling expected in generated apps. |
| `compose_after` | API bricks, recipes, or modules that must precede this snippet. |
| `compose_after_units` | Exact semantic unit ids that form the executable DAG predecessors. |
| `lifecycle_hook` | One fixed lifecycle mount point defined by `module-contract-schema.md`. |
| `compose_into` | Small modules, big modules, or app blueprints that can consume this snippet. |

## Extraction Levels

| Level | Output | Rule |
| --- | --- | --- |
| API statement | One SDK call or constant use. | Keep in exhaustive/constraint maps unless it is independently useful. |
| API brick | One stable SDK object or operation, such as `NvsStreamingContext.getInstance()`. | Document preconditions, result, and guards. |
| API recipe | Ordered calls that produce a usable SDK state, such as timeline creation or asset install. | Prefer pseudocode or compact Java, not full Activity code. |
| Small module | Feature block such as caption editor, sticker editor, filter, transition, music, or export. | Bind to recipes, resources, and parent module rules. |
| Big module | Product workflow such as editor, camera, asset center, template app, or PIP. | Compose small modules by dependency closure. |
| App blueprint | Full app shape with navigation and default modules. | Keep UI replaceable and do not copy Demo screens wholesale. |

## What To Keep

- SDK call order that is required for correctness.
- State ownership patterns such as `TimelineData`-style project state.
- Return value and callback gates.
- Lifecycle guards: stop playback/capture/export before structural mutation.
- Resource and model requirements.
- Minimal code blocks that can be transplanted into project-local controllers.
- Demo-proven UI workflow shape only when it affects correctness, such as media selection before `VideoEditActivity`.

## What To Rewrite

- Activity/Fragment code should become project-local controllers or concise Activity examples.
- Demo presenters, adapters, and view models should become module contracts unless their SDK logic is essential.
- Material network clients are not retained. Replace them with the skill-owned local catalog/install boundary; online-interface and `.lic` acquisition questions go to Meishe business.
- Large workflows that cannot be safely minimized should become API recipes and sequence diagrams rather than copied source.

## Extraction Workflow

1. Identify the demo feature from `demo-feature-list.md`.
2. Search exact SDK calls in `demo-simple-snippets-*.md`, `demo-api-touchpoints.md`, and `demo-simple-snippets-exhaustive-statements.md`.
3. Classify the code as API brick, API recipe, small module, big module, or app blueprint.
4. Record source labels and existing snippet ids.
5. Add resource keys from `resource-requirements-index.md`.
6. Add call-order and conflict rules from `demo-api-dependency-graph.md`, `demo-feature-dependency-graph.md`, and `demo-api-call-order-map.md`.
7. Update `demo-feature-simple-code-map.md`, `demo-api-simple-code-map.md`, and `sdk-module-registry.json`.
8. Run `audit_simple_code_coverage.py`.

## Acceptance Rules

- A feature is `mapped` when it has a module id, resource keys, at least one valid `java_unit` or `recipe`, and a dependency path.
- A feature is `recipe-only` when the correct reusable output is a sequence/contract rather than a code block.
- A feature is `workflow-only` when it is mainly navigation, permission, or UI shell and SDK logic is delegated to child modules.
- A feature is `coverage_gap` only when it cannot be implemented from existing snippets, recipes, docs, and demo-derived maps.
- Every observed API must be `evidence_only`, `contract_only`, `compiled_unit`, `generated_module`, or `runtime_verified`; `evidence_only` requires a reason.
- P0/P1 APIs must map to a direct unit or composed recipe.
- Every `java_unit` must have balanced code and compile against the selected SDK jar and Android platform jar.
- A `java_unit` that implements an overloaded API must bind its exact overload through `api_signatures`; a class/member-name fallback is not implementation coverage.
- Every unit must use one of the fixed lifecycle hooks documented in `module-contract-schema.md`.
