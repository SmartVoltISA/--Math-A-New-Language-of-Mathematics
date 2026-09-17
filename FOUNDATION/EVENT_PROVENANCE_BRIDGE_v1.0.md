# Ω-Math — Event and Provenance Bridge v1.0

**Status:** EXTENSION / OPEN FOR VALIDATION  
**Core:** Ω-Math v0.9 remains unchanged

## 1. Purpose

This document separates mathematical transition structure from the experimental record of an occurrence.

A transition already has the core form:

`T : S × U → S'`

An **event record** is a meta-level record that a particular transition/observation was executed or observed.

Conceptually:

`EVENT = (pre_state, input, transformation, post_state, observation, provenance)`

EVENT is not required as a new Ω-Math core primitive.

## 2. Order

Events may be ordered by a declared sequence relation. Ω-Math `ORDER` must not be identified with physical time.

`event_i < event_j`

means only that the declared ordering places `i` before `j`.

A physical-time interpretation requires a separate correspondence map.

## 3. Provenance

Provenance attaches origin and reproducibility metadata to observations, transformations, experiments, and claims.

A provenance record may include:

- experiment ID;
- hypothesis ID;
- preregistration/version;
- code/version identifier;
- input/configuration hash;
- execution environment;
- source/authority;
- observation method;
- record timestamp;
- validation status.

A record timestamp is not automatically a physical-time variable.

## 4. Separation rule

The following must remain distinct:

`mathematical state ≠ event record`

`event order ≠ physical time`

`provenance ≠ mathematical evidence by itself`

`observation ≠ identity`

`recorded occurrence ≠ causal explanation`

## 5. Evidence chain

For research claims, preserve:

`claim → observation → event record → provenance → reproducibility result`

A provenance record can establish traceability, but cannot by itself establish truth of the underlying claim.

## 6. Relation to Ω-Stand

The event/provenance bridge supports:

`FACT → CHECK → RESULT → DECISION → FIXATION`

The bridge should make it possible to recover which declared state, transformation, code/configuration, and observation produced a recorded result.

## 7. Current decision

**DECISION: OPEN EXTENSION.**

No new core primitive is promoted. Event and provenance remain meta-language/experimental infrastructure until a stronger mathematical necessity is demonstrated.
