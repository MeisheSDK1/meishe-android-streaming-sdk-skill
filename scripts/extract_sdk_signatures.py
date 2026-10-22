#!/usr/bin/env python3
"""Extract public Meishe SDK signatures from NvAndroidStreamingSdk.jar.

This is a build-time maintenance tool. It reads a user/developer supplied SDK
jar and writes a compact signature inventory that can be bundled with the skill.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

PUBLIC_DECLARATION_RE = re.compile(r"^\s{2}public\b(.+);$")
DESCRIPTOR_RE = re.compile(r"^\s+descriptor:\s+(.+)$")
CLASS_DECLARATION_RE = re.compile(r"^(?:public\s+)?(?:class|interface|enum)\s+([^\s{]+)")
JAVA_HOME_RE = re.compile(r"\s+java\.home\s+=\s+(.+)")
JAVA_MODIFIERS = {
    "abstract",
    "default",
    "final",
    "native",
    "private",
    "protected",
    "public",
    "static",
    "strictfp",
    "synchronized",
    "transient",
    "volatile",
}
PRIMITIVE_TYPES = {
    "B": "byte",
    "C": "char",
    "D": "double",
    "F": "float",
    "I": "int",
    "J": "long",
    "S": "short",
    "Z": "boolean",
    "V": "void",
}

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-jar", type=Path, required=True)
    parser.add_argument("--jdk-home", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()

def locate_jdk_home(explicit_home=None):
    candidates = []
    if explicit_home:
        candidates.append(explicit_home)
    if os.environ.get("JAVA_HOME"):
        candidates.append(Path(os.environ["JAVA_HOME"]))
    java_bin = shutil.which("java")
    if java_bin:
        result = subprocess.run(
            [java_bin, "-XshowSettings:properties", "-version"],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        for line in (result.stderr + "\n" + result.stdout).splitlines():
            match = JAVA_HOME_RE.match(line)
            if match:
                candidates.append(Path(match.group(1).strip()))
                break
        candidates.append(Path(java_bin).resolve().parents[1])
    for candidate in candidates:
        javap = candidate / ("bin/javap.exe" if os.name == "nt" else "bin/javap")
        if javap.is_file():
            return candidate.resolve()
    return None

def javap_path(jdk_home):
    if jdk_home:
        path = jdk_home / ("bin/javap.exe" if os.name == "nt" else "bin/javap")
        if path.is_file():
            return path
    path = shutil.which("javap")
    if path:
        return Path(path)
    raise SystemExit("javap not found. Supply --jdk-home or set JAVA_HOME.")

def class_names_from_jar(sdk_jar):
    with zipfile.ZipFile(sdk_jar) as archive:
        names = []
        for item in archive.namelist():
            if not item.startswith("com/meicam/") or not item.endswith(".class"):
                continue
            if item.endswith("module-info.class"):
                continue
            names.append(item[:-6].replace("/", "."))
    return sorted(names)

def simple_owner(full_owner):
    return full_owner.rsplit(".", 1)[-1]

def member_name_from_declaration(declaration, full_owner):
    if "(" not in declaration:
        before_args = declaration.split("=", 1)[0].strip()
        name = before_args.rsplit(" ", 1)[-1]
        return name, "field"
    before_args = declaration.split("(", 1)[0].strip()
    token = before_args.rsplit(" ", 1)[-1]
    owner_tail = full_owner.rsplit(".", 1)[-1]
    if token == full_owner or token == owner_tail:
        return "<init>", "constructor"
    return token, "method"

def descriptor_parameters(descriptor):
    if not descriptor.startswith("("):
        return []
    body = descriptor[1: descriptor.index(")")]
    params = []
    index = 0
    while index < len(body):
        start = index
        while index < len(body) and body[index] == "[":
            index += 1
        if index < len(body) and body[index] == "L":
            index = body.index(";", index) + 1
        else:
            index += 1
        params.append(body[start:index])
    return params

def descriptor_java_type(descriptor):
    dimensions = 0
    while descriptor.startswith("["):
        dimensions += 1
        descriptor = descriptor[1:]
    if descriptor in PRIMITIVE_TYPES:
        java_type = PRIMITIVE_TYPES[descriptor]
    elif descriptor.startswith("L") and descriptor.endswith(";"):
        java_type = descriptor[1:-1].replace("/", ".").replace("$", ".")
    else:
        java_type = descriptor
    return java_type + "[]" * dimensions

def descriptor_return(descriptor, kind):
    if kind == "field":
        return {"descriptor": descriptor, "java_type": descriptor_java_type(descriptor)}
    if ")" not in descriptor:
        return {"descriptor": "", "java_type": ""}
    return_descriptor = descriptor.split(")", 1)[1]
    return {
        "descriptor": return_descriptor,
        "java_type": descriptor_java_type(return_descriptor),
    }

def declaration_modifiers(declaration):
    prefix = declaration.split("(", 1)[0].split("=", 1)[0]
    return [
        token
        for token in prefix.replace(";", "").split()
        if token in JAVA_MODIFIERS
    ]

def declaration_constant_value(declaration, kind):
    if kind != "field" or "=" not in declaration:
        return None
    return declaration.split("=", 1)[1].strip()

def parse_javap_output(class_name, output):
    full_owner = class_name
    class_match = CLASS_DECLARATION_RE.search(output)
    if class_match:
        full_owner = class_match.group(1)
    owner = simple_owner(full_owner)
    pending = None
    members = []
    for line in output.splitlines():
        declaration_match = PUBLIC_DECLARATION_RE.match(line)
        if declaration_match:
            declaration = "public" + declaration_match.group(1)
            member_name, kind = member_name_from_declaration(declaration, full_owner)
            pending = {
                "owner": owner,
                "full_owner": full_owner,
                "member_name": member_name,
                "member": f"{owner}.{member_name}" if kind != "constructor" else f"{owner}.<init>",
                "kind": kind,
                "declaration": declaration,
            }
            continue
        descriptor_match = DESCRIPTOR_RE.match(line)
        if descriptor_match and pending:
            descriptor = descriptor_match.group(1).strip()
            stable_id = (
                f"{pending['owner']}#{pending['member_name']}:{descriptor}"
                if pending["kind"] == "field"
                else f"{pending['owner']}#{pending['member_name']}{descriptor}"
            )
            parameter_descriptors = descriptor_parameters(descriptor)
            modifiers = declaration_modifiers(pending["declaration"])
            returns = descriptor_return(descriptor, pending["kind"])
            pending.update(
                {
                    "id": stable_id,
                    "stable_id": stable_id,
                    "descriptor": descriptor,
                    "arity": len(parameter_descriptors),
                    "parameters": [
                        {
                            "name": f"arg{index}",
                            "descriptor": value,
                            "java_type": descriptor_java_type(value),
                        }
                        for index, value in enumerate(parameter_descriptors)
                    ],
                    "parameter_types": [
                        descriptor_java_type(value)
                        for value in parameter_descriptors
                    ],
                    "parameter_names_inferred": False,
                    "returns": returns,
                    "return_type": returns["java_type"],
                    "modifiers": modifiers,
                    "is_static": "static" in modifiers,
                    "is_final": "final" in modifiers,
                    "constant_value": declaration_constant_value(
                        pending["declaration"],
                        pending["kind"],
                    ),
                    "declared_owner": full_owner,
                    "jar_signature": True,
                }
            )
            members.append(pending)
            pending = None
    return members

def extract_signatures(sdk_jar, jdk_home=None):
    sdk_jar = sdk_jar.resolve()
    if not sdk_jar.is_file():
        raise SystemExit(f"Missing SDK jar: {sdk_jar}")
    resolved_jdk_home = locate_jdk_home(jdk_home)
    javap = javap_path(resolved_jdk_home)
    classes = class_names_from_jar(sdk_jar)
    members = []
    errors = []
    for class_name in classes:
        result = subprocess.run(
            [
                str(javap),
                "-classpath",
                str(sdk_jar),
                "-public",
                "-s",
                "-constants",
                class_name,
            ],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        if result.returncode:
            errors.append({"class": class_name, "error": result.stderr.strip()[-1000:]})
            continue
        members.extend(parse_javap_output(class_name, result.stdout))
    class_rows = [
        {
            "class": simple_owner(class_name),
            "full_class": class_name,
            "package": class_name.rsplit(".", 1)[0],
            "member_count": sum(member["full_owner"] == class_name for member in members),
        }
        for class_name in classes
    ]
    overloads = {}
    for member in members:
        overloads.setdefault(
            (member["full_owner"], member["member_name"]),
            [],
        ).append(member["stable_id"])
    for member in members:
        member["overload_ids"] = sorted(
            overloads[(member["full_owner"], member["member_name"])]
        )
    return {
        "version": 2,
        "source": "NvAndroidStreamingSdk.jar",
        "jdk_home": "<build-time-jdk>" if resolved_jdk_home else "",
        "class_count": len(classes),
        "member_count": len(members),
        "classes": class_rows,
        "members": sorted(members, key=lambda item: item["stable_id"]),
        "errors": errors,
    }

def main():
    args = parse_args()
    result = extract_signatures(args.sdk_jar, args.jdk_home)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    if args.as_json or not args.output:
        sys.stdout.write(text)
    else:
        print(
            json.dumps(
                {
                    "class_count": result["class_count"],
                    "member_count": result["member_count"],
                    "error_count": len(result["errors"]),
                    "jdk_home": result["jdk_home"],
                },
                indent=2,
            )
        )

if __name__ == "__main__":
    main()
