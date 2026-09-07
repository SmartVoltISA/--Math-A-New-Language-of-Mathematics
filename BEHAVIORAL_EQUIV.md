# Ω-Math v0.9 — Behavioral Equivalence

## Purpose

Static observational equivalence is insufficient for dynamic systems. Behavioral equivalence is a derived, task- and dynamics-relative construction; it is not a primitive.

## Finite horizon

For deterministic dynamics with observation map `O`, admissible inputs/interventions and horizon `h`, define `s≈ₕs'` when the declared observation trajectories agree through the chosen horizon under the declared semantics.

A canonical quotient is then the set of equivalence classes `[s]_h` induced by `≈ₕ`.

The relation is task-relative: changing the observation, dynamics, admissible inputs or horizon can change the equivalence classes.

## Infinite horizon

Define:

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

Therefore:

`≈∞ = ⋂ₕ≈ₕ`.

Infinite-horizon equivalence is derived from the finite-horizon family rather than introduced as a new primitive.

## Nondeterminism

For `N:S×U→𝒫(S)`, immediate successor sets are first-class. A behavioral equivalence must declare what is preserved: traces/outputs, full branching structure, existential reachability, universal safety, or another task predicate. No arbitrary branch selection is valid as a universal reduction.

Infinite-run fairness and liveness are explicit semantic predicates and are not silently built into equivalence.

## Static counterexample

Two entities can have equal current observation while their transition rules produce different future observations. Hence:

`same now ≠ same behavior`.

This remains a foundational counterexample against observation-only quotienting.

## Relation to established mathematics

The construction is closely related to established behavioral equivalence and bisimulation ideas. Ω-Math makes the task, horizon and retained semantics explicit and does not claim those general concepts as novel.

## Status

- static observational equivalence versus behavior — **FORMALLY DISTINGUISHED**;
- finite-horizon behavioral equivalence — **DEFINED / VERIFIED ON DECLARED FINITE MODELS**;
- infinite-horizon equivalence — **DERIVED**;
- nondeterministic equivalence — **TASK-SEMANTIC MODULE**;
- probabilistic equivalence — **OUTSIDE MINIMAL CORE**.

**Status: v0.9 SYNCHRONIZED**
