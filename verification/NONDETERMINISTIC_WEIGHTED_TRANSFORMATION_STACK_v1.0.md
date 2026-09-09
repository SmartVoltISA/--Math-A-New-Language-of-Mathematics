# Nondeterministic + Weighted Transformation Stack — Adversarial Verification v1.0

Date: 2026-09-09

## Objective

Extend the transformation layer beyond deterministic maps. Test nondeterministic relational transformations and nonnegative weighted transformations while explicitly checking that probability, time, energy, and metric assumptions are not introduced implicitly.

## Model

A nondeterministic transformation is a relation `T ⊆ E × E`. Its composition is relational composition:

`T ∘ U = {(x,z) : exists y, (x,y) in U and (y,z) in T}`.

A weighted transformation is a nonnegative matrix `W`, with ordinary matrix composition `W2 W1` as the declared weighted path aggregation rule. No probabilistic normalization is assumed.

## Results

### N1 — Nondeterministic composition associativity

Boolean relational composition was tested on 5000 random triples for n=5.

Result: PASS, zero failures.

This follows from existential relational composition and is a formal algebraic property, not an empirical physical law.

### N2 — Nondeterministic covariance under relabelling

For random relations A,B and random node permutations P:

`(PAP^T) ∘ (PBP^T) = P(A ∘ B)P^T`.

5000 random pairs were tested for n=6.

Result: PASS, zero failures.

### N3 — Weighted composition associativity

For nonnegative real matrices A,B,C:

`(AB)C = A(BC)`.

1000 random triples of 5×5 matrices were tested. Maximum observed relative numerical error was below `5e-16`.

Result: PASS.

### N4 — Weighted covariance under relabelling

Simultaneous permutation of source/target labels preserves matrix composition up to conjugation.

Result: PASS for the tested finite representations.

### N5 — Positive global weight scaling

For positive scalars a,b:

`(aA)(bB) = ab(AB)`.

2000 random cases with scale factors spanning 10^-3 to 10^3 were tested using relative numerical error.

Result: PASS; maximum relative error below `5e-16`.

Important: this is algebraic homogeneity of the declared weighted composition. It does NOT identify weight with energy, time, probability, or physical magnitude.

### N6 — Normalization is a semantic operation, not a neutral step

Row normalization changes weighted composition semantics. A two-state counterexample showed that normalizing factors before composition can produce a different transformation from composing raw weights and normalizing afterward.

Result: normalization must be explicitly typed as a transformation. It cannot be treated as representation-free bookkeeping.

### N7 — Probability boundary

A nonnegative weight matrix becomes a probability transition operator only after additional constraints such as row normalization and a stochastic interpretation are declared.

Result: probability is NOT implied by nonnegative weights.

### N8 — Time boundary

Weighted composition contains no intrinsic clock or ordering parameter beyond the compositional order supplied by the model.

Result: physical duration is NOT implied.

### N9 — Energy boundary

A positive weight has no intrinsic physical unit or conservation law in this formal system.

Result: physical energy is NOT implied.

### N10 — Metric boundary

Weighted paths can support path-cost or path-strength constructions, but a metric requires additional properties and a declared interpretation. Symmetry and triangle inequality do not follow from arbitrary directed weights.

Result: physical/geometric distance is NOT implied.

## Adversarial synthesis

The architecture survives the extension:

`state → relation → nondeterministic relation → weighted relation → composition → transformation → isomorphism/covariance → declared invariant`.

The same information boundary remains: quotienting or normalization can destroy or alter structure unless preservation conditions are explicit.

Weights remain a distinct formal type. They become probability, time, energy, or metric only through additional semantics that must be declared and tested.

## Promotion decision

### Ω-Math

PROMOTE as a formal structural extension:

- nondeterministic transformations are relations;
- weighted transformations are typed weighted relations;
- composition is explicit;
- relabelling acts covariantly;
- normalization is an explicit semantic transformation;
- physical interpretations are not silently inferred from algebraic form.

### FUNDAMENT

DO NOT PROMOTE as a physical law.

The stack establishes formal compatibility, not physical ontology.

## Strongest surviving statement

The strongest current structure is not a privileged scalar:

`typed state → relation → path/composition → transformation → representation change → declared invariant`

with explicit boundaries for information loss and semantic interpretation.

No probability, physical time, physical energy, or metric is required by the formal algebra itself.

## Status

SUPPORTED — formal Ω-Math structural layer.

NOT PROVEN — universal physical realization.
