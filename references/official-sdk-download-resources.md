# Official Android LTS Package Resources

Use this reference when SDK binaries, Effect SDK libraries, full face/segmentation models, Demo material families, or Demo source references are missing.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Download Route](#download-route)
- [Resolve Before Copying](#resolve-before-copying)
- [Core And Extension Paths](#core-and-extension-paths)
- [Human Detection And AI Models](#human-detection-and-ai-models)
- [Demo Material Families](#demo-material-families)
- [Template Boundary](#template-boundary)
- [Copy Rules](#copy-rules)
<!-- END GENERATED CONTENTS -->

## Download Route

1. Open `https://www.meishesdk.com/downloads`.
2. Enter `SDK下载及开发文档` and select Android LTS.
3. Click `下载SDK人脸版本`. The face variant is required when the request includes beauty, makeup, AR, face shape, avatar, hand/eye detection, human segmentation, sky segmentation, or SuperZoom.
4. Extract the package. Treat the directory containing `lib`, `extrasdk`, `samples`, and `doxygen` as `<sdk-root>`.
5. Never record the user's absolute download directory in generated source or skill references. Resolve the paths below relative to `<sdk-root>`.

The package used to train this skill is identified by the relative Demo root `samples/android/SdkDemo`. The skill remains independent: this path is an optional user-provided resource source, not a use-time dependency.

Build-time reference roots in the same package are `doxygen`, `samples/android/NvEffectKitDemo`, and `samples/android/customvideofx`. Normal Skill use never reads those trees; their reusable knowledge is already stored in the Skill.

## Resolve Before Copying

Run the bundled inspector against the extracted root:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\inspect_official_sdk_package.py --sdk-root <sdk-root> --strict
```

Filter the result for a feature:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\inspect_official_sdk_package.py --sdk-root <sdk-root> --resource-keys R0,R8,R9 --modules beauty-camera,segmentation-keying
```

The machine-readable map is `official-sdk-download-resource-map.json`.

## Core And Extension Paths

| Need | Source relative to `<sdk-root>` | Generated-project destination |
| --- | --- | --- |
| Streaming SDK Java API | `lib/android_jar/NvAndroidStreamingSdk.jar` | `app/libs/NvAndroidStreamingSdk.jar` |
| arm64 runtime | `lib/android_arm64/libNvStreamingSdkCore.so` | `app/src/main/jniLibs/arm64-v8a/libNvStreamingSdkCore.so` |
| armv7 runtime | `lib/android_armv7/libNvStreamingSdkCore.so` | `app/src/main/jniLibs/armeabi-v7a/libNvStreamingSdkCore.so` |
| Effect SDK Java API | `extrasdk/sdk/android/effectlib.jar` | `app/libs/effectlib.jar` |
| Media conversion | `extrasdk/sdk/android/cafconvertor.aar`, `nvconvertorlib.aar` | Copy only when the selected conversion module requires them. |
| Lyric/joke-caption/photo-album helpers | `extrasdk/sdk/android/nvmusicLyricslib.jar`, `nvjokeCaptionlib.jar`, `NvPhotoAlbumHelperLib.jar` | Copy only the selected helper. |
| Streaming Demo license | `samples/android/SdkDemo/app/src/main/assets/meishesdk.lic` | Demo/evaluation scope only. Production licensing goes through Meishe business. |
| Effect Kit Demo license | `samples/android/NvEffectKitDemo/app/src/main/assets/effectsdkdemo.lic` | Effect Kit Demo/evaluation scope only. |

`create_android_project.py --sdk-root <sdk-root>` already understands the `lib` and `extrasdk` layout. Use `--include-extra-sdk` only when the selected modules need optional helper libraries.

## Human Detection And AI Models

The complete Streaming SDK model directory is:

`samples/android/SdkDemo/app/src/main/assets/facemode`

Preserve its subdirectories:

- `facemode/ms`: 106-point and 240-point face models.
- `facemode/common`: face-common, advanced beauty, fake-face, human segmentation, hand, eye contour, avatar, and sky segmentation data.

Use it directly with:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --sdk-root <sdk-root> --human-models-dir <sdk-root>\samples\android\SdkDemo\app\src\main\assets\facemode
```

Do not copy the entire model directory when the selected feature needs only a subset. Read the exact file list in `official-sdk-download-resource-map.json` and preserve `facemode/ms` and `facemode/common` placement.

## Demo Material Families

All Streaming SDK Demo material families start at:

`samples/android/SdkDemo/app/src/main/assets`

Select only the requested subdirectory. Important mappings include:

| Feature | Relative source directories |
| --- | --- |
| Filters/effects/transitions | `filter`, `douvideoeditfilter`, `animation`, `transition`, `particle`, `picinpic` |
| Captions/stickers/fonts | `captionstyle`, `captionbubble`, `captionrichword`, `captionanimation`, `compoundcaption`, `sticker`, `customsticker`, `stickeranimation`, `font`, `cutsamefont` |
| Beauty/makeup/AR | `beauty`, `arface`, `msarface`, `capturescene`, `facemode` |
| Audio/lyrics/voice | `audio`, `music`, `musiccaption`, `flipcaption`, `voice`, `record` |
| Themes/quick splicing/PIP/watermark | `theme`, `meicam`, `background`, `picinpic`, `watermark`, `glitter` |

Keep each package file paired with its adjacent metadata, preview, and sidecar `.lic` when present. These Demo files do not grant production rights; production package or license questions still go to Meishe business.

## Template Boundary

The observed Android face package contains the implementation sources:

- Mimo: `samples/android/SdkDemo/app/src/main/java/com/meishe/sdkdemo/mimodemo`
- CutSame and SDK template workflows: `samples/android/SdkDemo/MCutSame`
- Quick-splicing XML/audio/image examples: `samples/android/SdkDemo/app/src/main/assets/meicam`

It does not contain a reusable `.template` file, Mimo ZIP, or local CutSame template resource package. `assets/font/info_mimo.json` is font metadata, not a Mimo package. Keep the skill's template resource slots and ask for a separately authorized template package rather than claiming one exists in the download.

## Copy Rules

- Do not copy the full `SdkDemo`, `NvEffectKitDemo`, `facemode`, or all asset families into a generated app.
- Copy the SDK runtime plus only the resource directories required by the selected module closure.
- Preserve package filenames and relative directory structure.
- Do not copy signing files, service request configuration, network clients, analytics configuration, or release settings.
- Validate the extracted package with the inspector whenever the downloaded SDK version changes.
