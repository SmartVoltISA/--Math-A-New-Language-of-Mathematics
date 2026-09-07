# Ω-Math — Path Algebra v0.2

## Purpose

Existing experiments show that counts, degree sequences and cycle rank can be matched while path organization and dynamic response differ. Path structure therefore needs an explicit object rather than an arithmetic proxy.

## 1. Path

A path is an ordered sequence

`P = (e₀,r₀₁,e₁,...,rₙ₋₁ₙ,eₙ)`

such that each relation is present in the relation domain and its target matches the next entity.

A path has at least one relation unless a zero-length path convention is explicitly introduced.

## 2. Path composition

If

`P₁ : e₀ ⇝ e_k`

and

`P₂ : e_k ⇝ e_n`,

then their concatenation is

`P₂ ∘ P₁ : e₀ ⇝ e_n`.

The shared endpoint is identified once.

This is sequence concatenation, not arithmetic addition of relation signs.

## 3. Elementary relation composition

For relations

`r_ab : a→b`

and

`r_bc : b→c`,

the composite path

`r_bc ∘ r_ab`

is always a valid length-2 path when both relations exist.

Whether this path can itself be represented as a primitive relation `r_ac` is **OPEN**.

Therefore Ω-Math currently distinguishes:

`path composition`

from

`relation composition`.

## 4. Signs

For a path, the sequence of relation signs is retained:

`σ(P)=(σ₀,...,σₙ₋₁)`.

Possible path-sign summaries are experimental derived observables, not primitive operations.

Candidate summaries include:

- sign sequence;
- parity of negative relations;
- product of signs;
- signed path class.

No one summary is selected as the Ω relation-composition law without testing.

## 5. Path equivalence

A path equivalence relation must specify what is ignored.

Examples:

- endpoint equivalence;
- same entity sequence;
- same relation-sign sequence;
- observational equivalence of visited entities;
- behavioral equivalence under a transition model.

Thus:

`P₁ ≈ P₂`

has no meaning until the equivalence criterion is declared.

## 6. Path profile

For a selected source `s`, define a path profile as a declared collection of path observables from `s`, for example:

`PP(Ω,s) = {reachable endpoints, path lengths, multiplicities, sign patterns, cycle participation}`.

This is a candidate structural descriptor, not yet a sufficient statistic.

The next counterexample test is:

`PP(Ω₁,s)=PP(Ω₂,s)`

while a controlled transition produces different observations.

If such a pair exists, path profile alone is insufficient for that dynamics.

## 7. Cycles

A cycle is a path satisfying a declared return criterion.

A cycle does not automatically imply feedback or causality.

Feedback requires a recurrence in the transition/dynamical semantics; causality requires an appropriate intervention criterion.

## 8. Redundancy

Multiple distinct paths between the same endpoints are a structural property. They must not be collapsed into one relation unless the quotient explicitly declares that operation.

This follows directly from prior collapse experiments: vertex quotienting and relation quotienting are separate choices.

## 9. Associativity test

Path concatenation is associative whenever concatenations are defined:

`(P₃ ∘ P₂) ∘ P₁ = P₃ ∘ (P₂ ∘ P₁)`.

The test target is different: determine whether a proposed **relation-level** composition `⊙` can satisfy associativity while preserving path distinctions relevant to behavior.

## 10. Required experiments

1. Enumerate all length-2 signed compositions.
2. Test candidate relation-level reductions against path semantics.
3. Test length-3 and length-4 associativity.
4. Search for conflicting parallel paths.
5. Test sign-preserving versus sign-collapsing quotients.
6. Test whether path profiles predict controlled propagation.
7. Compare path descriptors against standard graph invariants.

## 11. Status

`DEFINED: path object and concatenation`

`OPEN: primitive relation composition`

`OPEN: sufficient path profile`

`OPEN: canonical path equivalence`
