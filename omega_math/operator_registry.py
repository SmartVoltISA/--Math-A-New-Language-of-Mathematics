"""Canonical Ω-Math operator registry.

The registry is metadata, not a second semantic implementation. Runtime
functions remain authoritative; this file makes the semantic operator,
surface syntax and IR mapping explicit and auditable.
"""
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class OperatorSpec:
    name: str
    signature: str
    status: str
    surface: Optional[str]
    ir_op: str
    runtime: str
    notes: str = ""

# None surface means the current textual language does not yet encode the
# required executable rule/task/input. We do not serialize arbitrary Python.
OPERATOR_REGISTRY: Tuple[OperatorSpec, ...] = (
    OperatorSpec("DIST", "Entity × Entity → Distinction", "DEFINED", "dist", "DIST", "dist"),
    OperatorSpec("INCIDENT", "Entity × Relation → Incidence", "DEFINED", "incident", "INCIDENT", "incident"),
    OperatorSpec("PATH", "Relation* → Path", "DEFINED", "path", "PATH", "path"),
    OperatorSpec("PATH_EQ", "Path × Path → Boolean", "DERIVED / ADMITTED", "path_eq", "PATH_EQ", "path_eq"),
    OperatorSpec("CYCLE", "Path → Cycle ∪ Failure", "DEFINED", "cycle", "CYCLE", "cycle"),
    OperatorSpec("CONCAT", "Path × Path → Path", "DEFINED", "concat", "CONCAT", "concat"),
    OperatorSpec("SIGN", "Path → SignSequence / Summary", "DERIVED", "sign", "SIGN", "sign_summary"),
    OperatorSpec("COMPARE", "State × State → ChangeRecord", "DEFINED", None, "CALL", "compare"),
    OperatorSpec("TRANSFORM", "State × Rule/Input → State or Successors", "DEFINED", None, "CALL", "transform"),
    OperatorSpec("OBSERVE", "State → Observation", "DEFINED", None, "CALL", "observe"),
    OperatorSpec("EQUIV", "Objects × Task → Equivalence", "DEFINED", None, "CALL", "equiv"),
    OperatorSpec("QUOTIENT", "Object × Equivalence → Quotient", "DEFINED", None, "CALL", "quotient"),
    OperatorSpec("INVARIANT", "Property × TransformFamily → PreservationTest", "DEFINED", None, "CALL", "invariant"),
    OperatorSpec("BEHAVIOR", "State × Dynamics × Horizon → Behavior", "DEFINED", None, "CALL", "behavior"),
    OperatorSpec("COST", "Transformation → [0,∞]", "DEFINED FRAMEWORK", None, "CALL", "cost"),
    OperatorSpec("DISTANCE", "State × State → [0,∞]∪{∞}", "DERIVED", None, "CALL", "distance"),
    OperatorSpec("QUOTIENT_DISTANCE", "Quotient × BaseDistance → [0,∞]∪{∞}", "DERIVED", None, "CALL", "quotient_distance"),
    OperatorSpec("SYMMETRY", "State × TransformFamily → Orbit/Action", "DEFINED", None, "CALL", "symmetry"),
    OperatorSpec("RETAIN", "State × RetentionRule → MemoryCandidate", "DEFINED FRAMEWORK", None, "CALL", "retain"),
    OperatorSpec("ORDER", "TransitionSequence → OrderedIndex", "DERIVED", None, "CALL", "order"),
    OperatorSpec("HORIZON", "Dynamics × ℕ₀ → FiniteFutureDomain", "DEFINED", None, "CALL", "horizon"),
    OperatorSpec("BRANCH", "State × Input → 𝒫(State)", "DEFINED", None, "CALL", "branch"),
    OperatorSpec("REACH", "State × Task × Horizon → Boolean/Set", "DEFINED FRAMEWORK", None, "CALL", "reach"),
    OperatorSpec("MODEL", "State → InternalRepresentation", "HYPOTHESIS FRAMEWORK", None, "CALL", "model"),
    OperatorSpec("FEEDBACK", "State/Model × Dynamics → RecurrentDependency", "DEFINED FRAMEWORK", None, "CALL", "feedback"),
    OperatorSpec("COARSE", "Structure × Criterion → MacroObject", "DEFINED FRAMEWORK", None, "CALL", "coarse"),
)

BY_NAME = {spec.name: spec for spec in OPERATOR_REGISTRY}

def get_operator(name: str) -> OperatorSpec:
    try:
        return BY_NAME[name.upper()]
    except KeyError as exc:
        raise KeyError(f"unknown Ω-Math operator: {name}") from exc

def surface_operators() -> Tuple[OperatorSpec, ...]:
    return tuple(spec for spec in OPERATOR_REGISTRY if spec.surface is not None)

def runtime_operators() -> Tuple[OperatorSpec, ...]:
    return OPERATOR_REGISTRY
