# Ω-Math — EXPERIMENT_OMEGA_MULTI_CYCLE_CANONICALITY_016

## Status

`EXECUTED / EXACT FINITE TEST + BASIS-DEPENDENCE COUNTERTEST`

## Question

Can the cycle-derived reversible operator `C` be combined canonically when a general relation graph contains multiple overlapping cycles?

Target:

`multiple ordered cycles → C_total → A_total`

without introducing an arbitrary choice of cycle basis or cycle weights.

## 1. Test graph

Use a four-node graph with edges:

`e0: 1→2`

`e1: 2→3`

`e2: 3→4`

`e3: 4→1`

`e4: 2→4`

This graph contains multiple overlapping cycles.

The oriented incidence matrix is:

`B = [[1,0,0,-1,0],[-1,1,0,0,1],[0,-1,1,0,0],[0,0,-1,1,-1]]`.

## 2. Cycle-derived operator for each ordered cycle

For an ordered cycle with edge sequence `(e_i1,...,e_im)`, define its local successor operator by

`C_cycle[i_k,i_{k+1}] = +1/m`

`C_cycle[i_{k+1},i_k] = -1/m`

with cyclic wraparound.

Each cycle operator is skew-symmetric.

The induced node operator is

`A_cycle = B C_cycle B^T`.

Therefore each individual cycle produces a conservative skew-symmetric node operator.

## 3. Two different cycle bases

Basis A:

`C1 = (e0,e1,e2,e3)`

`C2 = (e0,e4,e3)`.

Basis B:

`C1 = (e1,e2,e4)`

`C2 = (e0,e4,e3)`.

Both are valid cycle decompositions of the same graph structure.

Using equal unit weights for the selected cycles gives two different aggregate operators.

For Basis A the induced operator is approximately:

`A_A = [[0,1.5,0,-1.5],[-1.5,0,0.5,1],[0,-0.5,0,0.5],[1.5,-1,-0.5,0]]`.

For Basis B:

`A_B = [[0,1,0,-1],[-1,0,-1/3,4/3],[0,1/3,0,-1/3],[1,-4/3,1/3,0]]`.

Their difference is nonzero; Frobenius norm:

`||A_A - A_B|| = 2`.

Therefore the induced reversible operator depends on the selected cycle basis when the combination rule is simply “sum the chosen cycle operators with equal weights”.

## 4. Invariants that survive

For both constructions:

`A^T = -A`.

`1^T A = 0`.

For any state/potential vector `phi`:

`phi^T A phi = 0`.

For nonconstant states, the induced motion is generally nonzero.

Thus the local cycle construction is structurally valid, but the global aggregation is not yet canonical.

## 5. Result

`PASS — INDIVIDUAL ORDERED CYCLES GENERATE VALID CONSERVATIVE REVERSIBLE OPERATORS.`

`PASS — THE INDUCED OPERATORS RETAIN SKEW-SYMMETRY AND CLOSED-NETWORK CONSERVATION.`

`FAIL — SIMPLE EQUAL-WEIGHT SUMMATION IS NOT BASIS-INDEPENDENT.`

Therefore Experiment 015 does not yet extend automatically from one simple cycle to a canonical general graph law.

## 6. Important boundary

The failure is useful rather than destructive.

It identifies the exact missing object:

`general relation graph → canonical cycle combination rule`.

A valid rule must not depend on an arbitrary choice of cycle basis. It must either:

1. use an invariant construction from the full graph;
2. derive cycle weights from declared graph semantics;
3. or prove that different valid cycle decompositions are equivalent under the induced node dynamics.

No such rule is admitted yet.

## 7. Current status of the candidate formula

The strongest verified form remains:

`dx/dt = B(C-K)B^T grad(Phi)`.

For simple ordered cycles, `C` can be derived from path order.

For general multi-cycle graphs, the canonical derivation of `C` remains an open research problem.

This experiment does not modify the canonical Ω-Math v0.9 core.
