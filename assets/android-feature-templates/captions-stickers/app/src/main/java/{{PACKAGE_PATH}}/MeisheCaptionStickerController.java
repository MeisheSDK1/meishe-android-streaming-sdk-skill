package {{PACKAGE_NAME}};

import android.graphics.PointF;

import com.meicam.sdk.NvsAnimatedSticker;
import com.meicam.sdk.NvsCaption;
import com.meicam.sdk.NvsClipAnimatedSticker;
import com.meicam.sdk.NvsClipCaption;
import com.meicam.sdk.NvsClipCompoundCaption;
import com.meicam.sdk.NvsColor;
import com.meicam.sdk.NvsCompoundCaption;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTimelineAnimatedSticker;
import com.meicam.sdk.NvsTimelineCaption;
import com.meicam.sdk.NvsTimelineCompoundCaption;
import com.meicam.sdk.NvsTimelineVideoFx;
import com.meicam.sdk.NvsVideoClip;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class MeisheCaptionStickerController {
    public NvsTimelineCaption addCaption(
            NvsTimeline timeline,
            String text,
            long inPointUs,
            long durationUs,
            String captionStylePackageId) {
        MeisheThreading.requireMainThread("addCaption");
        if (timeline == null || text == null || durationUs <= 0) {
            return null;
        }
        return timeline.addCaption(text, Math.max(0, inPointUs), durationUs, captionStylePackageId);
    }

    public NvsTimelineAnimatedSticker addAnimatedSticker(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String stickerPackageId) {
        MeisheThreading.requireMainThread("addAnimatedSticker");
        if (timeline == null || stickerPackageId == null || stickerPackageId.isEmpty() || durationUs <= 0) {
            return null;
        }
        return timeline.addAnimatedSticker(Math.max(0, inPointUs), durationUs, stickerPackageId);
    }

    public NvsTimelineCompoundCaption addCompoundCaption(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String compoundCaptionPackageId) {
        MeisheThreading.requireMainThread("addCompoundCaption");
        if (timeline == null || compoundCaptionPackageId == null || compoundCaptionPackageId.isEmpty() || durationUs <= 0) {
            return null;
        }
        return timeline.addCompoundCaption(Math.max(0, inPointUs), durationUs, compoundCaptionPackageId);
    }

    public NvsClipCaption addClipCaption(
            NvsVideoClip clip,
            String text,
            long clipInPointUs,
            long durationUs,
            String captionStylePackageId) {
        MeisheThreading.requireMainThread("NvsVideoClip.addCaption");
        if (clip == null || text == null || durationUs <= 0 || clipInPointUs < 0) {
            return null;
        }
        return clip.addCaption(text, clipInPointUs, durationUs, captionStylePackageId);
    }

    public NvsClipCaption addClipModularCaption(
            NvsVideoClip clip,
            String text,
            long clipInPointUs,
            long durationUs) {
        MeisheThreading.requireMainThread("NvsVideoClip.addModularCaption");
        if (clip == null || text == null || durationUs <= 0 || clipInPointUs < 0) {
            return null;
        }
        return clip.addModularCaption(text, clipInPointUs, durationUs);
    }

    public NvsClipAnimatedSticker addClipAnimatedSticker(
            NvsVideoClip clip,
            long clipInPointUs,
            long durationUs,
            String stickerPackageId,
            String customImagePath) {
        MeisheThreading.requireMainThread("add clip animated sticker");
        if (clip == null || clipInPointUs < 0 || durationUs <= 0
                || stickerPackageId == null || stickerPackageId.isEmpty()) {
            return null;
        }
        if (customImagePath != null && !customImagePath.isEmpty()) {
            return clip.addCustomAnimatedSticker(
                    clipInPointUs,
                    durationUs,
                    stickerPackageId,
                    customImagePath);
        }
        return clip.addAnimatedSticker(clipInPointUs, durationUs, stickerPackageId);
    }

    public List<NvsClipAnimatedSticker> listClipAnimatedStickers(NvsVideoClip clip) {
        List<NvsClipAnimatedSticker> stickers = new ArrayList<>();
        if (clip == null) {
            return stickers;
        }
        for (NvsClipAnimatedSticker sticker = clip.getFirstAnimatedSticker();
                sticker != null;
                sticker = clip.getNextAnimatedSticker(sticker)) {
            stickers.add(sticker);
        }
        return stickers;
    }

    public NvsClipCaption removeClipCaption(NvsVideoClip clip, NvsClipCaption caption) {
        MeisheThreading.requireMainThread("NvsVideoClip.removeCaption");
        return clip == null || caption == null ? null : clip.removeCaption(caption);
    }

    public NvsClipAnimatedSticker removeClipAnimatedSticker(
            NvsVideoClip clip,
            NvsClipAnimatedSticker sticker) {
        MeisheThreading.requireMainThread("NvsVideoClip.removeAnimatedSticker");
        return clip == null || sticker == null ? null : clip.removeAnimatedSticker(sticker);
    }

    public void setCaptionText(NvsTimelineCaption caption, String text) {
        MeisheThreading.requireMainThread("NvsTimelineCaption.setText");
        if (caption != null && text != null) {
            caption.setText(text);
        }
    }

    public void applyReadableDefaultStyle(NvsTimelineCaption caption) {
        MeisheThreading.requireMainThread("configure default caption style");
        if (caption == null) {
            return;
        }
        caption.setTextAlignment(NvsCaption.TEXT_ALIGNMENT_CENTER);
        caption.setTextColor(new NvsColor(1.0f, 1.0f, 1.0f, 1.0f));
        caption.setFontSize(48.0f);
        caption.setDrawOutline(true);
        caption.setOutlineColor(new NvsColor(0.0f, 0.0f, 0.0f, 1.0f));
        caption.setOutlineWidth(4.0f);
    }

    public boolean configureCaptionTypography(
            NvsCaption caption,
            String fontFilePath,
            boolean bold,
            boolean italic,
            boolean underline,
            float lineSpacing,
            float opacity,
            NvsColor backgroundColor,
            float backgroundRadius,
            NvsColor shadowColor,
            PointF shadowOffset) {
        MeisheThreading.requireMainThread("configure caption typography");
        if (caption == null) {
            return false;
        }
        if (fontFilePath != null && !fontFilePath.isEmpty()) {
            caption.setFontByFilePath(fontFilePath);
        }
        caption.setBold(bold);
        caption.setItalic(italic);
        caption.setUnderline(underline);
        caption.setLineSpacing(lineSpacing);
        caption.setOpacity(Math.max(0.0f, Math.min(1.0f, opacity)));
        if (backgroundColor != null) {
            caption.setBackgroundColor(backgroundColor);
            caption.setBackgroundRadius(Math.max(0.0f, backgroundRadius));
        }
        boolean drawShadow = shadowColor != null && shadowOffset != null;
        caption.setDrawShadow(drawShadow);
        if (drawShadow) {
            caption.setShadowColor(shadowColor);
            caption.setShadowOffset(shadowOffset);
        }
        return caption.getText() != null;
    }

    public boolean configureCaptionTransform(
            NvsCaption caption,
            PointF translation,
            float scaleX,
            float scaleY,
            float rotationZ,
            float zValue,
            long keyFrameTimeUs) {
        MeisheThreading.requireMainThread("configure caption transform");
        if (caption == null || translation == null || scaleX <= 0 || scaleY <= 0) {
            return false;
        }
        caption.setRecordingUserOperation(true);
        caption.setCurrentKeyFrameTime(Math.max(0, keyFrameTimeUs));
        caption.setCaptionTranslation(translation);
        caption.setScaleX(scaleX);
        caption.setScaleY(scaleY);
        caption.setRotationZ(rotationZ);
        caption.setZValue(zValue);
        caption.setRecordingUserOperation(false);
        return true;
    }

    public boolean applyModularCaptionAssets(
            NvsCaption caption,
            String stylePackageId,
            String contextPackageId,
            String rendererPackageId,
            String animationPackageId,
            String inAnimationPackageId,
            String outAnimationPackageId,
            int animationPeriodMs,
            int inDurationMs,
            int outDurationMs) {
        MeisheThreading.requireMainThread("apply modular caption assets");
        if (caption == null) {
            return false;
        }
        boolean applied = true;
        if (stylePackageId != null && !stylePackageId.isEmpty()) {
            applied &= caption.applyCaptionStyle(stylePackageId);
        }
        if (contextPackageId != null && !contextPackageId.isEmpty()) {
            applied &= caption.applyModularCaptionContext(contextPackageId);
        }
        if (rendererPackageId != null && !rendererPackageId.isEmpty()) {
            applied &= caption.applyModularCaptionRenderer(rendererPackageId);
        }
        if (animationPackageId != null && !animationPackageId.isEmpty()) {
            applied &= caption.applyModularCaptionAnimation(animationPackageId);
            caption.setModularCaptionAnimationPeroid(Math.max(0, animationPeriodMs));
        }
        if (inAnimationPackageId != null && !inAnimationPackageId.isEmpty()) {
            applied &= caption.applyModularCaptionInAnimation(inAnimationPackageId);
            caption.setModularCaptionInAnimationDuration(Math.max(0, inDurationMs));
        }
        if (outAnimationPackageId != null && !outAnimationPackageId.isEmpty()) {
            applied &= caption.applyModularCaptionOutAnimation(outAnimationPackageId);
            caption.setModularCaptionOutAnimationDuration(Math.max(0, outDurationMs));
        }
        return applied;
    }

    public boolean configureAnimatedSticker(
            NvsAnimatedSticker sticker,
            PointF translation,
            PointF scaleAnchor,
            float scale,
            float rotation,
            boolean horizontalFlip,
            float zValue,
            float leftVolume,
            float rightVolume,
            String periodAnimationPackageId,
            String inAnimationPackageId,
            String outAnimationPackageId,
            int animationPeriodMs,
            int inDurationMs,
            int outDurationMs) {
        MeisheThreading.requireMainThread("configure animated sticker");
        if (sticker == null || translation == null || scaleAnchor == null || scale <= 0) {
            return false;
        }
        sticker.translateAnimatedSticker(translation);
        sticker.scaleAnimatedSticker(scale, scaleAnchor);
        sticker.rotateAnimatedSticker(rotation);
        sticker.setHorizontalFlip(horizontalFlip);
        sticker.setZValue(zValue);
        sticker.setVolumeGain(leftVolume, rightVolume);
        boolean applied = sticker.getHorizontalFlip() == horizontalFlip;
        if (periodAnimationPackageId != null && !periodAnimationPackageId.isEmpty()) {
            applied &= sticker.applyAnimatedStickerPeriodAnimation(periodAnimationPackageId);
            sticker.setAnimatedStickerAnimationPeriod(Math.max(0, animationPeriodMs));
        }
        if (inAnimationPackageId != null && !inAnimationPackageId.isEmpty()) {
            applied &= sticker.applyAnimatedStickerInAnimation(inAnimationPackageId);
            sticker.setAnimatedStickerInAnimationDuration(Math.max(0, inDurationMs));
        }
        if (outAnimationPackageId != null && !outAnimationPackageId.isEmpty()) {
            applied &= sticker.applyAnimatedStickerOutAnimation(outAnimationPackageId);
            sticker.setAnimatedStickerOutAnimationDuration(Math.max(0, outDurationMs));
        }
        return applied;
    }

    public void setCompoundCaptionText(NvsTimelineCompoundCaption caption, int captionIndex, String text) {
        MeisheThreading.requireMainThread("NvsTimelineCompoundCaption.setText");
        if (caption != null && text != null && captionIndex >= 0) {
            caption.setText(captionIndex, text);
        }
    }

    public void setCompoundCaptionTextAt(
            NvsCompoundCaption caption,
            int captionIndex,
            String text) {
        MeisheThreading.requireMainThread("NvsCompoundCaption.setText");
        if (caption != null && captionIndex >= 0 && text != null) {
            caption.setText(captionIndex, text);
        }
    }

    public void removeCaption(NvsTimeline timeline, NvsTimelineCaption caption) {
        MeisheThreading.requireMainThread("removeCaption");
        if (timeline != null && caption != null) {
            timeline.removeCaption(caption);
        }
    }

    public void removeAnimatedSticker(NvsTimeline timeline, NvsTimelineAnimatedSticker sticker) {
        MeisheThreading.requireMainThread("removeAnimatedSticker");
        if (timeline != null && sticker != null) {
            timeline.removeAnimatedSticker(sticker);
        }
    }

    public void removeCompoundCaption(NvsTimeline timeline, NvsTimelineCompoundCaption caption) {
        MeisheThreading.requireMainThread("removeCompoundCaption");
        if (timeline != null && caption != null) {
            timeline.removeCompoundCaption(caption);
        }
    }

    public List<NvsTimelineCaption> listTimelineCaptions(NvsTimeline timeline) {
        MeisheThreading.requireMainThread("iterate timeline captions");
        List<NvsTimelineCaption> captions = new ArrayList<>();
        if (timeline == null) {
            return captions;
        }
        for (NvsTimelineCaption caption = timeline.getFirstCaption();
                caption != null;
                caption = timeline.getNextCaption(caption)) {
            captions.add(caption);
        }
        return captions;
    }

    public List<NvsTimelineCompoundCaption> listCompoundCaptions(NvsTimeline timeline) {
        MeisheThreading.requireMainThread("iterate compound captions");
        List<NvsTimelineCompoundCaption> captions = new ArrayList<>();
        if (timeline == null) {
            return captions;
        }
        for (NvsTimelineCompoundCaption caption = timeline.getFirstCompoundCaption();
                caption != null;
                caption = timeline.getNextCaption(caption)) {
            captions.add(caption);
        }
        return captions;
    }

    public List<NvsTimelineAnimatedSticker> listAnimatedStickers(NvsTimeline timeline) {
        MeisheThreading.requireMainThread("iterate animated stickers");
        List<NvsTimelineAnimatedSticker> stickers = new ArrayList<>();
        if (timeline == null) {
            return stickers;
        }
        for (NvsTimelineAnimatedSticker sticker = timeline.getFirstAnimatedSticker();
                sticker != null;
                sticker = timeline.getNextAnimatedSticker(sticker)) {
            stickers.add(sticker);
        }
        return stickers;
    }

    public List<NvsTimelineAnimatedSticker> animatedStickersAt(
            NvsTimeline timeline,
            long timelinePositionUs) {
        MeisheThreading.requireMainThread("getAnimatedStickersByTimelinePosition");
        if (timeline == null) {
            return Collections.emptyList();
        }
        List<NvsTimelineAnimatedSticker> stickers =
                timeline.getAnimatedStickersByTimelinePosition(Math.max(0, timelinePositionUs));
        return stickers == null ? Collections.<NvsTimelineAnimatedSticker>emptyList() : stickers;
    }

    public NvsTimelineAnimatedSticker addCustomAnimatedSticker(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String packageId,
            String imagePath) {
        MeisheThreading.requireMainThread("NvsTimeline.addCustomAnimatedSticker");
        if (timeline == null || durationUs <= 0 || packageId == null || packageId.isEmpty()
                || imagePath == null || imagePath.isEmpty()) {
            return null;
        }
        return timeline.addCustomAnimatedSticker(
                Math.max(0, inPointUs),
                durationUs,
                packageId,
                imagePath);
    }

    public long[] timelineCaptionRange(NvsTimelineCaption caption) {
        if (caption == null) {
            return new long[] {0, 0};
        }
        return new long[] {caption.getInPoint(), caption.getOutPoint()};
    }

    public long[] compoundCaptionRange(NvsTimelineCompoundCaption caption) {
        if (caption == null) {
            return new long[] {0, 0};
        }
        return new long[] {caption.getInPoint(), caption.getOutPoint()};
    }

    public long[] animatedStickerRange(NvsTimelineAnimatedSticker sticker) {
        if (sticker == null) {
            return new long[] {0, 0};
        }
        return new long[] {sticker.getInPoint(), sticker.getOutPoint()};
    }

    public long[] clipCaptionRange(NvsClipCaption caption) {
        if (caption == null) {
            return new long[] {0, 0};
        }
        return new long[] {caption.getInPoint(), caption.getOutPoint()};
    }

    public long[] clipAnimatedStickerRange(NvsClipAnimatedSticker sticker) {
        if (sticker == null) {
            return new long[] {0, 0};
        }
        return new long[] {sticker.getInPoint(), sticker.getOutPoint()};
    }

    public List<NvsClipCaption> listClipCaptions(NvsVideoClip clip) {
        List<NvsClipCaption> captions = new ArrayList<>();
        if (clip == null) {
            return captions;
        }
        for (NvsClipCaption caption = clip.getFirstCaption();
                caption != null;
                caption = clip.getNextCaption(caption)) {
            captions.add(caption);
        }
        return captions;
    }

    public List<NvsClipCompoundCaption> listClipCompoundCaptions(NvsVideoClip clip) {
        List<NvsClipCompoundCaption> captions = new ArrayList<>();
        if (clip == null) {
            return captions;
        }
        for (NvsClipCompoundCaption caption = clip.getFirstCompoundCaption();
                caption != null;
                caption = clip.getNextCaption(caption)) {
            captions.add(caption);
        }
        return captions;
    }

    public String registerFont(NvsStreamingContext streamingContext, String fontPath) {
        MeisheThreading.requireMainThread("NvsStreamingContext.registerFontByFilePath");
        if (streamingContext == null || fontPath == null || fontPath.isEmpty()) {
            return "";
        }
        String family = streamingContext.registerFontByFilePath(fontPath);
        return family == null ? "" : family;
    }

    public void setAbsoluteLetterSpacing(NvsCaption caption, float spacing) {
        MeisheThreading.requireMainThread("NvsCaption.setLetterSpacing");
        if (caption == null) {
            return;
        }
        caption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
        caption.setLetterSpacing(spacing);
    }

    public List<NvsTimelineCaption> addTimedLyrics(
            NvsTimeline timeline,
            List<String> lyricLines,
            List<Long> inPointsUs,
            List<Long> outPointsUs,
            String captionStylePackageId) {
        MeisheThreading.requireMainThread("add timed lyric captions");
        List<NvsTimelineCaption> captions = new ArrayList<>();
        if (timeline == null || lyricLines == null || inPointsUs == null || outPointsUs == null) {
            return captions;
        }
        int count = Math.min(lyricLines.size(), Math.min(inPointsUs.size(), outPointsUs.size()));
        for (int index = 0; index < count; index++) {
            String text = lyricLines.get(index);
            Long inPoint = inPointsUs.get(index);
            Long outPoint = outPointsUs.get(index);
            if (text == null || inPoint == null || outPoint == null || outPoint <= inPoint) {
                continue;
            }
            long safeInPoint = Math.max(0, inPoint);
            NvsTimelineCaption caption = timeline.addCaption(
                    text,
                    safeInPoint,
                    outPoint - safeInPoint,
                    captionStylePackageId);
            if (caption != null) {
                captions.add(caption);
            }
        }
        return captions;
    }

    public NvsTimelineVideoFx addFlipCaptionStoryboard(
            NvsTimeline timeline,
            String storyboardDescription) {
        MeisheThreading.requireMainThread("add flip-caption storyboard");
        if (timeline == null || storyboardDescription == null || storyboardDescription.isEmpty()
                || timeline.getDuration() <= 0) {
            return null;
        }
        NvsTimelineVideoFx storyboardFx = timeline.addBuiltinTimelineVideoFx(
                0,
                timeline.getDuration(),
                "Storyboard");
        if (storyboardFx != null) {
            storyboardFx.setStringVal("Description String", storyboardDescription);
            storyboardFx.setBooleanVal("Is Caption", true);
        }
        return storyboardFx;
    }
}
