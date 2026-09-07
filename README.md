# Ω-Math — A New Language of Mathematics

Ω-Math is an experimental mathematical language built from four primitive values with two different roles:

- `0, 1` — states of entities;
- `−1, +1` — states of relations.

The central research question is whether structure, dynamics, memory, geometry, time and higher-order phenomena can be represented or derived from relations between distinguishable entities.

This repository is a formal research program. It does not assume that nature is proven to have this ontology.

## Core distinction

The same numerical symbols must not be confused across types:

`Entity value ∈ {0, 1}`

`Relation value ∈ {−1, +1}`

Therefore `0 ≠ −1` and `1 ≠ +1` as mathematical objects of this language: they belong to different typed domains.

## Minimal object

An elementary Ω-relation is written as:

`eᵢ —rᵢⱼ→ eⱼ`

where `eᵢ, eⱼ ∈ {0,1}` and `rᵢⱼ ∈ {−1,+1}`.

A finite system is:

`Ω = (E, R, Dᴿ)`

where `E` is the set of entity states, `Dᴿ ⊆ E × E` is the domain on which relations are present, and `R` assigns `−1` or `+1` to each present relation.

**Absence of a relation is not automatically a third relation value.** This keeps absence of information separate from an observed negative or positive relation.

## Research layers

1. **Foundation** — entities, relations, distinction, typing.
2. **Algebra** — legal typed operations and relation composition.
3. **Structure** — paths, cycles, connectivity, boundaries, invariants.
4. **Transformation** — changes of configurations, symmetry, quotient and structural loss.
5. **Quantification** — transformation costs and derived distance/geometry.
6. **Dynamics** — state, transition, change, order, causality.
7. **Memory** — retained state that can causally affect future behavior.
8. **Emergence** — stable higher-level structures arising from lower-level relations.
9. **Self-reference** — systems that represent and act upon their own state.
10. **Consciousness research** — an explicit hypothesis layer built on the previous levels, never assumed as a primitive.

## Working chain

`distinction → relation → configuration → structure → path → transformation → invariant → equivalence → quotient → metric candidate → dynamics → memory → self-model → feedback → emergence`

This chain is a research decomposition, not a theorem.

## Current mathematical decision

Path concatenation is defined as the primary sequential operation. The sign-product on `{−1,+1}` is also defined as a valid closed summary algebra:

`(+,+)→+`
`(+,-)→-`
`(-,+)→-`
`(-,-)→+`

However, a formal counterexample shows that reducing a path to its sign-product can erase intermediate organization and change predicted future behavior under an explicit transition rule.

Therefore:

`PATH CONCATENATION ≠ SIGN-PRODUCT REDUCTION`.

The sign-product is a **summary**, not a universal information-preserving definition of relation composition. Primitive relation reduction remains open.

## Transformation-derived geometry

A first baseline has now been derived: if primitive transformations flip relation signs at unit cost, the minimum transformation cost is a genuine metric on the fixed finite relation-sign space. It is the discrete Hamming/hypercube geometry of that chosen representation.

This is a baseline, not a physical-space derivation. The general Ω metric remains open until costs, transformations, symmetries and quotient compatibility are tested without artificial fixed-slot assumptions.

## Existing Ω research integrated into this language

The Ω-Lab already contains relevant experimental branches:

- Ω-0: minimal reconstruction of internal order and functional memory;
- Ω-MEM: functional and predictive memory;
- Ω-INF: composition versus organization;
- Ω-B: internal dynamics and control experiments;
- Ω-Lab structural work: connectivity, cycles, stability and transitions.

The behavioral-equivalence experiments show that equal current observations can hide different transition structure, and that equal entity-state composition can hide different relational organization with different future trajectories under an explicit propagation rule.

The topology/structure experiments further show that equal counts, degree sequence and selected aggregate graph statistics can hide different path organization.

Point/boundary experiments support limited relational core/interface formation in tested models but do not establish a unique Point-like object.

## Method

`define → derive → implement → execute → verify → compare → falsify → record`

Every serious claim must state its status:

