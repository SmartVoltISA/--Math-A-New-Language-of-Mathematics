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
5. **Dynamics** — state, transition, change, order, causality.
6. **Memory** — retained state that can causally affect future behavior.
7. **Emergence** — stable higher-level structures arising from lower-level relations.
8. **Self-reference** — systems that represent and act upon their own state.
9. **Consciousness research** — an explicit hypothesis layer built on the previous levels, never assumed as a primitive.

## Working chain

`distinction → relation → configuration → structure → path → transformation → invariant → equivalence → quotient → dynamics → memory → self-model → feedback → emergence`

This chain is a research decomposition, not a theorem.

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

## v0.2 formal core

### Typed objects

`TYPE_SYSTEM.md` defines the object types, legal compositions and forbidden silent coercions.

### Paths

`PATH_ALGEBRA.md` defines path concatenation separately from the still-open problem of reducing a path to a primitive relation. This prevents path structure from being replaced by an unjustified sign arithmetic.

### Transformations

`TRANSFORMATION.md` defines transformations, composition, identity, inverse where applicable, symmetry, change, structural loss and candidate transformation-cost distance.

### Invariants

`INVARIANTS.md` defines invariance relative to an explicitly named transformation family and establishes label permutation as a mandatory representation control.

## Current open problem

The next central algebraic question remains relation composition.

For example, given:

`A —(+1)→ B —(+1)→ C`

what, if anything, is the relation from `A` to `C`?

Likewise:

`(+1) ∘ (+1)`
`(+1) ∘ (−1)`
`(−1) ∘ (+1)`
`(−1) ∘ (−1)`

must not be assigned values merely because ordinary arithmetic suggests an answer. Path concatenation is already defined; primitive relation reduction remains an experimental question.

## Long-term question

Can the language provide a common formal framework for describing physical, biological, cognitive and social systems while preserving falsifiability and comparison with established mathematics and science?

If it cannot, the failure is a valid result.

## Repository structure

- `FOUNDATION.md` — primitive ontology and typed syntax.
- `ALGEBRA.md` — operations, composition and candidate algebraic laws.
- `TYPE_SYSTEM.md` — typed object system and legal/illegal coercions.
- `PATH_ALGEBRA.md` — paths, path composition and path profiles.
- `STRUCTURE.md` — graphs, paths, cycles, boundaries and structural quantities.
- `TRANSFORMATION.md` — transformations, symmetry, quotient-related change and derived distance.
- `INVARIANTS.md` — invariants and symmetry framework.
- `DYNAMICS.md` — state, change, order, causality and memory.
- `EMERGENCE.md` — hierarchy, self-reference and consciousness hypotheses.
- `GLOSSARY.md` — controlled vocabulary.
- `RESEARCH_MAP.md` — mapping between Ω-Math and existing Ω experiments.
- `STATUS.md` — current research state and dependency-ordered open questions.

## Status

**Ω-Math v0.2 — typed structural core under active research.**

No claim in this repository should be promoted from hypothesis to established fact without explicit evidence.
