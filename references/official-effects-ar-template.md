# Official Effects AR And Template Docs

This reference is distilled from the SDK Doxygen Markdown and bundled inside the skill.
Prefer it for official API behavior and constraints, then use demo-derived references for implementation call order.

Read when: Use for Effect SDK integration, effect package management, beauty/AR scene, segmentation, keying, mask generation, virtual live broadcast, Mimo, template/cut-same package parsing, and template timeline generation.

Notes:
- iOS-only conditional sections are removed where the source document marks them explicitly.
- Image references are omitted because this skill keeps text/API knowledge self-contained.
- Source paths below are relative identifiers from the original documentation, not external runtime dependencies.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Source: md_ch/effect_Introduction.md](#source-md_cheffect_introductionmd)
- [Source: md_ch/effect_Overview.md](#source-md_cheffect_overviewmd)
- [Source: md_ch/effect_PortingGuide.md](#source-md_cheffect_portingguidemd)
- [Source: md_ch/effect_assetsPackageInstall.md](#source-md_cheffect_assetspackageinstallmd)
- [Source: md_ch/effect_EffectSdkUse.md](#source-md_cheffect_effectsdkusemd)
- [Source: md_ch/effect_middle_module.md](#source-md_cheffect_middle_modulemd)
- [Source: md_ch/AR_Scene_7_243.md](#source-md_char_scene_7_243md)
- [Source: md_ch/Segment.md](#source-md_chsegmentmd)
- [Source: md_ch/Mask_Generator.md](#source-md_chmask_generatormd)
- [Source: md_ch/Master_Keyer.md](#source-md_chmaster_keyermd)
- [Source: md_ch/virtualLiveBroadcast.md](#source-md_chvirtuallivebroadcastmd)
- [Source: md_ch/mimo_Android.md](#source-md_chmimo_androidmd)
- [Source: md_ch/Template_Android.md](#source-md_chtemplate_androidmd)
- [Source: md_ch/TemplateGenerate_Android.md](#source-md_chtemplategenerate_androidmd)
<!-- END GENERATED CONTENTS -->

## Source: `md_ch/effect_Introduction.md`

Purpose: Effect SDK capability overview.

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
美摄的Effect SDK，其主要是涵盖了特效渲染的功能，其应用场景是仅利用美摄的SDK进行特效类如滤镜、字幕、贴纸、道具等的渲染处理，往往应用在如拍摄的特效处理、直播、VR等场景，开发者可以根据自己的需求独立使用SDK的所有特效能力，美摄公司会随时根据手机系统、手机硬件、使用场景的变化，快速调整，完善，升级SDK工具包，保证SDK包的稳定性、高效率、高兼容性、给开发者带来良好的服务体验。

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
	* ios 9.0 iPhone5S 以上系统
	* Android 5.0以上系统

* 扩展包格式（扩展包是美摄用来承载扩展素材的内容包，包括主题、字幕、滤镜、贴纸等）：
	* 字幕：.captionstyle
	* 滤镜：.videofx
	* 贴纸：.animatedsticker
	* 转场：.videotransition
	* 道具：.arscene

产品特点
-----------------------
-----------------------
###智能美肤美型

提供完整的美肤、美型解决方案：任意调节五官、脸型比例，提供多种高级视频美颜滤镜。

美颜具有智能美白、磨皮、红润、滤镜、锐度等功能，效果更自然，色调高级，极富有质感，快速打造动人形象。

![美肤效果] (`effect_Beauty.png`)

美型具有，瘦脸、小脸（脸拉长收短）、大眼、下巴、额头、瘦鼻、嘴形等部位进行调节

![美型效果] (`effect_Beautiful.png`)

###推镜特效
时下流行的推镜特效，有火焰，爱心，电视，NO！，惊悚，凉凉，律动，弹跳，狗仔队，戏剧化等10个效果，让视频内容更具表现力、趣味性和冲击力。

![推镜特效] (`effect_Tuijing.jpg`)

###歌词字幕
在录制的时，可以选择一首音乐，并且录制中歌词会随着音乐的播放显示在录制的画面上。
字幕样式可以随心选择符合录制视频风格的样式。

![歌词字幕] (`effect_changci.jpg`)


###滤镜效果
美摄Effect SDK有着非常丰富的滤镜效果库，并且紧跟潮流趋势，不断开发制作更新滤镜样式和效果。

![滤镜效果] (`effect_Filter.png`)

漫画书，水墨，单色漫画

![漫画书，水墨，单色漫画] (`effect_manhua.jpg`)


线性，抖动，灵魂出窍，毛刺

![线性，抖动，灵魂出窍，毛刺] (`effect_douyin.jpg`)


###丰富的素材库和定制化服务
SDK同时会提供丰富的素材库供开发者们选择使用，并且会定期更新一些新的内容进入素材库中，并会有一定比例的免费内容让开发者们无偿使用，同时提供个性化定制内容，只需少量花费，专业团队为开发者们定制个性化素材，当前素材库包含：


具体可以点击[素材库] (http://www.meishesdk.com)了解。

## Source: `md_ch/effect_Overview.md`

Purpose: Effect SDK module overview.

Primary title: 基础结构与概念

Doc lead: 输入方式：GLTexture作为输入，因为图像的渲染应该在OpenGL线程中进行。

### 基础结构与概念

###数据流
输入方式：GLTexture作为输入，因为图像的渲染应该在OpenGL线程中进行。

通过上下文(NvsEffectSdkContext)加载的特效，都要通过渲染入口(NvsEffectRenderCore)来渲染到画面中。NvsEffect是生成特效时返回的特效类，通过它的set方法可以对添加的特效进行基于字段的个性化编辑。

SDK默认提供若干内置的编辑特效，更多的特效资源包可以在[美摄官网] (http://www.meishesdk.com)下载。

![EffectSDK数据流图] (`Shujutu.png`)

## Source: `md_ch/effect_PortingGuide.md`

Purpose: Effect SDK Android project import notes.

Primary title: 开发指南

Doc lead: 一、开发前的准备工作

### 开发指南


一、开发前的准备工作
为了方便开发者进行开发，请先在美摄SDK官网下载美摄SDK和适用于Android Studio的样例代码。强烈建议使用Android Studio(http://developer.android.com/sdk/index.html)进行开发。

1、创建一个Android Studio工程。注意：美摄SDK使用的minSdkVersion(minimum API level)是16。为了兼容性，请在创建工程时将minSdkVersion设置为16。

打开Android Studio，新建工程如下，填写Application name和Company Domain。点击Next。
![创建工程] (@ref CreateProject_android.png)

将minimum SDK更改为API 16:Android 4.1(Jelly Bean)。点击Next，直到Finish。
![更改minimum SDK] (@ref MinimumSDK_android.png)

2、导入SDK文件。打开美摄SDK下的lib目录，将android_jar目录下的.jar文件复制到目录MyApplication->app->libs里。

![jar文件目录图] (@ref JarFilePath.png)

在java、res和AndroidManifest.xml的同级目录创建文件夹jniLibs，进入jniLibs，将美摄SDK的lib目录下的android_armv7目录及其里面的.so文件复制到这个目录。最后注意将android_armv7目录名重命名为armeabi-v7a。导入SDK工作完成。

![so文件目录图] (@ref SOFilePath_android.png)

## Source: `md_ch/effect_assetsPackageInstall.md`

Purpose: Effect SDK asset package install flow.

Primary title: 素材包安装

Doc lead: 美摄SDK提供多种素材包，包括贴纸，滤镜，主题，转场等。在使用每种素材包时，都需要安装，甚至升级或者卸载。针对每种素材包，都有统一的安装方式。

### 素材包安装

美摄SDK提供多种素材包，包括贴纸，滤镜，主题，转场等。在使用每种素材包时，都需要安装，甚至升级或者卸载。针对每种素材包，都有统一的安装方式。
安装步骤如下：

1.登录美摄SDK官网，进入后台下载相应的素材包。注意：禁止修改下载的素材包的名称及后缀。同时，若要使用许可文件，也不允许修改其后缀。


2.初始化NvsEffectSdkContext后，通过资源包管理器对象接口getAssetPackageManager()，获取资源包管理器对象。

3.获取资源包管理器对象后，调用installAssetPackage()接口安装素材包。安装返回类型是
ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR或者是ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED则表示安装成功或者已经安装，
其他则安装失败。如果安装失败，用户可根据返回值查找对应安装失败的原因；安装成功，会对应获取到素材包的UUId值，
用于在添加包裹式素材（包括主题，滤镜，转场等）时使用。

注意：

安装容易出错有两点：一是安装接口installAssetPackage()里需传入待安装素材包的类型，可能会出错。

二是初始化NvsEffectSdkContext使用SDK的许可，则安装素材包时也得对应加上素材许可，否则会报错。

另外，安装后若要升级或者卸载，则需要调用upgradeAssetPackage()接口或者uninstallAssetPackage()接口即可。

## Source: `md_ch/effect_EffectSdkUse.md`

Purpose: Effect SDK context and renderer usage.

Primary title: effectSDK使用讲解

Doc lead: 美摄SDK effectSDK使用方式如下：

### effectSDK使用讲解

美摄SDK effectSDK使用方式如下：


NvsEffectSdkContext特效上下文类可视作整个SDK框架的入口。开发过程中，NvsEffectSdkContext提供了静态sharedInstance接口创建effectSDK上下文的唯一实例。
通过这个实例对象，我们可以一个或者多个特效的处理。整个使用完成后，要销毁特效上下文的对象实例。
添加素材资源包(采集特效包，场景资源包等)，都得先安装，安装成功后获取packageId才能使用，而内建采集特效(builtin)只需获取特效名称即可使用。

sdk接口中凡是需要传入资源、授权等文件路径时一定是全路径。
\warning NvsEffectSdkContext类中，所有public API都在UI线程使用！！！
\warning NvsEffectRenderCore类中，所有public API都在OpenGL线程使用！！！

1.初始化EffectSDK，全局只需一次，NvsEffectSdkContext是特效的上下文类。Context是安卓Context对象，sdkLicenseFilePath是授权文件路径，flags 标志字段，如果无特殊需求请填写0。

NvsEffectRenderCore是特效渲染类整个SDK的特效渲染入口，所有public API都必须在OpenGL线程使用！！！。

初始化代码：

			mEffectSdkContext = NvsEffectSdkContext.init(this, "assets:/effectsdkdemo.lic", 0);
			mEffectRenderCore = context.createEffectRenderCore();


NvsEffectRenderCore的初始化，flags 标志字段，如果无特殊需求请填写0。注意：initialize方法调用要在GL线程，和调用render方法在同一线程，保证GL上下文一致。

		mEffectRenderCore.initialize(0);

2.创建视频特效对象。

fxIds 特效id。对于内嵌视频特效，就是特效的名字，如果是资源包特效，就是资源包id，aspectRatio 特效的宽幅比。视频特效可以同时添加多个，搭配使用。

视频特效NvsVideoEffect是NvsEffect是的派生类，可以通过它进行视频特效的添加，移除和获取等操作。

相应代码如下：

			NvsRational aspectRatio = new NvsRational(9, 16);
			NvsEffect effect = mEffectSdkContext.createVideoEffect("Color Property", aspectRatio);

3.设置特效的相关参数。fxParam是对应的参数名称，val是参数的值。

相应代码如下：

			effect.setFloatVal("Saturation", 0);//饱和度
			effect.setFloatVal("Brightness", 0);//亮度
			effect.setFloatVal("Contrast", 0);//对比度


4.除了内置特效还有需要安装资源包的外置特效。assetPackageFilePath是资源包的路径，必须是全路径。licenseFilePath是授权文件路径，如果没有可以写null。type是资源包的类型。

synchronous是是否同步的标准，assetPackageId是安装后的资源包id。

相应代码如下：

			String fxPackagePath = "assets:/7CBBDCFB-4568-47FB-8A98-3A699893A043.3.videofx";
			int error = mEffectSdkContext.getAssetPackageManager().installAssetPackage(fxPackagePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX, true, m_fxPackageId);
			if (error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                && error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            Log.d(TAG, "Failed to install fx package!");
			}

5.使用完成，销毁视频特效。清除特效中携带的OPenGL资源，effect表示要清除的特效对象。

相应代码如下：

			mEffectRenderCore.clearEffectResources(effect);

6.退出时销毁。相应代码如下：

			NvsEffectSdkContext.close();

## Source: `md_ch/effect_middle_module.md`

Purpose: Effect SDK middle module usage for Android.

Primary title: 快速接入指南

Doc lead: ---

### 快速接入指南

### NveEffectKit使用说明文档

---

NveEffectKit集成了美颜、美型、美妆、妆容、滤镜、人脸道具功能。依赖库为3.8.0以上的美摄Effect库

#### 快速体验
- [美摄](https://www.meishesdk.com/downloads)官方网站下载SDK人脸版本(下载**zip**包为`NvStreamingSdk_Android_..._ARSCENE_MS.zip`
)
- 使用Android Studio打开`./samples/android/NvEffectKitDemo`快速体验相关功能。
- 运行demo时可查阅[常见问题](#常见问题)。

#### 如何导入项目？

Android打包为AAR库(`NveEffectKit.aar`)，复制到libs目录下(`./app/libs`)，在build.gradle设置aar的编译引入
>NveEffectKit.aar路径： `./samples/android/NvEffectKitDemo/libBase/libs/NveEffectKit.aar`

```groovy
api fileTree(dir: 'libs', include: ['*.jar', '*.aar'])
```

#### 初始化SDK

init时需传入授权文件路径，该路径可以是assets下路径，或本地的绝对路径。
`effectsdkdemo.lic`请联系[美摄商务](https://www.meishesdk.com/)获取

```java
/**
 * Context 上下文
 * 美摄 SDK 授权文件
 */
String licPath = "assets:/effectsdkdemo.lic";
NveEffectKit.getInstance().init(this, licPath);
```

#### 初始化人脸检测模型

初始化模型，需传入模型类型和路径（路径可以为assets路径或本地绝对路径）

```java
/**
 * Context 上下文
 * 模型类型
 * 模型路径
 */
NveEffectKit.getInstance().initModel(this, NveDetectionModelType.FACE, faceModelPath);
```

| 类型                                 | 名称     | 用途                 |
| ---------------------------------- |:------ | ------------------ |
| NveDetectionModelType.FACE         | 人脸     | 人脸道具使用             |
| NveDetectionModelType.FAKE_FACE    | 假脸     | 人脸道具使用             |
| NveDetectionModelType.MAKEUP2      | 美妆     | 美妆使用            |
| NveDetectionModelType.FACE_COMMON      | 人脸通用     | 美颜和美妆使用            |
| NveDetectionModelType.ADVANCED_BEAUTY      | 高级美颜     | 美颜和妆容使用            |
| NveDetectionModelType.EYEBALL      | 眼球     | 部分人脸道具会用到眼球效果      |
| NveDetectionModelType.SEGMENTATION | 背景分割   | 部分人脸道具会用到分割效果      |
| NveDetectionModelType.AVATAR       | Avatar | 根据表情动的特效果类别会使用这个模型 |

- **NveDetectionModelType.MAKEUP2在SDK3.13.x以上已废弃**
- **NveDetectionModelType.FACE_COMMON和NveDetectionModelType.ADVANCED_BEAUTY最低支持版本为 SDK3.13.x**

- *人脸模型详情可查看demo代码*
> **samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/Constants.java**
>
```java
samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/MainActivity.java

private void initEffectModel() {}
```
- 更多可查看[常见问题](#2模型中face240和face106有什么区别)。

#### 相机预览，录制参考demo代码
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/camera/...
```java
samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/MainActivity.java

private GLSurfaceView mGlView;
private RenderCameraUtil mRenderCameraUtil;
```

#### 美颜使用

```java
//美颜的使用
NveBeauty beauty= new NveBeauty();
//开关可以通过enable参数控制
beauty.setEnable(true);
//只设置一次即可，后续修改参数可直接调用beauty的参数set方法。
NveEffectKit.getInstance().setBeauty(beauty);

//磨皮和美白有多种类型，默认类型如下
beauty.setBlurType(NveBeautyBlurTypeEnum.AdvancedBuffingSkin1);
beauty.setWhiteningType(NveBeautyWhiteningTypeEnum.WhiteningA);
```

| 参数                  | 类型                        | 用途          |
| ------------------- | ------------------------- | ----------- |
| enable              | boolean                   | 美颜功能开关      |
| blurType            | NveBeautyBlurTypeEnum     | 磨皮类型        |
| blurIntensity       | float                     | 磨皮强度，[0-1]  |
| whiteningType       | NvBeautyWhiteningTypeEnum | 美白类型        |
| whiteningIntensity  | float                     | 美白强度，[0-1]  |
| matteIntensity      | float                     | 去油光强度，[0-1] |
| matteFillRadius     | float                     | 去油光半径，[0-1] |
| reddeningIntensity  | float                     | 红润强度，[0-1]  |
| definitionIntensity | float                     | 清晰度强度，[0-1] |
| sharpnessIntensity  | float                     | 锐度强度，[0-10] |

磨皮类型

| 名称                                         | 用途    |
| ------------------------------------------ | ----- |
| NveBeautyBlurTypeEnum.BuffingSkin          | 普通磨皮  |
| NveBeautyBlurTypeEnum.AdvancedBuffingSkin1 | 高级磨皮1 |
| NveBeautyBlurTypeEnum.AdvancedBuffingSkin2 | 高级磨皮2 |
| NveBeautyBlurTypeEnum.AdvancedBuffingSkin3 | 高级磨皮3 |

- 更多可查看[常见问题](#3普通磨皮高级磨皮1高级磨皮2高级磨皮3有什么区别)。

美白类型

| 名称                                   | 用途  |
| ------------------------------------ | --- |
| NvBeautyWhiteningTypeEnum.WhiteningA | 美白A |
| NvBeautyWhiteningTypeEnum.WhiteningB | 美白B |

- 更多可查看[常见问题](#4美颜a美颜b有什么区别)。

#### 美型使用

```java
//使用美型
NveShape shape= new NveShape();
shape.setEnable(true);
NveEffectKit.getInstance().setShape(shape);
//如何使用美型包？
//瘦脸 为例
//新增美型，分别传入类型，shapeDegree:美型强度[-1,1]，
float shapeDegree = 1f;
//packagePath 此处为模拟路径，替换为实际资源包路径
String packagePath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh";
// 资源包授权文件路径
String packageLicPath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.lic";
//如果资源的结尾是facemesh则类型为ASSET_PACKAGE_TYPE_FACE_MESH，如果是warp则为ASSET_PACKAGE_TYPE_WARP
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh
int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.warp
// int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
//shapePackageID：美型包ID(包需要安装,安装见下面安装使用)
String shapePackageID = NveAssetPackageManagerUtil.installFxPackage(packagePath, packageLicPath, packageType);
shape.setShapeData(NveShapeTypeEnum.FACE_SIZE, new NveShapeData(shapeDegree, shapePackageID));
//修改美型强度
shape.setDegreeByType(NveShapeTypeEnum.FACE_SIZE, shapeDegree);
NveEffectKit.getInstance().setShape(shape);
```

| 名称                            | 用途        |
| ----------------------------- | --------- |
| NveShapeTypeEnum.FACE_WIDTH   | 窄脸，[-1,1] |
| NveShapeTypeEnum.FACE_LENGTH  | 小脸，[-1,1] |
| NveShapeTypeEnum.FACE_SIZE    | 瘦脸，[-1,1] |
| NveShapeTypeEnum.FORE_HEAD    | 额头，[-1,1] |
| NveShapeTypeEnum.CHIN         | 下巴，[-1,1] |
| NveShapeTypeEnum.EYE_SIZE     | 大眼，[-1,1] |
| NveShapeTypeEnum.EYE_ANGLE    | 眼角，[-1,1] |
| NveShapeTypeEnum.NOSE_WIDTH   | 瘦鼻，[-1,1] |
| NveShapeTypeEnum.NOSE_LENGTH  | 长鼻，[-1,1] |
| NveShapeTypeEnum.MOUTH_SIZE   | 嘴型，[-1,1] |
| NveShapeTypeEnum.MOUTH_CORNER | 嘴角，[-1,1] |

#### 微整形使用

```java
//使用微整形
NveMicroShape microShape = new NveMicroShape();
microShape.setEnable(true);
NveEffectKit.getInstance().setMicroShape(microShape);

//新增微整形，分别传入类型，shapeDegree:微整形强度，
float shapeDegree = 0.5f;
//packagePath 此处为模拟路径，替换为实际资源包路径
String packagePath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh";
// 资源包授权文件路径
String packageLicPath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.lic";
//如果资源的结尾是facemesh则类型为ASSET_PACKAGE_TYPE_FACE_MESH，如果是warp则为ASSET_PACKAGE_TYPE_WARP
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh
int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.warp
// int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
//shapePackageID：微整形ID(包需要安装,安装见下面安装使用)
String shapePackageID = NveAssetPackageManagerUtil.installFxPackage(packagePath, packageLicPath, packageType);
//HEAD_SIZE 为例
shape.setMicroShapeData(NveMicroShapeTypeEnum.HEAD_SIZE, new NveMicroShapeData(shapeDegree,shapePackageID));
//修改微整形强度
shape.setDegreeByType(NveMicroShapeTypeEnum.HEAD_SIZE, shapeDegree);
```

| 名称                                      | 用途          |
| --------------------------------------- |:-----------:|
| NveMicroShapeTypeEnum.HEAD_SIZE         | 缩头，[-1,1]   |
| NveMicroShapeTypeEnum.CHEEKBONE_WIDTH   | 颧骨宽，[-1,1]  |
| NveMicroShapeTypeEnum.JAW_WIDTH         | 下颌宽，[-1,1]  |
| NveMicroShapeTypeEnum.TEMPLE_WIDTH      | 太阳穴宽，[-1,1] |
| NveMicroShapeTypeEnum.NASOLABIAL_FOLDS  | 法令纹，[0,1]   |
| NveMicroShapeTypeEnum.DARK_CIRCLES      | 黑眼圈，[0,1]   |
| NveMicroShapeTypeEnum.BRIGHTEN_EYES     | 亮眼，[0,1]    |
| NveMicroShapeTypeEnum.WHITEN_TEETH      | 美牙，[0,1]    |
| NveMicroShapeTypeEnum.EYE_ANGLE_DEGREE  | 眼角度，[-1,1]  |
| NveMicroShapeTypeEnum.EYE_DISTANCE      | 眼离，[-1,1]   |
| NveMicroShapeTypeEnum.EYE_HEIGHT        | 眼高度，[-1,1]  |
| NveMicroShapeTypeEnum.EYE_WIDTH         | 眼宽度，[-1,1]  |
| NveMicroShapeTypeEnum.EYE_ARC           | 眼弧度，[-1,1]  |
| NveMicroShapeTypeEnum.EYE_Y_OFFSET      | 眼上下，[-1,1]  |
| NveMicroShapeTypeEnum.PHILTRUM          | 人中，[-1,1]   |
| NveMicroShapeTypeEnum.NOSE_BRIDGE_WIDTH | 鼻梁宽度，[-1,1] |
| NveMicroShapeTypeEnum.NOSE_HEAD         | 鼻头，[-1,1]   |
| NveMicroShapeTypeEnum.EYEBROW_THICKNESS | 眉毛粗细，[-1,1] |
| NveMicroShapeTypeEnum.EYEBROW_ANGLE     | 眉角度，[-1,1]  |
| NveMicroShapeTypeEnum.EYEBROW_Y_OFFSET  | 眉上下，[-1,1]  |
| NvMicroShapeTypeEnum.EYEBROW_X_OFFSET   | 眉间距，[-1,1]  |

> [美摄SDK For Android: 特效名称列表 (meishesdk.com)](https://www.meishesdk.com/android/doc_ch/html/content/FxNameList_8md.html)

美颜、美型、微整形的各个参数均来自于美摄文档仓库中AR Scene的说明，更多进阶用法见上方链接。

---

#### 美妆

```java
//使用美妆
NveMakeup makeUp= new NveMakeup();
makeUp.setEnable(true);
NveEffectKit.getInstance().setMakeup(makeUp);

//新增美妆中的单妆，NvSingleMakeUp来自单妆包中解析的makeup.json
//(包需要安装,安装见下面安装使用)
makeUp.addSingleMakeUp(NveMakeupTypeEnum, NveSingleMakeUp);
//根据单妆类型删除使用的单妆，每个类型的单妆只能加一个，例如只能加一种类型的口红。
makeUp.removeSingleMakeUp(NveMakeupTypeEnum);

//妆容的使用，NvComposeMakeup来自妆容包中解析的info.json
//(包需要安装,安装见下面安装使用)
makeUp.setComposeMakeup(NveComposeMakeup);
//妆容的删除。妆容是由多个单妆、美颜、美型、微整形、滤镜等组成，每次只能应用一个妆容
makeUp.removeComposeMakeUp();

//调节单妆强度
makeUp.setIntensityByType(NveMakeupTypeEnum.Brighten,1);
//调节单妆颜色
makeUp.setColorByType(NveMakeupTypeEnum.Brighten,new NvsColor(0,0,0,0));
```
> **json解析安装等可参考：**
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/NvAssetManager
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/AssetInfoData

| 名称                              | 用途  |
| ------------------------------- | --- |
| NveMakeupTypeEnum.Lip           | 口红  |
| NveMakeupTypeEnum.Eyebrow       | 眉毛  |
| NveMakeupTypeEnum.Eyeshadow     | 眼影  |
| NveMakeupTypeEnum.Eyelash       | 睫毛  |
| NveMakeupTypeEnum.Eyeliner      | 眼线  |
| NveMakeupTypeEnum.Blusher       | 腮红  |
| NveMakeupTypeEnum.Shadow        | 修容  |
| NveMakeupTypeEnum.Brighten      | 高光  |
| NveMakeupTypeEnum.ComposeMakeup | 妆容  |

#### 滤镜

```java
//必传ID，包滤镜需安装，传入安装后的ID(安装见下面安装使用)
NveFilter filter = new NveFilter(effectId);
NveEffectKit.getInstance().addFilter(filter);

//setFilter表示使用滤镜，后续可以进行其他修改参数操作，例如修改强度：
filter.setFilterIntensity(0.5f);

//移除滤镜
NveEffectKit.getInstance().removeFilter(filter);
```
> **json解析安装等可参考：**
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/NvAssetManager
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/AssetInfoData
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/FilterJsonParseData

#### 道具

```java
NveFaceProp faceProp = new NveFaceProp();
faceProp.setEnable(true);
NveEffectKit.getInstance().setFaceProp(faceProp);

//设置道具Id(道具包需要安装,安装见下面安装使用)
String propId = "xxx"
faceProp.setPropId(propId);
```
> **json解析安装等可参考：**
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/NvAssetManager
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/AssetInfoData
> samples/android/NvEffectKitDemo/app/src/main/java/com/meicam/effectsdkdemo/data/StickerJsonParseData
---

#### 自定义特效

NveEffectKit除了上述已有功能，用户可自已创建美摄支持的特效，使用中间层来渲染。比如背景分割功能（需提前初始化人脸和分割模型），实现如下：

```java
//创建背景分割
NvsRational aspectRatio = new NvsRational(9, 16);
NvsVideoEffect mSegmentationEffect = NvsEffectSdkContext.getInstance().createVideoEffect("Segmentation Background Fill", aspectRatio);
mSegmentationEffect.setIntVal("Stretch Mode", 2);
mSegmentationEffect.setMenuVal("Segment Type", "Half Body");
mSegmentationEffect.setColorVal("Background Color", new NvsColor(0, 1, 0, 1));

//添加渲染
NveEffectKit.getInstance().addEffect(mSegmentationEffect);

//根据索引添加渲染
NveEffectKit.getInstance().insertEffect(mSegmentationEffect,0);

//移除创建的特效
NveEffectKit.getInstance().removeEffect(mSegmentationEffect);
```

---

#### 包安装

上述的内容中基本都涉及包安装，官网有安装说明

> [美摄SDK For Android: 素材包安装 (meishesdk.com)](https://www.meishesdk.com/android/doc_ch/html/content/assetsPackageInstall_8md.html)

可以使用已经封装好的工具类（NvAssetPackageManagerUtil）示例代码：

```java
//packagePath 此处为模拟路径，替换为实际资源包路径
String packagePath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh";
// 资源包授权文件路径
String packageLicPath = "assets:/beauty/shape/shapePackage/63BD3F32-D01B-4755-92D5-0DE361E4045A.1.lic";
//如果资源的结尾是facemesh则类型为ASSET_PACKAGE_TYPE_FACE_MESH，如果是warp则为ASSET_PACKAGE_TYPE_WARP
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.facemesh
int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
//63BD3F32-D01B-4755-92D5-0DE361E4045A.1.warp
// int packageType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
//shapePackageID：资源包ID(包需要安装,安装见下面安装使用)
String shapePackageID = NveAssetPackageManagerUtil.installFxPackage(packagePath, packageLicPath, packageType);
```

其中需要重点关注的参数有：

1、packagePath-- 安装包的路径，可以为assets路径或者本地绝对路径

2、packageLicPath-- 安装包的授权文件路径

3、packageType-- 安装包类型，具体类型见：[美摄SDK For Android: com.meicam.sdk.NvsAssetPackageManager类 参考 (meishesdk.com)](https://www.meishesdk.com/android/doc_ch/html/content/classcom_1_1meicam_1_1sdk_1_1NvsAssetPackageManager.html)

---

#### 渲染

####### 1.RenderCore相关初始化

```java
//注：需提前初始化SDK
NveEffectKit.getInstance().initialize();
```

####### 2.NveRenderInput说明

NveRenderInput主要包括渲染配置（NveRenderConfig），纹理（NveTexture），Buffer（NveImageBuffer），图像的格式（pixelFormat）。具体参数如下：

（1）NveRenderConfig相关参数，包括相机朝向（cameraOrientation）和渲染模式（NveRenderMode）

| NveRenderMode                                 | 说明              |
| --------------------------------------------- | --------------- |
| NveRenderConfig.NveRenderMode.TEXTURE_TEXTURE | 纹理入，纹理出         |
| NveRenderConfig.NveRenderMode.BUFFER_TEXTURE  | Buffer入，纹理出     |
| NveRenderConfig.NveRenderMode.BUFFER_BUFFER   | Buffer入，Buffer出 |

（2）NveTexture相关参数

| 参数               | 说明                          |
| ---------------- | --------------------------- |
| textureId        | 纹理ID                        |
| mirror           | 是否水平翻转，OES纹理转Texture 2D纹理需要 |
| NveSize          | 纹理宽高                        |
| NveTextureType   | 纹理类型                        |
| NveTextureLayout | 纹理方向                        |

| NveTextureType                   | 说明           |
| -------------------------------- | ------------ |
| NveTextureType.NV_COMMON_TEXTURE | 普通纹理         |
| NveTextureType.NV_OES_TEXTURE    | OpenGL OES纹理 |

| NveTextureLayout              | 说明   |
| ----------------------------- | ---- |
| NveTextureLayout.UP_SIDE_DOWN | 上下颠倒 |
| NveTextureLayout.DOWN_SIDE_UP | 正常   |

（3）NveImageBuffer相关参数

| 名称              | 说明                                          |
| --------------- | ------------------------------------------- |
| data            | Buffer数据                                    |
| NveSize         | Buffer宽高                                    |
| mirror          | 是否水平翻转                                      |
| displayRotation | 当前图像需要旋转的角度                                 |
| rowPitchY       | 图像每行在Frame中占的字节数，如果图像格式是NV21,YUV420, 则指Y平面  |
| rowPitchUV      | 图像每行在Frame中占的字节数 一般是指UV平面,如果格式为RGBA,这个量没有意义 |

（4）pixelFormat图像格式，其封装在NvFormatType中，具体对应可参考官网[视频帧像素格式]([美摄SDK For Android: com.meicam.sdk.NvsVideoFrameInfo类 参考](https://www.meishesdk.com/android/doc_ch/html/content/classcom_1_1meicam_1_1sdk_1_1NvsVideoFrameInfo.html#a879ad4bf8e42df9381768f5aff2693c8))

####### 3.NveRenderOutput说明

NveRenderOutput主要包括渲染结果（NveRenderError），输出纹理（NveTexture，参数同上），输出Buffer（NveImageBuffer，参数同上）。其渲染结果参数如下

| 名称                                 | 说明                      |
| ---------------------------------- | ----------------------- |
| NveRenderError.NO_ERROR            | 成功                      |
| NveRenderError.ERROR_UNKNOWN       | 未知错误                    |
| NveRenderError.INVALID_TEXTURE     | 无效的纹理                   |
| NveRenderError.INVALID_INPUT_PARAM | 无效的输入参数，针对NvRenderInput |

###### 4.渲染

```java
 //输入配置
 NveRenderInput  mRenderInput = new NveRenderInput();
 mRenderInput.setPixelFormat(NveFormatType.VIDEO_FRAME_PIXEL_FROMAT_NV21.getType());
 NveRenderConfig config = new NveRenderConfig()
                 .setRenderMode(NveRenderConfig.NveRenderMode.TEXTURE_TEXTURE)
                 .setCameraOrientation(mCameraProxy.getOrientation()).build();
 mRenderInput.setConfig(config);

 //输入纹理
 NveTexture nvTexture = new NveTexture();
 nvTexture.setTextureId(displayTex);
 Texture.setTextureType(NveTextureType.NV_OES_TEXTURE);
 nvTexture.setSize(new NveSize(texWidth, texHeight));
 nvTexture.setMirror(mCameraProxy.isFlipHorizontal());
 mRenderInput.setTexture(nvTexture);

 //输入Buffer
 NveImageBufferbuffer = new NveImageBuffer();
 buffer.setData(data);
 buffer.setSize(new NveSize(bufferWidth, bufferHeight));
 buffer.setDisplayRotation(mOrientation);
 buffer.setMirror(mCameraProxy.isFlipHorizontal());
 mRenderInput.setImageBuffer(buffer);

 //渲染
 NveRenderOutput renderOutput = mNvEffectKit.renderEffect(mRenderInput);

   ......

 if (null != renderOutput) {
      //回收render out
      NveEffectKitt.recycleOutput(renderOutput);
 }
```

###### 5.资源释放

在退出或者不再需要渲染时，需要释放相关资源，可调用下面的方法

```java
 NveEffectKit.getInstance().cleanUp();
```

注意：该方法需要在GLContext所在的线程调用

#### 销毁

在页面退出或者应用杀死的情况下进行SDK的销毁，可调用下面的方法

```java
NveEffectKit.getInstance().destroy();
```

注意：如果是在某个页面退出时进行销毁，那么在其他地方还需要使用SDK，那么在使用前就需要重新初始化SDK，即调用init方法

#### 常见问题
###### 1.使用Android Studio较高版本时run apk失败，需要修改Gradle JDK版本为 jdk 11
>Settings->Build,Execution,Deployment->Build Tools->Gradle->Gradle JDK (`java 11`)

*类似错误：*
```log
FAILURE: Build completed with 2 failures.

1: Task failed with an exception.
-----------
* What went wrong:
Execution failed for task ':app:processDebugMainManifest'.
> Unable to make field private final java.lang.String java.io.File.path accessible: module java.base does not "opens java.io" to unnamed module @16a1c82d

* Try:
Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Exception is:
org.gradle.api.tasks.TaskExecutionException: Execution failed for task
Caused by: java.lang.reflect.InaccessibleObjectException: Unable to make field private final java.lang.String java.io.File.path accessible: module java.base does not "opens java.io" to unnamed module @16a1c82d
```
###### 2.模型中face240和face106有什么区别？
> 240和160指的是人脸模型的点位数量，240效果更佳。`160点位不支持美妆`。

###### 3.普通磨皮，高级磨皮1，高级磨皮2，高级磨皮3有什么区别？
> `高级磨皮1`是`Android`端标准效果，`高级磨皮2`是`iOS`端标准效果，`高级磨皮3`是`男性`效果.
> [详情见文档：AR Scene](https://www.meishesdk.com/android/doc_ch/html/content/FxNameList_8md.html) *Advanced Beauty Type*

###### 4.美颜A，美颜B有什么区别？
> 实现方式不同，`美颜B`使用`Lut`文件。
> [详情见文档：AR Scene](https://www.meishesdk.com/android/doc_ch/html/content/FxNameList_8md.html) *Whitening Lut File*

###### 5.是否支持自定义GLSurfaceView/相机预览？
> 代码中示例供参考，如果用户已有相关实现，可以提供要渲染的纹理或者buffer 数据即可。详情可咨询[美摄技术支持](https://www.meishesdk.com/)

###### 6.导入项目后，渲染无效果或黑屏？
> 检查项目中`lic`文件与`applicationId`是否绑定。详情可咨询[美摄商务](https://www.meishesdk.com/)

###### 7.已接入NvAndroidStreamingSdk.jar，冲突如何处理？
> 删除项目中原`NvAndroidStreamingSdk.jar`，重新依赖`NveEffectKit.aar`。

## Source: `md_ch/AR_Scene_7_243.md`

Purpose: AR scene 7.2.43 Android usage.

Primary title: AR Scene 技术文档

Doc lead: AR Scene是美摄SDK中用于展示AR效果的特技，现支持道具，美颜，美型，美妆等功能。

### AR Scene 技术文档

### 1. 概述

AR Scene是美摄SDK中用于展示AR效果的特技，现支持道具，美颜，美型，美妆等功能。

### 2. 使用

#### 2.1 资源加载

AR Scene 中由于使用了人体检测相关的技术，在程序初始化阶段需要加载一些模型以及数据包资源。

##### 2.1.1 模型加载

首先判断该SDK是否包含AR功能，不包含AR功能的SDK无法加载人体检测模型。

```java
// 检测SDK包是否有AR模块
bool hasAR = NvsStreamingContext.hasARModule();
```

人体检测模型的加载通过调用 [InitHumanDetection](`com.meicam.sdk.NvsStreamingContext.initHumanDetection`) 和 [InitHumanDetectionExt](`com.meicam.sdk.NvsStreamingContext.initHumanDetectionExt`) 实现。[InitHumanDetection](`com.meicam.sdk.NvsStreamingContext.initHumanDetection`) 指定主模型的加载，只能调用一次。[InitHumanDetectionExt](`com.meicam.sdk.NvsStreamingContext.initHumanDetectionExt`) 指定扩展模型的加载，可以通过多次调用加载多个扩展模型。一般情况下我们使用人脸点位模型作为主模型。

如下是加载人脸点位模型与眼眼球轮廓模型的示例。

```java
// 人脸点位模型加载，使能“视频检测模式”
boolean initSuccess = NvsStreamingContext.initHumanDetection(
        MSApplication.getContext(),
        landmarksModelPath,
        null,
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK |
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION |
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE);


// 眼球轮廓模型加载，使能“视频检测模式”，与人脸模型的检测模式对齐
initSuccess = NvsStreamingContext.initHumanDetectionExt（
        MSApplication.getContext(),
        eyeballModelPath,
        null,
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK |
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE);
```

在程序销毁时还需调用 [closeHumanDetection](`com.meicam.sdk.NvsStreamingContext.closeHumanDetection`) 来卸载安装过的所有模型以及数据包。

```java
NvsStreamingContext.closeHumanDetection();
```

注：

- 模型初始化操作涉及文件拷贝耗时操作，建议放在子线程去出处理。

- **modelFilePath指定模型加载路径，不支持ASSET路径；**

- 使用美摄自研点位SDK licenseFilePath为空；

- features项指定模型类型以及所有支持的检测模式；

- 所有[InitHumanDetection](`com.meicam.sdk.NvsStreamingContext.initHumanDetection`) 和[InitHumanDetectionExt](`com.meicam.sdk.NvsStreamingContext.initHumanDetectionExt`) 调用中的检测模式，建议设置成相同模式，不同检测模式会影响程序运行效率。

###### 2.1.1.1 模型类型

模型分为两种，普通模型与复合模型。普通模型只支持单一的功能，复合模型可以支持多项功能。例如人脸检测模型就是复合模型，同时支持点位检测以及人脸动作检测。

SDK现支持具体如下：

| 模型        | 命名                         | 复合模型 | Flag                                                                                                                                                                                                                                          |
| --------- | -------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 106人脸检测模型 | ms_face_vX.X.X.model       | 是    | [HUMAN_DETECTION_FEATURE_FACE_LANDMARK ](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK`) \| [HUMAN_DETECTION_FEATURE_FACE_ACTION](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION`) |
| 240人脸检测模型 | ms_face240_vX.X.X.model    | 是    | [HUMAN_DETECTION_FEATURE_FACE_LANDMARK ](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK`) \| [HUMAN_DETECTION_FEATURE_FACE_ACTION](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION`) |
| 眼球轮廓检测模型  | ms_eyecontour_vX.X.X.model | 否    | [HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK`)                                                                                                                  |
| 表情检测模型    | ms_avatar_vX.X.X.model     | 否    | [HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION`)                                                                                                                |
| 手势检测模型    | ms_hand_vX.X.X.model       | 是    | [HUMAN_DETECTION_FEATURE_HAND_LANDMARK](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK`) \| [HUMAN_DETECTION_FEATURE_HAND_ACTION](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION`)  |
| 背景分割模型    | ms_humanseg_vX.X.X.model   | 否    | [HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND`)                                                                                                    |
| 天空分割模型    | ms_skyseg_vX.X.X.model     | 否    | [HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY`)                                                                                                                  |

注：

- 106人脸检测模型与240人脸检测模型只能选用一个；

- 可以使用240模型，但只使用其中的106点位检测功能，不影响检测效率；

- 对于复合模型，某个功能项没有或上，那么，AR Scene或其他使用到该功能项的特技将无法正常运行。

###### 2.1.1.2 检测模式

检测模式：

| 模式      | Flag                                                                                                                       | 描述                                     |
| ------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| 视频检测模式  | [HUMAN_DETECTION_FEATURE_VIDEO_MODE](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE`)           | 适用于拍摄场景，效率最高，视频间检测结果连续，但首帧通常无检测出来      |
| 图片检测模式  | [HUMAN_DETECTION_FEATURE_IMAGE_MODE](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE`)           | 适用于编辑模式，效率一般，检测结果不连续，首帧能够检测出来          |
| 半图片检测模式 | [HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`) | 适用于拍摄模式与编辑模式，效率较高，检测结果连续，首帧能够检测出来线程模式： |

在调用[InitHumanDetection](`com.meicam.sdk.NvsStreamingContext.initHumanDetection`) 和 [InitHumanDetectionExt](`com.meicam.sdk.NvsStreamingContext.initHumanDetectionExt`) 时features参数需要或上所有支持的检测模式。同时在AR Scene使用时，需要通过 [setDetectionMode](`com.meicam.sdk.NvsARSceneManipulate.setDetectionMode`) 指定该特技实例具体使用哪种检测模式。

例如，如下代码在模型加载阶段同时或上了“视频检测模式”和“图片检测模式”，在 AR Scene 特技使用时指定检测模型为“图片检测模式”。

```java
// 人脸点位模型加载，同时使能“视频检测模式”与“图片检测模式”
boolean initSuccess = NvsStreamingContext.initHumanDetection(
        MSApplication.getContext(),
        landmarksModelPath,
        null,
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK |
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION |
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE|
        NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE
);

....

// AR Scene 特技选择使用“图片检测模式”进行检测
NvsARSceneManipulate arSceneManipulate = mArSceneEffect.getARSceneManipulate();
if (arSceneManipulate != null) {
    arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
```

##### 2.1.2 数据包加载

数据包使用 [setupHumanDetectionData](`com.meicam.sdk.NvsStreamingContext.setupHumanDetectionData`) 来加载。如下代码展示美妆数据包的加载过程。

```java
// 加载美妆数据包
boolean setupSuccess = NvsStreamingContext.setupHumanDetectionData(
        NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_MAKEUP2,
        makeupDataFile);
```

数据包类型：

| 数据包               | 命名                        | 类型                                                                                                                             | 描述                                      |
| ----------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| 假脸数据包             | fakeface.dat              | [HUMAN_DETECTION_DATA_TYPE_FAKE_FACE](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE`)             | 假脸数据，用于AR Scene的人脸道具中，道具紧贴人脸，随面部表情变化而变化 |
| 美妆数据包（Deprecated） | makeup2_240_vX.X.X.dat    | [HUMAN_DETECTION_DATA_TYPE_MAKEUP2](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_MAKEUP2`)                 | 美妆相关数据，用于美妆以及美妆道具中（已废弃, 需替换成人脸通用数据包）    |
| 人脸通用数据包           | facecommon_vX.X.X.dat     | [HUMAN_DETECTION_DATA_TYPE_FACE_COMMON](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON`)         | 人脸通用数据包，用于美妆以及高级美颜                      |
| 高级美颜数据包           | advancedbeauty_vX.X.X.dat | [HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY](`com.meicam.sdk.NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY`) | 高级美颜相关数据                                |

注：使用美妆需设置人脸通用数据包，使用高级颜需同时设置人脸通用数据包以及高级美颜数据包。

#### 2.2 特技使用

##### 2.2.1 特技创建

AR Scene 是内建特技，对应特技名称为“AR Scene”。可以使用美摄SDK内建特技的标准创建方式进行创建。例如拍摄模式下：

```java
NvsVideoFx mArSceneEffect = mStreamingContext.appendBuiltinCaptureVideoFx("AR Scene");
```

<a id="settings"></a>

##### 2.2.2 其他设置

检测类特技，如AR Scene需要进行buddy buffer相关设置。分为以下几类情况：

###### 拍摄模式

预览开启时需要设置buddy buffer相关flags，[STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`)。

```java
mStreamingContext.startCapturePreview(mCurrentDeviceIndex, captureResolutionGrade,
        NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |
                NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME |
                NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE |
                NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null);
```

###### 编辑模式

检测类特效推荐以 Raw Filter 形式添加，效率更高。

播放时需要分别设置buddy buffer相关flags，[STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`)。

需要注意的是，如果特技是以 Raw Filter 的形式添加，flags 上才能够且必须或上[STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`)，否则会造成部分效果异常。

```java
mStreamingContext.playbackTimeline(mTimeLine, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true,
        NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME |
        NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME |
        NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE);
```

Seek时需要分别设置buddy buffer相关flags。[STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`)。

需要注意的是，如果特技是以 Raw Filter 的形式添加，flags 上才能够且必须或上[STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`)，否则会造成部分效果异常。

```java
mStreamingContext.seekTimeline(mTimeLine, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                seekShowMode |
                NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME |
                STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
```

Compile时需要分别设置buddy buffer相关flags。[STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`)。

需要注意的是，如果特技是以 Raw Filter 的形式添加，flags 上才能够且必须或上[STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME](`com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`)，否则会造成部分效果异常。

```java
mStreamingContext.compileTimeline(timeline, startTime, endTime, compileVideoPath, videoResolutionGrade, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH,
                 encoderFlag |
                 NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME |
                 NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
```

#### 2.3 特技功能

##### 2.3.1 道具

AR Scene 道具的应用，需要先安装道具包，再把返回的包ID设置给 AR Scene 特技。例如：

```java
// 道具安装
NvsAssetPackageManager assetPackageManager = mStreamingContext.getAssetPackageManager();
StringBuilder sceneId = new StringBuilder();
String packagePath = "assets:/arface/084A6EC1-43AB-40EF-BBD5-D83F692B011B.3.arscene";
int ret = assetPackageManager.installAssetPackage(packagePath , null,
        NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE, true, sceneId);

// 设置道具效果
mArSceneEffect.setStringVal("Scene Id", sceneId);
```

取消道具“Scene Id”传空。

```java
// 取消道具效果
mArSceneEffect.setStringVal("Scene Id", “”);
```

注：道具包使用前，需加载该包要求的人体检测模型以及数据包。各个包的具体要求参见美摄素材平台。

##### 2.3.2 美颜

美颜功能分为普通美颜与高级美颜，普通美颜不需要人体检测的支持，高级美颜需要。

**高级美颜与普通美颜都有磨皮的功能，如果同时开启，高级美颜的磨皮效果会覆盖普通美颜效果。**

###### 2.3.2.1 普通美颜

普通美颜功能包括：磨皮，Lut，美白，红润，锐化等功能。

具体参数参见 [美颜参数](`AR_SCENE_BEAUTY_PARAMS`)

###### 2.3.2.2 高级美颜

高级美颜功能包括：高级磨皮，祛黑眼圈，祛法令纹，眼亮，白牙，哑光，人脸Lut，清晰等功能。

具体参数参见 [高级美颜参数](`AR_SCENE_ADVANCED_BEAUTY_PARAMS`) 。

**高级美颜要求加载106人脸点位检测模型或者240人脸点位检测模型，二者在效果上有细微差别。同时需设置人脸通用数据包以及高级美颜数据包。**

##### 2.3.3 美型

美型功能能够对面部细节进行一些微调。具体参数参见 [美型参数 (Warp)](`AR_SCENE_FACE_WARP_PARAMS`)与[美型参数 (Face Mesh)](`AR_SCENE_FACE_MESH_PARAMS`) 。

**目前支持两套美型方案，Warp以及Face Mesh，通常情况下，我们推荐使用Face Mesh，只有头部缩放操作建议使用Face Warp。**

**美型要求加载106人脸点位检测模型或者240人脸点位检测模型。二者在效果上没有差别。**

美型的各项调节有默认的效果，同时也支持自定义美型包的形式。

如果使用美型包，需要先安装，再把返回的包ID设置给对应的包ID参数。

##### 2.3.3.1 美型(Warp)

```java
// 自定义头部缩放美型包安装
NvsAssetPackageManager assetPackageManager = mStreamingContext.getAssetPackageManager();
StringBuilder warpId = new StringBuilder();
String packagePath = "assets:/facewarp/084A6EC1-43AB-40EF-BBD5-D83F692B011B.3.warp";
int ret = assetPackageManager.installAssetPackage(packagePath , null,
        NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP, true, warpId );

// 设置自定义头部缩放效果
mArSceneEffect.setStringVal("Head Size Warp Custom Package Id", warpId );
```

如果要取消自定义美型效果，则对应包ID参数传空。

```java
// 设置自定义头部缩放效果
mArSceneEffect.setStringVal("Head Size Warp Custom Package Id", "");
```

##### 2.3.3.2 美型(Face Mesh)

```java
// 自定义大眼美型包安装
NvsAssetPackageManager assetPackageManager = mStreamingContext.getAssetPackageManager();
StringBuilder faceMeshId = new StringBuilder();
String packagePath = "assets:/facemesh/084A6EC1-43AB-40EF-BBD5-D83F692B011B.3.facemesh";
int ret = assetPackageManager.installAssetPackage(packagePath , null,
        NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH, true, faceMeshId );

// 设置自定义大眼效果
mArSceneEffect.setStringVal("Face Mesh Eye Size Custom Package Id", faceMeshId );
mArSceneEffect.setIntVal("Head Size Warp Strategy", 0x7FFFFFFF );
```

如果要取消自定义美型效果，则对应包ID参数传空。

```java
// 设置自定义大眼效果
mArSceneEffect.setStringVal("Face Mesh Eye Size Custom Package Id", "");
```

##### 2.3.4 美妆

美妆分为：单妆和妆容。

**美妆要求加载240人脸点位检测模型，如果使用美瞳也还需要加载眼球轮廓检测模型。**

**美妆要求加载人脸通用数据包。**

###### **2.3.4.1 单妆**

单妆是单一的美妆效果，现支持的有口红、眉毛、眼影、睫毛、眼线、腮红、高光、修容。

**每个单妆需要安装对应单妆包才可使用。**

如下是口红包的安装与使用过程。

```java
// 口红包安装
NvsAssetPackageManager assetPackageManager = mStreamingContext.getAssetPackageManager();
StringBuilder makeupId = new StringBuilder();
String makeupPath="assets:/makeup/07E4CE0F-3AEA-4510-8C23-9267522B7BFE.1.makeup";
int ret = assetPackageManager.installAssetPackage(makeupPath, null,
        NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP , true, uuid);

// 口红应用
mArSceneEffect.setColorVal("Makeup Lip Color", new NvsColor(1, 0, 0, 1));
mArSceneEffect.setFloatVal("Makeup Lip Intensity", 1);
mArSceneEffect.setStringVal("Makeup Lip Package Id", makeupId);
```

###### 2.3.4.2 妆容

妆容是若干单妆、美颜、美型、微整型、滤镜的整体效果。对于妆容的接入，美摄提供一套中间层的接口，具体可参考sdkdemo。

### 3. FAQ

**问：为什么道具没有效果？**

答：请做如下确认：

1. SDK是否支持美摄的AR功能；

2. 是否有相应功能的授权；

3. 道具所需检测模型是否加载成功；

4. 如果是假脸道具，假脸数据包是否加载成功；

5. 如果是美妆道具，美妆数据包是否加载成功；

6. buddy相关flags是否设置，见文中[2.2.2](#settings)；

7. 道具包是否安装成功；

8. 是否 AR Scene 指定的检测模式在模型加载阶段没有支持；

9. 如果是Effect Sdk，渲染时传入的物理角度是否正确；

10. 图像中人脸是不是过小，目前美摄检测模型支持的最小人脸屏占比为1%；

**问：为什么高级美颜，美型没有效果？**

答：请做如下确认：

1. SDK是否支持美摄的AR功能；

2. 是否有相应功能的授权；

3. 人脸检测模型是否加载成功；

4. 人脸通用数据包和高级美颜数据包是否设置（适用高级美颜没效果的情况）；

5. buddy相关flags是否设置，见文中[2.2.2](#settings)；

6. 开关是否开启，各子项强度是否大于0；

7. 是否 AR Scene 指定的检测模式在模型加载阶段没有支持；

8. 如果是Effect Sdk，渲染时传入的物理角度是否正确；

9. 图像中人脸是不是过小，目前美摄检测模型支持的最小人脸屏占比为1%；

**问：为什么单妆没有效果？**

答：请做如下确认：

1. SDK是否支持美摄的AR功能；

2. 是否有相应功能的授权；

3. 240人脸检测模型是否加载成功，**如果使用美瞳，眼球轮廓检测模型是否加载成功**；

4. 美妆数据包是否加载成功；

5. buddy相关flags是否设置，见文中[2.2.2](#settings)；

6. 美妆开关是否开启，美妆强度是否不为0，各子项强度是否大于0；

7. 美妆包是否安装成功；

8. 是否 AR Scene 指定的检测模式在模型加载阶段没有支持；

9. 如果是Effect Sdk，渲染时传入的物理角度是否正确；

10. 图像中人脸是不是过小，目前美摄检测模型支持的最小人脸屏占比为1%；

**问：为什么添加AR Scene后，添加的其他特效没有效果？**

答：在 [单缓冲](`AR_SCENE_SINGLE_BUFFER_PARAMS`) 模式下，AR Scene之前的特效会失效，需要其他特效移到AR Scene之后，或者改用双缓冲模式。

**问：想要自定义美型效果怎么办？**

答：AR Scene 支持自定义美型包，请联系美摄设计同学定制。

**问：如何确定检没检测到人体信息？**

答：通过 [setARSceneCallback](`com.meicam.sdk.NvsARSceneManipulate.setARSceneCallback`) 设置检测回调，查看检测到的目标个数。前提是，该荐功能已授权。

**问：低端机效果卡顿怎么办？**

答：需要对低端机做适配，可选配置如下：

1. 背景分割使用快速模型；

2. 禁用哑光效果；

3. 禁用[单缓冲](`AR_SCENE_SINGLE_BUFFER_PARAMS`)模式；

4. 通过 [Unified Max Faces](`ARSCENE_MAX_FACES_PARAMS`) 和 [Max Faces Respect Min](`ARSCENE_MAX_FACES_RESPECT_MIN_PARAMS`) 限制最大检测人脸数；

5. 禁用美瞳；

## Source: `md_ch/Segment.md`

Purpose: Segmentation usage.

Primary title: 背景分割特效 技术文档

Doc lead: 背景分割特效 技术文档

### 背景分割特效 技术文档


背景分割特效 技术文档
================

**1.说明：**

* 背景分割特效可以以道具包的形式使用，也可以以SDK内建特技的形式使用，但前提是都需要初始化**“人像背景分割模型”**，本文档以SDK内建特技的形式进行讲述。
* 背景分割特效既可以在**拍摄**中使用，也可以在**编辑**中使用，两者的应用方式不同，文档会详细说明
* CaptureScene只能在**拍摄**中使用


**2.背景分割的使用**

* 初始化人像背景分割模型。在拍摄中，相机为前置摄像头时可设置使用“半身分割模型”，是后置摄像头时可设置使用“全身分割模型”。在编辑中，设置使用“全身分割模型”。
```java
/**
 * 人像背景全身分割模型
 * Portrait Background Segmentation Model
 */
String segPath = "assets:/facemode/ms/ms_humanseg_v1.0.7.model";
boolean segSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
        segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);
Logger.e(TAG, "ms segSuccess-->" + segSuccess);

 /**
 * 人像背景半身分割模型
 * Half-length portrait background segmentation model, the effect is better when half-length
 */
String halfBodyPath = "assets:/facemode/ms/ms_halfbodyseg_v1.0.6.model";
boolean halfBodySuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
        halfBodyPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_HALF_BODY);
Logger.e(TAG, "ms halfBodySuccess-->" + halfBodySuccess);
```

* 背景分割是内建特效，创建如下：
```java
拍摄：
      //创建分割特技
      NvsCaptureVideoFx  mSegmentEffect = mStreamingContext.appendBuiltinCaptureVideoFx("Segmentation Background Fill");
      /*
       * 根据前置后置摄像头判断使用对应模型
       * 前置：半身模型
       * 后置：全身模型
       */
      if (mCurrentDeviceIndex == 0) {
          mSegmentEffect.setMenuVal("Segment Type", "Background");
      } else if (mCurrentDeviceIndex == 1) {
          mSegmentEffect.setMenuVal("Segment Type", "Half Body");
      }
      /*1:铺满  0：自适应*/
      mSegmentEffect.setIntVal("Stretch Mode", 1);

 编辑：
       //创建分割特技
       NvsVideoFx mSegmentEffect = clip.appendRawBuiltinFx("Segmentation Background Fill");
       mSegmentEffect.setMenuVal("Segment Type", "Background");
       /*1:铺满（可能会被拉伸）  0：自适应*/
       mSegmentEffect.setIntVal("Stretch Mode", 1);
```
 设置背景颜色
```java
mSegmentEffect.setColorVal("Background Color", new NvsColor(0.0f, 1.0f, 0.0f, 0.0f));
```
设置图片背景，目前支持设置图片
```java
   //filePath 图片的绝对路径
   mSegmentEffect.setStringVal("Tex File Path", filePath);
```
移除分割特效
```java
 拍摄：
  if (null != mSegmentEffect) {
    mStreamingContext.removeCaptureVideoFx(mSegmentEffect.getIndex());
  }

 编辑：
 if (null != mSegmentEffect) {
    clip.removeRawFx(mSegmentEffect.getIndex());
 }
```
>注：在编辑中应用背景分割特技后，需要在Seek、播放、导出添加对应的flag，即：NvsStreamingContext.STREAMING_ENGINE_XXX_FLAG_BUDDY_ORIGIN_VIDEO_FRAME

 >注：该内建分割特技目前不支持设置视频背景，如果需要，则需要使用captureScene素材包

* CaptureScene的使用。其背景既支持设置图片，也支持设置视频，使用如下：

 安装captureScene素材包
 ```java
 String path = "assets:/capturescene/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1.capturescene";
  StringBuilder sb = new StringBuilder();
int inCode = mStreamingContext.getAssetPackageManager().installAssetPackage(path, null
                , NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE, true, sb);
capturesceneId = sb.toString();
 ```

 创建背景分割特技（**“Segmentation Background Fill”**），同上创建（**必需**）

 调用**applyCaptureScene**添加
```java
  //创建拍摄场景资源信息
  NvsCaptureSceneInfo sceneInfo = new NvsCaptureSceneInfo();
  //片段数据集
  List<NvsCaptureSceneInfo.ClipData> clipDataList = new ArrayList<>();
  NvsCaptureSceneInfo.ClipData clipData = new NvsCaptureSceneInfo.ClipData();
  //视频使用，设置pan和scan
  clipData.scan = 1;
  //图片使用，设置填充模式，有："fit","letterBox","crop","stretch"
  clipData.imageFillMode = NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP;
  //图片或者视频路径
  clipData.mediaPath = filePath;
  clipDataList.add(clipData);
  //设置后景场景
  sceneInfo.foregroundClipArray = clipDataList;
  //应用拍摄场景资源包
  mStreamingContext.applyCaptureScene(mBgSegPackageId, sceneInfo);
```
移除当前拍摄场景
```java
mStreamingContext.removeCurrentCaptureScene();
```

## Source: `md_ch/Mask_Generator.md`

Purpose: Mask generator usage.

Primary title: Mask Generator 技术文档

Doc lead: Mask Generator文档

### Mask Generator 技术文档


Mask Generator文档
==================

Mask
Generator，中文意为蒙版。视频编辑技术的增强，需要精细化视频处理。视频技术增强的一个要求是加强界面部分区域的编辑与控制，强调细腻的视频处理，蒙版技术为局部精细化处理提供支持。

[image omitted: media/c79a6ba32d6b2975060679728fba5d7c.png]

SDK提供了方便的编程接口，用户根据自己的需求，快捷实现Mask
Generator。开发者可以根据客观需求，开发广阔应用。

蒙版包括字幕蒙版和形状蒙版，两者编程方式不同。形状蒙版需要用户定义区域，字幕蒙版不需要用户定义区域。后面主题会有介绍。下图是蒙版的两大组成部分。

[image omitted: media/7671b6f3144576ba0c39fcc58e0c0df9.png]

形状蒙版包含：线性、镜面、圆形、矩形、心形，星形。蒙版整体构成如下：

[image omitted: media/e1ceece3674f24bcf7c35e5fe3732ea6.png]

1、编程原理
-----------

Mask Generator技术属于视频特效范围，通过视频特效进行控制。

首先开启Mask Generator特效；设定区域范围；应用蒙版特效。

Mask
Generator属于对视频区域的精细化处理，必然对视频区域范围进行指定。对区域进行数学化的描述，是Mask
Generator编程的难点与核心所在。

技术人员通过窗口的范围、蒙版层的范围、中心点、数学公式等因素，最终决定蒙版的区域。

2、SDK支持
----------

下面接口参考api相关文档：Matrix、Path、PointF、Rect、RectF、NvsVideoFx、NvsMaskRegionInfo、NvsPosition2D、RegionInfo。

3、参数ID
---------

通过参数ID，对蒙版属性进行控制。参数ID应用和AR Scene类似。

| **序号** | **参 数**                    | **类 型** | **最 大 值** | **最 小 值** | **默 认 值** | **说 明**        |
|----------|------------------------------|-----------|--------------|--------------|--------------|------------------|
| 001      | Region Info                  | ARBDATA   |              |              |              | 区域信息         |
| 002      | Feather Width                | FLOAT     | 1000.0       | 0.0          | 0.0          | 羽化宽度         |
| 003      | Keep RGB                     | BOOL      |              |              | FALSE        | 保持RGB          |
| 004      | Inverse Region               | BOOL      |              |              | FALSE        | 区域反转         |
| 005      | Coordinate System            | STRING    |              |              | ndc          | 坐标类型         |
| 006      | Feather Compensation         | BOOL      |              |              | True         | 羽化补偿         |
| 007      | Text Mask Description String | STRING    |              |              |              | 文本遮罩描述文件 |
| 008      | Is Caption                   | BOOL      |              |              | false        | 是否是字幕       |

4、NvsMaskReginInfo
-------------------

应用Mask
Generator的时间，核心是生成蒙版区域信息对象。也即NvsMaskRegionInfo对象。4.2主题中，会讲述典型区域对象的生成。

Mask Generator结构，参考下图。详细描述参考官网文档。

[image omitted: media/afa3694ae8307b1b33b1ef9eb9fa130c.png]

区域对象的生成，是坐标定位的结果。美摄SDK坐标系分为如下两种。

[image omitted: media/a4dfe771ebbe40e81f5b470503083067.png]

#### 4.1、区域对象生成说明

第一步：生成NvsMaskReginInfo对象。

第二步：生成内部类ReginInfo对象。

第三步：给ReginInfo对象进行相关设置。

第四步：把ReginInfo对象注入到NvsMaskReginInfo对象中。

#### 4.2、典型Mask区域NvsMaskRegionInfo对象生成（详细代码参考this skill's demo-derived references）

开发过程中，技术人员如果能确定坐标点精确位置，直接形成NvsMaskRegionInfo对象，来实现蒙版效果。

也可以通过导入的视频宽高，依据视频属性、中心点、蒙版层大小等因素，来计算精确位置。本文档案例就是根据相关属性进行定位。

本主题提供的技术思路，作为形状蒙版的技术参考。技术人员可以实现更加炫酷的蒙版效果。

#### 4.2.1、线性蒙版

由于线性蒙版形状特点，相对简单。根据相关属性，得到点数组，根据点数组，形成蒙版对象。

下面函数通过视频中心点，蒙版区域宽高和角度形成蒙版边界点数组。

```java
A、点数组形成
/**
 * 线性蒙版使用 为了达到旋转之后的效果
 * Linear mask is used in order to achieve the effect after rotation
 * @param center 锚点坐标
 * @param angle  旋转角度
 * @return 新坐标集
 */
public static PointF[] buildLineMaskPoint(PointF center, int maskWidth, int maskHeight, float angle) {
    PointF leftTopPoint = new PointF(center.x - maskWidth, center.y - maskHeight);

    PointF rightTopPoint = new PointF(center.x + maskWidth, center.y - maskHeight);

    PointF rightBottomPoint = new PointF(center.x + maskWidth, center.y);

    PointF leftBottomPoint = new PointF(center.x - maskWidth, center.y);

    return new PointF[]{getPointByAngle(leftTopPoint, center, angle), getPointByAngle(rightTopPoint, center, angle),
            getPointByAngle(rightBottomPoint, center, angle), getPointByAngle(leftBottomPoint, center, angle)};
}


B、根据上面函数形成的点数组，及流媒体窗口相关信息与实际显示的宽高，生成线性蒙版区域信息对象。
/**
 * 构建蒙版特效区域  多边形区域
 * Build local special effects area Polygonal area
 * @param pointFList 点位集合
 * @param size
 * @return
 */
public static NvsMaskRegionInfo buildPolygonMaskRegionInfo(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {
    List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFList, liveWindow, size);
    //蒙版特效区域信息
    NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
    //设置类型
    // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
    // 多边形 MASK_REGION_TYPE_POLYGON
    NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);
    //参数意义
    regionInfo.setPoints(nvsPosition2DS);
    nvsMaskRegionInfo.addRegionInfo(regionInfo);
    return nvsMaskRegionInfo;
}
```

#### 4.2.2、镜面蒙版

根据相关属性，计算出点数组，根据点数组，生成蒙版区域信息对象

根据蒙版宽高，中心点，角度，生成区域点数组。

```java
A、获取关键点数组
/**
 * 绘制镜面蒙版的区域
 * Draw the area of the mirror mask
 * @param center
 * @param maskWidth
 * @param maskHeight
 * @param angle
 * @return
 */
public static PointF[] buildMirrorMaskPoint(int maskWidth, PointF center, int maskHeight, float angle) {
    PointF leftTopPoint = new PointF(center.x - maskWidth / 2, center.y - maskHeight / 2);
    PointF rightTopPoint = new PointF(center.x + maskWidth / 2, center.y - maskHeight / 2);
    PointF rightBottomPoint = new PointF(center.x + maskWidth / 2, center.y + maskHeight / 2);
    PointF leftBottomPoint = new PointF(center.x - maskWidth / 2, center.y + maskHeight / 2);
    return new PointF[]{getPointByAngle(leftTopPoint, center, angle), getPointByAngle(rightTopPoint, center, angle),
            getPointByAngle(rightBottomPoint, center, angle), getPointByAngle(leftBottomPoint, center, angle)};
}

B、根据区域数组、流媒体窗口属性及蒙版实际宽高，生成蒙版区域信息对象。

/**
 * 构建蒙版特效区域  多边形区域
 * Build local special effects area Polygonal area
 * @param pointFList 点位集合
 * @param size
 * @return
 */
public static NvsMaskRegionInfo buildPolygonMaskRegionInfo(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {
    List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFList, liveWindow, size);
    //蒙版特效区域信息
    NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
    //设置类型
    // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
    // 多边形 MASK_REGION_TYPE_POLYGON
    NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);
    //参数意义
    regionInfo.setPoints(nvsPosition2DS);
    nvsMaskRegionInfo.addRegionInfo(regionInfo);
    return nvsMaskRegionInfo;
}
```

#### 4.2.3、圆形蒙版

根据相关属性，生成区域信息对象，生成蒙版区域信息对象，把区域信息对象注入到蒙版区域信息对象中。实现算法与流程参考下面代码。

```java
/**
 * 构建蒙版特效区域  椭圆形区域
 * Build a local special effects area, an oval area
 * @param center     中心点坐标
 * @param maskWidth  蒙版宽
 * @param maskHeight 蒙版高
 * @param angle      旋转角度
 * @return
 */
public static NvsMaskRegionInfo buildCircleMaskRegionInfo(PointF center, float maskWidth, float maskHeight,
                                                          float angle, NvsLiveWindow liveWindow,
                                                          PointF size) {
    float widthPercent = 0, heightPercent = 0;
    widthPercent = maskWidth * 1.0f / size.x;
    heightPercent = maskHeight * 1.0f / size.y;
    center = mapViewToNormalized(center, liveWindow, size);
    //蒙版特效区域信息
    NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
    //设置类型
    // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
    // 多边形 MASK_REGION_TYPE_POLYGON
    NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D);
    //参数意义
    /**
     * 中心点坐标
     * 长半轴长 对应屏幕宽度的比例 [-1,1]区间
     * 短半轴长 对应屏幕高度度的比例 [-1,1]区间
     * 旋转角度
     */
    regionInfo.setEllipse2D(new NvsMaskRegionInfo.Ellipse2D(new NvsPosition2D(center.x, center.y), widthPercent, heightPercent, 0));
    NvsMaskRegionInfo.Transform2D transform2D = new NvsMaskRegionInfo.Transform2D();
    transform2D.setRotation(-angle);
    transform2D.setAnchor(new NvsPosition2D(center.x, center.y));
    regionInfo.setTransform2D(transform2D);
    nvsMaskRegionInfo.addRegionInfo(regionInfo);
    return nvsMaskRegionInfo;
}
```

#### 4.2.4、矩形蒙版

根据相关属性，生成区域信息对象，生成蒙版区域信息对象，把区域信息对象注入到蒙版区域信息对象中。实现算法与流程参考如下代码。

```java

    /**
     * 构建蒙版特效区域  矩形区域  带圆角所以用这个
     * Build a local special effect area, a rectangular area with rounded corners, so use this
     * @param center           中心点坐标
     * @param width            椭圆长半轴 对应的屏幕比例 屏幕宽度为
     * @param height           椭圆短半轴 对应的屏幕比例
     * @param angle            旋转角度
     * @param cornerRadiusRate 圆角比例
     * @return
     */
    public static NvsMaskRegionInfo buildRectMaskRegionInfo(PointF center, int width, int height,
                                                            float angle, NvsLiveWindow liveWindow,
                                                            float cornerRadiusRate, PointF size) {

//        center = liveWindow.mapViewToNormalized(center);
        //蒙版特效区域信息
        NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
        //设置类型
        // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
        // 多边形 MASK_REGION_TYPE_POLYGON
        NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE);
        //获取最小边 获取 圆角的半径
        int minSize = width > height ? height : width;
        int arcRadius = (int) (cornerRadiusRate * minSize * 0.5f);
        int controlPointDis = (int) (arcRadius * 0.45);

        //第一个点
        PointF nextPoint1 = new PointF(center.x - width * 0.5f, center.y - height * 0.5f + controlPointDis);
        PointF curPoint1 = new PointF(center.x - width * 0.5f, center.y - height * 0.5f + arcRadius);
        PointF prePoint1 = new PointF(center.x - width * 0.5f, center.y + height * 0.5f - arcRadius);
        Log.d(TAG, "point 1 c1.x:" + curPoint1.x + " y:" + curPoint1.y + " n1.x:" + nextPoint1.x
                + " y:" + nextPoint1.y + " p1.x:" + prePoint1.x + " y:" + prePoint1.y + " aD:" + arcRadius + "cD:" + controlPointDis);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint1, center, angle),
                getPointByAngle(nextPoint1, center, angle), getPointByAngle(prePoint1, center, angle), liveWindow, size);

        //第二点
        PointF nextPoint2 = new PointF(center.x - width * 0.5f, center.y - height * 0.5f + arcRadius);
        PointF curPoint2 = new PointF(center.x - width * 0.5f, center.y + height * 0.5f - arcRadius);
        PointF prePoint2 = new PointF(center.x - width * 0.5f, center.y + height * 0.5f - controlPointDis);
        Log.d(TAG, "point 2 c2.x:" + curPoint2.x + " y:" + curPoint2.y + " n2.x:" + nextPoint2.x
                + " y:" + nextPoint2.y + " p2.x:" + prePoint2.x + " y:" + prePoint2.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint2, center, angle),
                getPointByAngle(nextPoint2, center, angle), getPointByAngle(prePoint2, center, angle), liveWindow, size);

        //第三点
        PointF nextPoint3 = new PointF(center.x - width * 0.5f + controlPointDis, center.y + height * 0.5f);
        PointF curPoint3 = new PointF(center.x - width * 0.5f + arcRadius, center.y + height * 0.5f);
        PointF prePoint3 = new PointF(center.x + width * 0.5f - arcRadius, center.y + height * 0.5f);
        Log.d(TAG, "point 3 c3.x:" + curPoint3.x + " y:" + curPoint3.y + " n3.x:" + nextPoint3.x
                + " y:" + nextPoint3.y + " p1.x:" + prePoint3.x + " y:" + prePoint3.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint3, center, angle),
                getPointByAngle(nextPoint3, center, angle), getPointByAngle(prePoint3, center, angle), liveWindow, size);

        //第四点
        PointF nextPoint4 = new PointF(center.x - width * 0.5f + arcRadius, center.y + height * 0.5f);
        PointF curPoint4 = new PointF(center.x + width * 0.5f - arcRadius, center.y + height * 0.5f);
        PointF prePoint4 = new PointF(center.x + width * 0.5f - controlPointDis, center.y + height * 0.5f);
        Log.d(TAG, "point 4 c4.x:" + curPoint4.x + " y:" + curPoint4.y + " n4.x:" + nextPoint4.x
                + " y:" + nextPoint4.y + " p4.x:" + prePoint4.x + " y:" + prePoint4.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint4, center, angle),
                getPointByAngle(nextPoint4, center, angle), getPointByAngle(prePoint4, center, angle), liveWindow, size);

        //第五点
        PointF nextPoint5 = new PointF(center.x + width * 0.5f, center.y + height * 0.5f - controlPointDis);
        PointF curPoint5 = new PointF(center.x + width * 0.5f, center.y + height * 0.5f - arcRadius);
        PointF prePoint5 = new PointF(center.x + width * 0.5f, center.y - height * 0.5f + arcRadius);
        Log.d(TAG, "point 5 c5.x:" + curPoint5.x + " y:" + curPoint5.y + " n5.x:" + nextPoint5.x
                + " y:" + nextPoint5.y + " p5.x:" + prePoint5.x + " y:" + prePoint5.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint5, center, angle),
                getPointByAngle(nextPoint5, center, angle), getPointByAngle(prePoint5, center, angle), liveWindow, size);

        //第六点
        PointF nextPoint6 = new PointF(center.x + width * 0.5f, center.y + height * 0.5f - arcRadius);
        PointF curPoint6 = new PointF(center.x + width * 0.5f, center.y - height * 0.5f + arcRadius);
        PointF prePoint6 = new PointF(center.x + width * 0.5f, center.y - height * 0.5f + controlPointDis);
        Log.d(TAG, "point 6 c6.x:" + curPoint6.x + " y:" + curPoint6.y + " n6.x:" + nextPoint6.x
                + " y:" + nextPoint6.y + " p6.x:" + prePoint6.x + " y:" + prePoint6.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint6, center, angle),
                getPointByAngle(nextPoint6, center, angle), getPointByAngle(prePoint6, center, angle), liveWindow, size);

        //第七点
        PointF nextPoint7 = new PointF(center.x + width * 0.5f - controlPointDis, center.y - height * 0.5f);
        PointF curPoint7 = new PointF(center.x + width * 0.5f - arcRadius, center.y - height * 0.5f);
        PointF prePoint7 = new PointF(center.x - width * 0.5f + arcRadius, center.y - height * 0.5f);
        Log.d(TAG, "point 7 c7.x:" + curPoint7.x + " y:" + curPoint7.y + " n7.x:" + nextPoint7.x
                + " y:" + nextPoint7.y + " p1.x:" + prePoint7.x + " y:" + prePoint7.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint7, center, angle),
                getPointByAngle(nextPoint7, center, angle), getPointByAngle(prePoint7, center, angle), liveWindow, size);

        //第八点
        PointF nextPoint8 = new PointF(center.x + width * 0.5f - arcRadius, center.y - height * 0.5f);
        PointF curPoint8 = new PointF(center.x - width * 0.5f + arcRadius, center.y - height * 0.5f);
        PointF prePoint8 = new PointF(center.x - width * 0.5f + controlPointDis, center.y - height * 0.5f);
        Log.d(TAG, "point 8 c8.x:" + curPoint8.x + " y:" + curPoint8.y + " n8.x:" + nextPoint8.x
                + " y:" + nextPoint8.y + " p8.x:" + prePoint8.x + " y:" + prePoint8.y);
        maskRegionInfoAddPoints(regionInfo, getPointByAngle(curPoint8, center, angle),
                getPointByAngle(nextPoint8, center, angle), getPointByAngle(prePoint8, center, angle), liveWindow, size);
        Log.d(TAG, "point ====================================================================================");

        nvsMaskRegionInfo.addRegionInfo(regionInfo);
        return nvsMaskRegionInfo;
    }
```

#### 4.2.5、爱心蒙版

依据相关属性，计算点数组，根据点数组，生成区域信息对象，生成蒙版信息对象，把区域对象注入到蒙版信息对象中。具体实现算法与流程参考下面代码。

```java
/**
 * 构建蒙版特效区域  心形区域
 * Build a local special effects area, a heart-shaped area
 * @param center 中心点坐标
 * @param radius
 * @param angle  旋转角度
 * @return
 */
public static NvsMaskRegionInfo buildHeartMaskRegionInfo(PointF center, int radius, float angle,
                                                         NvsLiveWindow liveWindow, PointF size) {
    //蒙版特效区域信息
    NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
    //设置类型
    // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
    // 多边形 MASK_REGION_TYPE_POLYGON
    // 贝塞尔曲线MASK_REGION_TYPE_CUBIC_CURVE+
    NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE);

    PointF topIntersectionPoint = new PointF(center.x, center.y - radius * (2 * 1.0f / 6));
    PointF bottomIntersectionPoint = new PointF(center.x, center.y + radius);

    PointF prePoint = getPointByAngle(new PointF(center.x + 5 * 1.0f / 7 * radius, center.y - 0.8f * radius), center, angle);
    PointF curPoint = getPointByAngle(topIntersectionPoint, center, angle);
    PointF nextPoint = getPointByAngle(new PointF(center.x - 5 * 1.0f / 7 * radius, center.y - 0.8f * radius), center, angle);


    PointF prePoint1 = getPointByAngle(new PointF(center.x - 16 * 1.0f / 13 * radius, center.y + 0.1f * radius), center, angle);
    PointF curPoint1 = getPointByAngle(bottomIntersectionPoint, center, angle);
    PointF nextPoint1 = getPointByAngle(new PointF(center.x + 16 * 1.0f / 13 * radius, center.y + 0.1f * radius), center, angle);

    PointF[] pointFS = new PointF[]{curPoint, nextPoint, prePoint, curPoint1, nextPoint1, prePoint1};
    List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFS, liveWindow, size);

    regionInfo.setPoints(nvsPosition2DS);
    nvsMaskRegionInfo.addRegionInfo(regionInfo);
    return nvsMaskRegionInfo;
}
```

#### 4.2.6、星形蒙版

依据相关属性，计算出点数组，根据点数组，生成区域信息对象，生成蒙版信息对象，把区域对象注入到蒙版信息对象中。具体实现算法与流程参考如下代码。

```java
/**
 * 构建星型蒙版数据
 * Build star mask data
 * @param center
 * @param width
 * @param rotation
 * @param liveWindow
 * @param size
 * @return
 */
public static NvsMaskRegionInfo buildStarMaskRegionInfo(PointF center, int width, float rotation, NvsLiveWindow liveWindow, PointF size) {
    //蒙版特效区域信息
    NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
    //设置类型
    // 椭圆   MASK_REGION_TYPE_ELLIPSE2D
    // 多边形 MASK_REGION_TYPE_POLYGON
    // 贝塞尔曲线MASK_REGION_TYPE_CUBIC_CURVE+
    NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);

    //外圆
    float radius = width / 2.0f;
    float angel = (float) (Math.PI * 2 / 5);
    PointF[] outPoints = new PointF[5];
    //这里是获取五角星的五个定点的坐标点位置
    for (int i = 1; i < 6; i++) {
        float x = (float) (center.x - Math.sin(i * angel) * radius);
        float y = (float) (center.y - Math.cos(i * angel) * radius);
        outPoints[i - 1] = new PointF(x, y);
    }

    /// 越大越胖
    float radiusRate = 0.5f; //2/5
    //内圆
    float internalRadius = radius * radiusRate;
    float internalAngel = (float) (Math.PI * 2 / 5);
    PointF[] inPoints = new PointF[5];
    //这里是获取五角星的五个定点的坐标点位置
    for (int i = 1; i < 6; i++) {
        float x = (float) (center.x - Math.sin(i * internalAngel + Math.PI / 2 - Math.PI * 3 / 10) * internalRadius);
        float y = (float) (center.y - Math.cos(i * internalAngel + Math.PI / 2 - Math.PI * 3 / 10) * internalRadius);
        inPoints[i - 1] = new PointF(x, y);
    }

    //加入到一个集合中 一外一内的顺序
    PointF[] allPoints = new PointF[10];
    for (int i = 0; i < 5; i++) {
        PointF out = getPointByAngle(outPoints[i], center, rotation);
        PointF in = getPointByAngle(inPoints[i], center, rotation);
        allPoints[i * 2] = out;
        allPoints[i * 2 + 1] = in;
    }
    List<NvsPosition2D> position2DList = buildNvsPositionListFromPointFList(allPoints, liveWindow, size);

    regionInfo.setPoints(position2DList);
    nvsMaskRegionInfo.addRegionInfo(regionInfo);

    return nvsMaskRegionInfo;
}
```

5、根据区域信息，进行设置
-------------------------

环境搭建、对象生成、视频特效对象生成、区域设置、特效添加。

#### 5.1、蒙版设置

生成特效对象

    maskFx = videoClip.appendRawBuiltinFx(NvsConstants.KEY_MASK_GENERATOR);

#### 5.1.1、设置方式

SDK对蒙版的设置有两种方式，本质一样。实际应用中，两种方式可以混用。

#### 5.1.1.1、参数调整

常规方式是通过参数调整。示例代码如下：

```java
maskFx.setIntVal(“参数ID”,相应值);
maskFx.setFloatVal(“Feather Width”, 相应值);
maskFx.setStringVal(“Coordinate System”, 相应值);
maskFx.setBooleanVal(“Keep RGB”,相应值);
maskFx.setArbDataVal(“Region Info”,相应值);
```

#### 5.1.1.2、函数方式

也可以通过相关函数进行硬编码。示例代码如下：

```JAVA
//设置区域羽化宽度，参数自己调节
maskFx.setInverseRegion(false);

//是否忽略背景
maskFx.setIgnoreBackground(true);

//设置是否为局部
maskFx.setRegional(true);

maskFx.setRegionInfo(maskRegionInfo);
```

#### 5.1.2、参考代码

```JAVA
if (maskFx != null) {//如果找到蒙版特效
//设置区域羽化宽度，参数自己调节
    maskFx.setRegionalFeatherWidth(10);
//设置区域反转，根据需要进行设置
    maskFx.setInverseRegion(false);
//是否忽略背景
    maskFx.setIgnoreBackground(true);
//设置是否为局部
    maskFx.setRegional(true);
//如果是字幕蒙版
    if (infoData.getMaskType() == MaskInfoData.MaskType.TEXT) {
        maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, infoData.getTextStoryboard());
//区域信息数据设置为空
        maskFx.setRegionInfo(null);
    }
//如果不是字幕蒙版
else {
//故事板描述设置为空
maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, "");

//设置区域信息数据
maskFx.setRegionInfo(infoData.getMaskRegionInfo());
    }
}
```

#### 5.2、特别说明

#### 5.2.1、非字幕蒙版

故事板描述设置为空字符串，区域信息设置具体的值。

代码示例：
```JAVA
maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, "");
//蒙版区域信息对象，4.2主题讲述过该对象的生成
NvsMaskRegionInfo nvsMaskRegionInfo;

//根据蒙版区域信息对象，应用蒙版
maskFx.setRegionInfo(nvsMaskRegionInfo);
```

#### 5.2.2、字幕蒙版

字幕蒙版相对简单，不需要生成蒙版区域对象和区域对象。只需要进行NvsConstants.*KEY_MASK_STORYBOARD_DESC参数ID设置就可以。*

给故事板描述设置具体字符串，区域信息设置为空。

代码示例：


```JAVA
String captionInfo = “美摄字幕蒙版测试字符串”;
maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, captionInfo);
maskFx.setRegionInfo(null);
```

## Source: `md_ch/Master_Keyer.md`

Purpose: Master keyer usage.

Primary title: Master Keyer技术文档

Doc lead: 1.1版本

### Master Keyer技术文档

### Master Keyer技术文档

1.1版本

北京美摄网络科技有限公司

#### 目录

[toc]

#### 前置说明：
  美摄SDK抠像技术在拍摄和编辑时都可应用，本文档适用于拍摄。对于编辑应用，请参考美摄相关文档。

#### 1、抠像
  “抠像”一词来源于早期电视制作，英文称作“Key”。吸取画面中的某一种颜色作为透明色，将透明色从画面中抠去，使背景透出来，形成二层画面的叠加合成。可以使拍摄的人物经抠像后与其它景物叠加在一起，形成神奇的艺术效果。

[image omitted: media/38b26ee11e3919ac5e23506b3185c1d2.png]

  美摄SDK非线性编辑软件，巧妙地应用其中的Key功能，并与其它特技配合，达到高质量的抠像效果。

#### 2、素材要求
  所有的画面都可以抠像，如果实现比较好的抠像效果，最好流媒体前景与背景色差区别明显，色调不要过于接近，背景铺光要匀称。这样抠像效果最佳。

#### 3、如何利用美摄SDK进行抠像开发

##### 3.1、总体思想
  美摄SDK的很多功能实现是通过特效来进行实现的，抠像也不例外。抠像的实现是对流媒体添加特效。

  为了方便广大开发人员编程，抠像和AR Scene一样，都是通过字符串参数ID进行标记。通过Maseter Keyer参数ID构造特效对象，然后进行相关参数设定。

  抠像实现的本质是在当前流媒体界面上把一些相近颜色用其它颜色进行替代。用户在流媒体界面上发出事件，程序捕获用户点击范围，采集范围颜色，把界面上和范围相近的颜色用其它颜色来取代。

##### 3.2、抠像分类
  抠像整体分为3种模式，Master Mode、Hsv Mode、RGB Mode。分别为色度抠像，HSV空间抠像和RGB抠像。

[image omitted: media/f55d078e8da72c3274c8e40f04cd6b21.png]

##### 3.3、抠像参数ID
  通过字符串参数ID，方便开发者应用，Master Keyer整体代表抠像特技。在Master Keyer下有禁用预乘、靶色、收缩边界强度、柔软度修正、溢色去除、溢色去除强度等参数ID。根据实际需要，通过特效对象，进行相关参数设置。

  在美摄SDK种，参数ID按照抠像分类进行组织。即色度抠像参数ID，HSV空间抠像参数ID，RGB抠像参数ID，其次还有公共ID参数，公共参数ID可以被这三种模式调用。

  需要强调的是：模式内参数仅在模式选择为对应模式时生效。

###### 3.3.1、公共参数ID

| 标号 | 名字     | 解释 | 类型 | 最大 | 最小 | 默认 |
| :--- | :-- | :-- | :--| :-- | :---- | :---- |
| 01   | Master Keyer | 代表抠像 |  |  |  |  |
| 02   | Keyer Mode | 抠像类型：Master Mode；Hsv Mode；RGB Mode | String |  |  | Master Mode |
| 03   | Hsv Mode | RGB Mode |  |  |  |  |
| 04   | Key Color | 靶色 | COLOR |  |  | 0，0，0 |
| 05   | Aperture | 孔径范围，取色之后色度范围张角大小 | FLOAT | 360 | 0 | 90 |

###### 3.3.2、Master模式

| 标号 | 名字 | 解释 | 类型 | 最大 | 最小 | 默认 |
| :--| :-- | :-- | :-- | :-- | :-- | :-- |
| 01 | Disable Premultiply | 禁用预乘, 是否保留原图像alpha值 | BOOL |  |  | false |
| 02 | Shrink Intensity | 收缩边界强度，处理抠像边界 | FLOAT | 1.0 | 0.0 | 0.0 |
| 03 | Softeness Amendment | 柔软度修正，可以调整选区中区域抠至半透明 | FLOAT | 1.0 | -1.0 | 0.0 |
| 04 | Spill Removal | 溢色去除，抠像边界杂色称为溢色 | BOOL |  |  | false |
| 05 | Spill Removal Intensity | 溢色去除强度 | FLOAT | 1.0 | 0.0 | 0.25 |

###### 3.3.3、HSV模式

| 标号 | 名字     | 解释 | 类型 | 最大 | 最小 | 默认 |
| :--| :-- | :-- | :-- | :-- | :-- | :-- |
| 01 | Sat Width | S空间宽度 | FLOAT | 1 | 0 | 0.2 |
| 02 | Val Width | V空间宽度，各个空间宽度相当于和孔径一起控制对应的颜色 | FLOAT | 1 | 0 | 0.2 |
| 03 | Hue Roll Off | H空间柔边 | FLOAT | 1 | 0 | 0 |
| 04 | Sat Roll Off | S空间柔边 | FLOAT | 1 | 0 | 0 |
| 05 | Val Roll Off | 柔边对应软边，控制选中区域的半透明程度,V空间柔边 | FLOAT | 1 | 0 | 0 |

###### 3.3.4、RGB抠像参数ID

| 标号 | 名字 | 解释 | 类型 | 最大 | 最小 | 默认 |
| :--| :-- | :-- | :-- | :-- | :-- | :-- |
| 01 | RGB Softness | 同软边 | FLOAT | 1 | 0 | 0.2 |

###### 3.3.5、说明

  特别说明：在表格中，最大值与最小值是相对的，小的代表弱化，大的代表增强。

#### 4、类与函数

  在本部分中，用到NvsColor和RectF类，对于特效编程其它类，参考前面相关文档。

##### 4.1、NvsColor类

  美摄SDK封装的颜色类，是对r(红色)，g(绿色)，b(蓝色)以及a(透明度)的封装。

public 成员函数

    NvsColor (float r, float g, float b, float a)

public 属性

    float 	r      红色
    float 	g     绿色
    float 	b     蓝色
    float 	a     透明度

SDK中，NvsColor类属性r,g,b,a取值范围是[0,1]，而非[0,255]。

构造及析构函数说明：

不带参数构造函数：

    NvsColor()

带参数构造函数：

    NvsColor
    (
        float 	r,
        float 	g,
        float 	b,
        float 	a
    )

##### 4.2、相关函数

  相同名字的函数参考前面文档。本文档仅列出前面没有讲述过的函数。

###### 4.2.1、getCaptureVideoFxByIndex

获取采集视频特效。

原型：

    NvsCaptureVideoFx NvsStreamingContext.getCaptureVideoFxByIndex(int captureVideoFxIndex)

参数：
captureVideoFxIndex 视频特效索引
返回：
返回视频特效对象

###### 4.2.2、setColorVal()

给相关特效设置参数值。

原型：

    void com.meicam.sdk.NvsFx.setColorVal(String fxParam,NvsColor val)

设置特效颜色值参数值

参数：

fxParam	特效的颜色参数的类型。请参见PARAM_TYPE_COLOR

val	NvsColor自定义颜色对象

###### 4.2.3、sampleColorFromCapturedVideoFrame

采集区域颜色值。

原型：

    NvsColor com.meicam.sdk.NvsStreamingContext.sampleColorFromCapturedVideoFrame(RectF sampleRect)

对采集设备的视频帧内容进行采样

参数：
sampleRect：采样的矩形区域，坐标为实时预览窗口的自身坐标系

返回：
返回值为采样的颜色值，该颜色值是采样的矩形区域内所有像素颜色的平均值

#### 5、开发内容

##### 5.1、开发准备

  开发者首先申请摄像头权限，创建流媒体上下文（Streaming Context）对象，流媒体窗口显示NvsLiveWindow对象，并进行预览。

对象声明

    private NvsLiveWindow m_liveWindow;
    public NvsStreamingContext m_streamingContext;

    String licensePath = "assets:/meishesdk.lic";
    //对象定义
    m_streamingContext = NvsStreamingContext.init(getApplicationContext(), licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT);
    m_liveWindow = (NvsLiveWindow) findViewById(R.id.liveWindow);
    m_streamingContext.connectCapturePreviewWithLiveWindow(m_liveWindow);

##### 5.2、画面颜色采样

  从点击位置采集背景画面的颜色值。封装为成员函数

  矩形区域定位算法比较简单，不做讲述。

    private NvsColor getColorFromLiveWindow(MotionEvent event) {
    //矩形位置定位
        int sampleWidth = 20;
        int sampleHeight = 20;
        RectF sampleRect = new RectF();
        sampleRect.left = (int) (event.getX() - sampleWidth / 2);
        if (sampleRect.left < 0) {
            sampleRect.left = 0;
        } else if (sampleRect.left + sampleWidth > m_liveWindow.getWidth()) {
            sampleRect.left = m_liveWindow.getWidth() - sampleWidth;
        }

        sampleRect.top = (int) (event.getY() - sampleHeight / 2);
        if (sampleRect.top < 0) {
            sampleRect.top = 0;
        } else if (sampleRect.top + sampleHeight > m_liveWindow.getHeight()) {
            sampleRect.top = m_liveWindow.getHeight() - sampleHeight;
        }
        sampleRect.right = sampleRect.left + sampleWidth;
        sampleRect.bottom = sampleRect.top + sampleHeight;
    //采集位置颜色，并返回
        return m_streamingContext.sampleColorFromCapturedVideoFrame(sampleRect);
    }

##### 5.3、事件处理

  抠像的参数ID

    private final String NAME = "Master Keyer";

    m_liveWindow.setOnTouchListener(new View.OnTouchListener() {
        @Override
        public boolean onTouch(View v, MotionEvent event) {

    //判断是否添加过抠像特技，如果没有添加，则添加.不要重复添加。
            if (!isContainCaptureVideoFxByName(NAME)) {
                appendBuiltinCaptureVideoFx();
            }
    //调用上面函数
            NvsColor sampledColor = getColorFromLiveWindow(event);
            /*
            * 将吸取下来的背景画面颜色值设置给抠像特技
            * Set the extracted background color value to the keying effect
            * */
    //判断是否有特效对象
            NvsCaptureVideoFx keyerFx = m_streamingContext.getCaptureVideoFxByIndex(0);
            if (keyerFx == null) {
                return false;
            }
    //设置抠像颜色
            keyerFx.setColorVal("Key Color", sampledColor);
            return true;
        }
    });

##### 5.4、抠像特效设置

    private final String NAME = "Master Keyer";

    //生成抠像对象
    NvsCaptureVideoFx keyerFx = m_streamingContext.appendBuiltinCaptureVideoFx(NAME);

    //对抠像对象进行技术处理
    if (keyerFx != null) {
            /*
            * 开启溢色去除
            * Turn on overflow color removal
            * */
            keyerFx.setBooleanVal("Spill Removal", true);
            /*
            * 将溢色去除强度设置为最低
            * Set the overflow color removal intensity to minimum
            * */
            keyerFx.setFloatVal("Spill Removal Intensity", 0);
            /*
            * 设置收缩边界强度
            * Set shrink border strength
            * */
            keyerFx.setFloatVal("Shrink Intensity", 0.4);

        //Aperture：一个可以调节的孔径，代表取色之后的色度范围张角大小
    //参数30在0到90之间，可以调整，实例应用中，可以通过进度条控制

    keyerFx.setFloatVal("Aperture", 30);
    }

##### 5.5、运行效果

[image omitted: media/f55d078e8da72c3274c8e40f04cd6b33.png]

## Source: `md_ch/virtualLiveBroadcast.md`

Purpose: Virtual live broadcast usage.

Primary title: 虚拟直播

Doc lead: 在拍摄视频时，通过对视频进行抠像，然后运用美摄SDk的虚拟场景包(.capturescene)到视频上，即实现了虚拟直播功能。

### 虚拟直播

在拍摄视频时，通过对视频进行抠像，然后运用美摄SDk的虚拟场景包(.capturescene)到视频上，即实现了虚拟直播功能。

具体实现流程如下：
1. 初始化StreamingContext。创建NvsStreamingContext单例对象时，有两种方式，这里选用不带flags的创建方式。

            m_streamingContext = NvsStreamingContext.init(this, null);
2. 设置回调并将采集预览输出连接到NvsLiveWindow控件。

			//给streaming context设置回调接口
			m_streamingContext.setCaptureDeviceCallback(this);
			m_streamingContext.getAssetPackageManager().setCallbackInterface(this);

			//采集预览输出连接到NvsLiveWindow控件
			m_streamingContext.connectCapturePreviewWithLiveWindow(m_liveWindow);
3. 添加抠像采集特效。

			NvsCaptureVideoFx keyerFx = m_streamingContext.appendBuiltinCaptureVideoFx("Master Keyer");
			if(keyerFx != null) {
				//开启溢色去除
				keyerFx.setBooleanVal("Spill Removal",true);
				//将溢色去除强度设置为最低
				keyerFx.setFloatVal("Spill Removal Intensity",0);
				//设置收缩边界强度
				keyerFx.setFloatVal("Shrink Intensity",0.4);
			}

4. 启动采集预览。

			//需要对采集的视频进行颜色吸取操作，因此需要使用STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME标志
			m_streamingContext.startCapturePreview(0, NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH,
					NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME, null);
5. 点击吸色，并将吸取的背景画面颜色值设置给抠像特技。

			NvsColor sampledColor = m_streamingContext.sampleColorFromCapturedVideoFrame(sampleRect);
			//将吸取下来的背景画面颜色值设置给抠像特技
			NvsCaptureVideoFx keyerFx = m_streamingContext.getCaptureVideoFxByIndex(0);
			if(keyerFx) {
				keyerFx.setColorVal("Key Color",sampledColor);
			}
6. 运用虚拟场景包，然后就会出现虚拟直播的场景。

			m_streamingContext.applyCaptureScene(sceneId);

## Source: `md_ch/mimo_Android.md`

Purpose: Mimo Android package and API usage.

Primary title: 美摄Mimo技术文档

Doc lead: Mimo技术参数封装在json文件中，使用前首先将模版中info.json文件进行解析。

### 美摄Mimo技术文档

### Mimo Android使用文档

  Mimo技术参数封装在json文件中，使用前首先将模版中info.json文件进行解析。

  按照解析得到的信息，添加如下内容：

  A、添加镜头(注：shot，分为普通镜头和空镜头。空镜头指json中已经预定好指定素材的镜头，即用户无法对此镜头进行选素材操作)。

  B、添加时间线特效。

  C、添加clip特效等。

  最后形成合乎预期效果的时间线。再把时间线渲染成视频。

#### 1、Mimo规范

  Mimo具体规范，参考设计同事给定的范例文档。

#### 2、Demo参考代码

##### 2.1、MainActivity -> MimoActivity

  从主界面跳转到Mimo界面，用户在此界面选定某个Mimo模板，然后跳转至相册界面，选择相应素材，填充镜头数据。

##### 2.2、单镜头裁剪

  通过TrimEditActivity对单个镜头进行裁剪，设置素材的trimIn和trimOut参数。

##### 2.3、说明

  如果镜头对应选择素材为视频素材，而且该镜头包含reverse或repeat字段 需要对该视频素材进行转码操作。

  调用NvsMediaFileConvertor.convertMeidaFile 接口

    NvsMediaFileConvertor.convertMeidaFile(String srcFile,String dstFile,boolean isReverseConvert,long fromPositon,long toPosition,Hashtable< String, Object > configurations )

  镜头数据填充完毕后，跳转到MimoEditActivity页面，在此界面创建Timeline, 并按照模版信息进行添加素材及特效。

#### 3、创建时间线

##### 3.1、创建时间线

  创建时间线通过下面函数创建：

    MimoTimelineUtil.newTimeline(NvsVideoResolution videoResolution)

##### 3.2、Mimo参数配置

  通过下面函数，设置Mimo配置的各种参数。如主视频轨道、子视频轨道、字幕、特效、变速等效果。

    MimoTimelineUtil.rebuildTimelineByTemplate(NvsTimeline timeline)

##### 3.3、添加镜头数据

  参见下面方法：

    MimoTimelineUtil.addShotVideo()

  包括添加主视频轨道、子视频轨道、镜头变速、音频轨道、转场、时间线特效等。

###### 3.3.1、添加VideoClip
  通过如下函数添加：

    MimoTimelineUtil.appendVideoClip(NvsVideoTrack videoTrack,
                                        String videoFilePath,
                                        int shot,
                                        TrackClipInfo trackClipInfo,
                                        long inPoint)

###### 3.3.2、镜头变速

  针对镜头内speed数组不为空，需要进行变速操作。

  如果所选素材指定trimIn与trimOut不够镜头时长限制，也需进行变速操作。
封装方法如下：

    MimoTimelineUtil.changeSpeed（NvsVideoClip videoClip,TrackClipInfo trackClipInfo）

  注意：sdk 最小支持变速为 1/16.0

###### 3.3.3、镜头内特效

  镜头内特效按照是否存在变速分为两种：添加时间线特效和添加clip特效。

  注：其中因变速导致的一个镜头分割为多个clip的情况应将这些clip之间的转场设为空。

    MimoTimelineUtil.appendFilter(NvsVideoClip videoClip,String filterName)

###### 3.3.4、时间线特效

  按照模板信息对非镜头内特效(滤镜、复合字幕、贴纸等)进行添加。

  注：使用特效之前，应首先确保该特效已经正确安装。

    MimoTimelineUtil.setTimelineData(NvsTimeline timeline,MiMoLocalData selectTemplate)

##### 3.3.5、其它

  组合字幕字体：组合字幕可应用指定字体效果。注意的是，使用字体之前，首先对字体注册。

  片段水印：开启或关闭片段结尾水印。即添加和删除模板指定的动态水印。

  转场特效：视频转场需要在片段数据处理完毕后单独处理，否则无效！

## Source: `md_ch/Template_Android.md`

Purpose: Android template package usage.

Primary title: 模板使用技术文档

Doc lead: 美摄模板资源包的使用分三个步骤：安装、获取模板信息、创建timeline。本文档适用于Android，IOS参考相关文档。

### 模板使用技术文档

### 模板使用说明

美摄模板资源包的使用分三个步骤：安装、获取模板信息、创建timeline。本文档适用于Android，IOS参考相关文档。

#### 1、安装

和其他资源包的使用一样，调用assetPackageManager上的install接口安装，只是模板的安装必须是**异步安装，有安装完成回调。**

StringBuilder fx = new StringBuilder();

mStreamingContext.getAssetPackageManager().installAssetPackage

   (“assets:/FD76F889-8093-4757-B0FA-4FAE66273451.template”,

null,

NvsAssetPackageManager.ASSET_PACKAGE_TYPE\_TEMPLATE,false,

fx);

#### 2、设置所需的模板画幅比例（非必要步骤）

模板是可以支持多画幅的，如果想使用非默认的画幅，可以调用assetPackageManager上的changeTemplateAspectRatio接口设置所需的模板画幅：

public boolean changeTemplateAspectRatio(String uuidString, int aspectRatio)

模板所支持的画幅比例可以通过assetPackageManager上的getAssetPackageSupportedAspectRatio接口查询：

public int getAssetPackageSupportedAspectRatio(String assetPackageId, int type)

#### 3、获取模板信息

调用assetPackageManager上的相关接口获取模板信息。目前提供获取模板的素材列表、模板的可替换字幕列表。按产品需求，可以增加相应的接口来获取模板信息。

##### 3.1、获取模板的素材列表：

调用getTemplateFootages接口，传入安装后的模板资源包的UUID，返回模板的素材列表。

List\<NvsAssetPackageManager.NvsTemplateFootageDesc\> list =

m_streamingContext.getAssetPackageManager().getTemplateFootages(templateId);

素材信息类：

public static final int TEIMPLATE_FOOTAGE_TYPE_VIDEO_IMAGE = 0;

public static final int TEIMPLATE_FOOTAGE_TYPE_VIDEO = 1;

public static final int TEIMPLATE_FOOTAGE_TYPE_IMAGE = 2;

public static final int TEIMPLATE_FOOTAGE_TYPE_AUDIO = 3;

public static final int TEIMPLATE_FOOTAGE_TYPE_FAEEZE_FRAME = 4;

public static class NvsTemplateFootageCorrespondingClipInfo {

public int trackIndex;

public int clipIndex;

public long inpoint

public long outpoint

public boolean needReverse;

public boolean canReplace;

}

public static class NvsTemplateFootageDesc {

public String id;

public int type;

public boolean canReplace;

public String innerAssetFilePath;

public ArrayList\<String\> tags;

public ArrayList\<NvsTemplateFootageCorrespondingClipInfo\>
correspondingClipInfos;

}

##### 3.2、获取模板的可替换字幕列表：

调用getTemplateCaptions接口，传入安装后的模板资源包的UUID，返回可替换的字幕列表：

List\<NvsAssetPackageManager.NvsTemplateCaptionDesc\> arrayList =

m_streamingContext.getAssetPackageManager().getTemplateCaptions(templateId);

字幕信息类：

public static class NvsTemplateCaptionDesc {

public String replaceId; //字幕的id

public String text; //字幕的文字内容

}

如果需要替换文字内容，那么遍历timeline上的字幕对象，找到字幕对象的id和这个replaceId匹配的字幕对象，然后调用字幕类上的setText方法设置文字内容。

List\<NvsAssetPackageManager.NvsTemplateCaptionDesc\> captions =
m_streamingContext.getAssetPackageManager().getTemplateCaptions(templateId);

NvsTimelineCaption caption = timeline.getFirstCaption();
while (caption != null) {
String id = caption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID);

if(captions.get(0).replaceId.equals(id)) {

caption.setText(“test”);

break;

}

caption = m_timeline.getNextCaption(caption);
}

#### 4、创建timeline

调用streamingContext上的createTimeline方法，传入安装后的模板资源包的UUID，以及需要替换的footage的列表，返回模板对应的timeline。

public NvsTimeline createTimeline(String templateId, List\<templateFootageInfo\>
templateFootages);

public static class templateFootageInfo

{

public String footageId; // footage ID

public String filePath; // footage对应的文件路径

public String reverseFilePath; // footage对应的倒放文件路径

}

至此，应用层就可以播放这个timeline，或者进行二次编辑了。

## Source: `md_ch/TemplateGenerate_Android.md`

Purpose: Android template generation workflow.

Primary title: 模板生成技术文档

Doc lead: 模板是美摄SDK的重要技术之一，生成模板是使用模板技术的第一步，生成过程分两步：

### 模板生成技术文档

### 美摄sdk模板生成说明

模板是美摄SDK的重要技术之一，生成模板是使用模板技术的第一步，生成过程分两步：

#### 1、生成模板信息。

调用StreamingContext的exportTemplateInfo
接口生成一个timeline对应的模板信息，三个参数由外部传入。

函数原型如下：

// 输出模板包的信息,返回是否成功。

// 参数1：模板资源包ID

// 参数2：时间线对象

//
参数3：所需模板画幅比例，一般和timeline的画幅比例一致。请参见[模板资源包图幅比例](\@ref
ASSET_PACKAGE_ASPECT_RATIO)

public boolean exportTemplateInfo(String templateUuid, NvsTimeline timeline,

int requestedAspectRatio)

{

NvsUtils.checkFunctionInMainThread();

return nativeExportTemplateInfo(templateUuid, timeline, requestedAspectRatio);

}

如果需要模板支持多画幅，可以多次调用该接口，只要保证timeline和aspectRatio是需要的画幅，templateUuid相同即可。

调用这个接口之前，需要对timeline做一些前提操作，指定生成模板信息所需的一些额外信息。这些信息的指定均通过object上的setTemplateAttachment接口设定。

函数原型如下：

public void setTemplateAttachment(String key, String value)

目前可以设定的信息(key值)包括：

\#define TEMPLATE_ASSET_KEY_REPLACE_ID “MSTemplate-ReplaceId”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_CAN_REPLACE “MSTemplate-FootageCanReplace”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_ID “MSTemplate-FootageId”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_NAME “MSTemplate-FootageName”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_TAGS “MSTemplate-FootageTags”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_TYPE “MSTemplate-FootageType”

\#define TEMPLATE_ASSET_KEY_FOOTAGE_NEED_REVERSE “MSTemplate-FootageNeedReverse”

##### 1.1、footageId信息(必须)

key值为 "MSTemplate-FootageId"，value值为任一string。例如“footage0”。

模板在使用时是以footage为单位进行素材替换，多个clip可以对应同一个footage，一个clip也可以是一个footage。同一个footage意思是：footageId是相同的。对应于同一个footage的clip应保证以下条件：

A、trim时长一样，也就是trimOut - trimIn是一样的；

B、tag信息一致，footage可以携带tag信息，比如风景、动物等等属性，用于分类；

C、是否可替换；

D、是否需要倒放。

##### 1.2、footage是否可替换(非必须，默认是true)

key值为"MSTemplate-FootageCanReplace"，value值为“true”或者“false”。

footage可以设定为是否可以被替换，如果可以被替换，用户在使用模板时可以传入素材进行替换，实现想要的效果。

##### 1.3、footage名称(仅对不可替换footage需指定此项)

key值为"MSTemplate-FootageName"，value值为该clip使用的素材名称。例如“XXXX.jpg”。

不可替换footage是作为模板的一个内置资源存在的。对于内置的视频、音频素材，为减小模板包的size，应该转码出一个对应时长的文件。

比如一个十分钟的视频要内置，实际使用的trim段是它的第5至第20秒，那么应该转码出一个此trim段的视频，然后footageName设定为这个转码后的文件名。

##### 1.4、footage的属性(非必须，默认空字符串)

key值为"MSTemplate-FootageTags"，value值为tag的组合，例如“风景,动物”，以逗号隔开。

##### 1.5、footage的类型(必须)

key值为"MSTemplate-FootageType"，value值可为：

A：“video”；

B：“image”；

C：“videoImage”；

D：“audio”。

根据需要进行选择。

以此指定footage的类型，用户使用模板时可以据此传入相应类型的素材。

##### 1.6、footage是否需要倒放(非必须，默认false)

key值为"MSTemplate-FootageNeedReverse"，value值为“true”或者“false”。

表示这个footage是否需要倒放。对于需要倒放的footage，用户在使用模板时需要对传入的素材进行倒放。该设置仅对video类型的footage有效。

##### 1.7、replaceId设定

除了footage信息必须指定，还有一项非必要信息的指定：

对于timeline上使用的各种效果，包括贴纸、字幕、滤镜等等各种效果都可以进行替换，方法是设置replaceId(key值为"MSTemplate-ReplaceId"，value值为任一string，比如“caption0”。对于同类效果，value不可重复)。

通过以上设置，即可完成对模板所需信息的标定。

#### 生成模板文件

##### 2.1、函数说明

调用StreamingContext上的generateTemplatePackage接口，生成.templagte
的模板文件。函数原型如下：

//生成模板包，返回是否成功

public boolean generateTemplatePackage(

String templateUuid, //模板资源包ID

String innerAssetDir, //模板内部资源文件夹路径

String templateOutputDir //模板资源包输出路径

)

三个参数均由外部指定。其中：

templateUuid必须和exportTemplateInfo 接口使用的uuid一致；

innerAssetDir是timeline所用到的各种资源包的一个文件夹目录；

templateOutputDir是生成的模板文件的文件夹路径。

最终该接口在templateOutputDir路径下生成一个名称为templateUuid指定的uuid，后缀名为template的文件。

innerAssetDir所指定的文件夹是该接口的重点，也是调用这个接口前需要做的准备工作。

文件夹目录结构如图：

[image omitted: 1608621522(1)]

包含一个info.json文件和一些文件夹。

##### 2.2、文件和文件夹解释

###### 2.2.1、info.json文件

这个文件是对模板的一个描述，需要客户端生成出来，其结构如下：

[image omitted: 1608621760(1)]

1.  cover：模板的封面，非必须；

2.  minSdkVersion：模板支持的最低sdk版本，值必须是2.19.0以上；

3.  name：模板的名称；

4.  supportedAspectRatio：模板支持的画幅比例，之前调用exportTemplateInfo
    接口生成了一个什么比例的模板信息，这里就需要加一个什么比例；

5.  defaultAspectRatio：默认的画幅比例；

6.  translation：中英文翻译；

7.  uuid：模板的uuid，必须和调用接口传入的uuid一致；

8.  version：模板的版本号；

9.  innerAssetTotalCount：该模板用到的资源包的数量；

10. footageCount：可替换的footage数量；

11. duration：模板的时长；

12. creator：创作者；

13. description：模板的描述。

###### 2.2.2、其它文件夹

Timeline用到的package类型的资源包需要分类放置在这个文件夹下，分类标准是资源包的后缀名，分类文件夹名称和资源包的后缀名保持一致，如上图示。

每个分类不是必须的，有使用这个类别的资源包就放一个这个类别的文件夹，不用新建一个空文件夹。

某个类别的文件夹结构图如下：

[image omitted: 1608623315(1)]

innerAssetDir文件夹准备好后，调用StreamingContext的generateTemplatePackage接口完成模板文件生成。
