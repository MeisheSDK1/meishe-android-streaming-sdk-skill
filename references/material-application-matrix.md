# Material installation, application, editing, and removal

Use this matrix whenever a generated app exposes a material center. Installing or registering a file only makes the material available to the SDK. It is not an editor operation until a concrete timeline, clip, caption, sticker, transition, theme, or capture object uses the returned package ID or local path.

## Application matrix

| Material family | Application scope and API | Can apply with defaults? | Required user/project input | Instance properties to expose | Removal behavior |
|---|---|---|---|---|---|
| Packaged filter | Selected `NvsVideoClip`; `appendPackagedFx(packageId)` | Yes, after a target clip is selected | Target clip is project selection, not a form field | Filter intensity when supported by the package | Remove the matching clip FX or remove its descriptor and rebuild editor features |
| Clip animation / generic packaged video FX | Selected `NvsVideoClip`; `appendPackagedFx(packageId)` | Yes | Target clip | Package-supported intensity/parameters; do not invent undocumented parameter keys | Remove matching clip FX or descriptor |
| Transition | Boundary after the selected clip; `setPackagedTransition(sourceClipIndex, packageId)` | Yes when at least two clips exist | Two adjacent clips | Transition duration and duration-match mode | Replace with an empty built-in transition or remove the descriptor |
| Caption style | New or selected `NvsTimelineCaption`; `addCaption(..., stylePackageId)` or `applyCaptionStyle` | No when creating a caption | Visible caption text | Text, in/out or duration, font size, opacity, scale, rotation | `timeline.removeCaption(caption)` or remove descriptor |
| Caption context / renderer / animation | Create the caption with `addModularCaption(text, inPointUs, durationUs)`, then apply `applyModularCaptionRenderer`, `applyModularCaptionContext`, `applyModularCaptionAnimation` in that order (set the animation period before the animation apply) | No; a new modular caption must use `addModularCaption`, never `addCaption` | Visible caption text | Caption text/timing/typography/transform, X/Y via `setCaptionTranslation`, animation period when exposed | Remove the caption instance, or clear/replace the modular package on the selected caption |
| Compound caption | `addCompoundCaption(inPoint, duration, packageId)` | No | Text for one or more package-defined slots; line-separated text is an acceptable simple UI contract | Slot text, duration, opacity, scale, rotation | `timeline.removeCompoundCaption(caption)` or remove descriptor |
| Font | `registerFontByFilePath`, then `caption.setFontByFilePath(localPath)` | Only for an existing caption | Existing caption, or text when creating one | Caption text/timing/font size/opacity/transform | Removing the caption removes the applied font instance; registering the font itself is not an on-track item |
| Custom animated-sticker template | `addCustomAnimatedSticker(..., packageId, customImagePath)` | No | A readable local custom image path | Duration, translation, scale, rotation, opacity, volume, animation packages | `timeline.removeAnimatedSticker(sticker)` or remove descriptor |
| Sticker in/period/out animation | `applyAnimatedStickerInAnimation` and matching methods on an existing sticker | Yes only when a sticker already exists | Existing sticker selection | Sticker timing/transform/opacity/volume and animation duration | Removing the sticker removes its animation; a modifier package should not appear as an unrelated standalone timeline object |
| Music / audio | `NvsAudioTrack.addClip(path, ...)` | No | A readable audio source path | Timeline position, trims, volume, fade-in, fade-out | Remove matching audio clip or descriptor |
| Theme | `timeline.applyTheme(packageId)` | Yes when the timeline contains usable media | Timeline | Theme music volume | `timeline.removeCurrentTheme()` and clear the theme descriptor |
| Capture scene / AR scene | Capture preview only; capture-video-FX or AR-scene APIs | Yes only in the camera workflow and after model/license gates pass | Active capture preview; some AR features also require face models | Feature-specific capture parameters | Remove or replace it in the camera module; never list it as a timeline item |
| Face mesh | Bound by beauty/AR APIs | No standalone track operation | Beauty/AR scene plus required models | Beauty/AR module parameters | Managed by the owning beauty/AR effect |
| Makeup | Bound to the active AR-scene capture FX through makeup package and intensity parameters | No when the external bundle has no authorized makeup package | Active camera preview, AR/face models, selected makeup package | Makeup part, intensity, color when supported, replace/remove | Clear the owning AR-scene makeup parameter or replace the selected package |

## Generated-app contract

1. The material center must return a stable material key, human label, SDK package type, local path when relevant, and a semantic application kind. Do not dispatch only on `packageType`: filter, clip animation, particle, and picture-in-picture packages can all report `ASSET_PACKAGE_TYPE_VIDEOFX` but require different product semantics.
2. Show the selected material's application requirement and editable-property summary before installation and again before use.
3. Collect required input before creating the SDK object. Never insert placeholder caption text such as “style applied” or “font applied”.
4. Persist each applied instance with a stable ID. The editor's “Applied materials” strip must be derived from project state, not from the installed-package list.
5. A property update changes the descriptor, reapplies the editor state, persists history, and refreshes the LiveWindow. A deletion removes the descriptor, reapplies state, persists history, and refreshes the LiveWindow.
6. Modifier packages belong to their owning instance. A caption renderer belongs to a caption; a sticker in-animation belongs to a sticker. Show the modifier in that instance's summary instead of fabricating an unrelated track object.
7. Material binaries are not bundled in this Skill. For external use, tell the user to contact Meishe business for authorized material packages, licenses, and required models, then provide them with `--sample-assets-dir` when generating a local runnable sample.
8. When a camera opens the material center in picker mode, every installed capture-only material returns to that camera with the complete result contract. The material center must not launch a nested sample camera. The camera dispatches Capture Scene through `applyCaptureScene` and keeps AR Scene, Face Mesh, Makeup, and generic capture FX on their distinct semantic paths.

## Template implementation

- Catalog contract: `MeisheLocalMaterialCatalog.Entry`
- Intent extras: `MeisheAssetCenterConfig`
- Application dispatch: `MeisheEditorOverlayController.applyInstalledMaterial`
- Persistent descriptors and restore: `MeisheEditorProjectStore`
- Applied-instance model: `MeisheAppliedMaterial`
- Applied-material UI and property editor: `MeisheEditorUiBindings.renderAppliedMaterials`
- Required-input coordination: `MeisheEditorCoordinator`
