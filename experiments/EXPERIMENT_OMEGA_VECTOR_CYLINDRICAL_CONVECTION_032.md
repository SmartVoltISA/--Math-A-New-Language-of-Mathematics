# EXPERIMENT Ω-032 — Vector cylindrical convection

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Can the cylindrical vector convective term be constructed directly from conservative face fluxes, including the azimuthal curvature terms, while preserving discrete kinetic-energy neutrality without post-hoc skew projection?

## Construction
A 6×6 axisymmetric `(r,z)` control-volume grid is used on `0 < r <= 2`, `0 <= z <= 2`, with `dr = dz = 2/6`.

A vertex streamfunction generates meridional face fluxes

`F_r = r u_r = ∂ψ/∂z`,

`F_z = r u_z = -∂ψ/∂r`,

with `ψ = sin²(πr/2) sin²(πz/2)`. Boundary fluxes vanish and the discrete cylindrical divergence is evaluated directly from the face balances.

An independent swirl field is supplied:

`u_θ = 0.4 r exp(-z)(1-r/2)`.

For each transported velocity component, the conservative central face-flux operator is built directly from the physical face fluxes. The cylindrical curvature terms are then included in the vector acceleration:

`a_r = -adv(u_r) + u_θ²/r`,

`a_z = -adv(u_z)`,

`a_θ = -adv(u_θ) - u_r u_θ/r`.

No skew projection is used to construct this operator.

## Results
Maximum discrete cylindrical divergence:

`3.9968028886505635e-15`

Total convective kinetic-energy power:

`9.823955884891156e-16`

Power of the conservative scalar transports:

`9.66052934804791e-16`

Power of the two curvature terms together:

`-9.390301368033089e-20`

The curvature contributions cancel pairwise in the kinetic-energy balance:

`u_r(u_θ²/r) + u_θ(-u_r u_θ/r) = 0`.

## Result
**PASS — DIRECT VECTOR CONSERVATIVE CONSTRUCTION.**

The complete cylindrical vector convection operator is energy-neutral to numerical precision for the declared divergence-free face-flux field.

The important distinction from Ω-030 is that the reversible operator is not obtained by taking the skew part of an already-computed physical operator. It is assembled directly from geometry, face fluxes, central interfacial transport, and the cylindrical vector curvature relations.

## Boundary
NOT_PROVEN — full Navier–Stokes solution.

NOT_PROVEN — pressure prediction.

NOT_PROVEN — viscous vector Laplacian including all cylindrical curvature terms.

NOT_PROVEN — transient vortex prediction from independently supplied physical initial/boundary data.

NOT_PROVEN — novelty relative to established conservative finite-volume and skew-adjoint formulations.

## Consequence
The Ω construction now has a stronger physical bridge: geometry and face transport can generate an energy-neutral vector transport operator directly. The next test combines this with a pressure-gradient operator and an independently constructed positive viscous operator, then checks the complete discrete kinetic-energy balance.
