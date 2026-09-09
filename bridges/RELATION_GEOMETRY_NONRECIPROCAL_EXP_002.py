"""Synthetic experiment: directional path cost emerging from symmetric initialization.

The graph starts reciprocal. Directionality is introduced only through a
lagged local history-dependent update driven by a moving activity pulse.
This is an operational graph experiment, not physical spacetime.
"""
from __future__ import annotations

import heapq
import random
from dataclasses import dataclass

N = 12
STEPS = 400
ETA = 0.015
DECAY = 0.001
EPSILON = 0.05
SEEDS = tuple(range(20260909, 20260925))
TARGET_OFFSET = 3


@dataclass(frozen=True)
class RunResult:
    asymmetry: float
    control_asymmetry: float
    deltas: tuple[float, ...]
    control_deltas: tuple[float, ...]


def generate_activity(seed: int) -> tuple[tuple[float, ...], ...]:
    rng = random.Random(seed)
    series: list[tuple[float, ...]] = []
    for t in range(STEPS + 1):
        pulse = (t + seed) % N
        row = [rng.uniform(0.0, 0.05) for _ in range(N)]
        row[pulse] = 1.0
        row[(pulse + 1) % N] = 0.7
        series.append(tuple(row))
    return tuple(series)


def shuffle_activity(activity: tuple[tuple[float, ...], ...], seed: int):
    rng = random.Random(seed)
    shuffled = list(activity)
    rng.shuffle(shuffled)
    return tuple(shuffled)


def learn(activity: tuple[tuple[float, ...], ...]) -> dict[tuple[int, int], float]:
    weights = {(i, (i + 1) % N): 1.0 for i in range(N)}
    weights.update({((i + 1) % N, i): 1.0 for i in range(N)})

    for t in range(STEPS):
        current = activity[t]
        nxt = activity[t + 1]
        updated: dict[tuple[int, int], float] = {}
        for i, j in weights:
            value = (1.0 - DECAY) * weights[i, j] + ETA * current[i] * nxt[j]
            updated[i, j] = max(EPSILON, value)
        weights = updated
    return weights


def shortest(weights: dict[tuple[int, int], float], src: int, dst: int) -> float:
    distance = [float("inf")] * N
    distance[src] = 0.0
    queue = [(0.0, src)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distance[node]:
            continue
        if node == dst:
            return cost
        for nxt in range(N):
            edge = (node, nxt)
            if edge not in weights:
                continue
            candidate = cost + weights[edge]
            if candidate < distance[nxt]:
                distance[nxt] = candidate
                heapq.heappush(queue, (candidate, nxt))
    return float("inf")


def measure(weights: dict[tuple[int, int], float]) -> tuple[float, ...]:
    return tuple(
        shortest(weights, i, (i + TARGET_OFFSET) % N)
        - shortest(weights, (i + TARGET_OFFSET) % N, i)
        for i in range(N)
    )


def run(seed: int) -> RunResult:
    ordered_activity = generate_activity(seed)
    shuffled_activity = shuffle_activity(ordered_activity, seed + 1)
    learned = learn(ordered_activity)
    null = learn(shuffled_activity)
    deltas = measure(learned)
    control_deltas = measure(null)
    asymmetry = sum(abs(x) for x in deltas) / len(deltas)
    control_asymmetry = sum(abs(x) for x in control_deltas) / len(control_deltas)
    return RunResult(asymmetry, control_asymmetry, deltas, control_deltas)


def main() -> None:
    results = [run(seed) for seed in SEEDS]

    # Symmetric initialization is part of the experiment, not an assumption.
    initial = {(i, (i + 1) % N): 1.0 for i in range(N)}
    initial.update({((i + 1) % N, i): 1.0 for i in range(N)})
    assert all(initial[i, j] == initial[j, i] for i in range(N) for j in ((i + 1) % N,))

    ordered_mean = sum(r.asymmetry for r in results) / len(results)
    shuffled_mean = sum(r.control_asymmetry for r in results) / len(results)
    ratio = ordered_mean / shuffled_mean
    nonzero_fraction = sum(
        sum(abs(x) > 1e-12 for x in r.deltas) / len(r.deltas) for r in results
    ) / len(results)
    seedwise_win_fraction = sum(
        r.asymmetry > r.control_asymmetry for r in results
    ) / len(results)

    assert ordered_mean > 5.0 * shuffled_mean
    assert nonzero_fraction >= 0.75
    assert seedwise_win_fraction == 1.0

    # Relabelling invariance: pure node renaming preserves the directional
    # response vector after corresponding pair remapping.
    seed = SEEDS[0]
    learned = learn(generate_activity(seed))
    permutation = (3, 9, 1, 10, 5, 0, 8, 2, 11, 6, 4, 7)
    relabelled = {(permutation[i], permutation[j]): value for (i, j), value in learned.items()}
    original_pairs = tuple((i, (i + TARGET_OFFSET) % N) for i in range(N))
    transformed_pairs = tuple((permutation[i], permutation[(i + TARGET_OFFSET) % N]) for i in range(N))
    original = tuple(shortest(learned, a, b) - shortest(learned, b, a) for a, b in original_pairs)
    transformed = tuple(shortest(relabelled, a, b) - shortest(relabelled, b, a) for a, b in transformed_pairs)
    assert original == transformed

    print("PASS symmetric initialization")
    print(f"ordered_mean_abs_asymmetry={ordered_mean:.6f}")
    print(f"shuffled_mean_abs_asymmetry={shuffled_mean:.6f}")
    print(f"ordered_to_shuffled_ratio={ratio:.6f}")
    print(f"nonzero_direction_fraction={nonzero_fraction:.6f}")
    print(f"seedwise_win_fraction={seedwise_win_fraction:.6f}")
    print("PASS relabelling invariance")
    print("PASS emergent nonreciprocity criteria")


if __name__ == "__main__":
    main()
