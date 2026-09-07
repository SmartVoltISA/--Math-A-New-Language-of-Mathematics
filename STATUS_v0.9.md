# Ω-Math v0.9 — Research Status

The v0.9 frontier pass closes the remaining language-design gaps.

## Closed or derived

- exact path equality;
- empty-path identity for path concatenation;
- infinite-horizon equivalence as the intersection of finite-horizon equivalences;
- explicit nondeterministic successor-set semantics;
- task-parameterized trace, safety, reachability and branching semantics;
- infinite-run fairness/liveness as explicit predicates;
- quotient pseudodistance with metric conditions;
- declared continuous-state extensions;
- explicit causal intervention semantics.

## Intentionally non-primitive

Primitive relation composition, relation identity and relation inverse are not necessary primitives. Relations are atomic edges; path concatenation is their sequential composition. Any collapse of a path to a single relation must be an explicit abstraction.

## External bridges

Probability, physical time, physical energy and physical ontology are not derived from the minimal primitives. They require independent semantics or empirical calibration.

## Final boundary

**Ω-Math v0.9 is formally complete as a minimal typed relational language for its declared domain.**

This does not claim universal mathematical completeness or a completed physical theory. The repository preserves counterexamples wherever a tempting universal reduction fails.

Canonical frontier record: `FRONTIER_CLOSURE_v0.9.md`.
