package {{PACKAGE_NAME}};

import android.app.Activity;

import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;

public interface MeisheEditorHostContract {
    MeisheTimelineOwnership timelineOwnership();

    NvsTimeline acquireTimeline(
            NvsStreamingContext streamingContext,
            int requestedWidth,
            int requestedHeight);

    default NvsLiveWindow acquireLiveWindow(Activity activity) {
        return null;
    }

    default boolean allowStructuralMutations() {
        return timelineOwnership() == MeisheTimelineOwnership.EDITOR_OWNED;
    }

    default boolean allowEditorFeatureRebuild() {
        return timelineOwnership() == MeisheTimelineOwnership.EDITOR_OWNED;
    }

    default void onTimelineReady(NvsTimeline timeline) {
    }

    default void onProjectSaved(String projectId, String projectFilePath) {
    }

    default void onEditorClosed(NvsTimeline timeline) {
    }
}
