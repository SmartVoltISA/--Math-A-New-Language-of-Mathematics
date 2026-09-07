# Ω-Math — Typed Object System v0.2

## Purpose

Ω-Math uses typed primitives. This document makes the type boundaries explicit so that ordinary arithmetic cannot enter the language unnoticed.

## 1. Primitive types

### Entity

`Entity = (id,state)` with `state ∈ {0,1}`.

Identity and state are distinct fields.

### Relation

`Relation = (source,target,sign)` with `sign ∈ {−1,+1}` and `(source,target) ∈ D_R`.

Absence from `D_R` is not a relation value.

## 2. Derived types

`Distinction` — result of a declared comparison.

`Configuration` — complete arrangement of entities and relations at one modeling step.

`State` — configuration plus explicitly retained variables.

`Path` — ordered connected sequence of relations.

`Cycle` — path satisfying a declared return criterion.

`Transformation` — mapping between states/configurations.

`Observation` — mapping from a system/state to a selected description.

`Equivalence` — relation defining which objects are indistinguishable for a declared purpose.

`Quotient` — construction induced by an equivalence together with explicit entity/relation/path mapping rules.

`Invariant` — property preserved by a specified transformation family.

`Memory` — retained internal state with later causal/functional effect under a specified test.

`Model` — internal representation generated and used by a system under an explicit criterion.

## 3. Type-valid composition

The following operations are valid candidates:

| Input | Operation | Output | Status |
|---|---|---|---|
| Entity, Entity | `DIST` | Distinction | DEFINED |
| Entity, Relation | `INCIDENT` | structural relation | DEFINED |
| Relation, Relation | `COMPOSE` | Relation/path candidate | OPEN until composition semantics fixed |
| Relation sequence | `PATH` | Path | DEFINED |
| Path | `CYCLE` | Cycle / failure | DEFINED by criterion |
| State, State | `COMPARE` | Change/distinction object | DEFINED |
| State | `TRANSFORM` | State | DEFINED |
| State, Observation | `OBSERVE` | observation value | DEFINED |
| Observation | `EQUIV` | Equivalence relation | DEFINED |
| Equivalence | `QUOTIENT` | Quotient | DEFINED with explicit mapping rules |
| Transformation | `INVARIANT` | preserved property | DEFINED as a test |
| State, State | `BEHAVIOR` | trajectory relation | OPEN until horizon/input semantics fixed |

## 4. Invalid silent coercions

Ω-Math must reject or explicitly declare the following conversions:

- entity state `0` as relation absence;
- relation sign `−1` as subtraction;
- relation sign `+1` as numerical addition;
- change as ordinary subtraction;
- path as arithmetic sum of relation signs;
- cycle as proof of causality;
- graph connectivity as physical space;
- transformation non-invertibility as physical irreversibility;
- quotient collapse as destruction of entities;
- observation equality as identity equality;
- correlation as causality;
- state recording as memory.

## 5. Operator discipline

Every new operator must declare:

1. input types;
2. output type;
3. domain of definition;
4. whether it is primitive or derived;
5. algebraic laws claimed;
6. counterexamples or failure conditions;
7. whether an equivalent standard mathematical construction already exists.

## 6. Type separation and absence

Three distinctions are mandatory:

`entity state = 0`

`relation sign = −1`

`relation absent from D_R`.

They are different typed conditions and cannot be substituted for one another.

## 7. Behavioral typing

A state-only observation has type

`O_state : State → Observation`.

A behavior-preserving equivalence requires additional transition information. A candidate finite-horizon behavioral relation is written

`≈_β,h`

and is parameterized by observation, admissible inputs and horizon.

## 8. Status

`DEFINED / CORE DISCIPLINE`

This document is a typing specification, not a claim about physical ontology.
