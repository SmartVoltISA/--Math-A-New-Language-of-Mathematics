# Ω-Math v0.9 — Reduction and Information-Preservation Rules

A reduction `Q:X→Y` is safe only relative to a declared task, behavior or observation `F` when:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

This is equivalent to requiring the task to factor through the reduction: `F=F̄∘Q`.

## Core rules

1. Entity identity, state, relation presence and relation value remain distinct.
2. Paths are not silently replaced by scalar summaries.
3. Aggregate graph statistics are not complete structural descriptions without a sufficiency proof.
4. Observation equality does not imply identity or future behavioral equivalence.
5. A quotient is valid only for the declared task/behavior it preserves.
6. A witness `x≠y`, `Q(x)=Q(y)`, `F(x)≠F(y)` proves information loss for that task.
7. Promotion from summary to equivalence-preserving requires declared task, counterexample search and proof or exhaustive verification on the stated domain.

## Path reduction

`Σ(P)=∏ sign(r)` is a closed derived sign summary. It is not a universal information-preserving replacement for the ordered path object. Existing counterexamples demonstrate loss of intermediate organization and path multiplicity.

## Behavioral quotient

For finite horizon `h`, a quotient is behavior-preserving when equivalent representatives have identical declared observations under the declared dynamics and admissible inputs/interventions through horizon `h`. Infinite-horizon equivalence is derived by:

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

For nondeterministic systems, the task semantics must specify whether traces, branching structure, existential reachability, universal safety, or another predicate is preserved. Arbitrary branch collapse is forbidden.

## Quotient geometry

A quotient-induced distance is not automatically a pseudometric for an arbitrary equivalence relation. The candidate

`d_Q([x],[y])=inf{d(x',y'):x'~x,y'~y}`

requires explicit compatibility conditions before pseudometric/metric status is claimed. See `QUOTIENT_GEOMETRY_CONDITIONS.md`.

## Principle

**Never confuse compression with equivalence.**

`smaller description ≠ same object`

`same measurement ≠ same structure`

`same structure summary ≠ same behavior`

`quotient ≠ destruction`

## Status

`DEFINED / CORE METHODOLOGICAL RULE / v0.9 SYNCHRONIZED`
