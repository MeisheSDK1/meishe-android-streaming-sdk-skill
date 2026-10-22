# Runtime Verification

Use this reference to distinguish generated or compiled capability from behavior that has actually run on a physical Android device.

The machine-readable source is `runtime-verification-matrix.json`. A capability is `runtime_verified` only for the exact flow, module, unit, API signature, device class, SDK version, and resource configuration recorded there.

## Verified Baseline

- SDK: Android Streaming SDK `3.16.1.25`
- Device: Samsung `SM-A5460`
- Android API: `35`
- ABI: `arm64-v8a`
- Latest recorded run date: `2026-08-05`

## Short Video Editor

Verified on generated `new-app` projects:

- SDK initialization and five bundled package installations.
- Bundled media to Timeline creation and `NvsLiveWindow` binding.
- Bundled APK media copied into persistent app-owned storage before Timeline probing; direct `assets:/` media fallback is no longer assumed.
- Seek-driven preview refresh and structural clip split.
- Packaged clip filter, built-in readable caption, animated sticker, packaged transition, and bundled music.
- Material package installation and compile/export completion.
- Android `ACTION_OPEN_DOCUMENT` import into persistent app-owned project media storage.
- Two-item mixed MP4/PNG selection, ordered app-owned import, and mixed-media Timeline construction.
- SDK media probing, portrait Timeline creation, and `NvsLiveWindow` rendering from a user-selected MP4.
- Clip move, source-coordinate trim at the Timeline playhead, and post-mutation undo/redo snapshots.
- Structural project-state persistence for ratio, ordered clip paths, source trim ranges, speed, media type, and image-motion state.
- Force-stop/relaunch recovery through `Resume Latest Project`, with the restored two-clip Timeline rendered at both ends in `NvsLiveWindow`.
- Historical version-2 editor descriptors for packaged filters, readable captions, animated stickers, packaged transitions, bundled music, and voiceover, followed by successful migration to the version-3 project schema.
- Force-stop/relaunch recovery of two clips and six editor items, including a visibly restored caption/filter frame in `NvsLiveWindow`.
- Full-state undo/redo after restore: persisted filter descriptors changed from two to one and back to two with matching Timeline rebuilds.
- Microphone voiceover recording, dedicated audio-track insertion, and export with H.264 video plus AAC audio.
- Full-state export to a 4.017-second H.264/AAC MP4 after restored filter/caption/sticker/transition/music/voiceover state.
- Mixed-media export to a 10.9-second H.264/AAC MP4 whose duration matched the persisted trim ranges, with an empty crash buffer.
- Version-3 atomic persistence under `filesDir/meishe-projects/<projectId>/project.json`, including canvas/FPS, audio resolution, stable clip ids, stable filter/transition relations, and a namespaced extension codec.
- Mixed JPEG/H.264 project restoration, stable-id split/move/delete behavior, a 50-snapshot in-memory history cap, and cold force-stop/relaunch restoration from the latest project file.
- `HOST_OWNED` safe defaults: structural mutation, descriptor rebuild, undo, and redo were denied; closing the editor preserved two host clips and a host-created caption without removing the supplied Timeline.
- System status/navigation bar inset handling.

The default caption intentionally uses a skill-owned horizontal white-text/black-outline style. A downloaded caption-style package is applied only after the user selects it, so a narrow or vertical package does not silently replace the basic caption behavior.

## Beauty Camera

Verified on generated `new-app` projects:

- Ordered camera and microphone permission handling without callback recursion.
- SDK initialization before dynamic `NvsLiveWindow` construction.
- Live preview, camera switching, smooth/whitening controls, bundled capture filter, and recording.
- Material-center list, download, install, result return, and live capture effect application.
- Official-face-package `facemode` copy hook and initialization of face/common optional models.
- Built-in AR Scene creation with model-backed beauty strength and whitening parameters.
- Background-segmentation capture effect with menu, stretch, and background-color parameters.
- Green segmentation output in the physical-device preview and recording while AR/segmentation effects remained active.
- MP4 output creation with an empty crash buffer.

Large human-detection models were supplied from the Demo only for this build-time validation. They remain external user resources and are not bundled in the skill. No face subject was present, so face beautification, AI face-occlusion quality, and segmentation edge quality were not visually scored.

## Composition And Material Flows

Verified on generated `new-app` projects:

