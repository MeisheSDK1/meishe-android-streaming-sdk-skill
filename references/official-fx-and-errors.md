# Official Builtin Fx Parameters Errors And FAQ

This reference is distilled from the SDK Doxygen Markdown and bundled inside the skill.
Prefer it for official API behavior and constraints, then use demo-derived references for implementation call order.

Read when: Use for built-in effect names, effect parameter keys/types/ranges, SDK error codes, glossary terms, and official troubleshooting answers.

Notes:
- iOS-only conditional sections are removed where the source document marks them explicitly.
- Image references are omitted because this skill keeps text/API knowledge self-contained.
- Source paths below are relative identifiers from the original documentation, not external runtime dependencies.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Source: md_ch/FxNameList.md](#source-md_chfxnamelistmd)
- [Source: md_ch/ErrorCode.md](#source-md_cherrorcodemd)
- [Source: md_ch/QuestionList.md](#source-md_chquestionlistmd)
- [Source: md_ch/Glossary.md](#source-md_chglossarymd)
- [Source: md_ch/effect_QuestionList.md](#source-md_cheffect_questionlistmd)
<!-- END GENERATED CONTENTS -->

## Source: `md_ch/FxNameList.md`

Purpose: Built-in effect names and parameter tables.

Primary title: 特效名称列表

Doc lead: - Audio Echo（回声）

### 特效名称列表

### 特效名称列表

#### 1、特效概述

##### 1.1、内建音频特效(Builtin Audio Fx)

- Audio Echo（回声）

- Male Voice（男声）

- Female Voice（女声）

- Cartoon Voice（卡通）

- Fast Cartoon Voice（快速卡通）

- Monster Voice（怪兽）

- Audio Reverb（混响）

- Audio Wahwah（电子）

##### 1.2、内建视频特效(Builtin Video Fx)

- Sage（明快）

- Maid（少女时代）

- Mace（锐利）

- Lace（蕾丝）

- Mall（时尚）

- Sap（元气）

- Sara（调皮）

- Pinky（草莓薄荷）

- Sweet（粉嫩）

- Fresh（清爽）

- Beauty

说明：美颜。

| **参 数**   | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------- | ------- | --------- | --------- | --------- | ------- |
| Reddening | FLOAT   | 1.0       | 0.0       | 0.0       | 美红      |
| Whitening | FLOAT   | 1.0       | 0.0       | 0.0       | 美白      |
| Strength  | FLOAT   | 1.0       | 0.0       | 0.0       | 磨皮      |

- Color Property

说明：颜色属性。

| **参 数**    | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ---------- | ------- | --------- | --------- | --------- | ------- |
| Brightness | FLOAT   | 10.0      | 0.0       | 1.0       | 亮度      |
| Saturation | FLOAT   | 10.0      | 0.0       | 1.0       | 饱和度     |
| Contrast   | FLOAT   | 10.0      | 0.0       | 1.0       | 对比度     |

- Transform 2D

说明：2D变换。Anchor X，Anchor Y，Trans X，Trans Y置认处于标准坐标系，如果Is Normalized Coord为true，则处于归一化坐标系。

| **参 数**             | **类 型** | **最 大 值** | **最 小 值**   | **默 认 值**     | **范围**                               | **说 明**         |
| ------------------- | ------- | --------- | ----------- | ------------- | ------------------------------------ | --------------- |
| Scale X             | FLOAT   | 1000.0    | \-1000.0    | 1.0           |                                      | 横向缩放            |
| Scale Y             | FLOAT   | 1000.0    | \-1000.0    | 1.0           |                                      | 纵向缩放            |
| Rotation            | FLOAT   | 3600000.0 | \-3600000.0 | 0.0           |                                      | Z轴旋转角度          |
| Rotation X          | FLOAT   | 3600000.0 | \-3600000.0 | 0.0           |                                      | X轴旋转角度          |
| Rotation Y          | FLOAT   | 3600000.0 | \-3600000.0 | 0.0           |                                      | Y轴旋转角度          |
| Anchor X            | FLOAT   | 100000.0  | \-100000.0  | 0.0           |                                      | 横向定位            |
| Anchor Y            | FLOAT   | 100000.0  | 100000.0    | 0.0           |                                      | 纵向定位            |
| Trans X             | FLOAT   | 100000.0  | \-100000.0  | 0.0           |                                      | 横向平移            |
| Trans Y             | FLOAT   | 100000.0  | \-100000.0  | 0.0           |                                      | 纵向平移            |
| Opacity             | FLOAT   | 1.0       | 0.0         | 1.0           |                                      | 透明度             |
| Tex Wrap Mode       | Menu    |           |             | Clamp To Edge | Clamp To Edge,Mirrored Repeat,Repeat | 纹理贴图循环模式        |
| Tex Anchor X        | FLOAT   | 100.0     | \-100.0     | 0.0           |                                      | 纹理贴图横向定位（纹理坐标系） |
| Tex Anchor Y        | FLOAT   | 100.0     | \-100.0     | 0.0           |                                      | 纹理贴图纵向定位（纹理坐标系） |
| Tex Scale X         | FLOAT   | 1000.0    | \-1000.0    | 1.0           |                                      | 纹理贴图X向缩放        |
| Tex Scale Y         | FLOAT   | 1000.0    | \-1000.0    | 1.0           |                                      | 纹理贴图Y向缩放        |
| Tex Rotation        | FLOAT   | 3600000.0 | \-3600000.0 | 0.0           |                                      | 纹理贴图顺时针旋转角度     |
| Tex Trans X         | FLOAT   | 100000.0  | \-100000.0  | 0.0           |                                      | 纹理贴图横向平移（纹理坐标系） |
| Tex Trans Y         | FLOAT   | 100000.0  | \-100000.0  | 0.0           |                                      | 纹理贴图纵向平移（纹理坐标系） |
| Multisample         | BOOL    |           |             | FALSE         |                                      | 多重采样            |
| Is Normalized Coord | BOOL    |           |             | FALSE         |                                      | 是否为归一化坐标系       |

- CC Basic

说明：颜色基本处理。

| **参 数**                     | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                                                                                                  |
| --------------------------- | ------- | --------- | --------- | --------- | -------------------------------------------------------------------------------------------------------- |
| Is Process Other Tones      | BOOL    |           |           | FALSE     | 是否处理其他色调。值为FALSE，只有全色调(Master)生效，设置其他色调如阴影色调(Shadows),中间色调(Midtones),高光色调(Highlights)无效；值为true,其他色调才会生效。 |
| Master Saturation           | FLOAT   | 10.0      | 0.0       | 1.0       | 饱和度                                                                                                      |
| Master Contrast             | FLOAT   | 10.0      | 0.0       | 1.0       | 对比度                                                                                                      |
| Master Balance Hue          | FLOAT   | 360.0     | 0.0       | 0.0       | 平衡色调                                                                                                     |
| Master Balance Strength     | FLOAT   | 10.0      | 0.0       | 0.0       | 平衡强度                                                                                                     |
| Master Gain Master          | FLOAT   | 10.0      | 0.0       | 1.0       | 全通道增益。注：全通道增益分别与R,G,B值相乘。                                                                                |
| Master Gain Red             | FLOAT   | 10.0      | 0.0       | 1.0       | 红色增益                                                                                                     |
| Master Gain Green           | FLOAT   | 10.0      | 0.0       | 1.0       | 绿色增益                                                                                                     |
| Master Gain Blue            | FLOAT   | 10.0      | 0.0       | 1.0       | 蓝色增益                                                                                                     |
| Master Offset Master        | FLOAT   | 10.0      | \-10.0    | 0.0       | 通道偏移量。注：全通道偏移量分别与R,G,B值相加。                                                                               |
| Master Offset Red           | FLOAT   | 10.0      | \-10.0    | 0.0       | Red偏移量                                                                                                   |
| Master Offset Green         | FLOAT   | 10.0      | \-10.0    | 0.0       | Green偏移量                                                                                                 |
| Master Offset Blue          | FLOAT   | 10.0      | \-10.0    | 0.0       | Blue偏移量                                                                                                  |
| Shadows Saturation          | FLOAT   | 10.0      | 0.0       | 1.0       | 饱和度                                                                                                      |
| Shadows Contrast            | FLOAT   | 10.0      | 0.0       | 1.0       | 对比度                                                                                                      |
| Shadows Balance Hue         | FLOAT   | 360.0     | 0.0       | 0.0       | 平衡色调                                                                                                     |
| Shadows Balance Strength    | FLOAT   | 10.0      | 0.0       | 0.0       | 平衡强度                                                                                                     |
| Shadows Gain Master         | FLOAT   | 10.0      | 0.0       | 1.0       | 全通道增益。注：全通道增益分别与R,G,B值相乘。                                                                                |
| Shadows Gain Red            | FLOAT   | 10.0      | 0.0       | 1.0       | Red增益                                                                                                    |
| Shadows Gain Green          | FLOAT   | 10.0      | 0.0       | 1.0       | Green增益                                                                                                  |
| Shadows Gain Blue           | FLOAT   | 10.0      | 0.0       | 1.0       | Blue增益                                                                                                   |
| Shadows Offset Master       | FLOAT   | 10.0      | \-10.0    | 0.0       | 全通道偏移量。注：全通道偏移量分别与R,G,B值相加                                                                               |
| Shadows Offset Red          | FLOAT   | 10.0      | \-10.0    | 0.0       | Red偏移量                                                                                                   |
| Shadows Offset Green        | FLOAT   | 10.0      | \-10.0    | 0.0       | Green偏移量                                                                                                 |
| Shadows Offset Blue         | FLOAT   | 10.0      | \-10.0    | 0.0       | Blue偏移量                                                                                                  |
| Midtones Saturation         | FLOAT   | 10.0      | 0.0       | 1.0       | 饱和度                                                                                                      |
| Midtones Contrast           | FLOAT   | 10.0      | 0.0       | 1.0       | 对比度                                                                                                      |
| Midtones Balance Hue        | FLOAT   | 360.0     | 0.0       | 0.0       | 平衡色调                                                                                                     |
| Midtones Balance Strength   | FLOAT   | 10.0      | 0.0       | 0.0       | 平衡强度                                                                                                     |
| Midtones Gain Master        | FLOAT   | 10.0      | 0.0       | 1.0       | 全通道增益。注：全通道增益分别与R,G,B值相乘。                                                                                |
| Midtones Gain Red           | FLOAT   | 10.0      | 0.0       | 1.0       | Red增益                                                                                                    |
| Midtones Gain Green         | FLOAT   | 10.0      | 0.0       | 1.0       | Green增益                                                                                                  |
| Midtones Gain Blue          | FLOAT   | 10.0      | 0.0       | 1.0       | Blue增益                                                                                                   |
| Midtones Offset Master      | FLOAT   | 10.0      | \-10.0    | 0.0       | 全通道偏移量。注：全通道偏移量分别与R,G,B值相加。                                                                              |
| Midtones Offset Red         | FLOAT   | 10.0      | \-10.0    | 0.0       | Red偏移量。                                                                                                  |
| Midtones Offset Green       | FLOAT   | 10.0      | \-10.0    | 0.0       | Green偏移量                                                                                                 |
| Midtones Offset Blue        | FLOAT   | 10.0      | \-10.0    | 0.0       | Blue偏移量                                                                                                  |
| Highlights Saturation       | FLOAT   | 10.0      | 0.0       | 1.0       | 饱和度                                                                                                      |
| Highlights Contrast         | FLOAT   | 10.0      | 0.0       | 1.0       | 对比度                                                                                                      |
| Highlights Balance Hue      | FLOAT   | 360.0     | 0.0       | 0.0       | 平衡色调                                                                                                     |
| Highlights Balance Strength | FLOAT   | 10.0      | 0.0       | 0.0       | 平衡强度                                                                                                     |
| Highlights Gain Master      | FLOAT   | 10.0      | 0.0       | 1.0       | 全通道增益。注：全通道增益分别与R,G,B值相乘。                                                                                |
| Highlights Gain Red         | FLOAT   | 10.0      | 0.0       | 1.0       | Red增益。                                                                                                   |
| Highlights Gain Green       | FLOAT   | 10.0      | 0.0       | 1.0       | Green增益                                                                                                  |
| Highlights Gain Blue        | FLOAT   | 10.0      | 0.0       | 1.0       | Blue增益                                                                                                   |
| Highlights Offset Master    | FLOAT   | 10.0      | \-10.0    | 0.0       | 全通道偏移量。注：全通道偏移量分别与R,G,B值相加                                                                               |
| Highlights Offset Red       | FLOAT   | 10.0      | \-10.0    | 0.0       | Red偏移量                                                                                                   |
| Highlights Offset Green     | FLOAT   | 10.0      | \-10.0    | 0.0       | Green偏移量                                                                                                 |
| Highlights Offset Blue      | FLOAT   | 10.0      | \-10.0    | 0.0       | Blue偏移量                                                                                                  |

- Lut

说明：Lut滤镜。

| **参 数**        | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                   |
| -------------- | ------- | --------- | --------- | --------- | ------------------------- |
| Data File Path | STRING  |           |           |           | lut文件路径。传入.mslut格式文件或者png |
| Intensity      | FLOAT   | 4.0       | 0.0       | 1.0       | 强度                        |

- BasicImageAdjust

说明：图像调节。

| **参 数**    | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                |
| ---------- | ------- | --------- | --------- | --------- | ---------------------- |
| Exposure   | FLOAT   | 1.0       | \-1.0     | 0.0       | 曝光                     |
| Highlight  | FLOAT   | 1.0       | \-1.0     | 0.0       | 高光                     |
| Shadow     | FLOAT   | 1.0       | \-1.0     | 0.0       | 阴影                     |
| Brightness | FLOAT   | 1.0       | \-1.0     | 0.0       | 亮度                     |
| Contrast   | FLOAT   | 1.0       | \-1.0     | 0.0       | 对比度                    |
| Blackpoint | FLOAT   | 1.0       | \-1.0     | 0.0       | 黑点                     |
| Saturation | FLOAT   | 1.0       | \-1.0     | 0.0       | 饱和度                    |
| Vibrance   | FLOAT   | 1.0       | \-1.0     | 0.0       | 自然饱和度                  |
| Video Mode | BOOL    |           |           | FALSE     | 开启视频模式，该模式下会保证效果的帧间连续性 |

- Tint

说明：色温，色调。

| **参 数**     | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ----------- | ------- | --------- | --------- | --------- | ------- |
| Temperature | FLOAT   | 1.0       | \-1.0     | 0.0       | 色温      |
| Tint        | FLOAT   | 1.0       | \-1.0     | 0.0       | 色调      |

- Denoise

说明：去噪。

| **参 数**   | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------- | ------- | --------- | --------- | --------- | ------- |
| Intensity | FLOAT   | 1.0       | 0.0       | 0.8       | 强度      |

- Sharpen

说明：锐化。

| **参 数** | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------- | ------- | --------- | --------- | --------- | ------- |
| Radius  | FLOAT   | 10.0      | 0.0       | 5.1       | 半径      |
| Amount  | FLOAT   | 5.0       | 0.0       | 1.0       | 锐化量     |

- Vignette

说明：暗角。

| **参 数**   | **类 型** | **最 大 值** | **最 小 值** | **默 认 值**       | **说 明** |
| --------- | ------- | --------- | --------- | --------------- | ------- |
| Degree    | FLOAT   | 1.0       | 0.0       | 0.0             | 程度      |
| Color     | COLOR   |           |           | 0.0 0.0 0.0 1.0 | 颜色      |
| Min Alpha | FLOAT   | 1.0       | 0.0       | 0.0             | 最小透明度   |
| Max Alpha | FLOAT   | 1.0       | 0.0       | 1.0             | 最大透明度   |

- Definition

说明：清晰度。

| **参 数**         | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------------- | ------- | --------- | --------- | --------- | ------- |
| Intensity       | FLOAT   | 1.0       | 0.0       | 0.5       | 强度      |
| Highlight Boost | FLOAT   | 1.0       | 0.0       | 0.5       | 高光增益    |

- AR Scene /*! \anchor AR_SCENE */

说明：AR Scene。支持的功能有道具，美颜，美型和美妆。仅带有人体检测功能的SDK支持，程序初始化阶段需要加载相应检测模型。

| **参 数**                                                             | **类 型** | **最 大 值** | **最 小 值** | **默 认 值**              | **说 明**                                                                                           |
| ------------------------------------------------------------------- | ------- | --------- | --------- | ---------------------- | ------------------------------------------------------------------------------------------------- |
| Scene Id                                                            | STRING  |           |           |                        | 道具包ID                                                                                             |
| Description File                                                    | STRING  |           |           |                        | 道具包描述文件路径                                                                                         |
| Single Buffer Mode \anchor AR_SCENE_SINGLE_BUFFER_PARAMS            | BOOL    |           |           | ANDROID为TRUE,iOS为FALSE | 单buffer模式，检测与渲染是否使用同一buffer；单buffer模式会丢弃AR Scene之前特效渲染结果；双buffer时如果两个buffer不一致（Android）会导致画面效果有延时 |
| Face Camera Fovy                                                    | FLOAT   | 179       | 1         | 45                     | 摄像机张角                                                                                             |
| Beauty Effect \anchor AR_SCENE_BEAUTY_PARAMS                        | BOOL    |           |           | FALSE                  | 美颜开启（美颜）                                                                                          |
| Beauty Strength                                                     | FLOAT   | 1         | 0         | 0.5                    | 磨皮强度（美颜）                                                                                          |
| Default Beauty Enabled                                              | BOOL    |           |           | TRUE                   | 默认美颜Lut开启（美颜）                                                                                     |
| Default Intensity                                                   | FLOAT   | 1         | 0         | 1                      | 默认美颜Lut强度（美颜）                                                                                     |
| Default Beauty Lut File                                             | STRING  |           |           |                        | 默认美颜Lut文件路径（美颜）                                                                                   |
| Beauty Whitening                                                    | FLOAT   | 1         | 0         | 0.5                    | 美白强度（美颜）                                                                                          |
| Whitening Lut Enabled                                               | BOOL    |           |           | FALSE                  | 美白Lut开启（美颜）                                                                                       |
| Whitening Lut File                                                  | STRING  |           |           |                        | 美白Lut文件路径（美颜）                                                                                     |
| Beauty Reddening                                                    | FLOAT   | 1         | 0         | 0.5                    | 红润强度（美颜）                                                                                          |
| Reddening Lut File                                                  | STRING  |           |           |                        | 红润Lut文件路径（美颜）                                                                                     |
| Default Sharpen Enabled                                             | BOOL    |           |           | FALSE                  | 默认锐化已启用                                                                                           |
| Beauty Fast Mode Enabled                                            | BOOL    |           |           | FALSE                  | 美颜极速模式（美颜）                                                                                        |
| Lut Data File Path                                                  | STRING  |           |           |                        | Lut文件路径                                                                                           |
| Lut Intensity                                                       | FLOAT   | 4         | 0         | 1                      | Lut效果强度                                                                                           |
| Unified Max Faces \anchor ARSCENE_MAX_FACES_PARAMS                  | INT     | 8         | 1         | 5                      | 最多检测人脸数                                                                                           |
| Max Faces Respect Min  \anchor ARSCENE_MAX_FACES_RESPECT_MIN_PARAMS | BOOL    |           |           | FALSE                  | 多个资源包都有最多人脸数限制时，是否采用最少的那个                                                                         |
| AI Face Occlusion Enabled 									      | BOOL    |           |           | FALSE                  | 是否开启AI人脸遮挡检测，当前只对美妆有效                                                                         |
| Advanced Beauty Enable \anchor AR_SCENE_ADVANCED_BEAUTY_PARAMS      | BOOL    |           |           | FALSE                  | 高级美颜开启                                                                                            |
| Advanced Beauty Intensity                                           | FLOAT   | 1         | 0         | 1                      | 高级美颜磨皮强度                                                                                          |
| Advanced Beauty Type                                                | INT     | 2         | 0         | 0                      | 高级美颜类型：0是Android端标准效果，1是iOS端标准效果，2是男性效果                                                           |
| Advanced Beauty Remove Dark Circles Intensity                       | FLOAT   | 1         | 0         | 0                      | 高级美颜祛黑眼圈强度                                                                                        |
| Advanced Beauty Remove Nasolabial Folds Intensity                   | FLOAT   | 1         | 0         | 0                      | 高级美颜祛法令纹强度                                                                                        |
| Advanced Beauty Brighten Eyes Intensity                             | FLOAT   | 1         | 0         | 0                      | 高级美颜亮眼强度                                                                                          |
| Advanced Beauty Brighten Eyes Lut File                              | STRING  |           |           |                        | 高级美颜亮眼Lut文件路径（已废弃）                                                                                    |
| Advanced Beauty Whiten Teeth Intensity                              | FLOAT   | 1         | 0         | 0                      | 高级美颜白牙强度                                                                                          |
| Advanced Beauty Whiten Teeth Lut File                               | STRING  |           |           |                        | 高级美颜白牙Lut文件路径                                                                                     |
| Advanced Beauty Face Lut Intensity                                  | FLOAT   | 1         | 0         | 0                      | 高级美颜脸部Lut强度                                                                                       |
| Advanced Beauty Face Lut File                                       | STRING  |           |           |                        | 高级美颜脸部Lut文件路径                                                                                     |
| Advanced Beauty Clear Intensity                                     | FLOAT   | 1         | 0         | 0                      | 高级美颜清晰强度                                                                                          |
| Advanced Beauty Matte Intensity                                     | FLOAT   | 1         | 0         | 0                      | 高级美颜哑光（去油光）强度                                                                                     |
| Advanced Beauty Matte Fill Radius                                   | FLOAT   | 30        | 3         | 15                     | 高级美颜哑光（去油光）填充半径                                                                                   |
| Advanced Beauty Smooth Consumption Level                            | INT     | 2         | 0         | 0                      | 高级美颜磨皮功耗等级0最高，2最低. ('Advanced Beauty Smooth Disable Auto Consumption Level'为true时生效)              |
| Advanced Beauty Smooth Disable Auto Consumption Level               | BOOL    |           |           | FALSE                  | 高级美颜禁用自动磨皮等级                                                                                      |
| Beauty Shape \anchor AR_SCENE_FACE_WARP_PARAMS                      | BOOL    |           |           | FALSE                  | Warp美型开启                                                                                      |
| Head Size Warp Degree                                               | FLOAT   | 1         | -1        | 0                      | 头部增大程度                                                                                              |
| Head Size Warp Strategy                                             | INT     | 0x7FFFFFFF| 0         | 0                      | 头部增大策略(如果需要使用外置头部增大资源包，此项需设置成0x7FFFFFFF)                                                        |
| Head Size Warp Custom Package Id                              	  | STRING  |           |           |                        | 头部增大自定义资源包 ID                                                                                         |
| Face Mesh Internal Enabled \anchor AR_SCENE_FACE_MESH_PARAMS        | BOOL    |           |           | FALSE                  | Face Mesh美型开启                                                                                              |
| Face Mesh Eye Size Degree                                           | FLOAT   | 1         | -1        | 0                      | 大眼程度                                                                                              |
| Face Mesh Eye Corner Stretch Degree                                 | FLOAT   | 1         | -1        | 0                      | 眼角拉向外伸程度                                                                                          |
| Face Mesh Face Size Degree                                          | FLOAT   | 1         | -1        | 0                      | 瘦脸程度                                                                                              |
| Face Mesh Face Width Degree                                         | FLOAT   | 1         | -1        | 0                      | 窄脸程度                                                                                              |
| Face Mesh Face Length Degree                                        | FLOAT   | 1         | -1        | 0                      | 小脸（短脸）程度                                                                                          |
| Face Mesh Forehead Height Degree                                    | FLOAT   | 1         | -1        | 0                      | 额头高度                                                                                              |
| Face Mesh Malar Width Degree                                        | FLOAT   | 1         | -1        | 0                      | 颧骨变窄程度                                                                                            |
| Face Mesh Jaw Width Degree                                          | FLOAT   | 1         | -1        | 0                      | 下颌变窄程度                                                                                            |
| Face Mesh Chin Length Degree                                        | FLOAT   | 1         | -1        | 0                      | 下巴缩短程度                                                                                            |
| Face Mesh Eye Distance Degree                                       | FLOAT   | 1         | -1        | 0                      | 眼间距变窄程度                                                                                           |
| Face Mesh Nose Length Degree                                        | FLOAT   | 1         | -1        | 0                      | 鼻子拉长程度                                                                                            |
| Face Mesh Nose Width Degree                                         | FLOAT   | 1         | -1        | 0                      | 鼻子变窄程度                                                                                            |
| Face Mesh Mouth Size Degree                                         | FLOAT   | 1         | -1        | 0                      | 嘴部缩小程度                                                                                            |
| Face Mesh Mouth Corner Lift Degree                                  | FLOAT   | 1         | -1        | 0                      | 嘴角上拉程度                                                                                            |
| Face Mesh Temple Width Degree                                       | FLOAT   | 1         | -1        | 0                      | 太阳穴增宽程度                                                                                           |
| Face Mesh Head Size Degree                                          | FLOAT   | 1         | -1        | 0                      | 头部缩小程度                                                                                            |
| Face Mesh Eye Angle Degree                                          | FLOAT   | 1         | -1        | 0                      | 眼睛角度旋转程度（外眼角向上，内眼角向下）                                                                             |
| Face Mesh Nose Bridge Width Degree                                  | FLOAT   | 1         | -1        | 0                      | 鼻梁变窄程度                                                                                            |
| Face Mesh Philtrum Length Degree                                    | FLOAT   | 1         | -1        | 0                      | 人中缩短程度                                                                                            |
| Face Mesh Eye Arc Degree                                            | FLOAT   | 1         | -1        | 0                      | 眼睛弧形程度（眼角向上）                                                                                      |
| Face Mesh Eye Width Degree                                          | FLOAT   | 1         | -1        | 0                      | 眼睛宽度变大程度                                                                                          |
| Face Mesh Eye Height Degree                                         | FLOAT   | 1         | -1        | 0                      | 眼睛高度变大程度                                                                                          |
| Face Mesh Eye Y Offset Degree                                       | FLOAT   | 1         | -1        | 0                      | 眼睛向上偏移程度                                                                                          |
| Face Mesh Eyebrow Angle Degree                                      | FLOAT   | 1         | -1        | 0                      | 眉毛角度旋转程度（外眼角向上，内眼角向下）                                                                             |
| Face Mesh Eyebrow Thickness Degree                                  | FLOAT   | 1         | -1        | 0                      | 眉毛变粗程度                                                                                            |
| Face Mesh Eyebrow X Offset Degree                                   | FLOAT   | 1         | -1        | 0                      | 眉毛间距变宽程度                                                                                          |
| Face Mesh Eyebrow Y Offset Degree                                   | FLOAT   | 1         | -1        | 0                      | 眉毛向上偏移程度                                                                                          |
| Face Mesh Nose Head Width Degree                                    | FLOAT   | 1         | -1        | 0                      | 鼻头变窄程度                                                                                            |
| Face Mesh Eye Size Custom Package Id                                | STRING  |           |           |                        | 大眼美型包ID                                                                                           |
| Face Mesh Eye Corner Stretch Custom Package Id                      | STRING  |           |           |                        | 眼角拉向外伸美型包ID                                                                                       |
| Face Mesh Face Size Custom Package Id                               | STRING  |           |           |                        | 瘦脸美型包ID                                                                                           |
| Face Mesh Face Width Custom Package Id                              | STRING  |           |           |                        | 窄脸美型包ID                                                                                           |
| Face Mesh Face Length Custom Package Id                             | STRING  |           |           |                        | 小脸（短脸）美型包ID                                                                                       |
| Face Mesh Forehead Height Custom Package Id                         | STRING  |           |           |                        | 额头高度美型包ID                                                                                         |
| Face Mesh Malar Width Custom Package Id                             | STRING  |           |           |                        | 颧骨变窄美型包ID                                                                                         |
| Face Mesh Jaw Width Custom Package Id                               | STRING  |           |           |                        | 下颌变窄美型包ID                                                                                         |
| Face Mesh Chin Length Custom Package Id                             | STRING  |           |           |                        | 下巴缩短美型包ID                                                                                         |
| Face Mesh Eye Distance Custom Package Id                            | STRING  |           |           |                        | 眼间距变窄美型包ID                                                                                        |
| Face Mesh Nose Length Custom Package Id                             | STRING  |           |           |                        | 鼻子拉长美型包ID                                                                                         |
| Face Mesh Nose Width Custom Package Id                              | STRING  |           |           |                        | 鼻子变窄美型包ID                                                                                         |
| Face Mesh Mouth Size Custom Package Id                              | STRING  |           |           |                        | 嘴部缩小美型包ID                                                                                         |
| Face Mesh Mouth Corner Lift Custom Package Id                       | STRING  |           |           |                        | 嘴角上拉美型包ID                                                                                         |
| Face Mesh Temple Width Custom Package Id                            | STRING  |           |           |                        | 太阳穴增宽美型包ID                                                                                        |
| Face Mesh Head Size Custom Package Id                               | STRING  |           |           |                        | 头部缩小美型包ID                                                                                         |
| Face Mesh Eye Angle Custom Package Id                               | STRING  |           |           |                        | 眼睛角度旋转美型包ID                                                                                       |
| Face Mesh Nose Bridge Width Custom Package Id                       | STRING  |           |           |                        | 鼻梁变窄美型包ID                                                                                         |
| Face Mesh Philtrum Length Custom Package Id                         | STRING  |           |           |                        | 人中缩短美型包ID                                                                                         |
| Face Mesh Eye Arc Custom Package Id                                 | STRING  |           |           |                        | 眼睛弧形美型包ID                                                                                         |
| Face Mesh Eye Width Custom Package Id                               | STRING  |           |           |                        | 眼睛宽度变大美型包ID                                                                                       |
| Face Mesh Eye Height Custom Package Id                              | STRING  |           |           |                        | 眼睛高度变高美型包ID                                                                                       |
| Face Mesh Eye Y Offset Custom Package Id                            | STRING  |           |           |                        | 眼睛向上偏移美型包ID                                                                                       |
| Face Mesh Eyebrow Angle Custom Package Id                           | STRING  |           |           |                        | 眉毛角度旋转美型包ID                                                                                       |
| Face Mesh Eyebrow Thickness Custom Package Id                       | STRING  |           |           |                        | 眉毛变粗美型包ID                                                                                         |
| Face Mesh Eyebrow X Offset Custom Package Id                        | STRING  |           |           |                        | 眉毛间距变宽美型包ID                                                                                       |
| Face Mesh Eyebrow Y Offset Custom Package Id                        | STRING  |           |           |                        | 毛向上偏移美型包ID                                                                                        |
| Face Mesh Nose Head Width Custom Package Id                         | STRING  |           |           |                        | 鼻头变窄美型包ID                                                                                         |
| Makeup Enabled                                                      | BOOL    |           |           | TRUE                   | 美妆开启                                                                                              |
| Makeup Intensity                                                    | FLOAT   | 1         | 0         | 1                      | 美妆强度                                                                                              |
| Makeup Lip Package Id                                               | STRING  |           |           |                        | 美妆口红包ID                                                                                           |
| Makeup Eyebrow Package Id                                           | STRING  |           |           |                        | 美妆眉毛包ID                                                                                           |
| Makeup Eyeshadow Package Id                                         | STRING  |           |           |                        | 美妆眼影包ID                                                                                           |
| Makeup Eyelash Package Id                                           | STRING  |           |           |                        | 美妆睫毛包ID                                                                                           |
| Makeup Eyeliner Package Id                                          | STRING  |           |           |                        | 美妆眼线包ID                                                                                           |
| Makeup Blusher Package Id                                           | STRING  |           |           |                        | 美妆腮红包ID                                                                                           |
| Makeup Shadow Package Id                                            | STRING  |           |           |                        | 美妆阴影包ID                                                                                           |
| Makeup Brighten Package Id                                          | STRING  |           |           |                        | 美妆提亮包ID                                                                                           |
| Makeup Eyeball Package Id                                           | STRING  |           |           |                        | 美妆眼球包ID                                                                                           |
| Makeup Lip Color                                                    | COLOR   |           |           | 0, 0, 0, 0             | 美妆口红颜色                                                                                            |
| Makeup Eyebrow Color                                                | COLOR   |           |           | 0, 0, 0, 0             | 美妆眉毛颜色                                                                                            |
| Makeup Eyeshadow Color                                              | COLOR   |           |           | 0, 0, 0, 0             | 美妆眼影颜色                                                                                            |
| Makeup Eyelash Color                                                | COLOR   |           |           | 0, 0, 0, 0             | 美妆睫毛颜色                                                                                            |
| Makeup Eyeliner Color                                               | COLOR   |           |           | 0, 0, 0, 0             | 美妆眼线颜色                                                                                            |
| Makeup Blusher Color                                                | COLOR   |           |           | 0, 0, 0, 0             | 美妆腮红颜色                                                                                            |
| Makeup Shadow Color                                                 | COLOR   |           |           | 0, 0, 0, 0             | 美妆阴影颜色                                                                                            |
| Makeup Brighten Color                                               | COLOR   |           |           | 0, 0, 0, 0             | 美妆提亮颜色                                                                                            |
| Makeup Eyeball Color                                                | COLOR   |           |           | 0, 0, 0, 0             | 美妆眼球颜色                                                                                            |
| Makeup Lip Intensity                                                | FLOAT   | 1         | 0         | 1                      | 美妆口红强度                                                                                            |
| Makeup Eyebrow Intensity                                            | FLOAT   | 1         | 0         | 1                      | 美妆眉毛强度                                                                                            |
| Makeup Eyeshadow Intensity                                          | FLOAT   | 1         | 0         | 1                      | 美妆眼影强度                                                                                            |
| Makeup Eyelash Intensity                                            | FLOAT   | 1         | 0         | 1                      | 美妆睫毛强度                                                                                            |
| Makeup Eyeliner Intensity                                           | FLOAT   | 1         | 0         | 1                      | 美妆眼线强度                                                                                            |
| Makeup Blusher Intensity                                            | FLOAT   | 1         | 0         | 1                      | 美妆腮红强度                                                                                            |
| Makeup Shadow Intensity                                             | FLOAT   | 1         | 0         | 1                      | 美妆阴影强度                                                                                            |
| Makeup Brighten Intensity                                           | FLOAT   | 1         | 0         | 1                      | 美妆提亮强度                                                                                            |
| Makeup Eyeball Intensity                                            | FLOAT   | 1         | 0         | 1                      | 美妆眼球强度                                                                                            |

- Mask Generator

说明：蒙版特效。如果Text Mask Description String不为空，则使用该字符串生成蒙版，同时忽略除“Is Caption”外的其他参数。Feather Width默认会随蒙版尺寸变化，如果Fixed Feather Width为TRUE，则Feather Width会固定下来。

| **参 数**                      | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                                                                                                                                                |
| ---------------------------- | ------- | --------- | --------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Region Info                  | ARBDATA |           |           |           | 区域信息，具体坐标系由Coordinate System指定，参见 [NvsMaskRegionInfo](`com.meicam.sdk.NvsMaskRegionInfo`)。  (@ref NvsMaskRegionInfo)。 |
| Feather Width                | FLOAT   | 1000.0    | 0.0       | 0.0       | 羽化宽度程度，不属于任何坐标系                                                                                                                                        |
| Fixed Feather Width          | BOOL    |           |           | FALSE     | 固定羽化半径                                                                                                                                                 |
| Feather Compensation         | BOOL    |           |           | TRUE      | 抗锯齿                                                                                                                                                    |
| Keep RGB                     | BOOL    |           |           | FALSE     | 在输入图像上应用蒙版，否则只输出蒙版                                                                                                                                     |
| Inverse Region               | BOOL    |           |           | FALSE     | 区域反转                                                                                                                                                   |
| Coordinate System            | STRING  |           |           | NDC       | 坐标系类型：Timeline, NDC                                                                                                                                    |
| Text Mask Description String | STRING  |           |           |           | 蒙版的storyboard描述字符串,                                                                                                                                    |
| Is Caption                   | BOOL    |           |           | FALSE     | 蒙版描述字符串是否为文字效果                                                                                                                                         |

- Gaussian Blur

说明：高斯模糊。

| **参 数** | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**     |
| ------- | ------- | --------- | --------- | --------- | ----------- |
| Radius  | FLOAT   | 64.0      | 0.0       | 64.0      | 模糊半径（标准坐标系） |

- Dir Blur

说明：方向模糊。

| **参 数** | **类 型** | **最 大 值** | **最 小 值**    | **默 认 值** | **说 明**        |
| ------- | ------- | --------- | ------------ | --------- | -------------- |
| Length  | FLOAT   | 1000.0    | 0.0          | 15.0      | 模糊长度（标准坐标系）    |
| Angle   | FLOAT   | 3600000.0 | \- 3600000.0 | 0.0       | 逆时针模糊角度，0为水平模糊 |

- Zoom Blur

说明：缩放模糊。

| **参 数**  | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**            |
| -------- | ------- | --------- | --------- | --------- | ------------------ |
| Length   | FLOAT   | 1000.0    | 0.0       | 50.0      | 模糊长度（标准坐标系）        |
| Center X | FLOAT   | 1.0       | \-1.0     | 0.0       | 模糊中心点X值（标准坐标系）     |
| Center Y | FLOAT   | 1.0       | \-1.0     | 0.0       | 模糊中心点Y值（标准坐标系）     |
| Mipmap   | BOOL    |           |           | FALSE     | 启用多级模糊处理，更加平滑，但耗时多 |

- Spiral Blur

说明：螺旋模糊。

| **参 数**        | **类 型** | **最 大 值** | **最 小 值**    | **默 认 值** | **说 明**            |
| -------------- | ------- | --------- | ------------ | --------- | ------------------ |
| Center X       | FLOAT   | 1.0       | \-1.0        | 0.0       | 模糊中心点X值（归一化坐标系）    |
| Center Y       | FLOAT   | 1.0       | \-1.0        | 0.0       | 模糊中心点Y值（归一化坐标系）    |
| Radius         | FLOAT   | 10000.0   | 0.0          | 2000.0    | 模糊半径（标准坐标系）        |
| Angle          | FLOAT   | 3600000.0 | \- 3600000.0 | 0.0       | 模糊角度               |
| Rotation Angle | FLOAT   | 3600000.0 | \- 3600000.0 | 0.0       | 图像逆时针旋转角度          |
| Full Screen    | BOOL    |           |              | FALSE     | 是否全屏，全屏下参数Radius失效 |

- Shape

说明：该特技能够实现矢量图形的绘制，诸如矩形，椭圆以及path，并且能以单色或者渐变色的方式对shape进行填充。

| **参 数**      | **类 型** | **最 大 值** | **最 小 值**  | **默 认 值**       | **说 明**                           |
| ------------ | ------- | --------- | ---------- | --------------- | --------------------------------- |
| Type         | MENU    |           |            | Rectangle       | 绘制形状类型：可以为 Rectangle，Ellipse，Path |
| AnchorX      | FLOAT   | 100000.0  | -100000.0  | 0.0             | shape二维变换锚点X                      |
| AnchorY      | FLOAT   | 100000.0  | -100000.0  | 0.0             | shape二维变换锚点Y                      |
| ScaleX       | FLOAT   | 1000.0    | -1000.0    | 0.0             | 水平缩放系数                            |
| ScaleY       | FLOAT   | 1000.0    | -1000.0    | 0.0             | 垂直缩放系数                            |
| RotZ         | FLOAT   | 3600000.0 | -3600000.0 | 0.0             | 旋转角度                              |
| TransX       | FLOAT   | 100000.0  | -100000.0  | 0.0             | 水平平移                              |
| TransY       | FLOAT   | 100000.0  | -100000.0  | 0.0             | 垂直平移                              |
| CenterX      | FLOAT   | 100000.0  | -100000.0  | 0.0             | 中心点X坐标 仅在Rectangle和Ellipse有效      |
| CenterY      | FLOAT   | 100000.0  | -100000.0  | 0.0             | 中心点Y坐标，适用范围同上                     |
| Width        | FLOAT   | 100000.0  | 0.0        | 0.0             | shape宽度，同上                        |
| Height       | FLOAT   | 100000.0  | 0.0        | 0.0             | shape高度，同上                        |
| BorderRadius | FLOAT   | 100000.0  | 0.0        | 0.0             | 圆角半径，仅Rectangle                   |
| PathDesc     | STRING  |           |            |                 | 用于描述Path构成，仅Path                  |
| FillMode     | MENU    |           |            |                 | 填充模式                              |
| Color        | COLOR   |           |            | 1.0:1.0:1.0:1.0 | 填充颜色，仅在FillMode为Color生效           |
| GradientDesc | STRING  |           |            |                 | 填充渐变色，仅在FillMode为Gradient生效       |
| Antialiasing | BOOL    |           |            | TRUE            | 抗锯齿                               |

- Water Ripple

说明：水波纹。

| **参 数**      | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------------ | ------- | --------- | --------- | --------- | ------- |
| Pattern Path | STRING  |           |           |           | 样式文件路径  |

- Line Effect

说明：毛刺特技。

| **参 数**  | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                     |
| -------- | ------- | --------- | --------- | --------- | --------------------------- |
| Angle    | FLOAT   | 360.0     | 0.0       | 0.0       | 线条变化方向的角度值，取值仅限0，90，180，270 |
| Progress | FLOAT   | 1.0       | 0.0       | 0.0       | 条变化进度                       |
| Style    | STRING  |           |           | swipe     | 风格:swipe或blur               |

- Set Alpha

说明：设置输入图像或颜色的alpha通道。需要两个输入，依次为原图像与alpha图像。

| **参 数**             | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                                      |
| ------------------- | ------- | --------- | --------- | --------- | -------------------------------------------- |
| Invert Alpha        | BOOL    |           |           | FALSE     | 反转alpha图像                                    |
| Use Alpha Channel   | BOOL    |           |           | FALSE     | 输出图像的alpha通道为alpha图像的alpha通道，否则为alpha图像的R通道。 |
| Use Solid Src Color | BOOL    |           |           | FALSE     | 使用纯色作为原图像                                    |
| Src Color Red       | FLOAT   | 1.0       | 0.0       | 1.0       | 纯色的R分量（仅Use Solid Src Color为TRUE时有意义）        |
| Src Color Green     | FLOAT   | 1.0       | 0.0       | 1.0       | 纯色的G分量（仅Use Solid Src Color为TRUE时有意义）        |
| Src Color Blue      | FLOAT   | 1.0       | 0.0       | 1.0       | 纯色的B分量（仅Use Solid Src Color为TRUE时有意义）        |
| Src Color Alpha     | FLOAT   | 1.0       | 0.0       | 1.0       | 纯色的A分量（仅Use Solid Src Color为TRUE时有意义）        |

- Mosaic

说明：马赛克。

| **参 数**      | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------------ | ------- | --------- | --------- | --------- | ------- |
| Unit Size    | FLOAT   | 1.0       | 0.0       | 0.05      | 模糊单元大小  |
| Align Center | BOOL    |           |           | FALSE     | 是否居中对齐  |

- Glitter

说明：闪光。

| **参 数**      | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**  |
| ------------ | ------- | --------- | --------- | --------- | -------- |
| Quantity     | FLOAT   | 1.0       | 0.0       | 0.5       | 闪光数量     |
| Source Path  | STRING  |           |           |           | 闪光纹理文件路径 |
| Minus Thresh | FLOAT   | 1.0       | 0.0       | 0.15      | 阈值       |
| Glitter Size | FLOAT   | 1.0       | 0.0       | 0.5       | 闪光尺寸     |

- Cartoon

说明：卡通。Grayscale，Stroke Only同时为TRUE时，启用Stroke Only

| **参 数**     | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ----------- | ------- | --------- | --------- | --------- | ------- |
| Grayscale   | BOOL    |           |           | FALSE     | 只画轮廓    |
| Stroke Only | BOOL    |           |           | FALSE     | 是否是灰度圈  |
| Lut File    | STRING  |           |           |           | Lut文件路径 |

- Positioner

说明：属性特技是videoclip自带的一个特技，默认是关闭，通过enablePropertyVideoFx接口开启或者关闭属性特技。

| **参 数**                          | **类 型** | **最 大 值**  | **最 小 值**    | **默 认 值**     | **取 值 范 围**                                                         | **说 明**                                                                                                                         |
| -------------------------------- | ------- | ---------- | ------------ | ------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Fill Mode                        | Menu    |            |              | AspectFit     | "PanAndScan"：Pan&Scan模式。 "AspectFit"：fit模式。 "Stretch"：拉伸。 "Fill"：填充 | 图像的填充模式                                                                                                                         |
| Scan Value                       | FLOAT   | 1.0        | \-1.0        | 0.0           |                                                                     | 缩放（仅Pan&Scan模式有效）                                                                                                               |
| Pan Value                        | FLOAT   |            | \-1.0        | 0.0           |                                                                     | 平移（仅Pan&Scan模式有效）                                                                                                               |
| Scale X                          | FLOAT   | 1000.0     | \-1000.0     | 0             |                                                                     | X方向水平缩放                                                                                                                         |
| Scale Y                          | FLOAT   | 1000.0     | \- 1000.0    | 1.0           |                                                                     | Y方向垂直缩放                                                                                                                         |
| Rotation                         | FLOAT   | 3600000.0  | \- 3600000.0 | 0.0           |                                                                     | 旋转角度                                                                                                                            |
| Anchor X                         | FLOAT   | 100000.0   | \-100000.0   | 0.0           |                                                                     | 水平锚点                                                                                                                            |
| Anchor Y                         | FLOAT   | 100000.0   | \- 100000.0  | 0.0           |                                                                     | 垂直锚点                                                                                                                            |
| Trans X                          | FLOAT   | 100000.0   | \- 100000.0  | 0.0           |                                                                     | X方向平移                                                                                                                           |
| Trans Y                          | FLOAT   | 100000.0   | \- 100000.0  | 0.0           |                                                                     | Y方向平移                                                                                                                           |
| Enable MultiSample               | BOOL    |            |              | FALSE         |                                                                     | 是否开启重采样                                                                                                                         |
| Opacity                          | FLOAT   | 1.0        | 0.0          | 1.0           |                                                                     | 不透明度                                                                                                                            |
| Wrap Mode                        | Menu    |            |              | Clamp To Edge | "Clamp To Edge"：边缘裁剪 "Mirrored Repeat"：镜像循环 "Repeat"：循环             | 边缘模式                                                                                                                            |
| Background Mode                  | Menu    |            |              | Color Solid   | "Color Solid"：颜色 "Blur"：模糊 "Image File"：图片                          | 背景模式                                                                                                                            |
| Background Color                 | COLOR   |            |              | 0.0.0.0       |                                                                     | 设置背景颜色（仅颜色模式有效）                                                                                                                 |
| Background Image                 | STRING  |            |              |               |                                                                     | 设置背景图片路径（仅图片模式有效）                                                                                                               |
| Background Image Pan             | FLOAT   | 1.0        | \-1.0        | 0.0           |                                                                     | 设置背景图片平移（仅图片模式有效）                                                                                                               |
| Background Blur Radius           | FLOAT   | 64.0       | 0.0          | 0.0           |                                                                     | 设置背景模糊度（仅模糊模式有效）                                                                                                                |
| Enable Background Rotation       | BOOL    |            |              | FALSE         |                                                                     | 设置背景模糊图像是否跟随前景图像旋转                                                                                                              |
| Package Id                       | STRING  |            |              | 空字符串          |                                                                     | 设置滤镜资源包id（特技范围仅原始画面）                                                                                                            |
| Description File                 | STRING  |            |              |               |                                                                     | 故事版特技的描述文件路径（特技范围仅原始画面）                                                                                                         |
| Description String               | STRING  |            |              |               |                                                                     | 故事版特技的描述内容（特技范围仅原始画面）                                                                                                           |
| Is Storyboard 3D                 | BOOL    |            |              | FALSE         |                                                                     | 是否是三维故事版特技（特技范围仅原始画面）                                                                                                           |
| Post Package Id                  | STRING  |            |              |               |                                                                     | 设置滤镜资源包id（特技范围是整个timeline画幅）                                                                                                    |
| Post Description File            | STRING  |            |              |               |                                                                     | 故事版特技的描述文件路径（特技范围是整个timeline画幅）                                                                                                 |
| Post Description String          | STRING  |            |              |               |                                                                     | 故事版特技的描述内容（特技范围是整个timeline画幅）                                                                                                   |
| Is Post Storyboard 3D            | BOOL    |            |              | FALSE         |                                                                     | 是否是三维故事版特技（特技范围是整个timeline画幅）                                                                                                   |
| Package2 Id                      | STRING  |            |              |               |                                                                     | 设置第二个滤镜资源包id（特技范围仅原始画面）                                                                                                         |
| Package2 Description File        |         |            |              |               |                                                                     | 第二个故事版特技的描述文件路径（特技范围仅原始画面）                                                                                                      |
| Package2 Description String      | STRING  |            |              |               |                                                                     | 第二个故事版特技的描述内容（特技范围仅原始画面）                                                                                                        |
| Package2 Is Storyboard 3D        | BOOL    |            |              | FALSE         |                                                                     | 第二个故事版特技是否是三维故事版特技（特技范围仅原始画面）                                                                                                   |
| Post Package2 Id                 | STRING  |            |              |               |                                                                     | 设置第二个滤镜资源包id（特技范围是整个timeline画幅）                                                                                                 |
| Post Package2 Description File   | STRING  |            |              |               |                                                                     | 第二个故事版特技的描述文件路径（特技范围是整个timeline画幅）                                                                                              |
| Post Package2 Description String | STRING  |            |              |               |                                                                     | 第二个故事版特技的描述内容（特技范围是整个timeline画幅）                                                                                                |
| Package2 Is Post Storyboard 3D   | BOOL    |            |              | FALSE         |                                                                     | 第二个故事版特技是否是三维故事版特技（特技范围是整个timeline画幅）                                                                                           |
| Resource Dir                     | STRING  |            |              | 空字符串          |                                                                     | 资源文件路径                                                                                                                          |
| Package Effect In                | FLOAT   | INT32\_MAX | 0.0          | 0.0           |                                                                     | 滤镜特技的特技开始时间                                                                                                                     |
| Package Effect Out               | FLOAT   | INT32\_MAX | 0.0          | 0.0           |                                                                     | 滤镜特技的特技结束时间                                                                                                                     |
| Package2 Effect In               | FLOAT   | INT32\_MAX | 0.0          | 0.0           |                                                                     | 第二个滤镜特技的特技开始时间                                                                                                                  |
| Package2 Effect Out              | FLOAT   | INT32\_MAX | 0.0          | 0.0           |                                                                     | 第二个滤镜特技的特技结束时间                                                                                                                  |
| Mask Region Info                 | ARBDATA |            |              | null          |                                                                     | 蒙版的形状信息，参见 [NvsMaskRegionInfo](`com.meicam.sdk.NvsMaskRegionInfo`)。  (@ref NvsMaskRegionInfo)。 |
| Mask Feather Width               | FLOAT   | 1000.0     | 0.0          | 0.0           |                                                                     | 蒙版羽化宽度                                                                                                                          |
| Mask Inverse Region              | BOOL    |            |              | FALSE         |                                                                     | 蒙版区域反转                                                                                                                          |
| Mask Coordinate System           | STRING  |            |              | ndc           | “ndc”：归一化坐标系 “timeline”：timeline坐标系                                 | 蒙版坐标类型                                                                                                                          |

- Particle System

说明：粒子。

| **参 数**              | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**    |
| -------------------- | ------- | --------- | --------- | --------- | ---------- |
| Tail Fading Duration | FLOAT   | 2.0       | 0.0       | 0.0       | 粒子尾巴褪色持续时间 |
| Resource Dir         | STRING  |           |           |           | 资源文件路径     |
| Description String   | STRING  |           |           |           | 描述内容       |
| Description File     | STRING  |           |           |           | 描述文件       |

- Neat

说明：磨皮。

| **参 数**           | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ----------------- | ------- | --------- | --------- | --------- | ------- |
| Intensity         | FLOAT   | 1.0       | 0.0       | 0.8       | 强度      |
| Details Intensity | FLOAT   | 1.0       | 0.0       | 0.5       | 细节强度    |
| Blur Thresh       | FLOAT   | 1.0       | 0.0       | 0.2       | 模糊阈值    |
| Blur Radius       | FLOAT   | 1.0       | 0.0       | 0.5       | 模糊半径    |

- Segmentation

说明：人体及天空分割。仅带有人体检测功能的SDK支持，程序初始化阶段需要加载相应分割模型。

| **参 数**         | **类 型** | **最 大 值** | **最 小 值** | **默 认 值**  | **说 明**                                 |
| --------------- | ------- | --------- | --------- | ---------- | --------------------------------------- |
| Segment Type    | STRING  |           |           | Background | 分割类型，目前支持”Background”，”Half Body”，”Sky” |
| Inverse Segment | BOOL    |           |           | FALSE      | 反相                                      |
| Output Mask     | BOOL    |           |           | FALSE      | 输出蒙版或被蒙版处理后的图像                          |

- Segmentation Edge

说明：生成分割边缘。

| **参 数**           | **类 型** | **最 大 值** | **最 小 值** | **默 认 值**       | **说 明** |
| ------------------- | ------- | --------- | --------- | --------------- | ------- |
| Width               | FLOAT   | 1000.0    | 0.0       | 5.0             | 边缘宽度    |
| Color               | COLOR   |           |           | 1.0:1.0:1.0:1.0 | 边缘颜色    |
| Keep Input Color    | BOOL    |           |           | FALSE           | 是否保留原有输入图像                          |

- Line Painting

说明：标记箭头、线条的绘制。

| **参 数**        | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                                     |
| -------------- | ------- | --------- | --------- | --------- | ------------------------------------------- |
| Tex File Path  | STRING  |           |           |           | 纹理文件路径                                      |
| Desc File Path | STRING  |           |           |           | 描述文件路径，优先级高于描述字符                            |
| Desc String    | STRING  |           |           |           | 描述字符串                                       |
| Wrap Mode      | STRING  |           |           |           | 纹理环绕方式：Clamp To Edge，Mirrored Repeat，Repeat |

- Matte

说明：哑光。

| **参 数**     | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ----------- | ------- | --------- | --------- | --------- | ------- |
| Intensity   | FLOAT   | 1.0       | 0.0       | 0.0       | 强度      |
| Fill Radius | FLOAT   | 30.0      | 3.0       | 15.0      | 填充半径    |

- Mesh Warp

说明：网格变形特效。

| **参 数**      | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**                                                                                                                |
| ------------ | ------- | --------- | --------- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| Warp Info    | ARBDATA |           |           |           | 变形信息，参见 [NvsMeshWarpInfo](`com.meicam.sdk.NvsMeshWarpInfo`)。  (@ref NvsMeshWarpInfo)。 |
| Antialiasing | BOOL    |           |           | FALSE     | 开启抗锯齿                                                                                                                  |

- Midtones

说明：中间调。

| **参 数**         | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------------- | ------- | --------- | --------- | --------- | ------- |
| Color Tolerance | FLOAT   | 1.0       | 0.0       | 0.0       | 色容差     |
| Gray Min        | FLOAT   | 1.0       | 0.0       | 0.0       | 最低灰度    |
| Gray Max        | FLOAT   | 1.0       | 0.0       | 0.0       | 最高灰度    |
| Inverse         | BOOL    |           |           | FALSE     | 反相      |

- Video Echo

说明：彩虹幻影。

| **参 数**             | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------------------- | ------- | --------- | --------- | --------- | ------- |
| Echo Frame Count    | INT     | 22        | 2         | 15        | 幻影帧数量   |
| Echo Frame Interval | INT     | 5         | 1         | 1         | 帧间隔     |
| Opacity Array       | ARBDATA |           |           |           | 透明度数组   |
| Color Array         | ARBDATA |           |           |           | 透明度数组   |

- Master keyer

说明：色键的抠像。

| **参 数**                 | **类 型** | **最 大 值**          | **最 小 值**          | **默 认 值**          | **说 明** |
| ----------------------- | ------- | ------------------ | ------------------ | ------------------ | ------- |
| Key Color               | COLOR   | 1.0, 1.0, 1.0, 1.0 | 0.0, 0.0, 0.0, 0.0 | 0.0, 0.0, 0.0, 0.0 | 抠像基础颜色  |
| Softeness Amendment     | FLOAT   | 1.0                | -1.0               | 0.0                | 软边宽度    |
| Spill Removal           | BOOL    |                    |                    | FALSE              | 溢色去除开关  |
| Spill Removal Intensity | FLOAT   | 1.0                | 0.0                | 0.25               | 溢色去除强度  |
| Shrink Intensity        | FLOAT   | 1.0                | 0.0                | 0.0                | 缩边强度    |
| Disable Premultiply     | BOOL    |                    |                    | FALSE              | 关闭预乘    |
| Aperture                | FLOAT   | 360.0              | 0.0                | 90.0               | 抠像颜色孔径  |

- Liquefaction

说明：液化失真。

| **参 数** | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**       |
| ------- | ------- | --------- | --------- | --------- | ------------- |
| Point X | FLOAT   | 1.0       | 0.0       | 0.5       | 中心点X坐标（纹理坐标系） |
| Point Y | FLOAT   | 1.0       | 0.0       | 0.5       | 中心点Y坐标（纹理坐标系） |
| Radius  | FLOAT   | 1.0       | 0.0       | 0.25      | 半径（纹理坐标系）     |
| Type    | STRING  |           |           | Out       | 液化方式，支持In，Out |

- Horror

说明：恐惧。

- Grid

说明：网格特技。

| **参 数**   | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**            |
| --------- | ------- | --------- | --------- | --------- | ------------------ |
| Amplitude | FLOAT   | 3.0       | 0.0       | 1.0       | 振幅                 |
| Mode      | STRING  |           |           | Grid      | 模式 Grid，Point，Line |

- Noise Wave

说明：噪声波形扭曲。

| **参 数**         | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------------- | ------- | --------- | --------- | --------- | ------- |
| Wave Length     | FLOAT   | 0.5       | 0.0       | 0.05      | 波长      |
| Wave Amplify    | FLOAT   | 0.1       | 0.0       | 0.01      | 振幅      |
| Noise Magnitude | FLOAT   | 0.5       | 0.0       | 0.01      | 噪声强度    |
| Wave Frequency  | FLOAT   | 50.0      | 0.0       | 1.0       | 运动快慢    |

- Multi Shots

说明：分屏。

| **参 数**               | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------------------- | ------- | --------- | --------- | --------- | ------- |
| Horizontal Shot Count | INT     | 3         | 1         | 1         | 水平分屏数量  |
| Vertical Shot Count   | INT     | 3         | 1         | 1         | 垂直分屏数量  |

- Noise

说明：噪声。

| **参 数**       | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------------- | ------- | --------- | --------- | --------- | ------- |
| Intensity     | FLOAT   | 1.0       | 0.0       | 0.5       | 噪声强度    |
| Density       | FLOAT   | 1.0       | 0.0       | 0.5       | 噪声密度    |
| Grayscale     | BOOL    |           |           | FALSE     | 灰度噪声    |
| Tex File Path | STRING  |           |           |           | 纹理图片路径  |
| Tex Intensity | FLOAT   | 1.0       | 0.0       | 1.0       | 纹理强度    |
| Tex Scale     | FLOAT   | 1000.0    | 0.0       | 1.0       | 纹理缩放倍数  |

- Blend With Mask

说明：使用蒙版混合两个纹理，要求三个输入，依次为背景，前景，蒙版。

| **参 数**           | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**        |
| ----------------- | ------- | --------- | --------- | --------- | -------------- |
| Ignore Background | BOOL    |           |           | FALSE     | 忽略背景，将背景置为透明图像 |
| Inverse Mask      | BOOL    |           |           | FALSE     | 蒙版反相           |

- Hue Saturation

说明：色相/饱和度。

| 参 数      | 类 型     | 最 大 值 | 最 小 值 | 默 认 值 | 说 明                                                                                                                                                        |
| -------- | ------- | ----- | ----- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Settings | ARBDATA |       |       |       | 参数设置，参见 [NvsHueSaturationSettingInfo](`com.meicam.sdk.NvsHueSaturationSettingInfo`)。  (@ref NvsHueSaturationSettingInfo)。 |

##### 1.3、条件编译内建视频特效(Conditional Compiled Builtin Video Fx)

- Painting Effect

说明：画笔（参数设置见：
[NvsPaintingEffectContext](`com.meicam.sdk.NvsPaintingEffectContext`)

| **参 数** | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------- | ------- | --------- | --------- | --------- | ------- |
|         |         |           |           |           |         |

- Broken

说明：破碎效果。

| **参 数**            | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ------------------ | ------- | --------- | --------- | --------- | ------- |
| Cge File           | STRING  |           |           |           | Cge 文件  |
| Trans Normalized X | FLOAT   | 1.0       | \-1.0     | 0.0       | 平移X归一化  |
| Trans Normalized Y | FLOAT   | 1.0       | \-1.0     | 0.0       | 平移Y归一化  |

- Stroke Effect

说明：撞击效果。需三方技术支持。

| **参 数**          | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ---------------- | ------- | --------- | --------- | --------- | ------- |
| Source File Path | STRING  |           |           |           | 原文件路径   |

- Fluid

说明：流动。

| **参 数**   | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| --------- | ------- | --------- | --------- | --------- | ------- |
| Edge File | STRING  |           |           |           | 边缘文件    |

- Face Effect

说明：人脸美化效果。支持的功能有道具，美颜，美型和美妆。程序初始化阶段需要加载相应检测模型。人体检测与渲染方案来自三方合作伙伴。

| **参 数**                | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明** |
| ---------------------- | ------- | --------- | --------- | --------- | ------- |
| Face Type              | STRING  |           |           | NULL      | 脸型      |
| Face Shape Level       | FLOAT   | 1.0       | 0.0       | 0.5       | 基础脸型程度  |
| Cheek Thinning         | FLOAT   | 1.0       | 0.0       | 1.0       | 脸颊变薄    |
| Eye Enlarging          | FLOAT   | 1.0       | 0.0       | 0.5       | 大眼      |
| Beautification Package | STRING  |           |           |           | 美型包     |
| Face Ornament          | STRING  |           |           |           | 道具包     |
| FlipX                  | BOOL    |           |           | FALSE     | X方向翻转   |
| FlipY                  | BOOL    |           |           | FALSE     | Y方向翻转   |

- Face Effect2

说明：人脸美化效果。支持的功能有美颜，美型和美妆。程序初始化阶段需要加载相应检测模型。人体检测与渲染方案来自三方合作伙伴。

| **参 数**                       | **类 型** | **最 大 值**  | **最 小 值** | **默 认 值** | **说 明** |
| ----------------------------- | ------- | ---------- | --------- | --------- | ------- |
| Reddening                     | FLOAT   | 1.0        | 0.0       | 0.0       | 红润      |
| Whitening                     | FLOAT   | 1.0        | 0.0       | 0.0       | 美白      |
| Strength                      | FLOAT   | 1.0        | 0.0       | 0.0       | 磨皮      |
| Strength Mode                 | FLOAT   | 1.0        | 0.0       | 1.0       | 磨皮模式    |
| Eye Enlarging                 | FLOAT   | 1.0        | 0.0       | 0.0       | 大眼      |
| Shrink Face                   | FLOAT   | 1.0        | 0.0       | 0.0       | 瘦脸      |
| Shrink JAW                    | FLOAT   | 1.0        | 0.0       | 0.0       | 小脸      |
| Contrast                      | FLOAT   | 1.0        | 0.0       | 0.0       | 对比度     |
| Saturation                    | FLOAT   | 1.0        | 0.0       | 0.0       | 饱和度     |
| Sticker Mode                  | STRING  |            |           |           | 贴纸模式    |
| Sticker Music Disabled        | BOOL    |            |           | FALSE     | 音乐贴纸不可用 |
| Eye Enlarge Ratio             | FLOAT   | 1.0        | \-1.0     | 0.0       | 眼睛放大率   |
| Eye Corner Stretch Ratio      | FLOAT   | 1.0        | \-1.0     | 0.0       | 眼角拉伸比   |
| Shrink Face Ratio             | FLOAT   | 1.0        | \-1.0     | 0.0       | 缩脸比率    |
| Face Width Warp Ratio         | FLOAT   | 1.0        | \-1.0     | 0.0       | 脸宽扭曲率   |
| Face Length Warp Ratio        | FLOAT   | 1.0        | \-1.0     | 0.0       | 脸长扭曲率   |
| Forehead Warp Ratio           | FLOAT   | 1.0        | \-1.0     | 0.0       | 前额扭曲率   |
| Hairline Warp Ratio           | FLOAT   | 1.0        | \-1.0     | 0.0       | 发线扭曲率   |
| Malar Warp Ratio              | FLOAT   | 1.0        | \-1.0     | 0.0       | 颧骨扭曲率   |
| Jaw Warp Ratio                | FLOAT   | 1.0        | \-1.0     | 0.0       | 颚骨扭曲率   |
| Chin Warp Ratio               | FLOAT   | 1.0        | \-1.0     | 0.0       | 下巴扭曲率   |
| Eyebrow Warp Ratio            | FLOAT   | 1.0        | \-1.0     | 0.0       | 眉毛扭曲率   |
| Eye Distance Warp Ratio       | FLOAT   | 1.0        | \-1.0     | 0.0       | 眼间距扭曲率  |
| Nose Length Warp Ratio        | FLOAT   | 1.0        | \-1.0     | 0.0       | 鼻子长度扭曲率 |
| Nose Width Warp Ratio         | FLOAT   | 1.0        | \-1.0     | 0.0       | 鼻子宽度扭曲率 |
| Mouth Size Warp Ratio         | FLOAT   | 1.0        | \-1.0     | 0.0       | 嘴巴大小扭曲率 |
| Mouth Width Warp Ratio        | FLOAT   | 1.0        | \-1.0     | 0.0       | 嘴巴宽度扭曲率 |
| Mouth Corner Lift Ratio       | FLOAT   | 1.0        | \-1.0     | 0.0       | 嘴角提升率   |
| Narrow Nose Param             | FLOAT   | 1.0        | 0.0       | 0.0       | 瘦鼻      |
| Nose Length Param             | FLOAT   | 1.0        | \-1.0     | 0.0       | 长鼻参数    |
| Chin Length Param             | FLOAT   | 1.0        | \-1.0     | 0.0       | 下巴      |
| Mouth Size Param              | FLOAT   | 1.0        | \-1.0     | 0.0       | 嘴型      |
| Philtrum Length Param         | FLOAT   | 1.0        | \-1.0     | 0.0       | 人中      |
| Hairline Height Param         | FLOAT   | 1.0        | \-1.0     | 0.0       | 发际线     |
| Thin Face Shape Param         | FLOAT   | 1.0        | 0.0       | 0.0       | 瘦脸型     |
| Eye Distance Param            | FLOAT   | 1.0        | \-1.0     | 0.0       | 眼间距     |
| Eye Angle Param               | FLOAT   | 1.0        | \-1.0     | 0.0       | 眼睛角度    |
| Open Canthus Param            | FLOAT   | 1.0        | 0.0       | 0.0       | 开眼角     |
| Profile Rhinoplasty Param     | FLOAT   | 1.0        | 0.0       | 0.0       | 侧脸隆鼻参数  |
| Bright Eye Param              | FLOAT   | 1.0        | 0.0       | 0.0       | 亮眼      |
| Remove Dark Circles Param     | FLOAT   | 1.0        | 0.0       | 0.0       | 去黑眼圈    |
| Remove Nasolabial Folds Param | FLOAT   | 1.0        | 0.0       | 0.0       | 去法令纹    |
| White Teeth Param             | FLOAT   | 1.0        | 0.0       | 0.0       | 牙齿美白参数  |
| Apple Musle Param             | FLOAT   | 1.0        | 0.0       | 0.0       | 苹果肌     |
| Open External Canthus Param   | FLOAT   | 1.0        | 0.0       | 0.0       | 打开外眦参数  |
| Shrink Cheekbone Param        | FLOAT   | 1.0        | 0.0       | 0.0       | 收缩颧骨参数  |
| Custom Input Event            | INT     | 2147483647 | 0         | 0         | 自定制输入事件 |
| Makeup Eye Resource           | STRING  |            |           |           | 美妆眼睛资源  |
| Makeup Eye Strength           | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆眼睛强度  |
| Makeup Face Resource          | STRING  |            |           |           | 美妆脸部资源  |
| Makeup Face Strength          | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆脸部强度  |
| Makeup Lip Resource           | STRING  |            |           |           | 美妆嘴唇资源  |
| Makeup Lip Strength           | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆嘴唇强度  |
| Makeup Nose Resource          | STRING  |            |           |           | 美妆鼻子资源  |
| Makeup Nose Strength          | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆眉毛强度  |
| Makeup Brow Resource          | STRING  |            |           |           | 美妆眉毛资源  |
| Makeup Brow Strength          | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆眉毛强度  |
| Makeup Eyeliner Resource      | STRING  |            |           |           | 美妆眼线资源  |
| Makeup Eyeliner Strength      | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆眼线强度  |
| Makeup Eyelash Resource       | STRING  |            |           |           | 美妆睫毛资源  |
| Makeup Eyelash Strength       | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆睫毛强度  |
| Makeup Eyeball Resource       | STRING  |            |           |           | 美妆眼球资源  |
| Makeup Eyeball Strength       | FLOAT   | 1.0        | 0.0       | 1.0       | 美妆眼球强度  |
| Enable Landmark Callback      | BOOL    |            |           | FALSE     | 允许点位回调  |

#### 2、内建视频转场(Builtin Video Transition)

- Fade（淡入淡出）

- Turning（翻转）

- Swap（层叠）

- Stretch In（伸展进入）

- Page Curl（卷页）

- Lens Flare（镜头炫光）

- Star（星形）

- Dip To Black（闪黑）

- Dip To White（闪白）

- Push To Right（右推拉）

- Push To Top（上推拉）

- Upper Left Into（斜推）

## Source: `md_ch/ErrorCode.md`

Purpose: SDK error code meanings.

Primary title: 错误标识

Doc lead: CAPTURE_DEVICE_ERROR_UNKNOWN = 1（未知错误）

### 错误标识

###采集设备错误标识
		CAPTURE_DEVICE_ERROR_UNKNOWN = 1（未知错误）

		CAPTURE_DEVICE_ERROR_SERVER_DIED = 2 （服务关闭错误）

		CAPTURE_DEVICE_ERROR_FAIL_TO_START = 3 （启动失败错误）

		CAPTURE_DEVICE_ERROR_FAIL_TO_CONNECT = 4 （连接失败错误）

###硬件错误类型标识
		STREAMING_ENGINE_HARDWARE_ERROR_TYPE_VIDEO_ENCODER_SETUP_ERROR = 0 （视频编码器初始化错误）

		STREAMING_ENGINE_HARDWARE_ERROR_TYPE_VIDEO_ENCODING_ERROR = 1（视频编码错误）

		STREAMING_ENGINE_HARDWARE_ERROR_TYPE_VIDEO_DECODER_SETUP_ERROR = 2 （视频解码器初始化错误）

		STREAMING_ENGINE_HARDWARE_ERROR_TYPE_VIDEO_DECODING_ERROR = 3（视频解码错误）

###生成错误类型标识
		COMPILE_ERROR_TYPE_NO_ERROR = 0 （无错误）

		COMPILE_ERROR_TYPE_Cancelation = 1 (生成中断)

		COMPILE_ERROR_TYPE_VIDEO_ENCODER_SETUP_ERROR = 2 （视频编码器初始化失败）

		COMPILE_ERROR_TYPE_VIDEO_ENCODING_ERROR = 3 （编码错误）

		COMPILE_ERROR_TYPE_VIDEO_DECODING_ERROR = 4 （解码错误）

		COMPILE_ERROR_TYPE_MUXING_ERROR = 5 （视频封装失败）

## Source: `md_ch/QuestionList.md`

Purpose: Official troubleshooting FAQ.

Primary title: 疑难问题集锦

Doc lead: -# [如何生成方形视频？] (\ref 如何生成方形视频)

### 疑难问题集锦

-# [如何生成方形视频？] (\ref 如何生成方形视频)

-# [如何生成带有美肤特效的视频？] (\ref 如何生成带有美肤特效的视频)

-# [如何将多个素材生成一个视频文件？] (\ref 如何将多个素材生成一个视频文件)

-# [如何实现画中画？] (\ref 如何实现画中画)

-# [如何添加水印？] (\ref 如何添加水印)

-# [从录制界面到播放界面没有问题，返回之后，录制界面的预览黑屏] (\ref 从录制界面到播放界面没有问题，返回之后，录制界面的预览黑屏)

-# [NvsColor设置不生效] (`NvsColor`设置不生效)

-# [从录制界面到播出界面，播出界面的Livewindow闪黑然后播出正常] (\ref 从录制界面到播出界面，播出界面的Livewindow闪黑然后播出正常)

-# [某些手机录制的视频播放时画面方向不正常？] (\ref 某些手机录制的视频播放时画面方向不正常？)

-# [android使用美摄SDK时，代码混淆出错？] (`android`使用美摄SDK时，代码混淆出错？)

-# [使用H265如何设置进行视频拍摄和生成？] (\ref 使用H265如何设置进行视频拍摄和生成？)

-# [相机采集各档位分别对应的分辨率？] (\ref 相机采集各档位分别对应的分辨率？)

-# [生成各档位分别对应的码率？] (\ref 生成各档位分别对应的码率？)

-----------------------------------------------------------------------------------------------------------------------------
#### 详细解释

##### 1.如何生成方形视频?
	假设拍摄的视频是竖着拍摄分辨率1280*720，我们生成720*720的视频。

1)创建timeline
			NvsVideoResolution videoEditRes = new NvsVideoResolution();
			videoEditRes.imageWidth = 720;
			videoEditRes.imageHeight = 720;
			videoEditRes.imagePAR = new NvsRational(1, 1);
			NvsRational videoFps = new NvsRational(25, 1);
			NvsAudioResolution audioEditRes = new NvsAudioResolution();
			audioEditRes.sampleRate = 48000;
			audioEditRes.channelCount = 2;
			//创建时间线
			m_timeline = streamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);

	2)创建轨道和片段,path是片段的绝对路径。
			NvsVideoTrack videoTrack = m_timeline.appendVideoTrack();
			NvsVideoClip clip = videoTrack.appendClip(path);

	3)放大视频。
			clip.setPanAndScan(0, 1);

	详细设置参见[摇摄与扫描(Pan and Scan)] (`Pan_Scan.md`)

4)生成视频，path是生成视频的路径。
			m_streamingContext.compileTimeline(m_timeline, 0, m_timeline.getDuration(), path, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720
			, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, 0);

