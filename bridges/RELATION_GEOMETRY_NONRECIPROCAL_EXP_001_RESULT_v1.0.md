# RELATION-GEOMETRY-NONRECIPROCAL-001 — Result v1.0

**Status:** EXECUTED — SYNTHETIC CONTROLLED EXPERIMENT  
**Date:** 2026-09-09  
**Seed:** 20260909  
**Noise bound:** ±0.10 per directed edge  
**Model size:** 8 nodes, directed ring

## Question

Can a directed response-cost structure produce operationally distinct `D(i -> j)` and `D(j -> i)` while surviving direction reversal and a valid relabelling transformation?

## Hypothesis

A directed relation can induce a non-symmetric path-cost structure for the tested model.

## Null

The apparent asymmetry is generated equally by a reciprocal system or disappears under the declared controls.

## Model

For every adjacent pair on an 8-node directed ring:

- asymmetric model: clockwise edge cost = `1.0 ± 0.10`; reverse edge cost = `3.0 ± 0.10`;
- reciprocal control: both directions use `2.0 ± 0.10`;
- shortest directed path cost defines the operational observable `D(i -> j)`.

The observable is a graph response cost. It is **not** identified with physical distance, time, energy, or spacetime.

## Locked test pairs

`(i, i+3 mod 8)` for all eight starting nodes.

## Results

Asymmetric model:

- mean `|D(i -> j) - D(j -> i)|` = **2.039590**
- all eight directional differences were below `-1.83` under the declared noise draw;
- direction reversal changed the sign of every measured difference exactly.

Reciprocal control:

- mean `|D(i -> j) - D(j -> i)|` = **0.134806**;
- maximum absolute asymmetry = **0.217330**.

Thus the observed asymmetric signal was approximately 15.1× larger than the reciprocal-control mean absolute asymmetry.

## Relabelling control

A fixed permutation `(3,6,1,7,0,4,2,5)` was applied to every node label and the ordered test pairs were transformed by the same permutation. The complete vector of directional differences was unchanged.

**PASS — representation survives valid relabelling.**

## Explicit reverse-edge control

Both directions were explicitly present as separate directed edges. The experiment did not infer an inverse edge from a forward edge, and the two directed edges remained distinct.

**PASS — reverse relation is not silently invented.**

## Interpretation

**SUPPORT for the hypothesis within this synthetic graph model.** The tested system contains a stable non-reciprocal operational path-cost structure that survives the declared relabelling and direction-reversal controls and is much larger than the reciprocal-control asymmetry under the same noisy sampling scheme.

This is **not** evidence for physical non-reciprocal geometry, spacetime, universal emergence, or a universal metric. It is a controlled model result.

## Falsification boundary

The result would not support the hypothesis if the asymmetry disappeared under the relabelling/direction controls or were of comparable magnitude in the reciprocal null.

## Ω-Math boundary

No physical time, physical space, physical energy, probability, causality, or automatic inverse relation was introduced into Ω-Math primitives. The experiment remains an external research-layer result; only typed observations may be bridged into Ω-Math.