- `asset-center-demo`: the former request-based run is retired. The current bundled-local-material implementation is build-validated but still needs a new physical-device run before it can be called runtime verified.
- `pip-editor`: created two video tracks, applied `Transform 2D` scale/translation, rendered both bundled images, played, and exported an MP4.
- `quick-splicing-app`: appended three clips, applied transitions, connected LiveWindow, played, and exported an MP4.
- `camera-plus-editor`: routed independently to a runnable editor and camera; both export and capture recording produced MP4 files.

The PIP and quick-splice defaults use two contrasting, lightweight bundled images. User-selected media remains available through Android DocumentsUI and app-owned cache copies.

## Product Shell Boundaries

- `template-mimo-cutsame-app` now has a later passed execution run in addition to its historical partial shell run. The generated app asynchronously installed one standard `.template`, mapped 14 footage slots from one selected media item, generated required reverse media, and previewed both standard and CutSame Timelines. Its independent Mimo branch safely extracted a ZIP, parsed `info.json`, installed 12 child packages, built five clips with six effects and five captions plus music, previewed the result, and exported a 1,012,870-byte MP4.
- `full-sdk-demo` now has a later passed Stage 7 module run in addition to its historical partial hub run. The later probe completed all 31 previously unverified module contracts with `STAGE7_COMPLETE passed=31 partial=0 total=31`. Combined with earlier exact runs, all 57 registered modules have physical-device evidence for at least one recorded flow.
- `incremental-integration` now has passed physical-device runs for both `incremental` and `api-only`. Java/Groovy, Java/KTS, Kotlin/Groovy, and Kotlin/KTS hosts all applied/generated, built, installed, navigated from the host Activity, reused the SDK singleton, bound and sought a Timeline in `NvsLiveWindow`, added a caption, installed and queried a standard template, started physical-camera preview, received compile callbacks, produced MP4 output, and completed lifecycle cleanup. The Java/Groovy run additionally exercised real CAMERA and RECORD_AUDIO permission dialogs and callback delivery.
- The incremental ownership run supplied a `HOST_OWNED` Timeline and confirmed that closing the editor preserved the host clip/caption and did not remove the Timeline. Repeated identical apply was idempotent; a deliberately conflicting host source stopped before source, Manifest, or Gradle mutation, even with `--force`.

Physical-device evidence covers 8 of 9 registered blueprints. The missing blueprint is `asset-center-demo`; its current bundled-local-material implementation is build-validated but still needs a physical-device run. Runs marked `partial` confer verification only to the exact modules, units, APIs, and flows recorded in the machine-readable matrix.

Runtime evidence covers 60 of 62 registered Demo features. The missing features are `edit-view` and `presenter`.

The Stage 7 packages, template ZIPs, models, theme/makeup/capture resources, and HTTP fixture were temporary validation inputs under `.stage7-runtime-validation`. Stage 8 reused one temporary MP4 and one standard template only under `.stage8-integration-validation`. None of these validation resources are bundled in the skill or required by lookup, composition, or generation.

## Build And Isolation Verification

Build-only evidence is recorded separately in `build-verification-matrix.json` and must not be treated as physical-device verification.

- All nine app blueprints were regenerated and completed `:app:assembleDebug`.
- The same nine blueprints were copied, generated, and built in a temporary directory without original `SdkDemo` or Doxygen siblings.
- The isolated SDK fixture contained only `NvAndroidStreamingSdk.jar`, `libNvStreamingSdkCore.so`, `effectlib.jar`, and `meishesdk.lic`.
- Incremental and API-only integration generated, applied, and built against Java/Kotlin hosts using Groovy/Kotlin DSL Gradle files. Identical repeated apply and atomic conflict preflight were also validated.
- Strict knowledge compilation covers all 241 `java_unit` entries with zero structural gaps.
- The 218-case retrieval suite reports 74/74 exact API, 39/39 exact stable API, and 105/105 natural-language Top-1 results (100% in every category).

## Not Implied

This evidence does not mark every SDK member, package variant, visual-quality condition, or device class as runtime verified. Exact flows now cover all 57 registered modules, one standard template, one CutSame branch, one Mimo package, and selected advanced AR/makeup/segmentation resources. It does not claim arbitrary third-party package quality, face-subject AR quality, hand/avatar/sky segmentation quality, production material services, 32-bit behavior, tablets/foldables, or Android versions other than API 35. Host-owned preservation is verified only for the default no-mutation policy; explicit host opt-in mutation, arbitrary host serializers, keyframes, and complete effect-parameter restoration remain outside the verified set.
