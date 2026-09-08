"""Deterministic synthetic test for the RELATION non-reciprocal geometry protocol.

This is a graph-level response-cost experiment, not physical spacetime.
"""
from __future__ import annotations

import heapq
import random
from dataclasses import dataclass


N = 8
PAIRS = [(i, (i + 3) % N) for i in range(N)]
SEED = 20260909
NOISE = 0.10


@dataclass(frozen=True)
class Result:
    forward: tuple[float, ...]
    backward: tuple[float, ...]
    delta: tuple[float, ...]

    @property
    def mean_abs_delta(self) -> float:
        return sum(abs(x) for x in self.delta) / len(self.delta)


def build_graph(asymmetric: bool, seed: int = SEED, noise: float = NOISE):
    rng = random.Random(seed)
    edges: dict[tuple[int, int], float] = {}
    for i in range(N):
        j = (i + 1) % N
        forward = 1.0 if asymmetric else 2.0
        backward = 3.0 if asymmetric else 2.0
        edges[i, j] = forward + rng.uniform(-noise, noise)
        edges[j, i] = backward + rng.uniform(-noise, noise)
    return edges


def shortest(edges: dict[tuple[int, int], float], src: int, dst: int) -> float:
    distances = [float("inf")] * N
    distances[src] = 0.0
    queue = [(0.0, src)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distances[node]:
            continue
        if node == dst:
            return cost
        for nxt in range(N):
            edge = (node, nxt)
            if edge not in edges:
                continue
            candidate = cost + edges[edge]
            if candidate < distances[nxt]:
                distances[nxt] = candidate
                heapq.heappush(queue, (candidate, nxt))
    return float("inf")


def measure(edges: dict[tuple[int, int], float]) -> Result:
    forward = tuple(shortest(edges, a, b) for a, b in PAIRS)
    backward = tuple(shortest(edges, b, a) for a, b in PAIRS)
    delta = tuple(a - b for a, b in zip(forward, backward))
    return Result(forward, backward, delta)


def relabel(edges: dict[tuple[int, int], float], permutation: tuple[int, ...]):
    return {(permutation[a], permutation[b]): cost for (a, b), cost in edges.items()}


def remap_pairs(permutation: tuple[int, ...]):
    return tuple((permutation[a], permutation[b]) for a, b in PAIRS)


def measure_pairs(edges, pairs):
    return tuple(shortest(edges, a, b) - shortest(edges, b, a) for a, b in pairs)


def main() -> None:
    asymmetric = build_graph(True)
    reciprocal = build_graph(False)
    asym_result = measure(asymmetric)
    reciprocal_result = measure(reciprocal)

    assert asym_result.mean_abs_delta > 1.0
    assert reciprocal_result.mean_abs_delta < 0.25
    assert all(d < -1.5 for d in asym_result.delta)
    assert all(abs(d) < 0.25 for d in reciprocal_result.delta)

    reversed_delta = tuple(-d for d in asym_result.delta)
    assert reversed_delta == tuple(
        shortest(asymmetric, b, a) - shortest(asymmetric, a, b) for a, b in PAIRS
    )

    permutation = (3, 6, 1, 7, 0, 4, 2, 5)
    relabelled = relabel(asymmetric, permutation)
    original_delta = measure_pairs(asymmetric, PAIRS)
    transformed_delta = measure_pairs(relabelled, remap_pairs(permutation))
    assert original_delta == transformed_delta

    # Explicit reverse-edge control: both directions exist and remain distinct.
    for i in range(N):
        j = (i + 1) % N
        assert (i, j) in asymmetric
        assert (j, i) in asymmetric
        assert asymmetric[i, j] != asymmetric[j, i]

    print("PASS nonreciprocal asymmetry")
    print(f"mean_abs_delta={asym_result.mean_abs_delta:.6f}")
    print(f"reciprocal_mean_abs_delta={reciprocal_result.mean_abs_delta:.6f}")
    print("PASS direction reversal")
    print("PASS relabelling invariance")
    print("PASS explicit reverse-edge distinction")


if __name__ == "__main__":
    main()
