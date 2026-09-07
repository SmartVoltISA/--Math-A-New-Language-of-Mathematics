# Ω-Math — Relation Composition v0.2

## 1. Question

Can two sequential primitive relations be reduced to one primitive relation without losing distinctions that matter to Ω structure or behavior?

Given

`a —r₁→ b —r₂→ c`,

we seek a candidate operation

`r₂ ⊙ r₁`.

The operation is not assumed to be ordinary arithmetic.

## 2. Complete primitive cases

Because each relation sign belongs to `{−1,+1}`, there are exactly four ordered sign pairs:

| `r₂` | `r₁` | candidate input |
|---|---|---|
| `+1` | `+1` | `(+1,+1)` |
| `+1` | `−1` | `(+1,−1)` |
| `−1` | `+1` | `(−1,+1)` |
| `−1` | `−1` | `(−1,−1)` |

A complete composition law must assign a result or explicitly reject reduction for every case in its declared domain.

## 3. Candidate A — sign multiplication

`r₂ ⊙ₘ r₁ = r₂ r₁`

This gives:

| `r₂` | `r₁` | result |
|---|---|---|
| `+1` | `+1` | `+1` |
| `+1` | `−1` | `−1` |
| `−1` | `+1` | `−1` |
| `−1` | `−1` | `+1` |

This candidate is closed and associative because it is multiplication on the two-element sign group.

However, algebraic closure does not prove semantic adequacy.

## 4. Counterexample to sufficiency

Consider two length-2 paths with identical endpoints:

`P₁: A —(+1)→ B —(+1)→ C`

`P₂: A —(+1)→ D —(+1)→ C`.

Sign multiplication assigns `+1` to both.

If the two paths are structurally distinct and both are retained in the Ω-system, the reduction loses path multiplicity and intermediate-entity identity.

Therefore sign multiplication is a valid **path-sign summary**, but it is not demonstrated to be a sufficient universal relation-composition operator.

## 5. Parallel-path conflict

Consider:

`P₁: A —(+1)→ B —(+1)→ C`

`P₂: A —(+1)→ D —(−1)→ C`.

Sign multiplication gives:

`P₁ → +1`

`P₂ → −1`.

There is no primitive third sign representing the conflict.

Therefore a reduction that combines both paths into one primitive relation must either:

1. discard one path;
2. choose a priority rule;
3. retain a richer object than a primitive relation;
4. declare the result undefined/conflicting.

Ω-Math currently selects none of these as universal law.

## 6. Candidate B — context-dependent reduction

A reduction may depend on intermediate structure, path multiplicity, states, or direction.

This can preserve more information but ceases to be a function of the two signs alone.

It is therefore a candidate **higher-order composition rule**, not a primitive binary sign operation unless its required context is formally incorporated into the input type.

## 7. Candidate C — structural composition

Instead of forcing

`Path → Relation`,

retain

`Relation ∘ Relation → Path`.

This is already defined by `PATH_ALGEBRA.md` as path concatenation.

This candidate is information-preserving with respect to the ordered path object and does not require an artificial third relation value.

## 8. Associativity

Path concatenation is associative wherever defined.

Sign multiplication is also associative.

But associativity of a reduction does not establish that the reduction preserves the semantics of paths.

The critical test is therefore:

`semantic preservation + associativity`,

not associativity alone.

## 9. Current decision

`PATH COMPOSITION` — **DEFINED**.

`SIGN MULTIPLICATION` — **VALID DERIVED SUMMARY, NOT UNIVERSAL RELATION LAW**.

`PRIMITIVE RELATION REDUCTION` — **OPEN**.

`CONFLICT-COLLAPSING TO A THIRD SIGN` — **REJECTED by the current typed primitive layer**.

## 10. Required next tests

1. Exhaustive length-3 comparison of sign-reduction candidates.
2. Search for smallest associativity/semantic-preservation counterexamples.
3. Test relation reduction under reversed paths.
4. Test whether state-dependent transition behavior can distinguish paths with the same sign product.
5. Compare primitive reduction against retaining the full path object.

## 11. Conclusion

The first algebraic milestone is complete: all four primitive sign-pair cases are explicit, a closed candidate has been tested, and a concrete information-loss counterexample prevents promoting sign multiplication to the universal Ω relation-composition law.

The language therefore advances without inventing a forced answer:

`relation + relation → path` is defined;

`path → primitive relation` remains open.
