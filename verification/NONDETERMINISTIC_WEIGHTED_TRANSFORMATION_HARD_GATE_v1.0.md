# Nondeterministic + Weighted Transformation — Hard Gate v1.0

Date: 2026-09-09

## Objective

Test whether the structural stack survives extension from deterministic transformations to nondeterministic relations and weighted transformations without silently importing probability, physical time, energy, or metric assumptions.

## Model

A nondeterministic transformation is a relation `T ⊆ E × E`. Composition is relational composition.

A weighted transformation is represented by a matrix over an explicitly declared algebra. Two tested algebras were max-min and min-plus:

`(A ⊗ B)_ij = max_k min(A_ik,B_kj)` for max-min;

`(A ⊗ B)_ij = min_k (A_ik+B_kj)` for min-plus.

No probabilistic, temporal, energetic, or spatial interpretation is assigned to the entries.

## Results

### H1 — Nondeterministic composition covariance

For random Boolean relations, composition remained covariant under simultaneous node relabelling.

Sizes: `n ∈ {3,4,6,8}`; 500 random pairs per size.

Result: PASS, zero failures.

### H2 — Nondeterministic associativity

Relational composition satisfied associativity for all tested random triples.

Result: PASS, zero failures.

This follows from ordinary relational composition and is a formal structural property, not an empirical physical law.

### H3 — Weighted max-min composition

Random real-valued matrices were tested under max-min composition.

Sizes: `n ∈ {3,5,8}`; 300 triples per size.

Associativity: PASS.

Relabelling covariance: PASS.

### H4 — Weighted min-plus composition

Random real-valued matrices were tested under min-plus composition.

Sizes: `n ∈ {3,5,8}`; 300 triples per size.

Associativity: PASS.

Relabelling covariance: PASS.

The operation is algebraically valid without assigning its values the meaning of distance, energy, time, or probability.

### H5 — Weight semantics boundary

The same numerical weight can be interpreted differently depending on the declared algebra and observation semantics.

Therefore:

`weight ≠ probability`;

`weight ≠ time`;

`weight ≠ energy`;

`weight ≠ distance`.

A physical interpretation requires an additional declaration and empirical bridge.

Result: CONFIRMED.

### H6 — Nonlinear reparameterisation counterexample

Min-plus path comparison is not invariant under arbitrary monotone reparameterisation of edge values.

Example:

Direct edge: `0→2 = 9`.

Two-edge path: `0→1 = 2`, `1→2 = 3`.

Original additive values: `2+3=5 < 9`.

After square-root reparameterisation: `sqrt(2)+sqrt(3) ≈ 3.146 > sqrt(9)=3`.

Thus an ordering induced by a weighted composition law depends on the declared algebra/scale convention.

Result: FAIL for universal weight-coordinate invariance.

### H7 — Probability does not emerge automatically

A normalized nonnegative weight vector can be converted into a probability distribution, but that is an additional semantic operation. The relational structure itself does not select that normalization uniquely.

Result: NOT PROVEN / semantic choice required.

### H8 — Time does not emerge automatically

Composition depth counts transformation steps, but no physical duration follows from the count alone. Reparameterising or rescaling the step index leaves the formal structure intact.

Result: NOT PROVEN.

### H9 — Energy does not emerge automatically

Positive weights can be interpreted as costs, but the formal weighted algebra supplies no physical units or conservation law identifying them with energy.

Result: NOT PROVEN.

### H10 — Metric does not emerge automatically

Min-plus composition can produce shortest-path costs, but symmetry, triangle inequality, non-degeneracy and physical locality require separate conditions. Therefore a weighted path cost is not automatically a physical metric.

Result: NOT PROVEN universally.

## Adversarial synthesis

The architecture survives the extension:

`state → relation → nondeterministic transformation → weighted transformation → composition → isomorphism/covariance`.

What does not survive is the assumption that numerical weights possess a unique physical meaning.

The hard boundary is:

`formal weight → physical quantity`

requires an explicit semantic map plus empirical validation.

## Promotion decision

### Ω-Math

PROMOTE as a formal structural layer:

- nondeterministic transformations as relations;
- weighted transformations over declared algebras;
- composition and associativity;
- covariance under isomorphism;
- explicit separation of algebra from interpretation.

### FUNDAMENT

DO NOT PROMOTE any particular weight semantics.

No evidence here establishes probability, physical time, energy, distance, or a universal metric as consequences of the relational formalism alone.

## Strongest surviving statement

The strongest current abstraction is not a particular number or physical unit. It is:

`typed state → relation → transformation → composition → declared algebra → invariant/covariant structure`.

Physical quantities may be realized as semantic structures on top of this layer, but they are not obtained for free.

## Next hard gate

The next test is to examine whether a common abstract structure can simultaneously support multiple algebras and whether there is a principled criterion selecting an algebra from observable relational behavior rather than from human convention.
