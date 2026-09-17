# Ω-037 — Computational Results v1.0

**Status:** VALIDATED FOR DECLARED FINITE MODEL / OPEN FOR GENERALIZATION
**Experiment:** `O037_VALUE_REINFORCEMENT_POLARITY_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

A deterministic computational check was run on the declared finite alternative model with 100 fixed seeds (`0..99`). The analytical triangle control was also evaluated directly.

Environment used for this run: Python numerical execution environment available to the experimenter. The result is a model-level validation, not a physical validation.

## 2. Feasible-set / value-function control

For a triangle with three possible edges and:

`F(K) = { C : |C| ≥ K }`

`J(C)=|C|`

obtained:

`K = 0,1,2,3,4`

`V(K) = 0,1,2,3,∞`

Thus the empty-feasible-set case at `K=4` is explicit, and the optimum exists for `K=0..3`.

The feasible-set inclusion monotonicity control holds for the finite cases: tightening the constraint raises the minimum attainable objective.

## 3. Value alone versus reinforcement

Control A computes value/sensitivity without an update law. The computed `ΔV` is a mathematical quantity, while reinforcement remains absent because no state-update rule exists.

Therefore the computation supplies a direct counterexample to the strong implication:

`ΔV < 0 → reinforcement`

and, more generally, to the claim that marginal value by itself is an update mechanism.

## 4. Explicit reinforcement law

Treatment C used the preregistered example:

`a_i = exp(-βJ_i) / Σ_j exp(-βJ_j)`

`W_i(t+1)=W_i(t)+ηa_i`

with `β=2`, `η=0.1`, 20 update steps.

Across 100 fixed seeds, the Pearson correlation between candidate cost and accumulated reinforcement increment had:

- mean correlation ≈ `-0.9765`;
- median correlation ≈ `-0.9874`.

This shows that, inside this declared update law, lower objective value is strongly associated with greater reinforcement.

Crucially, this does **not** derive reinforcement from `ΔV`. The association is introduced by the explicit allocation/update rule `U`.

## 5. Permutation negative control

The same reinforcement increments were compared with a randomly permuted cost signal per run.

Across 100 runs:

- mean correlation after permutation ≈ `-0.0728`;
- median ≈ `0.0993`.

The strong negative association of the unpermuted treatment therefore disappears under the representation-matched permutation control in this finite model.

This supports the narrower statement that the declared value-coupled update law uses the objective signal, rather than producing the same association independently of it.

## 6. Reinforcement versus polarity

The reinforcement state uses nonnegative weights. Without a signed contrast or partition rule, there is no mathematical positive/negative polarity variable in the model.

Adding an explicit map such as:

`P(i,j)=sign(W_i-W_j)`

creates a polarity observable by definition. The sign is then a derived observable of the declared comparison rule; it is not supplied by reinforcement alone.

Hence:

`reinforcement → polarity`

is not established as a law. The computation instead confirms the need to declare the polarity map before measuring persistence or sign stability.

## 7. Representation controls

For scalar objective values `[0,1,2,3]`:

- identity objective selects index `0`;
- strictly increasing transform `exp(J)` also selects index `0`;
- non-monotone transform `(J-2)^2` selects index `2`.

Therefore strict monotone reparameterization preserves the argmin in the tested case, while a non-monotone transformation can change it, as required by the preregistration.

## 8. What was actually established

### ESTABLISHED IN THIS MODEL

1. Feasible-set definition and value-function minimization are computationally separable.
2. Empty feasible sets must be represented explicitly.
3. Tightening the finite feasible set cannot lower the minimum under the same objective in the tested construction.
4. `ΔV` can exist without any reinforcement mechanism.
5. Reinforcement appears when an explicit allocation/update law is supplied.
6. In the chosen softmax law, lower objective values receive greater allocation.
7. Permuting the objective signal destroys most of that association in the tested finite runs.
8. Nonnegative reinforcement does not itself define signed polarity.
9. A declared polarity map is an additional model ingredient.
10. Strictly increasing objective transforms preserve selection in the tested scalar case; non-monotone transforms need not.

### NOT ESTABLISHED

- a universal law `marginal cost ↓ → reinforcement`;
- a universal law `reinforcement → polarity`;
- physical energy correspondence;
- physical causality;
- universality outside the declared finite model and update family.

## 9. Decision

**H1:** PASS for the declared finite value-function/sensitivity construction and its representation/inclusion controls.

**H2:** PASS for the narrow sufficiency gate: sensitivity alone does not generate reinforcement; an explicit update mechanism is required. The stronger claim that sensitivity is universally predictive remains OPEN.

**H3:** PASS for the definitional gate: reinforcement without a signed/partition rule does not define polarity. General physical/biological polarity remains OPEN.

**Overall:** `VALIDATED FOR DECLARED FINITE MODEL / OPEN FOR GENERALIZATION`.

## 10. Fixation

The research chain is fixed for the next stage as:

`constraints → feasible set → objective → value function → optimum set → marginal sensitivity → explicit update/feedback → reinforcement → explicit polarity rule → testable polarity`

The earlier shorthand:

`marginal cost ↓ → reinforcement → polarity`

must remain labelled **HYPOTHESIS**, not theorem.

Next stage should test whether the same separation survives richer graph dynamics, history dependence/memory, competing channels, and independently declared objective families.