##### 2.如何生成带有美肤特效的视频?
	1)创建timeline、轨道、片段同问题1。

2)添加美肤特技。
                        clip.appendBeautyFx();

	3)生成视频。
##### 3.如何将多个素材生成一个视频文件？
	1)在创建轨道和片段的时候，添加多个素材创建出来多个片段。
			NvsVideoTrack videoTrack = m_timeline.appendVideoTrack();
			NvsVideoClip clip1 = videoTrack.appendClip(path1);
			NvsVideoClip clip2 = videoTrack.appendClip(path2);
			NvsVideoClip clip3 = videoTrack.appendClip(path3);
			NvsVideoClip clip4 = videoTrack.appendClip(path4);
			NvsVideoClip clip5 = videoTrack.appendClip(path5);

	2)生成视频。
			m_streamingContext.compileTimeline(m_timeline, 0, m_timeline.getDuration(), path, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720
			, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, 0));

	即可生成1个文件。
##### 4.如何实现画中画？
	简单的画中画，用两个不同分辨率的素材例如一个横着拍摄的素材和一个竖着拍摄的素材，分别添加到两个轨道上，就可以看到两个素材叠加在一起的效果。另外Transform 2D特技可以实现视频的放大缩小、旋转、给视频加透明度。
			NvsVideoTrack track1 = m_timeline.appendVideoTrack();
			NvsVideoTrack track2 = m_timeline.appendVideoTrack();
			NvsVideoClip clip1 = track1.appendClip(path1);
			NvsVideoClip clip2 = track2.appendClip(path2);

