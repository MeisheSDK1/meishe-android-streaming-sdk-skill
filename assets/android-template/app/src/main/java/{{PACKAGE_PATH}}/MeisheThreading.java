package {{PACKAGE_NAME}};

import android.os.Looper;

import com.meicam.sdk.NvsUtils;

public final class MeisheThreading {
    private MeisheThreading() {
    }

    public static void requireMainThread(String operation) {
        if (!NvsUtils.checkFunctionInMainThread()
                || android.os.Looper.myLooper() != android.os.Looper.getMainLooper()) {
            throw new IllegalStateException(operation + " must run on the Android UI thread");
        }
    }
}
