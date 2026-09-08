"""Structured intermediate representation for Ω-Math v1.0.

The IR separates parsing from execution. It carries only declared mathematical
operations; scientific interpretation belongs to the research layer.
"""
from dataclasses import dataclass
from typing import Any, Tuple


@dataclass(frozen=True)
class IRInstruction:
    op: str
    args: Tuple[Any, ...] = ()


@dataclass(frozen=True)
class IRProgram:
    instructions: Tuple[IRInstruction, ...]

    def validate(self) -> None:
        allowed = {
            "ENTITY", "RELATION", "PATH", "EPSILON", "CONCAT", "INCIDENT",
            "DIST", "SIGN", "CYCLE", "PATH_EQ",
        }
        for ins in self.instructions:
            if ins.op not in allowed:
                raise ValueError(f"unsupported IR operation: {ins.op}")

    def normalized(self):
        self.validate()
        return tuple((i.op, i.args) for i in self.instructions)
