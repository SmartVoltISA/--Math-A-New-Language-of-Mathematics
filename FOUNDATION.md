# Ω-Math v0.1 — Foundation

## 1. Purpose

Ω-Math starts from the smallest proposed typed vocabulary capable of separating two things that are often mixed in ordinary descriptions:

1. an entity and its state;
2. a relation and its state.

The primitive alphabet is therefore:

`{0, 1, −1, +1}`

but it is not one undifferentiated set. It contains two typed domains.

## 2. Entity domain

`E_val = {0, 1}`

An entity value describes whether the entity is in state 0 or state 1 within the chosen model.

The symbols do not yet mean physical absence and physical presence. Their meaning is model-dependent and must be defined for each application.

Write:

`eᵢ ∈ E_val`

## 3. Relation domain

`R_val = {−1, +1}`

A relation value describes one of two relation states.

At v0.1 the semantic labels are deliberately neutral:

`−1 = relation state A`

`+1 = relation state B`

Words such as attraction, opposition, support, inhibition, agreement or causation are application-level interpretations and cannot be assumed from the sign alone.

Write:

`rᵢⱼ ∈ R_val`

## 4. Type separation

The symbols can look numerically similar, but their type is part of the object.

`0 : Entity`
`1 : Entity`
`−1 : Relation`
`+1 : Relation`

Therefore:

`0 ≠ −1`
`1 ≠ +1`

in the typed language.

This is not a numerical inequality claim. It is a type distinction.

## 5. Distinguishability

For entity values define a binary distinction operator:

`D(a,b) = 0` if `a = b`
`D(a,b) = 1` if `a ≠ b`

Truth table:

`D(0,0) = 0`
`D(1,1) = 0`
`D(0,1) = 1`
`D(1,0) = 1`

Here `1` means that a distinction is present. It does not necessarily mean a count of one object.

The distinction operator is therefore an observation of difference, not ordinary addition.

## 6. Relation domain

Not every ordered pair must have a relation.

Let:

`D_R ⊆ I × I`

be the domain of present relations between entity indices.

For every `(i,j) ∈ D_R`:

`rᵢⱼ ∈ {−1,+1}`

If `(i,j) ∉ D_R`, the relation is **undefined/not present in the model**.

It is not automatically `0`.

This prevents absence of information from being silently converted into a third physical relation state.

## 7. Elementary Ω-expression

The smallest relational expression is:

`eᵢ —rᵢⱼ→ eⱼ`

or as a tuple:

`Bᵢⱼ = (eᵢ, rᵢⱼ, eⱼ)`

This is the basic typed unit of the language.

## 8. Finite Ω-system

A finite system is represented as:

`Ω = (E, R, D_R)`

where:

`E = (e₁,...,eₙ)`
`eᵢ ∈ {0,1}`
`D_R ⊆ I × I`
`R : D_R → {−1,+1}`

The system is therefore more than a list of numbers. It contains entities, relation-domain information and relation states.

## 9. State

A system state at step `t` is:

`Ω_t = (E_t, R_t, D_R,t)`

A transition is:

`Ω_t → Ω_t+1`

The transition rule is written:

`Ω_t+1 = T(Ω_t, U_t)`

where `U_t` is optional external input.

The transition operator `T` is not primitive yet. Different classes of systems require different transition laws.

## 10. Change

Do not interpret the symbol `−` in the word change as ordinary subtraction.

Define structural change as a comparison:

`ΔΩ_t = Compare(Ω_t, Ω_t+1)`

The output can record:

- entity-state changes;
- relation-state changes;
- relation births;
- relation removals;
- structural reconfiguration.

A future formal version may define a quantitative change measure, but v0.1 does not assume one.

## 11. Higher-level entity

A stable substructure may be represented as a higher-level entity.

Let:

`ω ⊆ Ω`

be a substructure satisfying a chosen stability criterion.

A coarse-graining map may then be defined:

`C(Ω) = Ω'`

where one or more substructures in `Ω` become entities in `Ω'`.

This is the formal entry point for emergence.

It is a hypothesis that stable higher-level entities can be derived this way; it is not assumed to hold for every system.

## 12. Minimal principles

### Principle P1 — Typed distinction

Entity states and relation states are different mathematical types.

### Principle P2 — Relation requires a domain

A relation value is assigned only where a relation is present or explicitly modeled.

### Principle P3 — Structure is relational

A system's structure depends on the configuration of its relations, not only on the multiset of entity values.

### Principle P4 — Change is comparison

A change is determined by comparing system states, not by assuming an external numerical difference operator.

### Principle P5 — Emergence requires a criterion

A higher-level entity must be identified by an explicit structural rule; visual or semantic intuition is insufficient.

## 13. What remains undefined

The following are deliberately open:

- composition of relation states;
- identity relation;
- inverse relation;
- path equivalence;
- relation conservation;
- metric/distance;
- probability;
- energy-like quantities;
- physical interpretation;
- consciousness.

These must be derived, defined or rejected in later versions.

## 14. Research constraint

No familiar mathematical object is imported as fundamental merely because it is convenient.

Instead ask:

`Can this object be defined from the typed Ω primitives?`

If yes, derive it.

If not, add the smallest necessary primitive and document why.

## 15. Current status

This document defines the foundation only. It does not claim that the four symbols constitute the ontology of nature.
