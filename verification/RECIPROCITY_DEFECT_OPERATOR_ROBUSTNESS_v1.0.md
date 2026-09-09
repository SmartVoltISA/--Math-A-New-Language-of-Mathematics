# Ω-Math — Reciprocity Defect Operator-Robustness Test v1.0

Date: 2026-09-09
Execution: local Python.

## Objective
Test whether the reciprocity defect

`rho(R) = ||R - R^T||_F / ||R + R^T||_F`

remains a structural discriminator when the same relational system is passed through several deterministic response operators.

This is a mathematical robustness test only. It does not establish physical time, energy, causality, or physical geometry.

## Paired model design
For each size N in {8, 12, 20, 32}, 20 independent directed weighted matrices were generated from the same random-generation family. A paired symmetric control was constructed by symmetrizing the corresponding matrix:

`S = (A + A^T)/2`.

Matrices were normalized by Frobenius norm before applying the nontrivial operators so that operator parameters were not confounded with arbitrary input scale.

Total: 80 directed realizations and 80 paired symmetric controls.

## Operators
Four deterministic operators were tested:

1. Direct response: `R = A`
2. Two-step response: `R = A^2`
3. Exponential response: `R = exp(A)`
4. Resolvent response: `R = (I - 0.2 A)^(-1)`

The same operator definition was applied to the directed and symmetric member of each pair.

## Results
For every operator, all 80 directed realizations had a positive reciprocity defect (apart from the mathematically possible degenerate denominator case, which did not occur here).

Directed rho ranges / means:

- Direct: 0.491532–1.000000; mean 0.841527
- Square: 0.160389–1.000000; mean 0.678417
- Exponential: 0.108686–0.250275; mean 0.162125
- Resolvent: 0.022086–0.050565; mean 0.033247

All 80 symmetric controls had rho numerically zero for all operators. Maximum observed symmetric-control rho was below `1e-16` for every operator.

## Exact invariance checks
For the reciprocity defect itself:

- Simultaneous node relabelling `R -> P R P^T`: invariant by Frobenius norm and confirmed numerically.
- Positive response scaling `R -> cR`, c > 0: invariant algebraically.
- Direction reversal `R -> R^T`: rho unchanged algebraically.
- Reciprocity `R = R^T`: rho = 0 whenever denominator is nonzero.

## Interpretation
This test closes an important weakness found in the previous dynamic-response audit. The earlier raw response statistic could become nonzero under a symmetric relational control because the observation operator itself introduced asymmetry. Here the candidate is defined directly on the response object and is tested with identical deterministic operators applied to paired symmetric/nonreciprocal structures.

Across the four tested operator families, symmetric inputs remain exactly reciprocal while directed inputs retain a positive reciprocity defect. The signal therefore survives operator transfer within this tested class.

This supports the following narrow mathematical statement:

> The reciprocity defect is a label-independent, positive-scale-invariant scalar of a declared directed response matrix, and it robustly separates symmetric from generic directed response structures under the tested matrix operators.

It does **not** show that every physical observation operator preserves structural nonreciprocity, nor that every directed system must have nonzero rho, nor that rho is a complete classifier of directed structures.

## Verdict
**SUPPORTED — candidate mathematical invariant.**

**NOT YET FOUNDATIONAL.**

The remaining promotion gates are project-independent reuse in RELATION-LAB, an explicit counterexample search for directed structures with `rho = 0`, robustness to noise/measurement perturbation, and confirmation that the definition can be represented in Ω-Math without importing physical semantics.
