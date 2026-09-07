# Ω-Math v0.9 — Equivalence, Quotient and Information Loss

## 1. Purpose

Ω-Math separates identity, state, observation, behavioral equivalence and quotienting. Equivalence is always relative to an explicitly declared criterion.

## 2. Identity versus state

`e=(id,state)` with `state∈{0,1}`.

Distinct identities may have equal states:

`e₁≠e₂` while `state(e₁)=state(e₂)`.

Equality of state is therefore not identity.

## 3. Observation equivalence

For a well-defined observation map `O`, define

`x≈_O y ⇔ O(x)=O(y)`.

Because equality is reflexive, symmetric and transitive, `≈_O` is an equivalence relation.

Its classes and quotient map are

`[x]_O={y:x≈_O y}`

and

`Q_O(x)=[x]_O`.

## 4. Behavioral equivalence

Current observational equality is not sufficient for dynamic behavior.

For a declared deterministic dynamics, observation criterion, admissible input/intervention class and finite horizon `h`, define `x≈ₕy` when the selected future observations agree through `h`.

Infinite-horizon equivalence is derived by

`x≈∞y ⇔ ∀h∈ℕ₀, x≈ₕy`.

This is related to established behavioral-equivalence/bisimulation ideas; Ω-Math does not claim those concepts as novel.

## 5. Nondeterministic systems

For

`N:S×U→𝒫(S)`,

the successor set is retained. Equivalence must declare what is preserved: traces, branching structure, existential reachability, universal safety or another task predicate.

Arbitrary branch selection is not a universal equivalence rule.

## 6. Reduction and quotient sufficiency

A reduction `Q` preserves a task `F` when

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

Equivalently, `F` is constant on the fibers of `Q` and therefore factors through `Q` on its image.

If a witness satisfies

`x≠y`, `Q(x)=Q(y)`, `F(x)≠F(y)`,

then the reduction loses information for that task.

## 7. Structural quotienting

Quotienting entities may merge paths, relations or structural distinctions. Such effects must be evaluated explicitly; they are not automatically physical changes.

`representation collapse ≠ underlying structural change`.

## 8. Path and summary distinctions

A scalar summary such as

`Σ(P)=∏ sign(r_i)`

does not define path equivalence. Equal summaries do not imply equal paths or equal behavior.

## 9. Physical boundary

No quotient operation in this document is identified with gravity, spacetime, black holes or any other physical phenomenon. A physical interpretation requires an independent mapping to observables, controls and predictions not used to construct the mapping.

## 10. Status

`CANONICAL v0.9 / DEFINED + DERIVED / TASK-RELATIVE`

Historical `EQUIVALENCE.md` remains preserved as a research record. This file is the current v0.9 equivalence specification.
