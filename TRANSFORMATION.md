# Ω-Math — Transformation Layer v0.2

## Purpose

The transformation layer is the mathematical engine between static relational structure and dynamics. It specifies how one Ω-configuration is changed into another without assuming ordinary arithmetic, metric geometry, physical time, energy or probability.

## 1. Ω-configuration

A configuration is

`Ω = (E,R,D_R)`

where:

- `E` is the set of entity positions with typed states in `{0,1}`;
- `R` is the set of signed relations with values in `{−1,+1}`;
- `D_R ⊆ I×I` is the relation domain.

A complete model state may additionally retain explicit memory or other variables:

`S = (Ω,M,Z,...)`.

The retained variables must be declared; they are not silently inferred.

## 2. Transformation

A transformation is a declared mapping

`T : S → S'`.

A transformation specification must state:

1. its domain;
2. its admissible outputs;
3. which components may change;
4. which components are preserved;
5. any control/input variables;
6. whether the mapping is deterministic or has multiple allowed outcomes.

A transition used by a dynamical model is therefore a particular transformation together with its input/control conditions.

## 3. Identity transformation

`Id(S)=S`.

The identity transformation changes no declared component.

For compatible transformations:

`T ∘ Id = T`

and

`Id ∘ T = T`.

These are formal laws of the transformation system, subject to the stated domains/codomains.

## 4. Composition

For

`T₁:S₀→S₁`

and

`T₂:S₁→S₂`,

the composite is

`T₂ ∘ T₁ : S₀→S₂`.

Composition is the primary operation for constructing multi-step changes.

Associativity is expected for ordinary function composition:

`T₃ ∘ (T₂ ∘ T₁) = (T₃ ∘ T₂) ∘ T₁`.

If Ω introduces a restricted transformation object for which this fails, the restriction must be explicit rather than hidden.

## 5. Inverse

A transformation `T:S→S'` has an inverse only if there exists `T⁻¹:S'→S` such that

`T⁻¹∘T = Id`

and

`T∘T⁻¹ = Id`.

Non-invertibility is allowed and must not be interpreted automatically as physical irreversibility.

A many-to-one observation or quotient transformation is generally not invertible because distinctions have been discarded.

## 6. Transformation classes

Ω distinguishes at least:

- `T_E` — entity-state transformation;
- `T_R` — relation transformation;
- `T_S` — structural transformation affecting organization;
- `T_O` — observation/transformation of description;
- `T_Q` — quotient/coarse-graining transformation;
- `T_D` — dynamical transition.

The same physical or computational process may induce several of these descriptions; they must not be conflated.

## 7. Change

Change is the declared comparison

`Δ_Ω(S,S') = Compare(S,S')`.

It is not defined as ordinary subtraction.

A comparison must specify the level at which change is measured: entity states, relations, topology, path structure, observation, or behavior.

## 8. Invariants

For a transformation family `𝒯`, a property `I` is invariant when

`I(T(S)) = I(S)`

for every admissible `T ∈ 𝒯` for which both sides are defined.

No quantity is called an invariant without naming the transformation family.

## 9. Symmetry

A symmetry of `S` under equivalence `≈` is a transformation preserving the selected structure up to that equivalence:

`Sym_≈(S) = {T | T(S) ≈ S}`.

Label permutations are the first required symmetry/control family. A label permutation must not change any genuinely structural observable.

## 10. Distance as a derived quantity

Distance is not primitive.

Given an admissible transformation set `𝒯`, one candidate structural distance is the minimum transformation cost:

`d_𝒯(S,S') = inf cost(τ)`

over admissible transformation sequences `τ` taking `S` to `S'`.

This definition is conditional: it becomes meaningful only after a transformation family and cost are independently specified.

It must be tested for:

- non-negativity;
- identity of indiscernibles or the chosen weaker condition;
- symmetry, if intended;
- triangle inequality.

Failure of any property does not invalidate the transformation system; it only prevents calling the derived quantity a metric under the standard meaning.

## 11. Information loss

For a transformation `T`, define the erased distinction set relative to an observation/equivalence relation:

`Loss_T = {(x,y) | x ≠ y, T(x)=T(y)}`.

This is a structural description of collapse, not automatically physical information loss.

A scalar information-loss measure is not yet primitive and must be derived only after a counting or weighting convention is declared.

## 12. Refinement and collapse

A transformation may refine a description by preserving previously hidden distinctions, or collapse a description by identifying them.

Therefore:

`observation change ≠ system change`

and

`quotient collapse ≠ destruction of the underlying system`.

## 13. Required tests

The transformation layer must be tested with:

1. identity;
2. composition;
3. inverse where applicable;
4. associativity;
5. label invariance;
6. preservation of declared invariants;
7. collapse and refinement;
8. path/topology transformations;
9. behavior-preserving transformations;
10. counterexamples to unjustified metric assumptions.

## 14. Status

`DEFINED / CORE LAYER`

The operators above are definitions or formal consequences of ordinary function composition where explicitly stated. No physical interpretation is claimed.

## 15. Open questions

- Which transformation families are fundamental or useful for Ω-Math?
- Which invariants are derivable from the primitive relational layer?
- When does a transformation preserve behavior?
- Which transformation costs produce useful derived geometry?
- Can an internal temporal ordering be reconstructed from transformation sequences without importing physical time?
