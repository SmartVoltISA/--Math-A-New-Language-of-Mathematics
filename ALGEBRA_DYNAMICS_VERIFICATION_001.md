# Ω-Experiment ALGEBRA-DYNAMICS-VERIFICATION-001

## Status

`EXECUTED / SUPPORTED UNDER DECLARED FINITE DETERMINISTIC MODEL`

## 1. Scope

This experiment connects the existing algebraic decision with the finite-horizon behavioral layer.

The tested Ω rule is:

`PATH` retains ordered relations;

`SIGN` may produce a sign-product summary;

`REDUCTION` is admissible only when the declared task is preserved.

## 2. Algebraic result retained

For relation signs in `{−1,+1}`, multiplication is closed and associative. However, the product does not retain intermediate entities, path multiplicity, topology, or other organization.

Therefore:

`sign product = derived summary`

and not:

`sign product = universal primitive composition`.

This agrees with `RELATION_COMPOSITION.md` and the existing path counterexamples.

## 3. Dynamic sufficiency test

A candidate algebraic reduction `Q` was evaluated by the Ω sufficiency criterion:

`Q(x)=Q(y) ⇒ B_h(x,u)=B_h(y,u)`.

The existing `PATH-PROFILE-004` construction supplies a counterexample for a restricted structural reduction: equal source-distance profiles can yield different future trajectories under one fixed deterministic dynamics.

Thus a structural scalar/profile cannot be promoted to a universal dynamic state merely because it is compact or geometrically meaningful.

## 4. Verified behavioral construction

The finite-horizon recursive quotient

`Q_0(s)=O(s)`

`Q_{h+1}(s)=(O(s), {(u,Q_h(T(s,u))):u∈U})`

was checked against direct exhaustive trajectory comparison on small finite deterministic transition systems.

The two equivalence constructions agree on the tested domain.

The horizon relation was also checked:

`≈_{h+1} ⊆ ≈_h`.

No tested model violated this nesting.

## 5. Consequence for the language

The algebraic layer and dynamic layer now have a common admissibility criterion:

> A proposed reduction may replace a richer Ω object only after proving that the replacement preserves the declared task.

This gives a single rule connecting:

`path → summary → reduction → behavior → quotient`.

## 6. Important boundary

This does **not** establish a new universal algebra of relations.

It establishes a verified decision procedure for the tested finite deterministic class:

1. propose reduction;
2. declare task and horizon;
3. compare behavior;
4. reject reduction if a counterexample exists;
5. retain the coarsest behavior-preserving quotient when required.

## 7. Decision

`PATH CONCATENATION`: retained as the information-preserving sequential representation.

`SIGN-PRODUCT`: retained as a derived summary.

`UNIVERSAL PRIMITIVE RELATION COMPOSITION`: remains OPEN.

`FINITE-HORIZON BEHAVIORAL QUOTIENT`: SUPPORTED under the declared finite deterministic model.

`PHYSICAL INTERPRETATION`: not inferred.

## 8. Next boundary test

The next decisive extension is to introduce nondeterministic transitions while keeping the Ω typed foundation fixed. The experiment must determine which notion of preservation is required before any probabilistic or physical interpretation is introduced.
