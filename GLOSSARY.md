# Ω-Math v0.9 — Controlled Vocabulary

This glossary defines the current vocabulary. Legacy documents may use older wording; the v0.9 definitions control current semantics.

## Entity
A distinguishable modeled object with identity and current state.

## Entity identity
The identifier distinguishing one entity from another. Identity is not state.

## Entity state
A primitive current value in `{0,1}`.

## Relation
A directed modeled connection between ordered entities. Its primitive state belongs to `{−1,+1}`.

## Relation state
The primitive signed state of a relation: `−1` or `+1`. It has no intrinsic physical interpretation.

## Relation domain
The set of ordered pairs for which relations are present/defined. Absence from the domain is not a relation value.

## Distinction
A declared comparison identifying equality or difference. At primitive entity-state level, `D(a,b)=0` for equality and `D(a,b)=1` for difference.

## Configuration
A declared arrangement of entities, relation domain and relations at one modeling step.

## State
A configuration together with explicitly retained variables such as memory or control state.

## Structure
The organization of entities and relations in a configuration.

## Path
An ordered compatible sequence of relations retaining endpoints, intermediate structure, relation order and states.

## Empty path
`ε_e`, the identity of compatible path concatenation. It is not a primitive relation identity.

## Path summary
A derived map from a path to a smaller description. A summary is not automatically sufficient or an equivalence.

## Sign summary
A derived scalar such as the product of relation signs along a non-empty path. It preserves only the declared property it measures and can lose organization.

## Transformation
A declared mapping between states/configurations.

## Transformation family
A declared collection of admissible transformations used for invariance, symmetry or distance.

## Invariant
A property preserved under a specified transformation family.

## Observation
A mapping that retains selected information and may erase distinctions.

## Observational equivalence
Equality under a declared observation map.

## Behavioral equivalence
Equality of declared future observations under specified dynamics, inputs/interventions, task and horizon.

## Quotient
A construction identifying objects under a declared equivalence and specifying how retained structure maps to quotient objects.

## Reduction
A map from a richer representation to a smaller/differently organized representation.

## Sufficiency
The property that a representation preserves all information required for a declared task or behavior.

## Information loss
A distinction in the original representation that is not recoverable from the reduced representation for the declared task.

## Transition
A declared rule or observed mapping from one state to another.

## Memory
Retained internal state that persists and can affect later behavior or comparison.

## Functional memory
Memory whose persistence and later functional influence are demonstrated by a controlled test.

## Predictive state
A representation sufficient for a specified prediction task under specified conditions.

## Causality
A relation supported by an explicit intervention/counterfactual criterion. Temporal succession alone is insufficient.

## Self-model
An internal representation of system state that participates functionally in subsequent dynamics.

## Feedback
A recurrent dependency in which later state influences subsequent dynamics that return to an earlier process or variable.

## Emergence
A candidate higher-level structure or behavior arising from lower-level organization under an explicit identification and validation criterion.

## Geometry
A mathematical structure derived from declared relations, transformations, costs or equivalences. Physical geometry is a separate empirical hypothesis.

## Metric
A function satisfying metric axioms on a declared domain. In Ω-Math it is admitted only after its construction and axioms are verified.

## Hypothesis
A proposition proposed for testing but not established.

## Derivation
A result following from stated definitions and accepted rules.

## Theorem
A formally proved proposition within the specified mathematical system.

## Executed result
A result obtained from an explicit finite computation or construction.

## Counterexample
A valid construction showing that a proposed universal implication fails under the stated assumptions.

## Validation
Evidence that a result passed predefined checks and controls.

## Reproduction
An independent execution reproducing a documented result under the same declared protocol.

## Artifact
A feature capable of creating an apparent result without the intended mechanism.

## Ω-system
A system represented using typed Ω primitives and declared derived structures.

## Ω-level
A descriptive scale obtained through explicit coarse-graining or structural aggregation.

## Ω-Math
The evolving formal language and research program developed in this repository. It is not assumed to be the ontology of nature.

## Status

`CANONICAL / v0.9 SYNCHRONIZED`
