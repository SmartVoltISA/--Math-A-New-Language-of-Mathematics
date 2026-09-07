# Ω-Math v0.9 — Frontier Closure

This document closes the remaining language-design frontiers without claiming to solve physical science.

## Relation composition
Primitive relation composition is not required. Relations remain atomic directed typed edges. Composition is path formation:

`r₁ ⧺ r₂ ⧺ ... ⧺ rₙ = P`.

A collapse `A(P)→Relation` is allowed only as an explicitly declared abstraction. No unique collapse follows from the core. `REL_COMPOSE` therefore remains non-primitive.

## Path equality
Exact path equality is admitted:

`P = Q ⇔ |P|=|Q| ∧ ∀i, rᵢ=qᵢ`.

This is representation identity, not structural, behavioral, homotopy or sign equivalence. `PATH_EQ` is therefore admitted at the exact-sequence level.

## Path identity and reversal
The empty path `ε_e` is the identity of path concatenation:

`ε_e⧺P=P`, `P⧺ε_e=P`.

This does not introduce a primitive relation identity. A path may be reversed as a sequence, `rev(P)`, but reversed edges are not assumed to exist. `REL_ID` and `REL_INV` remain non-primitive.

## Infinite horizon
Define:

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

Hence `≈∞ = ⋂ₕ≈ₕ`. Infinite-horizon equivalence is derived from finite-horizon semantics; it is not a new primitive.

## Nondeterminism
The successor set remains first-class:

`N:S×U→𝒫(S)`.

Equivalence is parameterized by task semantics: trace/output, branching-sensitive, existential reachability, universal safety, or another explicitly declared predicate. Arbitrary branch collapse is forbidden.

## Infinite runs
A run is an infinite state sequence consistent with `N`. Fairness and liveness are predicates over such runs. They are semantic modules, not hidden assumptions of equivalence.

## Quotient geometry
For an equivalence `~` and structural distance `d`:

`d_Q([x],[y])=inf{d(x',y'):x'~x,y'~y}`.

This is a quotient pseudodistance. It is a metric only under explicit separation conditions. Unequal-cardinality correspondence requires an explicitly declared edit/correspondence family.

## Continuous states
The state set may be any explicitly declared set `S`. Finite models are the current verification domain. Topology, measure, norm or differentiable structure must be declared externally; none is silently derived from the four primitive values.

## Probability
Probability is not derivable from the primitive typed values alone. A probabilistic kernel must be independently declared, e.g. `K:S×U→Dist(S)`. `PROB` remains outside the minimal core.

## Causal intervention
Causal claims require explicit intervention semantics. A declared intervention family may be represented as `I:S×A→S`. Temporal succession is not causal proof. `CAUSE` remains a semantic module.

## Physical time and energy
Internal order is `τ(Sₖ)=k`. Physical duration requires an independent empirical map from histories to physical time. Transformation cost is not physical energy unless independently calibrated. `TIME_PHYSICAL` and `ENERGY` remain empirical bridges.

## Emergence and physical ontology
Emergence is operationally testable through explicit coarse-graining, macro-property, persistence/prediction criterion and controls. A universal task-independent emergence theorem is not derived. The formal system also does not establish that its structures are the ontology of nature.

## Final classification

| Frontier | Classification |
|---|---|
| Primitive relation composition | NON-PRIMITIVE / REJECTED AS NECESSARY |
| Exact path equality | DERIVED / ADMITTED |
| Rich path equivalence | TASK-RELATIVE |
| Path identity | DERIVED |
| Relation inverse | NON-PRIMITIVE |
| Infinite-horizon equivalence | DERIVED |
| Nondeterministic branching | ADMITTED |
| Fairness/liveness | SEMANTIC MODULE |
| Quotient geometry | DERIVED WITH CONDITIONS |
| Continuous states | DECLARED EXTENSION |
| Probability | OUTSIDE MINIMAL CORE |
| Causal intervention | SEMANTIC MODULE |
| Physical time | EMPIRICAL BRIDGE |
| Energy | EMPIRICAL BRIDGE |
| Physical ontology | OPEN |
| Universal emergence | OPEN |

## Conclusion

The remaining frontiers no longer block completion of the Ω-Math formal language. They separate into derived constructions, task-selected semantic modules, and external empirical/physical bridges.

`complete language ≠ complete mathematics ≠ complete physics`.
