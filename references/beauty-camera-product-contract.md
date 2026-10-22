# Beauty Camera Product Contract

Use this contract when the `beauty-camera` product shell is generated with
capture modules beyond its default module set. Resolving a module is not enough:
each resolved user-facing capability must have a reachable control, an SDK call
chain, and an observable success, failure, or unavailable-resource state.

## Material picker and dispatch

1. The camera opens `MeisheAssetCenterActivity` in picker mode. An installed
   capture-only material returns to the owning camera with `RESULT_OK`; it must
   not launch a second camera/sample Activity from the material center.
2. The result preserves package ID, SDK package type, semantic application kind,
   material key, and human label.
3. Dispatch uses both semantic application kind and SDK package type:
   - a packaged filter or generic capture FX uses
     `appendPackagedCaptureVideoFx`;
   - Capture Scene uses `applyCaptureScene`;
   - an AR Scene package binds to the active AR Scene FX through `Scene Id`;
   - Face Mesh binds to an AR Scene FX and enables `Beauty Shape` and
     `Face Mesh Internal Enabled`; the repository sample is an eyebrow-angle
     package and therefore uses `Face Mesh Eyebrow Angle Custom Package Id`
     plus a nonzero `Face Mesh Eyebrow Angle Degree`;
   - Makeup binds to an AR Scene FX with its makeup enable, package, and
     intensity parameters, and enables `Makeup Custom Enabled Flag` with
     `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`.
4. Capture Scene, Face Mesh, and Makeup must never silently fall through to the
   generic packaged-filter branch.
5. Reject a returned result when its semantic application kind and SDK package
   type do not form a supported pair; do not guess a route from either value
   alone.
6. If an authorized Makeup or Face Mesh package is not present in the external
   material bundle, keep the control reachable and show a precise unavailable
   resource state. Do not claim a visible effect and do not fabricate a package.

## Full capture controls

When `capture-camera`, `capture-filter`, `capture-scene`, `beauty-camera`,
`makeup-service`, `ar-scene`, and `segmentation-keying` are all resolved, the
product screen exposes:

- camera switching and capture preview state;
- focus, flash, zoom, and exposure controls, capability-gated for the active
  device;
- capture filter and material-picker entry;
- Capture Scene, beauty, Makeup, Face Mesh, AR Scene, and segmentation entries;
- record, pause, resume, and stop states.

Focus/flash/zoom/exposure controls call
`MeisheCaptureController.getDeviceCapability` and
`MeisheCaptureController.configureDeviceControls`. Unsupported capabilities
remain disabled or report an explicit unsupported state rather than pretending
that an SDK call succeeded. Keep requested and active camera indexes separate:
the active index changes only after the preview/capability callback confirms the
device selected by the SDK.

## Recording and callbacks

Recording pause/resume is a real SDK state transition:

- pause calls `NvsStreamingContext.pauseRecording()` and changes UI state only
  when it returns `true`;
- resume calls `NvsStreamingContext.resumeRecording()` and changes UI state only
  when it returns `true`;
- stop finalizes the output and restores the idle controls.

Register `CaptureDeviceCallback`, `CaptureRecordingStartedCallback`,
`CaptureRecordingDurationCallback`, and
`CaptureRecordingFrameReachedCallback`. Use preview/capability callbacks to
confirm the active device, the first-frame callback to expose that recording is
actually producing frames, and the device callback's finished/error methods to
settle the final output state. A stop request uses synchronous finalization and
does not announce a saved recording before the finished callback. Their
callbacks update the user-visible camera/recording state on the Android UI
thread. Teardown clears all four callbacks consistently with the owning Activity
lifecycle.

## Android registration

Every Activity reachable from the generated camera screen must be declared in
`app/src/main/AndroidManifest.xml`. The full capture shell requires at least the
launcher `MainActivity`, `MeisheAssetCenterActivity`, `CAMERA`, and
`RECORD_AUDIO`. If a future Makeup, Face Mesh, Capture Scene, or device-control
flow introduces another Activity, generation must register that Activity in the
same change.

## Evidence boundary

Static generation proves controls and call chains only. A Gradle build proves
compilation, and a physical-device run proves the exercised runtime flow. Face
Mesh, Makeup, and AR visibility still require the exact authorized package,
models, subject conditions, and physical-preview visual evidence described in
`ar-face-runtime-troubleshooting.md`.
