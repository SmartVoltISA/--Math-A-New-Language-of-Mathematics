# Ω-Math Experiment — LIGHT Bridge 003

## Status

`EXECUTED / FINITE VERIFICATION`

## Question

Can declared locality be distinguished computationally from ordinary graph connectivity while keeping the Ω v0.9 primitive type system unchanged?

## Frozen setup

Four entities:

`A, B, C, D`

Two directed connected graphs:

### G1 — chain

`A→B`, `B→C`, `C→D`

### G2 — outward star

`A→B`, `A→C`, `A→D`

Both have:

- 4 entities;
- 3 directed relations;
- one weakly connected component;
- the same relation-sign assignment when all signs are `+1`.

The declared propagation rule follows outgoing relations for one step at a time.

## Executed finite test

Starting from `A`, reachable sets were computed for horizons `h=1,2,3`.

| horizon | G1 chain | G2 star |
|---|---|---|
| `h=1` | `{A,B}` | `{A,B,C,D}` |
| `h=2` | `{A,B,C}` | `{A,B,C,D}` |
| `h=3` | `{A,B,C,D}` | `{A,B,C,D}` |

The computation is exhaustive for these two finite graphs and the declared deterministic propagation rule.

## Result

The graphs share coarse connectivity properties but have different propagation neighborhoods and arrival structure.

Therefore:

`connectivity ≠ propagation locality`.

More precisely, ordinary connectedness does not determine the one-step local successor relation or finite-horizon propagation profile.

## Ω interpretation

This does not require a new primitive type. A locality predicate may remain a declared semantic structure over entities/configurations:

`Loc_C(x,y) ∈ {false,true}`.

The experiment therefore supports the weaker architectural rule:

> When transition semantics depend on locality, locality must be explicitly declared; it cannot be inferred universally from connectedness alone.

## Limits

This is not a physical derivation of spacetime locality. It is a finite graph-model verification of a representational boundary motivated by LIGHT.

It also does not show that every useful notion of locality is independent of graph structure. It shows only that connectivity alone is insufficient for the tested propagation task.

## Decision

`PASS — locality is a distinct semantic condition from ordinary connectivity.`

No primitive extension to Ω-Math v0.9 is justified by this result.
