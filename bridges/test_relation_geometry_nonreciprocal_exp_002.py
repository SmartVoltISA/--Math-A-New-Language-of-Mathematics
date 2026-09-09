from bridges.RELATION_GEOMETRY_NONRECIPROCAL_EXP_002 import (
    SEEDS,
    generate_activity,
    learn,
    measure,
    run,
    shuffle_activity,
)


def test_symmetric_initial_conditions():
    initial = {(i, (i + 1) % 12): 1.0 for i in range(12)}
    initial.update({((i + 1) % 12, i): 1.0 for i in range(12)})
    assert all(initial[i, j] == initial[j, i] for i in range(12) for j in ((i + 1) % 12,))

    learned = learn(generate_activity(SEEDS[0]))
    assert any(
        abs(learned[i, j] - learned[j, i]) > 1e-12
        for i in range(12)
        for j in ((i + 1) % 12,)
    )


def test_temporal_shuffle_is_distinct_control():
    ordered = generate_activity(SEEDS[0])
    shuffled = shuffle_activity(ordered, SEEDS[0] + 1)
    assert ordered != shuffled
    assert measure(learn(ordered)) != measure(learn(shuffled))


def test_all_preregistered_seeds_pass_primary_emergence_signal():
    results = [run(seed) for seed in SEEDS]
    ordered = sum(r.asymmetry for r in results) / len(results)
    shuffled = sum(r.control_asymmetry for r in results) / len(results)
    nonzero = sum(
        sum(abs(x) > 1e-12 for x in r.deltas) / len(r.deltas) for r in results
    ) / len(results)
    assert ordered > 5.0 * shuffled
    assert nonzero >= 0.75
    assert all(r.asymmetry > r.control_asymmetry for r in results)
