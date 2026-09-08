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

## First bridge completed

`REL-EXP-001-TIME-VARYING-RELATION` has been bridged at the **qualitative snapshot** level. The Ω-Math execution reproduces the representable directed-sign observation (`-1`) and records provenance through `ResearchRecord`.

This is intentionally classified **PARTIAL**: the source experiment also contains time windows, stochastic dynamics, continuous coupling magnitude, estimator recovery and shuffling control. Those are not represented by the minimal Ω-Math primitives and are not silently imported.

See `bridges/RELATION_EXP_001_BRIDGE_v1.0.md` and `bridges/test_relation_exp_001_bridge.py`.

## Next target

Select a RELATION-LAB experiment whose complete declared observable fits the current Ω-Math boundary. The stronger research target remains directed geometry without reciprocity, but any adapter must first prove that its observables are representable without adding physical primitives.

## Non-goals

Do not add physical time, physical energy, probability, causality, spatial ontology, or autonomous interpretation to Ω-Math merely to simplify integration.
