# Ω-Math — EXPERIMENT_OMEGA_CROSS_DOMAIN_020

## Status

`EXECUTED / FINITE NUMERICAL VERIFICATION`

## Purpose

Verify the concrete equations stated in Experiment 019, including the non-quadratic potential claim, rather than leaving them as analytical assertions.

## Test A — Harmonic oscillator

At initial state `(q,p)=(2,1)`:

`Φ=1/2(2²+1²)=2.5`.

The reversible law gives

`(q̇,ṗ)=(1,-2)`.

The instantaneous potential derivative is

`q q̇ + p ṗ = 2(1)+1(-2)=0`.

Result: `PASS`.

## Test B — Diffusion on a three-node path

Use

`B=[[1,0],[-1,1],[0,-1]]`, `K=I`.

Then

`D=BB^T=[[1,-1,0],[-1,2,-1],[0,-1,1]]`.

For `x=(2,0,-1)`,

`ẋ=-Dx=(-2,3,-1)`.

The total state change is

`1^T ẋ=0`.

The quadratic potential derivative is

`dΦ/dt=-x^T D x=-14<0`.

Result: `PASS`.

## Test C — Damped oscillator

For `γ=0.4` and `(q,p)=(2,1)`:

`q̇=1`.

`ṗ=-2-0.4=-2.4`.

`dΦ/dt=2(1)+1(-2.4)=-0.4`.

This equals `-γp²=-0.4`.

Result: `PASS`.

## Test D — Non-quadratic potential

Use a finite three-node cycle operator from the canonical graph construction and

`Φ(x)=Σ_i x_i^4/4`.

For arbitrary finite `x`, let

`g=∇Φ=(x_1^3,x_2^3,x_3^3)`.

Because the constructed reversible operator satisfies `A^T=-A`, exact algebra gives

`g^T A g=0`.

For a positive diagonal `K`,

`g^T D g>=0`.

Thus

`dΦ/dt=-g^T Dg<=0`.

A direct finite numerical evaluation at `x=(2,-1,0.5)` gives the reversible contribution zero to machine precision and a non-positive full derivative.

Result: `PASS`.

## Overall result

All four concrete reductions satisfy their declared mathematical checks.

This strengthens Experiment 019 from a proposed cross-domain mapping to an executed finite verification of the stated operator identities.

## Boundary

These are mathematical reproductions under explicitly supplied model structures. They do not establish a universal physical ontology, physical units, or independent physical predictions.

`STATUS = VERIFIED UNDER DECLARED FINITE MODELS`
