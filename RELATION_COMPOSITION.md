# Ω-Math v0.9 — Relation Composition

## Decision

Primitive relation-to-relation collapse is **not required** by the minimal language.

Given

`a —r₁→ b —r₂→ c`,

the information-preserving sequential object is the path

`P=(r₁,r₂)`.

Path concatenation is the composition layer:

`r₁ ⧺ r₂ → P`.

## Sign multiplication

For relation signs `{−1,+1}`, multiplication is closed and associative:

`(+,+)→+`, `(+,-)→-`, `(-,+)→-`, `(-,-)→+`.

It is a valid derived **summary** of a path's sign sequence. It is not a universal semantic replacement for the path.

A path can retain intermediate entities, order and multiplicity that sign multiplication discards. Existing counterexamples prevent promotion to a universal primitive relation law.

## Parallel paths

Different paths may connect the same endpoints with different sign summaries. The primitive domain contains no third conflict sign. Combining such paths therefore requires an explicit higher-level aggregation/decision rule rather than a hidden primitive collapse.

## Reversal and identity

The empty path `ε_e` supplies identity for path concatenation. Path reversal `rev(P)` is a sequence operation only; it does not imply that reversed relations exist. Primitive `REL_ID` and `REL_INV` are therefore unnecessary.

## Current status

- `PATH CONCATENATION` — **DEFINED**.
- `EXACT PATH EQUALITY` — **ADMITTED**.
- `SIGN MULTIPLICATION` — **DERIVED SUMMARY**.
- `PRIMITIVE RELATION COMPOSITION` — **NON-PRIMITIVE / NOT REQUIRED**.
- `REL_ID` — **NON-PRIMITIVE**.
- `REL_INV` — **NON-PRIMITIVE**.

## Boundary

`relation + relation → path` is the canonical sequential composition.

`path → primitive relation` is an optional explicit abstraction, not a core law.

No universal mathematical novelty claim is made; the construction is positioned against established composition, path and graph formalisms.

**Status: v0.9 FRONTIER CLOSED**
