# EXPERIMENT Ω-035 — Complete discrete kinetic-energy balance

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Purpose
Combine the independently constructed cylindrical vector convection, pressure work, and positive viscous operator into one kinetic-energy accounting check.

## Components
The reversible convective term is Ω-032: direct face-flux transport plus cylindrical curvature terms.

The pressure term is Ω-033: face pressure differences paired with the same physical volume fluxes.

The dissipative term is Ω-034: geometry-derived symmetric positive graph stiffness with `ν=0.05`.

No component is defined by subtracting the others from a known answer.

## Observed powers
Convective power:

`9.823955884891156e-16 W`

Pressure power:

`2.671474153004283e-16 W`

Viscous power:

`-1.7233430195339945 W`

Total instantaneous kinetic-energy power:

`-1.7233430195339936 W`

Thus, to numerical precision,

`dE_k/dt = P_conv + P_pressure + P_viscous`

with

`P_conv ≈ 0`,

`P_pressure ≈ 0`,

`P_viscous < 0`.

## Result
**PASS — COMPLETE DISCRETE KINETIC-ENERGY ACCOUNTING.**

The construction exhibits the intended Ω split at the level of a finite cylindrical vector flow:

`reversible transport + pressure-neutral constraint + positive dissipation`.

The result is obtained from geometry, face fluxes, curvature relations, and an independently positive stiffness operator.

## Critical boundary
This is still a finite-volume structural bridge, not a proof or complete independent solver for the physical Navier–Stokes equations.

The present viscous operator is componentwise and omits the full cylindrical strain-rate coupling. Pressure is supplied rather than solved from a pressure-Poisson equation. The initial field is analytically constructed rather than measured from an experiment.

Therefore the result establishes **discrete structural compatibility**, not a new physical law or an experimentally validated vortex mechanism.

## Next decisive test
Build an independent transient axisymmetric incompressible reference solver with pressure projection and full cylindrical viscous terms. Build the Ω transition from the geometry/flux rules without looking at the reference result, then compare one or more time steps, including velocity field, pressure-compatible constraint, and kinetic-energy change. Any mismatch is to be recorded as FAIL rather than repaired by post-hoc projection.
