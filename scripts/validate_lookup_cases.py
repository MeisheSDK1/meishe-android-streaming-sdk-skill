#!/usr/bin/env python3
"""Validate API and natural-language lookup cases for the Meishe skill."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

EXACT_API_QUERIES = [
    "NvsStreamingContext.init",
    "NvsStreamingContext.getInstance",
    "NvsStreamingContext.getSdkVersion",
    "NvsStreamingContext.getAssetPackageManager",
    "NvsStreamingContext.createTimeline",
    "NvsStreamingContext.getAVFileInfo",
    "NvsStreamingContext.getAVInfoFromFile",
    "NvsStreamingContext.connectTimelineWithLiveWindow",
    "NvsStreamingContext.connectTimelineWithLiveWindowExt",
    "NvsStreamingContext.seekTimeline",
    "NvsStreamingContext.playbackTimeline",
    "NvsStreamingContext.stop",
    "NvsStreamingContext.getStreamingEngineState",
    "NvsStreamingContext.getTimelineCurrentPosition",
    "NvsStreamingContext.compileTimeline",
    "NvsStreamingContext.setCompileCallback",
    "NvsStreamingContext.setCompileCallback2",
    "NvsStreamingContext.setCompileCallback3",
    "NvsStreamingContext.connectCapturePreviewWithLiveWindow",
    "NvsStreamingContext.getCaptureDeviceCount",
    "NvsStreamingContext.startCapturePreview",
    "NvsStreamingContext.startRecording",
    "NvsStreamingContext.stopRecording",
    "NvsStreamingContext.appendBuiltinCaptureVideoFx",
    "NvsStreamingContext.hasARModule",
    "NvsStreamingContext.initHumanDetection",
    "NvsStreamingContext.initHumanDetectionExt",
    "NvsTimeline.appendVideoTrack",
    "NvsTimeline.appendAudioTrack",
    "NvsTimeline.getVideoTrackByIndex",
    "NvsTimeline.getAudioTrackByIndex",
    "NvsTimeline.getDuration",
    "NvsTimeline.addBuiltinTimelineVideoFx",
    "NvsTimeline.addPackagedTimelineVideoFx",
    "NvsTimeline.addCaption",
    "NvsTimeline.addCompoundCaption",
    "NvsTimeline.addAnimatedSticker",
    "NvsVideoTrack.appendClip",
    "NvsVideoTrack.insertClip",
    "NvsTrack.splitClip",
    "NvsTrack.getClipCount",
    "NvsTrack.removeClip",
    "NvsTrack.removeAllClips",
    "NvsTrack.moveClip",
    "NvsTrack.setVolumeGain",
    "NvsClip.changeTrimInPoint",
    "NvsClip.changeTrimOutPoint",
    "NvsClip.changeSpeed",
    "NvsVideoClip.getImageMotionAnimationEnabled",
    "NvsVideoClip.setImageMotionAnimationEnabled",
    "NvsVideoClip.appendBuiltinFx",
    "NvsVideoClip.appendPackagedFx",
    "NvsVideoClip.appendRawBuiltinFx",
    "NvsFx.setFloatVal",
    "NvsFx.setBooleanVal",
    "NvsFx.setStringVal",
    "NvsFx.setIntVal",
    "NvsFx.setColorVal",
    "NvsCaption.setText",
    "NvsCompoundCaption.setText",
    "NvsAssetPackageManager.installAssetPackage",
    "NvsAssetPackageManager.upgradeAssetPackage",
    "NvsAssetPackageManager.getAssetPackageStatus",
    "NvsAssetPackageManager.getAssetPackageVersion",
    "NvsAssetPackageManager.getAssetPackageVersionFromAssetPackageFilePath",
    "NvsEffectSdkContext.init",
    "NvsEffectSdkContext.getInstance",
    "NvsEffectSdkContext.initHumanDetectionExt",
    "NvsEffectSdkContext.setupHumanDetectionData",
    "NvsAVFileInfo.getDuration",
    "NvsAVFileInfo.getVideoStreamDimension",
    "NvsAVFileInfo.getVideoStreamRotation",
    "NvsAudioTrack.addClip",
    "NvsAudioTrack.appendClip",
]

EXACT_STABLE_API_QUERIES = [
    "NvsStreamingContext#init(Landroid/app/Activity;Ljava/lang/String;I)Lcom/meicam/sdk/NvsStreamingContext;",
    "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;)Lcom/meicam/sdk/NvsTimeline;",
    "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;I)Lcom/meicam/sdk/NvsTimeline;",
    "NvsStreamingContext#playbackTimeline(Lcom/meicam/sdk/NvsTimeline;JJLcom/meicam/sdk/NvsRational;ZI)Z",
    "NvsStreamingContext#seekTimeline(Lcom/meicam/sdk/NvsTimeline;JLcom/meicam/sdk/NvsRational;I)Z",
    "NvsStreamingContext#startRecording(Ljava/lang/String;ILjava/util/Hashtable;)Z",
    "NvsStreamingContext#setCompileConfigurations(Ljava/util/Hashtable;)V",
    "NvsStreamingContext#getCaptureDeviceCapability(I)Lcom/meicam/sdk/NvsStreamingContext$CaptureDeviceCapability;",
    "NvsStreamingContext#initHumanDetection(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;I)Z",
    "NvsStreamingContext#closeHumanDetection()V",
    "NvsTimeline#getNextCaption(Lcom/meicam/sdk/NvsTimelineCaption;)Lcom/meicam/sdk/NvsTimelineCaption;",
    "NvsTimeline#getNextCaption(Lcom/meicam/sdk/NvsTimelineCompoundCaption;)Lcom/meicam/sdk/NvsTimelineCompoundCaption;",
    "NvsVideoClip#getNextCaption(Lcom/meicam/sdk/NvsClipCaption;)Lcom/meicam/sdk/NvsClipCaption;",
    "NvsVideoClip#getNextCaption(Lcom/meicam/sdk/NvsClipCompoundCaption;)Lcom/meicam/sdk/NvsClipCompoundCaption;",
    "NvsVideoTrack#setBuiltinTransition(ILjava/lang/String;)Lcom/meicam/sdk/NvsVideoTransition;",
    "NvsVideoTrack#setPackagedTransition(ILjava/lang/String;)Lcom/meicam/sdk/NvsVideoTransition;",
    "NvsVideoClip#appendRawBuiltinFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoFx;",
    "NvsAudioClip#setFadeOutDuration(J)V",
    "NvsMultiThumbnailSequenceView#mapTimelinePosFromX(I)J",
    "NvsStreamingContext#registerFontByFilePath(Ljava/lang/String;)Ljava/lang/String;",
    "NvsStreamingContext#compileTimeline(Lcom/meicam/sdk/NvsTimeline;JJLjava/lang/String;IILjava/util/Hashtable;I)Z",
    "NvsStreamingContext#createTimeline(Lcom/meicam/sdk/NvsVideoResolution;Lcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;I)Lcom/meicam/sdk/NvsTimeline;",
    "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;ILcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;)Lcom/meicam/sdk/NvsTimeline;",
    "NvsStreamingContext#init(Landroid/app/Activity;Ljava/lang/String;)Lcom/meicam/sdk/NvsStreamingContext;",
    "NvsStreamingContext#initHumanDetection(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    "NvsStreamingContext#initHumanDetectionExt(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    "NvsStreamingContext#stopRecording(Z)V",
    "NvsVideoClip#appendBuiltinFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
    "NvsVideoClip#appendRawBuiltinFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
    "NvsAudioTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsAudioClip;",
    "NvsClip#changeSpeed(D)V",
    "NvsClip#changeTrimInPoint(JZ)J",
    "NvsCompoundCaption#setText(ILjava/lang/String;)V",
    "NvsEffectSdkContext#init(Landroid/app/Activity;Ljava/lang/String;)Lcom/meicam/effect/sdk/NvsEffectSdkContext;",
    "NvsEffectSdkContext#initHumanDetectionExt(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    "NvsStreamingContext#setCompileCallback3(Lcom/meicam/sdk/NvsStreamingContext$CompileCallback3;)V",
    "NvsTrack#moveClip(IJZZ)Z",
    "NvsTrack#setVolumeGain(FF)V",
    "NvsVideoClip#appendPackagedFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
]

NATURAL_QUERY_CASES = [
    ("sdk init", "core-lifecycle"),
    ("初始化", "core-lifecycle"),
    ("license permission callback", "core-lifecycle"),
    ("权限回调", "core-lifecycle"),
    ("short video editor", "short-video-editor"),
    ("短视频编辑器", "short-video-editor"),
    ("complete editor", "short-video-editor"),
    ("mixed image video timeline", "short-video-editor"),
    ("resume saved editor project", "short-video-editor"),
    ("restore editor filters captions stickers audio", "short-video-editor"),
    ("editor project state restore", "short-video-editor"),
    ("多素材 图片 视频 时间线 工程恢复", "short-video-editor"),
    ("恢复工程滤镜字幕贴纸音乐", "short-video-editor"),
    ("编辑工程完整恢复", "short-video-editor"),
    ("我要做视频编辑器", "short-video-editor"),
    ("timeline trim split", "timeline-editing"),
    ("时间线剪辑", "timeline-editing"),
    ("append clip", "timeline-editing"),
    ("轨道片段裁剪", "timeline-editing"),
    ("preview playback seek", "preview-playback-export"),
    ("预览播放", "preview-playback-export"),
    ("compile export", "preview-playback-export"),
    ("缩略图导出", "preview-playback-export"),
    ("camera recording", "capture-recording"),
    ("相机录制", "capture-recording"),
    ("focus flash", "capture-recording"),
    ("拍摄预览", "capture-recording"),
    ("filter effect transition", "effects-transforms"),
    ("滤镜转场", "effects-transforms"),
    ("mask particle watermark", "effects-transforms"),
    ("遮罩粒子", "effects-transforms"),
    ("caption sticker", "captions-stickers"),
    ("compound caption font", "captions-stickers"),
    ("动态贴纸字体", "captions-stickers"),
    ("audio music voiceover", "audio-media"),
    ("音频配乐", "audio-media"),
    ("lyrics convert media file", "audio-media"),
    ("录音转码", "audio-media"),
    ("install asset package", "asset-packages"),
    ("安装素材包", "asset-packages"),
    ("upgrade package id", "asset-packages"),
    ("资源包升级", "asset-packages"),
    ("beauty makeup ar scene", "beauty-makeup-ar"),
    ("美颜美妆", "beauty-makeup-ar"),
    ("face mesh warp", "beauty-makeup-ar"),
    ("AR道具人脸", "beauty-makeup-ar"),
    ("真机检测到人脸但 AR 场景依旧没效果", "beauty-makeup-ar"),
    ("人脸网格已安装应用但没有视觉效果", "beauty-makeup-ar"),
    ("face detected but AR effect invisible", "beauty-makeup-ar"),
    ("Trial Version isSdkAuthorised false", "beauty-makeup-ar"),
    ("segmentation keyer", "segmentation-keying-ai"),
    ("分割抠像", "segmentation-keying-ai"),
    ("virtual background", "segmentation-keying-ai"),
    ("绿幕背景替换", "segmentation-keying-ai"),
    ("template mimo cutsame", "template-mimo-cutsame"),
    ("剪同款模板", "template-mimo-cutsame"),
    ("replace footage", "template-mimo-cutsame"),
    ("cutsame reverse footage and compound caption replacement", "template-mimo-cutsame"),
    ("mimo template reverse media mapping", "template-mimo-cutsame"),
    ("一键成片卡点", "template-mimo-cutsame"),
    ("pip watermark background", "themes-pip-watermark"),
    ("画中画水印", "themes-pip-watermark"),
    ("theme photo album", "themes-pip-watermark"),
    ("主题相册片尾", "themes-pip-watermark"),
    ("asset center download package", "asset-center"),
    ("素材中心", "asset-center"),
    ("online material", "asset-center"),
    ("远程素材下载", "asset-center"),
    ("Android LTS 下载SDK人脸版本", "official-sdk-resources"),
    ("facemode 模型在官网下载包哪里", "official-sdk-resources"),
    ("effectlib.jar 总包路径", "official-sdk-resources"),
    ("NvAndroidStreamingSdk.jar 官网包路径", "official-sdk-resources"),
    ("美摄SDK总包资源目录", "official-sdk-resources"),
    ("Mimo 模板包是否在SDK下载包中", "official-sdk-resources"),
    ("capture callbacks and device capability", "capture-recording"),
    ("拍摄回调和设备能力", "capture-recording"),
    ("compile bitrate fps encoder", "preview-playback-export"),
    ("导出码率帧率编码器", "preview-playback-export"),
    ("caption sticker time range", "captions-stickers"),
    ("字幕贴纸时间范围", "captions-stickers"),
    ("packaged transition and raw video fx", "effects-transforms"),
    ("素材包转场和原始特效", "effects-transforms"),
    ("human detection model lifecycle", "beauty-makeup-ar"),
    ("人体检测模型初始化释放", "beauty-makeup-ar"),
    ("configured timeline compile callback3", "preview-playback-export"),
    ("配置式时间线导出和二次进度回调", "preview-playback-export"),
    ("range clip fx", "effects-transforms"),
    ("区间滤镜", "effects-transforms"),
    ("synchronous stop recording", "capture-recording"),
    ("同步停止录制", "capture-recording"),
    ("extended human detection model", "beauty-makeup-ar"),
    ("人体检测扩展模型", "beauty-makeup-ar"),
    ("compound caption slot text", "captions-stickers"),
    ("复合字幕单槽文本", "captions-stickers"),
    ("字幕气泡", "captions-stickers"),
    ("富文本字幕渲染器", "captions-stickers"),
    ("字幕动画", "captions-stickers"),
    ("拼装字幕", "captions-stickers"),
    ("modular caption", "captions-stickers"),
    ("字幕位置移动", "captions-stickers"),
    ("贴纸位置移动", "captions-stickers"),
    ("字幕气泡不生效", "captions-stickers"),
    ("字幕贴纸属性编辑对话框", "short-video-editor"),
    ("stereo track volume", "audio-media"),
    ("音轨左右声道音量", "audio-media"),
]

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--natural-threshold", type=float, default=0.95)
    return parser.parse_args()

def scripts_dir():
    return Path(__file__).resolve().parent

def load_modules():
    sys.path.insert(0, str(scripts_dir()))
    import compose_modules
    import search_skill_index

    return compose_modules, search_skill_index

def top_natural_match(search_skill_index, query):
    entries = search_skill_index.load_index().get("entries", [])
    normalized_query = search_skill_index.normalize(query)
    terms = search_skill_index.split_terms(normalized_query)
    scored = [
        (search_skill_index.score_entry(normalized_query, terms, entry), entry)
        for entry in entries
    ]
    matches = [(score, entry) for score, entry in scored if score > 0]
    matches.sort(key=lambda item: (-item[0], item[1]["id"]))
    if not matches:
        return None, 0
    return matches[0][1]["id"], matches[0][0]

def main():
    args = parse_args()
    compose_modules, search_skill_index = load_modules()

    exact_failures = []
    for query in EXACT_API_QUERIES:
        matches = compose_modules.api_matches(query, limit=5)
        if not matches or matches[0][0] != 100 or matches[0][1].get("member") != query:
            exact_failures.append(
                {
                    "query": query,
                    "top": matches[0][1].get("member") if matches else None,
                    "score": matches[0][0] if matches else 0,
                }
            )

    stable_failures = []
    for query in EXACT_STABLE_API_QUERIES:
        matches = compose_modules.api_matches(query, limit=5)
        if (
            not matches
            or matches[0][0] != 120
            or matches[0][1].get("stable_id") != query
        ):
            stable_failures.append(
                {
                    "query": query,
                    "top": matches[0][1].get("stable_id") if matches else None,
                    "score": matches[0][0] if matches else 0,
                }
            )

    natural_failures = []
    natural_passes = 0
    for query, expected in NATURAL_QUERY_CASES:
        top_id, score = top_natural_match(search_skill_index, query)
        if top_id == expected:
            natural_passes += 1
        else:
            natural_failures.append(
                {"query": query, "expected": expected, "top": top_id, "score": score}
            )

    exact_rate = 1.0 - (len(exact_failures) / len(EXACT_API_QUERIES))
    natural_rate = natural_passes / len(NATURAL_QUERY_CASES)
    total_cases = (
        len(EXACT_API_QUERIES)
        + len(EXACT_STABLE_API_QUERIES)
        + len(NATURAL_QUERY_CASES)
    )
    print(f"Lookup cases: {total_cases}")
    print(f"Exact API: {len(EXACT_API_QUERIES)} cases, pass rate {exact_rate:.2%}")
    print(
        f"Exact stable API: {len(EXACT_STABLE_API_QUERIES)} cases, "
        f"pass rate {1.0 - (len(stable_failures) / len(EXACT_STABLE_API_QUERIES)):.2%}"
    )
    print(f"Natural language: {len(NATURAL_QUERY_CASES)} cases, top1 pass rate {natural_rate:.2%}")

    if exact_failures:
        print("Exact API failures:")
        for failure in exact_failures:
            print(f"- {failure}")
    if stable_failures:
        print("Exact stable API failures:")
        for failure in stable_failures:
            print(f"- {failure}")
    if natural_failures:
        print("Natural-language failures:")
        for failure in natural_failures:
            print(f"- {failure}")
    if total_cases < 100:
        raise SystemExit("Lookup validation requires at least 100 cases.")
    if exact_failures or stable_failures:
        raise SystemExit("Exact API lookup pass rate is below 100%.")
    if natural_rate < args.natural_threshold:
        raise SystemExit(
            f"Natural-language top1 pass rate {natural_rate:.2%} is below {args.natural_threshold:.2%}."
        )
    print("lookup validation passed")

if __name__ == "__main__":
    main()
