# EXPERIMENT Ω-030 — Axisymmetric transport falsification

## Status
EXECUTED / FALSIFICATION CHECK

## Question
Does taking the ordinary finite-volume transport operator and replacing it by its Euclidean skew part reproduce the physical discrete transport state transition?

## Setup
Axisymmetric `(r,z)` control-volume grid: `4×4`, `R=Z=2`, `dr=dz=0.5`.
The initial velocity has genuinely nonzero radial and axial components and is projected onto the discrete axisymmetric divergence-free subspace.

The cylindrical kinetic inner product uses control-volume weights proportional to `r dr dz`.

A finite-volume-like upwind transport operator `T(u)` is constructed directly from the velocity field. The candidate Ω reversible operator is its skew part

`C = (T - T^T)/2`.

The reference transport is `-T u`; the candidate Ω transport is `-C u`.

## Observed result
The projected initial field is divergence-free to numerical precision:

`max |H u| = 1.0269563e-15`.

However, the transport operator is not purely skew in this discretization. The measured values are

`||T u|| = 0.0301207130`

`||C u|| = 0.0198187048`

`||T u - C u|| = 0.0286938637`.

Therefore the naive identification

`physical transport = skew(T)`

FAILS for this finite-volume construction.

A second check using the cylindrical weighted inner product also shows a nonzero symmetric contribution. After mass weighting, the symmetric action has norm `0.0142701122` and quadratic contribution `z^T S z = 0.00115423305`.

## Interpretation
This is a useful negative result. Ω cannot simply declare the entire axisymmetric advection operator reversible by taking its skew part. The finite-volume transport contains a symmetric component that must either be explained as a genuine numerical/physical transport contribution, removed by a different conservative discretization, or represented by an additional operator.

This prevents a false PASS and identifies the next mathematical target: construct a genuinely energy-consistent cylindrical transport discretization whose reversible part is fixed by flux geometry and whose symmetric remainder has an independently justified meaning.

## Boundary
NOT_PROVEN — independent Ω prediction of axisymmetric Navier–Stokes.

NOT_PROVEN — that the symmetric transport remainder is physical dissipation; it may partly reflect the chosen upwind discretization.

NOT_PROVEN — pressure prediction and transient vortex evolution.

## Result
**FAIL — naive skew-only transport closure.**

The failure is informative: the next experiment must change the discretization/closure, not relax the criterion.
