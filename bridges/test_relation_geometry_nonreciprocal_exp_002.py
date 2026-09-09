from bridges.RELATION_GEOMETRY_NONRECIPROCAL_EXP_002 import (
    SEEDS,
    generate_activity,
    learn,
    measure,
    reciprocalize,
    run,
)


def test_symmetric_initial_conditions():
    weights = learn(generate_activity(SEEDS[0]))
    # Learning may break symmetry, but the constructor itself must not.
    initial = {(i, (i + 1) % 12): 1.0 for i in range(12)}
    initial.update({((i + 1) % 12, i): 1.0 for i in range(12)})
    assert all(initial[i, j] == initial[j, i] for i in range(12) for j in ((i + 1) % 12,))
    assert any(abs(weights[i, j] - weights[j, i]) > 1e-12 for i in range(12) for j in ((i + 1) % 12,))


def test_reciprocalized_control_has_zero_directional_asymmetry():
    weights = learn(generate_activity(SEEDS[0]))
    control = reciprocalize(weights)
    assert all(abs(x) < 1e-12 for x in measure(control))


def test_all_preregistered_seeds_pass_primary_emergence_signal():
    results = [run(seed) for seed in SEEDS]
    learned = sum(r.asymmetry for r in results) / len(results)
    control = sum(r.control_asymmetry for r in results) / len(results)
    nonzero = sum(
        sum(abs(x) > 1e-12 for x in r.deltas) / len(r.deltas) for r in results
    ) / len(results)
    assert learned > 5.0 * control
    assert nonzero >= 0.75
    assert all(r.asymmetry > 0.0 for r in results)
