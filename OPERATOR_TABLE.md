# Ω-Math v0.4 — Operator Table

This is the canonical operator inventory. An operator may not silently change type or meaning between documents.

| Operator | Signature | Status | Notes |
|---|---|---|---|
| `DIST` | `Entity × Entity → Distinction` | DEFINED | primitive comparison |
| `INCIDENT` | `Entity × Relation → incidence` | DEFINED | structural query |
| `PATH` | `Relation* → Path` | DEFINED | requires endpoint compatibility |
| `CYCLE` | `Path → Cycle ∪ Failure` | DEFINED | criterion must be declared |
| `CONCAT` / `⧺` | `Path × Path → Path` | DEFINED | compatible endpoints only |
| `SIGN` | `Path → RelationSummary` | DERIVED | scalar sign-product only |
| `COMPARE` | `State × State → ChangeRecord` | DEFINED | structural change, not subtraction |
| `TRANSFORM` | `State × Rule → State` | DEFINED FRAMEWORK | rule declares domain/action |
| `OBSERVE` | `State → Observation` | DEFINED | observation map is task-relative |
| `EQUIV` | `Observation/Behavior → Equivalence` | DEFINED | semantics must be declared |
| `QUOTIENT` | `Object × Equivalence → Quotient` | DEFINED FRAMEWORK | mapping rules required |
| `INVARIANT` | `Property × TransformFamily → Test` | DEFINED | preservation is relative |
| `BEHAVIOR` | `State × Transition × Horizon → Trajectory` | DEFINED FRAMEWORK | deterministic core first |
| `COST` | `Transformation → [0,∞]` | DEFINED FRAMEWORK | physical energy forbidden by default |
| `DISTANCE` | `State × State → [0,∞]∪{∞}` | DERIVED CANDIDATE | minimal transformation cost |
| `SYMMETRY` | `Equivalence × State → Transformations` | DEFINED | exact/observational/behavioral levels distinguished |

## Operator admission rule

Every new operator must declare:

1. signature;
2. domain restrictions;
3. primitive/derived status;
4. semantics;
5. algebraic laws;
6. counterexamples;
7. relation to existing mathematics;
8. tests.

## Reserved unresolved operators

The following names are intentionally not assigned canonical semantics yet:

`REL_COMPOSE`, `REL_ID`, `REL_INV`, `PATH_EQ`, `CAUSE`, `PROB`, `ENERGY`, `TIME_PHYSICAL`.

They may be used in hypotheses only with an explicit status label.

## Status

`DEFINED / CANONICAL INVENTORY`
