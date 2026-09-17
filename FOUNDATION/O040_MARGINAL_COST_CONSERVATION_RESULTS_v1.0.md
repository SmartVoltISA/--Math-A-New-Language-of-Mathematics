# Ω-040 — Marginal Cost + Conservation Results v1.0

**Status:** RESULT RECORDED / PREREGISTERED THRESHOLD NOT CONFIRMED
**Preregistration:** `O040_MARGINAL_COST_CONSERVATION_PREREGISTRATION_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

The frozen Ω-040 design was executed on the common Ω-038 two-pole ensemble for seeds 0..99.

Four matched graph-update modes were tested under competitive ON / high memory node dynamics:

- constrained cost minimization with exact total edge-weight conservation;
- unconstrained cost minimization from Ω-039;
- neutral redistribution control;
- explicit reinforcement positive control.

The same seed-specific initial state and perturbation were used across matched modes.

## 2. Results

| Mode | Mean ΔA same-sign | Mean ΔA cross-sign | R | R SD | Restoration rate | Median recovery |
|---|---:|---:|---:|---:|---:|---:|
| Constrained cost | 0.003154 | -0.003119 | 0.006273 | 0.000211 | 1.00 | 5 |
| Unconstrained cost | 0.000000 | -0.003119 | 0.003119 | 0.000084 | 1.00 | 8 |
| Neutral redistribution | -0.000250 | -0.000196 | -0.000054 | 0.000073 | 0.00 | N/A |
| Explicit positive control | 0.005287 | -0.003119 | 0.008406 | 0.000165 | 1.00 | 4 |

Conservation error for the constrained mode remained at numerical floating-point scale (maximum approximately `1.14e-13` in the executed run).

## 3. Decision against preregistration

The preregistered reinforcement threshold was `R>=0.01` with a matched-seed interval excluding zero and restoration at least 0.20 above neutral.

The constrained-cost mode satisfies the directional and restoration components but gives:

`R=0.006273 < 0.01`.

Therefore the combined preregistered criterion is **NOT CONFIRMED**.

## 4. What is supported

The conservation constraint changes the mechanism compared with Ω-039. Instead of only deleting costly cross-sign relations, the model redistributes released edge weight toward lower-cost relations. This creates positive same-sign growth without explicitly inserting a same-sign reward rule.

Thus the following finite-model mechanism is observed:

`mismatch cost + fixed resource → cross-sign reduction + compensating low-cost growth`

The effect is directional and reproducible across the matched seed set, but below the preregistered magnitude threshold.

## 5. What is not established

This does not establish that a decreasing marginal cost is the cause of reinforcement. The current mismatch cost is linear in edge weight, so its marginal cost is constant within each relation class. The conservation mechanism, not a decreasing marginal-cost law, is responsible for the compensating transfer.

Therefore:

`marginal cost ↓ → reinforcement`

remains OPEN.

## 6. Structural consequence

The next test should isolate the marginal-cost mechanism itself. A concave relation cost under a fixed resource budget provides a clean candidate because its marginal cost decreases with accumulated allocation:

`J(A)=Σ c_e f(A_e)`, with `f'>0` and `f''<0`.

Then

`MC_e = ∂J/∂A_e = c_e f'(A_e)`

and `f'` decreases as A grows. This permits a direct test of whether lower marginal cost causes concentration/reinforcement, rather than merely deleting expensive relations.

## 7. Decision

**RESULT:** conservation produces compensating reinforcement in the finite model.

**RESULT:** preregistered reinforcement magnitude threshold was not met.

**DECISION:** do not promote the marginal-cost chain to a law.

**NEXT:** Ω-041 should isolate decreasing marginal cost under a fixed resource budget and test whether concentration/reinforcement emerges without an explicit reinforcement update rule.

**STATUS:** OPEN.
