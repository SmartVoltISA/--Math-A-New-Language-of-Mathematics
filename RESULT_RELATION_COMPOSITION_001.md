# Ω-Math Result — RELATION-COMPOSITION-001

## Scope

This result closes the current minimal relation-composition test suite.

## 1. Four length-2 signed cases

For ordered sign pairs:

`(+,+) -> +`

`(+,-) -> -`

`(-,+) -> -`

`(-,-) -> +`

These are exactly the four cases of the sign-product summary.

## 2. Algebraic properties of the summary

The binary operation

`a ⊗ b = sign-product(a,b)`

on `{−1,+1}` is closed, commutative and associative, with `+1` as identity and each element self-inverse.

These are properties of the **summary operation**, not proof that sequential Ω-relations themselves obey this law as their complete semantics.

## 3. Information-loss counterexample

Two different paths can have the same endpoints and the same sign-product while differing in intermediate organization. PATH-DYNAMICS-001 gives an explicit deterministic transition rule under which the difference changes future behavior.

Therefore scalar reduction is not information-preserving in general.

## 4. Parallel conflict

Two distinct parallel paths may connect the same endpoints while carrying opposite or otherwise different relational histories. Mapping their coexistence to one primitive sign requires an additional rule that either discards, chooses, or encodes multiplicity/conflict elsewhere.

No such universal reduction is currently defined.

## 5. Direction

Because sign-product is commutative, reversal of a signed path preserves the scalar product. Therefore the scalar summary cannot by itself encode ordered directional organization.

## Final status

- `PATH CONCATENATION`: `DEFINED`.
- `SIGN-PRODUCT SUMMARY`: `DERIVED` as a valid closed algebra on relation signs.
- `SIGN-PRODUCT AS UNIVERSAL RELATION COMPOSITION`: `REJECTED` as an information-preserving universal law.
- `PRIMITIVE RELATION REDUCTION`: `OPEN`.
- `PATH SEMANTICS`: retained as the primary object whenever order/intermediate structure matters.
