# Standalone Workflow

This skill is designed to work after the original `SdkDemo` and `doxygen` folders are unavailable. Use the bundled references and code templates as the source of procedural knowledge. Material binaries are external inputs and are not stored inside the skill.

For project creation or integration, read `execution-and-qa-handoff.md` and notify the user before implementation that Gradle is user-run by default. Recommend optional automatic physical-device screenshot analysis while disclosing its additional time and token cost; continue with implementation unless the user explicitly opts into automatic execution.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Evidence Model](#evidence-model)
- [External Requirements](#external-requirements)
- [Retrieval Optimization](#retrieval-optimization)
- [Generator Command Recipes](#generator-command-recipes)
- [Generation Steps](#generation-steps)
- [Do Not Do](#do-not-do)
- [Skill Maintenance And QA](#skill-maintenance-and-qa)
<!-- END GENERATED CONTENTS -->

## Evidence Model

1. Use demo-derived maps/snippets as the primary evidence for Android SDK 3.16.1.25 integration, call order, Gradle/Manifest wiring, permissions, and version-proven SDK usage.
2. Use `official-docs-index.md` to select the smallest official Doxygen-derived reference for API semantics, constraints, parameter names/ranges, error codes, and SDK limitations.
3. Use `skill-lookup-index.json` or `scripts/search_skill_index.py` before loading large references; it maps natural-language intent to candidate refs, snippet groups, resource keys, module ids, blueprint ids, and optional feature templates.
4. Use `module-contract-schema.md`, `sdk-module-registry.json`, `app-blueprints.md`, and `scripts/compose_modules.py` for broad app generation, user-selected capability composition, or incremental API integration. The resolver must add prerequisite modules by dependency closure while still allowing optional modules to be omitted.
5. Use `resource-requirements-index.md` whenever a requested feature depends on proprietary SDK artifacts, user media, models, packages, fonts, permissions, or output paths.
6. Use `official-sdk-download-resources.md`, `official-sdk-download-resource-map.json`, and `scripts/inspect_official_sdk_package.py` to resolve missing runtime, helper library, model, and Demo material files from a user-downloaded official Android LTS face package.
7. Use `default-sample-assets.md` for the external small offline bundle layout, first-run effect demos, and sample package ids. Disclose the external-resource requirement before generation.
8. Use `asset-center-workflow.md` for the external local-material catalog, package install/upgrade, font registration, unavailable template slots, and the Meishe-business boundary for material, service, or `.lic` questions.
9. Use `capability-catalog.md` for first-time users, SDK/skill capability discovery, vague product goals, and "what can it do" questions.
10. Use `demo-validated-editor-architecture.md` for complete short-video editors, editor-first 0-to-1 apps, media selection -> ratio -> editor flows, and generated apps where subtitles/stickers/filters must be bound to a real editing page.
11. Use `simple-code-registry.json`, `demo-feature-simple-code-map.json`, and `demo-api-simple-code-map.json` to verify exact semantic units, recipes, resource gates, API coverage status, and module contracts. Use the matching Markdown maps only for concise human-readable routing.
12. Use `demo-feature-priority-map.md` and `demo-api-priority-map.md` for broad requests, implementation ordering, must-have APIs/modules, and missing-impact analysis.
13. Use `demo-api-dependency-graph.md` and `demo-feature-dependency-graph.md` for call chains, module dependencies, minimum subgraph selection, state conflicts, callback gates, and teardown rules.
14. Use `demo-feature-list.md` for feature/workflow requests; it is the implementation-facing map from demo features to source labels, primary SDK classes, and simple coverage.
15. Use `demo-api-list.md` for API/class/member requests; it is the capability-facing map from SDK APIs to demo evidence and simple/expanded coverage.
16. Use `demo-api-constraint-map.md` for preconditions, guard tags, parameter/return handling, and observed method call shapes.
17. Use `demo-sdk-constants-map.md` for built-in constants, nested callback/type names, template constants, and typed FX parameter keys.
18. Use `demo-api-call-order-map.md` for demo-proven feature-flow sequencing when composing new functionality.
19. Use `demo-feature-api-simple-coverage.md` for feasibility, "full coverage", or "can the skill build a robust project" questions.
20. Use `demo-simple-snippets-index.md` to select Demo evidence for the requested feature/API. Do not treat legacy snippets as composable code unless a semantic unit references them.
21. Use `rg` across `demo-simple-snippets-*.md` for exact SDK class names, method names, effect keys, constants, or snippet ids before loading a large snippet file.
22. Use `demo-simple-snippets-rare-structural.md` for low-frequency, nested, field-level, callback, caption-span, watermark, template constant, or Effect SDK object usages.
23. Use `demo-simple-snippets-exhaustive-statements.md` only when checking full demo coverage for an exact SDK statement/constant.
24. Use `api-usage-index.md` for SDK class/method names and common call frequency.
25. Use `capability-map.md` to choose the implementation area and required API families.
26. Use `demo-derived-code-patterns.md` for broader proven Android call order and lifecycle snippets extracted from the demo.
27. Use `demo-reuse-inventory.md` when broad coverage, Gradle/Manifest patterns, module boundaries, or source-map evidence is needed.
28. Use `demo-api-touchpoints.md` and `demo-coverage-audit.md` when checking whether the skill covers every demo API token/member/source area.
29. Use `android-integration.md` for Gradle, permissions, ABI, license, and asset-package setup.
30. Use this skill's `assets/android-template` or `.codex/skills/meishe-android-streaming-sdk-api/scripts/create_android_project.py` when creating a new Android project from the project root. Prefer `--blueprint` and `--modules`; select optional overlays with `--features` only for requested capabilities or resolver output.
31. Match the generated UI language to the language used in the request. Pass `--ui-language zh-CN` for Chinese or `--ui-language en` for English; for other languages, finish localization before delivery and do not leave mixed-language labels or status text.
32. For timeline editor shells, use the chosen project width/height both to create the Timeline and to size the LiveWindow container. Set `FILLMODE_PRESERVEASPECTFIT` so preview coordinates and visible content agree with the project canvas.
33. Do not bind Trim directly to a selection action that seeks to the clip boundary. Ask for a valid retained range or move the playhead inside the selected clip, then stop playback, mutate, persist, refresh, and display the new duration.

If official docs and demo-derived references disagree, prefer demo-derived references for generated Android behavior, project wiring, state guards, and call sequencing. Use official docs for API meaning where the demo is silent, and state the assumption when the choice can affect app behavior.

## External Requirements

The skill is independent from `SdkDemo` and the original Doxygen folder, but generated apps still need proprietary Meishe SDK runtime artifacts:

- A valid `meishesdk.lic` or equivalent license file.
- Meishe SDK Java/AAR/JAR artifacts.
- Native libraries such as `libNvStreamingSdkCore.so` for the chosen ABI.
- Optional model and asset packages for face, segmentation, makeup, filters, stickers, themes, captions, and AR scene.
- Authorized lightweight sample packages may be supplied externally for offline first-run demos. In this repository they are staged at `temp_assets/android-sample-assets`; outside it, obtain material resources from Meishe business and pass their bundle root with `--sample-assets-dir`. Large `facemode` human-detection models are also external; obtain them from `<sdk-root>/samples/android/SdkDemo/app/src/main/assets/facemode` after downloading the official Android LTS face package.

Do not assume these proprietary binaries can be recreated from the skill. Ask the user for an extracted official package root or already authorized files, then resolve only relative paths recorded in `official-sdk-download-resource-map.json`. Production application/package licenses and online material interfaces are not supplied by the map and remain Meishe-business questions.

## Retrieval Optimization

For normal requests, run:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\search_skill_index.py "<user request>"
```

Use the returned `module_ids`/`blueprint_ids` with:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\compose_modules.py --blueprint short-video-editor --modules caption-editor,sticker-editor,filter-editor,asset-center-service
```

Use the returned `resource_keys` to read `resource-requirements-index.md`, `simple_code_ids` to load exact reusable units, `snippet_refs`/`simple_code_refs` only for supporting evidence, and `optional_template_features` to decide whether `create_android_project.py --features ...` is useful. The lookup result is a router, not a replacement for the module registry, constraint maps, or official docs.

Do not load every routed document automatically. Prefer the smallest exact reference or semantic unit that resolves the implementation decision. Use exact `rg`, `rg -l`, or `rg --count`; avoid emitting complete large reference files, XML trees, asset inventories, or broad match sets.

## Generator Command Recipes

Inspect the current CLI surface before generation:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py --help
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py --list-features
```

Create a minimal Java integration skeleton, or dry-run a dependency-closed blueprint plan:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --package com.example.meisheapp --app-name MeisheApp
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py --blueprint short-video-editor --modules caption-editor,sticker-editor,filter-editor,asset-center-service --dry-run-plan
```

Copy authorized SDK artifacts and a license from a local distribution:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --package com.example.meisheapp --app-name MeisheApp --sdk-root <path-to-sdk-root> --license <path-to-meishesdk.lic>
```

Add an authorized external offline material gallery, or explicitly generate without sample materials:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --features asset-center,effects,captions-stickers --sample-assets-dir <authorized-bundle-root> --sdk-root <path-to-sdk-root> --license <path-to-meishesdk.lic>
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --no-sample-assets
```

Select external human-detection models for AR, beauty, makeup, or segmentation:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --features beauty-ar --human-models-dir <path-to-facemode-or-parent>
```

Use the new-app, incremental, and api-only examples in `../SKILL.md` for the three product integration modes. Apply optional overlays only when requested by the user or returned by lookup/composition.

## Generation Steps

1. Convert the user request into capabilities: initialization, complete short-video editor, media source/import, capture, timeline editing, effects, beauty/makeup/AR, captions/stickers, assets, audio, export, or template editing.
2. Run the lookup script or read `skill-lookup-index.json` to get candidate references, snippet files, resource keys, module ids, blueprint ids, and optional templates.
3. Run `scripts/compose_modules.py` or `create_android_project.py --dry-run-plan` when the request is an app, a module set, or an incremental SDK integration. Use the resolved dependency closure as the implementation plan, then use `create_android_project.py --mode incremental` to stage Java controllers and `patch-manifest.json` for host projects.
4. For runtime-dependent features, read `resource-requirements-index.md` and `official-sdk-download-resources.md`; list the official package-relative source, project destination, and any remaining authorization requirement before claiming the generated app is runnable.
5. Before generating first-run demo effects, tell the user that material resources are not stored in the skill and must be obtained from Meishe business. Read `default-sample-assets.md`, resolve `temp_assets/android-sample-assets` or `--sample-assets-dir`, and install copied sample packages with `MeisheSampleAssets.installDefaultPackages(...)`.
6. For material-library requests, read `asset-center-workflow.md` and select `asset-center-service` or `--features asset-center`. This stable module id renders an offline catalog only; do not add service requests or a `baseUrl`.
7. For first-time users or vague product goals, load `capability-catalog.md` and explain SDK capability, skill capability, and runtime boundaries before proposing implementation.
8. For complete short-video editors, load `demo-validated-editor-architecture.md` and build the media selection -> ratio -> timeline state -> livewindow editor -> child modules -> export chain before deciding UI screens.
9. For broad or ambiguous implementation requests, load `demo-feature-priority-map.md` and `demo-api-priority-map.md` to decide P0/P1 foundations before loading snippets.
10. For custom composition, load `demo-api-dependency-graph.md` and `demo-feature-dependency-graph.md`, then extract the smallest required subgraph instead of copying a full demo workflow.
11. Load `demo-feature-list.md` for feature intent or `demo-api-list.md` for API intent, then load `demo-feature-simple-code-map.md`, `demo-api-simple-code-map.md`, `demo-api-constraint-map.md`, `demo-sdk-constants-map.md`, or `demo-api-call-order-map.md` when the implementation depends on coverage, parameter rules, constants, return checks, or workflow sequencing.
12. Load `official-docs-index.md` and `demo-simple-snippets-index.md`, then only the relevant official and demo-derived reference files for those capabilities.
13. For ordinary generation, prefer method-level category snippets after checking constraints. For coverage-sensitive work, read `demo-feature-api-simple-coverage.md`, then search `demo-simple-snippets-exhaustive-statements.md` and `demo-api-touchpoints.md` before assuming an API is unsupported.
14. Start from the bundled code template for new projects, or patch the user's existing Android project in its local style. All nine app blueprints include product shells; `incremental-integration` preserves the host project's UI by staging controllers and an additive patch manifest unless `--apply` is explicitly supplied.
15. Use optional feature templates only as starter controllers selected by the request or resolver output; keep final code free to compose or omit any module.
16. Keep Activity classes thin. Put SDK operations in small controllers/managers.
17. Add runtime permission handling before camera/audio/media operations.
18. Add callback handling for playback, capture, recording, asset package install, and compile/export.
19. Keep `NvsStreamingContext`/`NvsEffectSdkContext` calls on the UI thread and `NvsEffectRenderCore` calls on the GL thread.
20. Use placeholders for license/app ids/secret-like values unless the user provides real non-secret replacements.
21. Generate or stage once and apply once. Do not build both an isolated staging project and the final host project.
22. Hand Gradle execution to the user by default. Provide a filled copy-paste command block with the absolute project path, module, variant, failure handling, and APK lookup. Run it only after explicit automatic-execution consent.
23. Keep device/UI screenshot QA optional but recommended. If the user opts in, warn once about time/token cost, install the final APK once, run a concise deterministic smoke flow, and print PASS/FAIL assertions instead of full UI trees.

For incremental integration, use `--mode incremental --host-project <project> --app-module <module>` to create a staging directory with controllers and `patch-manifest.json`. Add `--apply` only when you want the generator to copy Java files and additive Manifest/Gradle changes into the host module. Reapplying identical output is idempotent. If any generated target differs from an existing host file, preflight stops before all source, Manifest, and Gradle mutation; `--force` does not authorize overwriting host-owned source.

For API-level integration without a product shell, use `--mode api-only`. The output contains selected controllers, dependency/resource metadata, and a concrete `ApiOnlyUsage` sample whose methods are emitted only for resolved modules. Integrate the sample at the host's lifecycle and navigation boundaries instead of copying a Demo Activity.

## Do Not Do

- Do not read external `SdkDemo` source as a knowledge dependency while using this skill. It is permitted to copy explicitly selected runtime/model/material files from a user-provided official package according to `official-sdk-download-resource-map.json`.
- Do not read from or reference the original `doxygen` folder while using this skill.
- Do not run `extract_demo_simple_code.py` during normal skill use; it is a build-time maintenance tool for updating bundled references.
- Do not copy demo signing config, release credentials, analytics keys, FTP tasks, or private package names.
- Do not initialize every human-detection model by default; initialize only models required by the requested feature.
- Do not bundle large `facemode`, AR, template, full music, or full font directories by default; expose official-package-relative source paths and copy only resources selected by the module closure.
- Do not add any material media, package, font, model, or material `.lic` file to the skill. Keep authorized material bundles external and copy them only into the generated project.
- Do not request broad storage permissions when scoped storage or MediaStore APIs are enough.
- Do not run Gradle, install an APK, drive a device, or capture/analyze screenshots during ordinary project creation/integration unless the user explicitly requests automatic execution.
- Do not print full UI XML, complete asset/controller inventories, broad search results, or repeated build warnings when a focused match, count, or saved diagnostic file is sufficient.

## Skill Maintenance And QA

The commands below are maintainer/CI checks, not part of ordinary skill use. They read only skill-bundled files unless a required external path is noted. Run them from the repository root; use `python -B` to avoid regenerating `scripts/__pycache__`.

- `python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\validate_lookup_cases.py` — validates 218 API and natural-language lookup cases. Expected output: `lookup validation passed` with 100% pass rates. No required arguments.
- `python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\knowledge_audit.py` — standalone knowledge and module audit. Expected output: `Structural gaps: 0`. Optional flags: `--strict`, `--sdk-jar`, `--android-jar`, `--require-java-compile`.
- `python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\validate_local_material_assets.py` — validates bundled material catalog asset paths and the no-network boundary. Expected output: `PASS`. No required arguments.
- `python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\validate_incremental_fixtures.py --sdk-root <extracted-sdk-root>` — validates incremental host fixtures. `--sdk-root` is required; optional flags: `--modules`, `--skip-build`, `--verify-idempotency`.
- `python -m unittest discover -s .\.codex\skills\meishe-android-streaming-sdk-api\scripts -p "test_*.py"` — runs the contract test suite covering the entrypoint size budget, referenced-file existence, generation modes, routing commands, high-risk policies, and CLI UTF-8 output.
