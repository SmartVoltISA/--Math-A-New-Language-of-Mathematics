# Ω-Math v0.9 — Foundation

## Purpose

Ω-Math starts from a minimal typed vocabulary separating an entity from its state, a relation from its state, and relation presence from relation value.

## Primitive typed domains

`EntityState = {0,1}`

`RelationState = {−1,+1}`

These are disjoint typed domains. The symbols have no intrinsic physical meaning.

## Entity

`e=(id,state)`, with `state∈EntityState`.

Entity identity is distinct from entity state.

## Relation

`r=(src,dst,sign)`, with `sign∈RelationState` and `(src,dst)∈D_R`.

Relations are directed typed edges. Relation absence is a domain condition, not a third relation value.

## Configuration

`C=(E,D_R,R)` where `E` is the entity set, `D_R` is the explicit domain of present relations, and `R:D_R→RelationState` assigns relation states.

## State

`S=(C,M,X)` where retained variables are explicit. Nothing may be added to state implicitly.

## Transition and change

A transition is a declared mapping `T:S×U→S'`. Change is represented by `COMPARE(S,S')→ChangeRecord`; numerical magnitude requires a separate derived definition.

## Paths

A path is an ordered compatible sequence `P=(r₁,...,rₙ)`. Path concatenation `P⧺Q` is the primary sequential composition operation and is associative. Exact path equality is sequence identity. The empty path `ε_e` is the identity for compatible path concatenation.

Primitive relation-to-relation collapse, primitive relation identity and primitive relation inverse are not required by the foundation.

## Higher-level entities

A stable substructure may be mapped to a higher-level entity only through an explicit coarse-graining/identification map and validation criterion.

## Minimal principles

**P1 — Typed distinction.** Entity and relation states are different types.

**P2 — Relation requires a domain.** Presence is separate from sign.

**P3 — Structure is relational.** Entity-state multisets alone do not determine relational organization.

**P4 — Change is comparison.** No primitive subtraction is assumed.

**P5 — Paths retain order.** A path is not silently replaced by a scalar.

**P6 — Reduction requires sufficiency.** A compressed representation is not equivalent unless it preserves the declared task/behavior.

**P7 — Emergence requires identification.** A macro-object needs an explicit map and validation criterion.

**P8 — Completion requires final verification.** Work is not `DONE` until the written artifact has been reread and checked, dependent records have been synchronized, and the result is self-contained. See `WORK_COMPLETION_STANDARD_v1.0.md`.

## Scope

The foundation is the minimal typed relational base. Higher layers are defined and tested separately. v0.9 language closure does not claim universal mathematical completeness or a physical ontology.

Process completion is governed by `WORK_COMPLETION_STANDARD_v1.0.md` and does not add a mathematical primitive.

**Status: DEFINED / FOUNDATION / v0.9 SYNCHRONIZED**
