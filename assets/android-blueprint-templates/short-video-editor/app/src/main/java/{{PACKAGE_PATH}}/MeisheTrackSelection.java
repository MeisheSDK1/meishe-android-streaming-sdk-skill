package {{PACKAGE_NAME}};

public final class MeisheTrackSelection {
    public final int trackIndex;
    public final int clipIndex;
    public final long inPointUs;
    public final long outPointUs;

    public MeisheTrackSelection(int trackIndex, int clipIndex, long inPointUs, long outPointUs) {
        this.trackIndex = trackIndex;
        this.clipIndex = clipIndex;
        this.inPointUs = inPointUs;
        this.outPointUs = outPointUs;
    }

    public boolean isValid() {
        return trackIndex >= 0 && clipIndex >= 0 && outPointUs > inPointUs;
    }
}
