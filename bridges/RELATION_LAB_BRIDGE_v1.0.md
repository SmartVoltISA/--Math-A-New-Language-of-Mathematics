# Ω-Math ↔ RELATION-LAB Bridge v1.0

**Status:** ACTIVE / RESEARCH BRIDGE

## Purpose

Define a narrow, typed interface between Ω-Math and RELATION-LAB without importing laboratory interpretations into Ω-Math primitive semantics.

## Boundary

Ω-Math provides:

- entities;
- signed directed relations;
- paths and structural operators;
- transformations and observations where declared;
- deterministic execution;
- machine-readable research records.

RELATION-LAB provides:

- hypotheses;
- experiment protocols;
- datasets / graph instances;
- interventions;
- measurements;
- experiment-specific metrics and interpretations.

The bridge carries declared structures and results. It does not promote laboratory interpretation into mathematical primitive semantics.

## Exchange contract

```text
LAB EXPERIMENT
     ↓
DECLARED MODEL
     ↓
Ω-MATH REPRESENTATION
     ↓
EXECUTION / TRANSFORMATION
     ↓
OBSERVATION
     ↓
METRIC
     ↓
RESEARCH RECORD
     ↓
LAB RESULT
```

## Required provenance

Every bridged experiment must preserve:

- experiment ID;
- hypothesis ID/version;
- source repository and revision;
- Ω-Math version;
- model declaration;
- intervention declaration;
- observation definition;
- metric and criterion;
- seed or deterministic generation rule;
- result classification;
- limitations.

## Result classes

`SUPPORT`, `COUNTEREXAMPLE`, `INCONCLUSIVE`, and `INVALID` remain distinct. A bridge must never convert `SUPPORT` into universal truth or `COUNTEREXAMPLE` into global rejection beyond the tested scope.

## First target

Use the bridge to encode one existing RELATION-LAB experiment end-to-end, then compare the Ω-Math execution result with the laboratory record. The first implementation is intentionally narrow: demonstrate provenance and reproducibility before expanding the adapter surface.

## Non-goals

Do not add physical time, physical energy, probability, causality, spatial ontology, or autonomous interpretation to Ω-Math merely to simplify integration.
