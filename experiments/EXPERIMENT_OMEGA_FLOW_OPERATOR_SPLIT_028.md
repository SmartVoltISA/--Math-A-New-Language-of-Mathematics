# EXPERIMENT Ω-028 — Incompressible-flow operator split

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Can an energy-consistent finite incompressible-flow discretization be represented as reversible skew transport plus positive-semidefinite dissipation, with the same projected state transition?

## Model
Periodic 2D incompressible velocity field on a 10×10 grid. Spatial derivatives use Fourier differentiation matrices. The reference discretization uses the standard skew-symmetric advective form and a viscous operator `K = -νΔ`, with `ν = 0.05`.

The Ω form is

`z_dot = -C(z) z - K z`

where

`C(z) = (C_raw(z) - C_raw(z)^T)/2`.

A discrete pressure/incompressibility projection is applied after each explicit Euler step. The same initial state is used for both descriptions; 20 reference states are generated and, at every state, the Ω transition is independently evaluated and compared with the reference transition.

## Verification criteria
1. Initial projected divergence < `1e-10`.
2. `||C + C^T||_∞ < 1e-10`.
3. Reference-vs-Ω RHS residual < `1e-10` at all 20 states.
4. Projected next-state residual < `1e-10` at all 20 steps.
5. Minimum eigenvalue of `K` > `-1e-10`.
6. `|dE/dt + z^T K z| < 1e-12`.

## Observed result
All six criteria PASS in the executable run.

The energy identity is

`dE/dt = - z^T K z <= 0`

because the reversible contribution satisfies

`z^T C z = 0`.

## Interpretation
Ω-028 establishes a concrete finite-flow representation bridge: for this declared energy-consistent incompressible discretization, the transition law separates into a skew/reversible transport part and a PSD dissipative part while preserving the same projected transition.

This is stronger than an abstract arbitrary-matrix example, but it is **not an independent derivation** of Navier–Stokes. The reference discretization already uses a skew-symmetric energy-consistent advection form, so this experiment verifies compatibility/representation rather than novelty.

## Boundary
NOT_PROVEN — full axisymmetric Navier–Stokes derivation.

NOT_PROVEN — independent physical prediction of pressure, radial flux, and transient vortex evolution.

NOT_PROVEN — novelty relative to existing skew-adjoint/Hamiltonian, finite-volume, spectral, GENERIC, and port-Hamiltonian formulations.

## Next falsification target
Ω-029: move the same comparison to the axisymmetric `(r,z)` control-volume geometry with genuinely nonzero `u_r`, independently specified pressure/boundary conditions, viscous transport, and a reference finite-volume transition. The Ω graph geometry and operators must be fixed before the reference result is inspected.
