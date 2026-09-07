# Ω-Math v0.1 — Language Study

The language itself must be studied. This document records recurring structures, hidden assumptions and places where Ω concepts may duplicate earlier work.

## 1. First discovery: value is not identity

If two entities both have state `1`, then:

`e₁ = 1`
`e₂ = 1`

does not imply:

`e₁ = e₂`.

The entities are distinguished by their indices/identity, while `0` and `1` are their current states.

Therefore Ω-Math requires two levels:

`identity: i ∈ I`

`state: eᵢ ∈ {0,1}`.

This is essential. Otherwise a system containing many `1` states collapses into a single value and loses structure.

## 2. The same four symbols participate in different roles

The language is not simply a four-value number system.

`0,1` are entity-state values.

`−1,+1` are relation-state values.

A third operation may return a structural object rather than one of these four values.

This means Ω-Math is closer to a typed relational calculus than to a four-symbol arithmetic.

## 3. Recurring structure found in earlier Ω work

The following pattern appears repeatedly:

`state → difference → transition → retained trace → future effect`.

Other recurring structures are:

`relations → configuration → stable structure`

`structure → higher-level entity`

`multiple paths → redundancy/constraint`

`cycle → possible feedback`

`perturbation → recovery → stability measure`

`state representation → prediction`

These should be treated as candidate reusable operators/patterns rather than repeatedly renamed concepts.

## 4. Composition and organization repeat across domains

A fixed set of elements can be reorganized while preserving composition.

A fixed relation pattern can be applied to different entity states.

Therefore two independent axes recur:

`what exists`

and

`how it is organized`.

This is the conceptual bridge between Ω-INF, network structure and the new mathematical language.

## 5. Memory repeatedly appears as retained difference

Across Ω-0 and Ω-MEM, the useful distinction is not merely “something is stored.”

The recurring pattern is:

`past state → retained internal trace → later constraint on behavior`.

This suggests a candidate Ω abstraction:

`memory = causally effective retained distinction`.

This remains a definition candidate, not a universal law of memory in nature.

## 6. Stability repeatedly appears as persistence under change

A structure is not called stable merely because it exists.

It must survive a specified class of perturbations or transitions.

Candidate form:

`stability = persistence of a specified structural property under specified change`.

This gives a common language for network lifetime, recovery and persistent patterns.

## 7. Cycles repeatedly appear but must not be overinterpreted

A cycle is a structural fact in a graph representation.

A feedback loop is a dynamic claim.

A causal loop is a stronger causal claim.

These three must remain separate:

`cycle ≠ feedback ≠ causality`.

## 8. Numbers may be derived observables

The same structural object can produce different numerical measurements:

- size;
- edge count;
- degree;
- path count;
- cycle rank;
- lifetime;
- entropy;
- prediction accuracy.

Therefore a number is often an observation of a structure under a measurement rule.

This supports the research direction:

`structure → measurement → number`

rather than assuming every number is a primitive of the ontology.

## 9. Important danger: hidden imported mathematics

The language can accidentally import ordinary mathematics through words such as:

`sum`
`difference`
`distance`
`time`
`probability`
`energy`
`information`
`identity`
`causality`.

Whenever one of these is used, the repository must state whether it is:

- primitive;
- defined;
- borrowed as a comparison tool;
- derived;
- experimentally estimated.

## 10. Important danger: semantic drift of signs

`+1` and `−1` can easily acquire different meanings in different experiments.

At the foundation they mean only two relation states.

An experiment may define them as attraction/repulsion, activation/inhibition, agreement/opposition, etc., but that mapping must be recorded explicitly.

## 11. Important danger: absence versus negative relation

There are three logically different conditions:

`relation absent`

`relation present with state −1`

`relation present with state +1`.

Collapsing these into `−1,0,+1` changes the ontology of the model.

The foundation therefore keeps relation absence in the relation domain and reserves `−1,+1` for actual relation states.

## 12. Candidate reusable operator families

The language currently suggests these operator families:

`DIST(a,b)` — distinguish states.

`REL(i,j,r)` — assert a relation.

`PATH(R)` — compose an ordered chain of relations.

`CONFIG(E,R)` — construct a system configuration.

`TRANS(Ω_t,Ω_t+1)` — represent a transition.

`COMPARE(Ω_a,Ω_b)` — measure structural change.

`RETAIN(Ω_t)` — preserve state information.

`COARSE(Ω)` — map stable substructures to higher-level entities.

`MODEL(Ω)` — construct an internal representation.

`FEEDBACK(Ω,MODEL)` — allow the representation to affect subsequent state.

These are operator candidates. Their exact domains and laws must be formalized before they become part of the core algebra.

## 13. What should become the Ω-Math core

The smallest reusable core currently appears to be:

`identity`
`state`
`distinction`
`relation`
`configuration`
`transition`
`retention`
`comparison`.

Everything above this level should be tested as a derived construction.

## 14. Study rule

Whenever a new phenomenon is encountered, first ask:

1. Is this already represented by an existing Ω concept?
2. Is it a new state of an existing object?
3. Is it a new relation between existing objects?
4. Is it a new operation on existing structures?
5. Is it genuinely a new primitive?

Only the fifth case justifies expanding the foundation.

## 15. Current conclusion

The language already contains more than the four symbols.

Its real content is the typed grammar that connects them.

Therefore the next research target is not “more symbols.” It is discovering the smallest consistent grammar and algebra that reproduces the recurring structures already observed across Ω research.
