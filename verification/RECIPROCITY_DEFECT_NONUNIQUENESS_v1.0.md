# Ω-Math — Reciprocity Defect Non-Uniqueness Audit v1.0

Date: 2026-09-09
Execution: local Python.

## Objective
Test whether the scalar

`rho(R) = ||R-R^T||_F / ||R+R^T||_F`

uniquely identifies a directed relational structure.

## Protocol
Generate independent nonnegative directed matrices and search for structurally distinct pairs with nearly identical `rho`. Structural difference is measured directly from the full matrices after excluding trivial relabelling/scaling equivalences.

## Result
Near-equal values of `rho` occur for substantially different matrices. An example pair had:

- rho(A) = 0.34540557
- rho(B) = 0.34540556
- Frobenius matrix difference = 3.02267091

The two matrices are therefore not uniquely identified by the scalar defect.

## Interpretation
This is a **counterexample to completeness**, not to invariance.

The scalar `rho` is a coarse invariant: it measures the magnitude of the reciprocity defect, but it does not classify the complete directed relational structure. Different structures can share the same value.

That behavior is acceptable for a derived invariant unless completeness was part of the hypothesis. It means the stronger object should be treated as the equivalence class / normalized antisymmetric component when structural information is required, with `rho` as one scalar summary.

## Decision
- Invariance claim: unaffected.
- Completeness claim: rejected.
- Scalar uniqueness: rejected.
- Foundational use: allowed only as a **derived scalar invariant**, never as a complete representation of directionality.

## Boundary
No physical interpretation is inferred. The test concerns only declared mathematical response matrices.
