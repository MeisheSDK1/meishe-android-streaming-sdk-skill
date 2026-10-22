# Project Structure Rules

- Keep Activity classes focused on lifecycle, permissions, UI binding, Activity Result, and navigation. Put SDK work in small controllers/managers and initialize `NvsStreamingContext` once before using `getInstance()`.
- Keep `MeisheEditorActivity` free of direct `NvsTimeline`, track, clip, caption, sticker, audio, and `NvsLiveWindow` mutations. Route editor behavior through `MeisheEditorCoordinator`, session, command, overlay, voiceover, project, and UI-binding controllers.
- Persist editor projects as version-3 JSON under `filesDir/meishe-projects/<projectId>/project.json` with stable object ids, atomic writes, explicit migration, and namespaced extensions. Never persist SDK object references or synthesize undo history after process restoration.
- Keep undo/redo as at most 50 complete in-memory project snapshots, persist only the latest state, and remap stable ids after split/delete/move operations.
- A complete editor includes media import, ratio/resolution, persisted Timeline state, `NvsTimeline`, `NvsLiveWindow`, playback/seek callbacks, child editors, applied-material state, and compile/export. Preview and recording alone are not a complete editor.
- After deleting the final clip, explicitly clear/hide LiveWindow and show an empty state instead of seeking a zero-duration Timeline. Restore/reconnect the preview when media is added again.
- When an authorized bundle contains `customsticker/.../None`, use it as a custom-sticker template with `addCustomAnimatedSticker(..., customImagePath)`, not `addAnimatedSticker(...)`.
- When a caption receives context/renderer/animation packages, create it with `addModularCaption` and apply renderer -> context -> animation with the animation period set first; `addCaption` captions reject modular applies.
- Expose X/Y movement on caption/sticker property editors via `setCaptionTranslation` / `translateAnimatedSticker`, persist translationX/Y, and keep applied-material dialogs scrollable with a pinned bottom action bar.
- Stop playback/capture/export before structural Timeline mutation or compile. Register and handle playback, seek, engine-state, capture-device, recording, asset-install, and compile callbacks for interactive flows.
- Install packages with the correct type and original filename. Accept `ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS` only as an asynchronous start and wait for completion before querying descriptors or applying package ids. Installation never implies application.
- Keep Mimo separate from `.template` installation: safely extract its ZIP, parse `info.json`, install child packages, and build a normal Timeline from the shot recipe.
- Initialize `NvsEffectSdkContext` and only the human-detection models required by selected beauty, makeup, AR, or segmentation features. Import Effect SDK classes from `com.meicam.effect.sdk`. Prefer `arm64-v8a`; add `armeabi-v7a` only when requested or required.
- Request only capability-required permissions and gate camera, audio, and media actions on permission callbacks.
