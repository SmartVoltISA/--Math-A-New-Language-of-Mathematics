# Ω-Math v0.4 — Research Status

## Current state

The repository now contains a typed relational language with explicit syntax, semantics, operator discipline, reduction rules, transformations, invariants/symmetry, path algebra, behavioral equivalence and a first transformation-derived metric baseline.

The central discipline is:

`define → derive → execute → verify → compare → falsify → record`.

The language deliberately separates mathematical representation from physical interpretation.

## v0.4 language milestones

### L1 — Canonical type system

Entity state, relation state, relation absence, identity and configuration are explicitly typed.

Status: `DEFINED`.

### L2 — Canonical operator inventory

`OPERATOR_TABLE.md` fixes the signatures and status of current operators and reserves unresolved operators from silent use.

Status: `DEFINED`.

### L3 — Semantic discipline

`SEMANTICS.md` records direction, absence, path, transformation, observation, equivalence, quotient, causality, memory and emergence semantics.

Status: `DEFINED`.

### L4 — Reduction discipline

`REDUCTION_RULES.md` formalizes task-relative sufficiency and gives the canonical counterexample pattern:

`Q(x)=Q(y)` while `F(x)≠F(y)`.

Status: `DEFINED / DERIVED METHODOLOGICAL RULE`.

### L5 — Canonical reference examples

`CANONICAL_EXAMPLES.md` fixes minimal interpretations of entities, relations, paths, transformations, observations and reductions.

Status: `DEFINED`.

## Closed mathematical milestones

### M1 — Four length-2 signed cases

`(+,+)→+`, `(+,-)→-`, `(-,+)→-`, `(-,-)→+` under the scalar sign-product summary.

Status: `DERIVED`.

### M2 — Sign-product is not universal relation composition

The scalar sign-product is closed and useful as a summary, but path information can affect behavior.

Status: `COUNTEREXAMPLE / REJECTED AS UNIVERSAL LAW`.

### M3 — Path associativity

Path concatenation is associative. Scalar sign-product is associative. Neither result licenses erasure of intermediate path structure.

Status: `DEFINED / DERIVED`.

### M4 — Parallel-path conflict

Conflicting or multiple parallel paths cannot be silently collapsed to one primitive relation state.

Status: `OPEN / NO SILENT COLLAPSE`.

### M5 — Finite-horizon behavioral equivalence

`x ≈ᵦ,h y` is defined by equality of declared observations through horizon `h` under the same declared inputs for deterministic systems.

`≈ᵦ,h+1 ⊆ ≈ᵦ,h` follows directly from the definition.

Status: `DEFINED / DERIVED`.

### M6 — Invariants and symmetry

An invariant is always relative to a declared transformation family. Label permutation is a mandatory representation control unless labels are part of the modeled object.

Status: `DEFINED / DERIVED METHODOLOGICAL RULE`.

### M7 — Path-profile insufficiency

`EXPERIMENT_PATH_DYNAMICS_001.md` gives a deterministic counterexample where equal endpoints, length and sign summary hide different intermediate organization and future behavior.

Status: `COUNTEREXAMPLE`.

### M8 — Transformation-derived metric baseline

A fixed relation-slot representation with unit-cost sign flips induces the Hamming/hypercube metric.

Status: `DERIVED BASELINE`.

This is not a unique Ω metric and not physical space.

## Current algebraic decision

`PATH CONCATENATION`: `DEFINED`.

`SIGN-PRODUCT SUMMARY`: `DERIVED`.

`SIGN-PRODUCT AS COMPLETE RELATION COMPOSITION`: `REJECTED` as a universal information-preserving law.

`PRIMITIVE RELATION REDUCTION`: `OPEN`.

Path information must be retained until sufficiency is demonstrated for the declared task.

## Current geometry decision

Transformation-derived distance is a valid mathematical construction when the admissible transformations and costs are declared. The next task is to remove artificial fixed-slot assumptions.

Required tests:

1. relation addition/removal;
2. entity-state changes;
3. principled nonnegative costs;
4. label-permutation invariance;
5. reversible versus irreversible transformations;
6. directed versus symmetric distance;
7. quotient-induced distance and well-definedness;
8. comparison with standard graph/edit/configuration metrics.

## Point / boundary status

Executed closure, reconnection, redundancy and combined-factor probes did not establish a unique single Point-like object.

The current evidence supports only:

`relations → closure → relational separation → candidate core/interface`.

The Point remains `OPEN` and must be treated as a multi-criterion intermediate regime rather than maximum closure or maximum connectivity.

## Research-map position

The formalism now has enough structure for direct technical comparison with existing mathematics rather than only philosophical comparison.

Primary comparison targets:

- category/compositional systems;
- graph transformation/rewrite systems;
- type/equivalence systems;
- transition-system behavioral equivalence;
- coarse-graining and causal emergence;
- relational/pregeometric approaches.

The purpose is to identify both independent reconstruction and genuine mathematical novelty. Similarity is not claimed as novelty.

## Explicitly open

- canonical primitive relation composition;
- canonical path equivalence;
- universal sufficient path profile;
- unrestricted canonical metric;
- quotient geometry;
- physical time;
- probability;
- energy;
- physical ontology;
- task-independent emergence criterion;
- self-model and causal self-reference;
- physical bridge and independent empirical predictions.

## Confidence labels

`DEFINED` = language rule introduced explicitly.

`DERIVED` = follows formally from current rules.

`EXECUTED` = evaluated by an explicit finite construction/computation.

`SUPPORTED` = survives specified controls.

`COUNTEREXAMPLE` = evidence against a universal claim.

`REJECTED` = claim no longer retained under documented evidence.

`OPEN` = unresolved.

## Critical methodological rule

`representable ≠ explained`

`correlated ≠ caused`

`stable ≠ fundamental`

`compressed ≠ equivalent`

`emergent candidate ≠ emergence proven`

## Physical hypothesis

`H-BH-0` — extreme relational distinguishability collapse may have a physically meaningful correspondence with characteristic black-hole behavior.

Status: `OPEN`.

No physical interpretation is accepted until an Ω quantity is independently defined, mapped to established observables, tested against controls and used to make predictions not used in its construction.

## Version

**Ω-Math v0.4** — typed relational language, explicit semantics and reduction discipline, tested composition/path layer, and first transformation-derived metric baseline.
