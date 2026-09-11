# Ω-Math Extension — Local Relational Propagation

**Status:** Mathematical model class
**Source lineage:** REL-PULSE-03

## 1. Minimal spatial graph

On a periodic one-dimensional graph with sites j,

`dx_j/dt = x_(j+1) - x_(j-1)`.

The rule is local and antisymmetric under the discrete inner product.

## 2. Conservation

For

`E = 1/2 Σ_j x_j²`,

index cancellation gives

`dE/dt = 0`.

The rule redistributes state without changing the quadratic measure.

## 3. Spectral branch

For a plane wave

`x_j(t) = exp(i(kj - ωt))`,

one obtains

`ω(k) = -2 sin(k)`

up to Fourier/sign convention.

The group velocity is

`v_g = dω/dk = -2 cos(k)`,

so `|v_g| ≤ 2` in the chosen dimensionless lattice units.

## 4. Control

The symmetric nearest-neighbor Laplacian

`dx_j/dt = x_(j+1) - 2x_j + x_(j-1)`

has

`λ(k) = -4 sin²(k/2)`,

which is non-positive and therefore describes relaxation/diffusion rather than conservative oscillation.

Thus locality alone does not select propagation of oscillatory modes.

## 5. Ω chain

`local distinction → local relation → conservative skew feedback → spectrum → propagating branch`.

## Boundary

The construction does not derive physical space, physical time, a universal speed, Maxwell equations or electromagnetic waves. Geometry, locality and the discrete evolution class are model inputs.
