# EXPERIMENT — LIGHT Bridge 001

## Status

`PREREGISTERED / ANALYTICAL TEST`

## Question

Can the three strongest structural candidates extracted from LIGHT be represented without changing the Ω-Math v0.9 primitive type system?

Candidates:

1. admissibility constraint;
2. declared locality;
3. ordered path/loop residual.

## Frozen Ω primitives

- entity state: `{0,1}`
- relation state: `{−1,+1}`
- relation: `(src,dst,sign)`
- configuration: `(E,D_R,R)`
- state: `(C,M,X)`
- path: ordered relation sequence
- transformation: state transition/update rule
- observation: declared output map

No new primitive type is introduced by this experiment.

## Test A — Admissibility

Given a configuration `C`, define a predicate

`Adm_C(r) ∈ {false,true}`.

A transition candidate is legal only if every relation required by the declared transition rule satisfies the predicate.

### Result

This is a predicate over existing relations/configurations, so it does not require a new primitive value or primitive type. It can be represented semantically as a precondition on deterministic transitions or as a filter on nondeterministic successor sets.

**Decision: PASS as a derived semantic construct.**

## Test B — Locality

Define a declared predicate

`Loc_C(x,y) ∈ {false,true}`

that specifies which pairs may participate in local comparison/evolution under configuration `C`.

### Result

`Loc_C` is also a predicate over existing entities/configurations. It is therefore not forced into the primitive relation state domain `{−1,+1}` and does not require a new primitive type.

Crucially, `Loc_C` is not identified with graph connectivity. A connected graph may have a declared finite-range locality structure, and two connected configurations may have different locality predicates.

**Decision: PASS as a declared semantic structure; OPEN as to whether locality should become a first-class language object.**

## Test C — Loop residual

A generic ordered loop is already representable as a path whose first and last entity coincide. However, a nontrivial residual analogous in role to curvature requires an operation on local comparisons/transformations around the loop.

At v0.9, the path itself is available, but no universal primitive operation maps an arbitrary path to a curvature-like residual. A naive sign product is insufficient because existing experiments show that scalar summaries can erase intermediate organization.

### Result

Path/loop representation is available. A universal curvature operator is **not derived**.

**Decision: PARTIAL PASS — representation exists; operator remains open.**

## Overall decision

The LIGHT bridge does **not** expose a missing primitive type at this stage.

The strongest additions are semantic constructions:

`relation + configuration → admissibility`

`configuration → locality predicate`

`path/loop → candidate residual`

Only the third remains a genuine research frontier because the residual operator is not yet defined without importing additional mathematical structure.

## Falsification / next step

The bridge would be weakened if a minimal constrained propagation or locality model cannot be represented with the frozen v0.9 primitives and semantic predicates. The next decisive test is to construct explicit finite counterexamples for locality and loop residual sufficiency.
