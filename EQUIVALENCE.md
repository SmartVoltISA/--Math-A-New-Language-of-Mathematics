# Ω-Math v0.1 — Distinction, Equivalence and Collapse

## 1. Purpose

This document develops the next formal layer:

`DIST → EQUIVALENCE → QUOTIENT → COLLAPSE`

The purpose is to define precisely what it means for two entities to remain distinct, to be treated as equivalent under a chosen observation rule, and for structural distinctions to disappear under that rule.

This layer does **not** identify structural collapse with any physical phenomenon. In particular, it does not define a black hole. Any physical interpretation is a later hypothesis requiring independent tests.

## 2. Identity and state are different

The earlier representation `eᵢ ∈ {0,1}` is insufficient if two distinct entities can occupy the same state.

Use:

`eᵢ = (i,sᵢ)`

where:

- `i ∈ I` is an identity label;
- `sᵢ ∈ {0,1}` is the state of that entity in the chosen model.

Therefore:

`e₁ = (1,1)`
`e₂ = (2,1)`

gives:

`e₁ ≠ e₂`

while:

`s₁ = s₂`.

Thus:

`different identity ≠ different state`.

This distinction is required to prevent equal state values from automatically collapsing different entities.

## 3. Three notions that must not be confused

### 3.1 Identity equality

Two entity representations are identical when their identities and relevant state data are identical under the current model.

At minimum:

`eᵢ = eⱼ ⇒ i = j`.

Identity is therefore stronger than equality of state.

### 3.2 State equality

Two entities may have equal states:

`sᵢ = sⱼ`

without being the same entity:

`eᵢ ≠ eⱼ`.

### 3.3 Observational equivalence

Two entities may be different internally but indistinguishable under a selected observation rule `O`.

Define, for a chosen observation domain:

`eᵢ ≈ₒ eⱼ  iff  O(eᵢ) = O(eⱼ)`.

The subscript is essential: equivalence depends on what is observed.

Therefore:

`eᵢ = eⱼ` is not the same statement as `eᵢ ≈ₒ eⱼ`.

## 4. Distinction operators

Keep several levels explicit until a unification is proved.

### Identity distinction

`D_I(i,j) = 0` if `i=j`, otherwise `1`.

### State distinction

`D_S(eᵢ,eⱼ) = 0` if `sᵢ=sⱼ`, otherwise `1`.

### Observation distinction

`D_O(eᵢ,eⱼ) = 0` if `O(eᵢ)=O(eⱼ)`, otherwise `1`.

These can disagree.

Example:

`D_I(e₁,e₂)=1`
`D_S(e₁,e₂)=0`
`D_O(e₁,e₂)=0`.

The two entities are distinct, occupy the same state, and are indistinguishable to the selected observer.

## 5. Candidate equivalence relation

For a fixed observation rule `O`, define:

`eᵢ ≈ₒ eⱼ  iff  O(eᵢ)=O(eⱼ)`.

Equality of observations gives the standard equivalence properties:

1. Reflexive: `e ≈ₒ e`.
2. Symmetric: `e₁ ≈ₒ e₂ ⇒ e₂ ≈ₒ e₁`.
3. Transitive: `e₁ ≈ₒ e₂` and `e₂ ≈ₒ e₃ ⇒ e₁ ≈ₒ e₃`.

Therefore `≈ₒ` is a candidate equivalence relation whenever `O` is a well-defined function.

Important: the equivalence relation is **not** declared a new primitive. It is derived from an explicitly chosen observation/coarse-graining rule.

## 6. Equivalence classes

For an entity `e`, define its observational class:

`[e]ₒ = {x ∈ E : x ≈ₒ e}`.

The set of all classes is:

`E/≈ₒ = {[e]ₒ : e ∈ E}`.

The quotient map is:

`Qₒ : E → E/≈ₒ`

with:

`Qₒ(e)=[e]ₒ`.

This is the formal operation that replaces individually distinguishable entities by classes of entities that the chosen observation cannot distinguish.

## 7. Information loss

If:

`e₁ ≠ e₂`

but:

`Qₒ(e₁)=Qₒ(e₂)`,

then the quotient representation no longer preserves that distinction.

The original structure has not necessarily changed. The representation has become less discriminating.

This distinction is fundamental:

`physical/structural change ≠ observational information loss`.

A collapse caused only by `Qₒ` is a collapse **relative to the observation rule**.

## 8. Total observational collapse

For a finite entity set `E`, total collapse under `O` occurs when:

`∀eᵢ,eⱼ ∈ E : eᵢ ≈ₒ eⱼ`.

Equivalently:

`|E/≈ₒ| = 1`.

All entities belong to one observational class.

This is a precise mathematical statement, but it does not mean that the entities have ceased to exist or that the underlying structure has physically collapsed.

## 9. Structural collapse

Entity-level collapse is not sufficient to claim structural collapse.

Let an Ω-system contain entities and relations:

`Ω=(E,R,D_R)`.

A quotient on entities can induce a quotient on relations and paths. Two originally different relations may become relations between the same quotient classes.

For example:

`e₁ → e₃`
`e₂ → e₄`

may become:

`[e₁]ₒ → [e₃]ₒ`

when:

`e₁≈ₒe₂` and `e₃≈ₒe₄`.

Distinct original edges can therefore become indistinguishable at the quotient level.

A structural collapse claim requires showing which structural distinctions are lost, not merely showing that vertex labels are merged.

## 10. Quotient of paths

A path is:

`P=(e₀,r₁,e₁,...,rₖ,eₖ)`.

Apply `Qₒ` to every entity position:

