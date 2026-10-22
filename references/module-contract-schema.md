# Module Contract Schema

Use this schema to compose Meishe Android Streaming SDK features as building blocks. The implementation source of truth is `sdk-module-registry.json`; this document explains the fields and rules.

## Levels

| Level | Purpose | Example |
| --- | --- | --- |
| `api_brick` | Atomic SDK object or operation. | `streaming-context`, `asset-package-manager`, `live-window`. |
| `api_recipe` | Ordered API sequence that produces usable SDK state. | `timeline-build`, `connect-livewindow`, `install-asset-package`. |
| `small_module` | User-visible or reusable feature block. | `caption-editor`, `filter-editor`, `voiceover`, `transition-editor`. |
| `big_module` | Product workflow composed from small modules. | `short-video-editor`, `beauty-camera`, `template-editor`. |
| `app_blueprint` | Full application layout and default modules. | `camera-plus-editor`, `full-sdk-demo`, `incremental-integration`. |

## Required Fields

| Field | Applies to | Meaning |
| --- | --- | --- |
| `id` | all | Stable module id used by `compose_modules.py` and `create_android_project.py`. |
| `title` | all | Human-readable name. |
| `level` | all | One of the levels above. |
| `priority` | all | `P0`, `P1`, `P2`, or `P3`. |
| `category` | all | Capability group aligned with existing demo maps. |
| `aliases` | modules/blueprints | Natural-language terms used for query matching. |
| `requires` | modules/recipes | Required predecessor module ids. Dependencies are satisfied by capability, not demo class identity. |
| `provides` | modules/recipes | SDK object, state, UI workflow, or output the module creates. |
| `api_recipes` | modules/blueprints | Ordered recipe ids to load for implementation. |
| `simple_code_refs` | modules/recipes | Snippet ids, snippet files, or recipe labels used as reusable code evidence. |
| `simple_code_ids` | modules/recipes/blueprints | Exact `java_unit` or `recipe` ids from `simple-code-registry.json`; use these for composition and generation. |
| `render_units` | modules | Unit ids rendered or staged by generators for this module. |
| `manifest` | modules | Additive Android Manifest requirements such as permissions, activities, and metadata. |
| `gradle` | modules | Additive Gradle contract, including local SDK jar dependency expectations. |
| `resource_contract` | modules | Resource keys and user-provided runtime artifact requirements. |
| `navigation` | modules | Entry points and whether the host or product shell owns navigation. |
| `host_contract` | modules | Java/Kotlin host integration rules, threading boundary, and non-overwrite policy. |
| `resources` | modules/blueprints | `R*` keys from `resource-requirements-index.md`. |
| `permissions` | modules/blueprints | Android permissions needed by the module. |
| `template_features` | modules/blueprints | Existing generator overlays to apply. |
| `app_template` | blueprints | Optional standalone Activity/layout template under `assets/android-blueprint-templates`; only one product shell may be selected per generated app. |
| `guards` | modules/recipes | Preconditions, null checks, callback gates, package status checks, model gates. |
| `conflicts` | modules/recipes | State conflicts such as playback/export/capture mutation conflicts. |
| `lifecycle` | modules/recipes | Init, apply, refresh, teardown behavior. |
| `integration_modes` | modules | Supported modes: `new-app`, `incremental`, `api-only`. |

Incremental application is additive and transactional at the generator boundary: all generated target files are preflighted before host mutation, identical files are treated as unchanged, and any differing host file stops the operation before source, Manifest, or Gradle edits. `--force` may replace staging output but never conflicting host source. API-only composition emits the resolved controllers and a concrete usage sample; it does not imply that the host lifecycle, navigation, permissions, or object ownership can be omitted.
| `demo_evidence` | modules/features | Demo source labels or existing reference files proving behavior. |

## Simple Code Schema v2

`simple-code-registry.json` uses schema version 2. Every unit includes `schema_version`, `implementation_state`, `api_signatures`, `requires_modules`, `requires_capabilities`, `compose_after_units`, and `lifecycle_hook`.

`api_signatures` contains exact stable API ids in the form
`Owner#member(JVMDescriptor)` or `Owner#field:JVMDescriptor`. It is the
authoritative binding for overloaded members. `api_members` remains a
human-readable lookup aid and must not be used to choose between overloads.

`lifecycle_hook` must be one of:

- `sdk_init`
- `activity_create`
- `timeline_created`
- `live_window_bound`
- `asset_installed`
- `before_structural_mutation`
- `after_mutation_refresh`
- `destroy`

Allowed implementation and coverage states:

| State | Meaning |
| --- | --- |
| `evidence_only` | Demo or reference evidence exists, but no independent code or contract should be emitted as implementation. |
| `contract_only` | The API/module contract is known from jar signatures/docs/registry, but no compiled implementation unit is bundled. |
| `compiled_unit` | A skill-owned Java method or transitive feature recipe backed by Java units compiles against the SDK jar and Android jar. |
| `generated_module` | A recipe/module can be generated from ordered real unit ids, but is not itself a standalone Java method. |
| `runtime_verified` | Reserved for future device/emulator verification evidence. |

Recipe `steps` and `compose_after_units` reference real unit ids. Legacy `demo-simple-snippets-*` ids remain evidence/provenance and are not emitted as code unless converted into a v2 unit.

## Composition Rules

1. Resolve hard dependencies recursively through `requires`.
2. Preserve requested flexibility: a custom project controller can satisfy a module if it provides the same object/state and obeys the same guards.
3. Add optional modules only when requested by the user, selected by a blueprint, or required by a downstream module.
4. For feature modules with packaged assets, include `asset-package-service` and list the relevant `R*` resource keys.
5. For complete apps, select an `app_blueprint` first, then expand modules and recipes.
6. Apply at most one `app_template`. Add extra capabilities through modules so a second product shell cannot overwrite the first shell's navigation and Manifest.
7. For incremental integration, stage generated Java controllers and `patch-manifest.json` by default. Apply into a host project only when `--apply` is supplied.
8. For API-only output, resolve the minimum required unit chain and emit only `controllers/`, `sample/`, `deps/`, and `patch-manifest.json`.
9. Treat `simple_code_refs` as provenance and `simple_code_ids` as executable/composable knowledge. Never emit an `evidence_fragment` as code without converting it to a validated unit.
10. For an exact stable API query, bind through `api_signatures`, then expand only `compose_after_units`; do not infer a blueprint or unrelated sibling modules.
11. The unit DAG must preserve these transitive orders: Timeline creation before Clip insertion, LiveWindow connection before playback, and `java.engine.stop` before Timeline structural mutation, Timeline release, compile configuration, or export.

## Independence Rules

- `compose_modules.py` and `create_android_project.py` must read only files inside the skill and user-provided SDK/resource paths.
- `extract_demo_simple_code.py` may read an external Demo root only during skill construction or refresh.
- Registry source paths are labels; do not open them at skill use time.
- Large models are not bundled and must be selected from the mapped official Android LTS face-package paths, or supplied as equivalent authorized files. Production assets remain explicit authorized inputs.
