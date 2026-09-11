# Ω-Math Extension — Conservation and Operator Selection

**Status:** Mathematical extension / conditional theorem within a declared class
**Source lineage:** REL-PULSE-01/02

## 1. Setting

Let the state be x ∈ R^n and consider linear first-order evolution

`dx/dt = A x`.

Let a positive-definite quadratic quantity be

`E(x) = 1/2 xᵀ K x`,

where `K = Kᵀ > 0`.

## 2. Conservation condition

Exact conservation for every state requires

`dE/dt = xᵀ K A x = 0`.

For all x this is equivalent to

`K A + Aᵀ K = 0`.

Thus A is skew-adjoint with respect to the metric K.

Under the change of variables `y = K^(1/2)x`, the generator becomes

`B = K^(1/2) A K^(-1/2)`

with

`B + Bᵀ = 0`.

Therefore its eigenvalues are purely imaginary or zero.

## 3. Consequence

Within this exact class:

`positive quadratic conservation + linear first-order evolution`

`→ metric-skew generator`

`→ imaginary/zero spectrum`

`→ oscillatory or stationary linear modes`.

This is a theorem about the declared mathematical class, not a derivation of the class itself.

## 4. Boundaries

The result does not derive:

- first-order evolution;
- continuous physical time;
- positive-definite quadratic conservation;
- finite-dimensional state space;
- a particular frequency;
- a particular physical interpretation.

## 5. Counterexamples outside the class

`dx/dt = 0` conserves E but has no nontrivial motion.

A dissipative generator with negative real eigenvalues relaxes rather than oscillates and violates exact conservation.

Multiple independent rotations may be quasiperiodic rather than periodic.

## 6. Ω interpretation

The important reusable distinction is:

`conservation` does not by itself mean `oscillation`.

Oscillation follows only after the structural assumptions that place the generator in the skew-adjoint linear first-order class are explicitly declared.