`Qₒ(P)=([e₀]ₒ,r₁,[e₁]ₒ,...,rₖ,[eₖ]ₒ)`.

Different original paths can therefore map to the same quotient path.

If:

`P₁ ≠ P₂`

but:

`Qₒ(P₁)=Qₒ(P₂)`,

then the quotient has erased a path-level distinction.

This is stronger than merely saying that two entities became equivalent.

## 11. Path multiplicity and collapse

Suppose two distinct paths connect the same original endpoints:

`P₁ : A → B`
`P₂ : A → B`

with:

`P₁ ≠ P₂`.

If the quotient makes them identical:

`Qₒ(P₁)=Qₒ(P₂)`,

then one unit of path distinguishability has been lost at the quotient level.

This matters because prior Ω research treats multiple independent paths as a structural quantity. Therefore any future collapse measure must test whether path multiplicity is preserved, reduced, or destroyed.

No numerical collapse measure is introduced yet.

## 12. Collapse kernel

For an observation map `O`, define the indistinguishability relation:

`Ker(O) = {(x,y) ∈ E×E : O(x)=O(y)}`.

This is the set of distinctions erased by the observation.

It is useful to call this the **observation kernel** rather than a physical kernel. The term is descriptive: it identifies pairs that become observationally identical.

A candidate quantitative collapse measure may later be based on the size or structure of this kernel, but such a measure is not yet fundamental.

## 13. Refinement versus collapse

Two observation rules can be compared by their ability to distinguish entities.

If `O₂` distinguishes every pair distinguished by `O₁`, and possibly more, then `O₂` is a refinement of `O₁`.

Conceptually:

`fine description → coarse description`

is a loss of distinctions, while:

`coarse description → fine description`

is a recovery of distinctions only if the discarded information is still available somewhere.

A quotient cannot reconstruct distinctions that were not retained by the representation.

## 14. Relation to standard mathematics

The construction is closely related to established mathematical ideas:

- equivalence relations partition a set into equivalence classes;
- quotient sets replace individual elements by their equivalence classes;
- graph contraction merges vertices and can merge or alter edges;
- observational equivalence appears in several areas of mathematics and theoretical computer science;
- bisimulation provides a stronger, behavior-sensitive notion of equivalence for transition systems.

Ω-Math does not claim these concepts are new. The research question is whether one of these established constructions can be derived naturally from the Ω primitives and which version is sufficient for Ω systems.

In particular, simple observational equality may be too weak for dynamic systems. Two states can look identical now but behave differently under future transitions. This motivates testing a stronger behavioral equivalence later.

## 15. Critical distinction: observation versus behavior

For a dynamic system, define two candidate notions separately.

### Static observational equivalence

`e₁ ≈ₒ e₂`

when the current observation is identical.

### Behavioral equivalence

`e₁ ≈ᵦ e₂`

only if the relevant future behavior remains indistinguishable under the specified transition and observation rules.

The second notion is substantially stronger.

Therefore:

`≈ₒ ⇒/⇐ ≈ᵦ`

must not be assumed in either direction without a defined model and proof.

This is a direct connection to the existing Ω work on state, transition, memory and internal dynamics.

## 16. Minimal collapse ladder

The current formal ladder is:

`distinct entities`

`↓`

`same state`

`↓`

`observational equivalence`

`↓`

`quotient classes`

`↓`

`path distinctions may merge`

`↓`

`structural distinctions may be lost`

Only the first five steps can be stated without additional empirical assumptions. The last step requires an explicit structural preservation test.

## 17. Black-hole hypothesis — deliberately not derived

The earlier intuition that extreme distinction collapse might be related to a black hole is recorded only as a hypothesis:

`H-BH-0:` There may exist a physically meaningful regime in which an extreme form of relational distinguishability collapse corresponds to characteristic black-hole behavior.

This hypothesis is currently **OPEN**.

To test it, Ω-Math would need to reproduce independently established observables or invariants associated with black holes, without fitting the formalism to the desired result.

The following would be required before accepting any physical connection:

1. define the Ω structural quantity independently of black-hole data;
2. derive its transformation/invariance properties;
3. establish a quantitative mapping to known physical observables;
4. compare against non-black-hole controls;
5. test predictions not used to construct the mapping.

Until then:

`distinction collapse ≠ black hole`.

## 18. Current status

### DEFINED

- identity/state separation;
- identity distinction;
- state distinction;
- observation map;
- observational equivalence;
- equivalence classes;
- quotient map;
- observation kernel;
- quotienting of entity positions in paths.

### DERIVED

- observational equivalence is an equivalence relation when generated by equality under a well-defined observation map;
- total observational collapse is equivalent to a one-class quotient;
- quotienting can merge previously distinct paths.

### OPEN

- canonical observation map;
- canonical equivalence for Ω systems;
- behavioral equivalence/bisimulation analogue;
- quotient of relations with conflicting signs;
- invariants preserved by quotienting;
- quantitative collapse measure;
- physical interpretation.

### NOT CLAIMED

- that quotient collapse changes the underlying system;
- that collapse is necessarily irreversible;
- that collapse is gravity;
- that collapse is a black hole;
- that Ω-Math has yet reproduced physical spacetime.

## 19. Next experiment

Construct the smallest counterexample family for:

`same states + different identities`

`→ observational quotient`

`→ path merging`

and test which structural quantities survive:

- component count;
- edge count;
- degree structure;
- cycle structure;
- independent path count;
- relation-sign information.

The first objective is not to obtain a dramatic result. It is to find the exact boundary between information that the quotient preserves and information that it destroys.
