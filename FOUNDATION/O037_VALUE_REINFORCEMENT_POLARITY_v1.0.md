# Ω-037 — Value → Reinforcement → Polarity v1.0

**Status:** EXPERIMENT / OPEN
**Core:** Ω-Math v0.9 unchanged
**Purpose:** test whether optimal-value sensitivity predicts reinforcement, and whether reinforcement alone is sufficient to produce persistent polarity.

## 1. Research question

The working chain is:

`closure → constraints → feasible set → objective → value function → optimum set → marginal sensitivity → feedback/update → retention/reinforcement → polarity`

The experiment explicitly tests the two gaps:

1. Does value-function sensitivity contain predictive information about reinforcement beyond a null model?
2. Does reinforcement by itself produce polarity, or is an explicit signed/competitive rule additionally required?

## 2. Hypotheses

**H1 — sensitivity:** under a fixed declared objective and controlled feasible-set perturbations, value-function sensitivity `ΔV` / finite marginal `M` is a reproducible structural observable of the change in achievable optimum.

**H2 — reinforcement:** sensitivity alone does NOT cause reinforcement. Predictive association with reinforcement should appear only when an explicit allocation/update law couples objective/value information to state updates.

**H3 — polarity:** reinforcement alone does NOT logically imply polarity. Persistent polarity requires an explicit signed contrast, partition, competition, or equivalent symmetry-breaking rule.

## 3. Null hypotheses

**H0-1:** value sensitivity provides no predictive advantage over the declared baseline for the reinforcement outcome.

**H0-2:** the same reinforcement dynamics occur when the sensitivity signal is permuted or replaced by a representation-matched random control.

**H0-3:** reinforcement without an explicit signed/competitive rule does not produce persistent polarity above the predefined null baseline.

## 4. Mathematical domain

Use finite graphs with fixed vertex set and finite candidate configuration set.

A candidate configuration `C` is a subset of a fixed edge universe. Feasibility is controlled by a declared constraint parameter `K`.

For each `K`:

`F(K) = { C ∈ A | K(C) = true }`

Use a declared objective `J(C)` and value function:

`V(K) = min { J(C) | C ∈ F(K) }`

when the minimum exists.

Finite sensitivity:

`ΔV = V(K') - V(K)`

and, for scalar parameter steps:

`M(K;ΔK) = [V(K+ΔK)-V(K)]/ΔK`.

## 5. Required controls

### Control A — value only

Compute `F`, `J`, `V`, `Opt`, `ΔV`. Do not update relation weights.

Expected result: structural sensitivity exists, but reinforcement is undefined/absent because no update law exists.

### Control B — reinforcement without value signal

Use a fixed allocation/update law independent of `ΔV`.

Expected result: reinforcement may occur, demonstrating that reinforcement can arise from an explicit update rule rather than from sensitivity itself.

### Treatment C — value-coupled reinforcement

Declare an update law, for example:

`a_i(t) = exp(-β J_i(t)) / Σ_j exp(-β J_j(t))`

`W_i(t+1) = W_i(t) + η a_i(t)`

with fixed `β > 0`, `η > 0`.

The exact law is a model choice and is not claimed to be universal.

### Control D — permuted sensitivity

Keep the same data and update machinery but randomly permute the sensitivity signal across candidates/runs.

Expected result: any predictive effect attributable specifically to sensitivity should disappear or materially weaken.

### Control E — reinforcement without polarity rule

Run reinforcement with nonnegative weights and no signed partition.

Expected result: concentration/channelization may occur, but a persistent positive/negative polarity is not defined and therefore cannot be claimed.

### Treatment F — explicit polarity map

Add a declared signed contrast, e.g.

`P(i,j,t) = sign(W_i(t)-W_j(t))`

or another preregistered partition rule.

Test whether the sign persists after the rule is applied and under perturbation.

## 6. Primary metrics

1. `V(K)` and `ΔV`.
2. Finite marginal sensitivity `M` where applicable.
3. Optimum-set identity/overlap.
4. Reinforcement magnitude `R` under each explicit update law.
5. Predictive association between sensitivity and later reinforcement.
6. Null-control association after permutation.
7. Concentration/channelization metrics.
8. Polarity persistence and sign stability only when a polarity map is explicitly defined.
9. Run-to-run reproducibility.

