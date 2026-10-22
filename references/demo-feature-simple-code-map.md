# Demo Feature To Simple Code Map

Use this map to answer whether a Demo feature has reusable simple code coverage inside the skill. Source labels refer to the original Demo as evidence only; skill use does not require the original Demo folder.

Use `demo-feature-simple-code-map.json` for the authoritative mapping of all 62
features to exact semantic unit ids, parent modules, priorities, resources, and
`direct_unit`/`composed_recipe` status. The table below is a concise feature
router and retains legacy snippet references as provenance.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Coverage Semantics](#coverage-semantics)
- [High-Value Feature Map](#high-value-feature-map)
- [Bundled Product Bindings](#bundled-product-bindings)
- [Usage](#usage)
<!-- END GENERATED CONTENTS -->

## Coverage Semantics

- `mapped`: feature has a module id, recipe/snippet route, resource keys, and dependency path.
- `recipe-only`: feature is better represented as an ordered API recipe than as a transplantable code block.
- `workflow-only`: feature is mainly navigation, permission, or UI shell; SDK work is delegated to mapped children.
- `coverage-gap`: feature lacks enough demo-derived simple code to implement safely.

## High-Value Feature Map

| Demo feature | Module id | Coverage | Simple code refs | Required resources | Notes |
| --- | --- | --- | --- | --- | --- |
| `app-root` | `app-runtime` | mapped | `demo-simple-snippets-core-lifecycle.md`, `effects-transforms-001` | `R0` | SDK init, license, optional Effect SDK/model gates. |
| `base-meishe` | `app-runtime` | mapped | `core-lifecycle-*`, `preview-export-*` | `R0`, `R3` | Base lifecycle and preview helpers become controllers. |
| `utils` | `timeline-state-store` | mapped | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R3` | Timeline utility/state reconstruction evidence. |
| `selectmedia` | `media-import` | mapped | `audio-media-078`, `demo-validated-editor-architecture.md` | `R0`, `R1` | P0/P1 editor predecessor despite low SDK line count. |
| `edit` | `editor-shell` | mapped | `demo-validated-editor-architecture.md`, `preview-export-*`, `timeline-editing-*` | `R0`, `R1`, `R3` | Parent editor shell with `NvsLiveWindow` and child-result apply. |
| `edit-clipedit` | `clip-editor` | mapped | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-effects-transforms.md` | `R0`, `R1`, `R3` | Trim, split, crop, speed, volume, color, image duration/motion. |
| `edit-filter` | `filter-editor` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-assets-packages.md` | `R0`, `R3`, `R4`, `R5` | Built-in and packaged timeline/clip FX. |
| `edit-caption` | `caption-editor` | mapped | `demo-simple-snippets-captions-stickers.md`, `demo-simple-snippets-rare-structural.md` | `R0`, `R3`, `R4`, `R6` | Timeline captions, style packages, spans, text mutation. |
| `edit-animatesticker` | `sticker-editor` | mapped | `demo-simple-snippets-captions-stickers.md` | `R0`, `R3`, `R4`, `R6` | Animated/custom sticker placement and mutation. |
| `edit-compoundcaption` | `compound-caption-editor` | mapped | `demo-simple-snippets-captions-stickers.md` | `R0`, `R3`, `R4`, `R6` | Compound caption package workflow. |
| `edit-transition` | `transition-editor` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-assets-packages.md` | `R0`, `R1`, `R3`, `R4`, `R5` | Requires at least two clips. |
| `edit-music` | `music-editor` | mapped | `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R3`, `R7` | Music bed and audio timeline. |
| `edit-record` | `voiceover-editor` | mapped | `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R3`, `R7` | Requires `RECORD_AUDIO`. |
| `edit-mask` | `mask-editor` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-preview-export.md` | `R0`, `R1`, `R3`, `R5` | Needs live-window coordinate mapping. |
| `edit-background` | `background-editor` | mapped | `demo-simple-snippets-effects-transforms.md` | `R0`, `R1`, `R3`, `R5`, `R11` | Canvas/background replacement and color/blur modes. |
| `edit-watermark` | `watermark-editor` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-rare-structural.md` | `R0`, `R3`, `R4`, `R11` | Timeline/storyboard watermark flow. |
| `edit-anim` | `animation-editor` | mapped | `demo-simple-snippets-effects-transforms.md` | `R0`, `R1`, `R3`, `R5` | Clip animation/keyframe presets. |
| `edit-makeup` | `makeup-editor` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R1`, `R3`, `R4`, `R8` | Timeline makeup, model-gated when face features are used. |
| `capture` | `capture-camera` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R2`, `R4`, `R8` | Capture preview, effects, recording, beauty/AR hooks. |
| `capture-beauty` | `beauty-camera` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R2`, `R4`, `R8` | Camera beauty child module. |
| `capture-filter` | `capture-filter` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-assets-packages.md` | `R0`, `R2`, `R4`, `R5` | Capture FX/filter packages. |
| `capturescene` | `capture-scene` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-assets-packages.md` | `R0`, `R2`, `R4`, `R5`, `R8` | Capture scene package install/apply. |
| `ar-scene` | `ar-scene` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R2`, `R4`, `R8` | AR scene package/model gates. |
| `makeup` | `makeup-service` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R4`, `R8` | Shared makeup data/install/apply rules. |
| `superzoom` | `superzoom-ai` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md`, `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R8`, `R9` | AI face workflow; select required models from the official Android LTS face package. |
| `picinpic` | `pip-editor` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R3`, `R4`, `R11` | Requires two media items. |
| `cutsame-template` | `cutsame-template` | mapped | `demo-simple-snippets-template-mimo-cutsame.md` | `R0`, `R1`, `R4`, `R10` | CutSame package, footage validation, compile. |
| `mimodemo` | `mimo-template` | mapped | `demo-simple-snippets-template-mimo-cutsame.md` | `R0`, `R1`, `R4`, `R10` | Mimo timeline/material mapping. |
| `engine-meishe` | `template-engine` | mapped | `demo-simple-snippets-template-mimo-cutsame.md`, `demo-simple-snippets-timeline-editing.md` | `R0`, `R1`, `R3`, `R4`, `R10` | Template engine and generic timeline model evidence. |
| `quicksplicing` | `quick-splicing` | mapped | `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R12` | Passthrough convertor; no full editor required. |
| `urledit` | `url-media-import` | mapped | `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R12` | Remote/media URL inspection/import. |
| `musiclyrics` | `music-lyrics` | mapped | `demo-simple-snippets-audio-media.md`, `demo-simple-snippets-captions-stickers.md` | `R0`, `R1`, `R3`, `R6`, `R7` | Audio + lyric/caption timing. |
| `photoalbum` | `photo-album` | mapped | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-preview-export.md` | `R0`, `R1`, `R3`, `R11` | Image timeline and album preview/export. |
| `themeshoot` | `theme-shoot` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-template-mimo-cutsame.md` | `R0`, `R1`, `R2`, `R4`, `R10` | Capture plus template/theme preview. |
| `douvideo` | `dou-video-workflow` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-captions-stickers.md` | `R0`, `R1`, `R2`, `R3`, `R4`, `R6`, `R7` | Capture/edit bridge. |
| `boomrang` | `boomrang-capture` | mapped | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-preview-export.md` | `R0`, `R1`, `R2`, `R3` | Camera-first capture/playback flow. |
| `particle` | `particle-effects` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-capture-recording.md` | `R0`, `R1`, `R2`, `R3`, `R4`, `R5` | Particle package parser/effects. |
| `glitter` | `glitter-effects` | mapped | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-capture-recording.md` | `R0`, `R2`, `R4`, `R5` | Capture/timeline glitter effect flow. |
| `flipcaption` | `flip-caption` | mapped | `demo-simple-snippets-captions-stickers.md`, `demo-simple-snippets-effects-transforms.md` | `R0`, `R1`, `R3`, `R6` | Caption/timeline FX workflow. |
| `makecover` | `cover-maker` | mapped | `demo-simple-snippets-preview-export.md`, `demo-simple-snippets-effects-transforms.md` | `R0`, `R1`, `R3`, `R11` | Cover/frame selection and output. |
| `sequencenesting` | `sequence-nesting` | mapped | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-preview-export.md` | `R0`, `R1`, `R3` | Nested timeline/sequence editing. |
| `edit-livephoto` | `livephoto-editor` | mapped | `demo-simple-snippets-preview-export.md`, `demo-simple-snippets-timeline-editing.md` | `R0`, `R1`, `R3` | Live photo edit flow. |
| `edit-audio` | `audio-equalizer` | mapped | `demo-simple-snippets-audio-media.md` | `R0`, `R1`, `R3`, `R7` | Audio FX/equalizer. |
| `edit-timelineeditor` | `timeline-ui` | mapped | `demo-simple-snippets-preview-export.md`, `demo-simple-snippets-timeline-editing.md` | `R0`, `R1`, `R3` | Thumbnail/time-span UI helpers. |
| `edit-theme` | `theme-editor` | mapped | `demo-simple-snippets-template-mimo-cutsame.md`, `demo-simple-snippets-captions-stickers.md` | `R0`, `R1`, `R3`, `R4`, `R10` | Theme application and captions. |
| `edit-createpic` | `still-image-export` | mapped | `demo-simple-snippets-preview-export.md` | `R0`, `R1`, `R3` | Create picture/thumbnail output. |
| `activity` | `feature-hub` | workflow-only | `demo-validated-editor-architecture.md` | `R0` | Main activity routing, setting, CutSame/beauty entry. |
| `download` | `asset-center-service` | policy-replaced-local | `asset-center-workflow.md` | `R0`, `R4` | Stable legacy feature id now routes to bundled local browse/install only. |
| `main` | `feature-hub` | workflow-only | `capability-catalog.md` | `R0` | Web/help entry; not SDK-critical. |
| `utils-permission` | `permission-gates` | workflow-only | `demo-simple-snippets-core-lifecycle.md` | feature-dependent | Permission Activity wrapper. |
| `feedback` | `support-feedback` | mapped | `demo-simple-snippets-core-lifecycle.md` | `R0` | Low-priority SDK-adjacent feedback flow. |
| `repository` | `app-repository` | mapped | `demo-simple-snippets-core-lifecycle.md` | `R0` | Shared app state/repository pattern. |
| `libnet` | `asset-center-service` | mapped | `asset-center-workflow.md` | `R13` | Network pattern rewritten with configurable base URL. |
| `base` | `asset-center-service` | mapped | `asset-center-workflow.md`, `demo-simple-snippets-effects-transforms.md` | `R0`, `R13` | HTTP/material center manager and base Activity evidence. |
| `bean` | `effect-parameter-models` | mapped | `demo-simple-snippets-effects-transforms.md` | `R0`, `R5` | Data models for FX strength/color. |
| `edit-data` | `effect-parameter-models` | mapped | `demo-simple-snippets-effects-transforms.md` | `R0`, `R5` | Filter/mask data models. |
| `utils-datainfo` | `timeline-state-store` | mapped | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-rare-structural.md` | `R0`, `R1`, `R3` | `ClipInfo`, `TimelineData`, captions, transitions, FX state. |
| `dialog` | `editor-ui-shell` | workflow-only | `demo-simple-snippets-captions-stickers.md` | feature-dependent | Caption edit popup and UI shell. |
| `edit-view` | `makeup-editor` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R4`, `R8` | Makeup UI view; logic binds to makeup service. |
| `presenter` | `beauty-camera` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md` | `R0`, `R2`, `R4`, `R8` | Main/beauty presenter logic. |
| `utils-asset` | `asset-package-service` | mapped | `demo-simple-snippets-assets-packages.md` | `R0`, `R4` | `NvAsset` and `NvAssetManager` asset constants/install flow. |
| `view` | `editor-ui-shell` | mapped | `demo-simple-snippets-ar-makeup-segmentation.md`, `demo-simple-snippets-preview-export.md` | feature-dependent | Shared timeline/effect/capture views. |

## Bundled Product Bindings

The following skill-owned product shells compose the mapped Demo evidence without becoming new Demo provenance:

| App template | Mapped feature modules | Concrete binding |
| --- | --- | --- |
| `short-video-editor` | `feature-hub`, `media-import`, `editor-shell`, `clip-editor`, `filter-editor`, `caption-editor`, `sticker-editor`, `transition-editor`, `music-editor`, `voiceover-editor`, `asset-center-service`, `export-compile` | `ACTION_OPEN_DOCUMENT` -> app-private media -> ratio -> timeline -> `NvsLiveWindow` -> edit mutations -> material results -> compile. |
| `beauty-camera` | `capture-camera`, `beauty-camera`, `capture-filter`, `asset-center-service` | Permission gate -> capture preview -> beauty parameters/filter -> bundled or user-provided local capture package -> recording. |
| `asset-center-demo` | `asset-package-service`, `asset-center-service` | Bundled catalog -> local selection -> install/register -> typed result. Its standalone host applies an installed filter to a real sample Timeline/LiveWindow and exposes intensity/removal; picker mode delegates other material kinds to their owning feature. |

## Usage

When implementing a feature:

1. Find the Demo feature row here.
2. Use `Module id` to load `sdk-module-registry.json`.
3. Resolve dependencies with `compose_modules.py`.
4. Load the listed simple snippet groups and exact snippets only as needed.
5. Ask for resources from `Required resources`; do not copy full Demo assets.
