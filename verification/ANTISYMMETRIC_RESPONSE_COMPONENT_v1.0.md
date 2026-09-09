# Normalized Antisymmetric Response Component v1.0

## Objective
Test the stronger object

`N(R) = (R - R^T) / (R + R^T)`

for declared nonnegative response matrices, distinguishing exact relational isomorphism from arbitrary coordinate changes.

## Verification

1000 random positive 8x8 response matrices were tested.

- simultaneous node relabelling: PASS
- positive global response scaling: PASS
- transpose/direction reversal: PASS, `N(R^T) = -N(R)`
- elementwise bound: PASS, `|N_ij| <= 1`
- numerical errors were at floating-point roundoff level (`< 1e-12`)

## Important boundary

`N` is covariant under relational isomorphism, not invariant under arbitrary linear coordinate mixing. A general basis transformation changes the meaning of individual node-to-node relations and therefore is not a legitimate relational relabelling.

The object is also not complete. If each unordered pair is independently multiplied by a positive factor applied to both directions, `N` remains unchanged while the response matrix changes substantially. Thus `N` captures directional imbalance, not the full response structure.

## Status

**SUPPORTED — structural directional component.**

Not promoted as a universal physical invariant. No claim is made about physical time, physical space, causality, or an arrow of time.

The scalar reciprocity defect `rho` should be treated as a derived magnitude summary of this component, not as its replacement.

## Reproducibility

Verification script: `experiments/run_antisymmetric_response_component_v1.py`.

Seed: `20260909`.
