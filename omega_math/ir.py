"""Structured intermediate representation for Ω-Math v1.1."""
from dataclasses import dataclass
from typing import Any, Tuple

# CALL is an in-memory bridge for runtime operators whose arguments can be
# executable Python objects (rules, predicates, dynamics). The textual parser
# does not emit CALL until a declarative encoding for those objects exists.
OP_ARITY = {
    "ENTITY": 2,
    "RELATION": 4,
    "PATH": 2,
    "EPSILON": 2,
    "CONCAT": 3,
    "INCIDENT": 2,
    "DIST": 2,
    "SIGN": 1,
    "CYCLE": 1,
    "PATH_EQ": 2,
    "CALL": 2,  # runtime operator name, positional operand tuple
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
                raise ValueError(f"{ins.op} expects {expected} arguments, got {len(ins.args)}")
            if ins.op == "CALL":
                name, operands = ins.args
                if not isinstance(name, str) or not name.strip():
                    raise TypeError("CALL operator name must be a non-empty string")
                if not isinstance(operands, tuple):
                    raise TypeError("CALL operands must be a tuple")

    def normalized(self):
        self.validate()
        return tuple((i.op, i.args) for i in self.instructions)
