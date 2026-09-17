# Ω-038 — Formal Results v1.1: Anti-Collapse Two-Pole Self-Restoration

**Status:** RESULT RECORDED / OPEN INTERPRETATION
**Preregistration:** `O038_FORMAL_PREREGISTRATION_v1.1.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

The preregistered finite model was executed for all eight factorial conditions with matched seeds `0..99`.

A separate deterministic random stream was used for sign-shuffled metric permutations so that null evaluation does not alter the subsequent dynamical trajectory.

The preregistered rule was applied literally:

- valid two-pole state: `B=min(f_plus,f_minus) >= 0.20` and `D=S-S_null >= 0.10`;
- 100 sign permutations per evaluation point;
- perturbation: independent `Normal(0,0.5)` added to every node state;
- recovery window: post-perturbation steps 1..50;
- restoration requires a valid pre-perturbation two-pole state and a later valid two-pole state.

## 2. Results

| Competitive | Adaptive | Memory | Pre-valid seeds / 100 | Restored seeds | Restoration rate among pre-valid | Median recovery step | Mean pre D | Mean pre B | Mean pre S |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| OFF | OFF | Low | 0 | 0 | N/A | N/A | 0.00038 | 0.04425 | 0.91506 |
| OFF | OFF | High | 0 | 0 | N/A | N/A | -0.00171 | 0.18450 | 0.69328 |
| OFF | ON | Low | 0 | 0 | N/A | N/A | 0.01477 | 0.04575 | 0.92691 |
| OFF | ON | High | 1 | 1 | 1.000 | 10 | 0.16778 | 0.11300 | 0.96570 |
| ON | OFF | Low | 0 | 0 | N/A | N/A | 0.00073 | 0.43500 | 0.50189 |
| ON | OFF | High | 0 | 0 | N/A | N/A | -0.00103 | 0.42325 | 0.50924 |
| ON | ON | Low | 0 | 0 | N/A | N/A | 0.03044 | 0.43450 | 0.53121 |
| ON | ON | High | 100 | 100 | 1.000 | 13 | 0.42477 | 0.42400 | 0.93201 |

## 3. Primary finding

The preregistered anti-collapse criterion sharply separates the focal condition from the apparent one-sign/high-connectivity controls.

The `competitive + adaptive + high-memory` condition produced a valid two-pole state for all 100 seeds before perturbation and restored a valid two-pole state for all 100 seeds within the 50-step recovery window. Median recovery time was 13 steps.

The same-sign metric alone had previously suggested high organization in several noncompetitive conditions. The anti-collapse criterion shows that those states generally fail because one sign becomes under-occupied and/or the sign-topology correspondence is close to the sign-shuffled null.

## 4. Important limitation

This result does **not** establish a conventional between-condition restoration-rate comparison for the controls because most control conditions have zero pre-valid seeds. Their restoration rate is therefore undefined under the preregistered denominator.

Consequently, the result supports a stronger statement about **formation + restoration within the focal model condition**, but it does not by itself prove that competition, adaptation, or memory is individually necessary or sufficient.

A future design must alter the experiment so matched controls are placed in a common valid two-pole initial state, or otherwise condition all factors on the same pre-valid ensemble. Only then can restoration causality be compared cleanly.

## 5. Methodological result

The experiment validates the need for an anti-collapse polarity metric. A high same-sign fraction can be produced by global sign collapse; requiring both-sign occupancy plus excess separation over a sign-shuffled null removes that confound in this model.

The useful diagnostic tuple is:

`(B, S, D, restoration_time)`

rather than `S` alone.

## 6. Relation to the Ω chain

The observed model loop remains:

`objective allocation → signed state → adaptive reinforcement → graph separation → changed local agreement → allocation`

Memory changes the retention term through `δ`.

However, the experiment still contains reinforcement explicitly in the graph update equation. It therefore does **not** derive:

`marginal cost ↓ → reinforcement`.

The proposed chain remains OPEN/HYPOTHESIS.

Likewise, the experiment does not establish that polarity is a universal consequence of the objective function, nor does it provide physical correspondence.

## 7. Decision

**RESULT:** preregistered anti-collapse test executed.

**RESULT:** focal `competitive + adaptive + high-memory` condition formed and restored valid two-pole organization for all 100 matched seeds in this finite declared model.

**DISCOVERY:** controls mostly fail at the pre-valid-state gate, revealing that causal factor comparison requires a common valid initial ensemble.

**DECISION:** do not claim universal polarity law. Next experiment should initialize every factorial condition from the same valid two-pole ensemble and test restoration under matched perturbations.

**STATUS:** OPEN — next formal experiment required for factor attribution.
