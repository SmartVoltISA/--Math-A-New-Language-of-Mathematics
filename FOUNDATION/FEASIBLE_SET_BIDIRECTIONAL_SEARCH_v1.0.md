# Ω-Math Foundation — Feasible Set & Bidirectional Search v1.0

Status: Ω-MATH METHODOLOGY / EXTENSION

## Purpose

The feasible set makes the bidirectional methodology operational without promoting a physical interpretation to a primitive.

A search does not begin by asking which named physical object is wanted. It begins with declared constraints and asks which admissible structures satisfy them.

## Forward feasible set

For a declared goal `G` and structural constraint family `K_G`, define:

`F_G = { C ∈ A | K_G(C) = true }`

where `A` is the explicitly declared admissible configuration domain.

The feasible set may contain zero, one, or many candidates. Non-uniqueness is information, not failure.

## Reverse feasible set

For an observation `O` and an observation/measurement operator `Obs`, define the observation-compatible set:

`F_O = { C ∈ A | Obs(C) ≈ O }`

The compatibility relation `≈` must be declared together with tolerances, noise model, resolution, and measured observables. No hidden physical assumptions may enter through `≈`.

## Bidirectional intersection

When a goal and an observation are both available, candidate structures are restricted by:

`F* = F_G ∩ F_O`.

If `F* = ∅`, the current structural assumptions, constraints, or observation model are incompatible.

If `|F*| > 1`, the evidence does not identify a unique structure and further discriminating constraints are required.

If a unique candidate exists under the declared domain, it is a unique candidate only relative to those declarations; uniqueness must not be promoted to ontological identity.

## Structural signature

For candidate `C`, define a declared signature:

`Σ(C) = (I(C), B(C), P(C), T(C), …)`

where the components are selected invariants, boundary/incidence information, path or propagation properties, transformation behavior, and other explicitly declared structural observables.

Two independently produced signatures may be compared before assigning names:

`Σ_forward ↔ Σ_reverse`.

Agreement supports a correspondence hypothesis; disagreement is a falsification or OPEN result depending on the predeclared criteria.

## Search with cost

If several candidates satisfy the constraints, a secondary objective may select among them:

`C* ∈ argmin_{C ∈ F*} J(C)`.

`J` is a declared mathematical objective or transformation cost. It is not physical energy merely because it has a numerical value or is minimized.

The same discipline applies to marginal cost:

`ΔJ/Δconstraint` is a structural sensitivity measure unless an independent physical correspondence has been established.

A decreasing cost, reinforcement, stability, or recurrence is therefore not by itself evidence of causality or physical law.

## Reverse construction protocol

`physical observation`

`→ observable quantities`

`→ declared compatibility relation`

`→ structural constraints`

`→ feasible set`

`→ candidate structures`

`→ invariants/signature`

`→ comparison`

`→ falsification / correspondence hypothesis`

The physical name of a phenomenon is withheld from the structural search whenever a blind reconstruction is possible.

## Forward construction protocol

`goal`

`→ required structural properties`

`→ admissible domain`

`→ feasible set`

`→ candidate generation`

`→ transformation/cost analysis`

`→ invariants/signature`

`→ physical correspondence test`

The forward and reverse procedures are independent until their signatures are compared.

## Required controls

Every executable feasible-set experiment should declare before execution:

1. admissible domain `A`;
2. goal constraints `K_G`;
3. observation operator `Obs`, if used;
4. compatibility/tolerance rule `≈`;
5. objective/cost `J`, if used;
6. primary signature `Σ`;
7. positive and negative controls where applicable;
8. exclusion criteria;
9. stopping rule;
10. status vocabulary: `PASS`, `FAIL`, `OPEN`, `HYPOTHESIS`, `INVALID`.

## Information-loss gate

A reduction used to construct or compare feasible sets is admissible for task `F` only when:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

Otherwise the reduction can merge candidates that are distinguishable for the declared task and must not be treated as an equivalence.

## Boundaries

This methodology does not derive:

- physical ontology;
- physical units;
- physical energy from abstract cost;
- physical time from transition count;
- causality from correlation or optimization;
- uniqueness of a physical entity from structural uniqueness;
- a physical law from a mathematical identity.

Those require separate correspondence and empirical validation.

## Research status

This document defines a search and comparison methodology. It is not a theorem about nature and does not modify the Ω-Math v0.9 primitive vocabulary.

The intended research loop is:

`DEFINE → PREREGISTER → SEARCH → COMPARE → FALSIFY → VALIDATE → RECORD`.
