# Official Doxygen Documentation Index

Use this routing file before loading the larger official documentation references.
The references listed here are bundled with the skill and do not require the original `doxygen` directory at use time.

Priority rule: demo-derived references define version-proven Android SDK 3.16.1.25 call order, Gradle/Manifest wiring, permissions, and app structure. Official docs define API behavior, constraints, and parameter meaning where they do not contradict demo evidence.

## Routing

### `official-core.md`

Read when: Use for SDK architecture, initialization rules, supported formats, license/package setup, file info, coordinates, 4K support, engine changes, and general Android integration constraints.

| Source | Purpose | Primary title |
| --- | --- | --- |
| `md_ch/Mainpage.md` | Documentation landing page and module overview. | 美摄SDK |
| `md_ch/Introduction.md` | Product capabilities, package types, formats, and platform notes. | 产品概述 |
| `md_ch/Overview.md` | SDK architecture overview and core object model. | 基础结构与概念 |
| `md_ch/PortingGuide.md` | Android project import and migration notes. | 开发指南 |
| `md_ch/licenseFile.md` | License file placement and behavior. | 许可文件 |
| `md_ch/support4kVideoEdit.md` | 4K editing support constraints. | 4k视频编辑 |
| `md_ch/Coordinate.md` | Coordinate-system conventions. | 时间线与视图坐标(TimeLine and View Coordinate) |
| `md_ch/avFileInfo.md` | Audio/video file information APIs. | 音视频文件信息 |
| `md_ch/assetsPackageInstall.md` | Streaming SDK asset package install flow. | 素材包安装 |
| `md_ch/BreakpointContinuation.md` | Compile/export breakpoint continuation behavior. | 断点续导 |
| `md_ch/EngineChange.md` | Engine behavior changes relevant to app compatibility. | 引擎变化 |
| `md_en/Streaming_SDK_Guide.md` | English conceptual guide with compact Java API examples. | simple guide to Meishe streaming SDK |

### `official-editing-export.md`

Read when: Use for Android capture preview/recording, timeline creation, tracks/clips, playback/seek, music, captions, stickers, themes, transitions, trim, PIP, HDR, image ROI, albums, frame retrieval, recording modes, and compile/export behavior.

| Source | Purpose | Primary title |
| --- | --- | --- |
| `md_ch/Tutorial.md` | Detailed Android development guide; iOS conditional sections are removed. | 详细开发引导 |
| `md_ch/TrimInOut.md` | Trim-in/trim-out semantics. | 裁剪入点与出点(trimIn and trimOut) |
| `md_ch/videoFrameRetriever.md` | Frame retrieval APIs and constraints. | 视频帧图像提取 |
| `md_ch/videoRecorderMode.md` | Recording mode behavior and parameter notes. | 视频录制方式 |
| `md_ch/PIP_Android.md` | Android PIP editing workflow. | 美摄画中画技术文档 |
| `md_ch/HDR_Android_cn.md` | Android HDR editing/export workflow. | HDR |
| `md_ch/ImageROI.md` | Image ROI behavior. | 图片ROI |
| `md_ch/Photo_Album.md` | Photo album creation/editing workflow. | 美摄影集技术文档 |
| `md_ch/Pan_Scan.md` | Pan-scan parameter guidance. | 摇摄与扫描(Pan and Scan) |

### `official-effects-ar-template.md`

Read when: Use for Effect SDK integration, effect package management, beauty/AR scene, segmentation, keying, mask generation, virtual live broadcast, Mimo, template/cut-same package parsing, and template timeline generation.

| Source | Purpose | Primary title |
| --- | --- | --- |
| `md_ch/effect_Introduction.md` | Effect SDK capability overview. | 产品概述 |
| `md_ch/effect_Overview.md` | Effect SDK module overview. | 基础结构与概念 |
| `md_ch/effect_PortingGuide.md` | Effect SDK Android project import notes. | 开发指南 |
| `md_ch/effect_assetsPackageInstall.md` | Effect SDK asset package install flow. | 素材包安装 |
| `md_ch/effect_EffectSdkUse.md` | Effect SDK context and renderer usage. | effectSDK使用讲解 |
| `md_ch/effect_middle_module.md` | Effect SDK middle module usage for Android. | 快速接入指南 |
| `md_ch/AR_Scene_7_243.md` | AR scene 7.2.43 Android usage. | AR Scene 技术文档 |
| `md_ch/Segment.md` | Segmentation usage. | 背景分割特效 技术文档 |
| `md_ch/Mask_Generator.md` | Mask generator usage. | Mask Generator 技术文档 |
| `md_ch/Master_Keyer.md` | Master keyer usage. | Master Keyer技术文档 |
| `md_ch/virtualLiveBroadcast.md` | Virtual live broadcast usage. | 虚拟直播 |
| `md_ch/mimo_Android.md` | Mimo Android package and API usage. | 美摄Mimo技术文档 |
| `md_ch/Template_Android.md` | Android template package usage. | 模板使用技术文档 |
| `md_ch/TemplateGenerate_Android.md` | Android template generation workflow. | 模板生成技术文档 |

### `official-fx-and-errors.md`

Read when: Use for built-in effect names, effect parameter keys/types/ranges, SDK error codes, glossary terms, and official troubleshooting answers.

| Source | Purpose | Primary title |
| --- | --- | --- |
| `md_ch/FxNameList.md` | Built-in effect names and parameter tables. | 特效名称列表 |
| `md_ch/ErrorCode.md` | SDK error code meanings. | 错误标识 |
| `md_ch/QuestionList.md` | Official troubleshooting FAQ. | 疑难问题集锦 |
| `md_ch/Glossary.md` | Official terminology glossary. | 名词解释 |
| `md_ch/effect_QuestionList.md` | Effect SDK FAQ. | 疑难问题集锦 |

## Practical Lookup Order

1. Start with this file and choose the smallest official reference that covers the requested API area.
2. Use `official-core.md` for initialization, license, formats, package import, coordinates, file metadata, and compatibility constraints.
3. Use `official-editing-export.md` for capture, recording, timeline editing, preview, captions, stickers, audio, transitions, and compile/export.
4. Use `official-effects-ar-template.md` for Effect SDK, AR scene, segmentation, keying, virtual live, Mimo, and template/cut-same flows.
5. Use `official-fx-and-errors.md` for built-in effect parameter names/ranges, error codes, glossary terms, and FAQ.
6. After official behavior is clear, use `capability-map.md`, `api-usage-index.md`, and demo-derived references to map the request into concrete Android classes and implementation snippets. If the official flow differs from bundled demo evidence, use the demo flow for generated Android code.
