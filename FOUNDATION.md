# Ω-Math v0.4 — Foundation

## 1. Purpose

Ω-Math starts from a minimal typed vocabulary separating:

1. an entity from its state;
2. a relation from its state;
3. relation presence from relation value.

The primitive alphabet is:

`{0, 1, −1, +1}`

but it contains two disjoint typed value domains.

## 2. Entity domain

`EntityState = {0,1}`.

An entity is:

`eᵢ=(idᵢ,sᵢ)` with `sᵢ∈EntityState`.

The symbols do not intrinsically mean physical absence/presence.

## 3. Relation domain

`RelationState = {−1,+1}`.

A relation is:

`rᵢⱼ=(i,j,q)` with `q∈RelationState` and `(i,j)∈D_R`.

The signs have no intrinsic physical meaning. Attraction, opposition, support, inhibition or causation are application-level interpretations and require independent definitions.

## 4. Type separation

`0:EntityState`

`1:EntityState`

`−1:RelationState`

`+1:RelationState`

Therefore equal-looking numerical symbols are not interchangeable across types.

## 5. Distinction

For entity states:

`D(a,b)=0` if `a=b`;

`D(a,b)=1` if `a≠b`.

This is a declared comparison operator, not ordinary addition.

## 6. Relation domain and absence

`D_R ⊆ I×I` is the explicit domain of present/modelled relations.

If `(i,j)∉D_R`, the relation is absent/undefined in the model. It is not automatically `0`, `−1` or `+1`.

## 7. Elementary Ω expression

`eᵢ —q→ eⱼ`

with `q∈{−1,+1}`.

## 8. Configuration

`C=(E,D_R,R)` where:

`E` is the entity set;

`D_R` is the relation domain;

`R:D_R→RelationState` assigns relation states.

## 9. State

`S=(C,M,X)` where `M` and `X` are optional explicitly retained variables.

Nothing may be added to state implicitly.

## 10. Transition

A transition is a declared mapping:

`T:S×U→S'`

where `U` is optional external input.

Transition semantics are model-dependent and are not primitive physical laws.

## 11. Change

Change is a comparison:

`COMPARE(S,S')→ChangeRecord`.

The record may contain entity-state changes, relation-state changes, relation births/removals and structural reconfiguration.

A numerical magnitude requires a separate derived definition.

## 12. Paths

A path is an ordered compatible sequence of relations:

`P=(r₁,...,rₙ)`.

Path order, endpoints, intermediate entities and signs are retained.

Concatenation is:

`P⧺Q`

when endpoints are compatible.

Path concatenation is associative. This does not define a primitive relation reduction.

## 13. Higher-level entities

A stable substructure may be mapped to a higher-level entity only through an explicit coarse-graining/identification map and validation criterion.

This is the entry point for emergence; it is not an automatic consequence of stability.

## 14. Minimal principles

**P1 — Typed distinction.** Entity and relation states are different types.

**P2 — Relation requires a domain.** Presence is separate from sign.

**P3 — Structure is relational.** Entity-state multisets alone do not determine relational organization.

**P4 — Change is comparison.** No primitive subtraction is assumed.

**P5 — Paths retain order.** A path is not silently replaced by a scalar.

**P6 — Reduction requires sufficiency.** A compressed representation is not equivalent unless it preserves the declared task/behavior.

**P7 — Emergence requires identification.** A macro-object needs an explicit map and validation criterion.

## 15. Research constraint

No familiar mathematical object is imported as fundamental merely because it is convenient.

For every proposed object ask:

`Can it be derived from the typed Ω primitives?`

If yes, derive it.

If no, either add the smallest necessary primitive with justification or record the limitation.

## Status

`DEFINED / FOUNDATION`

The foundation is sufficient for the current v0.4 language layer. It is not a claim that the four primitive values constitute the ontology of nature.
