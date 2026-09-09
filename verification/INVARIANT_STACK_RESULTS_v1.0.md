# Ω-Math Invariant Stack Results v1.0

Execution mode: **local Python**, deterministic seed 20260909.

## Question

Can a directional response observable survive transformations that should not change the underlying relational organization?

Tested transformations:

1. node relabelling;
2. positive global scaling of response costs;
3. contiguous coarse-graining;
4. complete direction reversal.

The candidate observable is the normalized antisymmetric response

`A(i,j) = (D(i,j) - D(j,i)) / (D(i,j) + D(j,i))`.

It is used only as an operational graph observable. No physical unit is assumed.

## Model

A 64-node directed periodic ring is generated from right/left response speeds
`c_R = 0.32`, `c_L = 0.14`.

Baseline signature:

- signed mean: **-0.179139639**
- mean absolute asymmetry: **0.3118863959**
- RMS asymmetry: **0.3344268649**

## Results

### 1. Node relabelling

A random permutation of all node labels leaves the complete response-value multiset and the normalized antisymmetry signature unchanged.

**PASS**

### 2. Positive scale transformation

Scales `0.01, 0.1, 1, 10, 100` leave the normalized antisymmetry signature unchanged.

**PASS**

This blocks interpreting the signal as dependent on an arbitrary choice of response units.

### 3. Coarse-graining

Contiguous blocks preserve nonzero directional signal:

| block size | coarse nodes | mean absolute asymmetry |
|---:|---:|---:|
| 2 | 32 | 0.3116373507 |
| 4 | 16 | 0.3068173830 |
| 8 | 8 | 0.2912202071 |

**PASS for tested coarse-grainings.**

This is not a claim that arbitrary coarse-graining preserves directionality. A partition that merges distinguishability can still destroy identifiability.

### 4. Direction reversal

Replacing `D` by `D^T` flips the signed mean from `-0.179139639` to `+0.179139639`, while preserving mean absolute and RMS asymmetry.

**PASS**

Thus the observable separates orientation magnitude from orientation sign.

## Unified result

The tested directional observable has the following transformation behavior:

`relabel → invariant`

`positive scale → invariant`

`tested coarse-graining → retained`

`direction reversal → signed orientation flips, magnitude retained`

This is stronger than invariance of raw edge weights. The candidate object is therefore better represented as an **equivalence-class-level directed response structure** than as a particular coordinate-labelled graph.

## Scientific boundary

This result does **not** prove physical space, physical time, or a fundamental arrow of time. It establishes only that a directed relational response signature can be formulated so that several representation changes do not alter its essential magnitude, while reversal acts as a controlled orientation operation.

The coarse-graining result is model- and partition-dependent and therefore remains a tested property, not a universal axiom.

## Status

**SUPPORT — operational invariant stack established for the tested directed-response model.**

Not promoted to a foundational primitive yet. Promotion remains gated by independent reuse in another model family and explicit verification of the same transformation behavior.
