# Ω-038 — Formal Preregistration v1.2: Common Two-Pole Ensemble Restoration

**Status:** PREREGISTERED / OPEN FOR EXECUTION
**Parent:** `O038_FORMAL_PREREGISTRATION_v1.1.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Question

When every factorial condition starts from the same valid two-pole ensemble and receives the same structural perturbation, which declared factors affect restoration of two-pole organization?

## 2. Hypothesis

Adaptive relation reinforcement will increase two-pole restoration relative to nonadaptive matched controls. Competition and memory effects are secondary factors to be measured without assuming a direction.

This is a finite-model hypothesis, not a universal mathematical or physical claim.

## 3. Null

After conditioning on the same initial ensemble and matched perturbation, adaptive and nonadaptive conditions do not differ in restoration rate beyond the declared effect threshold.

## 4. Common initial ensemble

For each seed 0..99:

- N=40 nodes, exactly 20 positive and 20 negative initial signs;
- node signs are randomly permuted by the seed;
- initial graph is symmetric, diagonal zero, nonnegative weighted;
- within-sign edge weights are sampled from Normal(0.8,0.05), clipped to [0,1];
- cross-sign edge weights are sampled from Normal(0.2,0.05), clipped to [0,1];
- initial x_i = z_i + Normal(0,0.05);
- the same resulting A and x are copied identically to all eight factorial conditions.

The analytical sign-shuffled expectation is used for the null:

`S_null = [n_plus(n_plus-1)+n_minus(n_minus-1)]/[N(N-1)]`.

This equals the expected weighted same-sign fraction under a uniformly random sign permutation when edge weights are fixed.

Initial validity requires `B=min(f_plus,f_minus)>=0.20` and `D=S-S_null>=0.10`.

## 5. Factorial design

All 8 combinations are run:

- competitive OFF/ON;
- adaptive OFF/ON;
- memory low/high.

Parameters:

`T=100`, `eta=0.04`, `beta=3.0`, `gamma=0.5`, noise SD `0.002`, adaptive rate `rho=0.03`.

Low memory: `delta=0.12`.
High memory: `delta=0.01`.

Update:

`h_i = Σ_j A_ij z_i z_j / Σ_j A_ij`

`J_i = 1-gamma*h_i`

`a_i = exp(-beta J_i)/Σ_j exp(-beta J_j)`

Competitive:
`x_i'=(1-delta)x_i + eta(a_i-1/N)+noise`.

Noncompetitive:
`x_i'=(1-delta)x_i + eta*a_i+noise`.

Adaptive:
`A_ij'=clip(A_ij(1+rho),0,1)` for same-sign endpoints and
`A_ij'=clip(A_ij(1-rho),0,1)` for opposite-sign endpoints.

Nonadaptive: A unchanged.

## 6. Matched perturbation

After the common valid initial state is established, every condition receives the identical seed-specific perturbation:

1. choose 12 of 40 nodes without replacement and flip their current sign by `x_i := -x_i`;
2. add independent Normal(0,0.15) noise to every x_i;
3. randomly select 30% of undirected edges without replacement and multiply their weights by 0.10;
4. do not modify the perturbation across factorial conditions for a given seed.

The perturbation is applied once before the 100-step recovery window.

## 7. Valid two-pole state

At every evaluation step:

`B=min(f_plus,f_minus)`.

`S=W_same/W_total`.

`D=S-S_null` using the analytical fixed-count null.

Valid state requires:

`B>=0.20` and `D>=0.10`.

## 8. Restoration

A seed is restored if, after perturbation, a valid two-pole state is maintained for at least **10 consecutive evaluation steps** within the 100-step recovery window.

Recovery time is the first step of that 10-step valid run.

Because every condition begins from the same valid ensemble, restoration rates are directly comparable across factors.

## 9. Primary outcome

Restoration rate over all 100 matched seeds.

Primary factor comparison: adaptive ON versus adaptive OFF, pooled across the other declared factors, with matched-seed differences retained.

Primary effect threshold:

`absolute restoration-rate difference >= 0.20`.

No ranking of the eight conditions is declared.

## 10. Secondary outcomes

- restoration rate by each factorial cell;
- median recovery time;
- B, S, D trajectories;
- final within-sign/cross-sign connectivity;
- sign balance;
- conditional persistence while valid;
- factor interactions;
- objective permutation control.

## 11. Objective permutation control

A separate matched control permutes the mapping from node-local objective values J_i to allocation entries a_i while preserving the multiset of J values. The control is used only to test whether node-specific objective placement contributes beyond the value distribution.

## 12. Decision rules

Record all eight cells and matched per-seed outcomes. Report exact counts and uncertainty intervals.

Apply Benjamini-Hochberg FDR q=0.05 to secondary inferential comparisons. The primary 0.20 threshold is a declared decision threshold, not a theorem.

## 13. Freeze rule

After this commit, the parameters, ensemble construction, perturbation, validity criterion, 10-step persistence requirement, null definition, and decision rule are frozen for v1.2. Any change requires v1.3 or later.

## 14. Interpretation boundary

No physical meaning is assigned to energy, force, time, polarity, or memory. Reinforcement remains an explicit model rule. This experiment therefore does not by itself derive `marginal cost ↓ → reinforcement`.

## 15. Decision

**PREREGISTERED:** yes, after commit.
**EXECUTION:** pending.
**Claim level:** finite declared model only.
