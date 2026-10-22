package {{PACKAGE_NAME}};

import android.content.Context;
import java.io.File;

public final class MeisheEditorProjectRepository {
    private static final String PREFERENCES = "meishe_projects";
    private static final String LATEST_PROJECT_ID = "latest_project_id";

    private final Context context;

    public MeisheEditorProjectRepository(Context context) {
        if (context == null) {
            throw new IllegalArgumentException("context is required");
        }
        this.context = context.getApplicationContext();
    }

    public MeisheEditorProject loadOrCreate(String projectId, int width, int height) {
        MeisheEditorProject existing = loadExistingOrMigrate(projectId, width, height);
        return existing == null
                ? MeisheEditorProject.create(projectId, width, height)
                : existing;
    }

    public MeisheEditorProject loadExistingOrMigrate(
            String projectId,
            int fallbackWidth,
            int fallbackHeight) {
        if (projectId == null || projectId.isEmpty()) {
            return null;
        }
        String fileState = readProjectFile(projectId);
        if (!fileState.isEmpty()) {
            return MeisheEditorProject.fromSerialized(
                    projectId,
                    fileState,
                    fallbackWidth,
                    fallbackHeight);
        }
        String legacyState = context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
                .getString(projectId, "");
        if (legacyState == null || legacyState.isEmpty()) {
            return null;
        }
        MeisheEditorProject migrated = MeisheEditorProject.fromSerialized(
                projectId,
                legacyState,
                fallbackWidth,
                fallbackHeight);
        return save(migrated) ? migrated : null;
    }

    public boolean save(MeisheEditorProject project) {
        if (project == null || project.projectId().isEmpty()) {
            return false;
        }
        if (!MeisheAppSupport.saveAtomicProjectState(
                context,
                project.projectId(),
                project.serialize())) {
            return false;
        }
        return context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
                .edit()
                .putString(LATEST_PROJECT_ID, project.projectId())
                .commit();
    }

    public String latestProjectId() {
        return context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
                .getString(LATEST_PROJECT_ID, "");
    }

    public boolean hasProject(String projectId) {
        if (projectId == null || projectId.isEmpty()) {
            return false;
        }
        return projectFile(projectId).isFile()
                || !context.getSharedPreferences(PREFERENCES, Context.MODE_PRIVATE)
                .getString(projectId, "")
                .isEmpty();
    }

    public String projectFilePath(String projectId) {
        return projectFile(projectId).getAbsolutePath();
    }

    private String readProjectFile(String projectId) {
        return MeisheAppSupport.loadAtomicProjectState(context, projectId);
    }

    private File projectFile(String projectId) {
        String safeId = projectId == null
                ? "invalid"
                : projectId.replaceAll("[^A-Za-z0-9._-]", "_");
        File root = new File(context.getFilesDir(), "meishe-projects");
        return new File(new File(root, safeId), "project.json");
    }
}
