# Transformation Structure and Quotients — Adversarial Stack v1.0

Date: 2026-09-09

## Objective

Continue the relation → path → composition → transformation stack one level deeper. Test deterministic finite transformations as first-class objects, their composition, identity, covariance under relational isomorphism, conjugacy invariants, completeness limits, and the exact conditions under which a quotient can itself carry a well-defined transformation.

The goal is not to manufacture a scalar fundamental law. The goal is to identify the strongest structure that survives formal adversarial testing and to mark precisely where information is lost.

## Model

A deterministic transformation on a finite state set E is a map

`T : E → E`.

Composition is

`(T ∘ U)(x) = T(U(x))`.

A relabelling/isomorphism `P` transports T by conjugation:

`T' = P ∘ T ∘ P⁻¹`.

A quotient map `q : E → Q` supports an induced transformation only if there exists `T_Q` such that

`q ∘ T = T_Q ∘ q`.

Equivalently, every pair of states identified by q must remain identified after applying T.

## Results

### T1 — Transformation identity

The identity map `I(x)=x` satisfies both-sided identity under composition.

Tested exhaustively for all finite maps for n ≤ 4.

Result: PASS.

### T2 — Transformation composition associativity

`(T ∘ U) ∘ V = T ∘ (U ∘ V)`.

Exhaustive/random finite-map checks were run for n ≤ 4.

Result: PASS.

This is an algebraic property of function composition, not an empirical physical discovery.

### T3 — Conjugation covariance

For every tested transformation pair and permutation P:

`P(T ∘ U)P⁻¹ = (PTP⁻¹) ∘ (PUP⁻¹)`.

Random tests: n ∈ {3,4,5,6}, 500 cases per size.

Result: PASS, zero failures.

Thus the transformation algebra is representation-covariant under relabelling.

### T4 — Conjugacy invariants

The following quantities remain unchanged under relabelling/conjugation:

- image size `|Im(T)|`;
- number of fixed points;
- for bijections, cycle-length multiset.

Random tests: n ∈ {4,5,6}, 500 transformations per size.

Result: PASS, zero failures.

### T5 — Cycle structure is complete for permutations

For bijective transformations, two finite permutations are conjugate exactly when they have the same cycle-length multiset.

Exhaustive enumeration for n=4 produced 5 conjugacy classes, and each cycle type corresponded to exactly one conjugacy class.

Result: PASS for the finite permutation case.

Important boundary: this completeness result is for permutations/bijections, not arbitrary non-bijective transformations.

### T6 — Simple scalar invariants are not complete for arbitrary transformations

Counterexample at n=4:

`T1 = (0,0,0,1)`
`T2 = (0,0,1,1)`

Both have image size 2 and one fixed point, but they are not conjugate.

Result: FAIL for completeness of the pair `(image size, fixed-point count)`.

Therefore scalar summaries cannot in general recover transformation structure.

### T7 — Quotient/congruence condition

A quotient `q` can carry a well-defined induced transformation only when

`x ~ y  ⇒  T(x) ~ T(y)`.

Counterexample partition:

`{0,1}` and `{2,3}`.

Transformation:

`T=(0,2,2,3)`.

States 0 and 1 are identified by the quotient, but their images 0 and 2 belong to different quotient classes.

Result: FAIL for induced-transform existence.

A preserving example `T=(1,1,3,3)` satisfies the condition.

Result: PASS for the congruence criterion.

### T8 — Information-preserving versus information-destroying transformation

Relabelling is bijective and preserves the complete transformation structure up to conjugacy.

A general quotient is many-to-one and can destroy distinctions. When the congruence condition fails, the transformed quotient cannot be defined without adding extra information or changing the semantics.

Result: structural distinction CONFIRMED.

### T9 — Functional-graph structure

Every finite deterministic transformation can be represented as a directed functional graph: each node has exactly one outgoing edge. Its structure consists of directed cycles with rooted in-trees feeding into them.

The pair `(image size, fixed-point count)` is therefore only a coarse projection. For arbitrary transformations, a complete structural classification requires the full functional-graph isomorphism type (equivalently a canonical form), not a single scalar.

Result: SUPPORTED as the correct structural direction; no claim of a physical invariant.

## Adversarial synthesis

The transformation layer survives all formal tests that should survive:

`state → transformation → composition → identity → conjugation`.

The next boundary is equally clear:

`quotient → induced transformation`

is not automatic. It requires a congruence/information-preservation condition.

Likewise:

`scalar summary → full transformation`

is not reversible in general.

For permutations, cycle structure is a complete invariant of conjugacy. For arbitrary deterministic maps, the natural complete object is the functional-graph isomorphism class rather than a scalar statistic.

## Promotion decision

### Ω-Math

PROMOTE as a formal structural layer:

- transformations are typed maps between declared state spaces;
- composition and identity are explicit;
- representation changes act by conjugation/isomorphism;
- invariants are properties of transformation isomorphism classes;
- quotient transformations require an explicit congruence condition;
- information loss is a declared semantic event, not an accidental implementation detail.

### FUNDAMENT

DO NOT PROMOTE as an empirical/universal physical law.

Nothing in this stack establishes that physical reality must instantiate deterministic finite transformations, nor that any particular transformation invariant is universal.

## Strongest surviving statement

The deepest current Ω-Math object is increasingly clear:

`typed state → relation → path/composition → transformation → isomorphism class → invariant`

with an explicit rule:

`information-preserving map → covariance/isomorphism may be transported; information-destroying quotient → structure survives only if a congruence condition is satisfied.`

This is a stronger foundation than searching for one privileged scalar.

## Next hard gate

The next adversarial test should be the same construction for nondeterministic/relational transformations and then for weighted transformations, checking whether the same composition/congruence/isomorphism architecture survives without silently importing probability, time, energy, or metric assumptions.
