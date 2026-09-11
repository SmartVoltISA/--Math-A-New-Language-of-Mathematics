# Ω-026 — Compatible Cylindrical Pressure Projection

**Status:** EXECUTED / FINITE-VOLUME CONSTRAINT VERIFICATION

## 1. Objective

Repair the failure identified in Ω-025 by constructing the pressure correction from compatible finite-volume divergence/gradient operators with cylindrical geometry weights.

The key test is whether pressure correction can reduce the discrete incompressibility residual to numerical roundoff without inventing a physical energy source.

## 2. Grid

Cell centers:

`r = {0.6, 1.0, 1.4}`

`z = {0.2, 0.6, 1.0}`

`Δr = Δz = 0.4`, `ρ=1`, `Δt=0.1`.

The cell mass/volume weight per unit azimuth is

`M_i = r_i Δr Δz`.

Internal radial face weights are

`w_f = r_f Δz`.

Internal axial face weights are

`w_f = r_i Δr`.

These are geometry-derived rather than arbitrary graph weights.

## 3. Initial velocity

The same transient vortex family is used:

`u_r = 0.12(r-1)e^{-z}`

`u_θ = r^{-1}e^{-z}`

`u_z = 0.30(1-r/1.5)e^{-z}`.

Thus radial motion is present.

Using face interpolation and cylindrical finite-volume divergence, the initial maximum cell residual is

`max|∇·u| = 0.26919048901585885`.

This deliberately exposes the discrete constraint error before projection.

## 4. Compatible operators

Let `B` be the oriented cell-to-cell incidence matrix for the 12 internal relations and `W_f` the diagonal matrix of physical face areas/weights.

The positive weighted graph Laplacian is

`A_p = M^{-1} B W_f B^T`.

The pressure correction is constructed from the same operators:

`u^{n+1} = u^* - Δt ∇_h p`.

The discrete pressure equation is

`A_p p = (∇_h·u^*)/Δt`.

A zero-mean pressure gauge is imposed through the compatibility constraint.

## 5. Numerical result

The pressure system was solved with the zero-mean gauge.

Pressure norm:

`||p||₂ = 1.3396667239358593`.

The corrected divergence residual was

`max|∇·u^{n+1}| = 8.326672684688674×10^{-17}`.

Residual norm:

`||residual||₂ = 1.389512421408389×10^{-16}`.

Therefore the compatible pressure correction reduces the divergence constraint to machine precision.

## 6. Energy observation

Weighted kinetic energy before the cell-centered pressure correction was

`E_n = 0.3024409152435954`.

For the simple reconstructed cell-centered velocity used to inspect the correction, the resulting value was

`E_{n+1} = 0.32652600476440996`.

Hence

`ΔE = +0.024085089520814562`.

This change is **not** interpreted as physical energy generation. The pressure projection changes the velocity representation, and the present boundary treatment does not provide a complete closed/open energy budget. A future energy-consistent projection test must include all boundary pressure work and face kinetic-energy fluxes.

## 7. Ω structural correspondence

The same compatible incidence structure is directly compatible with the Ω graph construction.

For oriented continuation relations,

`C=(S-S^T)/2`

and

`A_Ω = B C B^T`.

Then

`A_Ω^T=-A_Ω`

and therefore

`g^T A_Ω g = 0`.

The pressure constraint operator is a separate symmetric geometry-weighted operator. This separation is important: reversible circulation, pressure constraint, and dissipation are not collapsed into one unexplained term.

## 8. Result

**PASS — CYLINDRICAL GEOMETRY WEIGHTS.** Face and cell weights follow the `r`-weighted finite-volume geometry.

**PASS — COMPATIBLE PRESSURE CORRECTION.** The discrete incompressibility residual is reduced to `8.33×10^-17`.

**PASS — ZERO-MEAN PRESSURE GAUGE.** The singular pressure null mode is handled explicitly.

**PASS — Ω SKEW STRUCTURE.** The relational circulation operator remains power-neutral.

**NOT_PROVEN — ENERGY-CONSERVING PRESSURE PROJECTION.** The inspected cell-centered energy change is not a closed physical energy balance.

**NOT_PROVEN — FULL TRANSIENT NAVIER–STOKES AGREEMENT.** Convection, viscous terms, boundary fluxes, and pressure work have not yet been compared as a complete solver step.

## 9. Interpretation

Ω-025's failure was numerical, not a failure of the underlying incompressibility concept. The corrected construction shows that the missing ingredient was operator compatibility and cylindrical geometry weighting.

This is a stronger result than Ω-025 because the pressure constraint is now actually enforced on the finite mesh.

At the same time, this does not validate Ω as a physical replacement for Navier–Stokes. It only establishes that the relational graph and a physically weighted finite-volume constraint can coexist without violating the local incompressibility constraint.

## 10. Next falsification target

Build Ω-027 as a full transient step containing:

`convection + pressure + viscous diffusion + radial/axial boundary fluxes`.

Use the same initial state and timestep for both the conventional finite-volume solver and the Ω decomposition. Compare the complete velocity field, pressure field, divergence, and energy budget rather than only the constraint projection.
