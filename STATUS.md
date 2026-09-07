# Ω-Math v0.2 — Research Status

## Current state

The foundation is written into the repository and the formal language is being treated as an object of study, not as a finished theory.

The v0.2 structural expansion adds an explicit typed object system, transformation layer, invariant/symmetry layer and path algebra layer.

## Primitive layer

### Defined

- Entity domain: `{0,1}` as state values.
- Relation domain: `{−1,+1}`.
- Type separation between the two domains.
- Entity identity/state separation `eᵢ=(i,sᵢ)`.
- Identity, state and observation distinctions.
- Explicit relation domain `D_R`.
- System configuration/state.
- Structural transition concept.
- Typed object categories.
- Path object and path concatenation.
- Transformation object and composition.
- Identity transformation.
- Invariant definition relative to a transformation family.
- Symmetry definition relative to an equivalence.

### Not yet derived

- unique primitive relation composition;
- identity relation as a relation-state primitive;
- relation inverse;
- canonical path equivalence;
- universal sufficient path profile;
- canonical metric;
- physical time;
- probability;
- energy;
- physical ontology.

## v0.2 formal expansion

### Transformation

`TRANSFORMATION.md` defines mappings between configurations/states, composition, identity, inverse where applicable, transformation classes, change, symmetry, derived transformation-cost distance and structural loss.

### Type system

`TYPE_SYSTEM.md` makes input/output types explicit and lists forbidden silent coercions. In particular:

`state 0 ≠ relation −1 ≠ relation absence`.

### Invariants and symmetry

`INVARIANTS.md` establishes that every invariant is relative to a named transformation family. Label permutation is the first mandatory representation control.

### Path algebra

`PATH_ALGEBRA.md` separates path concatenation from the still-open question of reducing a path to a primitive relation. It introduces path profiles as a testable candidate descriptor.

## Existing concepts that must NOT be reinvented

The Ω research history already contains working concepts for:

- state;
- difference/distinguishability;
- memory;
- history/trace;
- transitions;
- cycles;
- connectivity;
- stability/lifetime;
- independent paths;
- structural change;
- information versus organization;
- internal dynamics;
- experimental controls.

Ω-Math should formalize and connect these concepts rather than create duplicate names.

## Behavioral-equivalence findings

The executed constructions provide two important formal counterexamples:

1. identical current observations can hide different transition structure;
2. identical entity-state composition can hide different relational organization and therefore different future trajectories under the same explicit propagation rule.

Therefore:

`static observational equivalence ≠ behavioral equivalence`.

A behavior-preserving quotient must specify which observations, inputs and horizons it preserves.

## Structure findings

`TOPOLOGY-003` and `STRUCTURE-004` show that equal entity counts, relation counts, sign counts and selected graph statistics can still hide different path organization and different controlled dynamic responses.

Therefore aggregate graph statistics are not automatically complete state descriptions.

## Collapse findings

`EQUIV-001` shows that a structural quotient cannot be defined by vertex merging alone. A complete relational quotient needs explicit entity, relation and path mapping rules.

This gives the current collapse discipline:

`observation collapse ≠ system change`

`vertex quotient ≠ relation quotient ≠ path quotient`.

## Point/boundary findings

Executed results support, within tested models:

`relations → closure → relational separation → candidate core/interface`.

The tested closure-only, closure-plus-reconnection, closure-plus-redundancy and first combined-factor probes did **not** establish a single Point-like object. Strong closure can produce fragmentation, while strong combined mechanisms can produce near-global connectivity without a low-conductance dominant boundary.

Therefore the Point remains `OPEN` and must be searched as an intermediate regime satisfying multiple simultaneous criteria rather than as maximum closure or maximum connectivity.

## Open questions ranked by dependency

### Q1 — Relation composition

Can sequential relations be reduced to a relation without losing path information or importing ordinary arithmetic?

### Q2 — Path algebra

Which path equivalences and reductions preserve the selected structural/behavioral semantics?

### Q3 — Structural invariants

Which properties survive relabeling, permutation and representation changes?

### Q4 — Quantification

Which numbers arise naturally as measurements of Ω-structures rather than primitives?

### Q5 — Dynamics

Can transition rules be expressed entirely in relational terms?

### Q6 — Memory

Can functional memory be represented as a persistent relational structure with an intervention-tested effect?

### Q7 — Emergence

Under what conditions can a stable relation pattern become a higher-level entity?

### Q8 — Self-model

Can a system represent and causally use a model of its own state?

### Q9 — Consciousness

Do any self-model/feedback structures predict phenomena associated with consciousness better than simpler controls?

### Q10 — Physical bridge

Can the formalism reproduce independently established physical mathematics or observations without hidden imported assumptions?

## Current confidence labels

`DEFINED` = language definition.

`DERIVED` = follows formally from current rules.

`EMPIRICALLY OBSERVED` = reported by an executed experiment.

`SUPPORTED` = survived specified controls.

`OPEN` = unresolved.

`COUNTEREXAMPLE` = evidence against a stated universal claim.

`REJECTED` = claim no longer retained as valid under the documented evidence.

## Critical methodological rule

The ability to express a phenomenon in Ω-Math is not evidence that Ω-Math explains it.

`representable ≠ explained`

`correlated ≠ caused`

`stable ≠ fundamental`

`emergent candidate ≠ emergence proven`

## Next formal milestone

1. Enumerate the four length-2 signed relation cases.
2. Test candidate relation-level reductions against explicit path semantics.
3. Test associativity at lengths 3–4.
4. Construct conflicting parallel-path counterexamples.
5. Define finite-horizon behavioral equivalence precisely and test nesting.
6. Test quotient preservation of declared invariants.
7. Test whether path profiles are sufficient for the selected propagation dynamics.
8. Only then derive quantitative geometry from transformation cost.

## Physical hypotheses

`H-BH-0` — extreme relational distinguishability collapse may have a physically meaningful correspondence with characteristic black-hole behavior.

Status: `OPEN`.

No physical interpretation is accepted until an Ω quantity is defined independently, mapped to established observables, tested against controls, and used to make predictions not used in its construction.
