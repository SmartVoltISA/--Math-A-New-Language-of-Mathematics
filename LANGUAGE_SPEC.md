# Ω-Math v0.9 — Language Specification

## Purpose

This document defines the canonical Ω-Math language layer: primitive domains, typed objects, expressions, derived operators, task-relative reduction and extension rules. Physical interpretation is never implicit.

## 1. Primitive domains

`EntityState = {0,1}`

`RelationState = {−1,+1}`

The domains are disjoint by type. Relation absence is a domain condition, not a third relation value.

## 2. Primitive objects

`e=(id,s)`, `s∈EntityState`.

`r=(src,dst,q)`, `q∈RelationState`, `(src,dst)∈D_R`.

`C=(E,D_R,R)` with `R:D_R→RelationState`.

`S=(C,M,X)` with explicitly declared retained variables.

## 3. Core expression classes

### Path

`P=(r₁,...,rₙ)` with compatible endpoints. Path order and intermediate structure are retained.

### Path concatenation

`P⧺Q` is the ordered concatenation when endpoints are compatible. It is associative. The empty path `ε_e` is the identity for compatible path concatenation.

### Exact path equality

`P=Q ⇔ |P|=|Q| ∧ ∀i, r_i=q_i`.

This is representation identity only; it is not structural, behavioral, homotopy or sign equivalence.

### Observation and transformation

`O:S→Y` and a declared transformation/transition relation or function over typed states. Deterministic systems use `T:S×U→S'`; nondeterministic systems use `N:S×U→𝒫(S)`.

## 4. Canonical operators

See `OPERATOR_TABLE.md` for the synchronized inventory. Core operators include `DIST`, `INCIDENT`, `PATH`, `PATH_EQ`, `CYCLE`, `CONCAT`, `SIGN`, `COMPARE`, `TRANSFORM`, `OBSERVE`, `EQUIV`, `QUOTIENT`, `INVARIANT`, `BEHAVIOR`, `COST`, `DISTANCE`, `SYMMETRY`, `RETAIN`, `ORDER`, `HORIZON`, `BRANCH`, `REACH`, `MODEL`, `FEEDBACK`, and `COARSE`.

Primitive `REL_COMPOSE`, `REL_ID`, and `REL_INV` are not required by the minimal core.

## 5. Derived semantics

### Sign summary

`Σ(P)=∏ sign(r_i)` is a closed derived summary. It does not replace the path object universally.

### Finite-horizon behavior

For declared dynamics, observation map and admissible inputs/interventions, `B_h` records the selected finite future behavior.

### Behavioral equivalence

`s≈ₕs'` when the declared behavior/observation criterion agrees through horizon `h` for all admissible inputs under the selected semantics.

### Infinite horizon

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

Thus `≈∞ = ⋂ₕ≈ₕ`; no new primitive is required.

### Sufficient reduction

`Q(x)=Q(y) ⇒ F(x)=F(y)` is the task-relative sufficiency condition. If it fails, the reduction is information-losing for that task.

### Transformation distance

`d_c(x,y)=inf{c(T):T∈𝒯(x,y)}` is a candidate derived distance. Metric status requires proof/verification for the selected transformation family.

## 6. Nondeterminism

`N:S×U→𝒫(S)` retains the successor set. Equivalence must explicitly declare whether it preserves traces, branching, existential reachability, universal safety or another task. Fairness and liveness are explicit predicates over infinite runs.

## 7. Quotient geometry

For an equivalence `~`,

`d_Q([x],[y])=inf{d(x',y'):x'~x,y'~y}`

is a quotient-distance candidate. It is not automatically a pseudometric for an arbitrary equivalence relation. Pseudometric/metric status requires explicit compatibility and, for metric status, separation conditions. See `QUOTIENT_GEOMETRY_CONDITIONS.md`.

## 8. Causality and external bridges

Causal claims require explicit intervention semantics, e.g. `I:S×A→S`; temporal succession alone is not causal proof.

Probability requires an independently declared kernel such as `K:S×U→Dist(S)`.

Physical time requires an empirical duration map. Physical energy is not identified with generic transformation cost.

## 9. Forbidden implicit meanings

Entity state ≠ relation state; absence ≠ relation value; `−1` ≠ subtraction; `+1` ≠ addition; path ≠ scalar; cycle ≠ causality; connectivity ≠ physical space; observation equality ≠ identity; structural similarity ≠ behavioral equivalence; transition order ≠ physical duration; transformation cost ≠ physical energy.

## 10. Extension/admission rule

A new primitive requires a demonstrated need, declared type/semantics, comparison with existing mathematics, counterexample/failure analysis and tests before promotion.

## 11. Completeness boundary

Ω-Math v0.9 is formally complete as a minimal typed relational language for its declared domain. This does not mean universal mathematical completeness or a completed physical theory.

Open research remains in unrestricted path abstractions, general quotient geometry, probability, physical time/energy, physical ontology, task-independent emergence, causal self-model and independent physical predictions.

**Status: CANONICAL / v0.9 SYNCHRONIZED**
