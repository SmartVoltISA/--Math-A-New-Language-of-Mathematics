# Ω-Math — Invariants and Symmetry v0.2

## 1. Principle

An invariant is never absolute. It is always an invariant **under a specified transformation family**.

`I(T(S)) = I(S)` for all admissible `T ∈ 𝒯`.

## 2. First transformation families

### Label permutations

`𝒯_label` permutes entity identifiers while preserving relational organization and states attached to the corresponding entities.

Structural observables should be invariant under this family unless labels themselves are explicitly modeled.

### Relation-preserving isomorphisms

`𝒯_iso` changes representation while preserving the relevant typed relational structure.

### Observation quotients

`𝒯_Q` intentionally removes declared distinctions. Most fine-grained structural quantities are not expected to remain invariant; the preservation target must be stated.

### Dynamics

`𝒯_dyn` contains admissible transitions of a specified model. A dynamical invariant is a property preserved along those transitions.

## 3. Candidate structural invariants

For a declared representation, candidates include:

- entity count;
- relation count;
- sign counts;
- component count;
- degree sequence;
- cycle rank;
- path-length distribution;
- reachability relation;
- strongly connected component structure.

None is universal. Each depends on representation and transformation family.

## 4. Symmetry

For an equivalence `≈`, define

`Sym_≈(S) = {T | T(S) ≈ S}`.

A symmetry may preserve the system exactly or only at a declared observational/behavioral level.

This separates:

`same object`

from

`same description`

and

`same behavior`.

## 5. Invariant hierarchy

The current research hierarchy is:

`primitive identity/state`

`→ relation structure`

`→ topology`

`→ path structure`

`→ dynamics`

`→ behavior`.

A coarse invariant can survive while finer distinctions are lost. Therefore equality of one invariant is never sufficient to establish equivalence unless sufficiency has been demonstrated for the declared task.

## 6. Experimental rule

For every proposed invariant, record:

1. object being measured;
2. transformation family;
3. expected invariance;
4. exact calculation;
5. null/control;
6. counterexample search;
7. whether preservation is formal or empirical.

## 7. Derived geometry

A geometric quantity may be introduced only after a transformation family and structural cost are defined. Candidate distance is based on minimal admissible transformation cost, not primitive spatial distance.

If the resulting quantity satisfies metric axioms, it may be called a metric on the relevant quotient/domain. Otherwise it retains its weaker declared name.

## 8. Status

`DEFINED / RESEARCH FRAMEWORK`

No claim is made that the candidate invariants are fundamental laws of nature.
