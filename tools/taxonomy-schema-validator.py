# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "jsonschema>=4.21"]
# ///
"""Validate taxonomy files.

    uv run tools/taxonomy-schema-validator.py --all
    uv run tools/taxonomy-schema-validator.py taxonomies/techniques/techniques-0.9.1.yaml [...]

A taxonomy file is named `<name>-<major>.<minor>.<patch>.yaml` and validated against
`schemas/<name>-<major>.schema.json` in its own directory. `--all` takes every YAML file directly under
`taxonomies/*/`; one that is not named that way fails.

Every file: no mapping repeats a key, the schema holds, and the file name's version starts with the file's
`version` field (component-wise: `0.9` matches `0.9.1`).
`techniques`: slugs unique across techniques and group nodes; every `parent` names another technique or a group
node; every group node child names a technique.
`models`: every `parent`, `variant_of`, `based_on`, `distilled_from` and `same_weights_as` names another node; every
`maker` is a key of `meta.makers`; `meta.maker_facets` has exactly the keys of `meta.makers`.

Prints one line per file and exits 1 if any file fails.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
FILE_NAME = re.compile(r"^(?P<name>[a-z][a-z0-9_]*(?:-[a-z][a-z0-9_]*)*)-(?P<version>[0-9]+\.[0-9]+\.[0-9]+)\.yaml$")
NODE_REFS = ("parent", "variant_of", "based_on", "distilled_from", "same_weights_as")


class UniqueKeyLoader(yaml.SafeLoader):
    """A SafeLoader that refuses a mapping with a repeated key (PyYAML keeps the last one silently)."""


def _mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    seen: set = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key {key!r}", key_node.start_mark)
        seen.add(key)
    return loader.construct_mapping(node, deep=deep)


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def dupes(items: list[str]) -> list[str]:
    return sorted(k for k, n in Counter(items).items() if n > 1)


def check_techniques(doc: dict) -> list[str]:
    errs = []
    techs, groups = doc["techniques"], doc["group_nodes"]
    slugs = [t["slug"] for t in techs] + [g["slug"] for g in groups]
    errs += [f"slug {s!r} defined more than once" for s in dupes(slugs)]
    tech_slugs, known = {t["slug"] for t in techs}, set(slugs)
    for t in techs:
        p = t.get("parent")
        if p is not None and (p not in known or p == t["slug"]):
            errs.append(f"{t['slug']}: parent {p!r} is not another technique or group node")
    for g in groups:
        errs += [f"group node {g['slug']}: child {c!r} is not a technique" for c in g["children"] if c not in tech_slugs]
    return errs


def check_models(doc: dict) -> list[str]:
    errs = []
    nodes, makers = doc["nodes"], doc["meta"]["makers"]
    if set(doc["meta"]["maker_facets"]) != set(makers):
        diff = sorted(set(doc["meta"]["maker_facets"]) ^ set(makers))
        errs.append(f"meta.maker_facets and meta.makers have different keys: {diff}")
    for key, node in nodes.items():
        for field in NODE_REFS:
            ref = node.get(field)
            if ref is not None and (ref not in nodes or ref == key):
                errs.append(f"{key}: {field} {ref!r} is not another node")
        m = node.get("maker")
        for maker in [] if m is None else (m if isinstance(m, list) else [m]):
            if maker not in makers:
                errs.append(f"{key}: maker {maker!r} is not in meta.makers")
    return errs


CHECKS = {"techniques": check_techniques, "models": check_models}


def version_matches(field: object, file_version: str) -> bool:
    """The file name's version starts with the `version` field, component by component."""
    if not isinstance(field, str) or not field:
        return False
    head = field.split(".")
    return file_version.split(".")[: len(head)] == head


def problems(path: Path) -> list[str]:
    m = FILE_NAME.match(path.name)
    if m is None:
        return ["file name is not <name>-<major>.<minor>.<patch>.yaml"]
    name, version = m["name"], m["version"]
    schema_path = path.parent / "schemas" / f"{name}-{version.split('.')[0]}.schema.json"
    if not schema_path.is_file():
        return [f"no schema {schema_path.name} in {path.parent.name}/schemas/"]
    try:
        doc = yaml.load(path.read_text("utf-8"), Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot read: {' '.join(str(exc).split())}"]
    validator = Draft202012Validator(json.loads(schema_path.read_text("utf-8")))
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))
    out = [f"schema: {'/'.join(map(str, e.absolute_path)) or '(top)'}: {e.message[:200]}" for e in errors]
    if isinstance(doc, dict) and not version_matches(doc.get("version"), version):
        out.append(f"version field {doc.get('version')!r} does not match the file name's {version}")
    if not errors and name in CHECKS:
        out += CHECKS[name](doc)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate taxonomy files against their schemas.")
    ap.add_argument("paths", nargs="*", type=Path, help="taxonomy files to check")
    ap.add_argument("--all", action="store_true", help="check every YAML file directly under taxonomies/*/")
    args = ap.parse_args(argv)
    if args.all == bool(args.paths):
        ap.error("give either file paths or --all")
    files = sorted(ROOT.glob("taxonomies/*/*.yaml")) + sorted(ROOT.glob("taxonomies/*/*.yml")) if args.all \
        else args.paths
    if not files:
        print("no taxonomy files found")
        return 1
    failed = 0
    for path in files:
        shown = path.resolve().relative_to(ROOT) if path.resolve().is_relative_to(ROOT) else path
        errs = problems(path)
        if errs:
            failed += 1
            print(f"FAIL {shown}: " + "; ".join(errs))
        else:
            print(f"ok   {shown}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
