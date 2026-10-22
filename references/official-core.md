# Official Core And Integration Docs

This reference is distilled from the SDK Doxygen Markdown and bundled inside the skill.
Prefer it for official API behavior and constraints, then use demo-derived references for implementation call order.

Read when: Use for SDK architecture, initialization rules, supported formats, license/package setup, file info, coordinates, 4K support, engine changes, and general Android integration constraints.

Notes:
- iOS-only conditional sections are removed where the source document marks them explicitly.
- Image references are omitted because this skill keeps text/API knowledge self-contained.
- Source paths below are relative identifiers from the original documentation, not external runtime dependencies.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Source: md_ch/Mainpage.md](#source-md_chmainpagemd)
- [Source: md_ch/Introduction.md](#source-md_chintroductionmd)
- [Source: md_ch/Overview.md](#source-md_choverviewmd)
- [Source: md_ch/PortingGuide.md](#source-md_chportingguidemd)
- [Source: md_ch/licenseFile.md](#source-md_chlicensefilemd)
- [Source: md_ch/support4kVideoEdit.md](#source-md_chsupport4kvideoeditmd)
- [Source: md_ch/Coordinate.md](#source-md_chcoordinatemd)
- [Source: md_ch/avFileInfo.md](#source-md_chavfileinfomd)
- [Source: md_ch/assetsPackageInstall.md](#source-md_chassetspackageinstallmd)
- [Source: md_ch/BreakpointContinuation.md](#source-md_chbreakpointcontinuationmd)
- [Source: md_ch/EngineChange.md](#source-md_chenginechangemd)
- [Source: md_en/Streaming_SDK_Guide.md](#source-md_enstreaming_sdk_guidemd)
<!-- END GENERATED CONTENTS -->

## Source: `md_ch/Mainpage.md`

Purpose: Documentation landing page and module overview.

Primary title: 美摄SDK

Doc lead: * [API文档] (docs/index.html)

### 美摄SDK
* [API文档] (docs/index.html)


* 流媒体SDK(StreamingSDK)
	* [产品概述] (`Introduction.md`)

美摄SDK功能特点介绍
	* [名词解释] (`Glossary.md`)

开发中词汇的统一表达
	* [基础结构与概念] (`Overview.md`)

美摄SDK整体工作流程与结构概念
	* [技术专题讲解] (`Topic.md`)

用于学习了解复杂技术概念
	* [疑难问题解答] (`QuestionList.md`)
	* 附件

[内建特效名称列表] (`FxNameList.md`)

* effectSDK
	* [产品概述] (`effect_Introduction.md`)

effectsdk功能特点介绍
	* [名词解释] (`Glossary.md`)

开发中词汇的统一表达
	* [基础结构与概念] (`effect_Overview.md`)

effectsdk整体工作流程与结构概念
	* [技术专题讲解] (`effect_Topic.md`)

用于学习了解复杂技术概念
	* [疑难问题解答] (`effect_QuestionList.md`)
	* 附件

[内建特效名称列表] (`FxNameList.md`)

## Source: `md_ch/Introduction.md`

Purpose: Product capabilities, package types, formats, and platform notes.

Primary title: 产品概述

Doc lead: 法律声明

### 产品概述

法律声明
-----------------------
-----------------------
美摄SDK是一款为开发者快速接入视频拍摄、编辑、制作服务的软件开发工具包，北京美摄网络有限公司（简称美摄公司）拥有该产品的全部知识产权。开发者在签订协议后，拥有对于此款产品的使用权。开发者在使用此产品时，不得违反中华人民共和国有关法律法规及相关政策，因使用此产品发生任何争议由开发者自行解决并承担相关责任，如造成美摄公司损失的（包括但不限于财产损失、名誉损失等），还应承担赔偿责任。

美摄公司拥有对于美摄SDK、开发文档、及其他相关文件拥有全部版权，在未经美摄公司书面许可的情况下，不得复制、修改和擅自分发，如有相关情况，美摄会根据相应法律进行追责。

服务对象
-----------------------
-----------------------
美摄的Streaming SDK，其包含了视频拍摄、编辑、特效渲染等各种功能，其应用场景主要是完全依赖于美摄能力的视频全流程产品开发，后期视频编辑制作等，开发者可以根据自己的创意创建APP，实现各种音视频处理功能，美摄公司会随时根据手机系统、手机硬件、使用场景的变化，快速调整，完善，升级SDK工具包，保证SDK包的稳定性、高效率、高兼容性、给开发者带来良好的服务体验。

试用与正式使用
-----------------------
-----------------------
美摄SDK免费给任何开发者提供试用机会，只需通过在美摄SDK网站完成开发者注册，即可进行SDK下载试用，但是在生成作品中，会带有试用水印，以保证美摄公司权益，如果想获得完整的使用体验，请联系商务团队，进行沟通洽谈。

网站：[www.meishesdk.com] (http://www.meishesdk.com)

商务邮箱：[bd@meishesdk.com]

联系电话：8610-82853090

能力与限制
-----------------------
-----------------------
* 支持的系统：
    * iOS 9.0 iPhone5S 以上系统
        * Android 5.0 以上系统
        * Harmony Next 5.0.0 以上系统

* 输入规范：
	* 视频格式：MP4、MOV、WMV、M2V、MPG
        * 音频格式：MP3、FLAC、AAC、M4A、WAV
        * 图片格式：JPG、PNG、JPEG
	* 视频编码：H264、WMV、MPEG4
	* 音频编码：MP3、AAC、PCM、FLAC

* 输出规范：
	* 视频格式：MP4、MOV
	* 视频编码：H264
	* 音频编码：AAC
	* 图片规范：Bitmap

* 扩展包格式（扩展包是美摄用来承载扩展素材的内容包，包括主题、字幕、滤镜、贴纸等）：
	* 主题：.theme
	* 字幕：.captionstyle
	* 滤镜：.videofx
	* 贴纸：.animatedsticker
	* 转场：.videotransition
	* 道具：.arscene

产品特点
-----------------------
-----------------------
###实时特效、高清录制
SDK支持1080P高清视频录制，提供非常丰富的拍摄录制功能，在录制的同时可以叠加多种特效，并实时预览，最大程度满足不同场景的录制需求，具体特点如下：

* 最大录制1080P视频，并可设定720P、480P等多种质量
* 支持16:9、1:1等不同的画幅比例
* 支持多段视频录制
* 带有基础录制功能，例如对焦，镜头切换，曝光补偿、闪光灯等
* 自带美肤功能
* 自带滤镜功能，支持扩展

###支持多轨道、多段编辑
* 支持同时将不同格式的视频、图片、进行混合多段编辑
* 视频支持多轨道（视频、图片）
* 支持多种画幅16:9、1:1

###制作特效实时预览
通过预览窗口（LiveWindow）可以在制作的过程中实时预览制作效果，而不需进行预处理和打包，大大提升了制作的体验、降低了制作成本和时间

###高清视频输出
SDK支持多种格式内容的输入，并最高支持到4K输入，同时最高支持4K视频输出，并且开发者可以根据需求设定不同的输出级别（1080P、720P、480P等）

###全能的基础编辑功能
美摄SDK包含市面上最为丰富的基础编辑功能，非常简单的调用方式，开发者们可以根据自己的需求进行灵活组合使用。基础功能包括：

* 视频裁剪、分割
* 视频变速
* 视频、图片插入
* 视频、图片排序
* 视频、图片删除
* 图片时长设定
* 图片画面裁剪
* 图片运动设定
* 画面参数调整（亮度、饱和度、对比度等）
* 画面旋转等

###视频实时美肤处理
SDK中自带视频实时美肤特效，可以在拍摄、编辑的过程中直接加入美肤效果，并进行实时预览，同时可以调节美肤处理的等级，美白参数等处理

![美肤效果] (`Beauty.png`)

###绚丽的视频主题
SDK拥有一套强大的主题系统，每个主题都包含：片头尾、音乐、画面运动、前景动画、转场、字幕等，只需一键，就可以对视频进行智能处理，实现电影效果，具体特征如下：
* 拥有复杂的画面处理
* 配套片头尾、音乐、转场等
* 可嵌入配套字幕样式
* 支持3D场景
* 拥有150+已有主题可选
* 提供快速制作服务

![主题] (`Theme.png`)

###顶级字幕功能
SDK的字幕系统达到广电包装水准，不仅是添加一行文字这么简单，字幕功能可以实现一套非常绚丽的字幕包装效果，同时具有良好的扩展性，具体特征如下：

* 支持动画底图
* 支持文字运动，逐字运动
* 文字颜色、描边可调
* 支持透明度
* 支持多行字幕
* 支持载入字体

![字幕] (`Caption.png`)

###多轨道音频编辑
SDK支持不限数量的音频轨道编辑，单轨道音频同时支持多段音频导入与编辑，同时具有多种音频处理方式，具体如下：

* 多轨道音频输入
* 支持多段音频
* 音频裁剪
* 多种音频处理（电音、娃娃音效果等）
* 音频转场（淡入淡出等）
* 音量独立控制

###画面前景滤镜
拥有独有的前景滤镜处理方式，整个滤镜由图像处理，边框处理，前景动画效果叠加组成，不仅可以完成简单的调色，还可以实现更多丰富的画面效果，同时还提供前景滤镜的定制服务，满足个性化需求

![滤镜] (`Filter.png`)

###动画贴纸效果
SDK支持在制作过程中，向视频中加入动画贴纸进行修饰，同时可以对贴纸进行属性设置，达到美化视频画面的作品，具体如下：

* 支持复杂运动效果
* 支持有声贴纸
* 支持镜像
* 支持旋转
* 支持大小修改
* 支持贴纸扩展

![动画贴纸] (`Stiker.png`)

###转场过渡效果
SDK支持在片段间添加转场，保证衔接的过程中达到平滑、出色的过渡效果，让视频间更加流畅，同时美摄提供非常多的预置转场效果，供开发者们进行选择，同时可以根据开发者的需求，提供定制化转场服务

![转场] (`Transition.png`)

###丰富的素材库和定制化服务
SDK同时会提供丰富的素材库供开发者们选择使用，并且会定期更新一些新的内容进入素材库中，并会有一定比例的免费内容让开发者们无偿使用，同时提供个性化定制内容，只需少量花费，专业团队为开发者们定制个性化素材，当前素材库包含：


具体可以点击[素材库] (http://www.meishesdk.com)了解

## Source: `md_ch/Overview.md`

Purpose: SDK architecture overview and core object model.

Primary title: 基础结构与概念

Doc lead: 美摄SDK核心模块包括流媒体上下文、时间线、字幕、动画贴纸、轨道、音/视频片段等。

### 基础结构与概念

###模块结构
美摄SDK核心模块包括流媒体上下文、时间线、字幕、动画贴纸、轨道、音/视频片段等。

流媒体上下文是SDK中最基础的模块，它负责生成、保存并维护SDK引擎运行时的上下文环境。时间线由流媒体上下文生成，包含字幕，动画贴纸以及多个音视频轨道，各模块协同工作以生成最终的视频效果。其中每条音/视频轨道上可以添加若干个音/视频片段，片段上可以添加各种特效，片段之间可以设置不同的转场效果。

![美摄SDK总体结构] (`structure.png`)

###数据流
美摄SDK支持两种媒体输入方式，标准媒体文件与摄像头采集。

当输入为一个或多个媒体文件时，SDK会首先从文件中提取出对应的音频与视频片段，这些片段可以理解为对原音频流与视频流的裁剪与封装。以视频为例，在编辑过程中，用户可以对这些视频片段进行任意拼接，放到对应轨道上，轨道再放到时间线上。每一个轨道可以类比成一个图层，SDK引擎对轨道渲染的顺序是自下到上的，各层轨道之间可以通过设置透明度等参数来实现一些特殊的效果。SDK引擎支持对时间线、轨道与音/视频片段添加特效，包括音/视频特效、转场、字幕、动画贴纸以及主题等，其中主题可以当成是上述特效的一个闭包。SDK默认提供若干内置的编辑特效，更多的特效资源包可以在[美摄官网] (http://www.meishesdk.com)下载。编辑后的视频可以通过SDK提供的预览窗口进行预览，或者直接打包生成媒体文件。

当使用摄像头设备作为输入时，SDK引擎只能对其添加采集特效与包特效，不能使用转场、字幕、动画贴纸等其他特效。生成的视频同样可以通过SDK提供的预览窗口进行预览，或者直接打包生成媒体文件。

![美摄SDK数据流图] (`dfd.png`)


![美摄SDK数据流图] (`dfd-child.png`)

## Source: `md_ch/PortingGuide.md`

Purpose: Android project import and migration notes.

Primary title: 开发指南

Doc lead: 一、开发前的准备工作

### 开发指南


一、开发前的准备工作
为了方便开发者进行开发，请先在美摄SDK官网下载美摄SDK和适用于Android Studio的样例代码。强烈建议使用Android Studio(http://developer.android.com/sdk/index.html)进行开发。

1、创建一个Android Studio工程。注意：美摄SDK使用的minSdkVersion(minimum API level)是19。为了兼容性，请在创建工程时将minSdkVersion设置为19。

打开Android Studio，新建工程如下，填写Application name和Company Domain。点击Next。
![创建工程] (@ref CreateProject_android.png)

将minimum SDK更改为API 19:Android 4.4(KitKat)。点击Next，直到Finish。
![更改minimum SDK] (@ref MinimumSDK_android.png)

2、导入SDK文件。打开美摄SDK下的lib目录，将android_jar目录下的.jar文件复制到目录MyApplication->app->libs里。

![jar文件目录图] (@ref JarFilePath.png)

在java、res和AndroidManifest.xml的同级目录创建文件夹jniLibs，进入jniLibs，将美摄SDK的lib目录下的android_armv7目录及其里面的.so文件复制到这个目录。最后注意将android_armv7目录名重命名为armeabi-v7a。导入SDK工作完成。

![so文件目录图] (@ref SOFilePath_android.png)

## Source: `md_ch/licenseFile.md`

Purpose: License file placement and behavior.

Primary title: 许可文件

Doc lead: 美摄SDK有两种许可：SDK许可，素材包许可。SDK许可与素材包许可是同步使用的，即要么两者都使用，要么两者都不用。区别是，不使用许可在程序中会出现SDK的水印，反之水印会去掉。

### 许可文件

美摄SDK有两种许可：SDK许可，素材包许可。SDK许可与素材包许可是同步使用的，即要么两者都使用，要么两者都不用。区别是，不使用许可在程序中会出现SDK的水印，反之水印会去掉。
美摄SDK提供包括贴纸，滤镜，主题，转场等多种类型的素材，每种类型素材又包含多个素材包，一个素材包对应一个素材包许可。如果有使用SDK的用户，需要用到许可文件，则由美摄SDK后台开发人员提供。

## Source: `md_ch/support4kVideoEdit.md`

Purpose: 4K editing support constraints.

Primary title: 4k视频编辑

Doc lead: 如何支持4k视频编辑？

### 4k视频编辑

如何支持4k视频编辑？

在创建NvsStreamingContext单例对象时，有两种方式：一是不带flags的创建方式，另一种是带flags的创建方式。使用带flags的的创建方式,且输入参数flags值为
[STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT] (`com.meicam.sdk.NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT`)
，即创建了支持4k视频编辑的NvsStreamingContext单例对象。这里仅支持4k视频编辑，不支持4k视频拍摄。如果输入参数flags值为0，则该创建方式与不带flags的创建方式相同。

NvsStreamingContext单例对象创建方式不同，在创建NvsTimeline对象时，输入参数值的范围也就不同。如果是支持4k视频编辑，则可创建4k时间线对象，即输入参数videoEditRes里的
imageWidth*imageHeight不能高于3840*2160像素。相反，不支持的话，则对应的imageWidth*imageHeight不能高于1920*1080像素。而后续的视频裁剪，特效添加，生成等则是类同的。

## Source: `md_ch/Coordinate.md`

Purpose: Coordinate-system conventions.

Primary title: 时间线与视图坐标(TimeLine and View Coordinate)

Doc lead: SDk框架中，有两种坐标系：美摄SDK坐标系和视图坐标系。美摄SDK坐标系即时间线坐标系，是SDK中创建时间线，添加素材时所使用的坐标系。编辑视频时，使用时间线坐标对要添加的字幕、贴纸、视频特效、Transform 2D等素材进行相应的位置设置。Transform 2D特效在坐标系中可实现视频的缩放旋转及平移。

### 时间线与视图坐标(TimeLine and View Coordinate)

SDk框架中，有两种坐标系：美摄SDK坐标系和视图坐标系。美摄SDK坐标系即时间线坐标系，是SDK中创建时间线，添加素材时所使用的坐标系。编辑视频时，使用时间线坐标对要添加的字幕、贴纸、视频特效、Transform 2D等素材进行相应的位置设置。Transform 2D特效在坐标系中可实现视频的缩放旋转及平移。
录制或者编辑视频之前，我们需要按某种横纵比例设置其图像宽高。时间线坐标原点位于已设置的图像宽高所构建的矩形框的中心，X轴向右，Y轴向上。以创建1280 * 720 的视频为例，如下图，

![时间线坐标] (`timelineCoordinate.PNG`)

视图坐标系是Live Window控件播放视频使用的坐标系。在播放预览视频时，可设置Live Window的填充模式。如果需要将对应的时间线坐标转换成视图坐标，有相应的API接口可供调用进行转换。具体请参见
[NvsLiveWindow] (`com.meicam.sdk.NvsLiveWindow`)的转换接口。
视图坐标原点位于实时预览窗口的左上角，X轴向右，Y轴向下。如下图，视图坐标：

![视图坐标] (`viewCoordinate.PNG`)

## Source: `md_ch/avFileInfo.md`

Purpose: Audio/video file information APIs.

Primary title: 音视频文件信息

Doc lead: [NvsAVFileInfo](`com.meicam.sdk.NvsAVFileInfo`)

### 音视频文件信息

[NvsAVFileInfo](`com.meicam.sdk.NvsAVFileInfo`)
类即音视频文件信息类，包括音视频的时长，文件类型，数据速率，视频流数目，音频流数目，以及对应的接口来获取其他属性信息。对用户来说，在添加完所有片段之后，
要获取某个片段的音视频文件信息，则需要找到对应的音视频片段对象。获取音视频片段对象的操作如下：

1.通过时间线对象，获取相应的视频轨道[getVideoTrackByIndex()](`com.meicam.sdk.NvsTimeline.getVideoTrackByIndex`)或者音频轨道[getAudioTrackByIndex()](`com.meicam.sdk.NvsTimeline.getAudioTrackByIndex`)。

2.通过轨道对象，获取相应的视频片段[getClipWithIndex()] (`com.meicam.sdk.NvsVideoTrack.getClipByIndex`)或者音频片段[getClipWithIndex()] (`com.meicam.sdk.NvsAudioTrack.getClipByIndex`)，即得到音视频片段对象。

每个片段对象都可以获取此片段的文件路径[getFilePath()](`com.meicam.sdk.NvsClip.getFilePath`)，
然后通过NvsStreamingContext类的接口
[getAVFileInfo()](`com.meicam.sdk.NvsStreamingContext.getAVFileInfo`)接口，
即可获取相应的文件属性信息。注意：getAVFileInfo待输入的参数即所获取的片段对象的文件路径。

## Source: `md_ch/assetsPackageInstall.md`

Purpose: Streaming SDK asset package install flow.

Primary title: 素材包安装

Doc lead: 美摄SDK提供多种素材包，包括贴纸，滤镜，主题，转场等。在使用每种素材包时，都需要安装，升级或者卸载。每种素材包，都有统一的安装方式。

### 素材包安装

美摄SDK提供多种素材包，包括贴纸，滤镜，主题，转场等。在使用每种素材包时，都需要安装，升级或者卸载。每种素材包，都有统一的安装方式。
安装步骤如下：

1.登录美摄SDK官网，进入后台下载相应的素材包。注意：禁止修改下载的素材包的名称及后缀。同时，若要使用许可文件，也不允许修改其后缀。

2.初始化NvsStreamingContext后，通过getAssetPackageManager()，获取资源包管理器对象。

3.获取资源包管理器对象后，调用installAssetPackage()接口安装素材包。安装返回类型是
ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR或者是ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED则表示安装成功或者已经安装，
其他则安装失败。如果安装失败，用户可根据返回值查找对应安装失败的原因；安装成功，会对应获取到素材包的UUId值，
用于在添加包裹式素材（包括主题，滤镜，转场等）时使用。

注意,安装容易出错有两点：

一是安装接口installAssetPackage()里需传入待安装素材包的类型，可能会出错。

二是初始化NvsStreamingContext使用SDK的许可，则安装素材包时也得对应加上素材许可，否则会报错。

另外，安装后若要升级或者卸载，则需要调用upgradeAssetPackage()接口或者uninstallAssetPackage()接口即可。

## Source: `md_ch/BreakpointContinuation.md`

Purpose: Compile/export breakpoint continuation behavior.

Primary title: 断点续导

Doc lead: 断点续导是在文件生成过程中的一个概念，指在生成过程中因为各种原因导致生成中断，当下一次生成开始，在所有参数与上一次生成完全一致的情况下，可以从中断位置继续生成文件。

### 断点续导

###断点续导介绍
    断点续导是在文件生成过程中的一个概念，指在生成过程中因为各种原因导致生成中断，当下一次生成开始，在所有参数与上一次生成完全一致的情况下，可以从中断位置继续生成文件。

	断点续导需要在普通生成文件的基础上，开启断点续导标识、设置切片文件存储路径以及设置切片文件长度。

	当用户开启断点续导后，SDK会根据用户指定的切片长度（默认10秒）在用户指定的文件储存路径下生成切片文件，在所有切片文件都生成成功后再把所有切片文件合成一个最终文件。

###断点续导参数设置与接口使用
	通过在生成时间线时，设置时间线配置中的具体参数来实现
		public boolean compileTimeline(NvsTimeline timeline,
                                   long startTime,
                                   long endTime,
                                   String outputFilePath,
                                   int videoResolutionGrade,
                                   int videoBitrateGrade,
                                   Hashtable<String, Object> compileConfigurations,
                                   int flags)

		COMPILE_VIDEO_ENABLE_BREAKPOINT_CONTINUATION = "enable breakpoint continuation" 设置是否开启断点续导

		COMPILE_VIDEO_CACHE_FILE_PATH = "cache file path" 断点续导缓存文件路径

		COMPILE_VIDEO_CACHE_FILE_DURATION = "cache file duration" 断点续导切片视频长度

###断点续导FAQ
	1.断点续导默认切片长度

	答：切片默认长度为10秒。

	2.断点续导失败的原因

	答：在常规生成失败原因的基础上（如编码失败，解码失败，读写权限等），用户没有指定断点续导缓存路径，断点续导过程中切片文件或缓存路径被删除等也会导致断点续导失败。

	3.断点续导使用建议

	答：1）切片时长设置要适宜。设置的过短会造成切片过碎，设置的过长又会耗用比较长的时间。

	2）每个续导文件最好使用不同的缓存路径。虽然SDK内部会以命名规则来区分切片文件，但是使用不同的缓存路径会使得文件系统更清晰，也更利于管理。

	3）生成成功后，SDK并不会主动删除缓存切片文件，需要用户自行删除。

	4）如果生成文件时长不长的前提下，不建议使用断点续导。因为断点续导需要生成切片文件，最后还要将切片文件合成，所以不触发断点续导的前提下直接生成的效率要比设置断点续导更快。

## Source: `md_ch/EngineChange.md`

Purpose: Engine behavior changes relevant to app compatibility.

Primary title: 引擎变化

Doc lead: 流媒体引擎状态包括引擎停止、采集预览、采集录制、播放、定位以及生成。具体请参见

### 引擎变化

流媒体引擎状态包括引擎停止、采集预览、采集录制、播放、定位以及生成。具体请参见
[流媒体引擎状态](`STREAMING_ENGINE_STATE`)。
流媒体引擎状态变化如下图，
[image omitted: 流媒体引擎状态变化]

图中每个矩形框都表示一种引擎状态。由图可见，添加轨道、素材等会引发引擎状态发生变化。播放、定位、生成三种状态之间相互转换，都需要经过引擎停止状态。而由采集预览跳转采集录制状态，不用跳转到停止状态。视频录制完成后，要经过停止状态，才能跳转到播放，定位及生成状态。

## Source: `md_en/Streaming_SDK_Guide.md`

Purpose: English conceptual guide with compact Java API examples.

Primary title: simple guide to Meishe streaming SDK

Doc lead: This is a very simple guide to Meishe streaming SDK aimed to help developers to understand the basic concepts of video editing/capturing and visual effects Meishe SDK can handle, W

### simple guide to Meishe streaming SDK


### A simple guide to Meishe streaming SDK

  This is a very simple guide to Meishe streaming SDK aimed to help developers to understand the basic concepts of video editing/capturing and visual effects Meishe SDK can handle, We will also describe the basic steps to complete a common video editing/capturing task using Meishe streaming SDK.

  Meishe streaming SDK is a versatile video/audio processing SDK to help users to build their video content creation applications, including video capturing, video editing, visual effect and more. It currently works under Android 4.1+ and iOS 8.0+ (We also have Windows and macOS version, but not released as a product). Meishe streaming SDK implements nearly the same API for both Android and iOS, they differ only in language, one in JAVA and one in objective-C. For video editing, Meishe streaming SDK uses an architecture which is much like NLE(non-linear video editing) system, user can create a timeline with any number of video track/video clips and can modify them at any time without any pre-process to the original media files. For video capturing, Meishe streaming SDK will handle all the dirty work for developers and let them concentrate on the content they are capturing.

  This guide will first introduce the basic concept of video editing and steps to call the API; Then we will cover video capturing.

#### 1、Video editing

  To edit video and audio files by Meishe streaming SDK you must create a timeline to describe what to do with the media files. A timeline is a data structure to let developers tell the streaming engine how to process the media files. It is composed of any number of video tracks and audio tracks, each track can contain a sequence of video/audio clips. You can add video transition effects between two adjacent clips and can add unlimited video/audio filter effects in video/audio clip. Timeline video FX,animated sticker and caption can also be added in the timeline level.

  The following graph demonstrate the structure of a timeline.

[image omitted: Streaming Context]

  One can create any number of timelines at a time. If you want to create a timeline you can do it with the following code snippet:

    NvsStreamingContext streamingCtx = NvsStreamingContext.init(ctx, null, 0);
    NvsVideoResolution videoEditRes = new NvsVideoResolution();
    videoEditRes.imageWidth = 1280;
    videoEditRes.imageHeight = 720;
    videoEditRes.imagePAR = new NvsRational(1, 1);
    NvsRational videoFps = new NvsRational(30, 1);
    NvsAudioResolution audioEditRes = new NvsAudioResolution();
    audioEditRes.sampleRate = 44100;
    audioEditRes.channelCount = 2;
    NvsTimeline timeline = streamingCtx.createTimeline(videoEditRes, videoFps, audioEditRes);


  First of all you must call NvsStreamingContext.init() to initialize the SDK before doing anything with Meishe streaming SDK. The above code creates a timeline with a video dimension of 1280x720, 30 frames per second and the audio sample rate of 44100 and 2 audio channels. The created timeline object will be returned in NvsStreamingContext.createTimeline().

  Suppose that you have two video files: /tmp/video1.mp4（duration:10 seconds）and /tmp/video2（duration:5 seconds）,you want to add both video files to the timeline and edit them. You can do it as follows:


    NvsVideoTrack videoTrack = timeline.appendVideoTrack();
    NvsVideoClip videoClip1 = videoTrack.appendClip(“/tmp/video1.mp4”);
    NvsVideoClip videoClip2 = videoTrack.appendClip(“/tmp/video2.mp4”);

  NOTE: you must create at least one video track in the timeline to hold video clips since timeline can only hold tracks and clips are held in tracks. Now you have added two video clips with the specified media file path in the only video track of the timeline. The first video clip will occupy [0,10s) time interval in the video track and second will occupy [10,15). Now you want to preview the content in the timeline(i.e. the two video clips) then you can do it as follows:


    streamingCtx.connectTimelineWithLiveWindow(timeline, liveWindow);
    streamingCtx.playbackTimeline(timeline, 0, -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);

  NOTE: liveWindow here indicates a created view object of type NvsLiveWindow, it is used to display the timeline output frame. Before using it you must call NvsStreamingContext.connectTimelineWithLiveWindow() to connect a timeline with the live window. After calling NvsStreamingContext.playbackTimeline() the video files in the timeline will be played back and the output video frame will be presented in the live window.

  Now suppose you don’t like some contents of the two video files, you just want the first 4 seconds of the first video file and the last 2 seconds of the second video file, then you do it as follows:

    videoClip1.changeTrimOutPoint(4000000, true);
    videoClip2.changeTrimInPoint(3000000, true);

  Now you have done it, if you play back the timeline again you will the observe the change you have made. Note that the above code will finish instantly and will not modify the original physical video file, it just tells the timeline you want to crop the video file and all the work will be done in real-time when you play back the timeline.

  Now let me give you a brief introduction of what the function really does. First of all every clip has a trim in and a trim out point, it indicates which part of the media file you want to process in the timeline. For example, when you append /tmp/video1.mp4 at first, its trim in point will be 0, and trim out point will be 10000000 which means you will use the whole file(Please keep that in mind that all the time value used in Meishe streaming SDK will be in microsecond). videoClip1.changeTrimOutPoint(4000000, true); simply changes the trim out point of the first video clip to 4s which means the last 6s is cut out. The second parameter is set to true means the subsequent clips will be moved forward according to this change, if you set the second parameter to false it will leave a 6s hole between the first clip and the second. Then videoClip2.changeTrimInPoint(3000000, true); simply cuts the first 3s of the first video file.

  Note that there are many more operations you can do to edit the video/audio clips in the timeline but since this is a simple guide, we will not discuss them here.

  Say that you have completed your video editing and you want to generate a final video of the timeline, you can do this by:

    streamingCtx.compileTimeline(timeline, 0, timeline.getDuration(), “/tmp/output.mp4”, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, 0);

  By calling compileTimeline() the streaming engine starts to compile the final result of the timeline into a video file specified by you(in this example, /tmp/output.mp4). This call will return immediately after you call it, the compiling is being processed in the internal threads of the streaming engine. You must implement NvsStreamingContext.CompileCallback/NvsStreamingContext.CompileCallback2 interface to listen to the progress/failure/cancellation event of the compiling process.

  Suppose that you want more fun with the video you have created, you decide to add a cartoon effect to the first video clip and a color correction to the whole timeline, you can do this as follows:

    videoClip1.appendBuiltinFx(“Cartoon”);
    NvsTimelineVideoFx lutFx = timline.addBuiltinTimelineVideoFx(0, timeline.getDuration(), “Lut”);
    lutFx.setStringVal(“Data File Path, “/tmp/pink-3dlut.mslut”);

  Now, the visual effects has been added, you can play back the timeline to see the change. There are many built-in visual effects in Meishe streaming SDK, each one has a set of parameters which you can use to tune the visual effect. Apart from built-in visual effect there are also packaged visual effect which is the real power of Meishe SDK, it gives you unlimited possibility and extensibility to visual effect. We also have custom video FX. But these beyond the scope of this guide.

  Now you may want to add a caption to the timeline:

    timline.addCaption(“Hello World!”, 1000000, 3000000, null);

  A caption has been added to the timeline which start from 1s and last 3s. The last parameter of addCaption() indicate a caption style package which can give more visual impact on your caption, but we will not discuss it here.

  You can also add transition effect between clips such as:

    videoTrack.setBuiltinTransition(0, “Lens Flare”);

  You will see a lens flare effect between the first video clip and the second one.
There are also animated stickers but we don’t discuss it here.

  You can also add audio clips to an audio track of the timeline, you edit audio clips the same way as you edit video clips. Note that the audio track in a video file will also form a audio track of the timeline but it is invisible to developers (but you can change its volume if you want). You can also add audio effects to audio clips.

  The last thing I want to discuss is theme. A theme is package to beautify your timeline automatically. To apply a theme to a timeline you can do this:

    timeline.applyTheme(themeId);

  After this your timeline has been decorated by the given theme package. Every theme package has its own design, this is the fastest way to beautify your timeline. The theme package is among the several kinds of packaged materials of Meishe SDK provided.

  Below is a graph to demonstrate the usage of timeline:

[image omitted: Timeline]


#### 2、Video capturing

  Now let’s move to the topic of video capturing. Capture video with Meishe SDK is very easy, to start a camera preview simply do as the following:

    streamingCtx.connectCapturePreviewWithLiveWindow(mLiveWindow);
    streamingCtx.startCapturePreview(0, NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH , NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER, null));

  First, we connect capture preview with a live window object, then we call startCapturePreview() to start capture preview, the captured video frame will be presented in the live window view. The first parameter of startCapturePreview() is the capture device index,

  Meishe streaming SDK provides API to query capture device count and facing of each capture device. The second parameter indicates the resolution level of the capture preview. In general NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH will start a capture preview of 720P in dimension. You can also set some flags in the third parameters but we won’t discuss it here.

  There are many operations to control how you can capture a video such as focus, auto exposure, exposure compensation..., but these are beyond the scope of this guide.

  You may want to add a visual effect for video capturing, do it as follows:

    NvsStreamingContext.appendBuiltinCaptureVideoFx(“Beauty”);

  This will add a face beautification built-in effect to video capturing. Note that all the visual effects available for video editing also apply to video capturing. You can also add face related stickers to video capturing.

  To record the captured video frames to a file:


    streamingCtx.startRecording(“/tmp/record.mp4”);


  This will start video recording and save video frames to the specified media file. You can call NvsStreamingContext.stopRecording() to finish video recording. You can call startRecording()/stopRecording() multiple times to record several video files. It is also possible to record several interval into a single media file.

  Below is a graph to demonstrate video capturing:

[image omitted: Captrue video]


#### 3、Epilogue
  This is a very simple guide to Meishe streaming SDK. It can do much more than the functions described in this guide. Developers can take the sdk demo project as a starting point. There are also API documents in Meishe SDK website: https://www.meishesdk.com
