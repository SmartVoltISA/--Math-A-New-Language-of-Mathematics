# Ω-Math — EXPERIMENT_OMEGA_GRAPH_DERIVATION_014

## Status

`EXECUTED / EXACT FINITE + GENERAL ALGEBRAIC VERIFICATION`

## Question

Can the reversible operator `A` and dissipative operator `D` be constructed from the relation graph itself instead of being inserted as arbitrary node-space matrices?

This is the next step after `EXPERIMENT_OMEGA_NETWORK_TRANSITION_013`.

Target:

`relation graph → edge differences → edge coupling → node balance → A/D decomposition`.

## 1. Relation graph representation

Let `B` be an oriented incidence matrix of a finite directed relation graph.

For a node potential/state vector `phi`, the edge difference is:

`delta_phi = B^T phi`.

This is the explicit mathematical realization of:

`potential difference → relation`.

For an edge flux vector `j`, the node balance is:

`dx/dt = -B j`.

Because every column of an incidence matrix contains one `+1` and one `-1`,

`1^T B = 0`.

Therefore every closed relation network automatically satisfies:

`1^T dx/dt = 0`.

This is conservation by relation incidence, not by an independently imposed node correction.

## 2. Dissipative operator derived from relations

Let `K` be a symmetric positive-semidefinite edge coupling matrix.

Declare the passive edge law:

`j_D = K B^T phi`.

The induced node dynamics are:

`dx_D/dt = -B K B^T phi`.

Therefore define:

`D = B K B^T`.

Then:

`D^T = D`.

For every vector `phi`:

`phi^T D phi = (B^T phi)^T K (B^T phi) >= 0`.

Hence `D` is positive semidefinite and the potential contribution is non-increasing.

This is the weighted graph-Laplacian construction; the Laplacian is the standard node operator associated with graph incidence and conductance. The Ω result here is the relational derivation and its connection to the candidate transition law, not a claim that the Laplacian itself is new.

## 3. Reversible operator derived from relations

Let `C` be any skew-symmetric operator acting in edge space:

`C^T = -C`.

Define:

`A = B C B^T`.

Then:

`A^T = B C^T B^T = -B C B^T = -A`.

Also:

`1^T A = 1^T B C B^T = 0`.

Therefore the reversible operator is simultaneously:

- antisymmetric;
- conservative on the closed relation graph;
- derived from edge-level relation structure.

For every node potential/state vector `phi`:

`phi^T A phi = 0`.

Thus this relation-derived circulation changes the state without changing the quadratic potential directly.

## 4. Combined Ω graph transition law

The candidate law becomes:

`dx/dt = (A-D) grad(Phi)`

with

`A = B C B^T`

and

`D = B K B^T`.

Therefore:

`dx/dt = B (C-K) B^T grad(Phi)`.

The transition now has the desired relational chain explicitly inside the equation:

`node potential → B^T → edge difference → edge relation operator → B → node state change`.

No arbitrary node-space `A` or `D` is required.

## 5. Exact three-node cycle

Use the directed cycle:

`1 → 2 → 3 → 1`.

Choose

`B = [[1,0,-1],[-1,1,0],[0,-1,1]]`.

Choose unit dissipative edge coupling:

`K = I`.

Then:

`D = B K B^T`

is exactly:

`D = [[2,-1,-1],[-1,2,-1],[-1,-1,2]]`.

Choose the skew edge operator:

`C = (1/3) * [[0,1,-1],[-1,0,1],[1,-1,0]]`.

Then:

`A = B C B^T`

is exactly:

`A = [[0,1,-1],[-1,0,1],[1,-1,0]]`.

These are the matrices used in `EXPERIMENT_OMEGA_NETWORK_TRANSITION_013`, but here they are derived from the relation graph rather than inserted by hand.

## 6. Exact checks

For the initial state:

`phi = (2,0,-1)`

and quadratic potential:

`Phi = 1/2 * phi^T phi`,

all target identities hold exactly:

`phi^T A phi = 0`.

`phi^T D phi = 14`.

`1^T A = 0`.

`1^T D = 0`.

Therefore:

`dPhi/dt = -14` for the combined reversible+dissipative model.

The total node quantity remains conserved:

`d(1^T x)/dt = 0`.

The reversible-only transition is nonzero while `dPhi/dt = 0`.

## 7. What has changed from Experiment 013

Experiment 013 demonstrated the operator behavior for hand-specified matrices.

Experiment 014 removes that freedom for the tested construction:

`relation graph → incidence B → edge coupling C,K → induced A,D`.

The conservation and sign properties now follow structurally from the relation graph and edge operators.

## 8. Result

`PASS — DISSIPATIVE D IS DERIVABLE FROM RELATION INCIDENCE + SYMMETRIC POSITIVE EDGE COUPLING.`

`PASS — REVERSIBLE A IS DERIVABLE FROM RELATION INCIDENCE + SKEW EDGE COUPLING.`

`PASS — CLOSED-NETWORK CONSERVATION FOLLOWS FROM INCIDENCE: 1^T B = 0.`

`PASS — THE A/D SPLIT CAN BE BUILT AT EDGE LEVEL AND INDUCED AT NODE LEVEL.`

This moves the candidate formula one level closer to an Ω-derived mathematical construction.

## 9. Boundary

This still does not prove that physical systems universally use this operator decomposition.

The edge coupling matrices `C` and `K` remain model data/semantics. Their physical meaning is not supplied by Ω primitives.

The experiment also does not derive the physical potential `Phi` or physical energy from Ω-Math.

## 10. Next decisive test

The next step is to ask whether `C` itself can be derived from path/cycle structure rather than supplied as an arbitrary skew edge operator.

Target:

`ordered relation cycles → circulation operator C → A → transition`.

If that succeeds, the reversible part of the candidate law will be tied directly to Ω path/cycle structure rather than merely to an externally supplied skew matrix.
