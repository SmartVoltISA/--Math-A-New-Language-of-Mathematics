# Ω-Math v0.9 — Dynamics, Memory and Feedback

## 1. State and transition

A system state is a configuration together with explicitly retained variables:

`S=(C,M,X)`.

A deterministic transition is:

`S' = T(S,U)`

where `U` is an optional declared input.

For nondeterministic dynamics:

`N:S×U→𝒫(S)`.

The successor set is first-class; arbitrary branch selection is not permitted as a semantic shortcut.

## 2. Internal order and horizon

A realized trajectory has an ordered sequence:

`S₀→S₁→...→Sₙ`.

The transition index `τ(S_k)=k` gives internal order. A finite horizon `h∈ℕ₀` counts admissible transitions and is not physical duration.

Physical time requires an independent empirical bridge.

## 3. Functional memory

A stored record is not automatically memory.

Functional memory requires retained state that persists and produces a demonstrated later effect under a controlled comparison/intervention.

A minimal model may use:

`M_{t+1}=U_M(M_t,S_t,X_t)`

and

`S_{t+1}=T(S_t,M_t,X_t)`.

The research question is not maximum capacity but the smallest retained state sufficient to alter the declared future behavior.

## 4. Predictive state

For a specified prediction task, a representation is sufficient only if it preserves the required conditional behavior under the stated process/distribution.

A probabilistic expression such as

`P(Y|history)=P(Y|Q(history))`

requires an independently declared probabilistic model; probability is not primitive in Ω-Math.

## 5. Behavioral equivalence

Finite-horizon behavioral equivalence is task-relative. For deterministic systems it compares future observation trajectories under all declared input sequences up to the horizon.

The verified finite construction shows recursive behavioral signatures agree with direct exhaustive comparison on the tested finite deterministic domain.

For nondeterministic systems, equivalence must explicitly choose semantics such as trace/output, branching-sensitive, existential reachability or universal safety.

## 6. Causality

Temporal succession is not causality.

A causal claim requires explicit intervention/counterfactual semantics. A possible intervention operator is:

`I:S×A→S`.

No causal interpretation is inferred merely from a transition sequence.

## 7. Feedback

A graph cycle is not automatically a causal feedback loop.

A feedback claim requires direction, transition semantics and evidence that a later state influences subsequent dynamics that return to an earlier process or variable.

## 8. Self-model

Let `H_t` be an internal representation of system state. A self-model candidate requires:

`H_t=F(S_t)`

and functional use in subsequent dynamics:

`S_{t+1}=T(S_t,H_t,U_t)`.

This is a formal candidate, not a definition of consciousness.

## 9. Emergence

A macro-structure is an emergence candidate only when coarse-graining/identification is explicit and a higher-level property or behavior is demonstrated with persistence/prediction criteria and controls.

`description ≠ explanation`.

## 10. Geometry and dynamics

Geometry is not assumed to determine behavior. Experiments in the repository show that unsigned topology/geometry can be identical while relation signs change behavior under sign-sensitive dynamics.

Likewise, compact path summaries can erase intermediate organization relevant to dynamics.

Therefore:

`same descriptor ⇒ same behavior`

must be demonstrated for the declared task before the descriptor can replace the full state.

## 11. Research rule

Do not infer:

`sequence → causality`

`memory → consciousness`

`feedback → life`

`stable pattern → universal emergence`

`geometry → complete state`.

Each arrow is a separate testable claim.

## Status

`CANONICAL / v0.9 SYNCHRONIZED`
