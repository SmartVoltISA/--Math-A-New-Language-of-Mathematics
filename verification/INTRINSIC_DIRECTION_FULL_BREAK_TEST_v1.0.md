# Intrinsic Direction — Full Break Test v1.0

## Objective
Test whether directional information can be promoted from a derived response observable to a universal intrinsic relational invariant.

## Tests
1. **Direct relation level** — preserve explicit directed relation data. Direction is directly present and therefore not an emergent invariant; it is part of the declared relation.
2. **Reachability/path-existence level** — remove weights and retain only whether a path exists.
3. **Representation changes** — node relabelling and positive scaling of response values.
4. **Information-loss counterexample** — compare a directed cycle with its symmetric reachability closure.

## Hard counterexample
For any strongly connected directed cycle with N >= 3, every ordered pair is reachable. The transitive reachability matrix is therefore the all-ones matrix (up to the diagonal convention), which is symmetric, despite the original edge relation being strictly directed.

Example: edges i -> (i+1) mod N. The original adjacency matrix satisfies A != A^T, while its reachability closure satisfies Q = Q^T.

Thus direction is not recoverable from path existence/reachability alone.

## Interpretation
This does **not** refute directed relations in Ω-Math. It establishes a strict information boundary:

- explicit relation orientation can carry direction;
- derived reachability can erase it;
- therefore no claim of a universal direction invariant may rely only on connectivity/reachability.

The normalized antisymmetric response component N(R) remains a valid mathematical derived object of a declared response matrix, with previously verified covariance/invariance laws. It is not a proof of a fundamental physical arrow.

## Decision
**FUNDAMENTARY PHYSICAL PROMOTION: REJECTED.**

**Ω-Math derived invariant: RETAINED.**

The next admissible foundation candidate must be defined at the typed relation/transformation level and must survive an explicit information-preserving equivalence test. Any operation that discards orientation must be treated as lossy rather than invariant-preserving by default.
