# REL-EXP-001 ↔ Ω-Math v1.0 — First Bridge Record

**Status:** BRIDGED SNAPSHOT / PARTIAL

## Source

- Experiment: `REL-EXP-001-TIME-VARYING-RELATION`
- Repository: `SmartVoltISA/RELATION-LAB`
- Source revision: `5c1b6522d90763e89e61a9c7ae2ceb57c9e00265`
- Ω-Math revision: `9c4fc0a301f0721df9a80436cbbda72069c404e7`

## Scope

REL-EXP-001 is a time-varying stochastic experiment. Ω-Math v1.0 does **not** contain physical time, probability, or continuous-valued relation magnitudes as primitives. Therefore this bridge deliberately encodes only a qualitative directed snapshot: the existence and sign of a directed relation.

This is a bridge-conformance experiment, not a claim that Ω-Math reproduces the full REL-EXP-001 estimator.

## Declared Ω-Math model

```text
entity A 0
entity B 1
relation A B -1 rAB
path P = A->B
sign P
```

The execution result is `-1`.

## Research record

```json
{
  "experiment_id": "REL-EXP-001",
  "source_revision": "5c1b6522d90763e89e61a9c7ae2ceb57c9e00265",
  "omega_math_revision": "9c4fc0a301f0721df9a80436cbbda72069c404e7",
  "model": "qualitative directed snapshot of A -> B",
  "observation": "SIGN(A -> B)",
  "observed": -1,
  "status": "SUPPORT",
  "interpretation_scope": "snapshot only"
}
```

## Comparison

The source experiment reports recovery of relation presence and sign, including a negative coupling in its final window (`K_AB = -0.700`, estimated `-0.631`). The Ω-Math snapshot records only the qualitative negative relation state `-1`.

Therefore:

- **compatible:** directed relation and sign are representable;
- **not reproduced:** magnitude, stochastic dynamics, time windows, estimator, noise control;
- **not imported:** physical time, probability, energy, or causal interpretation.

## Result

**PARTIAL — bridge contract passes for the representable qualitative slice.**

No claim is made that the full laboratory result has been reproduced.

## Next step

Build the next adapter around a RELATION-LAB experiment whose complete declared observable can be represented without introducing new Ω-Math primitives. The decisive target remains directed geometry without reciprocity.
