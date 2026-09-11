# EXPERIMENT Ω-028 — Incompressible-flow operator split

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Can a finite incompressible-flow discretization be written as the sum of a reversible skew operator and a positive-semidefinite dissipative operator, while reproducing the same state transition as the reference discretized flow law?

## Model
A periodic 2D incompressible velocity field on a 10×10 grid is initialized from an analytic streamfunction. Spatial derivatives are represented by the exact Fourier differentiation matrices for the periodic grid.

The reference velocity law is

`z_dot = -N(z) - K z`

where `N(z)` is the pointwise advective term and `K = -ν Δ` with `ν = 0.05`.

The Ω reversible operator is constructed from the skew part of the frozen advection operator:

`C = (C_raw - C_raw^T)/2`

and the Ω form is

`z_dot = -C z - K z`.

Because the discrete velocity is divergence-free and the derivative matrices are skew-adjoint, the skew split reproduces the reference advective operator to numerical precision.

## Execution
20 explicit Euler transitions were run from the same initial state with `dt = 0.001`. At every step the reference and Ω right-hand sides were recomputed independently from their respective current states.

## Verification criteria
1. Initial discrete divergence < `1e-10`.
2. Skew residual `||C + C^T||_∞ < 1e-10`.
3. Reference-vs-Ω RHS residual < `1e-10`.
4. 20-step state residual < `1e-10`.
5. Dissipative operator has no negative eigenvalue below numerical tolerance.
6. Kinetic-energy rate plus dissipative quadratic form < `1e-12`.

## Observed result
All six criteria PASS.

The construction therefore reproduces the chosen finite incompressible-flow discretization with

`reversible/skew part + dissipative/PSD part`.

The energy identity checked is

`dE/dt = - z^T K z <= 0`

because the skew contribution satisfies `z^T C z = 0`.

## Interpretation
This is a stronger mathematical bridge than a purely abstract matrix example: the operators are tied to a concrete incompressible-flow discretization, and the state transition is reproduced over multiple steps.

It does **not** establish that Ω independently predicts the Navier–Stokes equations, nor does it yet establish the requested axisymmetric radial/axial vortex with independently solved pressure and boundary flux. The periodic 2D model is intentionally marked as a bridge test.

## Boundary
NOT_PROVEN — full axisymmetric Navier–Stokes derivation.

NOT_PROVEN — independent physical prediction of pressure, radial flux, and transient vortex evolution.

NOT_PROVEN — novelty relative to existing skew-adjoint/Hamiltonian, finite-volume, spectral, and GENERIC/port-Hamiltonian formulations.

## Next falsification target
Construct the same comparison on the axisymmetric `(r,z)` control-volume grid with `u_r != 0`, pressure projection, viscosity, and boundary flux. Compare the reference finite-volume transition against an Ω construction whose graph geometry, reversible transport operator, dissipative operator, and pressure constraint are fixed independently before the run.
