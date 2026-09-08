"""Structured intermediate representation for Ω-Math v1.0."""
from dataclasses import dataclass
from typing import Any, Tuple


# Exact arity of the reference IR operations. Arguments are symbolic names
# until the execution layer resolves them against the parsed program state.
OP_ARITY = {
    "ENTITY": 2,       # name, state
    "RELATION": 4,     # src, dst, sign, key
    "PATH": 2,         # name, entity sequence
    "EPSILON": 2,      # name, entity
    "CONCAT": 3,       # name, left, right
    "INCIDENT": 2,     # entity, relation
    "DIST": 2,         # source, target
    "SIGN": 1,         # path
    "CYCLE": 1,        # path
    "PATH_EQ": 2,      # left, right
}


@dataclass(frozen=True)
class IRInstruction:
    op: str
    args: Tuple[Any, ...] = ()


@dataclass(frozen=True)
class IRProgram:
    instructions: Tuple[IRInstruction, ...]

    def validate(self) -> None:
        for index, ins in enumerate(self.instructions):
            if not isinstance(ins, IRInstruction):
                raise TypeError(f"instruction {index} is not IRInstruction")
            if ins.op not in OP_ARITY:
                raise ValueError(f"unsupported IR operation: {ins.op}")
            if not isinstance(ins.args, tuple):
                raise TypeError(f"instruction {index} args must be a tuple")
            expected = OP_ARITY[ins.op]
            if len(ins.args) != expected:
                raise ValueError(
                    f"{ins.op} expects {expected} arguments, got {len(ins.args)}"
                )

    def normalized(self):
        self.validate()
        return tuple((i.op, i.args) for i in self.instructions)
