# Ω-Math — Boundary Flux and Global Conservation

**Status:** conditional mathematical result.

## Local-to-global audit

For the normalized two-field system

`∂t E = ω curl B`

`∂t B = −ω curl E`,

with

`H = 1/2 ∫_V (|E|²+|B|²) dx`,

one obtains

`dH/dt = ω∫_V [E·curl B − B·curl E] dx`.

Using

`∇·(B×E) = E·curl B − B·curl E`,

we obtain the boundary form

`dH/dt = ω∮_{∂V} (B×E)·n dS`.

Therefore global conservation on a finite domain requires the boundary flux to vanish. Periodic domains, sufficiently rapid decay, or appropriate boundary conditions can enforce this. Open boundaries generally permit exchange with the exterior.

## Consequence

The statement

`local antisymmetric dynamics ⇒ globally conserved quadratic quantity`

is incomplete unless the spatial domain and boundary conditions are specified.

The correct statement is:

`local antisymmetric dynamics + admissible pairing + zero net boundary flux ⇒ global conservation`.

## Why this matters for Ω-Math

This adds a precise boundary layer between local relation dynamics and global invariants. It also prevents confusing conservation inside a closed mathematical domain with conservation of an open subsystem.

## Evidence class

Derivation.

## Non-claims

No physical energy flux, Poynting vector, electromagnetic field, or physical conservation law is inferred by this mathematical identity alone.
