from bridges.RELATION_GEOMETRY_NONRECIPROCAL_EXP_001 import (
    PAIRS,
    build_graph,
    measure,
    measure_pairs,
    relabel,
    remap_pairs,
    shortest,
)


def test_nonreciprocal_signal_beats_reciprocal_control():
    asym = measure(build_graph(True))
    reciprocal = measure(build_graph(False))

    assert asym.mean_abs_delta > 1.0
    assert reciprocal.mean_abs_delta < 0.25
    assert asym.mean_abs_delta > 10 * reciprocal.mean_abs_delta


def test_direction_reversal_changes_only_orientation():
    edges = build_graph(True)
    delta = measure(edges).delta
    reversed_delta = tuple(
        shortest(edges, b, a) - shortest(edges, a, b) for a, b in PAIRS
    )
    assert reversed_delta == tuple(-x for x in delta)


def test_relabelling_preserves_directional_observable():
    edges = build_graph(True)
    permutation = (3, 6, 1, 7, 0, 4, 2, 5)
    transformed = relabel(edges, permutation)
    original = measure_pairs(edges, PAIRS)
    remapped = measure_pairs(transformed, remap_pairs(permutation))
    assert original == remapped


def test_reverse_edges_are_explicit_and_distinct():
    edges = build_graph(True)
    for i in range(8):
        j = (i + 1) % 8
        assert (i, j) in edges
        assert (j, i) in edges
        assert edges[i, j] != edges[j, i]
