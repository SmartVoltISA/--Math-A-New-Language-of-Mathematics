# Ω-Math — Internal Order and Time Layer v0.1

## 1. Goal

Separate three objects that are often silently identified:

`order of transitions`

`count of transitions`

`physical duration`.

## 2. Transition order

For a deterministic trajectory

`S₀ → S₁ → ... → Sₙ`

define the ordinal transition index:

`τ(S_k)=k`.

This is derived from the ordered transition sequence. No clock is required.

## 3. Horizon

A finite behavior horizon is a number of admissible transitions:

`h ∈ ℕ₀`.

The horizon controls how far future behavior is compared. It is not a physical time interval.

## 4. Duration candidate

A physical duration would require an independently measured mapping

`G : transition history → ℝ_{≥0}`

such that experimentally measured durations are reproduced within declared tolerance.

No such mapping is assumed by Ω-Math.

## 5. Event-weighted internal clock

A model may assign a declared positive weight to each transition/event:

`w(T_i)>0`.

Then an internal accumulated coordinate can be defined:

`θ_n = Σ_{i=0}^{n-1} w(T_i)`.

This is a model-derived path length in transition space. It becomes a physical time candidate only if independently calibrated against physical clocks and survives controls.

## 6. Invariance requirement

A temporal coordinate intended to describe system dynamics rather than labels should be invariant under representation-only relabelings.

If

`π(S_k)`

is a pure relabeling, then the corresponding internal ordering must remain unchanged.

## 7. Reparameterization

Different positive event weights may preserve event order while changing numerical duration:

`S₀→S₁→S₂`

can have

`θ=(0,1,2)`

or

`θ=(0,3,5)`.

Therefore ordering alone does not determine a unique metric duration.

This is the key boundary:

`order < duration`.

## 8. Nondeterministic case

For

`N(S,U)⊆S`

there may be many future trajectories. A temporal coordinate must therefore be attached to each realized branch or defined on the branching structure.

No branch may be selected merely to manufacture a unique clock.

## 9. Memory relation

A retained state may distinguish otherwise identical current observations and thereby affect future transition structure. Consequently a temporal description based only on current observation can be insufficient for prediction.

This follows the general Ω reduction rule:

`same representation ⇒ same declared task behavior`.

## 10. Result

**DEFINED:** transition order.

**DEFINED:** finite transition horizon.

**DERIVED:** transition-count coordinate.

**DERIVED CANDIDATE:** weighted internal path coordinate.

**OPEN:** physical duration and physical time.

## 11. Falsification target

Any proposed Ω physical-time mapping must fail if it:

- depends on arbitrary labels;
- depends on an unreported coordinate choice;
- cannot distinguish models with different measured durations;
- changes under an allowed reparameterization without a declared physical reason;
- merely renames an external clock.

## Status

`DEFINED / PHYSICAL BRIDGE OPEN`
