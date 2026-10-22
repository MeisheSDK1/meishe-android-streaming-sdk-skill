# App Blueprints

Use this reference when the user asks for a complete app, from-0-to-1 demo, or product-level capability selection. The machine-readable source is `sdk-module-registry.json`; this file explains the intended app shapes.

## Blueprint Catalog

| Blueprint | Default modules | User-facing app shape | Bundled product shell | Resource baseline |
| --- | --- | --- | --- | --- |
| `short-video-editor` | `app-runtime`, `media-import`, `editor-shell`, `clip-editor`, `filter-editor`, `caption-editor`, `sticker-editor`, `asset-center-service`, `export-compile` | Feature hub -> media selection -> ratio -> timeline editor with `NvsLiveWindow` -> child tools -> export. | Yes: thin Activity, ownership-aware Timeline session, version-3 atomic project state with stable ids and extension codecs, bounded undo/redo, media import, split/move/delete, filters, captions, stickers, transitions, music, voiceover, material result binding, playback/seek, and export. | `R0`, `R1`, `R3`, `R4`, plus child rows. |
| `beauty-camera` | `app-runtime`, `capture-camera`, `beauty-camera`, `capture-filter`, `asset-package-service` | Camera preview/recording with beauty/filter/AR hooks. | Yes: live camera, beauty parameters, packaged filter, material result binding, camera switch, and recording. When additional capture modules are resolved, their controls and SDK paths must follow `beauty-camera-product-contract.md`. | `R0`, `R2`, `R4`, `R8`. |
| `camera-plus-editor` | `beauty-camera` + `short-video-editor` bridge modules | Record media, then optionally enter the editor timeline and export. | Yes: lightweight camera/editor launcher shell with SDK readiness and staged controller hooks. | `R0`, `R1`, `R2`, `R3`, `R4`, `R8`. |
| `asset-center-demo` | `app-runtime`, `asset-package-service`, `asset-center-service` | Browse authorized external offline examples and install/register them. The standalone screen applies an installed filter to a real sample Timeline/LiveWindow, with intensity editing and removal; picker mode returns any selected material to its editor/camera owner. | Yes: aspect-matched sample preview, filter install/apply/edit/remove loop, local family filtering, package install/upgrade, font registration, and typed result contract. No service address or request layer. Material acquisition goes to Meishe business. | `R0`, `R4`. |
| `template-mimo-cutsame-app` | `app-runtime`, `asset-package-service`, `template-engine`, `template-editor`, `cutsame-template`, `mimo-template`, `asset-center-service` | Standard/CutSame: install a user-provided `.template`, query descriptors, map replacement media, generate required reverse media, and create the selected template Timeline. Mimo: extract a user-provided ZIP, parse `info.json`, install referenced child packages, then build a normal Timeline. | Yes: runnable local package picker, descriptor validation, reverse conversion callbacks, distinct standard/CutSame and Mimo execution paths, preview/export, and external local-material entry. The supplied Demo has no redistributable standard/Mimo/CutSame package. | `R0`, `R1`, `R3`, `R4`, `R10`. |
| `pip-editor` | `app-runtime`, `media-import`, `pip-editor`, `timeline-preview`, `export-compile` | Select two media items, build picture-in-picture timeline, preview, export. Add `asset-center-service` when the bundled PIP/effect sample gallery is requested. | Yes: PIP media-pair launcher shell with preview/export controller hooks. | `R0`, `R1`, `R3`, `R4`, `R11`. |
| `quick-splicing-app` | `app-runtime`, `quick-splicing`, `media-import` | Select media, run passthrough/convertor splice, produce output without full editor when possible. | Yes: quick-splice launcher shell with convertor/resource handoff points. | `R0`, `R1`, `R12`. |
| `full-sdk-demo` | all high-value big modules plus optional niche modules | Capability showcase for the whole SDK; should be generated as modular screens, not copied Demo source. | Yes: feature-hub shell that reports resolved modules and resource readiness. | Full resource checklist; large models/packages user-provided. |
| `incremental-integration` | selected modules only | Patch an existing Android project by adding missing SDK dependencies and module controllers, or emit API-only controllers and usage code. | Yes. `--mode incremental` stages Java controllers and `patch-manifest.json` without forcing host UI; `--apply` performs a preflighted additive merge. `--mode api-only` emits concrete selected-module calls without an app shell. | Depends on selected modules. |

## Blueprint Rules

1. Start with the user's product goal and select one blueprint.
2. Expand blueprint modules through `compose_modules.py`.
3. Add user-selected small modules, then resolve predecessors.
4. Use existing project style for `incremental-integration`; do not force feature hub UI.
5. Treat identical incremental output as idempotent and any differing host target as a blocking conflict. Never use `--force` to overwrite host-owned source.
5. For `full-sdk-demo`, default to dry-run planning unless the user confirms the resource scope.
6. Never require external Demo/Doxygen at generation time.
7. Do not bundle large model/resource directories; expose placement hooks and resource checklist.
8. A blueprint with `app_template` owns the launcher/product-screen composition. Select at most one such blueprint per generated app and add optional capabilities through modules.
9. Treat the nine bundled product shells as runnable reference implementations, not full replicas of every official Demo screen. Expand child-tool UX from module recipes without changing the dependency contracts.
10. When embedding editor modules into a host project, declare `EDITOR_OWNED` or `HOST_OWNED` Timeline ownership. Host-owned sessions preserve existing host objects and deny structural or descriptor rebuilds unless the host contract explicitly grants them.
11. Preserve the original package filename when importing `.template` files because UUID-based names can be part of package identification. Treat `ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS` as an accepted asynchronous start and wait for the install callback before querying descriptors.
12. Never route a Mimo ZIP through `ASSET_PACKAGE_TYPE_TEMPLATE` or the SDK template `createTimeline` overloads. Mimo has its own metadata and child-package composition recipe.
13. For a `beauty-camera` shell, render every resolved capture module into reachable UI and follow `beauty-camera-product-contract.md`; module closure without picker return, typed material dispatch, device controls, recording pause/resume, or callback state is incomplete.
