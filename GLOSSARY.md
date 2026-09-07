# Ω-Math v0.1 — Controlled Vocabulary

This glossary is intended to prevent the same word from acquiring different meanings in different experiments.

## Entity

A distinguishable position or unit whose modeled state belongs to `{0,1}`.

## Entity state

The current value of an entity: `0` or `1`.

## Relation

A modeled connection between ordered entity positions. Its primitive state belongs to `{−1,+1}`.

## Relation state

The current signed state of a relation: `−1` or `+1`.

## Relation domain

The set of ordered pairs for which a relation is present or explicitly modeled. Absence from the domain is not equal to relation value `0`.

## Distinction

An observable difference between two entity states. At the primitive level: `D(a,b)=0` for equality and `D(a,b)=1` for difference.

## Configuration

A complete arrangement of entity states and relations at one modeling step.

## Structure

Organization of relations and entities within a configuration.

## State

A configuration together with whatever additional variables are explicitly retained by the model.

## Transition

A rule or observed mapping from one system state to a later state.

## Change

A comparison between states. Change is not automatically ordinary subtraction.

## Path

An ordered sequence of connected relations.

## Cycle

A path satisfying the chosen return/identity criterion.

## Connectivity

A property of a representation describing whether and how entities remain mutually reachable.

## Boundary

A set of relations or structural conditions separating a selected substructure from its complement.

## Invariant

A property preserved under a specified transformation.

## Memory

Retained internal state that can causally affect later behavior or comparison.

## Functional memory

Memory demonstrated to have a measurable effect under an appropriate intervention or controlled comparison.

## Predictive state

A retained representation sufficient for a specified prediction task under specified data-generating conditions.

## Self-model

An internal representation generated from, and causally used with respect to, the system's own state.

## Feedback

A recurrent dependency in which later system state can influence subsequent dynamics that return to an earlier process or variable.

## Emergence

A candidate higher-level structure or behavior arising from lower-level organization under an explicit identification and validation criterion.

## Observation

A result obtained from a defined operation or executed experiment.

## Hypothesis

A proposition proposed for testing but not yet established.

## Derivation

A result that follows from stated definitions and rules.

## Theorem

A formally proved proposition inside the specified mathematical system.

## Validation

Evidence that a result passed the predefined checks for the experiment.

## Reproduction

An independent execution that reproduces the relevant result under the documented protocol.

## Artifact

An implementation or measurement feature that can create an apparent result without the intended mechanism.

## Ω-system

A system represented using the typed Ω primitives and their derived structures.

## Ω-level

A descriptive scale obtained by explicit coarse-graining or structural aggregation.

## Ω-Math

The evolving formal language developed in this repository. It is not assumed to be a theory of nature merely because it can model natural phenomena.