##### 5.如何添加水印？
	添加水印有两种方式：一是通过贴纸功能来实现的，需要用户发给一张带水印的图片，我们来进行制作。制作完的水印文件是UUID为文件名，.animatedsticker为扩展名的一个文件。有了这个文件，就可以通过我们的API实现添加水印的功能。
			StringBuilder m_stickerId = new StringBuilder();
			packagePath = "assets:/89740AEA-80D6-432A-B6DE-E7F6539C4121.animatedsticker";
			error = m_streamingContext.getAssetPackageManager().installAssetPackage(packagePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER, true, m_stickerId);
				if (error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
						&& error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
				Log.e(TAG, "Failed to install sticker package!");
			}

			m_timeline.addAnimatedSticker(0, m_timeline.getDuration(),m_stickerId.toString());

	二是通过NvsTimeline类里的addWatermark()接口添加水印。
			m_TimeLine.addWatermark(path, 0, 0, 1, NvsTimeline.NvsTimelineWatermarkPosition_TopLeft, 0, 0);//path是水印文件的路径，可以是PNG或JPG文件，或者是.caf格式文件

##### 6.从录制界面到播放界面没有问题，返回之后，录制界面的预览黑屏
	检查NvsStreamingContext类里的connectCapturePreviewWithLiveWindow()有没有调用或者调用出了问题，亦或是在调用startCapturePreivew()之后，调用了NvsStreamingContext上的stop()。同样，从录制界面到播出界面，播出黑屏，可能是调用playbackTimeline()后，又调用NvsStreamingContext的stop()。还有可能是NvsStreamingContext上的connectTimelineWithLiveWindow方法没有调用或调用出了问题。

