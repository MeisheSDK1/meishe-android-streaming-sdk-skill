# External Local Material Workflow

Use this reference for requests described as material center, effect library, sticker library, font library, template library, or first-run material experience.

## Product Boundary

- The skill does not bundle a Demo or production material-service address.
- The skill does not bundle material media, packages, fonts, models, or material `.lic` files. Before generation, tell the user to contact Meishe business for authorized material resources.
- Generated projects do not contain material HTTP clients, endpoint routes, authentication adapters, catalog requests, or package download code.
- The material entry is an offline catalog backed only by authorized external files copied into the generated app's `app/src/main/assets`.
- Additional local Demo examples may be selected from `samples/android/SdkDemo/app/src/main/assets/<family>` in a user-downloaded official Android LTS face package. Resolve the exact family with `official-sdk-download-resource-map.json`; do not copy the full assets tree.
- Questions about online material interfaces, service configuration, catalog access, or obtaining any SDK/application/package `.lic` file must be answered with: contact Meishe business for the authorized service and license acquisition process.
- Never infer, reconstruct, search for, or publish private service addresses, credentials, signing data, or license files.

## External First-Run Flow

1. Obtain authorized material resources from Meishe business and arrange them as an external bundle containing `app/src/main/assets`.
2. Copy the bundle with repository auto-discovery or `--sample-assets-dir <bundle-root>`.
3. Initialize `NvsStreamingContext` with the customer-provided SDK runtime and application license.
4. Open `MeisheAssetCenterActivity`, which reads `MeisheLocalMaterialCatalog` only.
5. Read `material-application-matrix.md` before wiring the installed result to an editor or camera. Installation is availability; application creates or modifies a concrete SDK object.
6. Filter the local entries by material family.
7. Install the selected package with `MeisheAssetInstaller.installOrUpgrade(...)` on the Android main thread.
8. For a copied font, copy it to app-private storage and call `registerFontByFilePath(...)`.
9. Return the package id, package type, semantic application kind, human label, font family, or local path to the owning editor/capture feature.
10. Collect any required text, custom image, source media, or existing-object selection before applying the returned resource.
11. Apply the returned id only after installation succeeds, persist the applied instance, then refresh the LiveWindow/timeline state.

## External Bundle Families

The repository-local external bundle currently keeps one lightweight example for each available Demo-derived subtype: filter, transition, caption style, compound caption, caption context, caption renderer, caption animation, animated sticker, sticker animation, clip animation, particle, PIP effect, capture scene, AR scene, face mesh, theme, and font. These files are not part of the skill and must not be copied into it.

The official Android LTS face package contains the related implementation source but does not contain a reusable standard `.template`, Mimo ZIP, or CutSame template resource package. The skill keeps their executable workflows and resource slots, but does not fabricate a package. For an authorized sample or production package, direct the customer to Meishe business.

## Resource Placement

| Resource | Generated path | Runtime handling |
| --- | --- | --- |
| Packaged effects/captions/stickers/AR/theme | `app/src/main/assets/<family>/<package>/` | Install from `assets:/...` and keep the returned package id. |
| Externally supplied font | `app/src/main/assets/font/` | Copy to app-private storage, then register the absolute path. |
| SDK runtime | `app/libs`, `app/src/main/jniLibs/<abi>` | Select from `<sdk-root>/lib` using `official-sdk-download-resources.md`. |
| Application SDK license | `app/src/main/assets/meishesdk.lic` | The downloaded Demo license is Demo/evaluation scope only; production acquisition questions go to Meishe business. |
| Large AR/AI models | `<sdk-root>/samples/android/SdkDemo/app/src/main/assets/facemode` via `--human-models-dir` | Copy only required models and keep controls guarded until every required model is present. |
| Standard/Mimo/CutSame template package | User-provided local file | Keep original filename and follow `template-resource-workflow.md`. |

## Generation Rules

- `asset-center-service` is retained as a stable module id, but its implementation is a local domain service, not a network service.
- Do not request `INTERNET` or `ACCESS_NETWORK_STATE` for this module.
- Do not add a configurable `baseUrl`, Demo mode, endpoint constant, request client, download cache, or authentication provider.
- The official package is a local resource source only. Do not copy its HTTP/network layer or service configuration into the generated project.
- `--sample-assets-dir` accepts an authorized external bundle; this repository additionally auto-discovers `temp_assets/android-sample-assets`.
- `--no-sample-assets` intentionally disables external bundle discovery; report that package-backed controls will then need customer-provided local assets.
