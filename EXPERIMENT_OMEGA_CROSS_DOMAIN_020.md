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

Use the canonical three-cycle construction with edges

`(1→2),(2→3),(3→1)`.

Its incidence matrix is

`B=[[1,0,-1],[-1,1,0],[0,-1,1]]`.

The continuation matrix is

`S=[[0,1,0],[0,0,1],[1,0,0]]`.

Therefore

`C=(S-S^T)/2`

and

`A=BCB^T
 =[[0,1.5,-1.5],[-1.5,0,1.5],[1.5,-1.5,0]]`.

Use

`Φ(x)=Σ_i x_i^4/4`,

so

`g=∇Φ=(x_1^3,x_2^3,x_3^3)`.

At

`x=(2,-1,0.5)`,

`g=(8,-1,0.125)`.

Direct evaluation gives

`g^T A g = 0` exactly in the finite arithmetic calculation.

With `K=I`,

`D=BB^T`

and

`g^T D g = 144.28125`.

Hence

`dΦ/dt = -144.28125 < 0`.

The reversible contribution is zero while the dissipative contribution is strictly negative.

Result: `PASS`.

## Overall result

All four concrete reductions satisfy their declared mathematical checks.

The non-quadratic test confirms that the skew-symmetry argument is not specific to the quadratic choice of `Φ`: the reversible contribution vanishes for the gradient of the tested nonlinear potential as well.

## Boundary

These are mathematical reproductions under explicitly supplied model structures. They do not establish a universal physical ontology, physical units, or independent physical predictions.

`STATUS = VERIFIED UNDER DECLARED FINITE MODELS`
