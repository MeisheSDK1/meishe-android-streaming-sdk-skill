# Demo Feature/API/Simple Coverage Assessment

This is the current implementation-readiness assessment for the standalone skill. It uses API v2 signatures, semantic Simple Code, module contracts, build evidence, and exact physical-device records. Historical Demo token and statement counts are evidence-discovery metrics only; they are not implementation coverage.

## Current Coverage Snapshot

<!-- BEGIN GENERATED CURRENT COVERAGE -->
| Surface | Metric | Current result | Coverage meaning |
| --- | --- | ---: | --- |
| API v2 | SDK types | 283 | Exact owners from the bundled SDK signature map. |
| API v2 | Exact members | 751 | Fields, constructors, methods, and overload descriptors. |
| API v2 | Demo-observed methods | 515 | Methods associated with retained Demo evidence. |
| API implementation | `compiled_unit` | 405 | Exact member has a compilable skill-owned unit. |
| API implementation | `contract_only` | 0 | Exact contract exists, but no exact compilable unit exists yet. |
| API implementation | `evidence_only` | 346 | Demo evidence exists; it is not counted as generated implementation. |
| Low-frequency P3 processing | Upgraded / retained | 149 / 346 | Frozen 495-member scope; retained members have member-level domains, modules, recipes, constraints, and explicit reasons. |
| Simple Code v2 | Semantic units | 322 | 241 `java_unit` and 81 `recipe` entries. |
| Composition | Demo features | 62 | Features have dedicated recipes and module mappings. |
| Composition | Modules / blueprints | 57 / 9 | Dependency-closed modules and application shells. |
| Runtime evidence | Device runs | 22 | 19 passed and 3 partial runs. |
| Runtime evidence | Blueprints with evidence | 8 | 8 have a passed run; 0 have partial-only evidence. |
| Runtime evidence | Modules / features / units / APIs | 57 / 60 / 112 / 111 | Applies only to exact recorded flows and resources. |
| Build evidence | Runs / blueprints | 41 / 9 | Build evidence never implies physical-device behavior. |
<!-- END GENERATED CURRENT COVERAGE -->

The generated block above is derived from `coverage-summary.json`. Run `scripts/coverage_summary.py --check` to reject stale documentation or `scripts/coverage_summary.py --write` after an intentional knowledge rebuild.

## Coverage States

| State | Meaning | Allowed claim |
| --- | --- | --- |
| `evidence_only` | Demo usage evidence exists without an independent implementation unit. | The Demo used this API; inspect evidence before implementation. |
| `contract_only` | Exact signature and constraints exist without an exact compilable unit. | The API can be planned, but implementation is still required. |
| `compiled_unit` | A skill-owned Java unit compiles against the SDK and Android jars. | The exact API has reusable code, subject to runtime resources and device behavior. |
| `generated_module` | The unit is rendered and connected by a generated module or blueprint. | The selected generated path contains the implementation. |
| `runtime_verified` | A recorded device flow exercised the exact unit/API/module configuration. | Only the scope and limitations in the runtime matrix may be claimed. |

## Judgment

| Question | Current answer | Boundary |
| --- | --- | --- |
| Can the skill cover all Demo-observed API usage? | Every normalized API has a v2 record and explicit coverage state. | `contract_only` and `evidence_only` are known gaps, not generated implementations. |
| Can it directly implement any API? | P0/P1 APIs have compiled units; many P2/P3 APIs are also compiled. | Exact overload coverage must be checked in `demo-api-simple-code-map.json`; related class or overload mappings do not count. |
| Can it implement every Demo feature? | All 62 features have dedicated recipes and module mappings. | Some modules are recipe/template-driven and still require productization, resources, or runtime validation. |
| Can it compose new feature blocks? | Yes when dependency closure resolves real units, lifecycle hooks, resources, and guards. | Evidence-only APIs cannot be promoted by composition, and Demo Activity structure is not mandatory. |
| Can it generate robust complete projects? | Nine blueprints and three integration modes provide reusable application or patch shells. | Product depth varies; proprietary SDK artifacts, models, packages, host behavior, and runtime QA remain explicit gates. |
| Can it claim full SDK runtime verification? | No. Runtime evidence is exact and resource-specific. | A `partial` run proves only its listed flows; it never means the complete blueprint passed. |

## Required Lookup Flow

1. Use `capability-catalog.md` for product-level discovery.
2. Search `skill-lookup-index.json` to resolve feature, API, module, blueprint, resource, and Simple Code IDs.
3. Read `demo-api-simple-code-map.json` for the exact API descriptor and coverage state.
4. Resolve module dependency closure with `compose_modules.py`.
5. Read the selected semantic units from `simple-code-registry.json`.
6. Use official references for semantics and Demo evidence references for version-proven call order.
7. Read resource requirements before generating a resource-gated feature.
8. Read build and runtime matrices before making build or device claims.
9. Use historical exhaustive snippets only when the exact API remains `evidence_only` or additional Demo context is required.

## Independence Boundary

- Current coverage is computed entirely from files bundled in this skill.
- Normal lookup, composition, generation, summary, and audit commands do not read the original `SdkDemo` or Doxygen directories.
- Demo and Doxygen remain optional build-time maintenance sources only.
- Capabilities absent from both sources remain out of scope instead of being inferred.
