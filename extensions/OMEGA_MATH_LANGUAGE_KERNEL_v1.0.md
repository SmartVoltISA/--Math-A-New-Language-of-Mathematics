# Ω-Math Language Kernel v1.0

Date: 2026-09-16
Status: Research specification / not promoted to primitive v0.9 core

## Purpose

Define a compact relational vocabulary for expressing structures discovered by the Ω-FUNDAMENT reduction work. This is a language layer: symbols denote declared roles and are not automatically identified with physical quantities.

## Primitive role candidates

`S` — state/configuration

`R` — relation/connection

`Δ` — distinction/difference between declared states or values

`C` — constraint limiting admissible states or transitions

`T` — transition rule

Candidate state transition:

`S' = T(S, Δ, R, C)`

The expression is schematic until a typed operational semantics is fixed.

## Structural operators

`BOUND(A,B)` — declares a boundary/domain separation between A and B.

`REL(A,B,r)` — declares a typed relation between A and B.

`DIFF(A,B)` — returns a declared difference/comparison object.

`LIMIT(X,C)` — restricts X by declared constraint C.

`CHANGE(S,S')` — denotes a state transition.

`FLOW(R,Δ,C,S)` — denotes a derived transfer/response object when the required semantics are declared.

`FEEDBACK(G)` — denotes a closed dependency/causal relation in a declared graph; not a primitive value.

`INVARIANT(F,T)` — declares a quantity/property F preserved by transition family T when proven or otherwise explicitly supported.

## Derived quantities / connector vocabulary

`POTENTIAL(Δ,R,C)` — candidate measure of available directed change under a relation and constraints.

`TRANSMISSION(R,S)` — generic connector property describing transfer capacity; conductivity and resistance are domain representations, not separate primitives.

`RESIST(ΔS,C)` — response opposing a declared change.

`IMPULSE(X,t) = ∫ X dt` — domain-specific integral construction.

`TRANSFER(X,Y) = ∫ X dY` — candidate generic transfer functional. It must not be called physical energy without domain validation.

`POWER(E,t) = dE/dt` — rate of a declared transfer quantity.

`MEMORY(S)` — retained information in state sufficient to alter future transition behavior; explicit history may be added when state augmentation is required.

`ADAPT(T,S)` — change in future transition behavior caused by feedback/state update.

## Graph principle

The language is graph-based, not a tree of permanent primitives.

A node may have one status in the core and another status in a derived graph. In particular:

`DERIVED(X) does not imply IRRELEVANT(X)`.

A derived object can become a connector between multiple domains while remaining non-primitive.

## Type discipline

Ω-Math must preserve the existing distinction between entity states and relation states. Do not encode absence as an additional relation value. Do not silently coerce physical scalars into primitive Ω values.

All future operators must declare:

- input types;
- output type;
- domain;
- algebraic assumptions;
- invariants/constraints;
- whether the operation is exact, approximate or empirical;
- verification status.

## Verification statuses

`DEF` — definition.

`DER` — mathematical derivation.

`EXEC` — executed computation/experiment.

`SUP` — independently supported structure.

`HYP` — hypothesis.

`THM` — theorem under stated assumptions.

`CE` — counterexample.

`REJ` — rejected.

## Anti-overreach rules

1. Structural similarity is not identity.
2. A common equation shape is not proof of a common physical ontology.
3. Transformation cost is not physical energy unless independently established.
4. Graph distance is not physical distance unless a physical mapping is demonstrated.
5. Sequence/order is not physical time unless a physical mapping is demonstrated.
6. Correlation is not causation.
7. A useful connector is not automatically a primitive.

## Current language loop

`DIFF → RELATE → LIMIT → TRANSITION → STATE → FEEDBACK → RELATE'`

This loop is the compact dynamic vocabulary currently being tested against the Ω-FUNDAMENT reduction.

## Research target

The language succeeds only if independent domain structures can be encoded with the same operators while preserving their necessary domain-specific constraints and without smuggling the target theory into the operator definitions.
