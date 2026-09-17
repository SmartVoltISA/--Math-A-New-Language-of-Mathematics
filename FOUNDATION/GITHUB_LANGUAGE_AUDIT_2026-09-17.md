# Ω-Math — Cross-Repository Language Audit

**Date:** 2026-09-17
**Scope:** accessible SmartVoltISA repositories and Ω/SPACE research relevant to the mathematical language
**Status:** AUDIT / CONSOLIDATION MAP
**Core rule:** this document does not promote a research hypothesis to a primitive merely because it appears repeatedly elsewhere.

## 1. Purpose

Search the wider repository ecosystem for structures already developed outside Ω-Math that may be necessary, useful, or testable extensions of the language.

The audit separates:

- **CORE** — already admitted by Ω-Math v0.9;
- **DERIVED** — constructible from the core under declared semantics;
- **EXTENSION CANDIDATE** — useful typed addition requiring tests;
- **SEMANTIC MODULE** — task-dependent machinery;
- **EMPIRICAL BRIDGE** — physical correspondence requiring independent validation;
- **HYPOTHESIS** — research claim not yet established;
- **NOT ADMITTED** — deliberately excluded from the minimal core.

## 2. Verified cross-repository findings

### 2.1 Relations have candidate internal properties

`Omega-lab-.--.-/research/RELATIONS/README.md` and `EDGE-PROPERTIES.md` independently enumerate candidate relation properties:

- existence/absence;
- direction;
- length/distance;
- area/thickness/volume;
- strength;
- stiffness;
- elasticity/recoverability;
- density;
- persistence/lifetime;
- capacity/bandwidth;
- propagation delay;
- orientation/anisotropy;
- relation state/history;
- creation/modification/destruction cost.

The research explicitly states that none is fundamental yet and requires one-property-at-a-time minimality testing.

**Language implication:** Ω-Math currently represents a relation as a typed edge without a canonical internal property record. A future extension should therefore permit a **typed relation annotation/state layer** without making any physical property primitive.

Proposed abstract shape:

`Relation = (source, target, relation_state, optional_declared_properties)`

This is an extension candidate, not a v0.9 primitive change.

### 2.2 Strength and stiffness are distinct

The relation research explicitly separates:

- strength = threshold before failure/rupture;
- stiffness = response to deformation/change.

A relation may therefore be strong but compliant, or weak but stiff.

**Language implication:** one generic scalar called `weight` is insufficient for all relation behavior. If relation properties are admitted later, each property needs its own type and operational definition.

### 2.3 Directional response / anisotropy already exists

The relation research defines a directional response candidate:

`C(theta)`

with anisotropy when:

`C(0) != C(pi/2)`.

The same repository contains physical/structural work where orientation changes propagation or response.

**Language implication:** orientation should be representable as a declared relation/structure property, but should not be conflated with directedness. `direction`, `orientation`, and `anisotropy` are distinct concepts.

### 2.4 Structural potential / energy-like quantity is already a research branch

The ENERGY branch contains the structural-potential hypothesis and a planned experimental family around it. The central question is whether a static relational configuration can have a measurable quantity predicting or constraining available transformations before a transition.

The branch explicitly keeps three alternatives open:

`relation → change → energy`

`relation/structure → stored potential → change → release`

`relation → configuration → transition rule → conserved quantity`

It also explicitly warns that transformation cost is not physical energy by definition.

**Language implication:** `POTENTIAL` is a strong extension candidate as a mathematical candidate observable over configurations, but not a primitive physical energy variable. The correct abstraction is closer to:

`POTENTIAL : Configuration × TransitionFamily → Measure/Order`

or an equivalent declared functional once a concrete semantics is fixed.

### 2.5 Cost already exists in Ω-Math, but cost functional selection is not yet closed

Ω-Math `OPERATOR_TABLE.md` defines:

`COST : Transformation → [0,∞]`

and derives structural distance from minimal declared transformation cost.

The newly added feasible-set extension defines:

`F_G = {C ∈ A | K_G(C)=true}`

`F_O = {C ∈ A | Obs(C) ≈ O}`

`F* = F_G ∩ F_O`

and candidate selection:

`C* ∈ argmin_{C∈F*} J(C)`.

The remaining question is not whether cost exists, but how a **cost functional/objective** is selected, normalized, compared, and tested against alternative functionals.

**Language implication:** `OBJECTIVE` / `FUNCTIONAL` should remain an extension candidate. It must not silently become scalar arithmetic. Its domain, codomain, admissible transformations and comparison rule must be declared.

### 2.6 Marginal cost is not yet established as a law

