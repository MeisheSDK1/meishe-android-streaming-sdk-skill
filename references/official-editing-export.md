# Official Editing Capture And Export Docs

This reference is distilled from the SDK Doxygen Markdown and bundled inside the skill.
Prefer it for official API behavior and constraints, then use demo-derived references for implementation call order.

Read when: Use for Android capture preview/recording, timeline creation, tracks/clips, playback/seek, music, captions, stickers, themes, transitions, trim, PIP, HDR, image ROI, albums, frame retrieval, recording modes, and compile/export behavior.

Notes:
- iOS-only conditional sections are removed where the source document marks them explicitly.
- Image references are omitted because this skill keeps text/API knowledge self-contained.
- Source paths below are relative identifiers from the original documentation, not external runtime dependencies.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Source: md_ch/Tutorial.md](#source-md_chtutorialmd)
- [Source: md_ch/TrimInOut.md](#source-md_chtriminoutmd)
- [Source: md_ch/videoFrameRetriever.md](#source-md_chvideoframeretrievermd)
- [Source: md_ch/videoRecorderMode.md](#source-md_chvideorecordermodemd)
- [Source: md_ch/PIP_Android.md](#source-md_chpip_androidmd)
- [Source: md_ch/HDR_Android_cn.md](#source-md_chhdr_android_cnmd)
- [Source: md_ch/ImageROI.md](#source-md_chimageroimd)
- [Source: md_ch/Photo_Album.md](#source-md_chphoto_albummd)
- [Source: md_ch/Pan_Scan.md](#source-md_chpan_scanmd)
<!-- END GENERATED CONTENTS -->

## Source: `md_ch/Tutorial.md`

Purpose: Detailed Android development guide; iOS conditional sections are removed.

Primary title: 详细开发引导

Doc lead: * 1 [概述] (\ref 概述)

### 详细开发引导

* 1 [概述] (\ref 概述)
	* 1.1 [支持格式] (\ref 支持格式)
	* 1.2 [注意事项] (\ref 注意事项)
		* 1.2.1 [限制](\ref 限制)
		* 1.2.2 [运行环境](\ref 运行环境)
		* 1.2.3 [重要提示](\ref 重要提示)
* 2 [快速接入] (\ref 快速接入)
	* 2.1 [导入库文件] (\ref 导入库文件)
* 3 [使用说明] (\ref 使用说明)
	* 3.1 [录制] (\ref 录制)
		* 3.1.1 [从CaptureDeviceCallback接口派生] (\ref 从CaptureDeviceCallback接口派生)
		* 3.1.2 [NvsStreamingContext类] (`NvsStreamingContext`类)
		* 3.1.3 [用NvsLiveWindow类预览] (\ref 用NvsLiveWindow类预览)
		* 3.1.4 [预览前的准备] (\ref 预览前的准备)
		* 3.1.5 [开启预览] (\ref 开启预览)
			* 3.1.5.1 [带美颜录制和不带美颜录制] (\ref 带美颜录制和不带美颜录制)
		* 3.1.6 [录制与停止录制] (\ref 录制与停止录制)
		* 3.1.7 [录制参数调节] (\ref 录制参数调节)
		* 3.1.8 [美颜] (\ref 美颜)
		* 3.1.9 [采集特效（滤镜）] (\ref 采集特效（滤镜）)
			* 3.1.9.1 [内建采集特效] (\ref 内建采集特效)
			* 3.1.9.2 [扩展采集特效] (\ref 扩展采集特效)
	* 3.2 [编辑] (\ref 编辑)
		* 3.2.1 [创建timeline设定视频尺寸] (\ref 创建timeline设定视频尺寸)
		* 3.2.2 [多段视频、图片混编] (\ref 多段视频、图片混编)
		* 3.2.3 [播放与定位预览] (\ref 播放与定位预览)
		* 3.2.4 [视频裁剪] (\ref 视频裁剪)
		* 3.2.5 [从轨道上移除片段] (\ref 从轨道上移除片段)
		* 3.2.6 [片段排序] (\ref 片段排序)
		* 3.2.7 [图片时长设定] (\ref 图片时长设定)
		* 3.2.8 [移除时间线与轨道] (\ref 移除时间线与轨道)
	* 3.3 [音乐] (\ref 音乐)
		* 3.3.1 [添加音乐] (\ref 添加音乐)
                * 3.3.2 [音乐裁剪] (\ref 音乐裁剪)
	* 3.4 [字幕] (\ref 字幕)
		* 3.4.1 [添加与删除字幕] (\ref 添加与删除字幕)
		* 3.4.2 [获取timeline上的字幕] (\ref 获取timeline上的字幕)
		* 3.4.3 [改变字幕的属性] (\ref 改变字幕的属性)
		* 3.4.4 [改变字幕的入出点] (\ref 改变字幕的入出点)
	* 3.5 [动画贴纸] (\ref 动画贴纸)
	    * 3.5.1 [添加与删除动画贴纸] (\ref 添加与删除动画贴纸)
		* 3.5.2 [获取timeline上的动画贴纸] (\ref 获取timeline上的动画贴纸)
		* 3.5.3 [改变动画贴纸的属性] (\ref 改变动画贴纸的属性)
		* 3.5.4 [改变动画贴纸的入出点] (\ref 改变动画贴纸的入出点)
	* 3.6 [主题] (\ref 主题)
		* 3.6.1 [添加与删除主题] (\ref 添加与删除主题)
		* 3.6.2 [获取timeline上的主题] (\ref 获取timeline上的主题)
		* 3.6.3 [改变主题的属性] (\ref 改变主题的属性)
	* 3.7 [转场] (\ref 转场)
	* 3.8 [特效] (\ref 特效)
		* 3.8.1 [视频特效] (\ref 视频特效)
		* 3.8.2 [音频特效] (\ref 音频特效)
		* 3.8.3 [时间线视频特效] (\ref 时间线视频特效)
			* 3.8.3.1 [添加与删除时间线特效] (\ref 添加与删除时间线特效)
			* 3.8.3.2 [获取时间线特效] (\ref 获取时间线特效)
			* 3.8.3.3 [改变时间线特效的入出点] (\ref 改变时间线特效的入出点)
	* 3.9 [生成] (\ref 生成)
	* 3.10 [素材包管理] (\ref 素材包管理)
	* 3.11 [回调] (\ref 回调)
* 4 [附件] (\ref 附件)


--------------------------------------------------------------------------------------------------------------------------------------------------------
#### 详细内容

##### 1 概述
美摄SDK致力于解决移动端视频开发的技术门槛，使仅有android界面开发经验的程序员，都可以开发出性能优异、渲染效果丰富的的视频录制、编辑功能。我们的优势体现在：
	* 录制、剪辑不限时长
	* 行业最高标准的美颜效果
	* 剪辑、变速实时预览，无需转码
	* 图片、视频混编
	* 生成视频最高支持1080p
	* 丰富的转场、滤镜、字幕样式
	* 独家的主题
	* 支持4K制作和生成
        * 开放的自定义贴纸功能
##### 1.1 支持格式
* 输入规范：
	* 视频格式：MP4、MOV、WMV、M2V、MPG
	* 音频格式：MP3、FLAC、AAC、M4A
	* 图片格式：JPG、PNG
	* 视频编码：H264、WMV、MPEG4
	* 音频编码：MP3、AAC、PCM、FLAC

* 输出规范：
	* 视频格式：MP4、MOV
	* 视频编码：H264
	* 音频编码：AAC

* 扩展包格式（扩展包是美摄用来承载扩展素材的内容包，包括主题、字幕、滤镜、贴纸等）：
	* 主题：.theme
	* 字幕：.captionstyle
	* 滤镜：.videofx
	* 贴纸：.animatedsticker
	* 转场：.videotransition
        * 道具：.arscene
##### 1.2 注意事项

##### 1.2.1 限制
美摄SDK的所有接口必须在UI线程调用，否则可能出现无法预料的错误。只有NvsVideoFrameRetriever类的getFrameAtTime()方法除外。
##### 1.2.2 运行环境
运行环境如下：android studio(必须)，android4.4以上版本
##### 1.2.3 重要提示

目前，美摄SDK安卓版支持armeabi-v7a和arm64指令集的包。

使用时在gradle命令行加入

>   defaultConfig {

>     ndk {

>       abiFilters "armeabi-v7a",”arm64-v8a”

>     }

>   }

最后，如何查看程序包含有.so呢?
最简单的方法是使用解压工具将apk后缀修改为.zip,直接查看libs里是否含有.so。

##### 2 快速接入

##### 2.1 导入库文件

如果没有Meishe
SDK库，请从美摄官网：<https://www.meishesdk.com/downloads>下载最新SDK接入版本。导入库文件的方式有两种：

方式一: 直接复制。
创建工程后，将NvStreamingSdk_Android_\*\*\*_\*\*\*\\lib\\android_jar路径下jar包，复制到工程的libs路径下。同时在工程的jniLibs文件夹下（没有就创建同名文件夹），创建两个文件夹，armeabi-v7和arm64-v8a。

将NvStreamingSdk_Android_\*\*\*_\*\*\*\\lib\\android_armv7里的所有.so文件，复制到前面创建的armeabi-v7a文件夹，同理将android_arm64文件夹下的内容复制到arm64-v8a文件夹下。

[image omitted: media/f51a5a9e28941ad8ea04e40808d8b430.png]

方式二：通过配置gradle命令行方式导入库。

美摄SDK的samples都是通过配置命令行的方式导入库文件。

[image omitted: media/3171c4ee2afc59adf2b292a5112ff9f3.png]

[image omitted: media/ccad4d50c3a551240be91d17d14dd85c.png]

##### 3 使用说明

##### 3.1 录制
录制的相关接口是在NvsStreamingContext类里，包括采集预览(startCapturePreview())，录制(startRecording())，添加视频采集特效(appendBuiltinCaptureVideoFx())等。强调：美摄SDK所有的类都是以“Nvs”开头。

视频录制时需要注意以下两点：
* 断点录制：美摄SDK实现断点录制的方式是通过循环调用开始录制(startRecording())和结束录制(stopRecording())实现的。缺点是录制产生了多个文件，需要用户自己维护和删除视频数据，
并需要通过后续的编辑操作将断点录制的文件生成一个完整的新文件。优点是独立文件之间可以加入各种转场特技，避免了因转换场景而造成的视频画面生硬的切换。
* 带特效录制与不带特效录制：带特效录制即所见即所得，所录制文件的效果就是预览的效果。不带特效录制是预览时使用滤镜或者想要录制1:1的视频，但是录制出的文件是原始的不带滤镜的16:9或9:16的视频，
需要将视频文件在编辑时，再加上滤镜并裁剪到1:1，编辑并生成后得到的视频才会与预览时的视频完全一致。

如果查看录制视频的具体功能实现，建议参考this skill's demo-derived references的视频拍摄模块
##### 3.1.1 从CaptureDeviceCallback接口派生
录制前，录制的Activity需要实现NvsStreamingContext类的CaptureDeviceCallback接口并重写接口里的所有方法。实现代码如下：

			//采集设备回调接口
			public class MainActivity extends AppCompatActivity implements NvsStreamingContext.CaptureDeviceCallback {
				......//请自行重写所有方法
			}

##### 3.1.2 NvsStreamingContext类
NvsStreamingContext是美摄SDK的流媒体上下文类，可视作整个SDK框架的入口。在开始使用美摄SDK的时候，需要先初始化NvsStreamingContext类，然后在其它Activity里使用时
获取NvsStreamingContext的对象，NvsStreamingContext是单例类。在不再使用美摄SDK或者程序退出前销毁NvsStreamingContext类的对象，请务必保证不要中途销毁NvsStreamingContext
类的对象！！！NvsStreamingContext类init()方法的第二个参数为授权文件的路径，没有授权文件时给空字符串。

 NvsStreamingContext初始化代码如下：

			@Override
			protected void onCreate(Bundle savedInstanceState) {
				super.onCreate(savedInstanceState);
				m_streamingContext = NvsStreamingContext.init(this, null);//初始化Streaming Context
				setContentView(R.layout.activity_main);
			}

NvsStreamingContext销毁代码如下：

			@Override
			protected void onDestroy() {
				//streamingContext销毁
				m_streamingContext = null;
				NvsStreamingContext.close();
			}

##### 3.1.3  用NvsLiveWindow类预览
录制界面的xml文件里需要使用NvsLiveWindow控件，NvsLiveWindow是用来录制预览或者编辑预览的。xml文件设置如下：

			<com.meicam.sdk.NvsLiveWindow
				android:layout_height="match_parent"
				android:id="@+id/liveWindow"
				android:layout_width="match_parent"
			/>

NvsLiveWindow的宽高比应该是1:1，4:3，16:9，9:16等，最好与采集预览startCapturePreview()的参数aspectRatio值保持一致。否则，预览的图像是录制完的视频被裁剪后的图像。

NvsLiveWindow的填充模式：

			public class NvsLiveWindow extends SurfaceView implements SurfaceHolder.Callback
			{
				//图像按比例均匀填充，必要时进行裁剪(默认模式)
				public static final int FILLMODE_PRESERVEASPECTCROP = 0;
			    //图像均匀地缩放来适合窗口，没有裁剪
				public static final int FILLMODE_PRESERVEASPECTFIT = 1;
				//图像被缩放来适合窗口
				public static final int FILLMODE_STRETCH = 2;
			}

对于三种填充模式，图片展示如下：
	* FILLMODE_PRESERVEASPECTCROP模式：
     ![] (PreserveAspectCrop.png)

    * FILLMODE_PRESERVEASPECTFIT模式：
     ![] (PreserveAspectFit.png)

	* FILLMODE_STRETCH模式：
	 ![] (Stretch.png)

另一种预览方式是通过与SurfaceTexture连接，在SurfaceView上预览显示。对应接口如下：

			//连接时间线和一个SurfaceTexture对象，该时间线的渲染结果将会输出到这个SurfaceTexture对象上面
			public boolean connectTimelineWithSurfaceTexture(NvsTimeline timeline, SurfaceTexture outputSurfaceTexture)

			//连接时间线和一个SurfaceTexture对象并设置代理级别，该时间线的渲染结果将会输出到这个SurfaceTexture对象上面
			public boolean connectTimelineWithSurfaceTexture(NvsTimeline timeline, SurfaceTexture outputSurfaceTexture, NvsRational proxyScale)

##### 3.1.4 预览前的准备

			//给Streaming Context设置采集设备回调接口（必须有）
			m_streamingContext.setCaptureDeviceCallback(this);
			if (m_streamingContext.getCaptureDeviceCount() == 0)
				return;
			// 将采集预览输出连接到NvsLiveWindow控件（必须有）
			if (!m_streamingContext.connectCapturePreviewWithLiveWindow(m_liveWindow)) {
				Log.e(TAG, "Failed to connect capture preview with livewindow!");
				return;
			}
			//采集设备数量判定，如果采集设备是1，不能开启前置摄像头。
			if (m_streamingContext.getCaptureDeviceCount() > 1)
				m_switchBackFacing.setEnabled(true);

			if (m_streamingContext.isCaptureDeviceBackFacing(0))//判断是否为后置采集设备
			{
				.....
			}

##### 3.1.5 开启预览
在启动视频录制之前，要进行视频采集预览。

			//启动采集预览
			m_streamingContext.startCapturePreview(m_currentDeviceIndex, NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH, 0, m_aspectRatio);

##### 3.1.5.1 带美颜录制和不带美颜录制
采集预览时，可以在预览画面上看到添加的美颜和滤镜。如果开启带特效录制，录制的文件则会带有美颜和滤镜。如果不开启，则录制的视频文件没有美颜和滤镜效果，
则可以在后续的编辑功能中，再添加美颜和滤镜。带特效录制，则必须将startCapturePreview()的flags参数值设为NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER，否则设为0。

更多信息请参考：<https://www.meishesdk.com/android/doc_ch/html/content/videoRecorderMode_8md.html>
##### 3.1.6 录制与停止录制
录制输出文件.mov 或者.mp4。startRecording()开启录制，stopRecording()停止录制。startRecording()的参数outputFilePath是录制视频文件的路径。

                        m_streamingContext.startRecording(file.getAbsolutePath());
                        m_streamingContext.stopRecording();

##### 3.1.7 录制参数调节
设置闪光灯是否开启：

                        m_streamingContext.toggleFlash(true);

自动聚焦：

                        m_streamingContext.startAutoFocus(new RectF(50,50,100,100));

设置曝光补偿：

                        m_streamingContext.setExposureCompensation(40);

设置缩放：

                        m_streamingContext.setZoom(0.8);

##### 3.1.8 美颜
添加美颜特效后，在预览窗口就可以看到美颜效果。录制视频时，用户需要根据手机性能任意选择带美颜录制或者不带美颜录制。
美颜特效可设置磨皮、美白，红润，基础美颜效果，基础美颜效果的程度，锐化。具体美颜效果可以参考this skill's demo-derived references的“视频拍摄”模块。

代码如下：

                        NvsCaptureVideoFx beautyFx = m_streamingContext.appendBeautyCaptureVideoFx();//添加美颜采集特效
                        beautyFx.setFloatVal("Strength", 0.5);//设置美颜磨皮值
                        beautyFx.setFloatVal("Whitening", 0.5);//设置美白强度值
                        beautyFx.setFloatVal("Reddening", 0.5);//设置红润强度值
                        beautyFx.setBooleanVal("Default Beauty Enabled", true);//设置基础美颜的开关
                        beautyFx.setBooleanVal("Default Sharpen Enabled", true);//设置锐化的开关
                        beautyFx.setFloatVal("Default Intensity", 0.5);//设置基础美颜的强度

##### 3.1.9 采集特效（滤镜）
采集特效分为两种，内建采集特效和扩展采集特效，扩展采集特效即通过资源包安装而得到的采集特效。
##### 3.1.9.1 内建采集特效
获取内建采集特效名称可以参考列表：<https://www.meishesdk.com/android/doc_ch/html/content/FxNameList_8md.html>。

添加与移除特效：

			m_streamingContext.appendBuiltinCaptureVideoFx(fxName);
			m_streamingContext.removeAllCaptureVideoFx();

##### 3.1.9.2 扩展采集特效
使用扩展采集特效，首先安装资源包，获取资源包ID值，然后添加扩展采集特效。例如，此处采用同步方式安装资源包，如果资源包尺寸太大或者根据需要可使用异步安装方式。
			String package1Path = "assets:/7FFCF99A-5336-4464-BACD-9D32D5D2DC5E.videofx";
			m_fxPackageId = new StringBuilder();
			int error = m_streamingContext.getAssetPackageManager().installAssetPackage(package1Path, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX, true, m_fxPackageId);
			if (error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
					&& error != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
				Log.e(TAG, "Failed to install asset package!");
			}

			//添加扩展采集特效
			m_streamingContext.appendPackagedCaptureVideoFx(m_fxPackageId.toString());

##### 3.2 编辑
实现视频编辑的一般步骤：
	* 先初始化NvsStreamingContext。如果已经初始化过，则直接获取对象。

			//NvsStreamingContext初始化
			m_streamingContext = NvsStreamingContext.getInstance(); // m_streamingContext对象

        * 创建时间线(timeline)。通过NvsStreamingContext类对象创建时间线，时间线占用资源较小，如有需要，一个程序中可以创建多个时间线。一般创建一条时间线即可。
	* 添加轨道，包括视频轨道(VideoTrack)与音频轨道(AudioTrack)。时间线上可以添加视频轨道和音频轨道，而在视频轨道上添加视频片段，音频轨道上添加音频片段。如果要实现画中画，则可添加两条视频轨道。添加音频轨道一般用来给视频加音乐或者配音功能。
	* 把素材片段添加到轨道上。视频轨道上可以添加多个片段，可以是视频文件或者图片，实现图片和视频的混编。音频轨道上也可以添加多个音乐文件。
##### 3.2.1 创建timeline设定视频尺寸
创建timeline对于编辑是非常关键的，timeline的分辨率决定了生成视频文件的最大分辨率（尺寸）。请将timeline的分辨率和NvsLiveWindow的宽高比适配一致。

			NvsVideoResolution videoEditRes = new NvsVideoResolution();
			videoEditRes.imageWidth = 1280; /*视频分辨率的宽*/
			videoEditRes.imageHeight = 720; /*视频分辨率的高*/
			videoEditRes.imagePAR = new NvsRational(1, 1); /*像素比，设为1:1*/
                        NvsRational videoFps = new NvsRational(25, 1); /*帧速率，可以设25或30，也可设为30 */

			NvsAudioResolution audioEditRes = new NvsAudioResolution();
			audioEditRes.sampleRate = 44100; /*音频采样率，可以是44100，或者48000*/
			audioEditRes.channelCount = 2; /*音频通道数,一般是2*/

			/*创建时间线*/
			m_timeline = m_streamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);
			//将timeline连接到LiveWindow控件
			m_streamingContext.connectTimelineWithLiveWindow(m_timeline,m_liveWindow);
			m_streamingContext.setCompileCallback(this);//设置生成回调接口
			m_streamingContext.setPlaybackCallback(this);//设置播放回调接口

##### 3.2.2 多段视频、图片混编
一般情况下创建一条视频轨道，然后往轨道上添加图片或者视频素材。添加到轨道上的素材，我们称它为片段（clip)。图片和视频素材都是通过文件路径添加到轨道上的。
请注意：如果图片素材尺寸过大，需要降低图片尺寸，降低尺寸后的图片和创建timeline的分辨率的尺寸大小匹配最好。

添加视频轨道：
			m_videoTrack = m_timeline.appendVideoTrack();

添加音频轨道：
                        m_audioTrack = m_timeline.appendAudioTrack();

添加片段：
			for(int i = 0; i < pathList.size(); i++) {
				NvsVideoClip clip = m_videoTrack.appendClip(pathList.get(i));
			}

##### 3.2.3 播放与定位预览
对于播放与定位预览接口，其参数videoSizeMode建议设置为NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE。若无特殊需求，设为NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE的模式会影响性能。
preload是预加载，设为true。注意：美摄SDK的时间单位是微秒，1/1000000秒。

视频播放，playbackTimeline()的参数endTime，值可以是_timeline.duration或者-1。

			m_streamingContext.playbackTimeline(m_timeline, m_streamingContext.getTimelineCurrentPosition(m_timeline), -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);

视频定位预览：

			m_streamingContext.seekTimeline(m_timeline, 0, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);

##### 3.2.4 视频裁剪
改变片段的入出点，裁剪片段。

                        NvsVideoClip clip = m_videoTrack.getClipByIndex(0);
			clip.changeTrimInPoint((long)trim_in, true);
			clip.changeTrimOutPoint((long)trim_out, true);

##### 3.2.5 从轨道上移除片段
移除片段：

			m_videoTrack.removeClip(0, false);

##### 3.2.6 片段排序
轨道上的片段可以互换位置，moveClip()的参数clipIndex和destClipIndex分别代表互换的两个素材的位置索引。

			m_videoTrack.moveClip(0,3);

##### 3.2.7 图片时长设定
NvsVideoTrack类提供appendClip(String filePath, long trimIn, long trimOut)可以根据需要自由设定图片时长。
filePath是图片素材的路径，trimIn设置0，trimOut设置为8000000，则图片显示为8秒。

			m_videoTrack.appendClip(pathList.get(i),0,8000000);

如果通过appendClip(String filePath)添加图片，则图片默认显示时长是4秒。
##### 3.2.8 移除时间线与轨道
创建的时间线，添加的视频轨道和音频轨道，如果当前不再需要，则要进行移除。操作如下：

移除时间线：

			m_streamingContext.removeTimeline(m_timeline);

移除视频轨道：

			m_timeline.removeVideoTrack(0);

移除音频轨道：

			m_timeline.removeAudioTrack(0);
##### 3.3 音乐

##### 3.3.1 添加音乐
给视频添加音乐是通过音频轨道添加音频片段实现的。创建时间线后，通过appendAudioTrack()添加音频轨道，然后把音乐文件以音频片段的形式添加到音频轨道上即可。可以添加多段音乐，音乐会连续播放。

                        m_audioTrack = m_timeline.appendAudioTrack();
			m_audioTrack.appendClip(pathList.get(i));

##### 3.3.2 音乐裁剪
音乐裁剪与视频裁剪是一样的，也是通过设置入出点的方式进行裁剪。

                        NvsAudioClip clip = m_audioTrack.getClipByIndex(0);
			clip.changeTrimInPoint((long)trim_in, true);
			clip.changeTrimOutPoint((long)trim_out, true);

##### 3.4 字幕
添加，删除以及获取字幕都是在时间线(timeline)上进行执行的，可以参考this skill's demo-derived references的字幕编辑模块。
##### 3.4.1 添加与删除字幕
添加字幕，可设置字幕显示的时长。

                         NvsTimelineCaption m_timelineCapion = m_timeline.addCaption("Meishe SDK", 0, m_timeline.getDuration(), null);

移除字幕，返回下一个时间线字幕对象。如果没有下一个字幕，则返回null。

                         NvsTimelineCaption nextCaption = m_timeline.removeCaption(m_timelineCapion);

##### 3.4.2 获取timeline上的字幕
有多种方式获取字幕：

                        //获得时间线上的第一个字幕
                        NvsTimelineCaption firstCaption = m_timeline.getFirstCaption();

                        //获得时间线上的最后一个字幕
                        NvsTimelineCaption lastCaption = m_timeline.getLastCaption();

                        //获得时间线上的当前字幕的前一个字幕
                        NvsTimelineCaption prevCaption = m_timeline.getPrevCaption(currentCaption);

                        //获得时间线上的当前字幕的后一个字幕
                        NvsTimelineCaption lastCaption = m_timeline.getNextCaption(currentCaption);

根据时间线上的位置获得字幕,返回保存当前位置字幕的List集合。获取的字幕列表排序规则如下：

1.添加时字幕入点不同，按入点的先后顺序排列；

2.添加时字幕入点相同，按添加字幕的先后顺序排列。

                        List<NvsTimelineCaption> cpationList = m_timeline.getCaptionsByTimelinePosition(1000000);

##### 3.4.3 改变字幕的属性
修改字幕属性可通过NvsTimelineCaption类的方法实现。获取字幕后，可设置字幕文本，颜色，加粗，斜体，描边等。

以修改字幕文本为例：

                        currentCaption.setText("Meishe SDK");

如果是全景图字幕，还可以设置字幕中心点的极角，字幕中心点的方位角等。以设置字幕中心点的极角为例：

                        currentCaption.setCenterPolarAngle(1.2);

##### 3.4.4 改变字幕的入出点
获取字幕后，可以修改字幕在时间线上的入点，出点以及偏移值。

                        //改变入点
                        currentCaption.changeInPoint(1000000);

                        //改变出点
                        currentCaption.changeOutPoint(5000000);

                        //改变显示位置(入点和出点同时偏移offset值)
                        currentCaption.movePosition(1000000);

##### 3.5 动画贴纸
添加，删除以及获取动画贴纸也是在时间线(timeline)上进行执行的，可以参考this skill's demo-derived references的贴纸模块。
##### 3.5.1 添加与删除动画贴纸
添加动画贴纸：

                         m_timeline.addAnimatedSticker(0, m_timeline.getDuration(), m_stickerId.toString());

移除动画贴纸，返回当前贴纸的下一个贴纸。如果没有下一下贴纸，则返回null。

                         NvsTimelineAnimatedSticker nextSticker = m_timeline.removeAnimatedSticker(currentSticker);

##### 3.5.2 获取timeline上的动画贴纸
有多种方式获取时间线上添加的动画贴纸。

                        //获取时间线上第一个动画贴纸
                        NvsTimelineAnimatedSticker firstSticker = m_timeline.getFirstAnimatedSticker();

                        //获取时间线上最后一个动画贴纸
                        NvsTimelineAnimatedSticker lastSticker = m_timeline.getLastAnimatedSticker();

                        //获取时间线当前动画贴纸的前一个动画贴纸
                        NvsTimelineAnimatedSticker prevSticker = m_timeline.getPrevAnimatedSticker(currentSticker);

                        //获取时间线当前动画贴纸的后一个动画贴纸
                        NvsTimelineAnimatedSticker nextSticker = m_timeline.getNextAnimatedSticker(currentSticker);

根据时间线上的位置获得动画贴纸,返回保存当前位置动画贴纸对象的List集合。
获取的动画贴纸列表排序规则如下：
1.添加时入点不同，按入点的先后顺序排列；
2.添加时入点相同，按添加动画贴纸的先后顺序排列。

                        List<NvsTimelineAnimatedSticker> stickerList = m_timeline.getAnimatedStickersByTimelinePosition(1000000);

##### 3.5.3 改变动画贴纸的属性
修改贴纸属性可通过NvsTimelineAnimatedSticker类的方法实现。获取贴纸后，可设置缩放值，水平翻转，旋转角度，平移等。

以修改贴纸缩放为例：

                        currentSticker.setScale(1.2);

如果是全景图动画贴纸，则还可以设置贴纸中心点的极角，中心点的方位角等。以设置中心点的极角为例：

                        currentSticker.setCenterPolarAngle(1.2);

##### 3.5.4 改变动画贴纸的入出点
获取贴纸后，可以修改动画贴纸在时间线上的入点，出点以及偏移值。

                        //改变入点
                        [currentSticker changeInPoint:1000000];

                        //改变出点
                        [currentSticker changeOutPoint:5000000];

                        //改变显示位置(入点和出点同时偏移offset值)
                        [currentSticker movePosition:1000000];

##### 3.6 主题
编辑视频时，如果需要运用主题，则可通过时间线(timeline)实现添加，移除。
##### 3.6.1 添加与删除主题
运用主题：
                        m_timeline.applyTheme(m_themeId.toString());

移除主题：

                        m_timeline.removeCurrentTheme();

##### 3.6.2 获取timeline上的主题
获取当前主题包Id：

                        m_timeline.getCurrentThemeId();

##### 3.6.3 改变主题的属性
运用主题后，可以设置主题片头，片尾，主题音乐音量等，以设置主题片头为例：

                        m_timeline.setThemeTitleCaptionText("Meishe SDK");

##### 3.7 转场
转场包括视频转场和音频转场。视频转场是在视频轨道上设置的，音频转场是在音频轨道上设置的。

视频转场包括内嵌式转场和包裹式转场。设置视频内嵌转场：

                        m_videoTrack.setBuiltinTransition(0,transitionName);

视频包裹式转场：

                        m_videoTrack.setPackagedTransition(1，m_transitionId.toString());

同样地，音频转场同视频转场是相同用法，用户可参照使用。
##### 3.8 特效
在视频后续编辑中，经常会使用到几种特效，分别是视频特效(NvsVideoFx)，音频特效(NvsAudioFx)，时间线视频特效(NvsTimelineVideoFx)。
##### 3.8.1 视频特效
视频特效是使用在视频片段上的，每个视频片段可以添加若干个视频特效。视频特效包括内嵌视频特效，包裹视频特效，美颜特效。

添加内嵌视频特效：

			videoClip.appendBuiltinFx(fxName);

添加包裹视频特效：

                        videoClip.appendPackagedFx(m_fxPackageId.toString());

添加美颜特效：

			videoClip.appendBeautyFx();

移除视频特效包括移除指定索引值特效和移除所有视频特。

移除指定索引值的特效：

                        videoClip.removeFx(0);

移除所有视频特效：
                        videoClip.removeAllFx();

##### 3.8.2 音频特效
音频特效是使用在音频片段上的，每个音频片段可以添加若干个音频特效。

添加音频特效：

                        audioClip.appendFx(fxName);

移除指定索引的音频特效：

                        audioClip.removeFx(0);

##### 3.8.3 时间线视频特效
时间线视频特效是使用在时间线上的一种特效，包含内嵌特效和包裹特效。时间线上可以添加若干个时间线视频特效。
##### 3.8.3.1 添加与删除时间线特效
添加时间线特效：

                        m_timeline.addBuiltinTimelineVideoFx(1000000,5000000,fxName);
                        m_timeline.addPackagedTimelineVideoFx(1000000,5000000,fxPackageId);


##### 3.8.3.2 获取时间线特效
有多种方法获取时间线特效。

                        //获取时间线上第一个时间线视频特效
                        NvsTimelineVideoFx firstTimelineFx = m_timeline.getFirstTimelineVideoFx();
                        //获取时间线上最后一个时间线视频特效
                        NvsTimelineVideoFx lastTimelineFx = m_timeline.getLastTimelineVideoFx();
                        //获取时间线上某个时间线视频特效的前一个时间线视频特效
                        NvsTimelineVideoFx prevTimelineFx = m_timeline.getPrevTimelineVideoFx(currentTimelineFx);
                        //获取时间线上某个时间线视频特效的下一个时间线视频特效
                         NvsTimelineVideoFx nextTimelineFx = m_timeline.getNextTimelineVideoFx(currentTimelineFx);

根据时间线上的位置获得时间线视频特效,返回当前位置时间线视频特效对象的数组。

获取的时间线视频特效数组排序规则如下：

1.添加时入点不同，按入点的先后顺序排列；

2.添加时入点相同，按添加时间线视频特效的先后顺序排列。

                        List<NvsTimelineVideoFx> timelineFxArray = m_timeline.getTimelineVideoFxByTimelinePosition(2000000);

##### 3.8.3.3 改变时间线特效的入出点
获取时间线特效后，可以修改时间线特效在时间线上的入点，出点以及偏移值。

                        //改变入点
                        currentTimelineFx.changeInPoint(1000000);
                        //改变出点
                        currentTimelineFx.changeOutPoint(5000000);
                        //改变显示位置(入点和出点同时偏移offset值)
                        currentTimelineFx.movePosition(1000000);

##### 3.9 生成
美摄SDK使用compileTimeline()用于将时间线上的片段生成输出一个新的视频。

生成视频:

			m_streamingContext.compileTimeline(m_timeline, 0, m_timeline.getDuration(),
				m_compilePath, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, 0);

##### 3.10 素材包管理
美摄SDK提供了丰富的素材库，包括动画贴纸，主题，字幕样式，转场等。素材包可以从网络上下载，或者由美摄SDK项目组提供，用户可以根据需要选择使用这些素材包。美摄SDK通过NvsAssetPackageManager类对这些素材包进行管理，可以安装，升级，卸载,获取素材包的状态，版本号等。

素材包安装：

			//此处采用同步安装方式，如果包裹过大可采用异步方式
			int error = m_streamingContext.getAssetPackageManager().installAssetPackage(stickerPackagePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER, true, m_stickerId);

素材包升级：

			//此处采用同步升级方式，如果包裹过大可采用异步方式
			int error = m_streamingContext.getAssetPackageManager().upgradeAssetPackage(stickerPackagePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER, true, m_stickerId);

素材包卸载：

			int error = m_streamingContext.getAssetPackageManager().uninstallAssetPackage(m_stickerId,NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);

##### 3.11 回调
美摄SDK提供了很多回调接口，如果要查询采集设备状态，采集录制状态，视频播放状态，文件生成状态，资源包安装状态等，则必须在创建NvsStreamingContext对象后设置回调并实现对应的回调方法。

以视频播放回调为例：

			m_streamingContext.setPlaybackCallback(this);

##### 4 附件
美摄SDK版本包括极速版，标准功能版，全功能PRO版，对于每个版本产品的功能点，请参考：<https://www.meishesdk.com/editsdk>，会有详细介绍。每个用户可根据个人需要选择使用，具体请联系美摄商务。

## Source: `md_ch/TrimInOut.md`

Purpose: Trim-in/trim-out semantics.

Primary title: 裁剪入点与出点(trimIn and trimOut)

Doc lead: 简单来说，即在轨道上添加音视频片段时，对所添加的音视频根据需要进行裁剪，裁剪后待添加片段的起点跟终点就是裁剪入点和出点。整个裁剪片段的大小由自己完全掌控，可长可短。在相关接口调用时，裁剪入点值跟裁剪出点值范围必须在整个片段的时长内，且裁剪入点小于裁剪出点。

### 裁剪入点与出点(trimIn and trimOut)

简单来说，即在轨道上添加音视频片段时，对所添加的音视频根据需要进行裁剪，裁剪后待添加片段的起点跟终点就是裁剪入点和出点。整个裁剪片段的大小由自己完全掌控，可长可短。在相关接口调用时，裁剪入点值跟裁剪出点值范围必须在整个片段的时长内，且裁剪入点小于裁剪出点。

如下图，显示片段裁剪的过程，适用于视频片段频或音频片段：

![裁剪入点与出点] (`trimInOutClip.PNG`)

添加片段时，会涉及两个新的概念点，即入点(inPoint)和出点(outPoint)。入点是待添加片段在时间线上的起点位置，而出点是待添加片段在时间线上的终点位置。在对片段进行添加、插入等操作时，可根据需要制作的视频长度在时间线上选择合适的入点和出点。

如下图，片段插入过程，也适用于视频片段频或音频片段：
![入点与出点] (`addClipInPoint.PNG`)

## Source: `md_ch/videoFrameRetriever.md`

Purpose: Frame retrieval APIs and constraints.

Primary title: 视频帧图像提取

Doc lead: 视频帧图像提取，即在某一时刻提取视频帧图像。提取的视频图像可作为我们待制作视频的封面，也可用作其他用途。在SDK中，提供了两种方式来提取视频帧图像。

### 视频帧图像提取

视频帧图像提取，即在某一时刻提取视频帧图像。提取的视频图像可作为我们待制作视频的封面，也可用作其他用途。在SDK中，提供了两种方式来提取视频帧图像。

一种是通过NvsStreamingContext的
[createVideoFrameRetriever()](`com.meicam.sdk.NvsStreamingContext.createVideoFrameRetriever`)
接口创建视频帧提取NvsVideoFrameRetriever对象，然后调用其
[getFrameAtTime()] (`com.meicam.sdk.NvsVideoFrameRetriever.getFrameAtTime`)
接口来获取。

另一种是通过NvsStreamingContext的
[grabImageFromTimeline()](`com.meicam.sdk.NvsStreamingContext.grabImageFromTimeline`)
接口来获取。

两种方式对比如下：第一种方式获取的是原始视频帧某一时刻的图像，可根据需要设置要提取的视频帧像素高度。同时还可跨线程使用，不影响引擎工作。缺点是不能提取时间上已添加的贴纸，字幕，特效等素材。如果要提取包括这些素材的视频，只能打包生成然后作为原始视频来提取。
而第二种方式提取的是时间线上某一时间戳的视频帧图像，包括相应添加的贴纸，字幕，特效等素材，都会提取。缺点是会停止引擎，并且只能在UI线程里面使用。

对使用者来说，两种方式各有利弊，可根据需求选择使用。

## Source: `md_ch/videoRecorderMode.md`

Purpose: Recording mode behavior and parameter notes.

Primary title: 视频录制方式

Doc lead: 美摄SDK目前提供两种方式来采集录制视频，用户可根据需要选择使用任意一种。简单来说，一种是使用系统采集设备来采集信号进行视频录制，录制的视频不带特效，且其横纵比也不是我们预设的横纵比值。

### 视频录制方式

美摄SDK目前提供两种方式来采集录制视频，用户可根据需要选择使用任意一种。简单来说，一种是使用系统采集设备来采集信号进行视频录制，录制的视频不带特效，且其横纵比也不是我们预设的横纵比值。
另一种是带特效的视频采集录制，录制完成，会得到我们预设的横纵比的视频，同时特效也会写进录制的视频中。

两种录制方式实现如下：
在采集预览时，通过传给NvsStreamingContext的[startCapturePreview()] (`com.meicam.sdk.NvsStreamingContext.startCapturePreview`)里的参数flags的值来区别选择哪种录制方式。对于第一种录制方式，flags传入值为0，然后调用
[startRecording()] (`com.meicam.sdk.NvsStreamingContext.startRecording`)接口来启动视频录制。而第二种录制方式，flags值为[STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER](`STREAMING_ENGINE_CAPTURE_FLAG`)，再通过[startRecording()] (`com.meicam.sdk.NvsStreamingContext.startRecording`)接口来启动视频录制。

两种方式对比如下：

对于第一种方式，整个录制过程不加特效，不会出现丢帧，对用户来说这是比较好的方面。缺点是录制完毕，无法得到期望横纵比的视频（比如想录制1:1视频，结果会得到9:16的视频）。要生成带美颜，特效以及期望横纵比的视频，则需要设置包括图像宽高，
像素比等相关参数(如生成1:1视频，则图像宽高设为同一值)来创建时间线，然后添加轨道，片段，及相应的特效，最后生成预期的视频。而第二种方式在录制过程中就会加上美颜，视频特效等素材，录制完成后，就可以得到预期横纵比的视频。相比第一种方式，没有后续的视频编辑及生成。
但是这种录制方式跟当前用户手机有很大的关系。手机性能配置不同，带特效录制时可能会出现不一样的效果，因此合理的选择所要添加的特效的数量，是很重要的。对于一个低性能的手机来说，如果添加的特效过多，处理起来过于复杂，可能会导致录制的视频卡顿，丢帧。
在这种情况下，预览所录制的视频时会发现视频画面会从一帧跳跃到不衔接的另一帧，跟期望录制的视频效果反差很大，很显然这不是我们期望的结果。所以请慎重，在使用这种录制方式时，要确保特效的处理对于当前用户手机是完全可以实时处理的，即能够实时完整的写进录制的视频当中，不会造成卡顿，丢帧现象。
对于android手机来说，android本身可能存在某些问题，导致在录制时可能还会出现花屏，重影等不可预知的问题。

## Source: `md_ch/PIP_Android.md`

Purpose: Android PIP editing workflow.

Primary title: 美摄画中画技术文档

Doc lead: （例如两个视频/图片的画中画效果，时间线需要添加两个视频轨道。）

### 美摄画中画技术文档

##### 1.创建时间线
##### 2.添加与需求相匹配的视频轨道。
（例如两个视频/图片的画中画效果，时间线需要添加两个视频轨道。）


```
NvsVideoTrack mVideoTrack = mTimeline.appendVideoTrack();
NvsVideoTrack mPipVideoTrack = mTimeline.appendVideoTrack();
```

##### 3.相关视频轨道分别添加素材。(这里以两个素材为例进行展示)

```
NvsVideoTrack  mVideoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip mVideoClip = mVideoTrack.appendClip(firstMediaPath);
//如果添加的素材是图片，可设置禁止图片运动，可根据需求决定是否添加
mVideoClip.setImageMotionAnimationEnabled(false);

NvsVideoTrack  mPipVideoTrack = mTimeline.getVideoTrackByIndex(1);
NvsVideoClip mPipVideoClip = mPipVideoTrack.appendClip(secondMediaPath);
//如果添加的素材是图片，可设置禁止图片运动，可根据需求决定是否添加
mPipVideoClip.setImageMotionAnimationEnabled(false);
```

##### 4.clip 片段添加"Transform 2D” 特效。

此特效针对需要移动的clip 来添加，这里以移动第二个clip 为例。如果第一个素材需要移动的话，那么第一个clip也需要添加"Transform 2D” 特效

```
NvsVideoFx mVideoFx = mPipVideoClip.appendBuiltinFx("Transform 2D");
```

##### 5.针对具体需求对"Transform 2D” 特效对象设置相应属性值（这里以手势拖动第二个clip 为例）

*需要注意的是，偏移值需转换为时间线偏移
```
//视图坐标转换成时间线坐标
PointF pointF1 = mLiveWindow.mapViewToCanonical(currentPoint);
PointF pointF2 = mLiveWindow.mapViewToCanonical(previousPoint);
double transX = mVideoFx.getFloatVal("Trans X");
double transY = mVideoFx.getFloatVal("Trans Y");
mVideoFx.setFloatVal("Trans X", transX + (pointF1.x - pointF2.x));
mVideoFx.setFloatVal("Trans Y", transY + (pointF1.y - pointF2.y));
```


| 属性        | 含义    |
|------------|---------|
| Trans X  | X 轴偏移 |
| Trans Y  | Y 轴偏移 |
| Scale X  | X 轴缩放 |
| Scale Y  | Y 轴缩放 |
| Rotation | 旋转 |


上面属性表中其他属性均可根据需求按照偏移示例代码进行赋值和应用。

## Source: `md_ch/HDR_Android_cn.md`

Purpose: Android HDR editing/export workflow.

Primary title: HDR

Doc lead: 美摄SDK支持HDR视频的导入、编辑和导出，即全流程的HDR视频处理。相比普通的SDR视频处理，在以下几步需要特殊设置：

### HDR

### HDR

#### HDR相关说明：

美摄SDK支持HDR视频的导入、编辑和导出，即全流程的HDR视频处理。相比普通的SDR视频处理，在以下几步需要特殊设置：

初始化SDK，创建timeline，设置liveWindow展示，导出HDR。


#### 获取本机HDR支持能力：

通过NvsStreamingContext类上的getEngineHDRCaps()接口可以获取本机的HDR支持能力，返回值含义如下：

    public static final int HDR_CAPABILITY_FLAG_SUPPORTED_BY_IMPORTER = 1;  (导入)
    public static final int HDR_CAPABILITY_FLAG_SUPPORTED_BY_EDITING = 2;   (编辑)
    public static final int HDR_CAPABILITY_FLAG_SUPPORTED_BY_EXPORTER = 4;  (导出)
    public static final int HDR_CAPABILITY_FLAG_SUPPORTED_BY_LIVEWINDOW = 8;(屏幕支持)


#### 1、初始化配置：

HDR功能需要添加下面标记：

    NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED

>
    String licensePath = "assets:/meishesdk.lic";
    NvsStreamingContext.init(mContext, licensePath,
    NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT|NvsStreamingContext.S TREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED);


#### 2、创建timeline：


创建timeline需要指定NvsVideoResolution的bitDepth属性，该属性有3个参数：

>   VIDEO\_RESOLUTION\_BIT\_DEPTH\_8\_BIT        （SDR编辑）

>   VIDEO\_RESOLUTION\_BIT\_DEPTH\_16\_BIT\_FLOAT（HDR编辑）

>   VIDEO\_RESOLUTION\_BIT\_DEPTH\_AUTO          （自动适配机型）


    //创建timeline
    videoEditRes.bitDepth = XXXX
    mStreamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);


#### 3、设置livewindow：

livewindow有3种支持模式，可以通过setHDRDisplayMode()配置：

    HDR_DISPLAY_MODE_SDR （按SDR模式显示，对于HDR的视频不做处理，画面可能过爆）
    HDR_DISPLAY_MODE_DEPEND_DEVICE （依据设备自动适配）
    HDR_DISPLAY_MODE_TONE_MAP_SDR（将HDR视频转换成SDR再显示，画面不会过爆）


#### 4、生成配置：

通过配置compileConfigurations来支持HDR的导出，需要设置两个参数：

    1.	key为：NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME  value为："hevc"
    2.	key为：NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER  value为："none"或者"st2084"或者"hlg"


>

    Hashtable<String, Object> compileConfigurations = new Hashtable<>();
    compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME,Constants.HDR_EXPORT_HEVC);
    compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER, settingValues.getExportConfig());

    mStreamingContext.setCompileConfigurations(compileConfigurations);

#### 5、色彩增益处理：

调整在SDR向HDR转换时候色彩增益，默认：0。

    /*!
    *  \brief
    *  \param
    *
    *  \brief 设置在SDR向HDR转换时候色彩增益
    *  \param gain 为色彩增益 范围是【1.0，10.0】
    *
    *  \since 2.23.0
    *  \sa getColorGainForSDRToHDR
    */
    void com.meicam.sdk.NvsStreamingContext.setColorGainForSDRToHDR(float gain)

    /*!
    *  \brief
    *  \return
    *
    *  \brief 获取在SDR向HDR转换时候色彩增益
    *  \return 返回色彩增益值 范围是【1.0，10.0】
    *
    *  \since 2.23.0
    *  \sa setColorGainForSDRToHDR
    */
    float com.meicam.sdk.NvsStreamingContext.getColorGainForSDRToHDR()

录制参数与导出参数：NVS_RECORD_VIDEO_ENCODEC_NAME，NVS_RECORD_HDR_VIDEO_COLOR_TRANSFER。

#### 其他：

媒体格式分为几类 SDR、HDR、HDR10、HDR10+、Dolby Vision。

| **类型**     | **颜色转换曲线名称**   |
|--------------|----------------|
| SDR          | none           |
| HDR          | hlg            |
| HDR10/HDR10+ | st2084(PQ视频) |
| Dolby Vision（仅IOS支持） | hlg dolby vision（仅IOS支持）

## Source: `md_ch/ImageROI.md`

Purpose: Image ROI behavior.

Primary title: 图片ROI

Doc lead: SDK中，在轨道上添加视频片段，选择图片作为视频源时，则可以对图片片段进行动态移动ROI处理。ROI(Region Of Interesting),即感兴趣区域。每张图片，不论是景或是人，都有大家喜欢感兴趣的部分，我们称该部分为图片ROI。对于由若干张图片创建的视频片段，通过两个矩形框来选择我们认为最美的部分作为图片片段的起始ROI(startROI)与终止

### 图片ROI

SDK中，在轨道上添加视频片段，选择图片作为视频源时，则可以对图片片段进行动态移动ROI处理。ROI(Region Of Interesting),即感兴趣区域。每张图片，不论是景或是人，都有大家喜欢感兴趣的部分，我们称该部分为图片ROI。对于由若干张图片创建的视频片段，通过两个矩形框来选择我们认为最美的部分作为图片片段的起始ROI(startROI)与终止ROI(endROI)。
具体API设置，参见
[setImageMotionROI()] (`com.meicam.sdk.NvsVideoClip.setImageMotionROI`)。

选择图片片段起始ROI，如下图：

[image omitted: 图片片段起始ROI]

选择图片片段终止ROI，如下图：

[image omitted: 图片片段终止ROI]

播放预览图片片段，图片片段会按照我们设定的起始ROI位置缓慢平滑的动态移动到终止ROI位置。整个动态移动过程是线性平移，从而使整个画面自然流畅地实时展示出来。

## Source: `md_ch/Photo_Album.md`

Purpose: Photo album creation/editing workflow.

Primary title: 美摄影集技术文档

Doc lead: 根据影集模板要求，用户选择一定数量的图片，把影集素材的文件地址、授权文件地址、影集模板目录和图片列表等参数传入美摄提供的接口中，得到一个有影集效果的timeline，然后使用livewindow就可以预览效果。

### 美摄影集技术文档

### 美摄影集使用说明

#### 1、功能描述

根据影集模板要求，用户选择一定数量的图片，把影集素材的文件地址、授权文件地址、影集模板目录和图片列表等参数传入美摄提供的接口中，得到一个有影集效果的timeline，然后使用livewindow就可以预览效果。

#### 2、模板主要文件介绍

info.json：模板描述信息，可以获取模板名称和需要替换的图片的最小数量和最大数量；

cover.jpg：影集封面图；

cover.mp4：影集封面视频；

fx9v16.msphotoalbum：影集模板文件；

368a621a-0d67-2a8a-d2d4-33fe1848b77c.lic：影集模板授权文件；

#### 3、接入方法（以android为例）

1.  把美摄提供的NvPhotoAlbumHelperLib.jar放入android工程的app/libs目录下；

1.  用户需要读取info.json文件获取需要替换的图片的最小数量和最大数量，然后根据数量去选择图片，选择完图片之后，根据需求调用如下的任何一个接口：

##### 接口一：

**说明：图片Crop方式9:16显示；如果图片数量小于最大数量，会循环利用这些图片，例如最多可以选5张，用户选了3张，显示结果是1,2,3,1,2。**

createPhotoAlbumTimeline（Context context, String filePath, String licFile,
String resourceDir, ArrayList\<String\> replaceFileList）接口：

参数说明：

Context：activity的context就可以；

filePath：fx9v16.msphotoalbum文件地址；

licFile：后缀是lic的文件地址；

resourceDir：影集模板解压缩之后的目录；

replaceFileList： 选择的需要替换的图片列表；

##### 接口二：

**说明：图片Crop方式9:16显示；图片数量处理逻辑同接口一，这个接口只是增加了字幕list，用户可以在影集模板中显示一些字幕。**

createPhotoAlbumTimeline（Context context, String filePath, String licFile,
String resourceDir, ArrayList\<String\> replaceFileList, ArrayList\<String\>
captionList）接口：

参数说明：

Context：activity的context就可以；

filePath：fx9v16.msphotoalbum文件地址；

licFile：后缀是lic的文件地址；

resourceDir：影集模板解压缩之后的目录；

replaceFileList： 选择的需要替换的图片列表；

captionList： 需要替换的文字列表；

##### 接口三：

**说明：图片Crop方式9:16显示；图片数量处理逻辑与前两个接口不同，如果图片数量超过最大数量，会循环使用模板，例如最多可以选3张，用户选了8张，显示结果是123，456，787，其中123、456和787都是同样的模板效果。**

createIgnoreMaxPhotoNumberLimitPhotoAlbumTimeline（Context context, String
filePath, String licFile, String resourceDir, ArrayList\<String\>
replaceFileList, ArrayList\<String\> captionList,

boolean ignoreMaxPhotoNumberLimit）接口：

参数说明：

Context：activity的context就可以；

filePath：fx9v16.msphotoalbum文件地址；

licFile：后缀是lic的文件地址；

resourceDir：影集模板解压缩之后的目录；

replaceFileList： 选择的需要替换的图片列表；

captionList： 需要替换的文字列表；

ignoreMaxPhotoNumberLimit：是否忽略照片最大数量限制，如果是，才说本接口说明的方式处理，反之则用接口一中的图片数量处理逻辑；

##### 接口四：

**说明：图片Fit方式9:16显示；**图片数量处理逻辑与接口一相同，图片需要全图显示，内部会根据用户输入的一个照片截取一张9:16全图显示的图片，所以需要外界传入一个图片缓存目录，交由用户去管理缓存目录。

createPhotoAlbumLetterBoxTimeline（Context context, String filePath, String
licFile, String resourceDir, ArrayList\<String\> replaceFileList, String
cacheImagePath）接口：

参数说明：

Context：activity的context就可以；

filePath：fx9v16.msphotoalbum文件地址；

licFile：后缀是lic的文件地址；

resourceDir：影集模板解压缩之后的目录；

replaceFileList： 选择的需要替换的图片列表；

cacheImagePath： 截取图片的缓存路径；

3）接口返回一个NvsTimeline，用户拿到timeline之后连接livewindow即可预览影集效果；

## Source: `md_ch/Pan_Scan.md`

Purpose: Pan-scan parameter guidance.

Primary title: 摇摄与扫描(Pan and Scan)

Doc lead: 摇摄与扫描通常用来调整视频图像在显示输出设备上的位置与大小信息。具体方法为纵向平移与横向裁剪，图像调整时保持宽高比不变。例如，在4：3显示设备上输出16：9视频图像时，裁剪左右两边，以确保画面比例为4：3，在16：9显示设备上输出4：3视频图像时，裁剪上下两边，以保证画面比例为16：9。

### 摇摄与扫描(Pan and Scan)

摇摄与扫描通常用来调整视频图像在显示输出设备上的位置与大小信息。具体方法为纵向平移与横向裁剪，图像调整时保持宽高比不变。例如，在4：3显示设备上输出16：9视频图像时，裁剪左右两边，以确保画面比例为4：3，在16：9显示设备上输出4：3视频图像时，裁剪上下两边，以保证画面比例为16：9。

在美摄SDK中摇摄与扫描用以调整视频片段的输出位置，参见
[摇摄与扫描API] (`com.meicam.sdk.NvsVideoClip.setPanAndScan`)来设置。
pan的取值是[-1,1]，控制纵向画面的展示，scan的取值是[0,1]，控制横向画面的裁剪。例如：

当pan为0，scan为0时，原图显示。

当pan为-1，画面整体上移，裁剪超出输出范围内的画面。

当pan为1，画面整体下移，裁剪超出输出范围内的画面。

当scan为1，画面横向扩充，裁剪超出输出范围内的画面。

![摇摄与扫描] (@ref pan_scan.png)
