# Ω-025 — Transient Vortex / Incompressibility Falsification

**Status:** EXECUTED / COARSE NUMERICAL FALSIFICATION

## 1. Objective

Strengthen Ω-024 by actually evaluating a radial-axial transient state on a larger 3×3 `(r,z)` mesh and attempting a pressure correction rather than simply prescribing a pressure field.

This is deliberately a falsification test. Failure of the coarse pressure projection is recorded as failure of this numerical closure, not hidden.

## 2. Mesh and initial state

Cell centers:

`r = {0.6, 1.0, 1.4}`

`z = {0.2, 0.6, 1.0}`

with `Δr = Δz = 0.4` and density `ρ=1`.

Initial velocity:

`u_r = 0.12(r-1)e^{-z}`

`u_θ = r^{-1}e^{-z}`

`u_z = 0.30(1-r/1.5)e^{-z}`.

Thus the test contains swirl, axial motion, and genuinely nonzero radial motion.

## 3. Initial incompressibility residual

Axisymmetric divergence was evaluated as

`∇·u = (1/r)∂(r u_r)/∂r + ∂u_z/∂z`.

On the coarse mesh, the maximum discrete residual was

`max|∇·u| = 0.08475173452016001`.

Therefore the prescribed initial field is **not exactly discretely incompressible** on this coarse grid.

This is important: the continuous-looking analytic ansatz does not automatically satisfy the discrete constraint used by the numerical solver.

## 4. Pressure-correction attempt

A discrete axisymmetric Laplacian was assembled and a least-squares pressure correction was applied for a forward step `Δt=0.1`.

The resulting maximum divergence residual was

`max|∇·u_corrected| = 0.08579276595005263`.

The residual therefore did **not** decrease on this first coarse implementation.

The pressure solution norm was

`||p||₂ = 0.014486270760628873`.

The result is a direct falsification of the present pressure-projection implementation as a valid incompressibility closure.

## 5. Energy check

The weighted kinetic energy before correction was

`E_n = 1.9002923149485051`.

After the attempted pressure correction it was

`E_{n+1} = 1.9001136740630165`.

Change:

`ΔE = -1.7864088548846×10^-4`.

The small energy change is not interpreted as physical dissipation because the present projection failed the incompressibility residual test.

## 6. Ω structural check

Independently of the failed pressure closure, the Ω graph construction remains:

`C=(S-Sᵀ)/2`

`A=BCBᵀ`

with

`Aᵀ=-A`.

Therefore

`gᵀAg=0`

for any gradient `g`.

This structural property does not repair the failed pressure projection and is not claimed to do so.

## 7. Result

**PASS — RADIAL MOTION PRESENT.** `u_r ≠ 0` is present in the test state.

**FAIL — COARSE DISCRETE INCOMPRESSIBILITY CLOSURE.** The attempted pressure correction increased the maximum divergence residual from `0.08475173452016001` to `0.08579276595005263`.

**PASS — Ω SKEW STRUCTURE.** The graph-derived reversible operator remains mathematically power-neutral.

**NOT_PROVEN — PHYSICAL TRANSIENT AGREEMENT.** The failed pressure closure prevents a valid comparison against Navier–Stokes for this step.

**NOT_PROVEN — PRESSURE EMERGENCE.** No pressure prediction claim is justified.

## 8. Interpretation

This is a useful negative result.

The difficult part is no longer writing an abstract Ω operator. The difficult part is making the relational representation satisfy the same local constraints as the physical fluid equations on a finite mesh.

The next implementation must therefore construct the discrete divergence and gradient as compatible adjoint operators, include consistent radial face areas/volumes, and impose boundary conditions explicitly. Only after that should the pressure Poisson solve be compared with Ω dynamics.

## 9. Boundary

This experiment does not disprove Ω as a mathematical framework. It disproves only the present coarse pressure-projection implementation as a valid incompressible transient solver.

No claim of a new physical mechanism is made.
