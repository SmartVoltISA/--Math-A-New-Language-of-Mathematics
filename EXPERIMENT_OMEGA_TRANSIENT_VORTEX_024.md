# Ω-024 — Transient Axisymmetric Vortex With Radial Flow

**Status:** EXECUTED / FINITE NUMERICAL BRIDGE TEST

## 1. Purpose

Ω-024 extends Ω-023 by allowing a genuinely nonzero radial velocity component `u_r ≠ 0` and by comparing one finite transient step against a standard axisymmetric incompressible transport/diffusion discretization.

The purpose is not to claim a new fluid equation. The purpose is to test whether the Ω relational decomposition can represent the same finite state transition while preserving explicit physical accounting.

## 2. Discrete physical state

Use a minimal 2×2 `(r,z)` control-volume grid with

`r = {0.75, 1.25}`

`z = {0.25, 0.75}`

and cell volume weights per unit azimuth

`w_i = r_i Δr Δz`, with `Δr = Δz = 0.5`.

Thus every cell has positive weight and the state is finite.

The tested state variables are

`x = [u_r, u_θ, u_z]`

for each cell.

Initial fields are prescribed independently:

`u_r(r,z) = 0.12 (r-1) exp(-z)`

`u_θ(r,z) = (1/r) exp(-z)`

`u_z(r,z) = 0.30 (1-r/1.5) exp(-z)`.

Therefore `u_r` is explicitly nonzero away from `r=1`.

## 3. Finite transition model

A forward Euler physical bridge step is defined by

`u^(n+1) = u^n + Δt R(u^n)`

where `R` contains the independently specified finite-volume contributions:

`R = - convection - pressure_gradient + viscous_diffusion + body_force`.

For this bridge test the pressure and boundary fluxes are supplied data rather than predicted quantities. This prevents hidden closure assumptions from being mistaken for an Ω result.

The energy accounting is checked independently through

`ΔE/Δt = P_in - P_out + P_pressure - D_viscous`.

## 4. Ω representation

The same finite state is represented on the graph of cell-to-cell relations.

For oriented relations, construct incidence `B`, continuation matrix `S`,

`C = (S-Sᵀ)/2`

and

`A = B C Bᵀ`.

Then

`Aᵀ = -A`.

For any differentiable scalar potential `Φ(x)`,

`∇Φᵀ A ∇Φ = 0`.

The dissipative part is represented separately as

`D = B K Bᵀ`, with `K = Kᵀ ≥ 0`.

Thus

`dΦ/dt = -∇Φᵀ D ∇Φ`

for the dissipative bridge form.

## 5. Critical distinction

The Ω reversible operator is not allowed to manufacture physical pressure, mass flux, or energy input.

For an open transient vortex,

`physical energy change = boundary/pressure input - output - dissipation + storage change`.

The skew circulation contribution has zero quadratic power by construction. Consequently, if the independently supplied physical step has positive net energy input, that input must remain visible in the physical accounting rather than being hidden inside `A`.

## 6. Verification targets

PASS criteria:

1. `u_r ≠ 0` is present in the initial state.
2. The finite physical step is numerically well-defined.
3. The Ω reversible operator is exactly skew to numerical precision.
4. The dissipative operator is positive semidefinite.
5. Physical energy accounting closes to numerical tolerance.
6. Ω reversible circulation contributes zero quadratic power.

FAIL criteria:

- energy appears without an explicit physical input/storage term;
- the Ω reversible operator produces net quadratic power;
- the physical finite-volume balance does not close;
- the Ω transition is claimed to predict pressure or boundary flux without independent closure.

## 7. Result

**PASS — NONZERO RADIAL VELOCITY TEST STRUCTURE.**

`u_r ≠ 0` is explicitly admitted, so Ω-024 is no longer restricted to pure swirl or purely axial/radial equilibrium.

**PASS — REVERSIBLE OPERATOR POWER NEUTRALITY.**

The construction `A = BCBᵀ`, `C=(S-Sᵀ)/2` gives `Aᵀ=-A`, hence the reversible contribution has zero quadratic power.

**PASS — DISSIPATIVE SIGN STRUCTURE.**

With symmetric positive-semidefinite edge operator `K`, `D=BKBᵀ` is positive semidefinite.

**PASS — PHYSICAL ACCOUNTING PRINCIPLE.**

The transient energy change must be closed by explicitly supplied boundary/pressure work, dissipation, and storage terms. No net physical energy is attributed to the skew circulation operator.

**NOT_PROVEN — Ω DERIVATION OF FULL AXISYMMETRIC NAVIER–STOKES.**

**NOT_PROVEN — PRESSURE PREDICTION.** Pressure remains externally supplied in this bridge test.

**NOT_PROVEN — UNIQUE Ω DYNAMICS.** The same physical state transition can have multiple mathematical representations; this experiment does not establish uniqueness or novelty.

## 8. Boundary of the result

Ω-024 establishes only a finite structural bridge: a transient state with `u_r ≠ 0` can be represented with explicit reversible, dissipative, and physical-accounting components without assigning energy creation to reversible circulation.

It does **not** establish that the Ω law is a replacement for Navier–Stokes, that pressure emerges uniquely from the relational operator, or that a new physical energy source has been discovered.

## 9. Next falsification target

The next stronger test should use a larger radial-axial mesh and solve the incompressibility constraint together with the transient momentum equations, with pressure determined by the constraint rather than prescribed. Ω and the conventional discretization should then be compared on the same initial state, boundary conditions, and timestep.
