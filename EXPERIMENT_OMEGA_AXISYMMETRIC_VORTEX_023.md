# Ω-Math — EXPERIMENT_OMEGA_AXISYMMETRIC_VORTEX_023

## Status

`EXECUTED / FINITE RADIAL-AXIAL PHYSICAL BRIDGE CHECK`

## Purpose

Extend the physical vortex bridge from a purely radial annulus to a finite axisymmetric radial+axial field. Geometry and directed transport relations are constructed first; the physical velocity field is supplied independently. The Ω operator is then checked for structural invariants and energy-accounting compatibility.

This is a bridge/falsification experiment, not a derivation of Navier–Stokes.

## Finite geometry

Use a 3 × 3 cylindrical cell field.

Radial cell centers:

`r = {0.5, 1.0, 1.5}`

Axial cell centers:

`z = {0, 0.5, 1.0}`

Cell spacing:

`dr = 0.5`, `dz = 0.5`.

Unit density is used:

`rho = 1`.

Each cell receives cylindrical volume weight

`w = 2*pi*r*dr*dz`.

The finite state therefore contains 9 spatial cells.

## Independently specified velocity field

Azimuthal velocity:

`u_theta(r,z) = K/r * exp(-z/L)`

with

`K = 1`, `L = 1`.

Axial velocity:

`u_z(r,z) = U0*(1-r/1.5)*exp(-z/L)`

with

`U0 = 0.3`.

The field values are generated from these physical expressions and are not fitted to the Ω operator.

The radial velocity is set to zero for this finite bridge:

`u_r = 0`.

This makes the test deliberately conservative about interpretation: it contains radial geometry and axial transport relations, but does not claim a nonzero radial velocity.

## Stored kinetic energy

Cell kinetic-energy density is

`e_k = 1/2*(u_theta^2 + u_z^2)`.

Weighted finite storage is

`E_k = sum(w*e_k)`.

Numerical evaluation gives

`E_k = 4.364366302899918 J`.

## Dissipation proxy

For a finite physical consistency check, use the positive quadratic gradient measure

`D = mu * sum[w*(|grad u_theta|^2 + |grad u_z|^2)]`

with

`mu = 0.1`.

Finite-difference derivatives use the stated uniform spacings `dr=dz=0.5`.

The resulting positive dissipation measure is

`D = 1.8016799204895362 W`.

This is explicitly a dissipation proxy for the finite field, not a claim that the discretization is a complete Navier–Stokes viscous operator.

## Directed transport graph

Nodes are the 9 cells.

Directed radial relations connect each cell to its neighbor at increasing r. Directed axial relations connect each cell to its neighbor at increasing z.

There are 12 directed nearest-neighbor relations in total:

`6 radial + 6 axial = 12`.

The incidence matrix `B` is constructed from these relations. For each edge `e=(a,b)`, its column has `+1` at `a`, `-1` at `b`.

Therefore

`1^T B = 0`.

## Ω reversible continuation operator

The directed edge-continuation matrix is constructed without fitting:

`S[e,f] = 1` iff the terminal node of edge `e` equals the initial node of edge `f`.

Then

`C = (S-S^T)/2`.

The induced node operator is

`A = B C B^T`.

Direct finite evaluation gives

`A^T = -A`

exactly.

Therefore, for every scalar gradient `g`,

`g^T A g = 0`.

The Ω reversible circulation structure is thus power-neutral under the scalar pairing, including this radial+axial geometry.

## Physical interpretation

The field has three distinct layers:

`azimuthal circulation → axial variation → dissipative gradient loss`.

The pressure field has deliberately not been inferred from the Ω operator. Likewise, no pressure gradient is inserted into the calculation and then declared to be predicted.

The test therefore checks the structural compatibility of Ω with a finite three-dimensional-looking axisymmetric transport geometry while preserving the physical boundary between structure and fluid dynamics.

## Key result

The finite radial+axial geometry produces a valid incidence operator and a graph-derived skew circulation operator.

The physical field has finite stored kinetic energy:

`E_k = 4.364366302899918 J`.

The finite positive dissipation proxy is:

`D = 1.8016799204895362 W`.

The graph-derived reversible operator satisfies:

`A^T + A = 0`.

Thus its scalar power contribution is identically zero:

`g^T A g = 0`.

## Falsification boundary

This experiment would fail as a structural bridge if the graph construction produced a nonskew reversible operator or violated incidence conservation.

It would also fail conceptually if the Ω operator were claimed to predict the supplied pressure, velocity, or dissipation without an independently specified physical constitutive model.

Neither failure occurs here.

## Result

`PASS — RADIAL+AXIAL GRAPH CONSTRUCTION`

`PASS — SKEW REVERSIBLE OPERATOR`

`PASS — FINITE POSITIVE DISSIPATION MEASURE`

`NOT_PROVEN — Ω DERIVATION OF AXISYMMETRIC NAVIER–STOKES`

`NOT_PROVEN — PHYSICAL PREDICTION OF PRESSURE FIELD`

## Next stronger test

Introduce a genuinely transient radial velocity `u_r != 0` and compare the Ω-predicted finite state transition against an independently solved axisymmetric fluid time step. The pressure, velocity and boundary flux must remain externally supplied until the comparison is complete.
