# Ω-Math — Reciprocity Defect Invariant v1.0

Date: 2026-09-09
Execution: local Python.

## 1. Candidate

For a declared nonnegative response matrix `R`, define

`rho(R) = ||R - R^T||_F / ||R + R^T||_F`

when the denominator is nonzero.

Interpretation is deliberately narrow: `rho` measures the defect of reciprocity of the declared response structure. It does not assert physical time, energy, causality, geometry, or a fundamental arrow.

## 2. Exact algebraic invariances

For any permutation matrix `P` and any positive scalar `c`:

- `rho(P R P^T) = rho(R)` — node relabelling invariance.
- `rho(c R) = rho(R)` — positive response-unit scaling invariance.
- `rho(R^T) = rho(R)` — direction reversal preserves magnitude.
- `rho(R) = 0` iff `R = R^T` (provided the denominator is nonzero).

The full antisymmetric component `A=(R-R^T)/2` changes sign under transpose, while its norm is preserved. Thus the scalar `rho` is an orientation-free magnitude; it intentionally does not encode which direction is preferred.

## 3. Independent numerical gate

Paired synthetic shortest-path response systems were generated locally:

- 20-node strongly connected directed weighted graphs.
- 20 independent directed realizations.
- Positive edge costs in `[0.2, 2.0]`.
- Connectivity enforced only by inserting a directed cycle.
- Response: `R_ij = exp(-d_ij)` from directed all-pairs shortest-path distance.
- Matched reciprocal controls use symmetric edge costs and the same response construction.

### Directed systems

All 20/20 directed systems had nonzero `rho`.

Mean `rho = 0.3559199`.
Range `0.2996560 – 0.4334039`.

### Reciprocal controls

All 20/20 symmetric controls had exactly `rho = 0` to numerical precision.

### Exact transformation checks

For every directed realization:

- random simultaneous node permutation: PASS
- positive multiplication by `17.3`: PASS
- transpose/direction reversal: PASS
- transpose preserves `rho`: PASS

Maximum numerical deviation from the original value across these checks was approximately `1.1e-16`.

## 4. Important boundary

This result does **not** prove that `rho` is an intrinsic invariant of an underlying system independent of its observation operator. The previous dynamic-response audit demonstrated that an asymmetric observable can be produced by a chosen propagation/normalization procedure even under symmetric underlying relations.

Therefore the claim being tested here is narrower and cleaner:

> Given a declared response structure `R`, `rho(R)` is a mathematically well-defined reciprocity-defect invariant under relabelling and positive response scaling.

The stronger claim — that the same quantity universally recovers intrinsic nonreciprocity from arbitrary physical or dynamical observations — remains unproven.

## 5. Promotion status

**SUPPORTED AS A MATHEMATICAL INVARIANT OF DECLARED RESPONSE STRUCTURES.**

**NOT promoted as a universal physical invariant.**

The candidate is eligible for reuse as an Ω-Math derived invariant because its transformation properties are exact and it passes an independent graph class with matched reciprocal controls. Further cross-model reuse should test the same definition without changing its semantics.

## 6. Required follow-up

1. Implement `rho` as a pure Ω-Math derived invariant operation or documented derived metric.
2. Reuse unchanged in RELATION-LAB experiments from at least two independent model classes.
3. Keep observation-operator assumptions explicit.
4. Treat coarse-graining as a separate conditional transformation; do not assume invariance under coarse-graining.
5. Do not promote the result to physical geometry, physical time, causality, or a fundamental arrow without independent evidence.
