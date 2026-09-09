"""Local verification of the normalized antisymmetric response component."""
from __future__ import annotations
import numpy as np

def normalized_antisymmetric(r: np.ndarray) -> np.ndarray:
    r = np.asarray(r, dtype=float)
    if r.ndim != 2 or r.shape[0] != r.shape[1] or r.shape[0] == 0:
        raise ValueError("R must be a non-empty square matrix")
    if np.any(r < 0):
        raise ValueError("R must be nonnegative")
    s = r + r.T
    out = np.zeros_like(r)
    mask = s > 0
    out[mask] = (r[mask] - r.T[mask]) / s[mask]
    return out

def run(seed=20260909, n=1000, size=8):
    rng = np.random.default_rng(seed)
    max_perm = max_scale = max_transpose = max_bound_excess = 0.0
    for _ in range(n):
        r = rng.uniform(0.01, 3.0, size=(size, size))
        nr = normalized_antisymmetric(r)
        p = rng.permutation(size)
        rp = r[np.ix_(p, p)]
        max_perm = max(max_perm, np.max(np.abs(normalized_antisymmetric(rp) - nr[np.ix_(p, p)])))
        max_scale = max(max_scale, np.max(np.abs(normalized_antisymmetric(17.3 * r) - nr)))
        max_transpose = max(max_transpose, np.max(np.abs(normalized_antisymmetric(r.T) + nr)))
        max_bound_excess = max(max_bound_excess, float(np.max(np.abs(nr)) - 1.0))
    r = rng.uniform(0.1, 2.0, size=(size, size))
    factors = rng.uniform(0.2, 5.0, size=(size, size))
    factors = np.triu(factors, 1); factors = factors + factors.T; factors += np.eye(size)
    r2 = r * factors
    same_n = np.max(np.abs(normalized_antisymmetric(r2) - normalized_antisymmetric(r)))
    matrix_distance = float(np.linalg.norm(r2 - r))
    return {"samples": n, "max_relabel_error": float(max_perm), "max_positive_scale_error": float(max_scale), "max_transpose_error": float(max_transpose), "max_bound_excess": float(max_bound_excess), "pairwise_rescaling_same_component_error": float(same_n), "pairwise_rescaling_matrix_distance": matrix_distance, "status": "PASS" if max(max_perm, max_scale, max_transpose, max_bound_excess) < 1e-12 and same_n < 1e-12 else "FAIL"}

if __name__ == "__main__":
    print(run())
