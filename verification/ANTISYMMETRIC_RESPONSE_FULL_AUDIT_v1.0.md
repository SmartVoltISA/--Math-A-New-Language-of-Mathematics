# Antisymmetric Response — Full Break-or-Promote Audit v1.0

## Objective

Test the candidate directed component

`N_ij(R) = (R_ij - R_ji) / (R_ij + R_ji)`

and its scalar summary `rho(R) = ||R-R^T||_F / ||R+R^T||_F` against representation changes, nonlinear observation maps, coarse-graining, and noise.

The purpose is explicitly falsification/promotion, not confirmation.

## Tests

### 1. Exact algebraic transformations

For positive response matrices, the following were tested on 1000 random 8x8 matrices:

- simultaneous node relabelling: `N(PRP^T) = P N(R) P^T`
- positive global response scaling: `N(cR) = N(R)`, `c > 0`
- direction reversal: `N(R^T) = -N(R)`
- pairwise bound: `|N_ij| <= 1`

All passed to numerical precision.

### 2. Observation/operator stress test

Paired symmetric and directed matrices were passed through eight deterministic elementwise operators: identity, clipping, thresholding, saturation (`tanh`), square root, `log1p`, square, and exponential normalization.

100 paired realizations per operator were tested. Directed responses exceeded symmetric controls in 100/100 cases for every operator. Symmetric controls remained exactly reciprocal for these entrywise maps.

This supports operator-robust discrimination only for this restricted class of entrywise operators.

### 3. Coarse-graining

300 random directed matrices were block-averaged with block sizes 2, 3, or 4. The scalar defect was not preserved: retention ratio ranged approximately 0.049–0.695, median approximately 0.312.

**Result: FAIL as a universal coarse-graining invariant.**

This is a hard boundary, not a software error. Coarse-graining may erase or dilute directionality.

### 4. Noise

500 paired symmetric/directed cases were tested at additive Gaussian noise levels 1%, 3%, 10%, 20%, 30%, 50%, and 100% of mean response scale, with clipping at zero.

Mean symmetric-control rho increased with noise:

| noise | mean symmetric rho | 95% symmetric rho | mean directed rho | directed > symmetric |
|---:|---:|---:|---:|---:|
| 0.01 | 0.00634 | 0.00742 | 0.33202 | 100.0% |
| 0.03 | 0.01902 | 0.02255 | 0.33338 | 100.0% |
| 0.10 | 0.06292 | 0.07511 | 0.33637 | 100.0% |
| 0.20 | 0.12444 | 0.14444 | 0.34649 | 100.0% |
| 0.30 | 0.18344 | 0.21783 | 0.36682 | 100.0% |
| 0.50 | 0.28567 | 0.33654 | 0.40723 | 98.6% |
| 1.00 | 0.44303 | 0.52835 | 0.48874 | 70.6% |

**Result:** robust statistical separation at moderate noise in this synthetic setup; not exact invariance under noisy observation. At very high noise the statistic loses discriminating power.

## Interpretation

The candidate survives as an exact mathematical transformation object of a declared response matrix. It does **not** survive as a universal observable independent of measurement/operator choice, and it does **not** survive arbitrary coarse-graining.

The strongest defensible statement is therefore:

> Ω-Math can define a label-covariant, positive-scale-invariant antisymmetric component of a declared response structure. Its scalar norm is a derived reciprocity-defect measure. Preservation under coarse-graining, arbitrary observation operators, noise, or physical interpretation is not part of the invariant claim.

## Promotion decision

**PROMOTE to Ω-Math as a derived mathematical invariant/object.**

**DO NOT promote to FUNDAMENT as a universal physical invariant.**

The promotion is conditional on the declared response structure and its domain. The failed coarse-graining universality and operator limitations remain explicit constraints.

## What is still open

1. Whether a representation-independent object can be defined directly at the relational/path level, before choosing a response operator.
2. Whether a canonical Ω-Math construction can produce the response structure without importing physical geometry, time, energy, or causality.
3. Whether the antisymmetric component has an independent predictive role across genuinely different model families.
4. Whether any stronger universal object survives coarse-graining without retaining pair/source-target identity information.

## Status

`SUPPORTED — derived relational invariant`

`NOT FOUNDATIONAL — physical universality not established`