## 7. Falsification logic

The following observations falsify the corresponding strong claim:

- If identical `ΔV` occurs with and without reinforcement, then `ΔV → reinforcement` is not sufficient.
- If reinforcement occurs in Control B without sensitivity, sensitivity is not necessary for that reinforcement mechanism.
- If permuted sensitivity performs comparably to true sensitivity, the claimed predictive role is unsupported.
- If reinforcement without a signed rule produces no defined polarity, then reinforcement does not itself define polarity.
- If polarity appears only after adding the explicit sign/competition map, the map is a necessary model ingredient for that observed polarity mechanism.

## 8. Minimal executable example

For a triangle with three possible edges and objective `J(C)=|C|`, define:

`F(K) = {C : |C| ≥ K}`.

Then for `K=0,1,2,3`:

`V(K)=0,1,2,3`.

For `K=4`, `F(K)=∅` and no optimum exists.

This verifies the basic value-function/feasibility separation and supplies an infeasibility control.

A direct counterexample to `ΔV → reinforcement` is obtained by computing `ΔV` while applying Control A: `ΔV` changes, but no reinforcement occurs because no update law is present.

A direct construction of reinforcement requires an explicit `U`. With the example softmax allocation above, a lower-cost candidate receives greater allocation, but that is a consequence of the declared update rule, not of the value function alone.

## 9. Representation controls

For scalar `J`, replace it by a strictly increasing transform `f(J)`. The optimum set must remain invariant.

Use at least one non-monotone transform as a negative representation control; a changed optimum set is expected and demonstrates that arbitrary reparameterization is not harmless.

## 10. Degeneracy controls

Include cases with:

- multiple equal minima;
- empty feasible set;
- feasible but unattained infimum where a continuous/discrete mixed model permits it;
- two distinct objectives with different optimum sets;
- multiobjective/Pareto selection.

No hidden tie-breaker may be used.

## 11. Reproducibility

Record:

- experiment ID;
- preregistration version;
- random seeds;
- graph/configuration generator;
- all parameter values;
- objective definition;
- constraint definition;
- update law;
- polarity map;
- code/version hash;
- environment;
- raw result hashes;
- validation result.

Target reproducibility: Level 2 (numerical tolerance) minimum; Level 3 where practical.

## 12. Multiple testing

If multiple sensitivity metrics, update laws, or polarity metrics are tested as one inferential family, declare the family before execution and apply the preregistered correction. Exploratory variants must remain labelled exploratory.

## 13. Decision criteria

**PASS for H1:** sensitivity is reproduced across independent runs and behaves according to the declared feasible-set/objective definitions, including the monotonicity control.

**PASS for H2:** the data show that reinforcement requires an explicit update mechanism; sensitivity alone is insufficient. Any stronger predictive claim requires comparison against the null and permutation control.

**PASS for H3:** reinforcement without an explicit signed/competitive rule does not define persistent polarity, while the preregistered polarity mechanism can be tested independently.

**FAIL:** a preregistered mathematical or reproducibility requirement is contradicted.

**OPEN:** evidence is insufficient, unstable, or dependent on model-specific choices.

A PASS here is a result about the declared model family, not a universal law of nature.

## 14. Current result

**RESULT:** analytical controls completed for the minimal finite example.

- `V(K)` is well-defined for the finite feasible cases.
- Empty-feasible-set behavior is explicit.
- Feasible-set sensitivity is distinct from candidate-level cost change.
- `ΔV` does not itself create reinforcement; reinforcement requires `U`.
- The proposed softmax allocation demonstrates a model in which lower objective values receive greater allocation, but this is an assumption of `U`, not a derived law.
- Polarity requires an explicit signed/partition rule and is not implied by nonnegative reinforcement.

**STATUS: OPEN — computational multi-run validation still required.**

## 15. Decision / fixation

Do **not** promote:

`marginal cost ↓ → reinforcement → polarity`

to a theorem or primitive.

The current accepted research chain is:

`constraints → feasible set → objective → value function → optimum set → marginal sensitivity → explicit update/feedback → reinforcement → explicit polarity rule → testable polarity`

Next validation must execute the preregistered controls with fixed seeds and record raw outputs before any final PASS/FAIL decision.
