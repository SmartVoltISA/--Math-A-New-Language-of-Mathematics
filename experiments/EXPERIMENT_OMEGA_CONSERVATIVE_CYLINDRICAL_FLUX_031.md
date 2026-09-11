# EXPERIMENT Ω-031 — Conservative cylindrical face-flux transport

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Can the reversible transport operator be obtained directly from cylindrical geometry and conservative face fluxes, without defining it by post-hoc skew projection of a known physical operator?

## Setup
A 4×4 axisymmetric `(r,z)` finite-volume grid is used on `0 < r < 2`, `0 < z < 2`, with `dr = dz = 0.5`.

The cylindrical kinetic-energy inner product is

`<a,b>_M = a^T M b`,

with cell weight

`M_i = r_i dr dz`.

A vertex streamfunction is fixed before constructing the transport operator:

`psi(r,z) = sin(pi r / 2) sin(pi z / 2)`.

It vanishes on all boundaries. The face fluxes are generated directly from geometry and the streamfunction:

`F_r = r u_r = d psi / dz`,

`F_z = r u_z = -d psi / dr`.

This makes the discrete cylindrical continuity equation hold by construction through telescoping face fluxes, while boundary flux is zero.

For a transported scalar `q`, the conservative central face law is

`dq_i/dt = -(1/M_i) sum_faces F_face (q_i + q_j)/2`.

No skew projection is applied to this operator.

## Verification
The independently constructed face flux satisfies the discrete cylindrical divergence constraint with maximum residual

`2.9605947323337506e-16`.

The resulting transport operator `T` satisfies the cylindrical metric energy condition

`T^T M + M T = 0`

with infinity-norm residual

`2.220446049250313e-16`.

For the test state

`q(r,z) = sin(r) cos(z)`,

the discrete kinetic-energy power is

`q^T M T q = 1.1102230246251565e-16`.

Thus the conservative face-flux construction is energy-neutral to numerical precision.

## Result
**PASS — direct geometry/face-flux construction of a reversible transport operator.**

The important point is methodological: the skew/reversible property was not imposed after constructing an arbitrary transport matrix. It follows from shared conservative face fluxes, the cylindrical mass measure, zero boundary flux, and central face exchange.

## Interpretation
Ω-031 supplies the missing bridge identified by Ω-030 for the scalar transport case:

`geometry → face flux → conservative exchange → metric-skew transport`.

This is substantially stronger than post-hoc replacement `T -> (T-T^T)/2` because the operator is generated before the energy test.

However, this experiment is **not yet a full Navier–Stokes derivation**. The tested transported quantity is a scalar `q`; the vector velocity equations contain additional cylindrical geometric terms, pressure coupling, angular momentum structure, and nonlinear velocity transport. Those terms must be derived independently rather than inserted afterward.

## Boundary
NOT_PROVEN — full axisymmetric Navier–Stokes derivation.

NOT_PROVEN — independent prediction of pressure, radial flux, or transient vortex evolution.

NOT_PROVEN — that the same construction uniquely determines the physical vector convection operator.

NOT_PROVEN — novelty relative to established conservative finite-volume and skew-adjoint formulations.

## Next falsification target
Ω-032: extend the direct face-flux construction from scalar transport to the full axisymmetric velocity state `(u_r,u_z,u_theta)`, including cylindrical geometric coupling. The operator must be generated from face fluxes and fixed geometry first; only then will its energy balance be compared with an independently specified reference discretization.