##### 7.NvsColor设置不生效？
    NvsClor类成员是Float类型，R,G，B,A取值是0到1，如果所给颜色值是100，100，100，则需要分别除以255。

##### 8.从录制界面到播出界面，播出界面的Livewindow闪黑然后播出正常
	调用playbackTimeline播出需要预览一段时间，为了避免这个问题，需要先调用seekTimeline到0的位置，再播出，就不会闪黑了。

##### 9.某些手机录制的视频播放时画面方向不正常？
	可能是有些手机播放器不支持自动旋转，会造成视频播放时画面方向不正常，因而导致用户对录制的视频播产生误导。
##### 10.android使用美摄SDK时，代码混淆出错？
	使用代码混淆时，注意避免对下面的几个类进行混淆，正确避免方式如下：

		-keep class com.cdv.**  {*;}
		-keep class com.meicam.**  {*;}

	单独使用effectsdk时，需要对下面的类进行混淆，正确避免方式如下：

		-keep class com.cdv.effect.**  {*;}
		-keep class com.meicam.effect.**  {*;}

##### 11.使用H265如何设置进行视频拍摄和生成？
	使用H265进行视频拍摄的用法如下：
			Hashtable<String, Object> config = new Hashtable<>();
            config.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME, "hevc"); //h265方式
			context.startRecording(filePath, 0, config);

	使用H265进行视频生成的用法如下：
			Hashtable<String, Object> config = new Hashtable<>();
            config.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME, "hevc"); //h265方式
			context.setCompileConfigurations(config);//调用compileTimeline API之前设置
			context.compileTimeline(timeline, startTime, endTime, compileVideoPath, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH,0);

	\warning
		并非所有的android机都可以支持H265拍摄和生成，如若不支持，则会回到默认设置进行视频拍摄和生成。

