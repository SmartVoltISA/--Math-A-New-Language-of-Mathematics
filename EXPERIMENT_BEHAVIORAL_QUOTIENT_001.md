# Ω-Experiment BEHAVIORAL-QUOTIENT-001 — Exhaustive Finite Verification

## Status

`EXECUTED / SUPPORTED UNDER DECLARED FINITE DETERMINISTIC MODEL`

## 1. Question

Does the finite-horizon behavioral quotient construction agree with direct exhaustive comparison, satisfy horizon nesting, and produce the coarsest task-sufficient partition in small deterministic systems?

## 2. Model

Use a finite state set `S={0,...,n-1}`, a finite input set `U={0,...,m-1}`, a deterministic transition table

`T:S×U→S`,

and a finite observation map

`O:S→Y`.

For a horizon `h` and an input sequence `u⃗=(u₀,...,u_{h−1})∈U^h`, define the observed trajectory

`B_h(s,u⃗)=(O(s), O(T(s,u₀)), O(T(T(s,u₀),u₁)), ..., O(T^{u⃗}(s)))`.

Here `T^{u⃗}(s)` denotes the state reached by applying the input sequence in order. For `h=0`, `B_0(s,())=(O(s))`.

Define direct behavioral equivalence:

`s≈_h s'` iff for every input sequence `u⃗∈U^h`,

`B_h(s,u⃗)=B_h(s',u⃗)`.

Define the recursive signature:

`Q_0(s)=O(s)`

`Q_{h+1}(s)=(O(s), {(u,Q_h(T(s,u))):u∈U})`.

Two states are recursively equivalent when their signatures are equal.

## 3. Exhaustive verification

The implementation enumerates finite deterministic transition systems for small `n,m`, together with binary observations, and compares:

1. direct trajectory equivalence;
2. recursive-signature equivalence;
3. all set partitions of the state space to test coarseness.

For every enumerated model:

`direct_equivalence_h = recursive_equivalence_h`.

No discrepancy was found.

## 4. Horizon nesting

For every tested model and every tested horizon:

`≈_{h+1} ⊆ ≈_h`.

No pair was found that became equivalent after increasing the horizon.

Thus increasing the horizon can split behavioral classes but cannot merge them.

## 5. Coarseness

For every tested model, the behavioral partition was compared with every partition of `S` that preserved the complete declared horizon-`h` behavior.

No strictly coarser task-sufficient partition than the behavioral quotient was found.

Therefore the quotient is coarsest among finite partitions preserving the declared deterministic finite-horizon observation behavior.

## 6. Interpretation

The result supports three separate statements under the declared finite model:

- the recursive construction computes the same equivalence as exhaustive behavior comparison;
- finite-horizon equivalence is nested by horizon;
- the resulting quotient is the coarsest behavior-preserving partition.

These are mathematical results about the declared finite deterministic transition model.

## 7. Relation to Ω-Math

The test validates the proposed stopping rule for reduction:

`Q(s)=Q(s') ⇒ B_h(s,u⃗)=B_h(s',u⃗)` for every declared input sequence `u⃗`.

A structural descriptor is not promoted merely because it is compact or descriptive. It must pass the behavioral sufficiency test for the declared task.

This connects the existing reduction rule with an executable quotient construction.

## 8. Limits

This experiment does not establish novelty relative to bisimulation, DFA minimization, partition refinement or related transition-system theory.

It does not cover nondeterministic transitions, probabilistic transitions, infinite state spaces, continuous observations, or causal/interventional semantics.

## 9. Decision

`SUPPORTED`: recursive finite-horizon behavioral quotient under the declared deterministic finite model.

`OPEN`: comparison with established theory and extension beyond deterministic finite systems.

No global novelty claim is made.
