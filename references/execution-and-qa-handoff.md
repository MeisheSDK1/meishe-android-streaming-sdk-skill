# Build and QA Handoff

Use this policy whenever creating a new Android project or integrating Meishe SDK into an existing project.

## Default execution boundary

1. Tell the user before implementation that Gradle execution is handed back by default.
2. Continue implementing without blocking for a reply.
3. Do not run Gradle, install an APK, drive a device, capture screenshots, or analyze screenshots unless the user explicitly requests automatic execution.
4. Recommend automatic physical-device screenshot analysis, while stating that it adds task time and token usage.
5. Let the user choose manual validation and return later with a screenshot, log, or one focused issue per follow-up task.

Use a concise notice in the user's language. For Chinese requests, use wording equivalent to:

> 默认我会完成代码并提供可直接粘贴执行的 Gradle 命令，不自动构建。推荐开启自动真机截图分析，但它会增加任务执行时间和 Token 消耗；也可以先手动验收，再按问题分任务逐步修复。若要开启，请明确回复“自动执行构建和真机截图分析”。

An initial request to create or integrate a project is not automatic-execution consent. Treat phrases such as “自动执行”, “帮我构建并安装”, “全流程跑完”, or “自动真机截图分析” as explicit consent for only the stated scope. Before running it, remind the user once that automatic execution adds elapsed time and token usage, then proceed without asking again unless a separate approval is required.

## First-turn assumptions notice

Before implementation, state the assumptions you are proceeding with, in the user's language, without blocking for a reply:

- Project type: new standalone project, or incremental integration into an existing project (including an already-open Android Studio project).
- SDK artifacts and license: user-provided; the generated project is a runnable skeleton until the authorized AAR/JAR, native `.so`, models, media, and asset packages are present.
- Sample assets: repository `temp_assets/android-sample-assets`, a user-provided `--sample-assets-dir`, or an explicitly clean shell with `--no-sample-assets`.
- UI language: matched to the request (`--ui-language zh-CN` for Chinese, `--ui-language en` otherwise).
- Execution boundary: Gradle build, device install, and screenshot QA are opt-in as described above.

State these assumptions and continue; the user may correct any that are wrong. Do not ask a blocking question unless a wrong assumption would make the delivered code unusable (for example, an existing host project is detected and `--mode incremental` is required).

## Copy-paste Gradle handoff

Always provide one complete command block after implementation. Fill the real absolute project path, Gradle module, and build variant. Do not leave placeholders such as `<project-path>`, `<module>`, or `<variant>` in the delivered block.

For Windows, provide one PowerShell block equivalent to the generator output:

```powershell
$projectPath = 'D:\absolute\project\path'
Set-Location -LiteralPath $projectPath
& '.\gradlew.bat' ':app:assembleDebug' '--console=plain' '--warning-mode' 'summary'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Get-ChildItem -LiteralPath (Join-Path $projectPath 'app\build\outputs\apk') -Recurse -Filter '*.apk' | Select-Object -ExpandProperty FullName
```

For macOS or Linux, provide one shell block equivalent to:

```bash
project_path='/absolute/project/path'
cd "$project_path"
./gradlew ':app:assembleDebug' --console=plain --warning-mode summary
find "$project_path/app/build/outputs/apk" -type f -name '*.apk' -print
```

The examples document shape only. The final handoff must contain real values. `create_android_project.py` prints a filled command block for new projects and applied incremental integrations; relay that block rather than reconstructing it when possible.

If the user requests another build variant, emit the exact task such as `:app:assembleRelease`. If the project has no wrapper, say so and provide the exact Android Studio action or approved repository-specific Gradle command instead of inventing a wrapper path.

## Efficient automatic build mode

When the user explicitly opts in:

1. Inspect package, module, Gradle style, compile SDK, ABI, license, and SDK artifacts once before mutation.
2. Generate or stage once. Do not build the staging project and host project separately.
3. Apply the reviewed patch once, batch implementation and UI fixes, then run one final `assemble<Variant>` build.
4. Use targeted compile/check tasks only while diagnosing a failure. Avoid repeated full builds for individual text or spacing changes.
5. Keep Gradle output compact with `--console=plain --warning-mode summary`. On failure, extract the first actionable error and only request `--stacktrace` when needed.
6. Retry a full build only after a concrete fix. Do not loop on unchanged failures.

## Optional screenshot and device QA

Automatic device QA is recommended because it catches Timeline/LiveWindow ratio errors, hidden stickers, ineffective Trim controls, empty-timeline preview bugs, material apply gaps, and clipped labels. It remains optional because repeated UI dumps, screenshots, and visual analysis consume extra time and tokens.

When opted in:

1. Install the final APK once unless an earlier install is required to diagnose a blocking runtime issue.
2. Drive one deterministic smoke flow and assert concise states instead of printing full UI trees.
3. Keep only target node text/bounds and PASS/FAIL output. Save full XML/logs to a temporary file and inspect narrow excerpts only on failure.
4. Capture only key screenshots: initial editor, one representative visual effect, and the empty/error state when relevant.
5. Read the crash buffer once at the end, scoped to the app process when possible.
6. Report only the flows actually exercised; never promote build success to runtime verification.

A complete editor smoke flow should prefer these checks when the features exist:

- SDK-ready home state.
- Timeline resolution and LiveWindow ratio agree.
- Trim changes the visible duration.
- Sticker or caption is visible and listed as applied.
- Installed material has a real apply entry.
- Applied material properties can be changed and the instance can be deleted.
- Deleting the final clip clears LiveWindow; previous-step restores it.
- Crash buffer is empty.

## Retrieval, output, and cleanup budget

- Run `search_skill_index.py` first and `compose_modules.py` once for broad composition. Load only routed references and exact semantic units.
- Prefer exact `rg`, `rg -l`, or `rg --count`. Never print an entire large XML tree, asset inventory, generated directory, or broad regex match set when a count or focused match answers the question.
- Cap routine command output; write verbose build/UI evidence to a temporary file and surface only actionable excerpts.
- Report counts plus key paths instead of enumerating every generated controller or material file.
- On Windows, validate an agent-created cleanup target is inside the workspace and use the `\\?\` long-path prefix from the first recursive cleanup attempt.