##### 12.相机采集各档位分别对应的分辨率？
			Camera1：低等级：360p；中等级：480p；高等级：720p；更高等级：1080p；超高等级：2160p

			Camera2：低等级：720p；中等级：720p；高等级：720p；更高等级：1080p；超高等级：2160p

	注：SDK会对用户手机系统整体处理能力进行评估，若能够实时处理录制的视频，则采用设置的分辨率等级进行录制；若不能处理，SDK会适当降低当前分辨率等级以匹配用户手机系统能够达到的录制等级。
	例如：用某一款手机录制时设置更高等级，但是它可能录制不了这个等级的视频，所以就会适当降低其等级到高甚至是中，所以才会出现有些用户设置的视频录制的等级跟拍摄的视频等级不一致的情况。
	同样的，如果使用不带特效录制方式（使用系统相机录制），则会根据相机能够达到的分辨率级别选择适当的分辨率等级。假如相机达不到设置的分辨率等级，可能也会降低相应的分辨率等级来进行录制。

##### 13.生成各档位分别对应的码率？
			低码率：基础分辨率864 * 480 基础码率1M；中码率：基础分辨率864 * 480 基础码率1.5M；高码率：基础分辨率1280 * 720 基础码率6M
			计算规则：实际码率 = （实际分辨率 / 基础分辨率）* 基础码率
			例：720p分辨率中等码率为 (1280 * 720) / (864 * 480) * 1.5 = 3.3M

