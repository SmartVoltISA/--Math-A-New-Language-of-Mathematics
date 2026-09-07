# Ω-Math v0.4 — Reduction and Information-Preservation Rules

## Purpose

This document makes structural reduction explicit. Ω-Math must not silently replace a rich object with a smaller description and then treat the result as equivalent.

## 1. Reduction

A reduction is a map:

`Q:X→Y`

where `Y` contains less or differently organized information than `X`.

Examples:

- path → sign-product;
- configuration → aggregate graph statistics;
- state → observation;
- system → quotient;
- transformation system → scalar distance.

## 2. Task-relative sufficiency

Let `F:X→Z` be the task, behavior, prediction or observation of interest.

`Q` is sufficient for `F` when:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

If this fails, there exist `x,y` that the reduction identifies while the task distinguishes them.

## 3. Behavior-preserving quotient

For a transition system, a quotient `Q` is behavior-preserving for horizon `h` when equivalent representatives generate identical declared observations through `h` under the declared input/intervention class.

The claim is always parameterized by:

`observation + transition rule + inputs/interventions + horizon`.

## 4. Path reduction

The scalar map

`Σ(P)=∏ sign(r)`

is valid as a summary algebra.

It is not behavior-preserving in general. `EXPERIMENT_PATH_DYNAMICS_001.md` gives a deterministic counterexample with equal endpoints, length and signs but different intermediate organization.

## 5. Aggregate graph reduction

Counts, degree sequences, component counts or other aggregates may be useful measurements. Equality of such measurements does not imply structural or behavioral equivalence unless sufficiency is proved for the task.

## 6. Observation reduction

If `O(x)=O(y)`, the correct conclusion is:

`x ≈_O y`.

It is not:

`x=y`.

## 7. Quotient safety condition

A quotient is safe for a declared property `F` when `F` factors through the quotient:

`F = F̄ ∘ Q`.

If such an `F̄` does not exist, the quotient is not sufficient for `F`.

## 8. Information-loss witness

A reduction is proven lossy for a task by constructing:

`x ≠ y`

such that

`Q(x)=Q(y)`

but

`F(x)≠F(y)`.

This is the preferred minimal counterexample pattern.

## 9. Reduction promotion rule

A reduction may be promoted from `summary` to `equivalence-preserving` only after:

1. the task is declared;
2. the information retained by the reduction is declared;
3. counterexample search is performed;
4. a sufficiency proof or exhaustive finite verification is available for the stated domain;
5. controls against representation artifacts are passed.

## 10. Core principle

**Never confuse compression with equivalence.**

`smaller description ≠ same object`

`same measurement ≠ same structure`

`same structure summary ≠ same behavior`

`quotient ≠ destruction`

## Status

`DEFINED / CORE METHODOLOGICAL RULE`
