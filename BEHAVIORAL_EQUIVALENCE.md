# Ω-Math v0.9 — Behavioral Equivalence

## 1. Purpose

Ω-Math distinguishes current observational equality from equality of future behavior. A representation can hide differences that become visible only after transitions.

## 2. Finite-horizon behavioral equivalence

Let `O` be an observation map, `T` a deterministic transition rule, and `U` a declared admissible input sequence. For horizon `h ≥ 0`, define `s ≈ₕ s'` when the selected observation criterion agrees for every step `0 ≤ k ≤ h` under the declared inputs.

At `h=0`, this reduces to current observational equivalence under `O`.

## 3. Horizon nesting

By definition,

`≈ₕ₊₁ ⊆ ≈ₕ`.

A larger finite horizon can preserve an equivalence or reveal a distinction; it cannot turn a previously distinguishable pair into an equivalent pair.

## 4. Infinite horizon

` s ≈∞ s' ⇔ ∀h∈ℕ₀, s≈ₕs' `.

Thus `≈∞ = ⋂ₕ≈ₕ`. This is a derived infinite-horizon relation, not a new primitive.

## 5. Behavioral quotient

A quotient is behavior-preserving for a specified task and horizon only when equivalent representatives produce the same selected future observations for the admissible input/intervention class.

Therefore equality of current observations alone does not guarantee behavioral sufficiency.

## 6. Relational systems

Two systems can have the same entity-state multiset while differing in relation organization, memory or other retained variables. Consequently:

`same composition ≠ same organization ≠ same behavior`.

## 7. Nondeterminism

For `N:S×U→𝒫(S)`, the successor set is retained. Behavioral equivalence must explicitly select its semantics, such as trace equality, branching-sensitive equivalence, existential reachability or universal safety. Probability requires a separately declared kernel.

## 8. Memory sufficiency

A representation `Q` is sufficient for task `F` when

`Q(x)=Q(y) ⇒ F(x)=F(y)`

for the declared task, dynamics, observation, input/intervention class and horizon. Sufficiency is therefore task-relative, not a universal scalar property of a state.

## 9. Path consequence

Equal sign products do not imply equal paths, equal structures or equal future behavior. Intermediate organization can remain behaviorally relevant.

`equal summary ≠ equal path ≠ equal structure ≠ equal behavior`.

## 10. Verification status

Finite-horizon nesting and behavioral quotient claims are formally testable and have been checked on finite models in the repository experiments. Those experiments do not establish universal empirical laws.

Nondeterministic and infinite-horizon behavior remain semantics-dependent and must not be collapsed into the deterministic finite-horizon definition.

## 11. Status

`CANONICAL / v0.9 SYNCHRONIZED`