## Source: `md_ch/Glossary.md`

Purpose: Official terminology glossary.

Primary title: 名词解释

Doc lead: \anchor StreamingContext

### 名词解释

\anchor StreamingContext
###流媒体上下文(Streaming Context)
包含时间线、预览窗口、采集、资源包管理等相关信息集合的对象，Context被销毁之后，SDk视频制作框架也随之不复存在。

\anchor Seek
###定位(Seek)
渲染出指定位置的画面，并更新时间线的时间戳。

\anchor Compile
###生成(Compile)
以指定码率、帧速率和压缩格式输出文件。

\anchor Capture
###采集(Capture)
捕获摄像头设备画面。

\anchor Record
###录制(Record)
输出采集画面到指定格式文件中。

\anchor Timeline
###时间线(Timeline)
编辑场景的时间轴实体，由轨道组成，可以有多个视频轨道和音频轨道，由视频轨道决定长度。

\anchor Track
###轨道(Track)
容纳片段的实体，分为视频轨道(Video Track)和音频轨道(Audio Track)，可随片段的增加不断延展。

\anchor Clip
###片段(Clip)
容纳音视频内容的实体，分为视频片段(Video Clip)和音频片段(Audio Clip)，视频片段可以是图片或者视频。

\anchor CaptureVideoFx
###采集视频特效(Capture Video Fx)
一种应用在采集中的视频特效。

