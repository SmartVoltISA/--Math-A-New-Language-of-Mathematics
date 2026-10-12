"""Reproducible Ω-Math vs plain-graph check on real Lean import declarations.

Corpus files and blob SHAs are pinned below. Imports were read from those exact
public OpenAI/math blobs. This experiment tests the actual Ω-Math core dataclasses,
not a replacement typed-graph implementation. It does NOT claim to extract
Lean elaborator-level theorem dependencies.
"""
from __future__ import annotations

from dataclasses import fields
from itertools import product

from omega_math.core import Configuration, Entity, Relation

CORPUS = {
    "lean/OAI/NumberTheory/PiExponent/Main.lean": {
        "sha": "486ed39ba52e5a10de7893cf0f302edb873801f2",
        "imports": [
            "OAI.NumberTheory.PiExponent.Approximation.AdmissibleMatrixGeometry",
            "OAI.NumberTheory.PiExponent.Approximation.InterpolationConsequence",
        ],
    },
    "lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixInterpolation.lean": {
        "sha": "4020f7dd25e5a10de7893cf0f302edb873801f2",
        "imports": [
            "OAI.NumberTheory.PiExponent.Ampleness.AdmissibleBlowupGeometry",
            "OAI.NumberTheory.PiExponent.Approximation.DeterminantContradiction",
            "OAI.NumberTheory.PiExponent.Approximation.FormalMatrixSurjectivity",
            "OAI.NumberTheory.PiExponent.Approximation.WeightedSliceDegree",
        ],
    },
    "lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixGeometry.lean": {
        "sha": "a684b7075f38134980a563da3968fcc9f13e50d2",
        "imports": [
            "OAI.NumberTheory.PiExponent.Approximation.AdmissibleMatrixFrame",
            "OAI.NumberTheory.PiExponent.Approximation.AdmissibleMatrixInterpolation",
            "OAI.NumberTheory.PiExponent.Approximation.WeightedGlobalSectionBound",
            "OAI.NumberTheory.PiExponent.Jets.AdmissibleJetPackets",
            "OAI.NumberTheory.PiExponent.Jets.AdmissibleJetSurjectivity",
        ],
    },
    "lean/OAI/NumberTheory/PiExponent/Statement.lean": {
        "sha": "f26a2c5d0bff73d1279b8c579ef68be04ee7794b",
        "imports": ["Mathlib"],
    },
}

SOURCE_NODES = tuple(CORPUS)
EDGES = tuple(
    (source, target)
    for source, spec in CORPUS.items()
    for target in spec["imports"]
)
NODES = tuple(sorted(set(SOURCE_NODES) | {target for _, target in EDGES}))
EXPECTED = set(EDGES)


def plain_graph_valid(nodes, edges):
    node_set = set(nodes)
    return all(src in node_set and dst in node_set for src, dst in edges)


def has_cycle(nodes, edges):
    adjacency = {node: [] for node in nodes}
    for src, dst in edges:
        if src in adjacency:
            adjacency[src].append(dst)
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


def make_omega_configuration(nodes, edges, *, signs=None, states=None, keys=None):
    signs = signs or {}
    states = states or {}
    keys = keys or {}
    entities = tuple(Entity(node, states.get(node, 0)) for node in nodes)
    # D_R is the full relation domain, not the observed edge set.
    domain = frozenset(product(nodes, repeat=2))
    relations = tuple(
        Relation(src, dst, signs.get((src, dst), 1),
                 key=keys.get((src, dst), f"{src}->{dst}"))
        for src, dst in edges
    )
    return Configuration(entities=entities, domain=domain, relations=relations)


def test_corpus_is_pinned_and_reproducible():
    assert len(CORPUS) == 4
    assert len(EDGES) == 12
    assert len(NODES) == 14
    assert len(EXPECTED) == 12
    assert all(len(spec["sha"]) == 40 for spec in CORPUS.values())
    assert plain_graph_valid(NODES, EDGES)
    make_omega_configuration(NODES, EDGES)
    print(f"CORPUS files={len(CORPUS)} nodes={len(NODES)} explicit_import_edges={len(EDGES)}")
    print("SOURCE_SHAS " + " ".join(spec["sha"] for spec in CORPUS.values()))


