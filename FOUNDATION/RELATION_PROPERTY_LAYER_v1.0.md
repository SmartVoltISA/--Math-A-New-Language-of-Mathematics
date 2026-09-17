# Ω-Math — Relation Property Layer v1.0

**Status:** EXTENSION / OPEN FOR VALIDATION  
**Core:** Ω-Math v0.9 remains unchanged  
**Purpose:** typed representation of relation properties without promoting empirical attributes to primitives

## 1. Scope

Ω-Math v0.9 distinguishes relation state from entity state. This extension adds a typed property layer above the core relation representation.

Core relation remains:

`r = (src, dst, sign)`

Extended annotation:

`r⁺ = (src, dst, sign, P_r)`

where `P_r` is a finite set/record of declared property values. `P_r` does **not** change the core relation state unless a task explicitly declares that a property participates in identity or equivalence.

## 2. Typed property specification

A property declaration is represented conceptually as:

`PropertySpec = (name, type, domain, codomain, definition_or_observation, status)`

A property value is a typed application:

`p(r,S) ∈ Codomain`

The state argument is optional only when the property is explicitly static. Otherwise properties are state-dependent by default.

Required distinctions:

- **state** — part of the declared mathematical state;
- **property** — typed attribute attached to an entity/relation/configuration;
- **observable** — map producing a value from a state/configuration;
- **law/constraint** — condition or update relation restricting admissible states/transitions;
- **unit** — representation convention for a quantity, not its ontology.

## 3. Candidate property families

The following are admissible research candidates, not primitives:

- direction;
- orientation;
- length/distance;
- strength;
- stiffness;
- elasticity/recoverability;
- density;
- persistence/lifetime;
- capacity/bandwidth;
- propagation delay;
- anisotropy;
- history dependence;
- creation/modification/destruction cost.

Each candidate must be independently defined and tested. Naming a property does not establish its universality or independence.

## 4. Non-identifications

The language must not silently identify:

`strength ≠ stiffness`

`direction ≠ orientation`

`orientation ≠ anisotropy`

`persistence ≠ physical time`

`cost ≠ physical energy`

`relation property ≠ relation state`

`measurement ≠ identity`

A physical interpretation requires an explicit correspondence map and evidence.

## 5. Missingness and undefined values

Absence of a declared property value is not a new value of the property and must not be confused with relation absence.

A property schema therefore needs an explicit policy for:

- undefined;
- unobserved;
- not applicable;
- observed value;
- inferred value.

These statuses must remain distinguishable where the task depends on them.

## 6. Property compatibility

Two property annotations are compatible when their declared types, domains, and validity conditions permit joint use without contradiction.

A property conflict is a failed consistency condition, not automatically a third property value.

Aggregation/composition of properties is not assumed. It must be defined per property family or by an explicit operator.

## 7. Identity and equivalence

Default rule:

`r⁺₁ ≡ r⁺₂` follows the core identity rules unless the declared task explicitly includes selected properties.

If a task depends on property set `P`, define a task-specific observation/identification map:

`Q_P(r⁺) = selected_property_values`

and only then derive task-relative equivalence.

Thus adding annotations does not automatically change the ontology of the core language.

## 8. Property laws

A property may be constrained by a law of the form:

`L(P, C, S, T) = true`

or updated by:

`P' = U_P(P, C, S, input)`.

This keeps static declaration, observation, constraint, and dynamics separate.

## 9. Physical correspondence gate

For a physical mapping, record explicitly:

`Ω-property → physical observable → measurement protocol → unit → uncertainty → evidence`

A mathematical property becomes a physical correspondence only after this chain is specified and independently checked.

## 10. Consequence for Ω-Math

No new universal primitive is required by this extension. The property layer is a typed semantic/structural extension over relations and configurations.

The principal research question is not "which familiar physical properties should become primitives?" but:

> Which property families are irreducible, reusable across tasks, compositionally stable, and empirically recoverable from the Ω-Math structure?

## 11. Validation requirements

A candidate property passes only if its definition is unambiguous, its domain/codomain are declared, its measurement or derivation is reproducible, and counterexamples do not collapse it into an already-defined property.

Minimum validation loop:

`DEFINE → TYPE → OBSERVE/DERIVE → COUNTEREXAMPLE → REPRODUCE → COMPARE → DECIDE → RECORD`

## 12. Current decision

**DECISION: OPEN EXTENSION.**

The property layer is formally specified as an extension. No candidate property is promoted to Ω-Math v0.9 core by this document.
