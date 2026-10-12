"""Full PiExponent source-module import graph vs the actual Ω-Math core.

The OpenAI/math checkout is pinned in .github/workflows/test.yml.
This tests module-import graph structure, not elaborator-level theorem dependencies
and not proof validity. Import declarations are the source-of-truth oracle.
"""
from __future__ import annotations

from dataclasses import fields
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path
import json
import re
import subprocess

from omega_math.core import Configuration, Entity, Relation

UPSTREAM_REPO = Path("openai-math")
LEAN_ROOT = UPSTREAM_REPO / "lean"
CORPUS_ROOT = LEAN_ROOT / "OAI" / "NumberTheory" / "PiExponent"
EXPECTED_UPSTREAM_COMMIT = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)\s*$", re.MULTILINE)


def git_blob_sha(content: bytes) -> str:
    header = f"blob {len(content)}\0".encode()
    return sha1(header + content).hexdigest()


def module_name(path: Path) -> str:
    return ".".join(path.relative_to(LEAN_ROOT).with_suffix("").parts)


def has_cycle(nodes, edges) -> bool:
    adjacency = {node: [] for node in nodes}
    for src, dst in edges:
        adjacency.setdefault(src, []).append(dst)
    visiting, visited = set(), set()

    def visit(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for nxt in adjacency.get(node, ()):
            if visit(nxt):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in nodes if node not in visited)


def make_omega(nodes, source_modules, edges, *, domain=None, signs=None, keys=None, states=None):
    signs, keys, states = signs or {}, keys or {}, states or {}
    entities = tuple(Entity(node, states.get(node, 0)) for node in nodes)
    if domain is None:
        # Every source module may import any known graph node. Thus a removed
        # edge remains admissible and an extra edge to an existing node is not
        # rejected merely because it was not observed in the source.
        domain = frozenset(product(source_modules, nodes))
    relations = tuple(
        Relation(src, dst, signs.get((src, dst), 1),
                 key=keys.get((src, dst), f"{src}::{dst}"))
        for src, dst in edges
    )
    return Configuration(entities=entities, domain=domain, relations=relations)


def main():
    if not CORPUS_ROOT.is_dir():
        raise SystemExit(f"missing sparse checkout: {CORPUS_ROOT}")
    commit = subprocess.check_output(
        ["git", "-C", str(UPSTREAM_REPO), "rev-parse", "HEAD"], text=True
    ).strip()
    if commit != EXPECTED_UPSTREAM_COMMIT:
        raise SystemExit(f"wrong upstream commit: {commit}; expected {EXPECTED_UPSTREAM_COMMIT}")

    source_files = sorted(CORPUS_ROOT.rglob("*.lean"))
    if not source_files:
        raise SystemExit("no Lean source files found in the PiExponent corpus")

    modules = {}
    blob_shas = {}
    for path in source_files:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        mod = module_name(path)
        blob_shas[mod] = git_blob_sha(raw)
        modules[mod] = tuple(IMPORT_RE.findall(text))

    source_modules = tuple(sorted(modules))
    edge_list = [
        (source, target)
        for source in source_modules
        for target in modules[source]
    ]
    duplicate_import_declarations = len(edge_list) - len(set(edge_list))
    edges = tuple(sorted(set(edge_list)))
    expected = set(edges)
    nodes = tuple(sorted(set(source_modules) | {dst for _, dst in edges}))
    node_set = set(nodes)
    internal_edges = {(s, t) for s, t in edges if t in modules}
    external_targets = {t for _, t in edges if t not in modules}

    if any(src not in node_set or dst not in node_set for src, dst in edges):
        raise AssertionError("source oracle contains an edge with a missing endpoint")

    plain_edges = set(edges)
    omega = make_omega(nodes, source_modules, edges)
    omega_edges = {(r.src, r.dst) for r in omega.relations}
    if omega_edges != expected:
        raise AssertionError("Ω-Math core did not preserve the import-edge set")

    # Oracle-based fault injection. Both graph encodings preserve mutations;
    # only comparison with the pinned source oracle can call them wrong.
    first_edge = edges[0]
    missing = expected - {first_edge}
    extra_edge = next((s, t) for s in source_modules for t in nodes if (s, t) not in expected)
    extra = expected | {extra_edge}
    assert missing != expected and extra != expected
    assert plain_edges != missing and plain_edges != extra
    make_omega(nodes, source_modules, tuple(sorted(missing)))
    make_omega(nodes, source_modules, tuple(sorted(extra)))

    # Endpoint integrity is checked by Ω-Math Configuration when the candidate
    # pair is inside the declared relation domain.
    dangling = (source_modules[0], "Unknown.Dangling")
    dangling_domain = frozenset(set(product(source_modules, nodes)) | {dangling})
    try:
        make_omega(nodes, source_modules, edges + (dangling,), domain=dangling_domain)
    except ValueError as exc:
        assert "endpoint entity is absent" in str(exc)
    else:
        raise AssertionError("Ω-Math Configuration accepted a dangling endpoint")

    # Ω-Math has a sign domain, but no source-specific semantic oracle for the
    # sign: both allowed signs are accepted. The relation schema has no kind or
    # provenance fields.
    try:
        make_omega(nodes, source_modules, edges, signs={first_edge: 0})
    except TypeError:
        pass
    else:
        raise AssertionError("Ω-Math Relation accepted sign=0")
    wrong_legal_sign = make_omega(nodes, source_modules, edges, signs={first_edge: -1})
    assert next(r for r in wrong_legal_sign.relations if (r.src, r.dst) == first_edge).sign == -1
    wrong_state = make_omega(nodes, source_modules, edges, states={source_modules[0]: 1})
    assert next(e for e in wrong_state.entities if e.id == source_modules[0]).state == 1
    relation_fields = {f.name for f in fields(Relation)}
    assert relation_fields == {"src", "dst", "sign", "key"}
    assert not has_cycle(nodes, edges), "cycle in PiExponent source-level import graph"

    digest = sha256(
        "\n".join(f"{mod} {blob_shas[mod]}" for mod in source_modules).encode()
    ).hexdigest()
    print("FULL_PROJECT_IMPORT_GRAPH PASS")
    print(f"UPSTREAM_COMMIT {commit}")
    print(f"SOURCE_MODULES {len(source_modules)}")
    print(f"GRAPH_NODES {len(nodes)}")
    print(f"IMPORT_EDGES {len(edges)}")
    print(f"INTERNAL_PIEXPONENT_EDGES {len(internal_edges)}")
    print(f"EXTERNAL_IMPORT_TARGETS {len(external_targets)}")
    print(f"DUPLICATE_IMPORT_DECLARATIONS {duplicate_import_declarations}")
    print(f"SOURCE_BLOB_SHA256_DIGEST {digest}")
    print(f"EDGE_RECOVERY baseline={len(plain_edges & expected)}/{len(expected)} omega_core={len(omega_edges & expected)}/{len(expected)}")
    print("MISSING_EDGE oracle_detects=baseline,omega_core; native_structure_rejects=neither")
    print("EXTRA_EDGE oracle_detects=baseline,omega_core; native_structure_rejects=neither")
    print("DANGLING_ENDPOINT omega_Configuration=REJECT")
    print("INVALID_SIGN 0=REJECT; VALID_BUT_WRONG_SIGN -1=ACCEPT")
    print("WRONG_VALID_ENTITY_STATE=ACCEPT")
    print("RELATION_FIELDS src,dst,sign,key; kind/provenance=NOT_REPRESENTABLE")
    print("SOURCE_IMPORT_GRAPH_CYCLES 0")


if __name__ == "__main__":
    main()
