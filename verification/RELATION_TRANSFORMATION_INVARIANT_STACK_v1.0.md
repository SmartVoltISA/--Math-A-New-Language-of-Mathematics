# Relation → Transformation → Invariant — Full Adversarial Stack v1.0

Date: 2026-09-09

## Objective

Test whether a deeper candidate than response-level reciprocity survives when defined directly on declared relations, paths, composition and transformations.

The stack deliberately separates structural covariance from information loss. A property is not promoted merely because an implementation preserves it; it must survive admissible representation changes and must have explicit counterexamples when an operation destroys the relevant information.

## Stack

### S1 — Relation under node relabelling

For a relation/support matrix A and permutation matrix P:

`A' = P A P^T`

The relation structure is preserved up to isomorphism.

Random tests: n ∈ {4, 6, 8, 12}, 400 cases per size.

Result: PASS, zero failures.

### S2 — Composition covariance

Boolean relational composition:

`A ∘ B = support(A B)`.

Under the same relabelling:

`(PAP^T) ∘ (PBP^T) = P(A ∘ B)P^T`.

Result: PASS, zero failures across 1200 random pairs.

### S3 — Associativity of relational composition

For Boolean support relations:

`(A ∘ B) ∘ C = A ∘ (B ∘ C)`.

Result: PASS, zero failures across 1200 random triples.

This is a structural algebraic property of the declared composition, not a discovered physical law.

### S4 — Endpoint/reachability quotient

Hard counterexample:

A: 0→1→2
B: 0→1→2 plus 0→2

Their transitive closures are identical while their direct relation sets differ.

Result: FAIL for completeness.

Therefore reachability/path-endpoint information cannot reconstruct the underlying relation structure.

### S5 — Path identity

A branching graph with 0→1→3 and 0→2→3 contains two distinct paths with the same endpoints.

Result: path identity contains information that endpoint-only representation loses.

Therefore `path ≠ endpoint pair` and path quotienting must be explicit.

### S6 — Direction through reachability

A directed 4-cycle has directed edges but its transitive closure is the complete relation. The closure is symmetric.

Result: FAIL for universal direction preservation.

Direction is not recoverable after an information-destroying reachability quotient.

### S7 — Transformation covariance

A transformation represented on the same labelled relational state is transported by conjugation under node relabelling. Structural predicates expressed through relational composition therefore transform covariantly.

Result: PASS for the tested finite representations.

### S8 — Positive scalar response scaling

Response-level normalized antisymmetric objects remain invariant under positive global scaling, but this property does not transfer automatically to arbitrary dynamical-law scaling.

Result: CONDITIONAL.

The observable and its units must be declared before claiming scale invariance.

### S9 — Coarse-graining

Merging nodes can erase distinctions, direct relations and directional information. Previous random-graph tests found substantial non-universal retention of response nonreciprocity.

Result: FAIL for universal coarse-graining invariance.

Coarse-graining is admissible only when its information-preservation conditions are explicitly stated.

### S10 — Observation/operator dependence

A dynamic observation operator can create asymmetry even from a symmetric underlying relation structure.

Result: FAIL for operator-free inference.

An observed asymmetry cannot be promoted to an intrinsic relational property without a declared operator model or an operator-robust theorem.

## Synthesis

The deepest object that survives the full stack is not a scalar invariant. It is the typed relational structure together with explicit path composition and declared transformations.

The strongest safe statement is:

`relation → path → composition → transformation → derived invariant`

with covariance under relational isomorphism and explicit accounting for information-losing quotients.

This is stronger and cleaner than treating `rho(R)` or `N(R)` as universal physical objects.

## Promotion decision

### Ω-Math

PROMOTE as a **structural algebraic layer**:

- typed relations;
- explicit paths;
- composition;
- transformations;
- invariants defined on declared structures;
- explicit distinction between covariance and invariance;
- explicit information-loss/quotient boundaries.

### FUNDAMENT

DO NOT PROMOTE as an empirical/universal physical law.

Reason: the surviving composition laws are properties of the formal relational system itself, while attempts to infer a universal physical invariant fail under information-losing quotients and observation/operator changes.

## Key conclusion

A fundamental candidate cannot be accepted merely because it survives representation changes. It must also survive every admissible information-preserving transformation and fail predictably when information is deliberately destroyed.

The current stack establishes that the **structure + transformation + declared invariant** framework is robust; it does not establish a unique universal scalar or physical invariant.
