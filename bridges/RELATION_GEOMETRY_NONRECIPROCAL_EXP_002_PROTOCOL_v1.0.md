# RELATION-GEOMETRY-NONRECIPROCAL-EXP-002 — Emergent directional geometry from symmetric initial conditions

Status: PREREGISTERED — synthetic controlled experiment

## Question

Can directional path-cost asymmetry emerge from a symmetric initial relation graph when edge costs are not initialized asymmetrically, but are updated by a local history-dependent rule?

## Null hypothesis

H0: Starting from a reciprocal graph with identical forward/backward edge weights, the declared local update rule and reciprocalized control do not produce persistent directional path-cost asymmetry beyond the seeded null distribution.

## Alternative

H1: A lagged local update rule can produce persistent directional path-cost asymmetry from symmetric initial edge weights, and the asymmetry is distinguishable from a reciprocalized control.

## Fixed model

- N = 12 nodes on a periodic ring.
- Every nearest-neighbour direction exists initially.
- Initial weight for every directed edge = 1.0.
- No direction receives a different initial cost.
- Seeded external activity is a moving local pulse; this supplies temporal ordering but does not prescribe edge costs.
- At each step, directed edge weight `w(i,j)` is updated from the previous source activity and current target activity.
- Weight decay is applied equally to both directions.
- Edge weights are constrained to remain positive.
- No shortest-path direction is used during learning.

## Learning rule

For each directed edge `i -> j`:

`w_ij(t+1) = max(epsilon, (1-delta) w_ij(t) + eta x_i(t) x_j(t+1))`

where `eta = 0.015`, `delta = 0.001`, `epsilon = 0.05`.

The activity pulse is local and moves one lattice position per step. A small seeded background component is added independently at each node. The same generated activity series is used for the learned and control measurements for each seed.

## Reciprocalized control

After learning, construct `w_sym(i,j) = (w(i,j)+w(j,i))/2` for every neighbour pair. This removes directional asymmetry while preserving the learned undirected mean weight.

## Measurement

For each node `i`, use target `j=(i+3) mod N` and calculate directed shortest-path costs:

`D(i->j)` and `D(j->i)`.

Primary metric:

`A = mean_i |D(i->j)-D(j->i)|`

Secondary metrics:

- fraction of pairs with nonzero directional difference;
- persistence of the sign of each directional difference across repeated seeds;
- ratio `A_learned / A_reciprocalized`;
- relabelling invariance of the complete directional-difference vector.

## Seeds and acceptance criteria

Seeds: `20260909..20260924` (16 independent deterministic runs).

Support H1 only if all are satisfied:

1. mean learned asymmetry exceeds 5 times the mean reciprocalized-control asymmetry;
2. at least 75% of learned pair measurements have nonzero asymmetry;
3. the learned asymmetry remains positive under every tested seed;
4. relabelling preserves the directional-difference vector after corresponding pair remapping;
5. no initial directed edge has asymmetric weight.

Otherwise classify as `INCONCLUSIVE` unless the null clearly contradicts the observed result, in which case report the observed counterexample to H0 without promoting it to physical geometry.

## Falsification / controls

- Reciprocalized post-learning control.
- Multiple independent fixed seeds.
- Explicit check of symmetric initialization.
- Node relabelling control.
- No asymmetric edge cost is allowed in initialization.

## Scope boundary

A positive result supports only the stated synthetic graph-level proposition: local history-dependent dynamics can generate operational directional path-cost asymmetry from symmetric initial costs under this model.

It is **not** evidence for physical nonreciprocal geometry, spacetime structure, physical time, physical energy, or a universal metric.

## Reproducibility

All constants, update rule, seed range, metrics, and acceptance criteria are fixed in this document before execution.
