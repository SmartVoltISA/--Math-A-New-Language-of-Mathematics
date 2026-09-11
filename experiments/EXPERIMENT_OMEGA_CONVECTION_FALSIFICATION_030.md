# EXPERIMENT Ω-030 — Independent axisymmetric convection falsification

## Status
EXECUTED / FINITE NUMERICAL FALSIFICATION

## Question
Does an independently specified axisymmetric pointwise convective operator automatically equal the Ω skew/reversible operator obtained by metric-weighted skew projection?

## Setup
A 4×4 axisymmetric `(r,z)` grid is used on `0 < r <= 2`, `0 <= z <= 2`, with `dr = dz = 0.5`. A smooth streamfunction generates the initial velocity, giving a numerically divergence-free cylindrical field.

The independent convective operator is

`N(u) = (u_r ∂_r + u_z ∂_z) u`

with cylindrical divergence constraint

`(1/r) ∂_r(r u_r) + ∂_z u_z = 0`.

The cylindrical kinetic-energy inner product uses the geometric weight

`<a,b>_M = a^T M b`, with `M` proportional to `r dr dz`.

From the independently constructed linearized transport operator `T`, define the Ω candidate by weighted skew projection

`C = 1/2 (T - M^{-1} T^T M)`.

Thus `C^T M + M C = 0`.

## Verification
Maximum discrete cylindrical divergence residual:

`1.1102230246251565e-16`.

Weighted skew residual:

`||C^T M + M C||_∞ = 0`.

Independent nonlinear convection kinetic-energy power:

`u^T M (-N(u)) ≈ -1.37e-16`.

Ω skew-part power:

`u^T M (-C u) ≈ 0`.

But the operators do not coincide:

`||N(u) - C u||_2 = 0.7736596636659783`.

`||N(u)||_2 = 0.7355546635395476`.

The mismatch is therefore order-one relative to the norm of the physical convective operator.

## Result
**FAIL — automatic identification of physical convection with Ω skew projection.**

The test rejects the stronger claim that metric-weighted skew projection alone determines the physical convective transition.

Energy conservation itself is not rejected: both the independent convection and Ω skew part have zero kinetic-energy power for this divergence-free test.

## Interpretation
This is a useful falsification result. The Ω decomposition identifies an energy-neutral/reversible subspace, but the physical transport law contains additional information that is lost when only the skew part of its linearized operator is retained.

Therefore a predictive Ω flow law requires an additional transport/closure rule connecting physical geometry, face fluxes, and the reversible operator. We must not define `C` from an already-known answer and then call the result a physical prediction.

The symmetric remainder is not automatically physical dissipation: its operator norm is nonzero, while its quadratic power on the tested state is approximately zero. Operator decomposition and physical energy dissipation must remain separate claims.

## Boundary
NOT_PROVEN — Ω derivation of the full axisymmetric Navier–Stokes convective term.

NOT_PROVEN — that the symmetric remainder represents viscosity or another physical mechanism.

NOT_PROVEN — independent prediction of pressure, radial flux, or transient vortex evolution.

NOT_PROVEN — novelty relative to established skew-adjoint, conservative finite-volume, spectral, Hamiltonian, GENERIC, or port-Hamiltonian formulations.

## Consequence for Ω-031
The next construction must specify the transport law from geometry and face fluxes **before** comparing with the reference solution. The target is a conservative cylindrical finite-volume operator whose energy balance is tested independently, rather than obtained by post-hoc skew projection.
