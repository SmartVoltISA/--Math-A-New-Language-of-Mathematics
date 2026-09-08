# LIGHT → Ω-Math Structural Bridge v0.1

## Status

`RESEARCH / CANDIDATE DERIVATION`

This document records a structural comparison between the LIGHT repository and the closed Ω-Math v0.9 core. It does **not** add new primitives to Ω-Math. It tests whether structures appearing in electromagnetic field theory can be represented by existing Ω layers before any extension is proposed.

## 1. Source structure from LIGHT

LIGHT gives the following physical/structural chain:

`local state → relation / comparison → constraint → connection → curvature / field strength → dynamics → propagation → boundary interaction → state transition → observable`

and, in the quantum-field layer:

`field configuration → mode decomposition → quantization → excitation → occupation / correlation → measurement statistics`.

The physical repository explicitly warns that these correspondences are architectural candidates, not physical identities.

## 2. First mapping into Ω

| LIGHT structure | Ω candidate | Status |
|---|---|---|
| local state | state / retained configuration | direct representational fit |
| local comparison | relation-derived comparison | candidate derivation |
| constraint | admissible-transition predicate | candidate extension at semantic level |
| connection | context-dependent comparison transport | OPEN |
| curvature / field strength | path/loop inconsistency or transformation invariant | OPEN; not identified with Ω relation |
| dynamics | transformation / transition rule | direct fit |
| propagation | path + ordered transitions + causal admissibility | partial fit |
| boundary | distinction between admissible/inadmissible transitions or domains | partial fit |
| interaction | state transformation conditioned on relation | direct fit |
| observable | observation map | direct fit |
| excitation | state/configuration transition class | partial fit |
| correlation | retained relation structure | partial fit |

## 3. Important negative result

`connection ≠ relation` is retained.

A gauge connection such as `A_mu` is not merely an edge between two objects. It specifies how local states are compared across a domain and transforms under a gauge redundancy. Therefore introducing `CONNECTION` as a new primitive solely because LIGHT contains `A_mu` would be an unjustified import of physical ontology.

Likewise:

`curvature ≠ sign`
`field strength ≠ relation state`
`photon ≠ edge`
`energy ≠ transformation cost`.

## 4. Constraint candidate

The strongest architectural candidate is not a new physical object but a semantic distinction:

`relation exists` ≠ `relation is admissible under C`.

Define, provisionally,

`Adm_C(r) ∈ {false,true}`

for a declared configuration `C` and relation/transition candidate `r`.

This is a predicate over existing objects, not a new primitive value. A transformation rule may then be restricted by:

`T_C(s) ⊆ {s' : all required transition relations satisfy Adm_C}`.

For deterministic dynamics this becomes an admissibility precondition. For nondeterministic dynamics it restricts the successor set before task-specific equivalence is evaluated.

This is compatible with the existing separation between state, relation, transformation, and nondeterministic successor semantics, but it must be tested before entering the canonical core.

## 5. Locality candidate

LIGHT repeatedly uses neighboring spacetime values and local derivatives. Ω currently has relations between entities but does not make locality primitive.

A safe candidate is therefore a **declared locality structure**, not a new primitive relation type:

`Loc_C(x,y)`

meaning that the declared model permits local comparison/evolution between `x` and `y` under configuration `C`.

No universal physical meaning is assigned to `Loc_C`.

The executed finite test `EXPERIMENT_LIGHT_BRIDGE_003.md` verifies that ordinary graph connectivity alone does not determine finite-horizon propagation neighborhoods. Thus locality must be declared when transition semantics depend on it.

## 6. Connection / curvature test

LIGHT gives:

`A_mu → F_muν`

with `F_muν` as an antisymmetric derivative combination.

The Ω question is not whether we can rename these as relation and difference. The question is whether an abstract construction can be built from:

`state + local comparison + ordered path/loop + transformation`

that produces a path-dependent residual/invariant analogous in role to curvature.

