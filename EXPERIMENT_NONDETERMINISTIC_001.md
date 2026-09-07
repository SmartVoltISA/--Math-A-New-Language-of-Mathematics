# Ω-Experiment NONDETERMINISTIC-001 — Branching Cannot Be Silently Collapsed

## Question

Does replacing a nondeterministic successor set by a single selected successor preserve behavior in general?

## Model

States:

`S={A,B,A0,A1,B0,B1}`

Single input `u`.

Observation:

`O(A)=O(B)=1`

`O(A0)=O(B0)=0`

`O(A1)=O(B1)=1`.

Transitions:

`N(A,u)={A0,A1}`

`N(B,u)={B0,B1}`.

At horizon one, the observable successor sets are equal: `{0,1}`.

Extend with input `v`:

`N(A1,v)={A0}`

`N(B1,v)=∅`.

Thus at horizon two the future branching behavior differs.

## Control

Define the full branching observation tree rather than selecting one successor.

At depth one both systems produce:

`1 → {0,1}`.

At depth two:

`A → {0,1} → A1 can continue under v`

`B → {0,1} → B1 is blocked under v`.

Therefore a task that observes whether `v` remains executable distinguishes the systems.

## Result

A one-step successor observation set is insufficient for a two-step task.

A deterministic selection rule such as choosing `A0` or `A1` would remove a branch and change the modeled behavior unless the selection rule is explicitly part of the system.

Therefore:

`nondeterministic state → single successor`

is not a semantics-preserving reduction in general.

## Consequence

The Ω reduction rule applies to branching systems exactly as to deterministic systems:

`Q(x)=Q(y) ⇒ B(x)=B(y)`

must be evaluated using the declared branching semantics.

Different tasks may require different preservation strength:

- full future-tree preservation;
- existential reachability;
- universal safety;
- another explicitly declared predicate.

## Status

**EXECUTED / SUPPORTED under the finite declared model.**

The experiment establishes only the stated counterexample. It does not define a universal nondeterministic theory or probability.
