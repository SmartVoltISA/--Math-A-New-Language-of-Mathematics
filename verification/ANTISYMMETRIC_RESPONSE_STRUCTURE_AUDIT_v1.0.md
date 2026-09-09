# Ω-Math — Antisymmetric Response Structure Audit v1.0

Date: 2026-09-09
Execution: local Python.

## Objective
Test whether the full normalized antisymmetric response structure is a stronger candidate than the scalar reciprocity defect `rho`.

For a declared nonnegative response matrix `R`, define the pairwise normalized directional component

`N_ij = (R_ij - R_ji) / (R_ij + R_ji)`

for pairs with positive denominator.

The scalar `rho` is retained as a magnitude summary. `N` retains pairwise directional information that `rho` necessarily discards.

## Algebraic checks

For a simultaneous node permutation represented by permutation matrix `P`:

`N(PRP^T) = P N(R) P^T`.

Thus `N` is not a scalar invariant; it is a covariant relational object whose content is preserved under relabelling.

For positive response scaling `c > 0`:

`N(cR) = N(R)`.

For direction reversal:

`N(R^T) = -N(R)`.

For positive `R_ij,R_ji`, each entry satisfies:

`-1 <= N_ij <= 1`.

If `R` is reciprocal, `N=0` for every defined pair. Conversely, `N=0` on every defined pair implies pairwise reciprocity.

## Local numerical audit

1000 independently generated positive response matrices were tested, with sizes 3–29.

Checks:

- relabelling covariance: PASS;
- positive scaling invariance: PASS;
- pairwise value preservation under relabelling: PASS;
- direction reversal sign flip: exact by construction;
- boundedness: PASS, maximum observed absolute entry 0.6631.

Maximum numerical deviation across permutation/scale checks: approximately `2.2e-16`.

## Structural finding

The full `N` object contains strictly more information than `rho`. Distinct response structures can share the same `rho` while having different `N` matrices. Therefore the earlier non-uniqueness counterexample against `rho` does not falsify `N`; it demonstrates that scalar compression is lossy.

However, `N` should not be called a scalar invariant. The correct mathematical classification is:

**normalized antisymmetric response structure — permutation-covariant, positive-scale invariant, orientation-odd.**

Its scalar norm or `rho` is the corresponding orientation-free invariant magnitude.

## Boundary

This remains a property of a declared response matrix. It does not establish that an arbitrary physical system has an intrinsic response matrix, nor does it derive physical time, energy, causality, geometry, or an arrow of time.

## Verdict

**SUPPORTED AS A STRONGER MATHEMATICAL OBJECT THAN `rho`.**

Do not promote as a universal physical ontology.

The correct candidate stack is:

`R -> N(R) -> rho(R)`

where `N` carries directional relational structure and `rho` is its scalar reciprocity-defect magnitude.
