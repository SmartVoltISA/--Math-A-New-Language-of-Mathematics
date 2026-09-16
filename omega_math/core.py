"""Typed Ω-Math core objects. No implicit arithmetic coercions are provided."""
from dataclasses import dataclass
from numbers import Real
from typing import Any, Callable, Tuple
import math

ENTITY_STATES = frozenset({0, 1})
RELATION_STATES = frozenset({-1, 1})

@dataclass(frozen=True)
class Entity:
    id: Any
    state: int
    def __post_init__(self):
        if isinstance(self.state, bool) or not isinstance(self.state, int) or self.state not in ENTITY_STATES:
            raise TypeError("EntityState must be an int exactly equal to 0 or 1")

@dataclass(frozen=True)
class Relation:
    src: Any
    dst: Any
    sign: int
    key: Any = None
    def __post_init__(self):
        if isinstance(self.sign, bool) or not isinstance(self.sign, int) or self.sign not in RELATION_STATES:
            raise TypeError("RelationState must be an int exactly equal to -1 or +1")

@dataclass(frozen=True)
class Configuration:
    entities: Tuple[Entity, ...]
    domain: frozenset[tuple]
    relations: Tuple[Relation, ...]
    def __post_init__(self):
        ids = [e.id for e in self.entities]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate entity id")
        keys = [r.key for r in self.relations if r.key is not None]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate relation key")
        idset = set(ids)
        for r in self.relations:
            if (r.src, r.dst) not in self.domain:
                raise ValueError("relation endpoint pair is outside D_R")
            if r.src not in idset or r.dst not in idset:
                raise ValueError("relation endpoint entity is absent")

@dataclass(frozen=True)
class State:
    config: Configuration
    memory: Any = None
    control: Any = None

@dataclass(frozen=True)
class Path:
    relations: Tuple[Relation, ...] = ()
    start: Any = None
    end: Any = None
    def __post_init__(self):
        if self.relations:
            if self.start is not None and self.relations[0].src != self.start:
                raise ValueError("path start mismatch")
            if self.end is not None and self.relations[-1].dst != self.end:
                raise ValueError("path end mismatch")
            for a, b in zip(self.relations, self.relations[1:]):
                if a.dst != b.src:
                    raise ValueError("path relations are incompatible")
    @property
    def length(self): return len(self.relations)
    @property
    def source(self): return self.start if self.start is not None else (self.relations[0].src if self.relations else None)
    @property
    def target(self): return self.end if self.end is not None else (self.relations[-1].dst if self.relations else None)

@dataclass(frozen=True)
class Transformation:
    name: str
    fn: Callable[[State, Any], Any]
    cost: float = 0.0
    def __post_init__(self):
        # COST is contractually [0,∞]. Reject signed/NaN costs at construction
        # so shortest-path and metric-adjacent operators cannot silently ingest
        # an invalid edge weight.
        if isinstance(self.cost, bool) or not isinstance(self.cost, Real):
            raise TypeError("Transformation.cost must be a real number in [0,∞]")
        if math.isnan(float(self.cost)) or self.cost < 0:
            raise ValueError("Transformation.cost must be in [0,∞]")
    def __call__(self, state, inp=None): return self.fn(state, inp)

@dataclass(frozen=True)
class Observation:
    value: Any


def dist(a: Entity, b: Entity):
    return 0 if a == b else 1

def incident(e: Entity, r: Relation):
    return e.id == r.src or e.id == r.dst

def concat(p: Path, q: Path):
    if p.length == 0: return q
    if q.length == 0: return p
    if p.target != q.source: raise ValueError("incompatible paths")
    return Path(p.relations + q.relations, p.source, q.target)

def sign_summary(p: Path):
    if not p.relations: raise ValueError("SIGN summary is defined for non-empty paths")
    out = 1
    for r in p.relations: out *= r.sign
    return out

def reverse_path(p: Path):
    """Reject reversal unless explicit inverse relations exist.

    Reversing a path's relation sequence does not create inverse edges. Since
    inverse relations are not primitive in Ω-Math v0.9, silently constructing
    such a path would violate the typed relational semantics.
    """
    if not p.relations:
        return p
    raise ValueError("path reversal requires explicit inverse relations; Ω-Math does not invent edges")

def compare(a: State, b: State):
    return {"equal": a == b, "config_equal": a.config == b.config, "memory_equal": a.memory == b.memory, "control_equal": a.control == b.control}
