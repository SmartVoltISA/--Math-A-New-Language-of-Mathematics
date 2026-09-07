# Ω-Math v0.1 — Dynamics, Order and Memory

## 1. State

A system state is:

`Ω_t = (E_t, R_t, D_R,t)`

A transition is:

`Ω_t → Ω_t+1`

or more explicitly:

`Ω_t+1 = T(Ω_t, U_t)`

where `U_t` is external input when present.

## 2. Internal order

A sequence of states can be represented without assuming that the model's first primitive is a physical clock:

`Ω₀ → Ω₁ → Ω₂ → ...`

The order is carried by the transition relation.

Ω-0 already tested a minimal construction in which an updating trace created an internally distinguishable before/after state. The reported mechanism was:

`ACT → TRACE → UPDATE`

The result was deliberately limited to formal internal order and was not interpreted as a proof that physical time is emergent. fileciteturn10file0

## 3. Functional memory

A stored record is not automatically memory.

Operational definition:

`memory = retained state that can causally affect a later system behavior or comparison`

This distinguishes:

`recording ≠ memory`

and

`persistent state + causal influence → candidate functional memory`.

## 4. Memory update

Let `M_t` be internal memory.

A minimal memory system has:

`M_t+1 = U_M(M_t, Ω_t, X_t)`

and future behavior:

`Ω_t+1 = T(Ω_t, M_t, X_t)`.

If changing `M_t` changes later behavior under controlled intervention, the memory has demonstrated causal function.

## 5. Minimality

The goal is not to maximize memory capacity.

The question is:

> What is the smallest retained state that changes future behavior in a reproducible way?

This connects directly to Ω-MEM research.

## 6. Predictive state

A memory representation is sufficient for a task if states with the same representation have the same relevant conditional prediction under the tested process.

For a process `X_t`, a candidate sufficient state `S_t` aims to satisfy:

`P(X_t+1 | history) = P(X_t+1 | S_t)`

for the prediction task and distribution under study.

This is a task-relative statement, not a universal claim that one memory representation is sufficient for every process.

Ω-MEM-4R provides a useful warning: three of four tested structured processes favored the matched representation over random controls at representative equal capacity, but Thue-Morse was a critical counterexample. fileciteturn11file0

## 7. Causality

Ω-Math must distinguish temporal succession from causal influence.

`A before B` does not by itself imply:

`A causes B`.

A candidate causal relation requires an intervention or another explicit identification criterion.

For an intervention `do(A=a)`, a causal effect can be operationalized as a difference in the distribution of a later observable `Y`:

`P(Y | do(A=a₁)) ≠ P(Y | do(A=a₂))`.

This notation is borrowed as a comparison tool; causal semantics are not a primitive of Ω-Math v0.1.

## 8. Feedback

A feedback loop exists when a later state can influence a future state that eventually affects the earlier process class again.

Minimal schematic form:

`A → B → ... → A'`

A cycle in a graph is not automatically a causal feedback loop. Direction, transition rules and intervention evidence are required.

## 9. Self-model

Let the physical/system state be `Ω_t` and an internal representation be `H_t`.

A self-model candidate satisfies:

`H_t = F(Ω_t)`

and the represented state participates in subsequent transition:

`Ω_t+1 = T(Ω_t, H_t, U_t)`.

The system then contains a representation of itself that has functional consequences.

This is a formal candidate, not a definition of consciousness.

## 10. Consciousness research layer

A consciousness hypothesis can be tested only after lower-level properties are operationalized.

Candidate ingredients:

`distinguishability`
`persistent memory`
`integrated state`
`self-model`
`feedback`
`counterfactual sensitivity`

A proposed consciousness metric must predict behavior or internal observables better than appropriate controls.

The language does not assume that any particular metric is consciousness.

## 11. Time research

A candidate internal time variable may be derived from ordered state transitions:

`Ω₀ → Ω₁ → ... → Ωₙ`.

A stronger hypothesis would claim that a useful temporal coordinate can be reconstructed from structural change alone.

That stronger claim requires experiments against systems where an external clock is available.

## 12. Dynamics research rule

Never infer:

`sequence → causality`

or

`memory → consciousness`

or

`feedback → life`

without intermediate evidence.

Each arrow is a separate research problem.