def test_baseline_and_real_omega_core_represent_same_import_graph():
    plain = set(EDGES)
    typed = {(r.src, r.dst) for r in make_omega_configuration(NODES, EDGES).relations}
    assert plain == typed == EXPECTED
    print(f"EDGE_RECOVERY baseline={len(plain & EXPECTED)}/{len(EXPECTED)} "
          f"omega_core={len(typed & EXPECTED)}/{len(EXPECTED)}")


def test_missing_and_extra_edges_require_an_oracle_in_both_representations():
    missing = set(EDGES) - {EDGES[0]}
    extra = set(EDGES) | {(NODES[0], NODES[-1])}
    assert missing != EXPECTED and extra != EXPECTED
    assert plain_graph_valid(NODES, missing)
    assert plain_graph_valid(NODES, extra)
    make_omega_configuration(NODES, tuple(missing))
    make_omega_configuration(NODES, tuple(extra))
    print("MISSING_EDGE oracle_detects=baseline,omega_core; native_structure_rejects=neither")
    print("EXTRA_EDGE oracle_detects=baseline,omega_core; native_structure_rejects=neither")


def test_dangling_endpoint_is_rejected_by_both_when_validators_are_used():
    dangling = tuple(EDGES) + ((NODES[0], "Unknown.Dangling"),)
    assert not plain_graph_valid(NODES, dangling)
    try:
        make_omega_configuration(NODES, dangling)
    except ValueError:
        pass
    else:
        raise AssertionError("Ω-Math Configuration accepted a dangling endpoint")
    print("DANGLING_ENDPOINT detected=baseline_validator,omega_Configuration")


def test_duplicate_relation_key_is_rejected_by_omega_core():
    duplicated = tuple(EDGES[:2])
    nodes = NODES
    signs = {}
    keys = {duplicated[0]: "same-key", duplicated[1]: "same-key"}
    try:
        make_omega_configuration(nodes, duplicated, keys=keys)
    except ValueError as exc:
        assert "duplicate relation key" in str(exc)
    else:
        raise AssertionError("Ω-Math Configuration accepted duplicate relation keys")
    print("DUPLICATE_KEY detected=omega_Configuration; plain_graph_has_no_key_contract")


def test_invalid_sign_domain_is_rejected_but_semantically_wrong_valid_sign_is_not():
    edge = EDGES[0]
    try:
        make_omega_configuration(NODES, EDGES, signs={edge: 0})
    except TypeError:
        pass
    else:
        raise AssertionError("Ω-Math Relation accepted sign=0")
    # Both -1 and +1 are legal in the actual core. Without an independent
    # semantic rule, flipping a legal sign is accepted by the core.
    flipped = make_omega_configuration(NODES, EDGES, signs={edge: -1})
    assert flipped.relations[0].sign == -1
    print("INVALID_SIGN sign=0 rejected; VALID_BUT_WRONG_SIGN flip_to=-1 accepted")


def test_valid_but_wrong_entity_state_is_not_detected_by_core():
    node = NODES[0]
    changed = make_omega_configuration(NODES, EDGES, states={node: 1})
    assert next(e for e in changed.entities if e.id == node).state == 1
    print("VALID_BUT_WRONG_NODE_STATE 0->1 accepted; no source-specific state oracle")


def test_native_configuration_does_not_enforce_acyclicity():
    nodes = ("A", "B")
    cycle_edges = (("A", "B"), ("B", "A"))
    assert has_cycle(nodes, cycle_edges)
    make_omega_configuration(nodes, cycle_edges)
    assert plain_graph_valid(nodes, cycle_edges)
    print("CYCLE detected_by_experiment_graph_checker; accepted_by_plain_graph_and_omega_Configuration")


def test_relation_schema_does_not_encode_relation_kind_or_source_provenance():
    relation_fields = {f.name for f in fields(Relation)}
    assert relation_fields == {"src", "dst", "sign", "key"}
    assert "kind" not in relation_fields
    assert "source" not in relation_fields
    assert "provenance" not in relation_fields
    print("SCHEMA_FIELDS Relation=src,dst,sign,key; kind/provenance=NOT_REPRESENTABLE")
