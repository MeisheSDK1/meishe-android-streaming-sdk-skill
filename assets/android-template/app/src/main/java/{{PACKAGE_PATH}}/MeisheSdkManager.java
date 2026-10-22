package {{PACKAGE_NAME}};

import android.content.Context;

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsStreamingContext;

public final class MeisheSdkManager {
    private final Context appContext;
    private NvsStreamingContext streamingContext;

    public MeisheSdkManager(Context context) {
        this.appContext = context.getApplicationContext();
    }

    public boolean initialize() {
        MeisheThreading.requireMainThread("NvsStreamingContext.init");
        if (NvsStreamingContext.getInstance() != null) {
            streamingContext = NvsStreamingContext.getInstance();
            return true;
        }
        String licensePath = "assets:/meishesdk.lic";
        int flags = NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP;
        streamingContext = NvsStreamingContext.init(appContext, licensePath, flags);
        return streamingContext != null;
    }

    public NvsStreamingContext getStreamingContext() {
        if (streamingContext == null) {
            initialize();
        }
        return streamingContext;
    }

    public void configureRuntime(int maxReaderCount, int iconSize) {
        MeisheThreading.requireMainThread("configure NvsStreamingContext");
        if (maxReaderCount > 0) {
            NvsStreamingContext.setMaxReaderCount(maxReaderCount);
        }
        if (iconSize > 0) {
            NvsStreamingContext.setIconSize(iconSize);
        }
    }

    public void stopEngine() {
        MeisheThreading.requireMainThread("NvsStreamingContext.stop");
        if (streamingContext != null) {
            streamingContext.stop();
        }
    }

    public boolean initializeForActivity(android.app.Activity activity, int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.init");
        if (activity == null) {
            return false;
        }
        streamingContext = NvsStreamingContext.init(
                activity,
                "assets:/meishesdk.lic",
                flags);
        return streamingContext != null;
    }

    public boolean initializeForActivityDefault(android.app.Activity activity) {
        MeisheThreading.requireMainThread("NvsStreamingContext.init");
        if (activity == null) {
            return false;
        }
        if (NvsStreamingContext.getInstance() != null) {
            streamingContext = NvsStreamingContext.getInstance();
            return true;
        }
        streamingContext = NvsStreamingContext.init(activity, "assets:/meishesdk.lic");
        return streamingContext != null;
    }

    public NvsAssetPackageManager getAssetPackageManager() {
        MeisheThreading.requireMainThread("NvsStreamingContext.getAssetPackageManager");
        return streamingContext == null ? null : streamingContext.getAssetPackageManager();
    }

    public void stopEngineWithFlags(int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.stop");
        if (streamingContext != null) {
            streamingContext.stop(flags);
        }
    }
}
