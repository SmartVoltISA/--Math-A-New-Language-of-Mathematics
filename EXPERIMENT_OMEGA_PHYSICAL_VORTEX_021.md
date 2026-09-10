# Ω-Math — EXPERIMENT_OMEGA_PHYSICAL_VORTEX_021

## Status

`EXECUTED / PHYSICAL-BRIDGE FINITE CHECK`

## Purpose

Test the Ω relation architecture against a concrete finite vortex balance using independently specified fluid observables: radius, density, circulation and pressure.

The target is deliberately narrow: verify whether the graph/relation architecture can represent the physical relation

`pressure potential difference ↔ azimuthal kinetic-energy difference`

without incorrectly interpreting the pressure difference as a net radial flow.

This is a bridge test, not a derivation of Navier–Stokes from Ω.

## Physical model

Use steady axisymmetric incompressible swirl with

`u_r = 0`, `u_z = 0`, `u_theta(r) = K/r`.

For radial equilibrium,

`dp/dr = rho * u_theta^2/r`.

Choose

`rho = 1`, `K = 1`, `r_i = 0.5`, `r_o = 2`, `p_o = 10`.

Integration gives

`p(r) = p_o + (rho*K^2/2)*(1/r_o^2 - 1/r^2)`.

Therefore

`p_i = 10 + 0.5*(0.25 - 4) = 8.125`.

The physical pressure-potential difference is

`(p_o-p_i)/rho = 1.875`.

## Kinetic contribution

At the inner contour,

`u_theta(r_i) = 1/0.5 = 2`.

Hence

`u_theta(r_i)^2/2 = 2`.

At the outer contour,

`u_theta(r_o) = 1/2 = 0.5`.

Hence

`u_theta(r_o)^2/2 = 0.125`.

Their difference is

`2 - 0.125 = 1.875`.

Thus the pressure-potential difference exactly equals the kinetic-energy difference:

`(p_o-p_i)/rho = [u_theta(r_i)^2-u_theta(r_o)^2]/2 = 1.875`.

Equivalently,

`p/rho + u_theta^2/2 = 10.125`

at both selected contours.

## Radial-force check

The radial Euler balance is

`a_r = - (1/rho) dp/dr + u_theta^2/r`.

Using the independently specified pressure law,

`(1/rho)dp/dr = u_theta^2/r`.

Therefore

`a_r = 0`.

This is a critical boundary result: a finite pressure difference and a circulating velocity field can coexist in radial equilibrium. The pressure difference is not, by itself, evidence of radial transport.

## Ω graph correspondence

The physical contours are treated as states connected by relations. A finite ordered cycle can supply the reversible circulation structure through

`C=(S-S^T)/2`.

The Ω reversible operator remains power-neutral for any gradient `g` because

`g^T A g = 0`,

with

`A=BCB^T`, `A^T=-A`.

For this physical bridge, the scalar quantity being compared is not declared to be the canonical Ω potential. The independently measured fluid quantity is the Bernoulli-type combination

`H = p/rho + u_theta^2/2`.

The finite vortex calculation gives the same `H=10.125` at `r_i` and `r_o`.

Therefore the bridge identifies a concrete physical invariant-like quantity that can serve as a candidate model potential for a future Ω fluid model, while keeping its physical status explicit rather than promoting it to a primitive.

## Numerical result

Using the stated values:

`Delta_p/rho = 1.875`.

`Delta_Kinetic = 1.875`.

`H_i = H_o = 10.125`.

`a_r = 0`.

All four checks pass to exact arithmetic for the supplied finite model.

## Falsification boundary

The test would fail as a physical Ω derivation if it claimed any of the following without additional equations or measurements:

1. that the Ω reversible term itself generates the pressure field;
2. that pressure difference alone implies radial flow;
3. that the scalar `H` is universally conserved in arbitrary viscous/open flows;
4. that the graph operator has thereby derived Navier–Stokes.

None of those claims is made here.

## Next physical test

The next stronger test is a transient/open vortex in which radial or axial mass flux is nonzero. There the model must account separately for boundary flux, pressure work, kinetic-energy change and dissipation, rather than only reproducing a steady balance.

## Result

`PASS — PHYSICAL RELATION CHECK`

`NOT_PROVEN — UNIVERSAL Ω FLUID DYNAMICS`

## Boundary

This experiment establishes a concrete correspondence between a known vortex pressure/kinetic balance and the Ω distinction between reversible circulation and dissipative transport. It does not establish that Ω is the governing physical theory of vortices or fluids.
