# Ω-Math — Independent Invariant Stack v1.0

Date: 2026-09-09  
Execution: local Python, deterministic seed 20260909.

## Question

Does the directed-response asymmetry contain an invariant component that survives arbitrary node relabelling and positive global rescaling, while reversing sign under complete direction reversal?

## Independent model class

100 random strongly connected directed weighted graphs:
- N ∈ {8, 12, 20, 32};
- 25 realizations per N;
- random directed edges with p=0.22;
- a directed cycle is inserted only to guarantee strong connectivity;
- positive edge weights in [0.2, 2.0];
- all-pairs directed shortest paths are computed.

The model has no ring response kernel and no prescribed geometric coordinates.

## Critical methodological correction

The signed pairwise statistic using the convention `i < j` is **not** invariant under arbitrary node relabelling: relabelling changes which member of a pair is written first and can change the signed mean.

Therefore the invariant candidate is restricted to:
- mean absolute normalized asymmetry;
- RMS normalized asymmetry.

The signed statistic is retained only as an orientation-sensitive quantity under a fixed labelling, and under full direction reversal it changes sign.

## Tests

For every graph:
1. Relabel all nodes by a random permutation.
2. Multiply all path costs by 17.3.
3. Transpose the directed distance matrix (reverse every direction).

Acceptance:
- magnitude statistics unchanged after relabelling;
- magnitude statistics unchanged under positive scale;
- direction reversal flips signed mean;
- direction reversal preserves magnitude statistics.

## Result

All **100/100** random graphs passed all four checks.

`magnitude_relabel_invariance = PASS`

`magnitude_positive_scale_invariance = PASS`

`direction_reversal_signed_flip = PASS`

`direction_reversal_magnitude_invariance = PASS`

Mean-absolute asymmetry remained nonzero across the tested realizations, with observed range approximately **0.16–0.47**.

## Interpretation

This independently supports a narrower and cleaner invariant statement:

> A directed relational response structure admits label-independent magnitude measures of nonreciprocity that are invariant under positive global rescaling and whose orientation-sensitive component reverses under direction reversal.

This is stronger than the ring-only test because the same property survives on an independent random-graph model class.

It does **not** prove physical geometry, physical direction, or a universal fundamental arrow. It also does not establish that the invariant uniquely characterizes all directed relational systems.

## Status

**SUPPORTED — independent model class.**

Not yet foundational. Further tests should include dynamic response matrices rather than shortest-path constructions and explicit coarse-graining on heterogeneous random graphs.
