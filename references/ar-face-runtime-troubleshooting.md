# AR And Face Runtime Troubleshooting

Use this checklist when an AR scene, capture scene, face mesh, face shape, makeup, or face-driven capture effect installs or reports success but remains invisible on a physical device.

## Evidence Rule

Keep these outcomes separate:

1. SDK/model initialization succeeded.
2. A package installed and returned a package id.
3. The effect setter stored the expected value.
4. Face detection callbacks returned a face.
5. The physical preview visibly changed.

Only item 5 proves a visible effect. Compilation, installation, setter success, package-id readback, or a nonzero face count must not be reported as visual success.

## Ordered Checklist

Run the checks in this order and stop once one layer fails.

1. Record the SDK version, device model/API, `applicationId`, camera facing, preview ratio, selected effect, package id, and package type.
2. Record `NvsStreamingContext.isSdkAuthorised()` and `NvsStreamingContext.hasARModule()` before applying the effect. Treat `isSdkAuthorised() == false` as trial/watermark evidence, not as proof that AR rendering is disabled and not as a reason to gate the control.
3. Confirm the selected 106-point or 240-point main human-detection model initialized. Do not initialize both as competing defaults. When reproducing Demo behavior, inspect its actual build variant: the standard `debug` variant in the observed 3.16.1.25 Demo uses the 106-point model, while `debug240` uses the 240-point model.
4. Record every optional data result needed by the effect, such as face-common, advanced-beauty, or fake-face data. Preserve the official `facemode/ms` and `facemode/common` layout.
5. Confirm capture preview uses `STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME` and a detectable front-camera face occupies a meaningful part of the frame.
6. Align the initialized detection feature flags with the selected model and version-proven Demo path. Do not force `setDetectionMode(...)`, `setDetectionAutoProbe(...)`, or `Use Face Extra Info` merely to make callbacks nonzero when the corresponding Demo capture path does not set them.
7. Record `isAndroidCameraPreferDualBufferAR()` and the effect's `Single Buffer Mode`; keep buffer mode consistent with the device path.
8. Validate package type, package path, supplied-or-empty package license path, install/upgrade result, ready status, and nonblank returned package id. An empty SDK or material license path is a valid trial path for packages that support evaluation; a missing license must not be treated as a universal install/render failure.
9. Apply the effect, then read back its stored package id/parameter. For AR scene check `Scene Id`; for face mesh check the enable flag, degree/strength, and exact custom package key.
10. Call `NvsAssetPackageManager.getARSceneAssetPackagePrompt(packageId)` immediately after AR-scene application. If it returns a nonblank instruction, show it in the UI or a toast and perform that action before declaring the material invisible. Some Demo packages are action-triggered rather than continuously visible.
11. Attach `NvsARSceneManipulate.setARSceneCallback(...)` and record both face-bounding-box count and face-feature count while a face is visible.
12. Capture a screenshot or short recording after performing any reported trigger. Treat `Trial Version` as evidence of evaluation mode: it neither proves nor disproves visual-effect rendering.

## Stable Issue Checklist

| ID | Failure evidence | Conclusion | Required action |
| --- | --- | --- | --- |
| `ARF-01` | `isSdkAuthorised() == false`, usually with `Trial Version` | The application is running in trial/evaluation mode. This does not by itself disable AR scene or face-mesh rendering. | Keep trial-capable controls usable and continue the model/package/prompt/preview checks. Contact Meishe business only for a production license that matches the exact `applicationId` and removes the watermark; never spoof another package name or copy an unrelated license. |
| `ARF-02` | `hasARModule()` reports unavailable | The selected runtime does not contain the required AR module. | Verify the SDK distribution before changing models or packages; obtain the correct commercial distribution from Meishe business when needed. |
| `ARF-03` | Main human-detection initialization returns `false` | Main model, path, feature flags, SDK binary, or authorization is invalid. | Validate the official face-package relative path and initialize only the selected main model. |
| `ARF-04` | Required optional face data returns `false` | The requested effect lacks supporting face-common/beauty/fake-face data. | Copy and initialize only the data required by the selected effect; log each result separately. |
| `ARF-05` | Buddy-host frame capture flag is absent | AR manipulation cannot receive the required capture frames. | Restart capture preview with `STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`. |
| `ARF-06` | Initialized feature flags and forced manipulation overrides disagree with the version-proven Demo path | The detector and AR scene may consume different face-data modes. | Align feature flags with the selected model and remove speculative detection-mode/autoprobe/extra-info overrides before adding more flags. |
| `ARF-07` | Face callbacks remain at zero | No usable face is reaching AR manipulation. | Check camera facing, permissions, lighting, face size, orientation, buddy frames, detection mode, and model results. |
| `ARF-08` | Install status is not ready, package id is blank, or readback differs | Package installation, type, license, or setter application failed. | Fix package/type/license/install ordering and wait for asynchronous completion before applying it. |
| `ARF-09` | Project model variant differs from the Demo build/resource variant being reproduced | Package/model behavior is being compared across different 106/240 configurations. | Match the Demo build variant and its single main-model path before evaluating the material. |
| `ARF-10` | Face count is nonzero, ids match, preview is unchanged, and `getARSceneAssetPackagePrompt(...)` returns an instruction | The material is action-triggered and the required action has not yet been demonstrated, or the application hid the instruction. | Display the prompt and perform the reported action on camera before declaring failure. |
| `ARF-11` | Package is documented as a smoke-test placeholder | The resource proves only API installation/application. | Do not use it as visual proof; obtain a customer-authorized visible package from Meishe business. |
| `ARF-12` | Only build logs, setter returns, UI status, or package ids exist | Runtime visual evidence is incomplete. | Report `build_verified`, `installed`, or `configured` only; request optional physical-device screenshot QA before claiming visibility. |
| `ARF-13` | Face count is nonzero, ids match, any prompt was performed, but preview is still unchanged | Remaining causes are package compatibility, effect parameters, model variant, ratio, preview-start ordering, or single/dual-buffer behavior. | Compare the exact Demo build/model, typed parameters, FX creation order, buffer settings, preview flags, and one known-visible package. Treat license as a cause only when an API/error explicitly reports a license failure. |

