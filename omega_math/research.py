"""Deterministic machine-readable research records for Ω-Math v1.0."""
from dataclasses import dataclass
import json
from typing import Any


SCHEMA_VERSION = "omega-math.research-record.v1"


@dataclass(frozen=True)
class ResearchRecord:
    study_id: str
    hypothesis_id: str
    null_id: str
    model: Any
    intervention: Any
    observation: Any
    metric: Any
    criterion: Any
    horizon: Any
    seed: int | None
    source_version: str
    status: str
    result: Any

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "study_id": self.study_id,
            "hypothesis_id": self.hypothesis_id,
            "null_id": self.null_id,
            "model": self.model,
            "intervention": self.intervention,
            "observation": self.observation,
            "metric": self.metric,
            "criterion": self.criterion,
            "horizon": self.horizon,
            "seed": self.seed,
            "source_version": self.source_version,
            "status": self.status,
            "result": self.result,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    def validate(self) -> None:
        required = ("study_id", "hypothesis_id", "null_id", "source_version", "status")
        for name in required:
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if self.seed is not None and not isinstance(self.seed, int):
            raise TypeError("seed must be an integer or None")
        if self.status not in {"SUPPORT", "COUNTEREXAMPLE", "INCONCLUSIVE", "INVALID"}:
            raise ValueError("unsupported research status")
        if self.model is None or self.observation is None or self.metric is None or self.criterion is None:
            raise ValueError("model, observation, metric and criterion must be declared")


def counterexample(record: ResearchRecord) -> ResearchRecord:
    """Return a validated record classified as a machine-detected counterexample."""
    record.validate()
    if record.status != "COUNTEREXAMPLE":
        raise ValueError("counterexample() requires COUNTEREXAMPLE status")
    return record
