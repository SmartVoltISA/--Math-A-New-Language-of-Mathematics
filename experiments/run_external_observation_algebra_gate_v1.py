"""Ω-Math external-observation algebra discrimination hard gate v1.0.

The candidate algebra is NOT used to define the observation.
Two independent external dynamical/transport models are used:
1) continuous-time Markov diffusion -> semigroup composition (sum-product);
2) shortest travel time -> path minimization (min-plus);
3) bottleneck capacity -> max-min path composition.

This is deliberately a model-class test, not a claim about physical universality.
"""
import numpy as np
from scipy.linalg import expm

SEED = 20260909
TRIALS = 300
rng = np.random.default_rng(SEED)


def max_min(a, b):
    return np.max(np.minimum(a[:, :, None], b[None, :, :]), axis=1)


def min_plus(a, b):
    return np.min(a[:, :, None] + b[None, :, :], axis=1)


def sum_product(a, b):
    return a @ b


def relerr(a, b):
    return np.linalg.norm(a - b) / max(np.linalg.norm(b), 1e-15)


def diffusion_trial(n=6, dt=0.03):
    # External observable: transition operator of a continuous-time directed
    # random walk. No candidate algebra is used to generate T.
    w = rng.uniform(0.05, 1.0, (n, n))
    np.fill_diagonal(w, 0.0)
    L = w.T - np.diag(w.sum(axis=1))
    t1 = expm(dt * L)
    t2 = expm(2.0 * dt * L)
    preds = [max_min(t1, t1), min_plus(t1, t1), sum_product(t1, t1)]
    return [relerr(p, t2) for p in preds]


def minplus_trial(n=8):
    # External observable: measured two-edge travel time, obtained by taking
    # the earliest arrival through any intermediate node.
    c = rng.uniform(0.2, 2.0, (n, n))
    np.fill_diagonal(c, 10.0)
    obs = np.min(c[:, :, None] + c[None, :, :], axis=1)
    preds = [max_min(c, c), min_plus(c, c), sum_product(c, c)]
    return [relerr(p, obs) for p in preds]


def maxmin_trial(n=8):
    # External observable: bottleneck capacity of the best two-edge route.
    w = rng.uniform(0.1, 1.0, (n, n))
    np.fill_diagonal(w, 0.0)
    obs = np.max(np.minimum(w[:, :, None], w[None, :, :]), axis=1)
    preds = [max_min(w, w), min_plus(w, w), sum_product(w, w)]
    return [relerr(p, obs) for p in preds]


def summarize(name, rows):
    rows = np.asarray(rows)
    wins = np.bincount(np.argmin(rows, axis=1), minlength=3)
    print(name)
    print("mean_relative_error", rows.mean(axis=0))
    print("wins_maxmin_minplus_sumproduct", wins)
    print("correct_exact_fraction", np.mean(rows.min(axis=1) < 1e-12))


if __name__ == "__main__":
    diffusion = [diffusion_trial() for _ in range(TRIALS)]
    minplus = [minplus_trial() for _ in range(TRIALS)]
    maxmin = [maxmin_trial() for _ in range(TRIALS)]
    summarize("EXTERNAL-DIFFUSION", diffusion)
    summarize("EXTERNAL-TRAVEL-TIME", minplus)
    summarize("EXTERNAL-BOTTLENECK", maxmin)
