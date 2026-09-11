# Ω-Math Extension — Dissipation vs Conservation

**Status:** Mathematical classification

## Conservative class

If a positive-definite quadratic measure is exactly conserved, the linear first-order generator is skew-adjoint in the corresponding metric. Its eigenvalues have zero real part.

Typical behavior: exchange, recurrence, oscillatory modes, neutral modes.

## Dissipative class

If the generator has a negative symmetric part, amplitudes can decay. For a Euclidean quadratic measure,

`dE/dt = xᵀ ((A+Aᵀ)/2) x`.

A negative-semidefinite symmetric part gives non-increasing E.

Typical behavior: relaxation, diffusion, decay.

## Unstable class

A positive symmetric contribution can produce growth for some states.

Typical behavior: amplification, bifurcation or instability, depending on nonlinear saturation and constraints.

## Key distinction

`feedback` does not imply `oscillation`.

`locality` does not imply `oscillation`.

`conservation + the declared linear first-order class` supplies the relevant spectral restriction.

## Ω use

This classification prevents the language from treating every feedback process as pulsation. It gives a formal place for negative controls and countermodels.
