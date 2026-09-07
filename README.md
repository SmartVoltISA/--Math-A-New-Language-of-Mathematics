# Ω-Math — A New Language of Mathematics

Ω-Math is an experimental mathematical language built from four primitive values with two different roles:

- `0, 1` — states of entities;
- `−1, +1` — states of relations.

The central research question is whether structure, dynamics, memory, geometry, time and higher-order phenomena can be represented or derived from relations between distinguishable entities.

This repository is a formal research program. It does not assume that nature is proven to have this ontology.

## Core distinction

The same numerical symbols must not be confused across types:

`EntityState ∈ {0,1}`

`RelationState ∈ {−1,+1}`

Therefore `0 ≠ −1` and `1 ≠ +1` as typed mathematical objects. Relation absence is a domain condition, not a third relation value.

## Minimal object

An elementary Ω-relation is:

`eᵢ —rᵢⱼ→ eⱼ`

where the endpoints are entities and `rᵢⱼ ∈ {−1,+1}`.

A finite configuration is:

`C = (E,D_R,R)`

where `D_R` is the explicit domain of present relations and `R:D_R→{−1,+1}`.

A state may additionally contain explicitly retained variables:

`S=(C,M,X)`.

## Research layers

1. **Foundation** — entities, relations, distinction, typing.
2. **Language** — syntax, semantics and operator discipline.
3. **Algebra** — legal typed operations and relation composition.
4. **Structure** — paths, cycles, connectivity, boundaries and invariants.
5. **Transformation** — changes, symmetry, quotient and structural loss.
6. **Quantification** — transformation costs and derived distance/geometry.
7. **Dynamics** — transition, order and causality.
8. **Memory** — retained state with demonstrated functional effect.
9. **Emergence** — validated higher-level organization.
10. **Self-reference / consciousness** — explicit hypothesis layers, never primitives.

## Working chain

`distinction → relation → configuration → structure → path → transformation → invariant → equivalence → quotient → metric candidate → dynamics → memory → self-model → feedback → emergence`

This is a research decomposition, not a theorem.

## Language specification

The current canonical language documents are:

- `LANGUAGE_SPEC.md` — syntax, types, signatures and extension rules.
- `SEMANTICS.md` — semantic rules and forbidden implicit meanings.
- `TYPE_SYSTEM.md` — typed object system.
- `OPERATOR_TABLE.md` — canonical operator inventory.
- `CANONICAL_EXAMPLES.md` — minimal reference expressions.
- `GLOSSARY.md` — controlled vocabulary.
- `REDUCTION_RULES.md` — information-preserving reduction discipline.

A new operator cannot become part of the core merely because it is convenient: it must have a declared signature, semantics, status, counterexample search and comparison with existing mathematics.

## Current mathematical decision

Path concatenation is the primary sequential operation:

`P ⧺ Q`.

The sign-product on `{−1,+1}` is a closed derived summary:

`(+,+)→+`
`(+,-)→-`
`(-,+)→-`
`(-,-)→+`

But a formal deterministic counterexample shows that sign-product can erase intermediate organization that changes future behavior.

Therefore:

`PATH CONCATENATION ≠ SIGN-PRODUCT REDUCTION`.

The sign-product is a **summary**, not a universal information-preserving definition of primitive relation composition.

## Reduction principle

For a task `F` and reduction `Q`, behavior/task sufficiency requires:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

If this implication fails, the reduction is information-losing for that task. This rule is central to Ω-Math: **compression is not equivalence**.

## Transformation-derived geometry

For admissible transformations `𝒯(S,S')` with declared cost `c`, define the candidate distance:

`d_c(S,S') = inf{c(T):T∈𝒯(S,S')}`.

A metric is accepted only when its axioms follow for the declared domain and transformation family. The first fixed-slot sign-flip construction gives the discrete Hamming/hypercube metric of that representation.

This is a mathematical baseline, not a derivation of physical space.

## Method

`define → derive → implement → execute → verify → compare → falsify → record`

Every serious claim must state its status:

- **Definition** — introduced by the language.
- **Derivation** — follows from definitions and accepted rules.
- **Executed** — obtained from an explicit finite construction/computation.
- **Supported** — survives specified controls.
- **Hypothesis** — proposed but unresolved.
- **Theorem** — formally proved.
- **Counterexample** — demonstrates failure of a universal claim.
- **Rejected** — no longer accepted under documented evidence.

## Important rules

Ω-Math must not become a new notation for old mathematics by assumption.

Do not silently identify:

- entity state with relation state;
- absence with a relation value;
- path with a scalar;
- observation with identity;
- stability with emergence;
- correlation with causality;
- connectivity with physical space;
- transformation irreversibility with physical irreversibility.

## Existing Ω research integrated into this language

The repository incorporates earlier Ω work on internal order, functional/predictive memory, composition versus organization, internal dynamics, connectivity, cycles, stability, transitions and Point/boundary experiments.

Those experiments remain evidence about the tested models, not automatic evidence about nature.

## Current open problems

- canonical primitive relation composition;
- canonical path equivalence;
- universal sufficient path profile;
- unrestricted transformation metric;
- quotient-induced geometry;
- physical time;
- probability;
- energy;
- physical ontology;
- task-independent emergence criterion;
- causal self-model;
- physical bridge and independent predictions.

## Repository structure

- `FOUNDATION.md`
- `LANGUAGE_SPEC.md`
- `SEMANTICS.md`
- `TYPE_SYSTEM.md`
- `OPERATOR_TABLE.md`
- `CANONICAL_EXAMPLES.md`
- `ALGEBRA.md`
- `PATH_ALGEBRA.md`
- `RELATION_COMPOSITION.md`
- `REDUCTION_RULES.md`
- `STRUCTURE.md`
- `TRANSFORMATION.md`
- `INVARIANTS.md`
- `GEOMETRY_FROM_TRANSFORMATION.md`
- `DYNAMICS.md`
- `EMERGENCE.md`
- `BEHAVIORAL_EQUIVALENCE.md`
- `GLOSSARY.md`
- `RESEARCH_MAP.md`
- experiment/result documents
- `STATUS.md`
- `LICENSE.md`

## Status

**Ω-Math v0.4 — typed relational language with explicit semantics, reduction discipline, tested path/composition layer and transformation-derived metric baseline.**

No claim should be promoted from hypothesis to established fact without explicit evidence.
