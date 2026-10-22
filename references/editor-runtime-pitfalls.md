# Verified Editor Runtime Pitfalls And Fixes

Device-verified fixes that must not regress when creating or patching an editor, material center,
or applied-material property editor. Evidence: SM-A5460 (Android 15, API 35, arm64-v8a), trial
license, `demo3` template project (build 2026-08-07).

## 1. Modular caption materials require a modular caption object

Symptom: 字幕气泡 (caption context), 富文本字幕渲染器 (caption renderer), and 字幕动画 (caption
animation) packages install successfully, but applying them to a new caption fails with
"字幕素材无法应用到新字幕，请检查素材类型与授权。" and the caption is removed.

Root cause: the caption was created with `timeline.addCaption(text, inPointUs, durationUs, styleId)`.
`applyModularCaptionContext`, `applyModularCaptionRenderer`, and `applyModularCaptionAnimation`
return `false` on a traditional (non-modular) caption. This is not an SDK-version or license gate;
the bundled SDK supports these packages (including NVAP v2 renderer packages).

Rules:
- Create the caption with `timeline.addModularCaption(text, inPointUs, durationUs)` whenever the
  apply plan includes a context, renderer, or animation package. Use `addCaption` only for plain or
  style captions.
- Apply in the Demo order: renderer first, then context, then combination animation. Set
  `setModularCaptionAnimationPeroid(periodMs)` before `applyModularCaptionAnimation` when the
  current period is 0.
- Guard with `caption.isModular()` before modular applies, and log which apply call returned false.
- The project restore path must also use `addModularCaption` for persisted modular captions
  (detect via non-empty context/renderer/animation package ids) and restore the animation period.
- Do not combine `applyCaptionStyle` and modular packages on the same caption; they are different
  caption types.

## 2. Applied-material property dialog must scroll and keep actions visible

Symptom: with many editable fields (text, duration, font size, opacity, scale, rotation, X/Y,
volume, fades) the dialog fills the whole screen and the 取消/删除/保存 buttons are below the fold.

Rules:
- Wrap the field container in a vertical `ScrollView` with `setFillViewport(true)`.
- Place the scroll area in a `LinearLayout` with `layout_weight = 1` and pin a bottom button bar
  (取消 / 删除 / 保存) below it so actions stay visible on any screen size.
- Cap the dialog window size, e.g. `MATCH_PARENT` width and `0.72 * screenHeight` height, instead
  of leaving the default full-height layout.

## 3. Captions, compound captions, and stickers must expose X/Y movement

Symptom: users cannot reposition a caption or sticker; only scale/rotation/opacity are editable.

Rules:
- Expose horizontal/vertical offset fields (canvas pixels; negative Y = up) for caption, compound
  caption, and animated sticker property editors.
- Apply on save with the correct SDK call:
  - caption / compound caption: `caption.setCaptionTranslation(new PointF(x, y))`; wrap in
    `setRecordingUserOperation(true/false)` and `setCurrentKeyFrameTime(...)` when recording
    keyframes.
  - animated sticker: `sticker.translateAnimatedSticker(new PointF(x, y))`.
- Persist `translationX` / `translationY` in the project descriptor and re-apply them on restore
  with the same calls; a position edit must survive reapply and process restart.
