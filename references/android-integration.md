# Android Integration

This reference is distilled from the Android demo project. It is enough to reconstruct SDK integration without reading the demo.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Demo Module Responsibilities](#demo-module-responsibilities)
- [Runtime Permissions Seen In Demo](#runtime-permissions-seen-in-demo)
- [Local SDK Artifacts Seen In Demo](#local-sdk-artifacts-seen-in-demo)
- [Asset Families Seen In Demo](#asset-families-seen-in-demo)
- [External Lightweight Sample Assets](#external-lightweight-sample-assets)
- [Standalone Project Rules](#standalone-project-rules)
- [Generator Runtime Copy Pattern](#generator-runtime-copy-pattern)
- [Minimal Gradle Pattern](#minimal-gradle-pattern)
<!-- END GENERATED CONTENTS -->

## Demo Module Responsibilities

- `:MArScene`: Beauty and AR scene helpers.
- `:MCutSame`: Cut-same/template workflows.
- `:MMakeup`: Makeup data, helpers, and package handling.
- `:app`: Main application, UI flows, capture, edit screens, export, assets, and AndroidManifest permissions.
- `:libBase`: Shared utilities, local AAR/JAR dependencies, native jniLibs, asset package install helpers.
- `:libEngine`: Reusable timeline/editor engine abstractions and model-to-Nvs binding helpers.
- `:libNet`: Network/download helpers; omit unless the generated app needs online asset download.

## Runtime Permissions Seen In Demo

- `android.permission.ACCESS_MEDIA_LOCATION`
- `android.permission.ACCESS_NETWORK_STATE`
- `android.permission.ACCESS_NOTIFICATION_POLICY`
- `android.permission.ACCESS_WIFI_STATE`
- `android.permission.CAMERA`
- `android.permission.CHANGE_WIFI_STATE`
- `android.permission.INTERNET`
- `android.permission.READ_EXTERNAL_STORAGE`
- `android.permission.READ_MEDIA_AUDIO`
- `android.permission.READ_MEDIA_IMAGES`
- `android.permission.READ_MEDIA_VIDEO`
- `android.permission.READ_MEDIA_VISUAL_USER_SELECTED`
- `android.permission.READ_PHONE_STATE`
- `android.permission.RECORD_AUDIO`
- `android.permission.VIBRATE`
- `android.permission.WRITE_EXTERNAL_STORAGE`

Request only the permissions needed by the generated workflow and gate the feature on the permission result callback. Camera recording normally needs `CAMERA` and `RECORD_AUDIO`; media import/export needs Android-version-specific media permissions and scoped-storage-safe paths.

## Local SDK Artifacts Seen In Demo

AARs under the demo's `libBase/libs`:
- `extension-flac-release.aar` (0.17 MB)
- `libMeicamAI-3.8.1.1.aar` (1.28 MB)
- `library-core-release.aar` (1.21 MB)
- `library-ui-release.aar` (0.21 MB)

Native libraries under the demo's `libBase/src/main/jniLibs`:
- `arm64-v8a/libNvStreamingSdkCore.so` (16.22 MB)
- `armeabi-v7a/libNvStreamingSdkCore.so` (12.41 MB)

License asset observed: `true`

## Asset Families Seen In Demo

- `animation`
- `arface`
- `audio`
- `background`
- `beauty`
- `captionanimation`
- `captionbubble`
- `captionrichword`
- `captionstyle`
- `capture`
- `capturescene`
- `compoundcaption`
- `curve_speed`
- `customsticker`
- `cutsamefont`
- `douvideoeditfilter`
- `facemode`
- `filter`
- `flipcaption`
- `font`
- `glitter`
- `meicam`
- `msarface`
- `music`
- `musiccaption`
- `particle`
- `picinpic`
- `record`
- `sticker`
- `stickeranimation`
- `theme`
- `transition`
- `voice`
- `watermark`

For feature-specific resource requests, use `resource-requirements-index.md` and `official-sdk-download-resources.md`. The latter maps each Demo family and model to an exact path relative to an extracted official Android LTS face package.

## External Lightweight Sample Assets

The skill stores no material binaries. In this repository, generated projects first look for `temp_assets/android-sample-assets`; an installed or relocated skill uses `--sample-assets-dir <authorized-bundle-root>`. The external bundle may contain a deliberately small offline demo set such as a packaged filter, transition, caption style, animated sticker, capture scene, watermark image, glitter image, small image, small audio clip, and empty background placeholder.

Before generation, tell the user to contact Meishe business for authorized material resources. After copying them into the project, use `MeisheSampleAssets.installDefaultPackages(...)` to install package assets and obtain package ids. Use `--no-sample-assets` only when the user asks for a clean project with no demo resources.

Do not confuse these small external samples with complete SDK assets. Large model/resource families such as `facemode`, `arface`, `msarface`, full `font`, full `cutsamefont`, template packages, full music, and full background sets also remain external.

## Standalone Project Rules

- Put the license at `app/src/main/assets/meishesdk.lic` or adapt the `assets:/...` URI in SDK initialization.
- Put `libNvStreamingSdkCore.so` under `app/src/main/jniLibs/<abi>/` or a library module's equivalent path.
- Put Meishe AAR/JAR files under `app/libs` or a dedicated SDK library module, then wire `flatDir`/`fileTree` dependencies.
- Import Streaming SDK classes from `com.meicam.sdk` and Effect SDK classes from `com.meicam.effect.sdk`, matching the demo.
- Prefer `arm64-v8a`; add `armeabi-v7a` only when required.
- Exclude demo FTP download tasks, signing configs, app ids, analytics keys, and network helper modules unless explicitly requested.
- Keep model and asset packages optional and feature-scoped. Face/beauty/segmentation/makeup/AR features need their corresponding model/package assets.
- Obtain human-detection models from `<sdk-root>/samples/android/SdkDemo/app/src/main/assets/facemode` in the official Android LTS face package. Use `--human-models-dir <path-to-facemode-or-parent>` to copy selected files into `app/src/main/assets/facemode` when AR/beauty/segmentation is requested.
- Use app-specific output directories plus MediaStore scanning/insertion for exported media.

## Generator Runtime Copy Pattern

Copy SDK runtime artifacts during project creation when a local SDK distribution is available:

```powershell
python .\.codex\skills\meishe-android-streaming-sdk-api\scripts\create_android_project.py <output-dir> --sdk-root <path-to-sdk-root> --license <path-to-meishesdk.lic>
```

Options:

- `--abis arm64-v8a`: default, copies `lib/android_arm64/libNvStreamingSdkCore.so`.
- `--abis arm64-v8a,armeabi-v7a`: also copies `lib/android_armv7/libNvStreamingSdkCore.so`.
- `--include-extra-sdk`: copies all `extrasdk/sdk/android` `.jar` and `.aar` files to `app/libs` and adds Demo-matched `androidx.appcompat:appcompat:1.0.0`, which is required by `cafconvertor.aar` resources.
- `--human-models-dir <path>`: copies selected `facemode` models from the official face package, or equivalent authorized files, into assets.
- `--sample-assets-dir <path>`: copies an authorized external bundle containing `app/src/main/assets`.
- `--no-sample-assets`: skips external sample bundle discovery and copying.

When `--sdk-root` is set, the generator copies `extrasdk/sdk/android/effectlib.jar` only when the selected composition enables the `beauty-ar` overlay or `--include-extra-sdk` is explicit. The core editor and asset-center shells normally need only `NvAndroidStreamingSdk.jar`, `libNvStreamingSdkCore.so`, and `meishesdk.lic`. Effect SDK initialization lives in the optional beauty/AR controller so the base runtime does not acquire that dependency accidentally.

## Minimal Gradle Pattern

The demo uses module-level `flatDir` repositories for local SDK artifacts. Do not combine module-level `repositories { flatDir ... }` with `RepositoriesMode.FAIL_ON_PROJECT_REPOS`; use project repositories or a non-failing repository mode.

```groovy
repositories {
    flatDir { dirs 'libs' }
}

android {
    defaultConfig {
        ndk { abiFilters 'arm64-v8a' }
    }
}

dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar', '*.aar'])
}
```
