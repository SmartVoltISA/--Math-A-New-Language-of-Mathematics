# Ω-Math v0.9 — Semantic Rules

## 1. Typed meaning

A symbol has meaning only together with its declared type and position.

`0:EntityState` and `0:RelationState` are different typed objects; in the minimal language `0:RelationState` is not admitted. Entity states are `{0,1}` and relation states are `{−1,+1}`.

Relation absence is domain absence, not a third relation value.

## 2. Identity and state

Entity identity is represented separately from entity state.

`(i,0) ≠ (j,0)` when `i ≠ j`.

Equal state does not imply equal entity.

A system state may contain configuration plus explicitly retained variables such as memory or control state.

## 3. Relation semantics

A relation is an ordered directed connection whose primitive state belongs to `{−1,+1}`. The signs have no intrinsic interpretation as attraction, repulsion, causation, force, truth or energy.

## 4. Direction and reversal

A directed relation retains source and target order. Reversal is a sequence transformation unless reverse edges are independently present or an explicit symmetry identifies the directions.

`rev(P)` does not imply `rev(r)` exists as a relation.

## 5. Relation domain and absence

If `(i,j) ∉ D_R`, the relation is absent/undefined in the declared relational domain. It is not silently represented by another relation state.

## 6. Paths

A path preserves:

- endpoint order;
- intermediate entities;
- relation order;
- relation states;
- path length;
- multiplicity when multiple paths exist.

Exact path equality is sequence equality. A scalar path summary is a declared reduction and is not automatically behavior-preserving.

## 7. Change and transformation

Change is a declared comparison between states/configurations. It is not ordinary subtraction unless an external arithmetic model explicitly says so.

A transformation must declare its domain, action and output. Invertibility is a property to prove or test, not a default assumption.

## 8. Observation

An observation intentionally retains selected information and may erase distinctions.

`O(x)=O(y)` establishes observational equivalence under `O`, not identity or universal behavioral equivalence.

## 9. Equivalence and behavior

An equivalence must specify the task, observation, transition semantics, input/intervention class and horizon where relevant.

For finite deterministic systems, finite-horizon behavioral equivalence may be defined recursively and verified against direct exhaustive comparison. Increasing the horizon can split classes but cannot merge them.

Infinite-horizon equivalence is derived as:

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

For nondeterministic systems, successor sets remain first-class and equivalence is task-relative: trace/output, branching-sensitive, existential reachability, universal safety, or another explicit predicate.

## 10. Quotients and reduction

A quotient identifies objects under a declared equivalence and must specify how retained structure maps to quotient structure.

A reduction is behavior-preserving only when the retained representation is sufficient for the declared task:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

This implication is a criterion to verify, not an automatic property of compact summaries.

## 11. Invariants and geometry

An invariant is always relative to a declared transformation family:

`I(T(x))=I(x)`.

Distance and geometry are not primitive. A candidate metric requires a declared transformation family and cost, followed by verification of metric axioms on the stated domain.

For quotient geometry, the infimum construction is only a candidate in general; triangle inequality and separation require explicit compatibility/conditions or finite verification.

## 12. Time, probability and causality

Transition order is distinct from physical duration. Physical time requires an independent empirical bridge.

Probability requires an independently declared kernel such as `K:S×U→Dist(S)`.

Temporal succession is not causality. Causal claims require explicit intervention/counterfactual semantics.

## 13. Memory, feedback and emergence

Persistent storage is not automatically functional memory. Memory requires persistence plus demonstrated later functional influence.

A graph cycle is not automatically causal feedback.

Emergence requires explicit coarse-graining/identification, a macro-property or behavior, persistence/prediction criteria, and controls.

## 14. Semantic priority

When intuition, analogy or ordinary arithmetic conflicts with a typed Ω definition, the explicit typed definition controls.

`description ≠ explanation`

`model ≠ reality`

`correlation ≠ causation`.

## Status

`CANONICAL / v0.9 SYNCHRONIZED`
