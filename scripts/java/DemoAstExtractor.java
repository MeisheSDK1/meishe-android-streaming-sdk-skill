import com.sun.source.tree.ClassTree;
import com.sun.source.tree.CompilationUnitTree;
import com.sun.source.tree.ExpressionTree;
import com.sun.source.tree.MemberSelectTree;
import com.sun.source.tree.MethodInvocationTree;
import com.sun.source.tree.MethodTree;
import com.sun.source.tree.Tree;
import com.sun.source.tree.VariableTree;
import com.sun.source.util.JavacTask;
import com.sun.source.util.SourcePositions;
import com.sun.source.util.TreeScanner;
import com.sun.source.util.Trees;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;

/**
 * Syntax-only Java extractor used while refreshing the skill from the external Demo.
 *
 * <p>The compiler tree API gives stable method ranges and invocation order without requiring
 * Android or SDK dependencies to resolve. Output is JSON Lines so the Python orchestrator can
 * stream and compact it before anything is persisted in the skill.</p>
 */
public final class DemoAstExtractor {
    private static final Pattern NVS_TYPE = Pattern.compile("\\b(Nvs[A-Za-z0-9_]+)\\b");
    private static final List<String> IGNORED_DIRS =
            List.of("build", ".gradle", ".idea", "captures", "outputs");