## Decision Matrix

| Authorization | Face count | Package/readback | Trigger/preview | Diagnosis |
| --- | ---: | --- | --- | --- |
| false | any | any | `Trial Version` visible | `ARF-01`; evaluation mode is confirmed, but it is not a rendering blocker. Continue with the remaining columns. |
| any | 0 | any | unchanged | `ARF-03` through `ARF-07`; inspect model and capture/detection pipeline. |
| any | greater than 0 | blank/different/not ready | unchanged | `ARF-08`; inspect package installation and setter contract. |
| any | greater than 0 | exact | nonblank prompt not yet performed | `ARF-10`; expose and perform the material trigger first. |
| any | greater than 0 | exact | prompt performed, still unchanged | `ARF-09` or `ARF-13`; inspect model variant, parameters, compatibility, ratio, FX creation order, and buffer mode. |
| any | greater than 0 | exact | visibly changed | The exact tested configuration has visual evidence. `isSdkAuthorised() == false` only explains the trial watermark; record the screenshot, device, SDK, application, trigger, and resource scope. |

## Minimum Diagnostic Log Contract

Capture concise, searchable lines for:

- `SDK diagnostics: authorised=<value>, arModule=<value>, sdkLicensePresent=<value>, preferDualBufferAr=<value>`
- `Human detection initialized: modelPoints=<106|240>, main=<value>, faceCommon=<value>, advancedBeauty=<value>, fakeFace=<value>`
- `AR scene installed: code=<value>, packageId=<value>, packageLicensePresent=<value>`
- `AR scene configured: singleBuffer=<value>, sceneId=<readback>, prompt=<value>`
- `Face mesh configured: enabled=<value>, strength=<value>, packageId=<readback>`
- `AR face bounding boxes: count=<value>`
- `AR face features: count=<value>`

Do not dump full model files, licenses, credentials, broad UI trees, or unrelated logcat output.

## Observed Diagnostic Case: 2026-08-05

This case corrects the earlier license-first diagnosis and records a physical-device visual verification.

- SDK: Android Streaming SDK `3.16.1.25`; device: Samsung `SM-A5460`, Android API `35`; application: `com.example.demo2`.
- The final comparison used the official Demo standard `debug` model choice: 106-point main model plus face-common, advanced-beauty, and fake-face data. The normal Demo feature flags were `FACE_LANDMARK | FACE_ACTION | SEMI_IMAGE_MODE`.
- SDK initialization and both AR-scene and face-mesh package installation were run with empty license paths. Logs reported `isSdkAuthorised() == false`, `sdkLicensePresent=false`, `packageLicensePresent=false`, and the preview displayed `Trial Version`.
- Buddy-host capture was enabled, dual-buffer preference produced `Single Buffer Mode=false`, and the AR scene id readback was `EDF352FC-701B-4C05-86CE-B0E293469341`.
- `getARSceneAssetPackagePrompt(...)` returned `请张嘴试一试~`. Once the subject opened their mouth, the dancing-note graphics became visible around the mouth while the trial watermark remained.
- Face-mesh package `CC86C182-62D7-4F1D-AE9D-F5E4E99977A5` installed with an empty package-license path and stored strength `1.0`; face-bounding-box and face-feature callbacks both reached `count=1`.
- Conclusion: lack of license was not the rendering blocker. The apparent AR failure was missing trigger guidance (`ARF-10`). Generated camera UIs must surface the package prompt instead of only saying that the material is installed or active. Production authorization is still required to remove the watermark and must be obtained from Meishe business.