The executed algebraic boundary test `EXPERIMENT_LIGHT_BRIDGE_004.md` shows that the existing scalar sign product cannot distinguish different ordered loop organizations with the same sign multiset and product.

This does **not** mean that Ω loses the loop information: the ordered path itself is retained. It means that no universal curvature-like reduction has yet been derived from the current scalar relation algebra.

If this requires importing vector spaces, differential forms, or gauge groups as unexplained primitives, the universal Ω claim is weakened rather than strengthened.

## 7. Propagation and causality

LIGHT distinguishes object speed, phase/group structure, signal propagation, and the causal structure represented by the light cone.

Ω should therefore not define `c` as a primitive scalar or equate `path length` with physical time.

A safer semantic layer is:

`admissible transition → ordered propagation → causal boundary → observation`.

The causal boundary is a domain constraint on which transitions are admissible, not a new relation sign.

## 8. Boundary

The LIGHT boundary examples suggest a reusable abstract pattern:

`boundary → admissibility change → interaction → state transition → observable`.

This can be represented with existing configuration/transition machinery plus an explicit boundary predicate. It does not yet justify a new primitive `BOUNDARY` type.

## 9. Energy and flow

LIGHT's electromagnetic energy accounting contains both stored energy and boundary flux. Ω already treats transformation cost as distinct from physical energy.

The candidate abstraction is therefore:

`state/configuration → conserved quantity candidate → transfer/flow across boundary → balance law`.

No identification of physical energy with Ω cost is permitted.

## 10. Photon and internal state

A photon is a quantized excitation of the electromagnetic field. Its polarization provides physical internal degrees of freedom.

This supports a methodological point for Ω:

`entity state ∈ {0,1}`

does not imply that every physical state must be binary. Higher-order state/configuration structure can encode internal degrees of freedom while preserving the primitive type separation.

Therefore no photon primitive is proposed.

## 11. Candidate Ω chain after LIGHT

The strongest currently defensible abstract chain is:

`state`
`→ relation / comparison`
`→ declared locality`
`→ admissibility constraint`
`→ ordered path / transformation`
`→ loop/path residual candidate`
`→ dynamics`
`→ propagation`
`→ boundary interaction`
`→ observation`

with:

`connection` and `curvature` remaining derived/typed research candidates rather than primitives.

## 12. Required experiments

### LΩ-01 — Admissibility

Test whether an admissibility predicate over existing Ω objects is sufficient to reproduce a nontrivial constrained propagation model without adding a new primitive type.

### LΩ-02 — Locality

Test whether a declared locality structure can express finite-range propagation and distinguish it from arbitrary graph connectivity.

### LΩ-03 — Loop residual

Test whether ordered local comparisons around a closed path produce a nontrivial residual that is not determined by pointwise scalar summaries.

### LΩ-04 — Boundary transfer

Test whether a boundary plus admissibility rule is sufficient to represent reflection/refraction-like state transitions at the abstract level, without importing Maxwell equations.

### LΩ-05 — Cross-domain invariance

Repeat LΩ-01–04 on at least one non-physical domain (e.g. lattice or network dynamics). Reject any abstraction that only works after inserting LIGHT-specific machinery.

## Decision rule

No new Ω primitive is accepted unless a construction:

1. is formally defined;
2. is not reducible to an existing Ω object only by notation;
3. survives counterexample search;
4. has an explicit sufficient-condition statement;
5. works outside the LIGHT domain or is explicitly declared domain-specific.

## Conclusion

LIGHT currently gives Ω-Math **three strong structural candidates**:

1. **admissibility constraints** over relations/transitions;
2. **declared locality** distinct from mere connectivity;
3. **path/loop residual structure** as a possible route toward connection/curvature.

The finite tests now support the first two as semantic distinctions and establish an algebraic boundary for the third. The v0.9 primitive core remains unchanged.

It does **not** yet justify adding `CONNECTION`, `CURVATURE`, `FIELD`, `PHOTON`, `ENERGY`, or `CAUSALITY` as primitive Ω types.
