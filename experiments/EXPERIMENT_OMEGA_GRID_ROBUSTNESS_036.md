# EXPERIMENT Ω-036 — Grid-family robustness

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Purpose
Check whether the direct vector cylindrical flux construction of Ω-032 is a single-grid accident.

The same mathematical construction is run on 4×4, 6×6, 8×8, 10×10 and 12×12 grids.

## Results
4×4: divergence `0.0`, convective power `7.77e-16`.

6×6: divergence `3.997e-15`, convective power `9.82e-16`.

8×8: divergence `5.68e-15`, convective power `1.78e-15`.

10×10: divergence `1.85e-14`, convective power `1.57e-15`.

12×12: divergence `3.20e-14`, convective power `3.83e-15`.

All values remain below the declared `1e-12` verification tolerance.

## Result
**PASS — GRID-FAMILY ROBUSTNESS.**

The energy-neutrality and discrete divergence properties persist over the tested grid family. The construction is therefore not dependent on one particular 6×6 matrix realization.

## Boundary
This remains a numerical structural verification of the declared finite-volume construction. It is not an independent experimental validation and does not establish the full physical Navier–Stokes equations.
