# Ω-Math Research Layer — Typed Transport v0.1

## Status

`PROPOSED / RESEARCH / NOT CORE`

## Purpose

This document defines the smallest transport layer currently justified by finite verification. It sits above the Ω v0.9 relational core and must not silently change primitive meanings.

## 1. Typed local state

Each entity `x` may carry an explicitly declared local state set `X_x`.

The sets may be identical or heterogeneous.

No numerical, physical, geometric or probabilistic interpretation is implied.

## 2. Transport on a relation

For a relation

`r:x→y`

an external model may declare a transport map

`T_r:X_x→X_y`.

The relation sign remains an Ω relation state and is not automatically identified with the transport map.

Therefore:

`Relation ≠ Transport`.

## 3. Path transport

For a path

`P=(r_1,...,r_n)`

with compatible fibers, define

`T_P=T_{r_n}∘...∘T_{r_1}`.

For the empty path,

`T_{ε_x}=id_{X_x}`.

For compatible paths,

`T_{P⧺Q}=T_Q∘T_P`.

Associativity and identity follow from ordinary function composition.

## 4. Loop residual

For a closed path `L` based at `x`, define its residual by comparison of

`T_L:X_x→X_x`

with `id_{X_x}`.

The simplest predicate is

`Trivial(L) ⇔ T_L=id_{X_x}`.

`Nontrivial(L) ⇔ T_L≠id_{X_x}`.

This is a derived structure, not an Ω primitive.

## 5. What is not required

The residual definition does not require:

- numerical addition;
- scalar sign multiplication;
- injectivity;
- surjectivity;
- inverses for the edge transports;
- a vector space;
- a metric;
- a topology;
- physical time;
- physical energy;
- probability;
- curvature.

## 6. Optional stronger layer: frame changes

If local frame changes are required, declare isomorphisms

`g_x:X_x→X_x`

with inverses. Then

`T'_{xy}=g_y∘T_{xy}∘g_x^{-1}`.

For a closed loop based at `x`,

`T'_L=g_x∘T_L∘g_x^{-1}`.

Hence identity/non-identity of loop transport is preserved.

This stronger requirement is separate from the minimal residual algebra.

## 7. Type boundaries

The following distinctions are mandatory:

`relation sign ≠ transport map`

`path ≠ path transport`

`transport composition ≠ Ω primitive relation composition`

`loop residual ≠ curvature`

`non-invertible transport ≠ physical irreversibility`

`transport map ≠ physical connection field`.

## 8. Minimality status

`EXPERIMENT_TRANSPORT_MINIMALITY_006.md` shows that arbitrary composable functions are sufficient for nontrivial residual generation and that bijectivity is therefore not required at the minimal layer.

The term “minimal” remains operational: it means a strictly weaker sufficient package than the bijective model tested in LIGHT Bridge 005, not a formal proof of uniqueness/minimality among all possible foundations.

## 9. Admission criteria before any promotion

Before this layer can become canonical or alter Ω primitives, it must pass:

1. heterogeneous-fiber typing;
2. identity and associativity checks;
3. path concatenation compatibility;
4. information-loss analysis;
5. interaction with transformations and equivalence;
6. cross-domain tests independent of LIGHT;
7. comparison with category-theoretic / automata / graph formulations;
8. explicit counterexamples to proposed reductions;
9. no hidden physical semantics.

## Decision boundary

Current status:

`Ω v0.9 core CLOSED`

`Typed Transport v0.1 PROPOSED / RESEARCH`

The transport layer is a candidate mathematical extension above the core, not yet a new primitive.
