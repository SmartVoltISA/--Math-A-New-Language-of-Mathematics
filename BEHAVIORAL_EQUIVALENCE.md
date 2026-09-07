# Ω-Math — Behavioral Equivalence v0.2

## 1. Motivation

The existing constructions show that equal current observations and equal aggregate graph statistics can hide different future behavior. Equivalence must therefore be indexed by what is observed and by the dynamics being preserved.

## 2. Horizon-dependent equivalence

Let `O` be an observation map and `U` an admissible input sequence. Define `≈ᵦ,h` by equality of the selected observations for all tested steps through horizon `h` under the declared input protocol.

At horizon zero:

`x ≈ᵦ,0 y` iff `O(x)=O(y)`.

For deterministic dynamics, a recursive definition is:

`x ≈ᵦ,h+1 y`

iff

`O(x)=O(y)`

and

`T(x,u) ≈ᵦ,h T(y,u)`

for every admissible input `u` in the declared test set.

This is a finite-horizon behavioral criterion, not a universal law for all possible systems.

## 3. Nesting

Under the recursive definition:

`≈ᵦ,h+1 ⊆ ≈ᵦ,h`.

A longer observation horizon can reveal distinctions that a shorter horizon cannot see. It cannot make two already distinguishable objects equivalent under the same observation protocol.

For nondeterministic systems the definition must be replaced by an explicitly chosen matching relation over possible successors or distributions.

## 4. Behavior-preserving quotient

A quotient by an equivalence `≈` is behavior-preserving for a declared transition system only if equivalent states have compatible successor behavior under the declared inputs.

A quotient that merges states with incompatible successors is not behavior-preserving for that task.

## 5. Relation to existing experiments

`BEHAVIORAL-EQUIV-001` provides the minimal counterexample:

`A≈ₒB` now,

but

`T(A)≉ₒT(B)`.

`BEHAVIORAL-EQUIV-002` shows that identical entity-state composition can hide different relational organization and therefore different trajectories under an explicit propagation rule.

`STRUCTURE-004` shows that even matched degree sequence, component count and cycle rank can hide path-level differences that become dynamically observable.

## 6. Behavioral collapse criterion

A collapse is acceptable only relative to a declared preservation target:

`Q : S → S/≈`.

The target must state:

- observation map;
- admissible inputs/interventions;
- time/horizon convention;
- deterministic or nondeterministic semantics;
- behavior that must be preserved.

Without these, the phrase `behavior-preserving collapse` is incomplete.

## 7. Status

`DEFINED: finite-horizon deterministic criterion`.

`SUPPORTED BY CONSTRUCTIONS: static equivalence can fail dynamically`.

`OPEN: canonical infinite-horizon equivalence`.

`OPEN: nondeterministic/probabilistic behavioral equivalence`.
