# Ω-Math — Objective, Functional, Optimum and Sensitivity v1.0

**Status:** EXTENSION / OPEN FOR VALIDATION  
**Core:** Ω-Math v0.9 remains unchanged  
**Purpose:** close the missing mathematical layer between feasible sets, selection, and marginal response

## 1. Scope

Given a declared admissible domain `A` and feasible set `F ⊆ A`, a selection criterion must be explicit before an optimum or marginal quantity is defined.

This extension separates:

`feasibility → objective → value → optimum set → sensitivity`

It does not imply any physical interpretation.

## 2. Objective

An objective is a declared map:

`J : F → V`

where `V` has a declared comparison relation `≼`.

A scalar objective is a special case where `V ⊆ R` and `≼` is the usual order.

The codomain need not be scalar, but its comparison rule must be explicit.

## 3. Functional versus cost

A **functional** is an objective map whose input is itself a mathematical object such as a function, path, field, configuration, or transformation family.

A **cost** is an objective whose declared interpretation is expenditure, burden, complexity, or transformation resource within the model.

Therefore:

`objective ⊇ cost`

and:

`mathematical cost ≠ physical energy`

unless an explicit physical correspondence has been independently established.

## 4. Optimum set

For minimization, define the strict comparison `≺` induced by `≼`.

The optimum set is:

`Opt(F,J) = {x ∈ F | ¬∃y ∈ F : J(y) ≺ J(x)}`

For a scalar objective this reduces to the ordinary argmin.

The language must retain the **set** of optima. Uniqueness is an additional result, never an assumption.

## 5. Empty and unattained cases

If:

`F = ∅`

then `Opt(F,J)` is undefined/empty by the declared convention and the experiment must record infeasibility.

If `inf J(F)` exists but no element attains it, then there is an infimum without an optimum:

`inf J(F)` exists, but `Opt(F,J) = ∅`.

These cases must not be silently converted into a selected candidate.

## 6. Value function — the missing bridge

Let a constraint/intervention parameter be `K`, inducing a feasible set `F(K)`.

Define the value function:

`V(K) = inf { J(x) | x ∈ F(K) }`

when the infimum exists in the declared codomain/order.

Then:

`Opt(K) = Opt(F(K), J)`

and the structural effect of changing constraints can be measured through the value function rather than ambiguously differentiating a candidate-level cost.

This gives the principal bridge:

`constraints → feasible set → objective → value function → optimum set`

## 7. Marginal response / sensitivity

For a finite intervention `K → K'`, define:

`ΔV = V(K') − V(K)`

when subtraction is defined.

For a scalar parameter `k`, a finite marginal quantity is:

`M(k;Δk) = [V(k+Δk) − V(k)] / Δk`

and a derivative `dV/dk` is permitted only when the required limiting conditions hold.

For discrete constraints, finite differences are primary; differential notation must not be used merely for appearance.

## 8. Local candidate sensitivity versus value sensitivity

Two different quantities must not be conflated:

**Candidate sensitivity:**
`ΔJ(x) = J'(x) − J(x)`

**Optimal-value sensitivity:**
`ΔV = V(K') − V(K)`

The second measures how the best achievable declared objective changes under a change in the feasible-set definition. It does not identify which candidate caused the change.

## 9. Monotonicity theorem for feasible-set inclusion

For minimization, if:

`F(K') ⊆ F(K)`

and both value functions are defined, then:

`V(K') ≥ V(K)`.

This is a mathematical consequence of set inclusion, not a physical law.

Conversely, enlarging the feasible set cannot increase the infimum under the same objective.

This theorem is useful as a structural negative/positive control for feasible-set experiments.

## 10. Multiple objectives

For:

`J(x) = (J₁(x), …, Jₙ(x))`

with product-order comparison, define the nondominated/Pareto set as the corresponding optimum construction.

Scalarization such as:

`J_λ = Σ λᵢJᵢ`

is an additional declared model choice. It must not be treated as equivalent to the original multiobjective problem without proof for the task at hand.

## 11. Selection invariance

For a scalar objective, if `f` is strictly increasing over the relevant range, then:

`Argmin(J) = Argmin(f ∘ J)`.

This provides a useful representation-control test.

A non-monotone transformation can change the selected set and therefore cannot be treated as a harmless reparameterization.

## 12. Degeneracy

If:

`|Opt(F,J)| > 1`

then the model has multiple equally optimal candidates under the declared objective.

A secondary selector may be introduced only as a new declared objective/constraint/ordering rule. The secondary rule must not be retroactively hidden inside the primary objective.

## 13. Counterexamples required

The extension must be tested against at least:

1. empty feasible set;
2. multiple minima;
3. unattained infimum;
4. objective codomain with non-scalar ordering;
5. multiobjective degeneracy;
6. strictly increasing objective reparameterization;
7. non-monotone reparameterization;
8. feasible-set tightening and enlargement;
9. sensitivity under discrete versus continuous parameters;
10. two distinct objectives producing different optimum sets.

## 14. Reinforcement and polarity gate

The chain:

`marginal cost ↓ → reinforcement → polarity`

is **not** a theorem of this extension.

A decreasing `ΔV`, `M`, or `dV/dk` only establishes a declared structural change in optimal value. Reinforcement requires a separate update law, for example:

`W_{t+1} = U(W_t, history, allocation, feedback)`

and polarity requires an explicit sign/partition map.

The causal/predictive claim must therefore be tested as a separate hypothesis against a null model.

## 15. Recommended research chain

The mathematically cleaner chain is:

`closure → constraints → feasible set → objective → value function → optimum set → marginal value/sensitivity → transformation/feedback → retention/reinforcement → new structure`

This replaces the ambiguous `minimal cost → ???` gap with the value-function layer while preserving the original research question.

## 16. Preregistration requirements

Every experiment using this layer must declare before execution:

- domain `A`;
- constraint family `K`;
- feasible-set construction `F(K)`;
- objective `J` and codomain/order;
- optimization convention;
- treatment of empty/unattained cases;
- sensitivity definition;
- negative control;
- positive control where applicable;
- reproducibility level;
- comparison metric;
- multiple-testing family and correction where applicable;
- PASS/FAIL/OPEN criteria.

## 17. Current decision

**DECISION: OPEN EXTENSION.**

The value-function layer is the current candidate for the missing bridge between feasible-set construction and marginal response. It is formally defined here but is not promoted to universal primitive status and does not establish reinforcement or polarity.
