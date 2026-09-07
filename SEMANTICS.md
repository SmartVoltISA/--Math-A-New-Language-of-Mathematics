# Ω-Math v0.4 — Semantic Rules

## 1. Meaning is typed

A symbol has meaning only together with its declared type and position in an expression.

`0:EntityState` is not `0:RelationState` and relation absence has no primitive numeric value.

## 2. Identity

Entity identity is represented by `id`. State is a separate field.

Therefore:

`(i,0) ≠ (j,0)` when `i ≠ j`.

Equal state does not imply equal entity.

## 3. Relation semantics

A relation sign has only the semantic meaning assigned by the current model. The signs `−1` and `+1` do not intrinsically mean attraction, repulsion, causation, truth, energy or force.

## 4. Direction

A directed relation retains source and target order. Reversal is a distinct transformation unless an explicit symmetry identifies the two directions.

## 5. Absence

If `(i,j) ∉ D_R`, the relation is absent/undefined in the current relational domain. It is not silently converted into a third relation state.

## 6. Path semantics

A path preserves:

- endpoint order;
- intermediate entities;
- relation order;
- relation signs;
- path length;
- multiplicity when multiple paths exist.

A scalar summary is allowed only as a declared map from the path to another type.

## 7. Change semantics

Change is a relation between two states/configurations. It records which declared components differ and how.

A quantitative magnitude of change must be separately defined.

## 8. Transformation semantics

A transformation is admissible only when its domain, action and output are declared. Invertibility is a property to test, not a default assumption.

## 9. Observation semantics

An observation is a mapping that intentionally forgets some distinctions. Equal observations imply only observational equivalence, not identity.

## 10. Equivalence semantics

An equivalence relation must specify what is considered irrelevant for the task. Different observations, horizons or interventions may induce different equivalence classes.

## 11. Quotient semantics

A quotient must specify how retained entities, relations and paths map into quotient objects. Merging names alone is insufficient.

## 12. Causality

Temporal succession or correlation is not causality. A causal claim requires a declared intervention or equivalent counterfactual criterion.

## 13. Memory

A stored value is not automatically memory in the functional sense. Memory requires persistence plus a demonstrated later effect under a specified test.

## 14. Emergence

A macro-object is an emergence candidate only when:

1. a lower-level construction is declared;
2. a higher-level identification map is explicit;
3. persistence/stability is tested;
4. the macro-level has a declared property or behavior;
5. controls show the result is not a measurement artifact.

## 15. Geometry

Distance is not primitive in the current core. A candidate distance must arise from a declared transformation family and cost. Physical space cannot be identified with the resulting mathematical metric without an independent bridge.

## 16. Semantic priority rule

When two interpretations conflict, the more explicit typed definition wins over intuition, analogy or ordinary arithmetic.

## Status

`DEFINED / CORE SEMANTICS`
