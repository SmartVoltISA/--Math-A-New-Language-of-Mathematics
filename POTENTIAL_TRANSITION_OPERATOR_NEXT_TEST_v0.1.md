# Ω-Math — Potential–Transition Operator: Conservation Test v0.1

## Purpose

This is the next test of `POTENTIAL_TRANSITION_OPERATOR_v0.1.md`.

The first candidate used one functional `Phi` for both reversible motion and dissipation:

`dx/dt = (A-D) delta(Phi)/delta(x)`.

The first structural question is whether that can remain valid when the physical system has **both conservation and irreversible production**.

## 1. Immediate result: one potential is too restrictive for a general thermodynamic claim

If

`dx/dt = A grad(Phi) - D grad(Phi)`

with `A*=-A` and `D=D*>=0`, then

`dPhi/dt = - <grad(Phi), D grad(Phi)> <= 0`.

Therefore the same `Phi` cannot simultaneously be a strictly conserved physical energy and a quantity that monotonically decreases under dissipation, except in special cases where the dissipative contribution is degenerate.

This is a **restriction of the first candidate**, not a failure of the relational principle.

## 2. Minimal two-potential extension

Introduce two declared state functionals:

`E[x]` — conserved quantity / energy-like invariant;

`S[x]` — entropy-like ordering functional.

Candidate dynamics:

`dx/dt = A[x] delta(E)/delta(x) + D[x] delta(S)/delta(x)`.

Structural conditions:

`A* = -A`

`D* = D, D >= 0`

and degeneracy conditions:

`A delta(S)/delta(x) = 0`

`D delta(E)/delta(x) = 0`.

## 3. Consequences

Energy balance:

`dE/dt = <delta(E), A delta(E)> + <delta(E), D delta(S)> = 0`.

The first term vanishes by antisymmetry. The second vanishes by `D delta(E)=0`.

Entropy balance:

`dS/dt = <delta(S), A delta(E)> + <delta(S), D delta(S)> = 0 + <delta(S), D delta(S)> >= 0`.

The first term vanishes by the degeneracy condition `A delta(S)=0`.

Thus the extended structure separates:

`conservative transition -> E conserved`

`irreversible transition -> S nondecreasing`.

## 4. Relation to the Ω principle

The original relational statement remains:

`POTENTIAL DIFFERENCE -> RELATION -> TRANSITION -> STATE CHANGE`.

The conservation test shows that a single scalar `Phi` should not be forced to represent every role.

A more precise candidate is:

`CONSERVATIVE DIFFERENCE -> reversible relation -> transition`

and

`IRREVERSIBLE DIFFERENCE -> dissipative relation -> transition`.

The balance condition is therefore typed by the quantity being balanced.

## 5. Network form

For a closed network with antisymmetric edge fluxes

`J_ij = -J_ji`,

the total conserved amount

`Q = sum_i Q_i`

satisfies

`dQ/dt = -sum_i sum_j J_ij = 0`.

Local flows may remain nonzero while the global sum is zero.

This gives the precise mathematical form of:

`BALANCE != ABSENCE`.

## 6. Critical boundary

The two-functional structure is closely related to established reversible/irreversible frameworks, especially GENERIC. This document does not claim independent discovery.

The Ω research task is to determine whether the same structure can be derived from the Ω relational primitives or must remain an external mathematical bridge.

## 7. Next falsification target

Do not add more physical examples yet.

First test whether a minimal finite relational network can realize all four properties simultaneously:

1. nonzero internal transitions;
2. exact conservation of `E`;
3. nondecreasing `S` under `D`;
4. zero global balance without zero local fluxes.

If this cannot be represented without importing extra primitives, the Ω formulation must be restricted.

## Status

- Single-functional operator: **restricted; insufficient as a general thermodynamic form**.
- Two-functional conservative/irreversible operator: **candidate bridge**.
- Conservation derivation under stated degeneracy/symmetry assumptions: **conditional algebraic result**.
- Universal Ω law: **UNKNOWN / NOT PROVEN**.