\anchor VideoFx
###视频特效(Video Fx)
一种视频图像的特殊效果，可能改变视频图像的整体或局部的颜色、亮度、透明度等信息，使视频显示特殊的效果。

\anchor AudioFx
###音频特效(Audio Fx)
一种音频的特殊效果，可能改变音频的声调、速率等信息。

\anchor VideoTransition
###视频转场(Video Transition)
片段间切换的特效，从一个视频到另一个视频的播放衔接过渡效果。添加转场后，片段在转场时间内可能有重叠效果。

\anchor Theme
###主题(Theme)
一系列特效应用的集合，包括片头、片尾、视频特效、视频转场、音乐、字幕样式等。

\anchor Caption
###字幕(Caption)
视频上叠加的自定义文字，可以设置字号和颜色等样式。

\anchor CaptionStyle
###字幕样式(Caption Style)
预定义字幕属性集合，包括字号和颜色等。

\anchor AnimatedSticker
###动画贴纸(Animated Sticker)
带有动画效果的贴纸，叠加在视频上产生一些特殊效果。

\anchor LiveWindow
###预览窗口(Live Window)
实时显示时间线或者采集图像的窗口。

\anchor VideoResolution
###视频解析度(Video Resolution)
视频的基本信息，包括图像宽高和[像素横纵比] (@ref PixelAspectRatio)等。