- **Definition** — introduced by the language.
- **Derivation** — follows from definitions and accepted rules.
- **Observation** — obtained from an executed experiment.
- **Hypothesis** — proposed explanation requiring tests.
- **Theorem** — formally proved inside the specified system.
- **Empirical law** — repeatedly supported by independent observations under stated conditions.

## Important rule

Ω-Math must not become a new notation for old mathematics by assumption. We first define typed objects and their legal compositions, then investigate which familiar mathematical structures emerge from them.

Ordinary arithmetic must not be used to silently identify entity values with relation values.

## v0.3 formal core

### Typed objects

`TYPE_SYSTEM.md` defines the object types, legal compositions and forbidden silent coercions.

### Paths and composition

`PATH_ALGEBRA.md` and `RELATION_COMPOSITION.md` define path concatenation and distinguish it from primitive relation reduction.

`RESULT_RELATION_COMPOSITION_001.md` records the four signed cases, algebraic properties of the scalar summary, and the information-loss counterexamples.

### Transformations

`TRANSFORMATION.md` defines transformations, composition, identity, inverse where applicable, symmetry, change, structural loss and candidate transformation-cost distance.

### Invariants

`INVARIANTS.md` defines invariance relative to an explicitly named transformation family and establishes label permutation as a mandatory representation control.

### Behavioral equivalence

`BEHAVIORAL_EQUIVALENCE.md` defines finite-horizon behavioral equivalence relative to observations, inputs/interventions, transition rules and horizon. `EXPERIMENT_PATH_DYNAMICS_001.md` demonstrates why restricted path summaries cannot be assumed behavior-sufficient.

### Quantitative structure

`GEOMETRY_FROM_TRANSFORMATION.md` defines transformation-derived distance and its metric conditions. `EXPERIMENT_METRIC_001.md` gives the first explicit metric baseline.

## Current open problem

The relation-composition milestone is closed at the level that can be justified:

- path composition is defined;
- sign-product is derived as a scalar summary;
- sign-product is rejected as a universal information-preserving relation law;
- primitive relation reduction remains open.

The next central problem is **general transformation geometry**: allow relation addition/removal and entity-state changes, define principled costs, test symmetry and quotient compatibility, and determine whether a stable geometry can emerge without importing physical space by assumption.

## Long-term question

Can the language provide a common formal framework for describing physical, biological, cognitive and social systems while preserving falsifiability and comparison with established mathematics and science?

If it cannot, the failure is a valid result.

## Repository structure

- `FOUNDATION.md` — primitive ontology and typed syntax.
- `ALGEBRA.md` — operations, composition and candidate algebraic laws.
- `TYPE_SYSTEM.md` — typed object system and legal/illegal coercions.
- `PATH_ALGEBRA.md` — paths, path composition and path profiles.
- `RELATION_COMPOSITION.md` — relation-composition candidates and decisions.
- `RESULT_RELATION_COMPOSITION_001.md` — current composition result.
- `STRUCTURE.md` — graphs, paths, cycles, boundaries and structural quantities.
- `TRANSFORMATION.md` — transformations, symmetry, quotient-related change and derived distance.
- `INVARIANTS.md` — invariants and symmetry framework.
- `GEOMETRY_FROM_TRANSFORMATION.md` — route from transformation cost to derived geometry.
- `EXPERIMENT_METRIC_001.md` — first transformation-derived metric baseline.
- `DYNAMICS.md` — state, change, order, causality and memory.
- `EMERGENCE.md` — hierarchy, self-reference and consciousness hypotheses.
- `GLOSSARY.md` — controlled vocabulary.
- `RESEARCH_MAP.md` — mapping between Ω-Math and existing Ω experiments.
- `EXPERIMENT_PATH_DYNAMICS_001.md` — formal dynamic counterexample to restricted path-profile sufficiency.
- `EXPERIMENT_INVARIANT_001.md` — invariant/transformation test.
- `STATUS.md` — current research state and dependency-ordered open questions.

## Status

**Ω-Math v0.3 — typed structural core, tested path/composition layer, and first transformation-derived metric baseline.**

No claim in this repository should be promoted from hypothesis to established fact without explicit evidence.
