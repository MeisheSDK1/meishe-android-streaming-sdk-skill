package {{PACKAGE_NAME}};

public final class MeisheAppliedMaterial {
    public static final String TYPE_CLIP_EFFECT = "clip_effect";
    public static final String TYPE_CAPTION = "caption";
    public static final String TYPE_COMPOUND_CAPTION = "compound_caption";
    public static final String TYPE_STICKER = "sticker";
    public static final String TYPE_TRANSITION = "transition";
    public static final String TYPE_AUDIO = "audio";
    public static final String TYPE_THEME = "theme";

    public final String id;
    public final String type;
    public final String title;
    public final String summary;
    public final String text;
    public final long durationUs;
    public final float intensity;
    public final float fontSize;
    public final float opacity;
    public final float scale;
    public final float rotation;
    public final float volume;
    public final long fadeInUs;
    public final long fadeOutUs;

    public MeisheAppliedMaterial(
            String id,
            String type,
            String title,
            String summary,
            String text,
            long durationUs,
            float intensity,
            float fontSize,
            float opacity,
            float scale,
            float rotation,
            float volume,
            long fadeInUs,
            long fadeOutUs) {
        this.id = id == null ? "" : id;
        this.type = type == null ? "" : type;
        this.title = title == null ? "" : title;
        this.summary = summary == null ? "" : summary;
        this.text = text == null ? "" : text;
        this.durationUs = durationUs;
        this.intensity = intensity;
        this.fontSize = fontSize;
        this.opacity = opacity;
        this.scale = scale;
        this.rotation = rotation;
        this.volume = volume;
        this.fadeInUs = fadeInUs;
        this.fadeOutUs = fadeOutUs;
    }

    public static final class Edits {
        public String text;
        public long durationUs;
        public float intensity;
        public float fontSize;
        public float opacity;
        public float scale;
        public float rotation;
        public float volume;
        public long fadeInUs;
        public long fadeOutUs;
    }
}
