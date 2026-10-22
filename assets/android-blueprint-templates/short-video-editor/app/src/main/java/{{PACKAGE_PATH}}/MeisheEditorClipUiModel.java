package {{PACKAGE_NAME}};

public final class MeisheEditorClipUiModel {
    public final int clipIndex;
    public final String displayName;
    public final long inPointUs;
    public final long outPointUs;

    public MeisheEditorClipUiModel(
            int clipIndex,
            String displayName,
            long inPointUs,
            long outPointUs) {
        this.clipIndex = clipIndex;
        this.displayName = displayName == null ? "" : displayName;
        this.inPointUs = Math.max(0, inPointUs);
        this.outPointUs = Math.max(this.inPointUs, outPointUs);
    }

    public long durationUs() {
        return outPointUs - inPointUs;
    }
}
