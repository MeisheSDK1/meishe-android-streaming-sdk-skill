# Demo Feature Priority Map

This reference ranks demo-derived feature modules by reuse value, SDK density, snippet coverage, and project criticality. Use it when a user asks for a broad app or when selecting which module patterns to load first.

Priority semantics:
- `P0`: project baseline or shared controller architecture.
- `P1`: common/high-value app workflows.
- `P2`: feature-family implementation modules.
- `P3`: optional workflow shell or low-frequency feature.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Summary](#summary)
- [Editor Product Priority Override](#editor-product-priority-override)
- [Category Priority Summary](#category-priority-summary)
- [Must-Use Feature Shortlist](#must-use-feature-shortlist)
- [Feature Module Priority Map](#feature-module-priority-map)
- [Selection Rules](#selection-rules)
<!-- END GENERATED CONTENTS -->

## Summary

| Priority | Features | Use first when |
| --- | ---: | --- |
| `P0` | 4 | Scaffolding a robust SDK project, managers/controllers, and common utilities. |
| `P1` | 6 | Building a broad editor/camera app with normal user workflows. |
| `P2` | 18 | Implementing a selected feature family such as captions, AR, filters, or templates. |
| `P3` | 34 | Handling exact niche demos or optional screens. |

## Editor Product Priority Override

The table below was generated from SDK density, reuse value, and source coverage. For a product-level short-video editor, also apply the device-validated workflow priority from `demo-validated-editor-architecture.md`:

- `selectmedia` is P0/P1 for editor products even though its direct SDK call count is low. It creates the media seed, ratio, resolution, and `TimelineData` inputs needed by `VideoEditActivity`.
- `edit` is the P1 editor shell. It is not merely a caption/sticker module; it owns the timeline, live preview, child-module routing, result application, and export entry.
- `edit-clipedit` is a P1 child module under the editor shell for trim/split/speed/volume/color/crop/photo controls.
- When generating a broad editor with captions, stickers, filters, beauty, or material center, load `demo-validated-editor-architecture.md` before selecting optional snippets.

## Category Priority Summary

| Category | P0 | P1 | P2 | P3 | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ar-makeup-segmentation` | 0 | 1 | 1 | 7 | 9 |
| `assets-packages` | 0 | 0 | 1 | 2 | 3 |
| `audio-media` | 0 | 0 | 5 | 4 | 9 |
| `captions-stickers` | 0 | 3 | 7 | 10 | 20 |
| `core-lifecycle` | 3 | 0 | 0 | 5 | 8 |
| `effects-transforms` | 0 | 0 | 2 | 4 | 6 |
| `preview-export` | 0 | 0 | 1 | 1 | 2 |
| `template-mimo-cutsame` | 0 | 2 | 1 | 1 | 4 |
| `timeline-editing` | 1 | 0 | 0 | 0 | 1 |

## Must-Use Feature Shortlist

| Feature | Priority | Score | Category | Why it matters | Required API families |
| --- | --- | ---: | --- | --- | --- |
| `engine-meishe` Engine Meishe | `P0` | 100 | `timeline-editing` | project baseline or controller architecture | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoResolution`, `NvsAudioResolution`, `NvsAssetPackageManager` |
| `utils` Utils | `P0` | 97 | `core-lifecycle` | project baseline or controller architecture | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoResolution`, `NvsAudioResolution`, `NvsRational`, `NvsAVFileInfo` |
| `app-root` App Root | `P0` | 90 | `core-lifecycle` | project baseline or controller architecture | `NvsStreamingContext`, `NvsEffectSdkContext` when AR/human-detection is enabled, license/assets/application lifecycle |
| `base-meishe` Base Meishe | `P0` | 90 | `core-lifecycle` | project baseline or controller architecture | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindowExt`, `NvsMultiThumbnailSequenceView`, `NvsAssetPackageManager` |
| `selectmedia` Media selection workflow | `P0/P1` | 88 | `timeline-editing` | editor cannot start from real user media without this or an equivalent import flow | `NvsStreamingContext`, `NvsAVFileInfo`, `NvsVideoResolution`, `TimelineData`-style clip/ratio state |
| `edit-clipedit` Edit Clipedit | `P1` | 88 | `timeline-editing` | common editor workflow fails or becomes incomplete | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, clip mutation APIs |
| `cutsame-template` CutSame/template module | `P1` | 80 | `template-mimo-cutsame` | high-value feature family degrades | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, template package descriptors |
| `mimodemo` Mimo demo workflow | `P1` | 80 | `template-mimo-cutsame` | high-value feature family degrades | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, template package descriptors |
| `edit-caption` Edit Caption | `P1` | 79 | `captions-stickers` | high-value feature family degrades | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` |
| `edit` Edit | `P1` | 76 | `timeline-editing` | common editor workflow fails or becomes incomplete | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` |
| `capture` Capture | `P1` | 72 | `ar-makeup-segmentation` | common app workflow fails or becomes incomplete | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models |

## Feature Module Priority Map

| Feature | Priority | Score | Category | Snippets | SDK lines | Coverage | Required API families | Missing impact |
| --- | --- | ---: | --- | ---: | ---: | --- | --- | --- |
| `engine-meishe` Engine Meishe | `P0` | 100 | `timeline-editing` | 293 | 868 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoResolution`, `NvsAudioResolution`, `NvsAssetPackageManager` | project baseline or controller architecture |
| `utils` Utils | `P0` | 97 | `core-lifecycle` | 61 | 439 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoResolution`, `NvsAudioResolution`, `NvsRational`, `NvsAVFileInfo` | project baseline or controller architecture |
| `app-root` App Root | `P0` | 90 | `core-lifecycle` | 4 | 47 | `method-snippets` | `NvsStreamingContext`, `NvsEffectSdkContext` when AR/human-detection is enabled, license/assets/application lifecycle | project baseline or controller architecture |
| `base-meishe` Base Meishe | `P0` | 90 | `core-lifecycle` | 26 | 107 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindowExt`, `NvsMultiThumbnailSequenceView`, `NvsAssetPackageManager` | project baseline or controller architecture |
| `edit-clipedit` Edit Clipedit | `P1` | 88 | `timeline-editing` | 170 | 388 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, clip mutation APIs | common editor workflow fails or becomes incomplete |
| `cutsame-template` CutSame/template module | `P1` | 80 | `template-mimo-cutsame` | 70 | 252 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, template package descriptors | high-value feature family degrades |
| `mimodemo` Mimo demo workflow | `P1` | 80 | `template-mimo-cutsame` | 73 | 266 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, template package descriptors | high-value feature family degrades |
| `edit-caption` Edit Caption | `P1` | 79 | `captions-stickers` | 57 | 271 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit` Edit | `P1` | 76 | `timeline-editing` | 62 | 146 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | common editor workflow fails or becomes incomplete |
| `capture` Capture | `P1` | 72 | `ar-makeup-segmentation` | 37 | 110 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | common app workflow fails or becomes incomplete |
| `ar-scene` AR scene beauty module | `P2` | 69 | `ar-makeup-segmentation` | 39 | 61 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, AR scene/beauty package descriptors | high-value feature family degrades |
| `makeup` Makeup module | `P2` | 69 | `ar-makeup-segmentation` | 40 | 54 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `douvideo` DouVideo capture/edit workflow | `P2` | 60 | `captions-stickers` | 53 | 141 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `themeshoot` Theme shoot workflow | `P2` | 58 | `captions-stickers` | 37 | 132 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-animatesticker` Edit Animatesticker | `P2` | 55 | `captions-stickers` | 34 | 87 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-filter` Edit Filter | `P2` | 55 | `assets-packages` | 29 | 100 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager` | feature-specific scope |
| `particle` Particle | `P2` | 55 | `effects-transforms` | 32 | 91 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `capturescene` Capture scene workflow | `P2` | 53 | `capture-recording` | 27 | 74 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `edit-mask` Edit Mask | `P2` | 52 | `captions-stickers` | 27 | 66 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `picinpic` Picture-in-picture editing | `P2` | 48 | `audio-media` | 17 | 49 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `boomrang` BoomRang capture/playback workflow | `P2` | 47 | `capture-recording` | 19 | 35 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `edit-compoundcaption` Edit Compoundcaption | `P2` | 47 | `captions-stickers` | 15 | 49 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-record` Edit Record | `P2` | 47 | `captions-stickers` | 21 | 34 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-music` Edit Music | `P2` | 46 | `audio-media` | 18 | 32 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `makecover` Make cover workflow | `P2` | 46 | `effects-transforms` | 14 | 44 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-anim` Edit Anim | `P2` | 45 | `effects-transforms` | 13 | 34 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `photoalbum` Photo album workflow | `P2` | 45 | `captions-stickers` | 11 | 43 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `sequencenesting` Sequencenesting | `P2` | 45 | `preview-export` | 9 | 20 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt` | feature-specific scope |
| `base` Base | `P3` | 44 | `effects-transforms` | 15 | 27 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-background` Edit Background | `P3` | 44 | `effects-transforms` | 10 | 37 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-theme` Edit Theme | `P3` | 43 | `captions-stickers` | 12 | 29 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-timelineeditor` Edit Timelineeditor | `P3` | 43 | `captions-stickers` | 9 | 39 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-audio` Edit Audio | `P3` | 41 | `audio-media` | 10 | 20 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `superzoom` SuperZoom AI workflow | `P3` | 41 | `ar-makeup-segmentation` | 8 | 28 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `utils-datainfo` Utils Datainfo | `P3` | 41 | `captions-stickers` | 10 | 21 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `activity` Activity | `P3` | 40 | `template-mimo-cutsame` | 6 | 31 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, template package descriptors | high-value feature family degrades |
| `edit-livephoto` Edit Livephoto | `P3` | 40 | `preview-export` | 5 | 15 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt` | feature-specific scope |
| `edit-makeup` Edit Makeup | `P3` | 40 | `ar-makeup-segmentation` | 9 | 19 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `presenter` Presenter | `P3` | 40 | `ar-makeup-segmentation` | 8 | 23 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `edit-createpic` Edit Createpic | `P3` | 38 | `captions-stickers` | 6 | 20 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `musiclyrics` Music lyrics workflow | `P3` | 38 | `captions-stickers` | 7 | 19 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `quicksplicing` Quick splicing / passthrough convert | `P3` | 38 | `captions-stickers` | 6 | 20 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `utils-asset` Utils Asset | `P3` | 38 | `ar-makeup-segmentation` | 4 | 32 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `view` View | `P3` | 38 | `ar-makeup-segmentation` | 5 | 27 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `edit-watermark` Edit Watermark | `P3` | 37 | `captions-stickers` | 9 | 11 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `capture-beauty` Capture Beauty | `P3` | 35 | `ar-makeup-segmentation` | 7 | 9 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `flipcaption` Flipcaption | `P3` | 35 | `captions-stickers` | 5 | 15 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-transition` Edit Transition | `P3` | 33 | `captions-stickers` | 4 | 11 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `libnet` Libnet | `P3` | 33 | `core-lifecycle` | 2 | 8 | `method-snippets` | `NvsStreamingContext` | project baseline or controller architecture |
| `glitter` Glitter | `P3` | 32 | `audio-media` | 2 | 18 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `capture-filter` Capture Filter | `P3` | 31 | `assets-packages` | 4 | 7 | `method-snippets` | `NvsStreamingContext`, `NvsAssetPackageManager` | feature-specific scope |
| `edit-data` Edit Data | `P3` | 29 | `effects-transforms` | 3 | 6 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `dialog` Dialog | `P3` | 27 | `captions-stickers` | 2 | 6 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `edit-view` Edit View | `P3` | 27 | `ar-makeup-segmentation` | 4 | 3 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAssetPackageManager`, `NvsEffectSdkContext`/human detection models | high-value feature family degrades |
| `feedback` Feedback | `P3` | 25 | `core-lifecycle` | 2 | 1 | `method-snippets` | `NvsStreamingContext` | project baseline or controller architecture |
| `repository` Repository | `P3` | 25 | `core-lifecycle` | 2 | 1 | `method-snippets` | `NvsStreamingContext` | project baseline or controller architecture |
| `selectmedia` Media selection workflow | `P0/P1` | 88 | `timeline-editing` | 1 | 7 | `method-snippets` | `NvsStreamingContext`, `NvsAVFileInfo`, `NvsVideoResolution`, `TimelineData`-style clip/ratio state | editor cannot start from real user media without this or an equivalent import flow |
| `urledit` Urledit | `P3` | 25 | `audio-media` | 2 | 4 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAudioTrack`/`NvsAudioClip` | feature-specific scope |
| `bean` Bean | `P3` | 24 | `effects-transforms` | 2 | 3 | `method-snippets` | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsLiveWindow`/`NvsLiveWindowExt`, `NvsAssetPackageManager` | high-value feature family degrades |
| `main` Main | `P3` | 10 | `core-lifecycle` | 0 | 0 | `manifest-only` | `NvsStreamingContext` | project baseline or controller architecture |
| `utils-permission` Utils Permission | `P3` | 10 | `core-lifecycle` | 0 | 0 | `manifest-only` | `NvsStreamingContext` | project baseline or controller architecture |
| `download` Download | `P3` | 5 | `assets-packages` | 0 | 0 | `manifest-only` | `NvsStreamingContext`, `NvsAssetPackageManager` | feature-specific scope |

## Selection Rules

- For a full editor, load `demo-validated-editor-architecture.md`, then P0 features, `selectmedia` or an equivalent media import flow, P1 `edit`, `edit-clipedit`, preview/export, and requested child modules such as `edit-caption`, `edit-filter`, `edit-animatesticker`, audio, beauty, or material center.
- For a camera-first app, load P0 features plus `capture`, `capturescene`, `boomrang`, and the requested AR/makeup/effect modules.
- For template/CutSame/Mimo, load P0 features plus `engine-meishe`, `cutsame-template`, and `mimodemo` before snippets.
- For captions/stickers, load `edit-caption`, `edit-animatesticker`, `edit-compoundcaption`, and relevant caption/sticker simple snippets.
- For asset-heavy features, always load `NvsAssetPackageManager` priority rows and constants before implementation.
- Do not load P3 modules unless the user explicitly asks for that workflow or an exact API search lands there.
