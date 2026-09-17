# Ω-040 — Marginal Cost + Conservation Preregistration v1.0

**Status:** PREREGISTERED / OPEN FOR EXECUTION
**Parent:** Ω-039
**Core:** Ω-Math v0.9 unchanged

## 1. Question

Does adding a fixed resource/edge-weight budget convert cost reduction into compensating reinforcement, without explicitly encoding same-sign reinforcement?

## 2. Hypothesis

Under a fixed total edge-weight budget, a cost-minimizing update will reduce high-cost cross-sign relations and redistribute released weight toward lower-cost same-sign relations, producing positive differential reinforcement.

## 3. Null

Without a conservation constraint, cost minimization does not require compensating growth of low-cost relations; with the declared neutral redistribution control, no positive same-vs-cross reinforcement difference is expected.

## 4. Common model

Use the same N=40 common two-pole ensemble, seeds 0..99, and Ω-038 v1.2 structural perturbation.

Node-state dynamics: competitive ON, high memory (`delta=0.01`), `eta=0.04`, `beta=3.0`, `gamma=0.5`, noise SD `0.002`.

At each graph update define mismatch cost:

`c_ij=(1-z_i z_j)/2`.

Graph objective:

`J(A,z)=Σ_{i<j} A_ij c_ij`.

Total edge resource:

`W=Σ_{i<j} A_ij`.

## 5. Cost-constrained update

For each step, consider bounded transfers of edge weight from donor edges to recipient edges.

A transfer is:

`A_d' = A_d - q`, `A_r' = A_r + q`

with `q=0.03*min(A_d, 1-A_r)` and bounds enforced.

For each step select transfers that maximize the one-step objective decrease `ΔJ = J(A,z)-J(A',z)` while preserving exactly the total resource W, using greedy selection over all donor/recipient pairs.

No rule may refer directly to "same-sign" as a reward. Selection uses only `c_ij`, objective decrease, and the conservation constraint.

## 6. Controls

A. **Constrained cost:** objective-minimizing transfers with exact W conservation.

B. **Unconstrained cost:** Ω-039 cost-derived update, which can delete cross-sign weight without compensating growth.

C. **Neutral redistribution:** same bounded donor/recipient transfers but recipient/donor selection is randomized independently of cost.

D. **Explicit positive control:** Ω-038 adaptive same-sign growth/cross-sign decay.

All use identical matched seeds and perturbations.

## 7. Primary metrics

- reinforcement ratio `R = mean(ΔA_same)-mean(ΔA_cross)`;
- total edge weight conservation error;
- objective decrease per step;
- restoration rate under Ω-038 anti-collapse criterion;
- median recovery time.

## 8. Preregistered decision threshold

The conservation mechanism supports differential reinforcement if:

`R >= 0.01`,

95% matched-seed interval for R excludes zero,

and constrained-cost restoration exceeds neutral redistribution by at least 0.20.

A positive result remains a finite-model result, not a universal theorem.

## 9. Falsification

If R remains below 0.01 despite exact conservation, or if constrained-cost behavior is not distinguishable from neutral redistribution, the hypothesis is not confirmed.

## 10. Freeze

All parameters, objective, conservation law, transfer bound, controls, metrics, and thresholds are frozen after this commit. Changes require a new preregistration version.

## 11. Interpretation boundary

This tests a mathematical resource constraint. `W` is a model quantity, not physical energy. A positive result would support a structural mechanism for compensating reinforcement, not a universal physical law.

**Execution:** pending.
