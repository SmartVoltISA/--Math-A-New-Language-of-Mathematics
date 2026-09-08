# Ω-Math v0.9 — Experiment: Causal Intervention and Baseline Observational Equivalence

**ID:** EXPERIMENT_CAUSAL_INTERVENTION_012  
**Status:** EXECUTED / FINITE EXHAUSTIVE VERIFICATION  
**Scope:** causal intervention as explicit transformation/input semantics; no new Ω primitive proposed.

## 1. Question

Can causal intervention be represented using the existing Ω transformation/input layer, while demonstrating that temporal succession and baseline observation alone do not determine causal direction?

Secondary question: can quotienting erase an interventionally relevant distinction?

## 2. Frozen Ω boundary

No new primitive is introduced. Existing typed objects are used:

- state `S`;
- deterministic transition `T:S×U→S`;
- transformation `I:S→S` representing an intervention/reset;
- observation `O:S→Y`;
- finite-horizon behavior.

An intervention is operationally a declared transformation applied before the transition. A causal effect is therefore a comparison of declared observations/behaviors under different interventions, not a primitive symbol meaning "cause".

## 3. Finite exhaustive model

State space:

`S={(0,0),(0,1),(1,0),(1,1)}`.

All deterministic state-transition functions `T:S→S` were enumerated:

`4^4 = 256` functions.

For every ordered pair `(T1,T2)`, every initial state, and a two-step baseline trajectory, equality was checked. Then one-step trajectories after coordinate-setting interventions were compared.

The coordinate interventions were explicit transformations:

`setX_v(x,y)=(v,y)`

`setY_v(x,y)=(x,v)`.

## 4. Exhaustive result A — temporal succession is not causality

Across all `256×256×4 = 262,144` ordered model/start cases:

- **28,672** cases had identical two-step baseline trajectories for the two models;
- **25,344** of those also admitted an intervention (`setX_v` or `setY_v`) that produced different one-step outcomes.

Thus baseline temporal behavior can be identical while intervention behavior differs.

This is a finite counterexample to the inference:

`same observed succession ⇒ same causal structure`.

It does **not** establish a universal causal theory; it establishes the insufficiency of baseline succession on the tested finite domain.

## 5. Explicit directional counterexample

Two models are:

`M_X→Y: X'=X,  Y'=X`

`M_Y→X: X'=Y,  Y'=Y`.

From baseline state `(0,0)`, both produce the identical trajectory

`(0,0) → (0,0) → (0,0) → ...`.

Under `setX_1`:

- `M_X→Y` gives `(1,1)` after the transition;
- `M_Y→X` gives `(0,0)` after the transition.

Under `setY_1` the distinction reverses:

- `M_X→Y` gives `(0,0)`;
- `M_Y→X` gives `(1,1)`.

Therefore intervention distinguishes directional models that baseline succession from the chosen initial state cannot distinguish.

## 6. Exhaustive result B — intervention is reducible to existing transformation semantics

The intervention operations used above are ordinary deterministic functions on the existing finite state space. No new object type is required to represent them.

The causal comparison is consequently expressible as:

`O(B(T,I,S,h)) ≠ O(B(T,I',S,h))`

for declared interventions `I,I'`, observation `O`, transition rule `T`, and horizon `h`.

The semantic content is supplied by the declared intervention class and comparison criterion, not by a new primitive `CAUSE`.

## 7. Quotient / information-loss boundary

If a quotient `Q` identifies states or intervention outcomes that differ before reduction, then an interventionally relevant distinction may disappear after quotienting.

Therefore causal sufficiency must be tested after reduction just as behavioral sufficiency is tested elsewhere in Ω-Math:

`Q(x)=Q(y) ⇒ F_I(x)=F_I(y)`

for the declared intervention task.

This is a task-relative sufficiency condition, not an automatic property of a quotient.

## 8. Decision

**PASS — intervention is representable by existing typed transformations/inputs.**

**PASS — baseline temporal succession is insufficient to determine causal/interventional structure on the tested finite domain.**

**PASS — directional models can be observationally indistinguishable from a baseline state yet interventionally distinguishable.**

**OPEN — causal direction/dependency for multi-variable systems requires an explicit intervention model and comparison criterion; it is not derived from temporal order alone.**

**NO NEW PRIMITIVE JUSTIFIED.**

## 9. Boundary of claim

This experiment does not prove a universal definition of causality, physical causation, or causal discovery. It verifies only the representational and finite counterexample claims above.

The next research frontier is **multi-variable causal dependency and intervention sufficiency**, followed by probability/uncertainty if required.

`sequence ≠ causality`  
`observation ≠ intervention`  
`temporal order ≠ causal direction`  
`causal claim requires declared intervention semantics`
