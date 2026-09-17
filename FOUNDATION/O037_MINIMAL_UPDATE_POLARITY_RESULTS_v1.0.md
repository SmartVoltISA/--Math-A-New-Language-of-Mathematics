# Ω-037 — Minimal Update Law and Polarity Results v1.0

**Status:** COMPUTATIONALLY VALIDATED FOR DECLARED FINITE MODEL / OPEN FOR GENERALIZATION  
**Experiment family:** `O037_VALUE_REINFORCEMENT_POLARITY_v1.0.md`  
**Core:** Ω-Math v0.9 unchanged

## 1. Question

The previous Ω-037 run established that value sensitivity does not itself update state. This run attacks the next gap:

`value signal → update law → reinforcement → polarity`

The question is: what is the minimum additional mechanism required to move from objective preference to reinforcement and then to a signed polarity?

## 2. Deterministic model

Use six candidates with fixed objective values:

`J = [0,1,2,3,4,5]`.

Initial state:

`W_i(0)=1` for all candidates.

At each step define the normalized value-sensitive allocation:

`a_i = exp(-β(J_i-J_min)) / Σ_j exp(-β(J_j-J_min))`.

Parameters:

`β=2`, `η=0.05`, `T=200`.

All 100 runs use seeds `0..99`.

The objective itself is deterministic; the seeds therefore serve as fixed-run reproducibility identifiers. A random control uses the seed to generate an independent allocation.

## 3. Three update mechanisms

### A — neutral accumulation

`W(t+1)=W(t)+η/n`.

No objective signal enters the update.

Result: all weights remain equal. There is no reinforcement preference and no spontaneous signed polarity.

### B — positive reinforcement

`W(t+1)=W(t)+η a`.

The update is nonnegative and objective-coupled.

Result for seed 0:

`W ≈ [9.6467, 2.1702, 1.1584, 1.0214, 1.0029, 1.0004]`.

Across all 100 seeds the deterministic objective gives the same trajectory because no stochastic term enters the update. The objective ranking is reinforced, but all state variables remain positive.

Therefore reinforcement/channelization exists without an intrinsic positive/negative polarity variable.

### C — zero-sum competitive update

`W(t+1)=W(t)+η(a-1/n)`.

The update conserves total weight increment:

`Σ_i ΔW_i = 0`.

This introduces competition relative to a neutral baseline.

For seed 0 after 200 steps:

`W ≈ [7.9800, 0.5035, -0.5083, -0.6452, -0.6638, -0.6663]`.

The state itself now contains both positive and negative values.

This is the first tested mechanism in this family where polarity is present as a property of the **signed competitive state**, rather than being imposed afterward by `sign(W_i-W_j)`.

## 4. Random competitive negative control

Replace `a` by a normalized random allocation `a_rand`, then use:

`W(t+1)=W(t)+η(a_rand-1/n)`.

In the 100-seed sample, random competition can create signed states as well. For seed 0:

`W ≈ [1.0619,1.0380,1.0205,0.9542,1.0460,0.8784]`.

Thus **signed competition alone can generate a sign partition**, but it does not establish a stable correspondence between sign and objective value.

This separates two ingredients:

1. competition can create polarity;
2. objective-coupled allocation can align that polarity with the declared objective.

## 5. Minimal-ingredient comparison

| Mechanism | Objective signal | Reinforcement | Signed state | Objective-aligned polarity |
|---|---:|---:|---:|---:|
| A neutral | no | no | no | no |
| B positive reinforcement | yes | yes | no | no intrinsic polarity |
| C competitive | yes | yes | yes | yes in this declared model |
| random competitive | no | stochastic | yes | no demonstrated objective alignment |

The table is a model-level decomposition, not a universal theorem.

## 6. Important distinction

The computation does **not** show:

`marginal cost ↓ → polarity`.

It shows a more precise conditional chain:

`objective/value signal`

`→ declared allocation rule`

`→ reinforcement`

`→ if update is zero-sum/signed, competition can create polarity`

`→ if allocation depends monotonically on objective, polarity can become objective-aligned`.

The update law is the active mechanism connecting these stages.

## 7. Stronger mathematical observation

For the positive reinforcement law:

`ΔW_i = η a_i ≥ 0`.

Starting from positive `W_i(0)`, no component can cross zero. Therefore this mechanism cannot generate an endogenous sign change.

For the competitive law:

`ΔW_i = η(a_i-1/n)`.

Some candidates have `a_i>1/n` and others have `a_i<1/n`. Hence the update has both positive and negative increments and can cross zero.

This identifies a concrete structural requirement for endogenous sign formation in this model: the state/update must contain a signed contrast or an equivalent conservation/competition constraint.

## 8. What is established

1. A value/objective signal requires an explicit update law to affect state.
2. Nonnegative reinforcement can strongly channel state toward lower objective values without producing an intrinsic signed polarity.
3. A zero-sum competitive update can create signed polarity from the same objective-sensitive allocation.
4. Random competition can also create signs, so sign formation alone is insufficient evidence of objective selection.
5. Objective-aligned polarity requires both a signed competitive mechanism and an objective-dependent allocation in this model.
6. The earlier shorthand is therefore refined to:

`value sensitivity → allocation/update → reinforcement`

and, under an additional signed competitive constraint:

`reinforcement + competition → polarity`

with objective alignment inherited from the allocation rule.

## 9. What remains OPEN

- whether this decomposition survives adaptive graphs rather than six fixed candidates;
- whether memory/history changes the minimum mechanism;
- whether polarity can emerge through symmetry breaking without an explicitly signed state variable;
- whether the same result holds for independent objective families;
- whether an empirical physical correspondence exists;
- whether any of these mechanisms are universal.

## 10. Reproducibility

Execution: local deterministic Python numerical environment. 100 fixed seeds, `0..99`; `β=2`, `η=0.05`, `T=200`, `n=6`.

No GitHub Actions result is claimed. The computation was executed directly in the available numerical environment.

## 11. Decision / fixation

**DECISION:** PASS for the declared finite model decomposition; OPEN for generalization.

The current research chain is fixed as:

`constraints → feasible set → objective → value function → sensitivity → allocation/update law → reinforcement → competition/signed contrast → polarity`

The phrase `marginal cost ↓ → reinforcement → polarity` remains a hypothesis shorthand only. It is not promoted to theorem or primitive.
