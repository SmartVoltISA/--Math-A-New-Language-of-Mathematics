# Ω-Math v0.5 — Research Status

## Current state

The repository contains a typed relational language with explicit syntax, semantics, operator discipline, reduction rules, transformations, invariants/symmetry, path algebra, behavioral equivalence and a structural-edit geometry.

The central discipline remains:

`define → derive → execute → verify → compare → falsify → record`.

The language deliberately separates mathematical representation from physical interpretation.

## v0.5 mathematical milestone

### M9 — Structural relational geometry

`RELATIONAL_GEOMETRY_001.md` removes the artificial fixed relation-slot assumption from the first metric baseline.

A configuration can now change by:

- entity-state flip;
- relation addition;
- relation removal;
- relation sign flip.

A transformation path has additive declared cost, and structural distance is the minimum cost of a path between configurations.

Status: `DERIVED CONSTRUCTION`.

### M10 — Quotient / label-independent geometry

For equal-cardinality finite configurations, minimizing structural edit distance over all entity bijections produces a distance on structural orbits under the declared relabeling group.

Under reversible equal-cost edits, non-negativity, symmetry and triangle inequality follow from the edit algebra and composition.

Status: `DERIVED THEOREM UNDER DECLARED ASSUMPTIONS`.

### M11 — Exhaustive finite verification

`EXPERIMENT_RELATIONAL_GEOMETRY_001.md` enumerates all 12 configurations of the two-entity/one-relation finite model and exhaustively checks identity, non-negativity, symmetry, triangle inequality and the corresponding two-element relabeling quotient.

Status: `EXECUTED / SUPPORTED UNDER DECLARED FINITE MODEL`.

### M12 — Geometry signature

`Γ_h(C)` records the spectrum of structural distances from a configuration to configurations that are behaviorally distinguishable within horizon `h`.

This is introduced as a derived observable, not as a universal invariant.

Status: `DEFINED / OPEN FOR GENERAL PROPERTIES`.

## What changed mathematically

The geometry layer is no longer restricted to changing values inside a fixed encoding.

It now admits structural events:

`absence ↔ relation`.

Therefore the geometry can measure the cost of changing relational organization itself.

This is a new Ω-Math construction. It is **not** claimed to be globally novel without a dedicated literature/novelty audit.

## Existing closed milestones

### M1 — Four length-2 signed cases

`(+,+)→+`, `(+,-)→-`, `(-,+)→-`, `(-,-)→+` under the scalar sign-product summary.

Status: `DERIVED`.

### M2 — Sign-product is not universal relation composition

Status: `COUNTEREXAMPLE / REJECTED AS UNIVERSAL LAW`.

### M3 — Path associativity

Status: `DEFINED / DERIVED`.

### M4 — Parallel-path conflict

Status: `OPEN / NO SILENT COLLAPSE`.

### M5 — Finite-horizon behavioral equivalence

Status: `DEFINED / DERIVED`.

### M6 — Invariants and symmetry

Status: `DEFINED / DERIVED METHODOLOGICAL RULE`.

### M7 — Path-profile insufficiency

Status: `COUNTEREXAMPLE`.

### M8 — Fixed-slot transformation metric

Status: `DERIVED BASELINE`.

## Current algebraic decision

`PATH CONCATENATION`: `DEFINED`.

`SIGN-PRODUCT SUMMARY`: `DERIVED`.

`SIGN-PRODUCT AS COMPLETE RELATION COMPOSITION`: `REJECTED`.

`PRIMITIVE RELATION REDUCTION`: `OPEN`.

Path information must be retained until sufficiency is demonstrated for the declared task.

## Current geometry decision

`FIXED-SLOT HAMMING`: established baseline.

`STRUCTURAL EDIT DISTANCE`: derived for declared edit systems.

`LABEL-INDEPENDENT QUOTIENT DISTANCE`: derived for finite equal-cardinality configurations under the stated assumptions.

`PHYSICAL SPACE`: not derived.

Next mathematical tests:

1. unequal entity cardinality;
2. entity insertion/deletion with incident relations;
3. directed relations;
4. asymmetric transformation costs;
5. quotient distance for behavioral equivalence classes;
6. well-definedness of quotient geometry;
7. relation/path conflict geometry;
8. comparison with graph edit distance, orbit metrics and configuration-space metrics.

## Point / boundary status

Executed closure, reconnection, redundancy and combined-factor probes did not establish a unique single Point-like object.

Current evidence supports only:

`relations → closure → relational separation → candidate core/interface`.

The Point remains `OPEN`.

## Novelty discipline

The repository must distinguish:

- independent reconstruction of known mathematics;
- a new definition inside Ω-Math;
- a new theorem derived from Ω definitions;
- a genuinely new mathematical result after comparison with prior literature.

No global novelty claim is made for M9–M12 yet.

## Explicitly open

- canonical primitive relation composition;
- canonical path equivalence;
- universal sufficient path profile;
- unrestricted canonical metric;
- quotient geometry in the general case;
- physical time;
- probability;
- energy;
- physical ontology;
- task-independent emergence criterion;
- self-model and causal self-reference;
- physical bridge and independent empirical predictions.

## Critical methodological rule

`representable ≠ explained`

`correlated ≠ caused`

`stable ≠ fundamental`

`compressed ≠ equivalent`

`emergent candidate ≠ emergence proven`

## Version

**Ω-Math v0.5** — structural relational geometry derived from typed edit transformations, with finite exhaustive verification and explicit quotient construction.
