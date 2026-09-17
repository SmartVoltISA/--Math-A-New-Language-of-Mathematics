# Ω-039 — Cost-Derived Reinforcement Results v1.0

**Status:** RESULT RECORDED / HYPOTHESIS NOT CONFIRMED BY PREREGISTERED THRESHOLD
**Preregistration:** `O039_COST_DERIVED_REINFORCEMENT_PREREGISTRATION_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

The frozen Ω-039 experiment was executed for 100 seeds in three matched modes:

1. `cost`: graph update derived from the declared mismatch cost functional;
2. `neutral`: bounded zero-mean random edge update independent of sign mismatch;
3. `explicit`: Ω-038 same-sign reinforcement / cross-sign weakening positive-control rule.

All modes used the same seed-specific initial two-pole ensemble, the same structural perturbation, and the same node-state dynamics (competitive ON, high memory).

## 2. Cost-derived rule

The declared objective was:

`J(A,z)=Σ_{i<j} A_ij (1-z_i z_j)/2`.

With bounded edge change and quadratic change penalty, the cost gradient implies:

- same-sign edge cost coefficient = 0 → no objective-driven increase is required;
- cross-sign edge cost coefficient = 1 → reducing cross-sign weight lowers the objective.

The executed cost-derived update therefore decreases cross-sign weights by 3% per step and leaves same-sign weights unchanged. No explicit same-sign reinforcement rule was inserted.

## 3. Results

| Mode | Mean ΔA same-sign | Mean ΔA cross-sign | Reinforcement ratio R | R SD | Restoration rate | Median recovery |
|---|---:|---:|---:|---:|---:|---:|
| Cost-derived | 0.000000 | -0.003119 | 0.003119 | 0.000084 | 1.00 | 8 |
| Neutral | -0.000238 | -0.000196 | -0.000042 | 0.000070 | 0.00 | N/A |
| Explicit positive control | 0.005028 | -0.003119 | 0.008147 | 0.000160 | 1.00 | 4 |

The cost-derived reinforcement ratio has an estimated 95% normal-approximation interval of approximately `[0.003102, 0.003136]`, which excludes zero but is below the preregistered threshold `R>=0.01`.

## 4. Decision against preregistration

The preregistered reinforcement criterion required:

`R >= 0.01`

and a 95% interval excluding zero, together with restoration at least 0.20 above the neutral control.

Observed:

- `R = 0.003119` → threshold NOT met;
- interval excludes zero → directional differential change is present;
- restoration = 1.00 versus neutral = 0.00 → restoration threshold met.

Therefore the combined preregistered criterion is **NOT CONFIRMED**.

## 5. What was learned

This is a useful negative/partial result.

The declared cost functional can produce a differential graph update and full restoration in this finite model, but the mechanism is **cross-sign suppression**, not same-sign reinforcement. The experiment therefore does not support the stronger claim that minimizing this cost automatically creates positive reinforcement of favorable relations.

The explicit positive-control rule produces a larger reinforcement ratio because it directly increases same-sign edges. This confirms that the metric can detect the distinction between:

`same-sign growth + cross-sign decay`

and

`cross-sign decay only`.

## 6. Consequence for the Ω chain

The chain is now experimentally split:

`cost functional → differential structural change` **SUPPORTED IN THIS MODEL**

`cost functional → same-sign reinforcement` **NOT ESTABLISHED**

`marginal cost ↓ → reinforcement` **OPEN / HYPOTHESIS**

`reinforcement → polarity` remains supported only for the explicitly reinforced dynamic model studied in Ω-038, not as a universal law.

## 7. Important methodological point

A scalar cost can select which relations should be reduced without specifying a mechanism that increases the complementary relations. Therefore a future derivation needs either:

- a conservation/resource redistribution constraint;
- a fixed total edge-weight budget;
- a competition term between relation classes;
- or another explicitly declared coupling in the functional.

Only then can lowering one class force growth elsewhere rather than merely deleting costly relations.

## 8. Decision

**RESULT:** Ω-039 executed as preregistered.

**RESULT:** cost minimization produced differential relation change and robust restoration, but failed the preregistered reinforcement threshold.

**DECISION:** do not promote cost-derived reinforcement to a law.

**NEXT:** Ω-040 should add a declared conservation/resource-allocation constraint and test whether `marginal cost ↓` then produces compensating reinforcement without hard-coding sign preference.

**STATUS:** OPEN.
