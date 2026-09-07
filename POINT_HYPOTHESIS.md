# Ω-Math — Point Hypothesis v0.1

## Purpose

This document formalizes a research hypothesis proposed in the Ω-Math program. The object is called a **Point** (`Π`) to avoid importing a physical interpretation such as a black hole into the definition.

The hypothesis concerns a limiting organization of relations, not the literal geometric size of an object.

## 1. Starting structure

A system is:

`Ω=(E,R,D_R)`

with entities `e_i=(i,s_i)` and relations defined only on their domain.

Partition a system for an experiment into:

`Ω = I ∪ B ∪ X`

where `I` is an interior region, `B` a candidate boundary, and `X` the exterior.

The partition is experimental bookkeeping, not a new primitive of Ω-Math.

## 2. Two independent directions

### Direction A — inward relational closure

Let:

- `R_II` = relations whose endpoints are both in `I`;
- `R_IB` = relations between `I` and `B`;
- `R_IX` = relations between `I` and `X`.

Define the measured closure ratio:

`C_in = R_II / (R_II + R_IB + R_IX)`

and the corresponding external-coupling ratio:

`C_out = (R_IB + R_IX) / (R_II + R_IB + R_IX)`.

Thus `C_in + C_out = 1` for this measurement definition.

The Point hypothesis predicts a limiting regime:

`C_in → 1`

and

`C_out → 0`.

This does **not** require entities inside the system to become identical.

### Direction B — outward information through a boundary

Let `O_B` denote the information available through the chosen boundary representation. Let `O_I` denote information required to distinguish internal configurations.

The hypothesis is that increasing internal relational closure can coexist with a nonzero boundary channel:

`I_boundary > 0`

while external access to internal detail becomes compressed or quotient-like.

The key distinction is:

`internal distinguishability ≠ external distinguishability`.

A loss of external distinguishability is not by itself structural destruction.

## 3. Candidate Point condition

A Point is a limiting organizational regime satisfying, relative to a specified experimental partition and observation class:

`C_in → 1`

`C_out → 0`

while at least some internal distinctions remain structurally meaningful.

A possible additional condition is a persistent boundary information channel:

`I_boundary > 0`.

The last condition is a hypothesis to test, not part of the minimal definition.

## 4. Energy channel is deliberately separate

Energy is not currently a primitive of Ω-Math. Therefore the statement that “energy comes out” cannot be encoded as an Ω-Math theorem yet.

If a future physical bridge introduces an independently defined energy-like observable `E` and boundary flux `Φ_E`, then the relevant test is whether a Point-like relational regime can satisfy:

`C_in → 1`, `C_out → 0`, and `Φ_E ≠ 0`.

This is a future physical test, not a current result.

## 5. What would count as evidence

Support for the structural hypothesis requires a model in which the Point-like regime emerges from relational rules rather than being imposed by hand.

At minimum we must observe:

1. increasing internal closure;
2. decreasing external coupling;
3. persistence of internal structural distinctions;
4. an identifiable boundary or equivalent separating interface, if one is claimed;
5. robustness under relabeling and reasonable null models.

## 6. What would falsify or weaken it

The hypothesis is weakened if:

- closure requires manually forcing all relations into self-loops;
- the boundary is inserted solely to produce the desired result;
- internal distinctions disappear simultaneously and no nontrivial structure remains;
- the behavior is reproduced equally by random/null systems;
- the result depends on arbitrary labels rather than relational structure.

## 7. Physical interpretation

No identification with a black hole is made here.

A later comparison may ask whether a Point-like regime has a correspondence with known gravitational systems. Such a correspondence must be established from independently defined quantities and predictions.

## Status

`HYPOTHESIS` — formal target for controlled experiments.

Not a physical claim.
