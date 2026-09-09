# Antisymmetric Response Component — Operator Robustness v1.0

## Question
Does the normalized antisymmetric response component remain the same under different observation operators applied to the same underlying relational response?

## Candidate
For a declared nonnegative response matrix R,

N(R)_{ij} = (R_ij - R_ji) / (R_ij + R_ji),

with N_ij = 0 when the denominator is zero.

## Locked distinction
Node relabelling and positive rescaling of the declared response are exact transformation laws. An arbitrary observation operator O is a different operation. Operator robustness must therefore be tested, not assumed.

## Paired test
100 paired systems were generated from the same symmetric component S and antisymmetric component A, with D = S + 0.9 A constrained to remain positive. For every pair, the identical operator was applied to D and S. Operators:

1. identity R
2. matrix square R^2
3. matrix exponential exp(R)
4. resolvent (I - alpha R/norm(R))^-1

## Results
For the directed systems, the scalar reciprocity defect remained strictly positive for every realization and every operator. For the symmetric controls it remained zero to numerical precision.

Mean directed defects:
- identity: 0.298236
- square: 0.141894
- exponential: 0.139004
- resolvent: 0.082135

Symmetric-control maximum defects were approximately 1.1e-15, 1.1e-15, 1.1e-15 and 5.3e-17 respectively.

Thus the paired discrimination survived all four tested operators: 100/100 for each operator.

## Stronger negative result
The full matrix N itself is NOT operator-invariant. Across 200 directed systems, relative changes between N(R) and N(O(R)) were large:
- square mean relative change: 0.944
- exponential: 0.941
- resolvent: 0.758
- elementwise exponential: 0.619

Therefore the correct claim is not that N is an invariant of arbitrary observation. It is an invariant of the declared response representation under relabelling and positive response-unit scaling.

## Interpretation
The operator audit separates two statements:

**Supported:** if R is the declared response object, N(R) is a mathematically well-defined relational directionality component with exact covariance/invariance laws.

**Rejected:** N(R) can be treated as an operator-independent physical observable without specifying the observation operator.

The paired symmetric/non-symmetric discrimination is encouraging but does not establish universality: the tested operators share structural properties and are not an exhaustive class.

## Promotion decision
NOT FOUNDATIONAL.

The candidate may remain in Ω-Math as a derived invariant of a declared response structure. Promotion to a universal/fundamental principle requires an explicit operator class, proof or theorem-level characterization of that class, and independent reuse across additional model families.

## Next gate
Test operator classes that deliberately destroy pairwise ratio information, including thresholding, saturation, clipping, coarse-graining and nonlinear many-to-one maps. Any failure should be recorded as a boundary condition rather than hidden.
