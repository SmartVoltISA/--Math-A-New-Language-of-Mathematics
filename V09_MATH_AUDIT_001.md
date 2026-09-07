# Ω-Math v0.9 — Mathematical Audit 001

## Scope

This audit checks selected v0.9 claims for logical consistency and searches for a concrete failure of the unrestricted quotient-distance construction.

## 1. Finite-horizon behavioral equivalence

For deterministic transitions and a fixed observation map/input sequence, the relation `≈ₕ` defined by equality of observations for all `0≤k≤h` is an equivalence relation for each finite `h`.

The nesting property

`≈ₕ₊₁ ⊆ ≈ₕ`

follows directly because horizon `h+1` contains all observations required at horizon `h` plus one additional step.

An exhaustive finite check over deterministic transition functions with 2–4 states and horizons through 3 confirmed reflexivity, symmetry, transitivity and horizon nesting for the tested observation maps.

**Status: DERIVED / FINITELY VERIFIED**

## 2. Infinite-horizon equivalence

Define

`≈∞ = ⋂ₕ≈ₕ`.

Because every `≈ₕ` is an equivalence relation, their intersection is also an equivalence relation. No new primitive operator is required.

This is a mathematical consequence of the definition, not an empirical claim.

**Status: DERIVED**

## 3. Quotient-distance warning: unrestricted infimum formula fails

For a metric space `(X,d)` and arbitrary equivalence relation `~`, the candidate

`d_Q([x],[y]) = inf{d(x',y'): x'~x, y'~y}`

is not automatically a pseudometric.

A finite counterexample uses the unweighted graph with edges

`0—1`, `0—3`, `1—2`.

Its shortest-path metric is:

`d(1,2)=1`, `d(1,0)=1`, `d(0,3)=1`, `d(2,3)=3`.

Use equivalence classes

`A={0,1}`, `B={2}`, `C={3}`.

The induced infimum distances are:

`d_Q(B,C)=3`,
`d_Q(B,A)=1`,
`d_Q(A,C)=1`.

Hence

`d_Q(B,C)=3 > 1+1 = d_Q(B,A)+d_Q(A,C)`.

Triangle inequality fails.

Therefore v0.9 correctly treats the formula as a **candidate construction** and requires compatibility conditions before promoting it to a pseudometric/metric.

**Status: COUNTEREXAMPLE CONFIRMED**

## 4. Sign summary

For non-empty paths over relation signs `{−1,+1}`, the product summary is closed and associative/commutative as ordinary multiplication of summary values. This does not establish a universal law for relational composition because the path object contains information that the scalar summary discards.

**Status: DERIVED / SCOPE-BOUNDED**

## 5. Path identity

The empty path `ε_e` is an identity for compatible path concatenation. This supplies path-level identity without introducing a third primitive relation value.

A primitive relation identity remains unnecessary for the minimal core.

**Status: DERIVED**

## 6. Audit conclusion

No contradiction was found in the audited v0.9 claims. One important overclaim was explicitly eliminated earlier: unrestricted quotient-distance infimum is not automatically a pseudometric. The counterexample above justifies the current guarded formulation.

Remaining open areas are not silently promoted: general quotient geometry, richer relation collapse, nondeterministic equivalence semantics, probability, physical time/energy, physical ontology and task-independent emergence.

`AUDIT-001: PASS WITH EXPLICIT LIMITS`
