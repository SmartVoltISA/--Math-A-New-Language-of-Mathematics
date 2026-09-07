# Ω-Math — Nondeterministic Dynamics v0.1

## 1. Purpose

The deterministic transition rule

`T:S×U→S`

assigns one successor. Real or abstract models may instead permit several admissible successors. Ω-Math must not hide that branching by selecting one outcome.

## 2. Nondeterministic transition relation

Define

`N:S×U→𝒫(S)`

where `N(s,u)` is the set of admissible successors.

A transition is therefore

`s —u→ s'` iff `s'∈N(s,u)`.

If `N(s,u)=∅`, the transition is blocked/terminal for that input. This is distinct from a successor state whose observation happens to be empty.

## 3. Reachable behavior tree

For horizon `h`, the behavior of `s` under input sequence `u` is no longer one trajectory. It is a branching observation tree.

Let

`BT_0(s) = O(s)`.

Recursively,

`BT_{h+1}(s,u_0...u_h)`

contains `O(s)` together with the collection of successor behavior trees

`{BT_h(s',u_1...u_h) : s'∈N(s,u_0)}`.

The collection is a set only when successor multiplicity is semantically irrelevant. Otherwise it must be a multiset or another explicitly declared structure.

## 4. Universal and existential behavior

Two different task semantics must not be silently identified.

### Universal preservation

A reduction is sufficient when **all admissible futures** are preserved.

`Q(s)=Q(s') ⇒ BT_h(s,u)=BT_h(s',u)`.

### Existential preservation

A weaker task may ask only whether at least one future satisfies a predicate `P`:

`Reach_h(s,u,P)=true`

iff at least one admissible depth-`h` future satisfies `P`.

A reduction sufficient for existential reachability need not preserve the full future tree.

Therefore:

`universal sufficiency ≠ existential sufficiency`.

## 5. Nondeterministic behavioral equivalence

For a declared behavior semantics `B`, define

`s ≈^B_h s'`

iff their behavior objects are equal under the exact declared comparison rule.

The comparison rule is part of the task. Ω-Math does not introduce one universal nondeterministic equivalence.

## 6. Alternating branching example

Let two states have the same current observation:

`O(A)=O(B)=1`.

For input `u`:

`N(A,u)={A_0,A_1}`

`N(B,u)={B_0,B_1}`.

Suppose their observations are:

`O(A_0)=0, O(A_1)=1`

`O(B_0)=0, O(B_1)=1`.

Under one-step universal observation, they are equivalent if successor multiplicity and identity are not observed.

Now suppose only `A_1` permits a future input `v`, while `B_1` does not. At horizon two, the systems separate.

Thus nondeterministic equivalence must preserve the branching structure required by the declared task, not merely the set of immediate observations.

## 7. Reduction rule

For a candidate reduction `Q`, universal finite-horizon sufficiency is:

`Q(s)=Q(s') ⇒ B_h^N(s,u)=B_h^N(s',u)`

for every admissible input sequence.

For a predicate task `P`, existential sufficiency may instead require:

`Q(s)=Q(s') ⇒ Reach_h(s,u,P)=Reach_h(s',u,P)`.

The second condition is weaker and task-specific.

## 8. Dead ends and terminality

A blocked transition must remain distinguishable from an ordinary state when the task can observe whether another input is executable.

Therefore `N(s,u)=∅` is not silently replaced by `N(s,u)={s}` or by a null observation.

## 9. Relation to probability

Nondeterminism does not assign probabilities.

If two successors are possible, Ω-Math currently says only that both are admissible. Assigning weights

`p(s'|s,u)`

requires a separate probabilistic extension.

Thus:

`possible ≠ probable`.

## 10. Current status

**DEFINED:** nondeterministic transition relation and branching behavior representation.

**DERIVED:** universal finite-horizon sufficiency condition relative to a declared branching behavior object.

**OPEN:** canonical nondeterministic equivalence; probabilistic extension; infinite-horizon semantics; fairness/liveness; intervention semantics.

## 11. Core rule

> When the future branches, the branch set is part of the state-transition semantics. Choosing one branch without a declared rule is an information-changing operation.
