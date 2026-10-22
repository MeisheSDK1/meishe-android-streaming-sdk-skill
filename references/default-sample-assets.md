# External Sample Assets

Use this reference when generating a first-run Android app or explaining the optional offline demo experience backed by authorized external materials.

## Rule

The skill stores no sample media, material packages, fonts, models, or material license files. Before generation, tell the user that material resources must be obtained from Meishe business. `scripts/create_android_project.py` can copy an authorized external bundle into the generated project.

The `short-video-editor`, `beauty-camera`, `asset-center-demo`, `pip-editor`, `quick-splicing-app`, `camera-plus-editor`, and `full-sdk-demo` product shells can use these packages or lightweight media during their baseline flows. When the external bundle is copied, generated projects retain an offline first-run path without a material-service endpoint or request layer.

Do not treat these sample assets as a replacement for production assets. For additional Demo examples or full models, resolve selected files from the official Android LTS face package. Commercial package and license authorization remains the user's responsibility.

## Generator Behavior

In this repository, default generation first looks for `temp_assets/android-sample-assets` and copies it when present:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --package com.example.meisheapp --app-name MeisheApp
```

For an installed or relocated skill, pass the authorized bundle explicitly:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --sample-assets-dir <authorized-bundle-root>
```

The bundle root must contain `app/src/main/assets`. If no bundle is found, the generator prints a pre-generation notice directing the user to Meishe business and continues without sample assets. Skip discovery explicitly when the user wants a clean shell:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --no-sample-assets
```

## Expected External Bundle

All paths below are copied into `app/src/main/assets`.

| Key | Asset path | Package type / use |
| --- | --- | --- |
| `filter` | `filter/394EB525-1B7A-4AA1-BBAD-3FD75527A60C/...5.videofx` plus `.lic`, `.json`, preview | `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX` |
| `transition` | `transition/C94516F7-0380-430E-AADC-83D9ED386790/...11.videotransition` plus `.lic`, `.json`, preview | `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION` |
| `captionStyle` | `captionstyle/91FC65DD-AE99-4079-B6A4-BDE60A3F6DF9/...2.captionstyle` plus `.lic`, `.json`, preview | `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE` |
| `animatedSticker` | `customsticker/E14FEE65-71A0-4717-9D66-3397B6C11223/...5.animatedsticker` plus `.lic`, `.json`, preview | `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER` |
| `captureScene` | `capturescene/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1/...capturescene` plus `.lic`, `.json` | `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`; the observed package has an empty material name and a 927-byte package file, so use it only to smoke-test installation and `applyCaptureScene(...)`, not as proof of a visible effect |
| `compoundCaption` | `compoundcaption/13E33AA6-85DC-4D7E-B5B0-23A9F0317909/` | `ASSET_PACKAGE_TYPE_COMPOUND_CAPTION` |
| `captionContext` | `captionbubble/33C8A32B-CC07-4B62-95BA-14A8365B75F1/` | `ASSET_PACKAGE_TYPE_CAPTION_CONTEXT` |
| `captionRenderer` | `captionrichword/72D49EAD-B9E4-4ADC-A188-545046835F65/` | `ASSET_PACKAGE_TYPE_CAPTION_RENDERER` |
| `captionAnimation` | `captionanimation/combination/0DC345B0-A396-4818-A27D-F1BC3D89DEF3/` | `ASSET_PACKAGE_TYPE_CAPTION_ANIMATION` |
| `stickerInAnimation` | `stickeranimation/in/ECF06228-5D1F-4728-80FB-0B1943A60C23/` | `ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION` |
| `clipAnimation` | `animation/in/37154A36-8816-492B-B1F5-F8122660C686/` | packaged video FX |
| `particle` | `particle/touch/34B095C8-628A-4E9D-B36D-093F9774DAF7/` | packaged video FX |
| `pipEffect` | `picinpic/pip_sreenleftup/64EC065F-17AE-4881-99EB-854C265FE950/` | packaged video FX |
| `arScene` | `arface/EDF352FC-701B-4C05-86CE-B0E293469341/` | `ASSET_PACKAGE_TYPE_ARSCENE`; visible application requires the AR module, matching human-detection models/data, `STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`, a detectable face, and the action reported by `getARSceneAssetPackagePrompt(...)` (`请张嘴试一试~` for this package). Empty SDK/material license paths still render this package in trial mode with a watermark. |
| `faceMesh` | `beauty/shapePackage/CC86C182-62D7-4F1D-AE9D-F5E4E99977A5/` | `ASSET_PACKAGE_TYPE_FACE_MESH`; applying it requires supported face detection |
| `theme` | `theme/97489A20-5143-4923-9A3D-0F57ED030366.1.theme` | `ASSET_PACKAGE_TYPE_THEME` |
| `font` | `font/FZSSJW.ttf` | copy to app-private storage, then `registerFontByFilePath(...)` |
| `sampleImage` | `sample/demo_base.jpg` | visible lightweight timeline and PIP base image |
| `sampleOverlayImage` | `sample/demo_overlay.jpg` | contrasting lightweight PIP overlay image |
| `sampleAudio` | `meicam/cartoon/cartoon.m4a` | smoke-test audio |
| `watermark` | `watermark/static_watermark.png` | static watermark image |
| `glitter` | `glitter/star4.png` | image input for glitter/overlay effects |
| `emptyBackground` | `background/nobackground.png` | background placeholder |

The repository-local external `temp_assets` bundle contains the inspected official Android LTS Demo's complete 11-file `facemode` directory (39,548,841 bytes) so local camera projects can select the correct model without reaching into the Skill. Generated capture code must still initialize only the models required by the requested effect: `demo2` uses the 240-point face model plus `facecommon`, `advancedbeauty`, and `fakeface`; it does not initialize segmentation, hand, eye-contour, avatar, or sky models. The bundle still excludes `msarface`, full AR/beauty material libraries, full fonts, full music, full background images, standard `.template`, Mimo, CutSame packages, and other optional resources. These model files remain external project inputs and are not stored inside the Skill. The observed official package has no reusable standard/Mimo/CutSame template package; contact Meishe business for any authorized material, template package, or production `.lic` acquisition.

APK asset paths are valid for asset-package installation and some SDK resource parameters, but generated editors must not assume `assets:/sample/demo_base.jpg` can be used as a Timeline media path. Before media probing or appending a copied external image/video clip, call `MeisheMediaFiles.copyAssetToProject(...)` and pass the resulting app-owned absolute file path. Keep the copied file in persistent project storage so process-death restore does not point at cache data that Android may evict.

## Install In Generated Apps

Generated projects include `MeisheSampleAssets` and `MeisheAssetInstaller`; their paths become usable only after the matching authorized external files are copied into the app.

```java
MeisheAssetInstaller installer = new MeisheAssetInstaller(sdkManager.getStreamingContext());
Map<String, String> packageIds = MeisheSampleAssets.installDefaultPackages(installer);
String filterPackageId = packageIds.get("filter");
String captionStylePackageId = packageIds.get("captionStyle");
String stickerPackageId = packageIds.get("animatedSticker");
```

Use the returned package ids with the normal SDK APIs:

- `NvsVideoClip.appendPackagedFx(filterPackageId)` or `NvsTimeline.addPackagedTimelineVideoFx(...)`
- `NvsVideoTrack.setPackagedTransition(...)` / transition APIs for packaged transitions
- `NvsTimeline.addCaption(..., captionStylePackageId)`
- The external `customsticker/.../None` package is an intentionally empty custom-sticker template. To produce a visible sample, call `NvsTimeline.addCustomAnimatedSticker(..., stickerPackageId, customImagePath)` with a copied image such as `assets:/watermark/static_watermark.png`; plain `addAnimatedSticker(...)` can succeed while displaying no content.

Always handle an empty package id as installation failure. Common causes are an explicitly reported license error, an incompatible supplied license, wrong package type, or omitted sample assets. Absence of a license is not universally a failure: known Demo packages can install and render in trial mode with empty license paths and a watermark. Do not search for replacement `.lic` files; direct production acquisition questions to Meishe business.

Do not label a capture-scene or AR-scene package as visibly applied merely because package installation or the setter/API call returned success. Gate AR controls on the required human-detection initialization and buddy capture flag. After setting `Scene Id`, call `getARSceneAssetPackagePrompt(...)`, expose any nonblank trigger instruction, perform it, and only then judge visibility. For the repository-local 927-byte capture-scene sample, show an explicit API-smoke-test limitation and require a customer-authorized visible capture-scene package before claiming a visual result. If installation, parameter readback, or face detection succeeds while the physical preview remains unchanged, follow `ar-face-runtime-troubleshooting.md`. Never convert `isSdkAuthorised() == false` alone into `LICENSE_REQUIRED`; it can mean trial rendering with a watermark. Refer users to Meishe business for production application/feature authorization and watermark removal.

## Large Human Models Hook

Human detection, AR face, beauty makeup, segmentation, avatar, eye contour, hand, and sky segmentation models are not stored in the skill. Download the official Android LTS face package, then use `<sdk-root>/samples/android/SdkDemo/app/src/main/assets/facemode` when those features are requested. Exact model filenames are recorded in `official-sdk-download-resource-map.json`.

Use the generator hook:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --features beauty-ar --human-models-dir <path-to-facemode-or-parent>
```

The script copies selected official-package files into `app/src/main/assets/facemode`. The `beauty-ar` template exposes `initializeMsHumanDetectionModels(...)` but does not call it by default. Validate the extracted root first with `scripts/inspect_official_sdk_package.py --sdk-root <sdk-root> --resource-keys R8,R9 --strict`.
