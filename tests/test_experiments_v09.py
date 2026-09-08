from itertools import product


def step_reach(edges, enabled, horizon):
    current = {0}
    seen = {0}
    for _ in range(horizon):
        nxt = {b for (a, b) in edges if (a, b) in enabled and a in current}
        seen |= nxt
        current = nxt
        if not current:
            break
    return seen


def test_experiment_010_locality_admissibility_boundary():
    edges = {(0, 1), (1, 2), (2, 3), (0, 3)}
    local = {(0, 1), (1, 2), (2, 3)}
    broad = edges
    assert step_reach(edges, local, 1) == {0, 1}
    assert step_reach(edges, broad, 1) == {0, 1, 3}
    restricted = edges - {(1, 2)}
    assert step_reach(edges, restricted, 3) == {0, 1, 3}


def test_experiment_011_exhaustive_mask_composition():
    edges = ((0, 1), (1, 2), (2, 3), (0, 3))
    for lm in range(16):
        loc = {edges[i] for i in range(4) if lm & (1 << i)}
        for am in range(16):
            adm = {edges[i] for i in range(4) if am & (1 << i)}
            eff = loc & adm
            for h in range(4):
                assert step_reach(set(edges), loc & adm, h) == step_reach(set(edges), eff, h)


def test_experiment_011_quotient_masks_transformation():
    T = {0: 1, 1: 0, 2: 2}
    Q = {0: 0, 1: 0, 2: 1}
    assert T != {0: 0, 1: 1, 2: 2}
    assert all(Q[T[x]] == Q[x] for x in T)


def test_experiment_012_directional_intervention_counterexample():
    def mx(state):
        x, _ = state
        return (x, x)

    def my(state):
        _, y = state
        return (y, y)

    baseline = (0, 0)
    assert mx(baseline) == my(baseline) == baseline
    set_x1 = (1, 0)
    assert mx(set_x1) != my(set_x1)


def test_experiment_012_exhaustive_baseline_case_count():
    states = list(product((0, 1), repeat=2))
    functions = list(product(states, repeat=4))
    assert len(states) == 4
    assert len(functions) == 256
    identical = 0
    interventionally_distinct = 0
    interventions = [(1, 0), (0, 1)]
    for f1 in functions:
        m1 = dict(zip(states, f1))
        for f2 in functions:
            m2 = dict(zip(states, f2))
            for s in states:
                trajectory1 = (s, m1[s], m1[m1[s]])
                trajectory2 = (s, m2[s], m2[m2[s]])
                if trajectory1 == trajectory2:
                    identical += 1
                    if any(m1[i] != m2[i] for i in interventions):
                        interventionally_distinct += 1
    assert identical == 28672
    assert interventionally_distinct == 25344
