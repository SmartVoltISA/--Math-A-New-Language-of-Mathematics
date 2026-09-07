# Ω-Math v0.4 — Controlled Vocabulary

This glossary is canonical for the current language. A term must not silently change meaning between experiments.

## Entity
A distinguishable modeled position with an identity and a current state.

## Entity identity
The identifier that distinguishes one entity from another. Identity is not the same as state.

## Entity state
The current value of an entity: `0` or `1`.

## Relation
A directed modeled connection between ordered entity positions. Its primitive state belongs to `{−1,+1}`.

## Relation state
The current signed state of a relation: `−1` or `+1`.

## Relation domain
The set of ordered pairs for which relations are present or explicitly modeled. Absence from the domain is not a relation value.

## Distinction
A declared comparison showing whether two selected objects differ. At the primitive entity-state level, `D(a,b)=0` for equality and `D(a,b)=1` for difference.

## Configuration
A complete declared arrangement of entities and relations at one modeling step.

## State
A configuration together with explicitly retained additional variables such as memory or control state.

## Structure
The organization of entities and relations in a configuration.

## Path
An ordered connected sequence of relations. Order and intermediate structure are retained.

## Path summary
A derived map from a path to a smaller description. A summary is not automatically an equivalence.

## Cycle
A path satisfying a declared return criterion. A cycle alone does not imply causality.

## Transformation
A declared mapping between states/configurations.

## Transformation family
A declared set/class of admissible transformations used to define invariants, symmetry or distance.

## Invariant
A property preserved by a specified transformation family.

## Symmetry
A transformation that preserves an object exactly or up to a declared equivalence.

## Observation
A mapping from a state to a selected description that may intentionally erase distinctions.

## Observational equivalence
Two objects with equal outputs under a declared observation map.

## Behavioral equivalence
Equivalence of declared future observations under a specified transition rule, input/intervention class and horizon.

## Quotient
A construction that identifies objects under a declared equivalence and specifies how retained structure maps to quotient structure.

## Reduction
A map from a richer representation to a smaller or differently organized representation.

## Sufficiency
A property of a representation that it preserves all information required for a declared task or behavior.

## Information loss
A distinction present in the original representation that is not recoverable from the reduced representation for the declared task.

## Transition
A rule or observed mapping from one state to another.

## Change
A declared comparison between states. It is not automatically ordinary subtraction.

## Memory
Retained internal state that persists and can affect later behavior or comparison.

## Functional memory
Memory demonstrated to have a measurable later effect under an appropriate intervention or controlled comparison.

## Predictive state
A retained representation sufficient for a specified prediction task under specified conditions.

## Causality
A relation supported by a declared intervention/counterfactual criterion. Succession or correlation alone is insufficient.

## Self-model
An internal representation generated from, and causally used with respect to, the system's own state.

## Feedback
A recurrent dependency in which later system state influences subsequent dynamics that return to an earlier process or variable.

## Emergence
A candidate higher-level structure or behavior arising from lower-level organization under an explicit identification and validation criterion.

## Geometry
A mathematical structure derived from declared relations, transformations, costs or equivalences. Physical geometry is a separate hypothesis.

## Metric
A function satisfying the metric axioms on a declared domain. In Ω-Math it is derived only after its transformation/cost basis is specified.

## Hypothesis
A proposition proposed for testing but not established.

## Derivation
A result that follows from stated definitions and accepted rules.

## Theorem
A formally proved proposition inside the specified mathematical system.

## Executed result
A result obtained from an explicit finite computation or construction.

## Validation
Evidence that a result passed predefined checks and controls.

## Reproduction
An independent execution reproducing a documented result under the same declared protocol.

## Artifact
A feature that can create an apparent result without the intended mechanism.

## Ω-system
A system represented using typed Ω primitives and derived structures.

## Ω-level
A descriptive scale obtained by explicit coarse-graining or structural aggregation.

## Ω-Math
The evolving formal language developed in this repository. It is a research program, not an assumed theory of nature.
