# Low-Frequency P3 API Processing

This file is generated from `p3-api-processing.json`. The frozen scope contains 495 Demo-observed P3 members with fewer than 10 occurrences.

## Result

| Metric | Count |
| --- | ---: |
| Processed | 495 |
| Upgraded to exact compiled units | 149 |
| Retained as evidence with explicit reasons | 346 |
| Unclassified | 0 |
| Missing module mapping | 0 |
| Generic retention reasons | 0 |

An upgraded member must reference a real `java_unit`. A retained member keeps its exact jar signature, Demo evidence, member-level domains, modules, related recipes, constraints, and a specific reason. Constants, callbacks, diagnostic getters, value objects, OpenGL operations, and caller-owned lifecycle operations are not promoted with empty wrapper code.

## Domain Mapping

| Domain | Frozen members |
| --- | ---: |
| `ar-beauty-segmentation` | 40 |
| `asset-packages` | 44 |
| `audio-editing` | 15 |
| `caption-editing` | 129 |
| `capture-recording` | 23 |
| `core-runtime` | 16 |
| `effect-parameters` | 77 |
| `export-compile` | 11 |
| `media-conversion` | 6 |
| `media-inspection` | 42 |
| `particle-effects` | 7 |
| `preview-playback` | 20 |
| `render-core` | 10 |
| `sticker-editing` | 31 |
| `template-workflows` | 14 |
| `timeline-editing` | 83 |
| `timeline-ui` | 13 |
| `transition-editing` | 15 |

## Retention Reasons

| Reason code | Retained members |
| --- | ---: |
| `ar-beauty-segmentation.owned_lifecycle_operation` | 1 |
| `ar-beauty-segmentation.typed_constant` | 23 |
| `asset-packages.read_only_query` | 2 |
| `asset-packages.typed_constant` | 31 |
| `audio-editing.read_only_query` | 5 |
| `caption-editing.read_only_query` | 16 |
| `caption-editing.stateful_operation_requires_context` | 25 |
| `caption-editing.typed_constant` | 15 |
| `caption-editing.value_object_contract` | 35 |
| `capture-recording.read_only_query` | 3 |
| `capture-recording.stateful_operation_requires_context` | 2 |
| `capture-recording.typed_constant` | 4 |
| `core-runtime.callback_contract` | 2 |
| `core-runtime.owned_lifecycle_operation` | 2 |
| `core-runtime.read_only_query` | 4 |
| `core-runtime.stateful_operation_requires_context` | 4 |
| `core-runtime.typed_constant` | 3 |
| `effect-parameters.read_only_query` | 20 |
| `effect-parameters.stateful_operation_requires_context` | 15 |
| `effect-parameters.typed_constant` | 15 |
| `effect-parameters.value_object_contract` | 5 |
| `export-compile.stateful_operation_requires_context` | 1 |
| `export-compile.typed_constant` | 8 |
| `media-conversion.callback_contract` | 2 |
| `media-conversion.typed_constant` | 2 |
| `media-inspection.callback_contract` | 1 |
| `media-inspection.owned_lifecycle_operation` | 2 |
| `media-inspection.read_only_query` | 15 |
| `media-inspection.stateful_operation_requires_context` | 2 |
| `media-inspection.typed_constant` | 15 |
| `preview-playback.callback_contract` | 1 |
| `preview-playback.stateful_operation_requires_context` | 4 |
| `preview-playback.typed_constant` | 7 |
| `render-core.opengl_operation` | 7 |
| `render-core.typed_constant` | 2 |
| `sticker-editing.read_only_query` | 3 |
| `sticker-editing.stateful_operation_requires_context` | 7 |
| `template-workflows.read_only_query` | 1 |
| `template-workflows.stateful_operation_requires_context` | 3 |
| `template-workflows.typed_constant` | 3 |
| `timeline-editing.read_only_query` | 9 |
| `timeline-editing.stateful_operation_requires_context` | 1 |
| `timeline-editing.typed_constant` | 10 |
| `timeline-ui.typed_constant` | 1 |
| `transition-editing.read_only_query` | 3 |
| `transition-editing.typed_constant` | 4 |

Use `p3-api-processing-scope.json` for the immutable member list and `p3-api-processing.json` for per-member status. These files are skill-owned runtime knowledge and do not require the external Demo or Doxygen tree.
