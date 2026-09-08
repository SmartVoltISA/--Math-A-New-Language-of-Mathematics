# Ω-Math v0.9 — Implementation Conformance

## Boundary

The reference runtime implements the declared finite/structural semantics without adding primitive mathematical meaning.

| Area | Runtime status |
|---|---|
| EntityState `{0,1}` | IMPLEMENTED |
| RelationState `{-1,+1}` | IMPLEMENTED |
| Typed relation-domain guard | IMPLEMENTED |
| Path / ordered concatenation | IMPLEMENTED |
| Empty-path identity | IMPLEMENTED |
| Exact path equality | IMPLEMENTED |
| Sign summary | IMPLEMENTED as derived summary |
| State comparison | IMPLEMENTED |
| Transformation | IMPLEMENTED |
| Observation wrapper | IMPLEMENTED |
| Finite behavior | IMPLEMENTED |
| Nondeterministic branching | IMPLEMENTED |
| Reachability | IMPLEMENTED |
| Task-relative reduction sufficiency | IMPLEMENTED |
| Invariant check | IMPLEMENTED |
| Quotient-distance finite construction | IMPLEMENTED as candidate |
| Metric verification | IMPLEMENTED |
| Horizon / internal order | IMPLEMENTED |
| Feedback/coarse/retain hooks | IMPLEMENTED as semantic hooks |
| Probability | EXTERNAL |
| Physical time | EXTERNAL |
| Physical energy | EXTERNAL |
| Universal CAUSE primitive | NOT ADMITTED |
| Primitive relation composition | NOT ADMITTED |
| Primitive relation identity/inverse | NOT ADMITTED |

## Important status

This is a **reference implementation**, not a claim that every natural-language statement in the repository has been mechanized. The remaining gap is formal machine-readable conformance for every canonical document and every historical experiment.

The correct next increment is to encode each experiment as a deterministic executable test vector, with frozen inputs, expected outputs and explicit failure codes.
