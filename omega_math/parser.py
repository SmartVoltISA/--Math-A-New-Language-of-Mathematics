"""Deterministic Ω-Math reference parser with v1 IR lowering."""
import re
from .core import Entity, Relation, Path, concat, incident, dist
from .ir import IRInstruction, IRProgram


class ParseError(ValueError):
    pass


class Program:
    def __init__(self):
        self.entities = {}
        self.relations = {}
        self.paths = {}
        self.results = []
        self.instructions = []

    def _add(self, op, *args):
        self.instructions.append(IRInstruction(op, tuple(args)))

    def to_ir(self):
        ir = IRProgram(tuple(self.instructions))
        ir.validate()
        return ir

    def run(self, text):
        for no, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            try:
                self._line(line)
            except Exception as e:
                raise ParseError(f"line {no}: {e}") from e
        return self.results

    def _line(self, line):
        m = re.fullmatch(r"entity\s+(\S+)\s+([01])", line)
        if m:
            name, state = m.groups()
            if name in self.entities:
                raise ValueError(f"duplicate entity {name}")
            self.entities[name] = Entity(name, int(state))
            self._add('ENTITY', name, int(state))
            return

        m = re.fullmatch(r"relation\s+(\S+)\s+(\S+)\s+([+-]1)(?:\s+(\S+))?", line)
        if m:
            a, b, s, key = m.groups()
            if a not in self.entities or b not in self.entities:
                raise ValueError("relation endpoint entity is absent")
            key = key or f"{a}->{b}#{len(self.relations)}"
            if key in self.relations:
                raise ValueError(f"duplicate relation {key}")
            sign = int(s)
            self.relations[key] = Relation(a, b, sign, key=key)
            self._add('RELATION', a, b, sign, key)
            return

        m = re.fullmatch(r"path\s+(\S+)\s*=\s*epsilon\((\S+)\)", line)
        if m:
            name, entity = m.groups()
            if name in self.paths:
                raise ValueError(f"duplicate path {name}")
            if entity not in self.entities:
                raise ValueError(f"unknown entity {entity}")
            self.paths[name] = Path((), entity, entity)
            self._add('EPSILON', name, entity)
            return

        m = re.fullmatch(r"path\s+(\S+)\s*=\s*(\S+(?:->\S+)*)", line)
        if m:
            name, nodes = m.groups()
            if name in self.paths:
                raise ValueError(f"duplicate path {name}")
            ids = nodes.split('->')
            if len(ids) < 2:
                raise ValueError("non-empty path needs at least one relation; use epsilon(entity) for an empty path")
            if any(x not in self.entities for x in ids):
                raise ValueError("path endpoint entity is absent")
            rs = []
            for a, b in zip(ids, ids[1:]):
                candidates = [r for r in self.relations.values() if r.src == a and r.dst == b]
                if not candidates:
                    raise ValueError(f"missing relation {a}->{b}")
                if len(candidates) > 1:
                    raise ValueError(f"ambiguous relation {a}->{b}; assign and use an explicit relation key")
                rs.append(candidates[0])
            self.paths[name] = Path(tuple(rs), ids[0], ids[-1])
            self._add('PATH', name, tuple(ids))
            return

        m = re.fullmatch(r"concat\s+(\S+)\s*=\s*(\S+)\s*\+\s*(\S+)", line)
        if m:
            name, left, right = m.groups()
            if name in self.paths:
                raise ValueError(f"duplicate path {name}")
            if left not in self.paths or right not in self.paths:
                raise ValueError("unknown path in CONCAT")
            self.paths[name] = concat(self.paths[left], self.paths[right])
            self._add('CONCAT', name, left, right)
            return

        m = re.fullmatch(r"incident\s+(\S+)\s+(\S+)", line)
        if m:
            entity, relation = m.groups()
            if entity not in self.entities:
                raise ValueError(f"unknown entity {entity}")
            if relation not in self.relations:
                raise ValueError(f"unknown relation {relation}")
            self.results.append(incident(self.entities[entity], self.relations[relation]))
            self._add('INCIDENT', entity, relation)
            return

        m = re.fullmatch(r"(dist|sign|cycle|path_eq)\s+(.+)", line)
        if m:
            op, rest = m.groups()
            args = rest.split()
            if op == 'dist':
                if len(args) != 2 or args[0] not in self.entities or args[1] not in self.entities:
                    raise ValueError('DIST needs two known entities')
                self.results.append(dist(self.entities[args[0]], self.entities[args[1]]))
                self._add('DIST', args[0], args[1])
            elif op == 'sign':
                if len(args) != 1 or args[0] not in self.paths:
                    raise ValueError('SIGN needs one known path')
                self.results.append(self._sign(self.paths[args[0]]))
                self._add('SIGN', args[0])
            elif op == 'cycle':
                if len(args) != 1 or args[0] not in self.paths:
                    raise ValueError('CYCLE needs one known path')
                p = self.paths[args[0]]
                self.results.append(p.length > 0 and p.source == p.target)
                self._add('CYCLE', args[0])
            else:
                if len(args) != 2 or args[0] not in self.paths or args[1] not in self.paths:
                    raise ValueError('PATH_EQ needs two known paths')
                self.results.append(self.paths[args[0]] == self.paths[args[1]])
                self._add('PATH_EQ', args[0], args[1])
            return

        raise ValueError('unsupported syntax')

    @staticmethod
    def _sign(p):
        out = 1
        if not p.relations:
            raise ValueError('SIGN requires non-empty path')
        for r in p.relations:
            out *= r.sign
        return out
