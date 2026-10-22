package {{PACKAGE_NAME}};

import android.graphics.Bitmap;

import com.meicam.sdk.NvsAVFileInfo;
import com.meicam.sdk.NvsSize;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsVideoFrameRetriever;

public final class MeisheMediaProbeController {
    private final NvsStreamingContext streamingContext;

    public MeisheMediaProbeController(NvsStreamingContext streamingContext) {
        this.streamingContext = streamingContext;
    }

    public MediaProbe probe(String filePath) {
        MeisheThreading.requireMainThread("getAVFileInfo");
        if (streamingContext == null || filePath == null || filePath.isEmpty()) {
            return null;
        }
        NvsAVFileInfo fileInfo = streamingContext.getAVFileInfo(filePath);
        if (fileInfo == null) {
            fileInfo = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
        }
        if (fileInfo == null) {
            return null;
        }
        long durationUs = fileInfo.getDuration();
        NvsSize size = fileInfo.getVideoStreamDimension(0);
        int rotation = fileInfo.getVideoStreamRotation(0);
        return new MediaProbe(durationUs, size, rotation);
    }

    public NvsAVFileInfo probeWithFlags(String filePath, int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.getAVFileInfo");
        if (streamingContext == null || filePath == null || filePath.isEmpty()) {
            return null;
        }
        return streamingContext.getAVFileInfo(filePath, flags);
    }

    public NvsVideoFrameRetriever createFrameRetriever(String filePath) {
        MeisheThreading.requireMainThread("NvsStreamingContext.createVideoFrameRetriever");
        if (streamingContext == null || filePath == null || filePath.isEmpty()) {
            return null;
        }
        return streamingContext.createVideoFrameRetriever(filePath);
    }

    public Bitmap retrieveFrame(
            NvsVideoFrameRetriever retriever,
            long timestampUs,
            int flags,
            int customVideoFrameHeight) {
        if (retriever == null || timestampUs < 0) {
            return null;
        }
        if (customVideoFrameHeight > 0) {
            return retriever.getFrameAtTimeWithCustomVideoFrameHeight(
                    timestampUs,
                    customVideoFrameHeight);
        }
        return retriever.getFrameAtTime(timestampUs, flags);
    }

    public void releaseFrameRetriever(NvsVideoFrameRetriever retriever) {
        MeisheThreading.requireMainThread("NvsVideoFrameRetriever.release");
        if (retriever != null) {
            retriever.release();
        }
    }

    public static final class MediaProbe {
        public final long durationUs;
        public final NvsSize size;
        public final int rotation;

        public MediaProbe(long durationUs, NvsSize size, int rotation) {
            this.durationUs = durationUs;
            this.size = size;
            this.rotation = rotation;
        }
    }
}
