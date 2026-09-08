# Ω-Math — Experiment GEOMETRY-SIGN-001

## Question
Can two configurations have identical declared geometry/topology while producing different behavior when the dynamics is sensitive to relation signs?

## Claim under test
`same geometry ≠ same relational state ≠ same behavior`.

More precisely, a geometry descriptor that omits relation signs is not sufficient for a sign-sensitive task unless sign information is separately retained or proven irrelevant.

## Construction
Use the same directed graph topology in both configurations:

- entities: `A,B,C`
- relations: `A→B`, `B→C`, `A→C`
- identical entity states
- identical edge set, degree data, connectivity, path lengths and cycle rank

Configuration `C+` has signs:

`A→B : +1`, `B→C : +1`, `A→C : +1`.

Configuration `C−` has the same topology but:

`A→B : +1`, `B→C : +1`, `A→C : −1`.

Thus all unsigned geometric/topological descriptors are identical while one relation-state channel differs.

## Declared dynamics
At each step, for every directed edge `u→v`, propagate a token from `u` to `v` only when the edge sign is `+1`. A `−1` edge blocks propagation. The rule is deterministic and explicitly sign-sensitive.

Initial state: one token at `A`.

## Prediction
At horizon 1, both configurations reach `B`. At horizon 1, `C+` also reaches `C` directly, while `C−` does not. Therefore their reachable-state sets differ immediately.

## Verification
The construction is finite and directly enumerable. The unsigned graph is identical by construction. The sign-labelled graphs differ, and the declared transition operator distinguishes them.

For the chosen initial condition and horizon 1:

`Reach(C+) = {A,B,C}`

`Reach(C−) = {A,B}`

Therefore:

`geometry(C+) = geometry(C−)`

but

`Behavior(C+) ≠ Behavior(C−)`

under the declared sign-sensitive dynamics.

## Result
**SUPPORTED COUNTEREXAMPLE.** An unsigned geometry/topology descriptor is not universally sufficient to represent Ω-Math configurations. Relation signs carry independent information and can affect behavior.

This does not imply that geometry is useless. It implies that sufficiency is task- and dynamics-relative:

`Q(x)=Q(y) ⇒ F(x)=F(y)`

must be established for the declared task before `Q` may replace the full state for that task.

## Boundary
This experiment does not establish a physical interpretation of `+1` or `−1`. It establishes only a formal distinction inside the declared Ω-Math dynamics.
