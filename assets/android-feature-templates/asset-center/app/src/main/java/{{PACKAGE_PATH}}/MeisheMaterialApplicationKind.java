package {{PACKAGE_NAME}};

public final class MeisheMaterialApplicationKind {
    public static final String FILTER = "filter";
    public static final String CLIP_EFFECT = "clip_effect";
    public static final String TRANSITION = "transition";
    public static final String CAPTION_STYLE = "caption_style";
    public static final String COMPOUND_CAPTION = "compound_caption";
    public static final String CAPTION_CONTEXT = "caption_context";
    public static final String CAPTION_RENDERER = "caption_renderer";
    public static final String CAPTION_ANIMATION = "caption_animation";
    public static final String CUSTOM_STICKER = "custom_sticker";
    public static final String STICKER_IN_ANIMATION = "sticker_in_animation";
    public static final String CAPTURE_SCENE = "capture_scene";
    public static final String AR_SCENE = "ar_scene";
    public static final String FACE_MESH = "face_mesh";
    public static final String MAKEUP = "makeup";
    public static final String THEME = "theme";
    public static final String FONT = "font";

    private MeisheMaterialApplicationKind() {
    }

    public static boolean requiresCaptionText(String applicationKind) {
        return CAPTION_STYLE.equals(applicationKind)
                || COMPOUND_CAPTION.equals(applicationKind)
                || CAPTION_CONTEXT.equals(applicationKind)
                || CAPTION_RENDERER.equals(applicationKind)
                || CAPTION_ANIMATION.equals(applicationKind)
                || FONT.equals(applicationKind);
    }

    public static boolean requiresCustomImage(String applicationKind) {
        return CUSTOM_STICKER.equals(applicationKind);
    }

    public static boolean isCaptureOnly(String applicationKind) {
        return CAPTURE_SCENE.equals(applicationKind)
                || AR_SCENE.equals(applicationKind)
                || FACE_MESH.equals(applicationKind)
                || MAKEUP.equals(applicationKind);
    }
}
