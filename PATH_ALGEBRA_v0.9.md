# Ω-Math v0.9 — Path Algebra

## 1. Path

A path is an ordered compatible sequence

`P=(r₁,...,rₙ)`.

The zero-length path at entity `e`, written `ε_e`, is admitted in v0.9 and is the identity for compatible path concatenation.

## 2. Concatenation

For compatible paths,

`P⧺Q`

is ordered sequence concatenation. It is associative:

`(P⧺Q)⧺R=P⧺(Q⧺R)`.

The empty path satisfies

`ε_e⧺P=P` and `P⧺ε_e=P`

whenever the endpoint types are compatible.

This is path-level identity, not primitive relation identity.

## 3. Exact equality

`P=Q ⇔ |P|=|Q| ∧ ∀i, r_i=q_i`.

This is representation identity only. It is not behavioral, structural, homotopy or sign equivalence.

## 4. Relation-level composition

Sequential composition is retained as a path. A primitive operation

`REL_COMPOSE: RelationState×RelationState→RelationState`

is not required by the minimal language.

A path may be collapsed to a single relation only by an explicitly declared derived abstraction.

## 5. Sign summaries

For a non-empty path,

`Σ(P)=∏ᵢ sign(rᵢ)`.

This is a closed derived summary on `{−1,+1}`. It does not preserve path order, length, intermediate entities, parallel alternatives or conflicts.

Therefore:

`equal sign summary ≠ equal path`.

## 6. Reversal

`rev(P)` reverses the stored sequence. It does not imply that reverse directed relations exist. `REL_INV` is therefore non-primitive.

## 7. Cycles

A cycle is a path satisfying an explicitly declared return criterion. A cycle does not imply feedback or causality. Feedback requires a recurrence in declared dynamics; causality requires intervention semantics.

## 8. Path profiles

A path profile is a declared collection of path observables. It is not automatically a sufficient statistic. `EXPERIMENT_PATH_PROFILE_004.md` gives a finite counterexample showing that a restricted source-distance profile can fail to preserve future behavior.

## 9. Status

`CANONICAL v0.9 / PATH LAYER`

Historical `PATH_ALGEBRA.md` remains preserved as a research record. This file is the current v0.9 path-algebra specification.
