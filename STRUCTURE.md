# Ω-Math v0.1 — Structure

## 1. From values to structure

A list of entity values is not yet a relational structure.

Example:

`E = [1,1,0,1]`

Two systems can have exactly the same entity values and completely different relations.

Therefore composition and organization are separate variables.

`composition = which entity states exist`

`organization = how entities are related`

This distinction is already central to Ω-INF research.

## 2. Directed signed relation graph

An Ω-system can be represented by:

- vertices = entity positions;
- directed edges = present relations;
- edge sign = `−1` or `+1`.

This representation is useful, but it is not declared identical to the underlying concept of relation. A graph is one representation of a relational system.

## 3. Path

A path is a sequence:

`e₀ —r₁→ e₁ —r₂→ ... —rₖ→ eₖ`

The path itself is a higher-order object. Its meaning cannot be reduced automatically to the arithmetic sum of its signs.

## 4. Cycle

A path is a cycle when its terminal entity returns to its initial entity under the chosen identity criterion.

Cycles matter because they create feedback routes and multiple paths.

The existing Ω-Lab work has already treated cycles and connectivity as structural quantities. They should therefore be integrated into Ω-Math as derived structural observables, not assumed primitives.

## 5. Connectivity

For an Ω-structure define standard graph connectivity only as a derived representation where a graph representation has been explicitly chosen.

Potential measures include:

- number of edges;
- degree distribution;
- vertex connectivity;
- edge connectivity;
- cycle rank β₁;
- number of independent paths;
- component count.

These quantities are not interchangeable.

Previous Ω experiments found cases where edge count and average independent paths were more informative for stability than β₁ alone. Those observations belong in the empirical layer and should not be promoted to universal laws without further replication.

## 6. Boundary

A boundary separates a substructure from the rest of a structure.

A candidate boundary can be represented by the set of relations crossing between two subsets:

`∂S = { relations connecting S to Ω \ S }`

The exact boundary operator remains representation-dependent in v0.1.

## 7. Stable structure

A substructure `S` is a candidate stable structure when its organization persists under a defined class of transitions.

Conceptually:

`S_t ≈ S_t+1`

but the comparison relation `≈` must be explicitly defined.

Possible stability measures include:

`lifetime(S)`

`recovery_time(S)`

`structural_similarity(S_t,S_t+k)`

No single measure is currently declared fundamental.

## 8. Higher-level entity

A structure can become an entity at a higher scale if three conditions are met:

1. it can be identified by an explicit rule;
2. it persists sufficiently to be distinguished;
3. treating it as one unit improves or preserves the description required by the task.

This gives a candidate operational definition of emergence.

## 9. Scale transition

Let:

`Ω⁰` = microscopic representation.

A coarse-graining operator produces:

`C(Ω⁰) = Ω¹`.

Repeated application gives:

`Ω⁰ → Ω¹ → Ω² → ...`

A higher-level entity is then not necessarily a new primitive. It can be a stable pattern in the lower-level relation structure.

## 10. Invariants

An invariant is a quantity or property that remains unchanged under a specified transformation.

Candidate Ω invariants include:

- component structure;
- cycle rank;
- signed path parity under a selected composition rule;
- degree sequence;
- relation counts;
- conserved labels, if a transition model proves conservation.

Every invariant must name the transformation under which it is invariant.

## 11. Structure versus interpretation

A detected cycle is an observation.

Calling it a feedback mechanism is an interpretation.

Calling it a physical causal loop is a stronger hypothesis.

Ω-Math must keep these levels separate.

## 12. Structural research program

The next structural studies should compare:

`same entities + different relations`

against

`same relations + different entity states`.

This allows us to measure what is contributed by composition and what is contributed by organization.

The goal is to determine which quantities are invariant under relabeling, permutation and representation changes.
