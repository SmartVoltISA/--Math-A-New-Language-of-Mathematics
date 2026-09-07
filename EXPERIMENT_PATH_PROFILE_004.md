# Ω-Experiment PATH-PROFILE-004 — Same Source-Distance Profile, Different Future Behavior

## Status

`EXECUTED / FORMAL COUNTEREXAMPLE UNDER DECLARED FINITE MODEL`

## 1. Question

Can two non-isomorphic relational systems have the same source-distance profile while producing different future behavior under the same deterministic transition rule?

## 2. Systems

Use four entities, all initially in state `1`. Every structural edge is represented by two opposite `+1` Ω-relations.

### ΩP₄-A

`A-D, B-C, B-D, C-D`

Source: `B`.

Distances from `B`:

`B=0, C=1, D=1, A=2`.

Profile:

`{0,1,1,2}`.

Degree sequence:

`(3,2,2,1)`.

The vertices `B,C,D` form a triangle.

### ΩP₄-B

`A-B, A-D, B-C, C-D`

Source: `A`.

Distances from `A`:

`A=0, B=1, D=1, C=2`.

Profile:

`{0,1,1,2}`.

Degree sequence:

`(2,2,2,2)`.

There is no triangle; the graph is a four-cycle.

The graphs are non-isomorphic because their degree sequences differ.

## 3. Common transition rule

The following deterministic local rule is fixed before execution:

> At each step, a state-1 entity becomes state 0 at the next step iff it has at least one state-0 neighbor **and** the entity belongs to a 3-cycle (triangle) in the current relational structure. State 0 persists.

The rule is intentionally structural. It tests whether a source-distance profile can determine behavior when another relational property is relevant to the transition.

## 4. Execution

Initial perturbation:

`t0`: source = `0`; all other entities = `1`.

### ΩP₄-A

`t0: B=0, C=D=A=1`.

`C` and `D` each have a zero-valued neighbor `B` and each belongs to triangle `B-C-D`.

Therefore:

`t1: B=0, C=0, D=0, A=1`.

At `t2`, `A` has no triangle membership and remains `1`.

Final state:

`B=C=D=0, A=1`.

### ΩP₄-B

`t0: A=0, B=C=D=1`.

`B` and `D` have zero-valued neighbor `A`, but no vertex belongs to a triangle because the structure is a 4-cycle.

Therefore:

`t1: A=0, B=C=D=1`.

The state remains unchanged thereafter.

Final state:

`A=0, B=C=D=1`.

## 5. Result

The two systems have identical:

- entity count;
- relation count;
- relation-sign multiset;
- connected-component count;
- source-distance profile `{0,1,1,2}`.

Yet they produce different trajectories under the same fixed transition rule.

Therefore:

`same source-distance profile ≠ behavioral equivalence`.

More specifically:

`distance profile` does not encode all relational organization relevant to this declared dynamics.

## 6. Interpretation

The missing information is not another numerical distance. It is a relational property of the organization: triangle membership / local cycle structure.

This does not prove that distance profiles are useless. It proves only that the tested profile is not sufficient for the tested transition task.

The general Ω sufficiency condition remains:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

Here the chosen profile `Q` is equal for the two systems, while the future behavior `F` differs; therefore `Q` fails the sufficiency condition for this task.

## 7. Consequence for geometry

A scalar distance or source-distance histogram cannot automatically be promoted to a complete geometric state descriptor.

A richer geometry may need to retain additional relational organization, such as:

- path multiplicity;
- cycle participation;
- local motif structure;
- directed reachability;
- transformation accessibility;
- behavioral response.

Which additions are necessary must be determined task-by-task.

## 8. Status decision

`PATH-PROFILE-003`: structural counterexample plus recorded failed dynamic attempt.

`PATH-PROFILE-004`: positive executed behavioral counterexample.

The stronger claim is now supported under the declared finite model:

`restricted source-distance profile → not behavior-sufficient`.

No universal claim about all possible path profiles is made.

## 9. Next mathematical step

Construct a richer path/organization descriptor and search for the next minimal counterexample:

`same descriptor → different behavior`.

The goal is not to endlessly enlarge a descriptor, but to identify the minimal information required by a declared transition class and determine whether that requirement has a clean Ω formulation.
