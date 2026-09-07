# Ω-Math v0.1 — Algebra Research

## Purpose

The central algebraic question is not how to add `−1` and `+1`. Ordinary arithmetic already knows that.

The question is:

> What operations are legal on typed entities and typed relations, and what algebraic structures arise from those operations?

## 1. Primitive types

`Entity = {0,1}`

`Relation = {−1,+1}`

These are disjoint typed domains even though their labels are numerical.

## 2. Entity operations

At v0.1 we define only equality and distinction for entity values.

Equality:

`Eq(a,b) = true` when `a=b`.

Distinction:

`D(a,b) = 0` when `a=b`.
`D(a,b) = 1` when `a≠b`.

We deliberately do not define entity addition as primitive.

## 3. Relation composition

Given:

`A —r₁→ B —r₂→ C`

we want to study whether a composed relation

`r₁ ⊙ r₂`

can be defined.

The four primitive cases are:

`(+1) ⊙ (+1)`
`(+1) ⊙ (−1)`
`(−1) ⊙ (+1)`
`(−1) ⊙ (−1)`

Their values must not be assigned by ordinary arithmetic before the semantics of composition are specified.

## 4. Candidate composition laws

We will test at least four candidate families.

### A. Arithmetic projection

Map relation states directly onto integers and use multiplication or addition.

This is a baseline, not the Ω definition.

### B. Sign composition

Use multiplication:

`(+1)·(+1)=+1`
`(+1)·(−1)=−1`
`(−1)·(+1)=−1`
`(−1)·(−1)=+1`

This models parity of relation polarity.

### C. Context-dependent composition

The result may depend on the intermediate entity state:

`r₁ ⊙_b r₂`

This is important if the same relation pair behaves differently in different states.

### D. Structural composition

The composition result may not be a single sign at all. It may be a relation plus information about path multiplicity, conflict or uncertainty.

This is likely the most important candidate to test rather than assume away.

## 5. Why a sign may be insufficient

Suppose:

`A → B → C`

and there are two paths:

`A —(+1)→ B —(+1)→ C`

`A —(−1)→ D —(+1)→ C`

A single relation value from `A` to `C` cannot preserve the fact that the paths disagree.

Therefore higher-order structure may require a value richer than `{−1,+1}`.

The primitive relation can remain binary while the composed object becomes structured.

This is a key research direction.

## 6. Identity

An identity relation would need an element `I` such that:

`I ⊙ r = r`

and

`r ⊙ I = r`.

There is no third primitive relation value available in v0.1.

Therefore we must determine whether identity can be represented structurally rather than by adding a new primitive.

## 7. Inverse

For a relation `r`, an inverse operation would satisfy some criterion involving:

`r⁻¹`

and the reverse path.

But because `+1` and `−1` are semantic states rather than assumed group elements, we do not yet identify:

`(+1)⁻¹ = +1`

or

`(+1)⁻¹ = −1`.

Both are hypotheses requiring a defined semantics.

## 8. Associativity

A candidate composition `⊙` must be tested for:

`(a ⊙ b) ⊙ c = a ⊙ (b ⊙ c)`.

If associativity fails, that failure is important: it tells us that relational composition depends on grouping or intermediate structure.

If associativity holds under a specified model, we gain an algebraic structure that can be studied formally.

## 9. Commutativity

Test:

`a ⊙ b = b ⊙ a`.

There is no reason to assume this.

Directed relations naturally suggest non-commutativity.

## 10. Closure

For a candidate binary composition on relation values, closure would require:

`a,b ∈ {−1,+1}  ⇒  a ⊙ b ∈ {−1,+1}`.

If empirical or structural composition produces a richer object, closure in the primitive relation set fails. That may be a feature rather than an error.

## 11. Important separation

There are at least three different operations that can look like “combining relations”:

1. **Path composition** — sequential relation through an intermediate entity.
2. **Parallel aggregation** — several relations between the same endpoints.
3. **State transition** — a relation changes because the system changes.

They must not be collapsed into one operator.

## 12. Parallel conflict

If two relations connect the same endpoints:

`A —(+1)→ B`

and

`A —(−1)→ B`

we do not force them to cancel to `0`.

The correct representation may be a multirelation, a conflict state, a weighted structure or an unresolved pair.

The important point is that `0` is not a primitive relation value in Ω-Math v0.1.

## 13. Research tests

The algebra branch should enumerate all compositions of length 2, 3 and 4 and test:

- closure;
- associativity;
- commutativity;
- identity;
- inverse;
- path equivalence;
- conflict preservation;
- sensitivity to entity state;
- sensitivity to direction.

The output should distinguish mathematically derived properties from properties observed only in a chosen model.

## 14. First expected result

The first deliverable is not a grand theorem.

It is a complete table of legal typed operations and their status:

`DEFINED`
`DERIVED`
`HYPOTHESIZED`
`UNDEFINED`
`REJECTED`

That table becomes the algebraic backbone of Ω-Math.
