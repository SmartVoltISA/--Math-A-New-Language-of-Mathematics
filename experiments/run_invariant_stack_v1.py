"""Local deterministic verification of an invariant stack for directed response geometry.

This is an operational graph experiment, not a physical-space proof.
"""
from __future__ import annotations

import numpy as np

SEED = 20260909


def response_ring(n: int, c_right: float = 0.32, c_left: float = 0.14) -> np.ndarray:
    d = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            r = (j - i) % n
            d[i, j] = min(r / c_right, (n - r) / c_left)
    return d


def relabel(d: np.ndarray, permutation: np.ndarray) -> np.ndarray:
    return d[np.ix_(permutation, permutation)]


def coarse(d: np.ndarray, block: int) -> np.ndarray:
    n = len(d)
    assert n % block == 0
    m = n // block
    out = np.zeros((m, m), dtype=float)
    for a in range(m):
        for b in range(m):
            if a != b:
                out[a, b] = d[a*block:(a+1)*block, b*block:(b+1)*block].mean()
    return out


def antisymmetry_signature(d: np.ndarray) -> tuple[float, float, float]:
    vals = []
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            denom = d[i, j] + d[j, i]
            if denom:
                vals.append((d[i, j] - d[j, i]) / denom)
    a = np.asarray(vals)
    return float(a.mean()), float(np.abs(a).mean()), float(np.sqrt(np.mean(a * a)))


def main() -> None:
    rng = np.random.default_rng(SEED)
    d = response_ring(64)
    base = antisymmetry_signature(d)

    # Node relabelling must preserve the unlabeled response signature.
    p = rng.permutation(len(d))
    relabeled = antisymmetry_signature(relabel(d, p))
    assert np.allclose(base, relabeled)

    # Positive global scaling changes units, not normalized directionality.
    for scale in (0.01, 0.1, 1.0, 10.0, 100.0):
        assert np.allclose(base, antisymmetry_signature(d * scale))

    # Contiguous coarse-graining preserves nonreciprocal signal at tested scales.
    coarse_signals = {k: antisymmetry_signature(coarse(d, k))[1] for k in (2, 4, 8)}
    assert all(v > 0 for v in coarse_signals.values())

    # Reversing every response direction must flip signed orientation while
    # preserving its magnitude statistics.
    reversed_sig = antisymmetry_signature(d.T)
    assert np.isclose(reversed_sig[0], -base[0])
    assert np.isclose(reversed_sig[1], base[1])
    assert np.isclose(reversed_sig[2], base[2])

    print(f"base_signed_mean={base[0]:.9f}")
    print(f"base_mean_abs={base[1]:.9f}")
    print(f"base_rms={base[2]:.9f}")
    print("relabel_invariance=PASS")
    print("positive_scale_invariance=PASS")
    for k, v in coarse_signals.items():
        print(f"coarse_block_{k}_mean_abs={v:.9f}")
    print("coarse_graining_signal=PASS")
    print(f"reversal_signed_mean={reversed_sig[0]:.9f}")
    print("direction_reversal=PASS")
    print("INVARIANT_STACK=PASS")


if __name__ == "__main__":
    main()
