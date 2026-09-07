# Ω-Math — Behavioral Equivalence v0.2

## 1. Purpose

Static observation can hide differences that become visible only after a transition. Ω-Math therefore distinguishes observational equivalence from equivalence of future behavior.

## 2. Finite-horizon behavioral equivalence

Let `O` be an observation map and `T` a deterministic transition rule under a declared input sequence `U₀,U₁,...`.

For horizon `h ≥ 0`, define:

`x ≈ᵦ,h y`

iff the observation sequences generated from `x` and `y` are equal through horizon `h` under the same declared inputs:

`O(T^k(x;U)) = O(T^k(y;U))` for every `0 ≤ k ≤ h`.

For `h=0`, this reduces to current observational equivalence:

`x ≈ᵦ,0 y ⇔ O(x)=O(y)`.

## 3. Horizon nesting

By construction,

`≈ᵦ,h+1 ⊆ ≈ᵦ,h`.

Increasing the observation horizon cannot turn an already distinguishable pair into an equivalent pair. It can only preserve equivalence or reveal a distinction.

This is a formal property of the deterministic finite-horizon definition, not an empirical law.

## 4. Behavioral quotient compatibility

A quotient `Q` is behavior-preserving for horizon `h` only if equivalent representatives generate the same declared observations through that horizon under the specified inputs.

Therefore a quotient based only on current observation may fail to be behavior-preserving.

The executed constructions in `EXPERIMENT_BEHAVIORAL_EQUIV_001.md` and `EXPERIMENT_BEHAVIORAL_EQUIV_002.md` provide minimal examples of this failure.

## 5. Relational systems

For an Ω-system, the state may contain:

- entity states;
- relation organization;
- retained memory;
- other explicitly declared variables.

Two systems with equal entity-state multisets can therefore belong to different behavioral classes when their relation organization differs.

`same composition ≠ same organization ≠ same behavior`.

## 6. Inputs and nondeterminism

The definition above is deterministic and uses a fixed input sequence.

For nondeterministic systems, behavioral equivalence must explicitly choose its semantics, for example:

- equality of all possible future observations;
- existence of matching futures;
- probability-distribution equivalence, if probability is independently introduced.

Ω-Math does not silently choose among these alternatives.

## 7. Relation to memory

A representation is behaviorally sufficient for a specified task and horizon when replacing the full state by that representation preserves the selected future observations.

Thus memory sufficiency is relative to:

`task + observation + transition rule + input class + horizon`.

No universal memory quantity follows from behavioral equivalence alone.

## 8. Path-level consequence

If two paths have the same scalar sign product but different intermediate organization, they are equivalent under that summary only if the selected dynamics cannot distinguish the intermediate organization.

Therefore:

`equal path summary ≠ behavioral equivalence`.

This is the key test connecting `RELATION_COMPOSITION.md`, `PATH_ALGEBRA.md` and the behavioral layer.

## 9. Required tests

1. Verify finite-horizon nesting computationally on exhaustive finite transition systems.
2. Find minimal systems where `≈ᵦ,h` holds but `≈ᵦ,h+1` fails.
3. Test path pairs with equal sign products and different ordered signs.
4. Test topology pairs with equal aggregate graph statistics.
5. Test which quotients preserve a declared observation/transition family.

## 10. Status

`DEFINED / TESTABLE`

Finite-horizon behavioral equivalence is a definition. Its usefulness and sufficiency for particular Ω models remain empirical/formal questions.
