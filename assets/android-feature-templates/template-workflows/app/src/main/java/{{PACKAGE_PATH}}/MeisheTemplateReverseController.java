package {{PACKAGE_NAME}};

import android.os.Handler;

import com.meicam.sdk.NvsMediaFileConvertor;

import java.io.File;
import java.util.Hashtable;

public final class MeisheTemplateReverseController {
    private final NvsMediaFileConvertor convertor = new NvsMediaFileConvertor();

    public void registerCallback(
            NvsMediaFileConvertor.MeidaFileConvertorCallback callback,
            Handler callbackHandler) {
        MeisheThreading.requireMainThread("register media convertor callback");
        if (!convertor.isReleased() && callback != null && callbackHandler != null) {
            convertor.setMeidaFileConvertorCallback(callback, callbackHandler);
        }
    }

    public long generateReverseMedia(
            String sourcePath,
            String outputPath,
            long trimInUs,
            long trimOutUs,
            Integer outputHeight) {
        MeisheThreading.requireMainThread("generate reverse template footage");
        if (convertor.isReleased() || sourcePath == null || outputPath == null
                || !new File(sourcePath).isFile() || trimInUs < 0 || trimOutUs <= trimInUs) {
            return -1;
        }
        File output = new File(outputPath);
        File parent = output.getParentFile();
        if (parent != null && !parent.exists() && !parent.mkdirs()) {
            return -1;
        }
        Hashtable<String, Object> configurations = null;
        if (outputHeight != null && outputHeight > 0) {
            configurations = new Hashtable<>();
            configurations.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, outputHeight);
        }
        return convertor.convertMeidaFile(
                sourcePath,
                outputPath,
                true,
                trimInUs,
                trimOutUs,
                configurations);
    }

    public void cancel(long taskId) {
        MeisheThreading.requireMainThread("cancel reverse media conversion");
        if (!convertor.isReleased() && taskId >= 0) {
            convertor.cancelTask(taskId);
        }
    }

    public void release() {
        MeisheThreading.requireMainThread("release media convertor");
        if (!convertor.isReleased()) {
            convertor.release();
        }
    }
}
