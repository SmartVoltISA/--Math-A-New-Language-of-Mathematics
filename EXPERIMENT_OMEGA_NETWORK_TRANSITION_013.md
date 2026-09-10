# Ω-Math — EXPERIMENT_OMEGA_NETWORK_TRANSITION_013

## Status

`EXECUTED / FINITE EXACT VERIFICATION`

## Question

Can the minimal Ω network derive, from potential differences and relations alone, all four target properties simultaneously?

1. local nonzero transition;
2. global conservation of the transferred state quantity;
3. non-increasing potential under the dissipative component;
4. nonzero motion with zero net change of the conserved potential under the reversible component.

This test is the first direct finite test of the candidate potential-transition operator against the Ω relational chain:

`DISTINCTION → POTENTIAL DIFFERENCE → RELATION → TRANSITION → STATE CHANGE → BALANCE`.

## Frozen mathematical model

Use three nodes arranged as a closed directed cycle.

State:

`x = (x1,x2,x3)`.

Declare the quadratic potential:

`Phi(x) = 1/2 * x^T x`.

Therefore:

`grad Phi = x`.

### Reversible / circulation operator

`A = [[0,1,-1],[-1,0,1],[1,-1,0]]`.

It satisfies:

`A^T = -A`.

### Dissipative / equalizing operator

`D = [[2,-1,-1],[-1,2,-1],[-1,-1,2]]`.

It satisfies:

`D^T = D` and `x^T D x >= 0` for all `x`.

Both operators have zero row sum and zero column sum.

The candidate transition law is:

`dx/dt = (A - D) grad Phi`.

The reversible-only test is:

`dx/dt = A grad Phi`.

The dissipative-only test is:

`dx/dt = -D grad Phi`.

## Test 1 — reversible transition is nonzero while potential is conserved

Initial state:

`x = (2,0,-1)`.

Then:

`grad Phi = (2,0,-1)`.

The reversible transition is:

`A x = (1,-3,2)`.

Therefore:

`dx/dt != 0`.

But:

`dPhi/dt = x^T A x = 0`.

The state is moving while the declared potential remains exactly constant.

This is an exact algebraic result, not a numerical approximation.

## Test 2 — conservation of total state quantity

For the same reversible transition:

`1^T A = 0`.

Therefore:

`d(x1+x2+x3)/dt = 1^T A x = 0`.

For the dissipative operator:

`1^T D = 0`.

Therefore:

`d(x1+x2+x3)/dt = 0`.

For the combined operator:

`1^T(A-D)=0`.

Therefore the total state quantity is conserved in all three modes.

This is the network form of local transfer with no net creation/destruction at the closed boundary.

## Test 3 — dissipative transition reduces the potential

For the same initial state:

`-D x = (-5,1,4)`.

The transition is nonzero.

The potential derivative is:

`dPhi/dt = -x^T D x = -14`.

Hence:

`dPhi/dt < 0`.

The potential difference is being reduced by the dissipative relation.

## Test 4 — combined transition separates circulation from equalization

For the combined operator:

`(A-D)x = (-4,-2,6)`.

The transition remains nonzero.

The total state quantity remains conserved because:

`1^T(A-D)=0`.

The potential derivative remains:

`dPhi/dt = x^T(A-D)x = -14`.

The reversible part contributes exactly zero to the potential derivative; the dissipative part contributes all of the decrease.

## Exact structural result

For any state `x`:

`x^T A x = 0`

because `A` is antisymmetric.

And:

`x^T D x >= 0`

because `D` is positive semidefinite.

Therefore:

`dPhi/dt = -x^T D x <= 0`.

At the same time, because the operators have zero column sum:

`d(1^T x)/dt = 0`.

Thus the same minimal closed network supports both:

`LOCAL TRANSITION != 0`

and

`GLOBAL BALANCE = 0`.

## What this establishes

`PASS` — a finite relational network can contain nonzero local transitions while its total transferred quantity is exactly conserved.

`PASS` — an antisymmetric relation operator produces circulation/state redistribution without changing the quadratic potential.

`PASS` — a symmetric positive-semidefinite relation operator produces potential reduction while preserving the closed-system total state quantity.

`PASS` — the combined operator separates reversible circulation from dissipative equalization.

This is the precise finite mathematical realization of:

`BALANCE != ABSENCE`.

## What this does NOT establish

It does not establish that `A-D` is a new fundamental law of nature.

It does not derive physical energy, entropy, pressure, temperature, time, or causality from Ω-Math.

It does not prove that every physical system admits this exact finite representation.

The result is a mathematical bridge and an exact finite verification under explicitly declared assumptions.

## Important boundary

The Ω v0.9 primitive core remains unchanged.

The experiment uses ordinary real-valued state variables and linear operators as an external mathematical bridge. These are not silently promoted to Ω primitives.

## Next test

The next decisive step is to remove the hand-specified matrices and construct `A` and `D` directly from the Ω relation/path structure of a finite graph.

Target:

`relation graph → edge potential differences → edge fluxes → node balance → induced A/D decomposition`.

If the decomposition can be derived from the relational structure rather than inserted by hand, the candidate formula moves one level closer to an Ω-derived mathematical law.
