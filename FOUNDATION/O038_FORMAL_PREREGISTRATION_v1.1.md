# Ω-038 — Formal Preregistration v1.1: Anti-Collapse Two-Pole Self-Restoration

**Status:** PREREGISTERED / OPEN FOR EXECUTION
**Parent:** `O038_DYNAMIC_GRAPH_MEMORY_POLARITY_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Question

Does the declared dynamic-graph model produce a nontrivial two-sign organization that survives a perturbation and returns to the same structural regime, rather than merely collapsing into one sign?

## 2. Hypothesis

Under the declared model, competitive allocation + adaptive same-sign reinforcement + high memory will produce a higher rate of valid two-pole self-restoration than matched controls.

This is a model hypothesis, not a universal mathematical or physical claim.

## 3. Null hypothesis

After controlling for both-sign occupancy and a sign-shuffled null, the factorial conditions do not differ in valid two-pole self-restoration rate beyond the preregistered effect threshold.

## 4. Fixed model

- N = 40 nodes
- T = 300 pre-perturbation steps
- seeds = 0..99
- η = 0.04
- β = 3.0
- γ = 0.5
- noise amplitude = 0.002
- adaptive rate ρ = 0.03
- low-memory δ = 0.12
- high-memory δ = 0.01
- initial graph: symmetric dense nonnegative weighted graph from matched fixed seed, diagonal zero
- initial node state: x_i ~ Normal(0,1) from the matched fixed seed
- z_i = sign(x_i); zero is assigned +1
- h_i = Σ_j A_ij z_i z_j / Σ_j A_ij
- J_i = 1 − γ h_i
- a_i = exp(−β J_i) / Σ_j exp(−β J_j)
- competitive update: x_i'=(1−δ)x_i + η(a_i−1/N)+noise
- noncompetitive update: x_i'=(1−δ)x_i + ηa_i+noise
- adaptive graph update: A_ij' = clip(A_ij(1+ρ),0,1) for same-sign endpoints and A_ij' = clip(A_ij(1−ρ),0,1) for opposite-sign endpoints
- nonadaptive control leaves A unchanged

## 5. Factorial design

All eight matched conditions are executed:

1. competitive OFF / adaptive OFF / low memory
2. competitive OFF / adaptive OFF / high memory
3. competitive OFF / adaptive ON / low memory
4. competitive OFF / adaptive ON / high memory
5. competitive ON / adaptive OFF / low memory
6. competitive ON / adaptive OFF / high memory
7. competitive ON / adaptive ON / low memory
8. competitive ON / adaptive ON / high memory

## 6. Primary anti-collapse metrics

For each seed at each evaluation point:

### 6.1 Two-sign occupancy

`B = min(f_plus, f_minus)`.

Valid two-pole occupancy requires:

`B >= 0.20`.

### 6.2 Weighted same-sign fraction

`S = W_same / W_total`.

### 6.3 Sign-shuffled null

For the observed graph and observed sign counts, randomly permute the node signs without changing the number of positive and negative nodes. Use 100 independent permutations per evaluation point.

Let `S_null` be the mean same-sign weighted fraction across these permutations.

Define:

`D = S − S_null`.

The preregistered separation threshold is:

`D >= 0.10`.

### 6.4 Valid two-pole state

A state is valid only if all conditions hold:

- `B >= 0.20`
- `D >= 0.10`

This prevents one-sign collapse from counting as polarity.

## 7. Perturbation protocol

After the 300-step pre-perturbation state, perturb every node state independently:

`x_i := x_i + Normal(0,0.5)`.

Do not modify the graph directly.

Then run 50 additional model steps with the same declared update equations and parameters.

Evaluate the state after every post-perturbation step.

## 8. Self-restoration criterion

A seed is counted as **restored** if:

1. the pre-perturbation state is valid two-pole;
2. after perturbation, at least one post-perturbation evaluation within steps 1..50 is valid two-pole;
3. the first valid recovery occurs without ever requiring one-sign collapse as an intermediate success criterion.

Recovery time is the first post-perturbation step satisfying the valid two-pole criterion.

A seed that starts in a one-sign state is not a successful restoration, even if it remains persistent.

## 9. Primary outcome

Per condition:

`restoration_rate = restored_seeds / pre_valid_seeds`.

The primary comparison is the matched difference in restoration rate between conditions, with particular attention to the full `competitive + adaptive + high-memory` condition versus its matched controls.

Because this is a factorial experiment, no single-condition "winner" is declared in advance; all eight condition results are retained.

## 10. Secondary outcomes

- pre-perturbation valid-state rate;
- post-perturbation valid-state rate by step;
- median recovery time among restored seeds;
- B before perturbation and during recovery;
- S before perturbation and during recovery;
- D before perturbation and during recovery;
- within-sign versus cross-sign weighted connectivity;
- sign persistence conditioned on valid two-pole occupancy;
- graph modularity as descriptive secondary metric only.

## 11. Controls

### 11.1 Matched-seed control

The same seed generates the initial state for every factorial condition.

### 11.2 Sign-shuffled null

Preserves observed sign counts while destroying node-sign/topology correspondence.

### 11.3 Objective permutation control

For a separate control run, permute the mapping between node-local objective values `J_i` and allocation entries before the update while preserving the multiset of `J_i`. This tests whether node-specific objective allocation matters beyond the value distribution itself.

### 11.4 No physical interpretation

All quantities remain mathematical/model variables. No physical energy, force, time, or material polarity is inferred.

## 12. Statistical decision rule

Primary effect threshold:

`Δ restoration_rate >= 0.20` for the preregistered focal comparison, with the sign-shuffled and anti-collapse criteria satisfied.

Report exact counts, matched per-seed differences, uncertainty intervals, and all eight conditions. Do not convert the threshold into a universal claim.

Multiple-testing family: the eight factorial condition estimates plus the focal control comparisons are treated as one declared exploratory family; report raw values and apply Benjamini–Hochberg FDR at q=0.05 for secondary inferential comparisons. The primary preregistered threshold remains a descriptive decision threshold, not a theorem.

## 13. Falsification conditions

The hypothesis is weakened/fails for this model if the focal condition does not show a materially higher restoration rate than its matched controls, or if apparent separation disappears after the occupancy and sign-shuffled controls.

A failure is a valid result and must be recorded without parameter tuning after inspection.

## 14. Freeze rule

After this document is committed, numerical parameters, metric definitions, thresholds, perturbation protocol, permutation count, and decision rule are frozen for Ω-038 v1.1.

Any later modification requires a new preregistration version and must not overwrite the interpretation of this run.

## 15. Decision

**PREREGISTERED:** yes, after commit.

**EXECUTION:** pending.

**Claim level:** finite declared model only.
