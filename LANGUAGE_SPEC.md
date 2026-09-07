# Ω-Math v0.6 — Language Specification

## Purpose

This document defines the canonical Ω-Math language layer: primitive domains, typed objects, expressions, derived operators, task-relative reduction, and rules for admitting extensions.

Ω-Math is a typed formal research language. Physical interpretation is never implicit.

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

A configuration is:

`C = (E,D_R,R)`

with entity set `E`, relation domain `D_R`, and relation assignment `R:D_R→RelationState`.

A state is:

`S = (C,M,X)`

where `M` and `X` are optional explicitly declared retained variables. They must never be added silently.

## 3. Core expression classes

### Relation

`e_i —q→ e_j`

### Path

`P = (r_1,r_2,...,r_n)` with compatible endpoints.

### Path concatenation

If the endpoint of `P` equals the start of `Q`:

`P ⧺ Q`

is the ordered concatenated path.

Path concatenation is associative:

`(P ⧺ Q) ⧺ R = P ⧺ (Q ⧺ R)`.

No scalar replacement is implied.

### Observation

`O:S→Y` where `Y` is explicitly declared.

### Transformation

`T:S×U→S'` with a declared input domain, output type and admissibility condition.

### Transition system

A declared deterministic system is

`𝒟=(S,U,T,O)`.

## 4. Canonical operators

| Operator | Input | Output | Status |
|---|---|---|---|
| `DIST` | Entity, Entity | Distinction | defined |
| `INCIDENT` | Relation, Entity | Incidence record | defined |
| `PATH` | compatible Relation sequence | Path | defined |
| `CYCLE` | Path | Cycle record | defined conditionally |
| `CONCAT` | compatible Paths | Path | defined |
| `SIGN` | Path | Relation-sign sequence / summary | defined derived view |
| `COMPARE` | State, State | Change record | defined |
| `TRANSFORM` | State + rule/input | State | defined framework |
| `OBSERVE` | State | Observation | defined |
| `EQUIV` | States + declared task | Equivalence relation candidate | defined |
| `QUOTIENT` | Equivalence relation | Quotient state space | defined |
| `INVARIANT` | Object family + transformation family | Invariant candidate | defined framework |
| `BEHAVIOR` | State + declared task | Behavior trace | defined |
| `COST` | Transformation | Nonnegative cost | defined framework |
| `DISTANCE` | States + admissible transformations | Extended distance candidate | derived |
| `SYMMETRY` | Configuration + relabeling | Orbit/action record | defined framework |

Reserved until separately admitted: `REL_COMPOSE`, `REL_ID`, `REL_INV`, `PATH_EQ`, `CAUSE`, `PROB`, `ENERGY`, `TIME_PHYSICAL`.

## 5. Derived operators

### Sign summary

For a finite path with signs `q_1,...,q_n`:

`Σ(P) = ∏ q_i`.

This is a scalar summary only.

### Finite-horizon behavior

For input sequence `u=(u_0,...,u_{h-1})`:

`B_h(s,u)=(O(T^0_u(s)),...,O(T^h_u(s)))`.

### Behavioral equivalence

`s ≈_h s'` iff

`B_h(s,u)=B_h(s',u)`

for every admissible input sequence `u` of length `h`.

### Sufficient relational state

For task `𝒟=(S,U,T,O)` and horizon `h`, define

`SR_𝒟,h(s)=[s]_h`

where `[s]_h` is the behavioral-equivalence class of `s`.

A candidate reduction `Q:S→Z` is sufficient when

`Q(s)=Q(s') ⇒ B_h(s,u)=B_h(s',u)`

for every admissible `u`.

### Transformation distance

For admissible transformations `𝒯(x,y)` and cost `c`:

`d_c(x,y)=inf{c(T):T∈𝒯(x,y)}`.

Whether this is a metric is a theorem to be established for the selected transformation family.

## 6. Recursive behavioral construction

Base:

`Q_0(s)=O(s)`.

For deterministic finite systems, a finite-horizon refinement can be represented recursively by current observation and successor classes under every declared input:

`Q_{h+1}(s)=(O(s), {(u,Q_h(T(s,u))) : u∈U})`.

The collection type must be declared when input order or multiplicity matters.

The construction is an Ω-Math formulation of task-preserving behavioral refinement. No global novelty claim is attached to it.

## 7. Reduction rule

A reduction `Q:X→Y` is admissible for task `F` only if its retained representation is sufficient for the declared output/behavior.

Strong finite-horizon condition:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

If the implication fails, `Q` is information-losing for `F` and cannot be called behavior-preserving for that task.

Compression must therefore remain distinct from equivalence.

## 8. Forbidden implicit meanings

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

`structural similarity = behavioral equivalence`

`finite-horizon equivalence = infinite-horizon equivalence`

## 9. Extension/admission rule

A new primitive may be added only when:

1. existing primitives cannot express the required object without contradiction or uncontrolled ambiguity;
2. the missing capability is demonstrated by a counterexample or formal impossibility result;
3. the new primitive has a declared type and semantics;
4. competing existing mathematical constructions are recorded;
5. tests are defined before promotion;
6. the proposed primitive is not merely a convenient alias for an existing derived construction.

## 10. Status levels

`DEFINED` — syntax/semantic rule introduced by the language.

`DERIVED` — follows from existing rules.

`EXECUTED` — tested by explicit finite computation/construction.

`SUPPORTED` — survives specified controls.

`HYPOTHESIS` — proposed but unresolved.

`THEOREM` — formally proved under stated assumptions.

`COUNTEREXAMPLE` — demonstrates failure of a universal claim.

`REJECTED` — no longer accepted under documented evidence.

`OPEN` — unresolved.

## 11. Completeness boundary

Ω-Math is now a coherent typed language for:

`entity → relation → configuration → state → path → transformation → observation → behavior → equivalence → quotient → reduction → cost → structural geometry`.

This is language completeness for the currently admitted domain, not universal mathematical completeness.

Still open as mathematical extensions or physical bridges:

- primitive relation composition;
- canonical path equivalence;
- unrestricted metric;
- general quotient geometry;
- probability;
- physical time;
- energy;
- physical ontology;
- task-independent emergence criterion;
- causal self-model;
- independent physical predictions.
