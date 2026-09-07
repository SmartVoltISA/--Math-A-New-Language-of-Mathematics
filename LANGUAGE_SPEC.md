# Ω-Math v0.4 — Language Specification

## Purpose

This document turns the research vocabulary into a compact language specification. It separates syntax, types, semantics and derived constructions.

## 1. Primitive domains

`EntityState = {0,1}`

`RelationState = {−1,+1}`

The domains are disjoint by type.

## 2. Primitive objects

An entity is:

`e = (id, s)` where `s ∈ EntityState`.

A relation is:

`r = (src, dst, q)` where `q ∈ RelationState` and `(src,dst) ∈ D_R`.

A relation is directed because `(src,dst)` and `(dst,src)` are distinct ordered pairs unless an explicit symmetry identifies them.

## 3. Configuration

A configuration is:

`C = (E,D_R,R)`

with entity set `E`, relation domain `D_R`, and relation assignment `R:D_R→RelationState`.

A state is:

`S = (C,M,X)`

where `M` and `X` are optional explicitly declared retained variables. They must never be added silently.

## 4. Core expressions

### Relation

`e_i —q→ e_j`

### Path

`P = (r_1,r_2,...,r_n)`

with compatible endpoints.

### Path concatenation

If the endpoint of `P` equals the start of `Q`:

`P ⧺ Q`

is the ordered concatenated path.

Path concatenation is associative:

`(P ⧺ Q) ⧺ R = P ⧺ (Q ⧺ R)`.

This does not imply that a path can be replaced by a primitive relation.

### Observation

`O:S→Y`

where `Y` is explicitly declared.

### Transformation

`T:S→S'`

with a declared domain, output type and admissibility condition.

## 5. Primitive operators

| Operator | Input | Output | Status |
|---|---|---|---|
| `DIST` | Entity, Entity | Distinction | defined |
| `PATH` | compatible Relation sequence | Path | defined |
| `COMPARE` | State, State | Change record | defined |
| `OBSERVE` | State | Observation | defined |
| `TRANSFORM` | State + rule | State | defined framework |

## 6. Derived operators

### Sign summary

For a finite path with signs `q_1,...,q_n`:

`Σ(P) = ∏ q_i`.

This is a scalar summary only.

### Behavioral equivalence

For deterministic transition `T`, observation `O`, fixed input sequence `U` and horizon `h`:

`x ≈_β,h y`

iff

`O(T^k(x;U)) = O(T^k(y;U))`

for every `0≤k≤h`.

### Transformation distance

For admissible transformations `𝒯(x,y)` and cost `c`:

`d_c(x,y)=inf{c(T):T∈𝒯(x,y)}`.

Whether this is a metric is a theorem to be established for the selected transformation family.

## 7. Forbidden implicit meanings

The language does not allow these identifications without an explicit rule:

`0 = absence of relation`

`−1 = subtraction`

`+1 = addition`

`path = sign sum`

`cycle = causality`

`connectivity = physical distance`

`change = arithmetic subtraction`

`observation equality = identity`

`stable pattern = emergence proven`

## 8. Reduction rule

A map `Q:X→Y` is an admissible task-relative reduction for task `F` only if the retained representation is sufficient for the declared output/behavior.

A strong behavior-preserving condition is:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

If this implication fails, `Q` is information-losing for `F` and cannot be called behavior-preserving for that task.

## 9. Extension rule

A new primitive may be added only when:

1. existing primitives cannot express the required object without contradiction or uncontrolled ambiguity;
2. the missing capability is demonstrated by a counterexample or formal impossibility result;
3. the new primitive has a declared type and semantics;
4. competing existing mathematical constructions are recorded;
5. tests are defined before promoting the primitive to core status.

## 10. Status levels

`DEFINED` — syntax/semantic rule introduced by the language.

`DERIVED` — follows from existing rules.

`EXECUTED` — tested by explicit finite computation/construction.

`SUPPORTED` — survives specified controls.

`OPEN` — unresolved.

`REJECTED` — no longer accepted under documented evidence.

## 11. Current boundary

The language is complete enough to express typed entities, signed relations, paths, transformations, observations, equivalence and candidate quantitative structure.

It is intentionally **not** complete as a universal mathematics. Primitive relation reduction, unrestricted metric, probability, physical time, energy and physical interpretation remain open.
