# Ω-Math — Task-Relative Sufficient Relational State

**Status:** DERIVED / EXECUTED framework; comparison with existing behavioral-equivalence methods remains OPEN.

## 1. Purpose

Ω-Math needs a precise answer to a central question:

> When is a reduced representation of a relational state sufficient for a declared task?

The answer must be task-relative. No structural summary is assumed to be universally sufficient.

## 2. Declared transition system

Let

`S` — state space;

`U` — declared input space;

`T:S×U→S` — deterministic transition rule;

`O:S→Y` — declared observation.

For an input sequence

`u=(u_0,...,u_{h-1})`

and initial state `s`, define the trajectory

`T^0_u(s)=s`

and

`T^{k+1}_u(s)=T(T^k_u(s),u_k)`.

The finite-horizon behavior is

`B_h(s,u)=(O(T^0_u(s)),...,O(T^h_u(s)))`.

## 3. Behavioral equivalence

For a fixed horizon `h`, define

`s ≈_h s'`

iff

`B_h(s,u)=B_h(s',u)`

for every admissible input sequence `u` of length `h`.

Thus two states are equivalent exactly when the declared task cannot distinguish them within the declared horizon under any allowed input sequence.

## 4. Sufficient representation

A reduction

`Q_h:S→Z`

is sufficient for the finite-horizon task `B_h` when

`Q_h(s)=Q_h(s') ⇒ B_h(s,u)=B_h(s',u)`

for every admissible `u`.

Equivalently, behavior factors through the reduction:

`B_h = B̄_h ∘ Q_h`.

This is the Ω-Math form of the principle:

**compression is not equivalence; a reduction is sufficient only when the discarded information cannot change the declared task output.**

## 5. Coarsest task-preserving quotient

Define the canonical finite-horizon quotient

`[s]_h = {s' ∈ S : s' ≈_h s}`.

Let

`Q_h(s)=[s]_h`.

Then `Q_h` is sufficient for `B_h` by construction.

Moreover, it is the coarsest equivalence relation that preserves the complete declared finite-horizon behavior: any other task-sufficient representation may distinguish states that `Q_h` identifies, but cannot identify two states that `Q_h` distinguishes without losing some declared behavior.

This is a theorem of the declared deterministic model, not a claim that this construction is globally new mathematics.

## 6. Horizon nesting

If `h+1`-step behavior is preserved, then `h`-step behavior is preserved:

`≈_{h+1} ⊆ ≈_h`.

Therefore increasing the horizon can only split equivalence classes; it cannot merge previously distinguished states.

This produces a hierarchy:

`Q_0 → Q_1 → Q_2 → ...`

where each later quotient retains at least as much task-relevant information as the preceding one.

## 7. Relation to structural reductions

A structural descriptor such as a source-distance profile is a candidate `Q`.

It is admissible only after testing:

`Q(x)=Q(y) ⇒ B_h(x,u)=B_h(y)`.

Experiment `EXPERIMENT_PATH_PROFILE_004.md` provides a positive counterexample to the sufficiency of source-distance profile for a declared triangle-gated propagation dynamics.

Therefore:

`source-distance profile ≠ complete task-sufficient relational state`.

The failure does not invalidate distance profiles. It establishes only that the profile is insufficient for that declared task.

## 8. Recursive construction

For deterministic systems, a finite-horizon behavioral partition can be constructed recursively.

Base level:

`Q_0(s)=O(s)`.

Recursive level:

`Q_{h+1}(s)` retains the current observation together with the task-relevant responses of successor states under every declared input:

`Q_{h+1}(s) = (O(s), { (u,Q_h(T(s,u))) : u∈U })`.

The exact representation of the successor collection depends on whether `U` is ordered, finite, continuous, or otherwise structured; no silent set/multiset identification is allowed.

For finite deterministic systems this gives a direct constructive route to the finite-horizon behavioral quotient.

## 9. Why this matters for Ω-Math

This gives Ω-Math a precise stopping rule for reduction:

Do not ask whether a representation is "complete" in the abstract.

Ask:

1. What is the task?
2. What is observable?
3. What transitions are admissible?
4. What horizon is declared?
5. Which states remain behaviorally distinguishable?
6. Does the proposed reduction preserve exactly those distinctions?

A representation can therefore be:

- sufficient for one task and insufficient for another;
- sufficient for horizon `h` and insufficient for `h+1`;
- structurally informative but behaviorally lossy;
- behaviorally sufficient while discarding irrelevant structural detail.

## 10. Ω-Math object: sufficient relational state

For a declared task

`𝒟=(T,O,U,h)`

define the task-relative sufficient relational state as the quotient

`SR_𝒟(s) = [s]_h`.

This is not a new primitive entity type. It is a derived quotient object whose meaning is completely determined by the declared task.

## 11. Verification requirements

Before promoting any concrete `Q` to a canonical Ω-Math reduction, test:

- reflexivity of the induced equivalence;
- symmetry;
- transitivity;
- observation preservation;
- transition-response preservation;
- exhaustive sufficiency on finite models where possible;
- counterexamples outside the tested domain;
- comparison with existing notions of behavioral equivalence, bisimulation, automata minimization and sufficient statistics.

## 12. Current status

**DERIVED:** task-relative sufficiency condition and finite-horizon quotient construction.

**EXECUTED:** structural source-distance profile has been falsified as universally sufficient for at least one explicit dynamics.

**OPEN:** full comparison with established bisimulation/minimization theory; treatment of nondeterministic systems; infinite state/input spaces; probabilistic transitions; continuous observations; causal/interventional tasks.

**No global novelty claim is made.**

## 13. Core rule

> A representation is not complete because it describes much of a system. It is sufficient only when every distinction removed by the representation is irrelevant to the declared task.
