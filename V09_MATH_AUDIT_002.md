# Ω-Math v0.9 — Mathematical Audit 002

## Scope

Second mathematical/documentation consistency pass after v0.9 closure. The goal is to find contradictions between the current canonical layer, legacy documents and the mathematical claims themselves.

## 1. Path identity consistency

The v0.9 canonical layer defines an empty path `ε_e` as the identity for compatible path concatenation.

A legacy `PATH_ALGEBRA.md` still says that a path has at least one relation unless a zero-length convention is introduced. That sentence is now stale relative to v0.9.

Decision:

- empty paths are admitted in v0.9;
- `ε_e` is path-level identity only;
- no primitive relation identity is introduced;
- legacy wording must be treated as superseded.

**Status: DOCUMENTATION CONFLICT FOUND / CANONICAL MATHEMATICS CONSISTENT**

## 2. Behavioral equivalence

Finite-horizon equivalence remains an equivalence relation for a fixed deterministic model, observation criterion, admissible input/intervention class and horizon. Horizon nesting follows directly from the definition.

Infinite-horizon equivalence is the intersection of all finite-horizon relations and therefore remains an equivalence relation.

No counterexample found to these claims under the declared semantics.

**Status: PASS**

## 3. Reduction sufficiency

The condition

`Q(x)=Q(y) ⇒ F(x)=F(y)`

is exactly the fiber-constancy condition required for a task `F` to factor through `Q` on the image of `Q`.

Therefore the Ω reduction rule is mathematically sound as a task-relative criterion.

It does not imply that one universal reduction exists for all tasks.

**Status: PASS**

## 4. Quotient geometry

The unrestricted representative-infimum construction

`d_Q([x],[y]) = inf{d(x',y'): x'~x, y'~y}`

is not automatically a pseudometric. The finite counterexample recorded in `V09_MATH_AUDIT_001.md` violates triangle inequality.

The current guarded formulation in `QUOTIENT_GEOMETRY_CONDITIONS.md` is therefore retained.

**Status: PASS WITH COUNTEREXAMPLE**

## 5. Transformation-derived distance

For

`d_c(x,y)=inf{c(T):T∈T(x,y)}`

the triangle inequality follows when admissible transformations compose and their costs are subadditive. Symmetry requires reversible equal-cost transformations. Identity of indiscernibles requires exclusion of zero-cost distinct states or an explicit accepted equivalence.

No universal metric is implied without those conditions.

**Status: PASS / CONDITIONS EXPLICIT**

## 6. Sign product

For non-empty paths over `{−1,+1}`, the product summary is closed and associative/commutative as ordinary multiplication. This is only a derived summary and does not preserve path order, intermediate structure, multiplicity or conflict information.

No contradiction found.

**Status: PASS / SCOPE-BOUNDED**

## 7. Path-profile counterexample

`EXPERIMENT_PATH_PROFILE_004.md` gives a finite deterministic counterexample in which the same source-distance profile produces different behavior under a fixed triangle-sensitive transition rule.

This supports only the declared statement:

`restricted source-distance profile → not behavior-sufficient`.

It does not show that all geometric/path descriptors are insufficient.

**Status: SUPPORTED FINITE COUNTEREXAMPLE**

## 8. New documentation finding

`EQUIVALENCE.md` remains explicitly labeled v0.1 and contains historical collapse/black-hole hypothesis material. Its conceptual distinctions are still useful, but it must not be read as the current v0.9 canonical equivalence specification.

`PATH_ALGEBRA.md` remains labeled v0.2 and contains the stale zero-length-path sentence described above.

These are synchronization problems, not failures of the v0.9 formal core.

## 9. Audit conclusion

No new mathematical contradiction was found in the current v0.9 core.

Two legacy documents still require canonical synchronization or explicit supersession marking:

- `EQUIVALENCE.md`
- `PATH_ALGEBRA.md`

The important mathematical boundaries remain intact:

`compression ≠ equivalence`

`path ≠ scalar summary`

`quotient distance ≠ automatically metric`

`transformation cost ≠ physical energy`

`transition order ≠ physical time`

`cycle ≠ causality`

`stable pattern ≠ automatically emergence`

`model ≠ reality`

**AUDIT-002: PASS WITH DOCUMENTATION ACTIONS**
