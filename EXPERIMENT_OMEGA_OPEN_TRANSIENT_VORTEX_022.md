# Ω-Math — EXPERIMENT_OMEGA_OPEN_TRANSIENT_VORTEX_022

## Status

`EXECUTED / FINITE OPEN-SYSTEM ENERGY-BALANCE CHECK`

## Purpose

Test the Ω architecture on a deliberately open, transient vortex-like transport model where mass and energy cross a boundary. The test must distinguish:

`stored energy change`, `boundary energy flux`, `pressure work`, `kinetic energy`, and `dissipation`.

This is stronger than Experiment 021 because the system is no longer in radial equilibrium and has nonzero boundary transport.

## Finite physical model

Consider a unit-density control volume containing a rotating annular fluid packet. Its tracked state is represented by a scalar kinetic-energy storage `E_k` and a boundary flux `F_out`.

At an instant, choose

`E_k = 2.0 J`,

`F_in = 3.0 W`,

`F_out = 1.5 W`,

`P_pressure = 0.5 W`,

`D = 1.0 W`.

The signs are defined so that positive `F_in` enters the control volume, positive `F_out` leaves it, pressure power `P_pressure` enters the tracked mechanical-energy budget, and `D` is irreversible dissipation/rejection.

The open-system accounting law is

`dE_system/dt = F_in - F_out + P_pressure - D`.

Therefore

`dE_system/dt = 3.0 - 1.5 + 0.5 - 1.0 = 1.0 W`.

So the stored energy increases at `1.0 J/s`.

## Boundary transport as relation flow

Represent the control volume and its environment as states joined by directed relations. Let `B` be the incidence operator. For an edge flux vector `j`, node balance is

`dx/dt = -B j`.

The identity

`1^T B = 0`

shows that internal edge exchange cancels in the closed aggregate. For the open system, boundary edges are retained explicitly rather than hidden inside the state.

This gives the structural distinction:

`internal circulation != boundary transport`.

A skew/reversible operator can represent circulation, while boundary flux and dissipative terms account for net exchange and irreversible loss.

## Transient vortex interpretation

Take two contours with azimuthal speeds

`u_theta,i = 2 m/s`,

`u_theta,o = 0.5 m/s`.

Their kinetic-energy difference per unit mass is

`Delta K = (2^2 - 0.5^2)/2 = 1.875 J/kg`.

Unlike Experiment 021, the present test does not set radial acceleration to zero. A boundary flux is explicitly present, so the pressure/kinetic relation cannot be interpreted as a closed equilibrium identity.

The physical model therefore requires the accounting identity rather than only a Bernoulli-type equality.

## Ω correspondence

The structural decomposition is

`transition = reversible circulation + dissipative transport + boundary exchange`.

For the graph-derived reversible term

`A = B C B^T`,

with

`C = (S-S^T)/2`,

we have

`A^T = -A`.

Thus for any gradient `g`,

`g^T A g = 0`.

This means the reversible circulation term is power-neutral with respect to the scalar potential pairing. It cannot by itself account for the net `+1.0 W` stored-energy increase of the open system.

The missing contribution is precisely represented by boundary and dissipative terms. This is a useful constraint rather than a failure: an open system cannot be modeled as a closed conservative circulation alone.

## Numerical accounting check

`F_in - F_out + P_pressure - D = +1.0 W`.

Over a short interval `dt = 2 s`, assuming these instantaneous rates remain constant,

`Delta E_system = 2.0 J`.

Starting from `E_system(0)=2.0 J`,

`E_system(2 s)=4.0 J`.

The energy increase is fully accounted for by the declared external/irreversible terms.

## Falsification boundary

The model fails if the Ω mapping is forced to explain the observed open-system energy change using only the skew circulation operator. It cannot: the skew contribution has zero scalar power.

It also fails if boundary exchange is omitted while claiming energy accounting for an open control volume.

Therefore the stronger model requirement is:

`open dynamics = internal relation dynamics + explicit boundary exchange + dissipation/storage accounting`.

## Result

`PASS — OPEN-SYSTEM ACCOUNTING STRUCTURE`

`PASS — REVERSIBLE CIRCULATION REMAINS POWER-NEUTRAL`

`NOT_PROVEN — Ω DERIVATION OF TRANSIENT NAVIER–STOKES`

## Boundary

This is a finite consistency/bridge experiment with explicitly assigned physical rates. It demonstrates the required accounting architecture but does not independently predict those rates from Ω. A genuine predictive test must obtain pressure, velocity, flux and dissipation from measured or independently solved fluid data and then test the Ω decomposition without fitting the result.

## Next test

The next target is therefore a discretized radial/axial fluid field with pressure and velocity supplied independently. The Ω operators must be constructed from the geometry and directed transport graph before comparing predicted state change against the independent fluid solution.