The wider research chain discussed in Ω work is:

`closure → feasible set → minimal cost → cost functional → ??? → marginal cost ↓ → reinforcement → polarity`

The repository audit found reinforcement experiments, but no verified Ω-Math derivation establishing that decreasing marginal cost necessarily produces reinforcement or polarity.

In particular, ENERGY experiments include reinforcement models, while at least one repository record explicitly notes that an independent toy implementation did not reproduce the reported numerical values exactly.

**Status:** `OPEN / HYPOTHESIS`, not a language law.

**Language implication:** the language needs a way to represent **sensitivity / marginal change of an objective under a constraint or intervention**, but the causal/reinforcement interpretation must remain external.

Candidate form:

`MARGINAL(J, constraint) → declared sensitivity`

with no automatic implication `MARGINAL↓ ⇒ REINFORCEMENT`.

### 2.7 Reinforcement + memory produces channelization in research models

ENERGY experiments E-ENERGY-0031–0033 study competing paths, limited resources, reinforcement and memory. One result reports strong localization/channelization when memory and reinforcement are present, while a later independent check states that exact numerical values were not independently reproduced.

**Language implication:** the language should be able to express:

- resource allocation;
- competing admissible paths;
- update/reinforcement rule;
- retention/history dependence;
- observable concentration/channelization.

These are dynamics/semantic modules, not primitives.

### 2.8 Memory is more than storage

The wider Ω work represents memory as preserved dependence on previous states and also studies hysteresis/return-point behavior. This is stronger than merely storing a snapshot.

**Language implication:** `MEMORY` should be represented as a relation between past state/history and future transition behavior, e.g. a retention rule or state extension, rather than as an undifferentiated data container.

Ω-Math already has `RETAIN` as a framework operator and `MODEL`/`FEEDBACK` as framework concepts. No new primitive is required at present.

### 2.9 Order is distinct from physical time

The TIME research explicitly distinguishes a precedence relation/order over transitions from physical duration. Ω-Math already has `ORDER` as an internal ordered index and `TIME_PHYSICAL` as an empirical bridge.

**Language implication:** retain this separation. Do not add physical time to the core merely because ordered paths exist.

### 2.10 Event is present in the wider system foundation but absent as an Ω-Math operator

`SYSTEM-FOUNDATION` defines a universal substrate containing:

`IDENTITY + STATE + EVENT + RELATION + PROVENANCE + HISTORY`.

`CICADA-LANGUAGE` likewise treats states, events, relations, transitions and provenance as a communication language for SPACE organs.

**Language implication:** an `EVENT` construct may be useful for the *operational/meta-language* around Ω-Math, especially provenance and transition records. It is not yet necessary as a primitive mathematical object because `TRANSFORM`, `ORDER` and transition sequences already describe the mathematical change layer.

Recommended status: `SEMANTIC / META-LANGUAGE CANDIDATE`.

### 2.11 Provenance is important but belongs outside the mathematical core

The system-wide foundation treats provenance and change lineage as first-class audit requirements. This is directly compatible with Ω-Stand's evidence discipline.

**Language implication:** provenance should be attached to observations, experiments, mappings and claims, not smuggled into the primitive mathematical ontology.

### 2.12 Graph-native algebra is already developed separately

`CICADA-LANGUAGE/02_SEMANTICS/MINIMAL_GRAPH_ALGEBRA_v0.1.md` and `GRAPH_NATIVE_MODEL_v0.1.md` establish a separate graph-native semantic layer with tests.

Ω-Math already treats paths and relations as first-class. The CICADA layer is therefore a useful implementation/communication target, not evidence that graph algebraic operations must be added to the Ω-Math primitive core.

### 2.13 Information has a structurally useful but nontrivial layer

Ω-Lab information experiments distinguish quantities such as symbol entropy, conditional entropy, unique n-grams and compression behavior. Some quantities remain invariant under reconstruction while others change.

**Language implication:** information cannot be reduced to one generic scalar. The language can support declared observables over structures, but information-theoretic measures remain external mathematical constructions until their semantics are explicitly selected.

### 2.14 Invariants, operators, equivalence and quotient are already substantially represented

The Ω-Math repository already contains canonical definitions for:

`DIST, INCIDENT, PATH, PATH_EQ, CYCLE, CONCAT, SIGN, COMPARE, TRANSFORM, OBSERVE, EQUIV, QUOTIENT, INVARIANT, BEHAVIOR, COST, DISTANCE, QUOTIENT_DISTANCE, SYMMETRY, RETAIN, ORDER, HORIZON, BRANCH, REACH, MODEL, FEEDBACK, COARSE`.