\anchor AudioResolution
###音频解析度(Audio Resolution)
音频的基本信息，包括采样率和声道数等。

\anchor PanAndScan
###摇摄和扫描(Pan and Scan)
一种调整图像适配的方法，可以横向剪切和纵向平移。

\anchor AssetPackage
###资源包(Asset Package)
一种需要安装的特效资源，安装后可以作为特效使用，包括视频特效、视频转场、主题、字幕样式、动画贴纸。

\anchor AssetPackageID
###资源包ID(Asset Package ID)
资源包的唯一标识，安装资源包成功后获得，添加特效时使用。

\anchor TrimIn
###裁剪入点(Trim In)
裁剪片段的起始点。对于裁剪入点，裁剪出点，入点，出点的详细解释，请参见[裁剪入点与出点(trimIn and trimOut)专题] (`TrimInOut.md`)

\anchor TrimOut
###裁剪出点(Trim Out)
裁剪片段的终止点。

\anchor InPoint
###入点(In Point)
片段在时间线的起始点。

\anchor OutPoint
###出点(Out Point)
片段在时间线上的终止点。

\anchor Speed
###播放速度(Speed)
片段播放的速度，速度没有改变的情况下，(出点-入点)=(裁剪出点-裁剪入点)，如果播放速度为2倍速，(出点-入点)*2=(裁剪出点-裁剪入点)。

\anchor Bitrate
###码率(Bitrate)
每秒传送的比特数，码率越高，视频质量越好。

\anchor SampleRate
###采样率(Sample Rate)
每秒从连续信号中采集的离散信号个数。

\anchor FrameRate
###帧速率(Frame Rate)
每秒刷新图像的帧数，帧速率越高，视频的连续性越好。

\anchor AspectRatio
###横纵比(Aspect Ratio)
图像的横向尺寸与纵向尺寸的比例。

\anchor PixelAspectRatio
###像素横纵比(Pixel Aspect Ratio)
一个像素点的宽与高的比例。SDK中仅支持1:1。

## Source: `md_ch/effect_QuestionList.md`

Purpose: Effect SDK FAQ.

Primary title: 疑难问题集锦

Doc lead: -# [android使用effectSDK时，代码混淆出错？] (`android`使用effectSDK时，代码混淆出错？)

### 疑难问题集锦

-# [android使用effectSDK时，代码混淆出错？] (`android`使用effectSDK时，代码混淆出错？)


-----------------------------------------------------------------------------------------------------------------------------
#### 疑难详细解释

##### 1.android使用effectSDK时，代码混淆出错？
        使用effectsdk时，需要避免对下面的类进行混淆，正确避免方式如下：

		-keep class com.cdv.effect.**  {*;}

		-keep class com.meicam.effect.**  {*;}
