# Historical Evidence-Layer Coverage Audit

This historical audit records the original Demo token, statement, and touchpoint extraction pass. Its counts measure whether Demo evidence was retained; they do not measure current API v2 contracts, compilable units, generated modules, or physical-device coverage. Use `coverage-summary.json` and `demo-feature-api-simple-coverage.md` for current readiness.

## Verdict

The baseline method-level simple snippets were broad but not full. They intentionally compressed methods that contained reusable SDK statements, so they missed or underrepresented field-only, import-only, nested-type, callback, caption-span, watermark constant, and rare Effect SDK usages.

After this expansion, the skill has two layers:
- Method-level snippets for reusable call sequences.
- Exhaustive statement/touchpoint references for full demo API coverage and rare structural usages.

## Historical Evidence Metrics

| Metric | Value |
| --- | ---: |
| Java files scanned | 1226 |
| SDK-bearing Java/source files | 264 |
| SDK-related non-import code lines | 4557 |
| Unique `Nvs*`/SDK-adjacent tokens in demo | 99 |
| Unique `Nvs*` tokens in baseline simple snippets | 88 |
| Missing `Nvs*`/SDK-adjacent tokens before expansion | 11 |
| Unique `Nvs*` tokens after expansion | 99 |
| Missing `Nvs*`/SDK-adjacent tokens after expansion | 0 |
| Unique direct `NvsClass.member` tokens in demo | 377 |
| Direct `NvsClass.member` tokens after exhaustive/touchpoint expansion | 377/377 |

## Missing Before Expansion

- `NvsARSceneManipulateCallback`
- `NvsCaptureAudioFx`
- `NvsFaceBoundingRectInfo`
- `NvsItalicSpan`
- `NvsObject`
- `NvsPanAndScan`
- `NvsRendererIdSpan`
- `NvsTimelineWatermarkPosition_TopRight`
- `NvsTrackCaption`
- `NvsUnderlineSpan`
- `NvsVideoEffectAnimatedSticker`

## Missing After Expansion

- None for `Nvs*` tokens present in Java imports or non-import SDK-adjacent code lines.

## How To Use The Expanded Layer

Treat every value in this document as evidence-discovery coverage. Never promote it to `compiled_unit`, `generated_module`, or `runtime_verified`.

- Use `demo-simple-snippets-index.md` and the category snippet files for normal implementation work.
- Use `capability-catalog.md` for first-time users, capability discovery, SDK-vs-skill explanation, and vague product-goal routing.
- Use `demo-feature-list.md` to map a requested feature/workflow to implementation entries and simple coverage.
- Use `demo-api-list.md` to map a requested API/class/member to demo evidence and capability coverage.
- Use `demo-feature-priority-map.md` and `demo-api-priority-map.md` to decide P0/P1 foundations, feature/API weights, and missing-impact priority before loading large snippet files.
- Use `demo-api-dependency-graph.md` and `demo-feature-dependency-graph.md` to turn coverage into composable call chains, required/recommended/optional module dependencies, conflict handling, and teardown rules.
- Use `demo-api-constraint-map.md`, `demo-sdk-constants-map.md`, and `demo-api-call-order-map.md` to turn presence coverage into safe API usage rules, constants, parameter/return handling, and feature-flow order.
- Use `demo-feature-api-simple-coverage.md` for the direct answer to whether simple+skill coverage is enough for arbitrary API use, feature implementation, composition, or complete project generation.
- Use `demo-simple-snippets-rare-structural.md` when a class is low-frequency or missing from curated method snippets.
- Use `demo-simple-snippets-exhaustive-statements.md` to check every unique SDK-related Java statement pattern from the demo.
- Use `demo-api-touchpoints.md` to audit class/import/member coverage and locate source labels.
