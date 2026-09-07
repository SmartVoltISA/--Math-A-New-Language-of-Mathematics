# Ω-Experiment PATH-PROFILE-003 — Same Source-Distance Profile, Different Behavior

## Status

`EXECUTED / FORMAL COUNTEREXAMPLE UNDER DECLARED FINITE MODEL`

## 1. Question

Is the shortest-path distance multiset from a source sufficient to determine future behavior under a fixed local transition rule?

Target:

`same source-distance profile + same entity count + same relation count`

but

`different controlled behavior`.

## 2. Construction

Use four entities, all initially in state `1`.

All structural adjacencies are represented by opposite `+1` Ω-relations.

### ΩP₃-A

Edges:

`A-D, B-C, B-D, C-D`

Choose source `B`.

Degrees:

`deg(A)=1, deg(B)=2, deg(C)=2, deg(D)=3`.

### ΩP₃-B

Edges:

`A-B, A-D, B-C, C-D`

Choose source `A`.

Degrees:

`deg(A)=2, deg(B)=2, deg(C)=2, deg(D)=2`.

The two graphs have:

- 4 entities;
- 4 structural edges;
- one connected component;
- identical all-`+1` relation signs;
- identical source-distance multiset:

`{0,1,1,2}`.

They are **not isomorphic** because ΩP₃-A has degree sequence `(3,2,2,1)` while ΩP₃-B has `(2,2,2,2)`.

Thus the difference cannot be removed by relabeling.

## 3. Transition rule

The same deterministic rule is applied to both systems.

At `t=0`, only the selected source is changed to `0`.

At each subsequent step:

> An entity changes from `1` to `0` at time `t+1` iff at least two of its neighboring entities were `0` at time `t`.

A `0` state persists.

This is a declared local threshold dynamics; it is not asserted to be a physical law.

## 4. Execution

### ΩP₃-A

`t0: B=0; A=C=D=1`

`t1: B=0; A=C=1; D=1`

Only `D` has a zero-valued neighbor (`B`), so no second threshold is reached.

`t2` and later remain unchanged.

Final changed set:

`{B}`.

### ΩP₃-B

`t0: A=0; B=C=D=1`

`t1: A=0; B=C=D=1`

Again, each neighbor has only one zero-valued neighbor.

`t2: C=0`

because `C` has two zero-valued neighbors `B` and `D`? **Correction:** under the stated synchronous rule, `B` and `D` are not zero at `t1`, so this does not occur.

Therefore this particular threshold rule does **not** distinguish the pair and is rejected as a failed dynamic witness.

## 5. Revised transition rule search

The pair remains valid as a structural counterexample to distance-profile completeness, but a dynamic witness requires a rule sensitive to a structural feature not encoded by source-distance multiset.

A valid next rule should be selected before execution and then tested identically on both graphs. Candidate controls include:

- degree-sensitive threshold;
- triangle-sensitive propagation;
- two-path redundancy rule;
- cycle-dependent transition.

No positive dynamic result is claimed until such a rule is explicitly executed.

## 6. What IS established

The two systems prove the purely structural statement:

`same source-distance profile ≠ same graph structure`.

The source-distance profile `{0,1,1,2}` does not encode the degree organization or cycle structure.

## 7. Decision

`PATH-PROFILE-003` is a **structural counterexample**, not yet a behavioral counterexample.

This distinction is intentional: the failed transition attempt is recorded rather than silently discarded.

## 8. Next test

Search exhaustively over small local transition rules whose inputs are neighborhood states and a bounded structural feature, and find the smallest rule for which the non-isomorphic pair has different future observations.

The rule must be fixed before comparing the two systems.

Core requirement:

`same representation summary + same transition rule → different trajectory`.
