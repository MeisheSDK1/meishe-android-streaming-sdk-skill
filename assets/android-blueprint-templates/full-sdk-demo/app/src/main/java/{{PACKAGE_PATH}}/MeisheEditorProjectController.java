package {{PACKAGE_NAME}};

import android.content.Context;

public final class MeisheEditorProjectController {
    private final Context context;
    private final String projectId;
    private final int width;
    private final int height;
    private final MeisheEditorSessionController session;
    private final MeisheEditHistory history = new MeisheEditHistory();
    private final MeisheEditorProjectRepository repository;
    private MeisheEditorProject currentProject;
    private String editorStateJson = MeisheEditorProjectStore.emptyEditorState();
    private int restoredFeatureCount;

    public MeisheEditorProjectController(
            Context context,
            String projectId,
            int width,
            int height,
            MeisheEditorSessionController session) {
        if (context == null || projectId == null || projectId.isEmpty() || session == null) {
            throw new IllegalArgumentException("project context, id, and session are required");
        }
        this.context = context.getApplicationContext();
        this.projectId = projectId;
        this.width = width;
        this.height = height;
        this.session = session;
        repository = new MeisheEditorProjectRepository(this.context);
    }

    public String loadSerializedProject(boolean restoreProject) {
        currentProject = restoreProject
                ? repository.loadExistingOrMigrate(projectId, width, height)
                : null;
        if (currentProject == null) {
            currentProject = MeisheEditorProject.create(projectId, width, height);
        }
        editorStateJson = currentProject.editorState();
        return currentProject.serialize();
    }

    public int restoreEditorFeatures(boolean restoreProject) {
        currentProject.synchronizeTimeline(session.timeline());
        restoredFeatureCount = restoreProject && session.canRebuildEditorFeatures()
                ? MeisheEditorProjectStore.restoreEditorFeaturesByClipIds(
                        session.timeline(),
                        editorStateJson,
                        currentProject.clipIds())
                : 0;
        persist();
        history.captureProject(currentProject.serialize());
        return restoredFeatureCount;
    }

    public boolean persist() {
        if (currentProject == null || session.timeline() == null) {
            return false;
        }
        currentProject.synchronizeTimeline(session.timeline());
        currentProject.setEditorState(editorStateJson);
        boolean saved = repository.save(currentProject);
        if (saved && session.hostContract() != null) {
            session.hostContract().onProjectSaved(
                    projectId,
                    repository.projectFilePath(projectId));
        }
        return saved;
    }

    public void captureAndPersist() {
        if (persist()) {
            history.captureProject(currentProject.serialize());
        }
    }

    public int reapplyEditorState() {
        if (!session.canRebuildEditorFeatures()) {
            return 0;
        }
        MeisheEditorProjectStore.clearEditorFeatures(session.timeline());
        restoredFeatureCount = MeisheEditorProjectStore.restoreEditorFeaturesByClipIds(
                session.timeline(),
                editorStateJson,
                currentProject.clipIds());
        return restoredFeatureCount;
    }

    public boolean undo() {
        if (!session.canMutateStructure() || !session.canRebuildEditorFeatures()) {
            return false;
        }
        return restoreHistory(history.undoProject());
    }

    public boolean redo() {
        if (!session.canMutateStructure() || !session.canRebuildEditorFeatures()) {
            return false;
        }
        return restoreHistory(history.redoProject());
    }

    public void onClipSplit(int sourceIndex) {
        String sourceClipId = currentProject.clipIdAt(sourceIndex);
        String newClipId = currentProject.splitClip(sourceIndex);
        editorStateJson = MeisheEditorProjectStore.onClipSplitById(
                editorStateJson,
                sourceClipId,
                newClipId);
    }

    public void onClipRemoved(int removedIndex) {
        String removedClipId = currentProject.removeClip(removedIndex);
        editorStateJson = MeisheEditorProjectStore.onClipRemovedById(
                editorStateJson,
                removedClipId);
    }

    public void onClipMoved(int sourceIndex, int targetIndex) {
        if (currentProject.moveClip(sourceIndex, targetIndex)) {
            editorStateJson = MeisheEditorProjectStore.onClipMovedById(editorStateJson);
        }
    }

    public String clipIdAt(int index) {
        return currentProject == null ? "" : currentProject.clipIdAt(index);
    }

    public String projectFilePath() {
        return repository.projectFilePath(projectId);
    }

    public String editorState() {
        return editorStateJson;
    }

    public void replaceEditorState(String value) {
        editorStateJson = value == null
                ? MeisheEditorProjectStore.emptyEditorState()
                : value;
    }

    public int restoredFeatureCount() {
        return restoredFeatureCount;
    }

    public String selectedCaptionStylePackageId() {
        return MeisheEditorProjectStore.selectedCaptionStylePackageId(editorStateJson);
    }

    public void selectCaptionStyle(String packageId) {
        editorStateJson = MeisheEditorProjectStore.setSelectedCaptionStylePackageId(
                editorStateJson,
                packageId);
        persist();
    }

    private boolean restoreHistory(String serializedProject) {
        if (serializedProject == null || serializedProject.isEmpty()) {
            return false;
        }
        currentProject = MeisheEditorProject.fromSerialized(
                projectId,
                serializedProject,
                width,
                height);
        editorStateJson = currentProject.editorState();
        if (currentProject.restoreTimeline(session.timeline(), true) == 0) {
            return false;
        }
        reapplyEditorState();
        return persist();
    }
}
