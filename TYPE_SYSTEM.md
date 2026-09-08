# Ω-Math v0.9 — Typed Object System

## Purpose

Ω-Math uses explicit types so ordinary arithmetic or physical interpretation cannot enter the language implicitly.

## 1. Primitive types

### Entity

`Entity=(id,state)` with `state∈{0,1}`.

Identity and state are distinct fields.

### Relation

`Relation=(source,target,sign)` with `sign∈{−1,+1}` and `(source,target)∈D_R`.

Absence from `D_R` is not a relation value.

## 2. Derived types

- `Distinction` — result of a declared comparison.
- `Configuration` — entities plus relation domain and relations.
- `State` — configuration plus explicitly retained variables.
- `Path` — ordered compatible sequence of relations.
- `Cycle` — path satisfying a declared return criterion.
- `Transformation` — declared mapping between states/configurations.
- `Observation` — mapping from state to selected description.
- `Equivalence` — indistinguishability relation for a declared task.
- `Quotient` — construction induced by an equivalence plus mapping rules.
- `Invariant` — property preserved by a specified transformation family.
- `Memory` — retained state with demonstrated later functional effect.
- `SelfModel` — internal representation generated from and functionally used with respect to system state.

## 3. Canonical type-valid operations

| Input | Operation | Output | Status |
|---|---|---|---|
| Entity, Entity | `DIST` | Distinction | DEFINED |
| Relation sequence | `PATH` | Path | DEFINED |
| Path, Path | `CONCAT` | Path | DEFINED, compatible endpoints |
| State, State | `COMPARE` | ChangeRecord | DEFINED |
| State + Rule | `TRANSFORM` | State | DEFINED FRAMEWORK |
| State | `OBSERVE` | Observation | DEFINED |
| Observation + dynamics | `EQUIV` | Equivalence | DEFINED FRAMEWORK |
| Object + Equivalence | `QUOTIENT` | Quotient | DEFINED FRAMEWORK |
| Property + TransformFamily | `INVARIANT` | Preservation test | DEFINED |
| State + Transition + Horizon | `BEHAVIOR` | Behavior descriptor | DEFINED FRAMEWORK |
| Transformation + Cost | `DISTANCE` | Candidate distance | DERIVED |

## 4. Invalid silent coercions

Forbidden unless explicitly declared by a model:

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
- stored record as functional memory;
- internal order as physical duration;
- transformation cost as physical energy.

## 5. Operator admission

Every new operator must declare:

1. input types;
2. output type;
3. domain of definition;
4. primitive or derived status;
5. semantics;
6. claimed laws;
7. information-loss behavior;
8. counterexamples/failure conditions;
9. comparison with existing mathematics.

## 6. Behavioral typing

A state-only observation has type:

`O_state:State→Observation`.

Finite-horizon behavioral equivalence is parameterized by observation, transition rule, inputs/interventions and horizon.

For nondeterministic systems the successor set is retained rather than silently collapsed.

## 7. Reduction typing

A reduction has type:

`Q:X→Y`.

It is task-sufficient only relative to a declared behavior `F` when:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

## Status

`CANONICAL / v0.9 SYNCHRONIZED`
