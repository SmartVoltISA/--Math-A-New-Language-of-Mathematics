# EXPERIMENT Ω-033 — Cylindrical pressure-work compatibility

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Does a pressure-gradient work operator built from the same cylindrical face geometry become power-neutral on the divergence-free transport field, as required by incompressible kinetic-energy balance?

## Construction
The Ω-032 6×6 cylindrical control-volume geometry and divergence-free face fluxes are reused unchanged. A smooth cell pressure field is supplied independently:

`p(r,z) = sin(πr/2) cos(πz/2)`.

Pressure work is evaluated directly from face pressure differences and the physical face volume fluxes. No pressure projection is used to manufacture the result.

## Results
Maximum discrete cylindrical divergence:

`3.9968028886505635e-15`

Discrete pressure power:

`2.671474153004283e-16`

Thus pressure work is zero to numerical precision for this closed, divergence-free configuration.

## Result
**PASS — PRESSURE/TRANSPORT POWER COMPATIBILITY.**

The same geometric face-flux structure that enforces mass conservation also gives the discrete pressure-work cancellation expected from incompressibility.

This is a structural compatibility test, not a pressure solver or pressure prediction. The pressure field remains independently supplied.

## Boundary
NOT_PROVEN — independent pressure determination from the momentum equations.

NOT_PROVEN — full transient incompressible Navier–Stokes solution.

NOT_PROVEN — physical vortex pressure prediction.

## Consequence
The reversible side of the discrete kinetic-energy balance now contains two separately constructed pieces: conservative vector convection and pressure work. Both are power-neutral under the declared closed incompressible geometry. The next test adds a symmetric positive viscous operator and verifies the full energy accounting.
