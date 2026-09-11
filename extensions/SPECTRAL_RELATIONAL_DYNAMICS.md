# Ω-Math Extension — Spectral Relational Dynamics

**Status:** Mathematical extension

## Core object

For a linear relational evolution

`dx/dt = A x`,

spectral decomposition describes the intrinsic modes of the relation operator.

## Mode classes

- `λ = 0` — stationary / neutral mode at linear order.
- `Re(λ) < 0` — dissipative / relaxing mode.
- `Re(λ) > 0` — unstable / amplifying mode.
- `λ = iω` with `ω ≠ 0` — oscillatory mode in the conservative linear class.
- Complex eigenvalues with nonzero real and imaginary parts — damped or amplified oscillation.

## Conservative restriction

For a positive-definite quadratic conserved measure, the operator is metric-skew and its spectrum lies on the imaginary axis (including zero), as established in the Conservation and Operator Selection extension.

## Important distinctions

`oscillatory mode ≠ periodic trajectory` in general.

A system may contain several incommensurate frequencies and therefore be quasiperiodic.

`zero eigenvalue ≠ zero state`.

A neutral mode can contain nonzero stored state while remaining stationary at linear order.

## Ω role

Spectrum is the bridge between relational operators and dynamical behavior. It provides a representation in which stability, relaxation, oscillation, recurrence and mode selection can be stated without identifying the mathematical state with a physical quantity.

## Boundary

No physical interpretation of eigenvalues, frequency, energy or time is assumed here. Such interpretations require separate declared models and dimensional matching.
