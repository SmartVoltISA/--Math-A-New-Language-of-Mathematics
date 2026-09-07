# Ω-Math v0.9 — Algebraic Layer

## Purpose

Ω-Math does not assign ordinary arithmetic meaning to the symbols `0, 1, −1, +1`. Algebra is typed: entity states and relation states belong to disjoint domains.

The algebraic layer studies which compositions are legal, which structures are derived, and which stronger laws require additional semantics.

## 1. Primitive domains

`EntityState = {0,1}`

`RelationState = {−1,+1}`

These domains are disjoint by type.

## 2. Entity algebra

Primitive entity-state operations are intentionally minimal:

- equality/distinction are defined;
- entity-state addition is not primitive;
- arithmetic coercion is forbidden unless an external model explicitly declares it.

`DIST(a,b)=0` when `a=b`, otherwise `1`.

## 3. Path composition is the canonical sequential composition

For compatible paths `P=(r₁,...,rₙ)` and `Q=(q₁,...,qₘ)`, `P⧺Q` is their ordered concatenation.

Path concatenation is associative, and the empty path `ε_e` is the identity for compatible path concatenation.

This does not introduce a primitive relation identity.

## 4. Relation-to-relation collapse

A primitive binary operation `REL_COMPOSE : RelationState × RelationState → RelationState` is **not required** by the minimal language.

Sequential relational organization is retained as a path. Any collapse of a path into a single relation is an explicitly declared derived abstraction and may lose information.

## 5. Sign product

For a path `P=(r₁,...,rₙ)`, define the derived sign summary `Σ(P)=∏ᵢ sign(rᵢ)`.

For non-empty paths over `{−1,+1}`, this remains in `{−1,+1}` and is associative and commutative as an ordinary multiplication operation on the summary values.

This is a valid algebraic **summary**, not a universal law of relational composition. It can lose path length, order, intermediate entities, alternatives and conflicts.

## 6. Parallel aggregation is separate

Several relations sharing endpoints are not sequential composition. In particular, `A —(+1)→ B` and `A —(−1)→ B` do not imply a primitive relation `0`.

Possible representations include multirelations, conflict records or richer structures, but none is promoted to a primitive without declared semantics and tests.

## 7. Direction and reversal

`rev(r₁,...,rₙ)=(rₙ,...,r₁)` is a sequence operation. It does not imply that reverse directed edges exist. Therefore `REL_INV` is not primitive.

## 8. Identity and inverse

No primitive relation identity or inverse is admitted in v0.9. The path-level identity is supplied by `ε_e`. A relation inverse requires additional semantics for directed relations and cannot be inferred from sign labels.

## 9. Established algebraic laws

| Structure | Law | Status |
|---|---|---|
| Path concatenation | associativity | DERIVED |
| Path concatenation | empty-path identity | DERIVED |
| Exact path equality | reflexive/symmetric/transitive | DERIVED |
| Sign summary | closure on non-empty paths | DERIVED |
| Sign summary | associativity | DERIVED from multiplication |
| Sign summary | commutativity | DERIVED for the summary operation |
| Primitive relation composition | closure | NOT ADMITTED |
| Primitive relation composition | identity | NOT ADMITTED |
| Primitive relation composition | inverse | NOT ADMITTED |
| Universal physical composition law | — | OPEN |

## 10. Richer composition remains model-relative

If a future model defines a richer composition operator, its associativity, identity, inverse and closure must be proved or tested for that exact representation. Failure is a structural result, not something to repair silently.

## 11. Algebra and behavior

Equal sign summaries do not imply equal paths or equal future behavior. Behavioral equivalence requires a declared observation/dynamics/task criterion.

`equal summary ≠ equal path ≠ equal structure ≠ equal behavior`.

## 12. Admission and verification

Any new algebraic primitive requires: typed signature; domain restrictions; semantics; algebraic laws; information-loss analysis; counterexamples/failure conditions; comparison with existing mathematics; and executable or exhaustive tests where finite verification is possible.

## 13. Status

`CANONICAL / v0.9 SYNCHRONIZED`

The minimal algebraic boundary is closed: path composition is defined; sign multiplication is a derived summary; primitive relation composition, identity and inverse remain outside the required core.

See `PATH_ALGEBRA.md`, `RELATION_COMPOSITION.md`, `OPERATOR_TABLE.md`, and `FRONTIER_CLOSURE_v0.9.md` for corresponding canonical definitions and limits.