The frontier closure also explicitly handles nondeterminism, infinite horizon, quotient geometry conditions, continuous states, probability, causal intervention, physical time, energy and emergence.

**Language implication:** do not duplicate these concepts. The main missing layer is not another large list of operators; it is the typed connection between configuration properties, feasible sets, objective/functional selection, sensitivity, and empirical correspondence.

## 3. Candidate language layers after the audit

### Layer A — Minimal core

Already closed in v0.9:

`distinction → typed state → relation → configuration → path → transformation → invariant/equivalence → quotient`

### Layer B — Structural descriptors

Candidate extension:

`relation → declared property → response → persistence/capacity/orientation/etc.`

Properties remain typed and operationally defined.

### Layer C — Search / feasibility

Now explicitly represented:

`constraints → admissible domain → feasible set → observation-compatible set → intersection`

### Layer D — Selection / optimization

Partially represented:

`feasible set → objective/functional → minimal candidate`

Still open:

- objective choice;
- normalization;
- competing objectives;
- sensitivity/marginal cost;
- degeneracy and Pareto-like cases.

### Layer E — Dynamics / adaptation

Already represented across Ω work as framework modules:

`transition → feedback → retention → reinforcement → redistribution → emergent pattern`

The causal status of each arrow must remain model-specific.

### Layer F — Observation / correspondence

Now represented by the bidirectional methodology:

`physical observation → observables → compatibility → structural candidate → signature → falsification`

and the reverse:

`goal/structure → feasible candidates → predicted observables → physical correspondence test`.

### Layer G — Meta-language / provenance

Wider system architecture supplies:

`event + provenance + history + authority + evidence + decision lineage`.

This should support the research language without being inserted into the minimal mathematical ontology.

## 4. Important missing concepts identified

The audit finds five concrete frontiers worth formalizing next:

1. **Typed relation-property model** — how a relation acquires declared measurable properties without making them primitives.
2. **Objective/functional layer** — how a feasible candidate is scored/selected and how competing objectives are represented.
3. **Sensitivity/marginal layer** — how change in objective is measured with respect to constraints/interventions.
4. **Degenerate/multi-optimum selection** — how the language represents a feasible set with multiple equally valid minima without inventing uniqueness.
5. **Event/provenance bridge** — how mathematical transitions become auditable records without confusing record order with physical time.

## 5. Concepts explicitly NOT promoted

The following remain outside the minimal core unless independent tests justify a change:

- physical energy;
- physical time;
- physical force;
- physical mass;
- physical space;
- probability as a primitive;
- causality from correlation or optimization;
- polarity as a universal primitive;
- reinforcement as a universal law;
- stiffness/strength as primitive relation properties;
- graph weight as physical quantity;
- uniqueness as physical identity.

## 6. Current synthesis

The strongest complete architecture supported by the audited material is:

`DISTINCTION`
`↓`
`RELATION`
`↓`
`CONFIGURATION / STRUCTURE`
`↓`
`DECLARED PROPERTIES`
`↓`
`CONSTRAINTS`
`↓`
`FEASIBLE SET`
`↓`
`OBSERVATION COMPATIBILITY`
`↓`
`CANDIDATE STRUCTURES`
`↓`
`INVARIANTS / SIGNATURES`
`↓`
`OBJECTIVE / COST FUNCTIONAL`
`↓`
`MINIMAL / PARETO / DEGENERATE SOLUTIONS`
`↓`
`SENSITIVITY / MARGINAL RESPONSE`
`↓`
`TRANSFORMATION / FEEDBACK`
`↓`
`RETENTION / REINFORCEMENT`
`↓`
`NEW STRUCTURE`
`↓`
`OBSERVATION`
`↺`

This is a research architecture, not a claim that every arrow is a theorem.

## 7. Decision

**Do not expand Ω-Math v0.9 core yet.**

The audit indicates that the next mathematically meaningful extension is the **objective/functional + sensitivity + multi-optimum layer**, because the feasible-set work has already created the admissible search domain and the wider Ω research already supplies cost, potential, reinforcement and competing-path experiments.

The relation-property layer should be specified in parallel as an extensible typed annotation mechanism, not as a list of physical primitives.

## 8. Verification limitation

This audit used the accessible GitHub connector and repository/file search. Some private repositories are not code-search indexed; their existence and top-level descriptions were visible, but their complete file contents were not necessarily searchable through the connector. Therefore this document is a **maximal verified audit of accessible/searchable material today**, not a proof that every private file in the account was exhaustively read.

Local execution of Ω-Math conformance remains separately unverified when the environment cannot reach GitHub/DNS.
