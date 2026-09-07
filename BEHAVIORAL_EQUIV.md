# Ω-Math v0.1 — Behavioral Equivalence

## 1. Purpose

Static observational equivalence is insufficient for a dynamic system. Two entities can have the same current observation and nevertheless have different future behavior.

This document defines a candidate behavioral equivalence layer without making it primitive.

Core distinction:

`same now ≠ same behavior`

## 2. Dynamic entity

Let an entity be represented by:

`e=(i,s)`

with identity `i` and current state `s`.

A transition rule produces a successor:

`T(e,u) → e'`

where `u` is optional input.

An observation map is:

`O(e) = observed state/data`.

## 3. Static observational equivalence

For a fixed observation map:

`e₁ ≈ₒ e₂  iff  O(e₁)=O(e₂)`.

This relation describes indistinguishability at one observation instant.

It says nothing by itself about future transitions.

## 4. Behavioral equivalence candidate

For a deterministic transition system, define a candidate relation `≈ᵦ` such that:

`e₁ ≈ᵦ e₂`

only when:

1. `O(e₁)=O(e₂)`;
2. corresponding transitions preserve equivalence;
3. recursively, future observations remain indistinguishable under the same admissible inputs.

For a transition function this can be expressed schematically as:

`e₁≈ᵦe₂ ⇒ O(T(e₁,u))=O(T(e₂,u))`

and:

`e₁≈ᵦe₂ ⇒ T(e₁,u)≈ᵦT(e₂,u)`.

The exact definition depends on whether the system is deterministic, nondeterministic, finite-horizon or infinite-horizon.

## 5. Minimal counterexample

Take two entities with equal current state:

`A=(1,1)`
`B=(2,1)`

and observation:

`O(A)=O(B)=1`.

Thus:

`A≈ₒB`.

Define different transitions:

`T(A)=A`

`T(B)=(2,0)`.

At the next step:

`O(T(A))=1`

`O(T(B))=0`.

Therefore:

`A≈ₒB`

but:

`A ≉ᵦ B`.

This is a formal counterexample to the claim that current observational equivalence is sufficient to establish behavioral equivalence.

## 6. Why this matters for Ω-Math

A quotient based only on current observation can merge entities whose future behavior is different.

Therefore:

`Qₒ` may be valid for a static description while being invalid for a dynamic description.

A dynamic quotient must preserve whatever behavior the model declares relevant.

This gives a stronger requirement:

`valid dynamic quotient = distinction loss without loss of relevant future behavior`.

## 7. Relation to path structure

A path contains a sequence of states and relations:

`P=(e₀,r₁,e₁,...,rₖ,eₖ)`.

Behavioral equivalence can be extended from entities to paths by requiring corresponding observations and transitions to remain equivalent.

However, path equality and behavioral equivalence must remain separate:

`P₁=P₂`

is stronger than:

`P₁≈ᵦP₂`.

Two different paths can implement the same observable behavior.

## 8. Static versus behavioral collapse

There are now at least two distinct collapse modes:

### Static observational collapse

Different entities map to one observation class at the current instant.

`e₁≠e₂` and `Qₒ(e₁)=Qₒ(e₂)`.

### Behavioral collapse

Different entities are equivalent with respect to the complete behavior selected by the model.

`e₁≠e₂` and `e₁≈ᵦe₂`.

Behavioral collapse is therefore stronger than static observational collapse.

But neither means physical disappearance of the underlying entities.

## 9. Relation to standard mathematics

This construction is closely related to established behavioral-equivalence ideas, including bisimulation for transition systems and quotient constructions that preserve selected behavior.

Ω-Math does not claim these ideas are new. The research question is whether the required behavioral equivalence can be derived from the existing Ω primitives and what minimum structure must be added.

## 10. Important limitation

For nondeterministic systems, the simple successor equation above is insufficient. One must specify whether equivalence preserves:

- every possible future;
- at least one matching future;
- probability distributions over futures;
- finite-horizon observations;
- infinite-horizon behavior.

These are different mathematical requirements.

Therefore no universal `≈ᵦ` is declared yet.

## 11. Current status

### DERIVED / FORMALLY SHOWN

- static observational equivalence does not imply behavioral equivalence;
- a dynamic quotient can erase distinctions that become observable later;
- behavioral equivalence must reference transition structure, not only current state.

### OPEN

- canonical behavioral equivalence for Ω systems;
- nondeterministic version;
- path-level behavioral equivalence;
- minimal conditions for quotient preservation;
- relation to memory and history.

## 12. Next experiment

Hold the observation map fixed and construct pairs of systems with:

`same current observation`

but:

`different transition structure`.

Measure the first time horizon at which their observations diverge.

This produces a concrete test for the boundary between static indistinguishability and behavioral distinguishability.
