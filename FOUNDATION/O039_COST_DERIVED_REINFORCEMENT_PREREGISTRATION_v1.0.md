# Ω-039 — Cost-Derived Reinforcement Preregistration v1.0

**Status:** PREREGISTERED / OPEN FOR EXECUTION
**Parent:** Ω-038 v1.2
**Core:** Ω-Math v0.9 unchanged

## 1. Question

Can relation reinforcement emerge from a declared objective/cost functional, without explicitly hard-coding same-sign reinforcement?

## 2. Hypothesis

If a graph update minimizes a declared structural objective subject to bounded change, then edges whose modification lowers the objective will receive greater retained weight, potentially producing reinforcement and two-pole organization.

## 3. Null

A cost-driven update does not produce greater reinforcement/separation than a matched neutral update when no explicit same-sign reward is included.

## 4. Model boundary

The cost is mathematical/model cost. It is not physical energy.

For each undirected edge e=(i,j), define mismatch cost:

`c_ij = (1 - z_i z_j)/2`, so same-sign edges have cost 0 and cross-sign edges have cost 1.

Define total graph cost:

`J(A,z)=Σ_{i<j} A_ij c_ij`.

At each step, propose bounded edge changes `ΔA_ij` with `|ΔA_ij| <= rho*A_ij` and `A_ij+ΔA_ij ∈ [0,1]`.

The cost-derived update selects the feasible proposal that minimizes `J(A+ΔA,z)` plus a quadratic change penalty:

`J_total = J(A+ΔA,z) + lambda Σ_{i<j}(ΔA_ij)^2`.

Set `rho=0.03`, `lambda=1.0`.

No explicit rule may reference "same-sign reinforcement" or "opposite-sign weakening".

## 5. Matched conditions

Run 100 seeds with the same common two-pole initial ensemble and the same perturbation protocol as Ω-038 v1.2.

Compare:

1. cost-derived graph update;
2. neutral graph update with zero-mean bounded edge proposals and the same quadratic change penalty;
3. explicit Ω-038 adaptive rule as a positive-control reference.

Node-state dynamics use the Ω-038 v1.2 equations with competition ON and high memory (`delta=0.01`) for the focal comparison, with all other parameters unchanged.

## 6. Primary metrics

- mean signed edge change by edge class (same-sign vs cross-sign);
- reinforcement ratio `R = mean(ΔA_same) - mean(ΔA_cross)`;
- restoration rate using Ω-038 anti-collapse criterion `B>=0.20`, `D>=0.10`, sustained for 10 consecutive steps;
- recovery time.

## 7. Secondary metrics

- total cost J before/after;
- objective decrease per step;
- within/cross connectivity;
- sign balance;
- correlation between edge-level cost change and retained ΔA;
- comparison with neutral control.

## 8. Decision threshold

Cost-derived reinforcement is considered present in this model if:

`R >= 0.01`

and its 95% matched-seed interval excludes zero, with restoration rate at least 0.20 higher than the neutral control.

This is a model-specific decision rule, not a universal law.

## 9. Falsification

The hypothesis is weakened if the cost-derived update produces no positive reinforcement ratio, if reinforcement disappears under the neutral control comparison, or if two-pole restoration does not exceed the neutral control by the declared threshold.

## 10. Freeze

All parameters, cost definition, proposal bound, quadratic penalty, controls, metrics and thresholds are frozen after this commit. Any modification requires a new preregistration version.

## 11. Interpretation boundary

Even a positive result would establish only that a particular declared cost functional can generate reinforcement in the finite model. It would not establish `marginal cost ↓ → reinforcement` as a universal law or physical principle.

**Execution:** pending.
