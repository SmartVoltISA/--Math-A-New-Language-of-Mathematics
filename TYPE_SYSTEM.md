# Ω-Math v0.4 — Typed Object System

## Purpose

Ω-Math uses explicit types so ordinary arithmetic cannot enter the language unnoticed.

## 1. Primitive types

### Entity

`Entity=(id,state)` with `state∈{0,1}`.

Identity and state are distinct fields.

### Relation

`Relation=(source,target,sign)` with `sign∈{−1,+1}` and `(source,target)∈D_R`.

Absence from `D_R` is not a relation value.

## 2. Derived types

- `Distinction` — result of a declared comparison.
- `Configuration` — entities plus relation domain and relation states.
- `State` — configuration plus explicitly retained variables.
- `Path` — ordered compatible sequence of relations.
- `Cycle` — path satisfying a declared return criterion.
- `Transformation` — declared mapping between states/configurations.
- `Observation` — mapping from state to a selected description.
- `Equivalence` — relation defining indistinguishability for a declared purpose.
- `Quotient` — construction induced by equivalence plus explicit mapping rules.
- `Invariant` — property preserved by a specified transformation family.
- `Memory` — retained state with demonstrated later functional effect.
- `Model` — internal representation generated and used under explicit criteria.

## 3. Canonical type-valid operations

| Input | Operation | Output | Status |
|---|---|---|---|
| Entity, Entity | `DIST` | Distinction | DEFINED |
| Relation sequence | `PATH` | Path | DEFINED |
| Path, Path | `CONCAT` | Path | DEFINED, compatible endpoints |
| State, State | `COMPARE` | ChangeRecord | DEFINED |
| State + Rule | `TRANSFORM` | State | DEFINED FRAMEWORK |
| State | `OBSERVE` | Observation | DEFINED |
| Observation/Behavior | `EQUIV` | Equivalence | DEFINED |
| Object + Equivalence | `QUOTIENT` | Quotient | DEFINED FRAMEWORK |
| Property + TransformFamily | `INVARIANT` | Preservation test | DEFINED |
| State + Transition + Horizon | `BEHAVIOR` | Trajectory | DEFINED FRAMEWORK |
| Transformation + Cost | `DISTANCE` | Candidate distance | DERIVED |

## 4. Invalid silent coercions

The following are forbidden unless explicitly declared by a model:

- entity state `0` as relation absence;
- relation sign `−1` as subtraction;
- relation sign `+1` as numerical addition;
- change as ordinary subtraction;
- path as arithmetic sum/product;
- cycle as causality;
- connectivity as physical space;
- transformation non-invertibility as physical irreversibility;
- quotient collapse as destruction of entities;
- observation equality as identity;
- correlation as causality;
- state recording as functional memory.

## 5. Operator admission

Every new operator must declare:

1. input types;
2. output type;
3. domain of definition;
4. primitive or derived status;
5. semantics;
6. algebraic laws claimed;
7. counterexamples/failure conditions;
8. comparison with existing mathematics.

## 6. Behavioral typing

A state-only observation has type:

`O_state:State→Observation`.

Finite-horizon behavioral equivalence is parameterized by observation, transition rule, inputs/interventions and horizon:

`≈_β,h`.

## 7. Reduction typing

A reduction has type:

`Q:X→Y`.

It becomes behavior/task-sufficient only relative to a declared `F` when:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

## Status

`DEFINED / CORE TYPE DISCIPLINE`