    private DemoAstExtractor() {
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            throw new IllegalArgumentException("Usage: DemoAstExtractor <demo-root>");
        }
        Path root = Paths.get(args[0]).toAbsolutePath().normalize();
        if (!Files.isDirectory(root)) {
            throw new IllegalArgumentException("Missing demo root: " + root);
        }
        List<Path> sources = findJavaSources(root);
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        if (compiler == null) {
            throw new IllegalStateException("A JDK with javac is required");
        }
        try (StandardJavaFileManager fileManager =
                     compiler.getStandardFileManager(null, null, StandardCharsets.UTF_8)) {
            Iterable<? extends JavaFileObject> files =
                    fileManager.getJavaFileObjectsFromPaths(sources);
            JavacTask task = (JavacTask) compiler.getTask(
                    null,
                    fileManager,
                    diagnostic -> { },
                    List.of("-proc:none", "-Xlint:none"),
                    null,
                    files);
            Trees trees = Trees.instance(task);
            SourcePositions positions = trees.getSourcePositions();
            for (CompilationUnitTree unit : task.parse()) {
                emitCompilationUnit(root, unit, positions);
            }
        }
    }

    private static List<Path> findJavaSources(Path root) throws IOException {
        List<Path> sources = new ArrayList<>();
        try (Stream<Path> stream = Files.walk(root)) {
            stream.filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".java"))
                    .filter(path -> !hasIgnoredPart(root.relativize(path)))
                    .forEach(sources::add);
        }
        sources.sort(Comparator.comparing(Path::toString));
        return sources;
    }

    private static boolean hasIgnoredPart(Path relativePath) {
        for (Path part : relativePath) {
            if (IGNORED_DIRS.contains(part.toString())) {
                return true;
            }
        }
        return false;
    }

    private static void emitCompilationUnit(
            Path root,
            CompilationUnitTree unit,
            SourcePositions positions) throws IOException {
        Path sourcePath = Paths.get(unit.getSourceFile().toUri()).toAbsolutePath().normalize();
        String relativePath = root.relativize(sourcePath).toString().replace('\\', '/');
        String source = Files.readString(sourcePath, StandardCharsets.UTF_8);
        for (Tree declaration : unit.getTypeDecls()) {
            if (declaration instanceof ClassTree) {
                emitClass(relativePath, source, unit, positions, (ClassTree) declaration, new HashMap<>());
            }
        }
    }

    private static void emitClass(
            String relativePath,
            String source,
            CompilationUnitTree unit,
            SourcePositions positions,
            ClassTree classTree,
            Map<String, String> inheritedSymbols) {
        Map<String, String> classSymbols = new HashMap<>(inheritedSymbols);
        for (Tree member : classTree.getMembers()) {
            if (member instanceof VariableTree) {
                addDeclaredType(classSymbols, (VariableTree) member);
            }
        }
        for (Tree member : classTree.getMembers()) {
            if (member instanceof MethodTree) {
                emitMethod(relativePath, source, unit, positions, (MethodTree) member, classSymbols);
            } else if (member instanceof ClassTree) {
                emitClass(
                        relativePath,
                        source,
                        unit,
                        positions,
                        (ClassTree) member,
                        classSymbols);
            }
        }
    }

    private static void emitMethod(
            String relativePath,
            String source,
            CompilationUnitTree unit,
            SourcePositions positions,
            MethodTree method,
            Map<String, String> classSymbols) {
        long startOffset = positions.getStartPosition(unit, method);
        long endOffset = positions.getEndPosition(unit, method);
        if (startOffset < 0 || endOffset <= startOffset || endOffset > source.length()) {
            return;
        }
        Map<String, String> symbols = new HashMap<>(classSymbols);
        for (VariableTree parameter : method.getParameters()) {
            addDeclaredType(symbols, parameter);
        }
        InvocationScanner scanner =
                new InvocationScanner(unit, positions, symbols);
        scanner.scan(method.getBody(), null);
        if (scanner.invocations.isEmpty()) {
            return;
        }
        long startLine = unit.getLineMap().getLineNumber(startOffset);
        long endLine = unit.getLineMap().getLineNumber(Math.max(startOffset, endOffset - 1));
        String methodSource = source.substring((int) startOffset, (int) endOffset);
        StringBuilder output = new StringBuilder();
        output.append('{');
        field(output, "source", relativePath).append(',');
        field(output, "method", method.getName().toString()).append(',');
        numberField(output, "start_line", startLine).append(',');
        numberField(output, "end_line", endLine).append(',');
        field(output, "code", methodSource).append(',');
        output.append("\"invocations\":[");
        for (int index = 0; index < scanner.invocations.size(); index++) {
            if (index > 0) {
                output.append(',');
            }
            output.append(scanner.invocations.get(index).toJson());
        }
        output.append("]}");
        System.out.println(output);
    }

    private static void addDeclaredType(Map<String, String> symbols, VariableTree variable) {
        if (variable.getType() == null) {
            return;
        }
        Matcher matcher = NVS_TYPE.matcher(variable.getType().toString());
        if (matcher.find()) {
            symbols.put(variable.getName().toString(), matcher.group(1));
        }
    }

    private static final class InvocationScanner extends TreeScanner<Void, Void> {
        private final CompilationUnitTree unit;
        private final SourcePositions positions;
        private final Deque<Map<String, String>> scopes = new ArrayDeque<>();
        private final List<Invocation> invocations = new ArrayList<>();

        InvocationScanner(
                CompilationUnitTree unit,
                SourcePositions positions,
                Map<String, String> initialSymbols) {
            this.unit = unit;
            this.positions = positions;
            scopes.push(new LinkedHashMap<>(initialSymbols));
        }

        @Override
        public Void visitVariable(VariableTree variable, Void unused) {
            addDeclaredType(scopes.peek(), variable);
            return super.visitVariable(variable, unused);
        }

        @Override
        public Void visitMethodInvocation(MethodInvocationTree invocation, Void unused) {
            ExpressionTree select = invocation.getMethodSelect();
            String methodName;
            String receiver;
            if (select instanceof MemberSelectTree) {
                MemberSelectTree memberSelect = (MemberSelectTree) select;
                methodName = memberSelect.getIdentifier().toString();
                receiver = memberSelect.getExpression().toString();
            } else {
                methodName = select.toString();
                receiver = "";
            }
            String owner = inferOwner(receiver);
            if (!owner.isEmpty()) {
                long offset = positions.getStartPosition(unit, invocation);
                long line = offset < 0 ? 0 : unit.getLineMap().getLineNumber(offset);
                invocations.add(new Invocation(
                        owner,
                        methodName,
                        receiver,
                        line,
                        invocation.getArguments().size()));
            }
            return super.visitMethodInvocation(invocation, unused);
        }

        private String inferOwner(String receiver) {
            Matcher directType = NVS_TYPE.matcher(receiver);
            if (directType.find()) {
                return directType.group(1);
            }
            String root = receiver;
            int dot = root.indexOf('.');
            if (dot >= 0) {
                root = root.substring(0, dot);
            }
            int bracket = root.indexOf('[');
            if (bracket >= 0) {
                root = root.substring(0, bracket);
            }
            for (Map<String, String> scope : scopes) {
                String type = scope.get(root);
                if (type != null) {
                    return type;
                }
            }
            return "";
        }
    }

    private static final class Invocation {
        final String owner;
        final String method;
        final String receiver;
        final long line;
        final int arity;

        Invocation(String owner, String method, String receiver, long line, int arity) {
            this.owner = owner;
            this.method = method;
            this.receiver = receiver;
            this.line = line;
            this.arity = arity;
        }

        String toJson() {
            StringBuilder output = new StringBuilder();
            output.append('{');
            field(output, "owner", owner).append(',');
            field(output, "method", method).append(',');
            field(output, "receiver", receiver).append(',');
            numberField(output, "line", line).append(',');
            numberField(output, "arity", arity);
            output.append('}');
            return output.toString();
        }
    }

    private static StringBuilder field(StringBuilder output, String name, String value) {
        return output.append('"').append(escape(name)).append("\":\"")
                .append(escape(value)).append('"');
    }

    private static StringBuilder numberField(StringBuilder output, String name, long value) {
        return output.append('"').append(escape(name)).append("\":").append(value);
    }

    private static String escape(String value) {
        StringBuilder escaped = new StringBuilder();
        for (int index = 0; index < value.length(); index++) {
            char character = value.charAt(index);
            switch (character) {
                case '\\':
                    escaped.append("\\\\");
                    break;
                case '"':
                    escaped.append("\\\"");
                    break;
                case '\n':
                    escaped.append("\\n");
                    break;
                case '\r':
                    escaped.append("\\r");
                    break;
                case '\t':
                    escaped.append("\\t");
                    break;
                default:
                    if (character < 0x20) {
                        escaped.append(String.format("\\u%04x", (int) character));
                    } else {
                        escaped.append(character);
                    }
            }
        }
        return escaped.toString();
    }
}
