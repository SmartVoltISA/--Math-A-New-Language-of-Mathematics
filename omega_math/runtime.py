"""Reference semantics for the canonical Ω-Math operators."""
from .core import *
from .ir import IRProgram
from collections import deque
import heapq


def path(relations): return Path(tuple(relations))
def path_eq(a,b): return a == b
def cycle(p): return p.length > 0 and p.source == p.target

def transform(state, rule, inp=None):
    out = rule(state, inp) if isinstance(rule, Transformation) else rule(state, inp)
    return out

def observe(state, fn=lambda s: s): return Observation(fn(state))
def cost(t): return t.cost if isinstance(t, Transformation) else 0.0

def behavior(state, transition, observe_fn=lambda s:s, horizon=0, inputs=()):
    states = [state]
    current = {state}
    for h in range(horizon):
        nxt = set()
        inp = inputs[h] if h < len(inputs) else None
        for s in current:
            z = transition(s, inp)
            nxt.update(z if isinstance(z, (set, frozenset, tuple, list)) else [z])
        current = nxt
        states.append(current)
    return tuple(tuple(observe_fn(s) for s in sorted(level, key=repr)) if isinstance(level, set) else observe_fn(level) for level in states)

def reach(initial, transition, horizon, goal=None, inputs=()):
    current = {initial}; seen = {initial}
    if goal is not None and goal(initial): return True
    for h in range(horizon):
        nxt = set()
        inp = inputs[h] if h < len(inputs) else None
        for s in current:
            z = transition(s, inp)
            nxt.update(z if isinstance(z, (set, frozenset, tuple, list)) else [z])
        if goal is not None and any(goal(s) for s in nxt): return True
        seen.update(nxt); current = nxt
        if not current: break
    return seen if goal is None else False

def branch(state, transition, inp=None):
    z = transition(state, inp)
    return frozenset(z if isinstance(z, (set, frozenset, tuple, list)) else [z])

def equiv(x, y, key=lambda z:z, task=None):
    return key(x) == key(y) if task is None else task(x) == task(y)

def quotient(domain, equivalence):
    remaining = list(domain); classes = []
    while remaining:
        x = remaining.pop(0)
        cls = [y for y in remaining if equivalence(x, y)] + [x]
        cls_set = frozenset(cls); classes.append(cls_set)
        remaining = [y for y in remaining if y not in cls_set]
    return tuple(classes)

def sufficient(reduction, task, domain):
    vals = {}
    for x in domain:
        q = reduction(x); f = task(x)
        if q in vals and vals[q] != f:
            witness = next(k for k in domain if reduction(k)==q and task(k)==vals[q])
            return False, (witness, x)
        vals[q] = f
    return True, None

def invariant(prop, transforms, domain):
    return all(prop(t(x)) == prop(x) for x in domain for t in transforms)

def quotient_distance(classes, base_distance):
    return {(a,b): min(base_distance(x,y) for x in a for y in b) for a in classes for b in classes}

def distance(start, target, transforms, max_steps=None):
    """Minimal declared transformation cost; not physical energy."""
    if start == target: return 0.0
    heap = [(0.0, 0, start)]; best = {start: 0.0}; steps = {start: 0}; serial = 1
    while heap:
        total, _, state = heapq.heappop(heap)
        if total != best.get(state): continue
        if state == target: return total
        if max_steps is not None and steps[state] >= max_steps: continue
        for t in transforms:
            nxt = transform(state, t)
            successors = nxt if isinstance(nxt, (set, frozenset, tuple, list)) else (nxt,)
            for ns in successors:
                new_cost = total + cost(t)
                if new_cost < best.get(ns, float("inf")):
                    best[ns] = new_cost; steps[ns] = steps[state] + 1
                    heapq.heappush(heap, (new_cost, serial, ns)); serial += 1
    return float("inf")

def verify_metric(points, d):
    for x in points:
        if d(x,x) != 0: return False, "identity"
        for y in points:
            if d(x,y) < 0: return False, "non-negativity"
            if d(x,y) != d(y,x): return False, "symmetry"
            if x != y and d(x,y) == 0: return False, "separation"
            for z in points:
                if d(x,z) > d(x,y) + d(y,z): return False, "triangle"
    return True, None

def symmetry(state, transforms):
    orbit = {state}; queue = deque([state])
    while queue:
        current = queue.popleft()
        for t in transforms:
            nxt = transform(current, t)
            successors = nxt if isinstance(nxt, (set, frozenset, tuple, list)) else (nxt,)
            for ns in successors:
                if ns not in orbit: orbit.add(ns); queue.append(ns)
    return frozenset(orbit)

def model(state, representation=lambda s:s): return representation(state)
def order(history): return tuple(range(len(history)))
def horizon(h):
    if h < 0: raise ValueError("horizon must be non-negative")
    return tuple(range(h+1))
def feedback(state, model, transition, inp=None): return transition(state, inp) if model(state) else state
def coarse(structure, criterion): return criterion(structure)
def retain(state, rule): return rule(state)


def execute_ir(program: IRProgram):
    """Execute the v1 reference IR and return query results in source order."""
    program.validate()
    entities, relations, paths, results = {}, {}, {}, []
    for ins in program.instructions:
        op, args = ins.op, ins.args
        if op == 'ENTITY':
            name, state = args
            if name in entities: raise ValueError(f"duplicate entity {name}")
            entities[name] = Entity(name, state)
        elif op == 'RELATION':
            a, b, sign, key = args
            if a not in entities or b not in entities: raise ValueError("relation endpoint entity is absent")
            if key in relations: raise ValueError(f"duplicate relation {key}")
            relations[key] = Relation(a, b, sign, key=key)
        elif op == 'EPSILON':
            name, entity = args
            if entity not in entities: raise ValueError(f"unknown entity {entity}")
            if name in paths: raise ValueError(f"duplicate path {name}")
            paths[name] = Path((), entity, entity)
        elif op == 'PATH':
            name, nodes = args
            if name in paths: raise ValueError(f"duplicate path {name}")
            ids = tuple(nodes)
            if not ids or any(x not in entities for x in ids): raise ValueError("path endpoint entity is absent")
            rs = []
            for a, b in zip(ids, ids[1:]):
                candidates = [r for r in relations.values() if r.src == a and r.dst == b]
                if not candidates: raise ValueError(f"missing relation {a}->{b}")
                if len(candidates) > 1: raise ValueError(f"ambiguous relation {a}->{b}; assign and use an explicit relation key")
                rs.append(candidates[0])
            paths[name] = Path(tuple(rs), ids[0], ids[-1])
        elif op == 'CONCAT':
            name, left, right = args
            if name in paths: raise ValueError(f"duplicate path {name}")
            if left not in paths or right not in paths: raise ValueError("unknown path in CONCAT")
            paths[name] = concat(paths[left], paths[right])
        elif op == 'INCIDENT':
            entity, relation = args
            if entity not in entities or relation not in relations: raise ValueError("unknown incident operand")
            results.append(incident(entities[entity], relations[relation]))
        elif op == 'DIST':
            a, b = args
            if a not in entities or b not in entities: raise ValueError("DIST needs two known entities")
            results.append(dist(entities[a], entities[b]))
        elif op == 'SIGN':
            (name,) = args
            if name not in paths: raise ValueError("SIGN needs one known path")
            results.append(sign_summary(paths[name]))
        elif op == 'CYCLE':
            (name,) = args
            if name not in paths: raise ValueError("CYCLE needs one known path")
            results.append(cycle(paths[name]))
        elif op == 'PATH_EQ':
            left, right = args
            if left not in paths or right not in paths: raise ValueError("PATH_EQ needs two known paths")
            results.append(path_eq(paths[left], paths[right]))
        elif op == 'CALL':
            name, operands = args
            if not isinstance(operands, tuple): raise TypeError("CALL operands must be a tuple")
            results.append(execute(name, *operands))
    return results


def execute(op, *args, **kwargs):
    table = {
        "DIST": dist, "INCIDENT": incident, "PATH": path, "PATH_EQ": path_eq,
        "CYCLE": cycle, "CONCAT": concat, "SIGN": sign_summary, "COMPARE": compare,
        "TRANSFORM": transform, "OBSERVE": observe, "EQUIV": equiv, "QUOTIENT": quotient,
        "BEHAVIOR": behavior, "COST": cost, "DISTANCE": distance, "REACH": reach,
        "BRANCH": branch, "INVARIANT": invariant, "QUOTIENT_DISTANCE": quotient_distance,
        "SYMMETRY": symmetry, "MODEL": model, "ORDER": order, "HORIZON": horizon,
        "FEEDBACK": feedback, "COARSE": coarse, "RETAIN": retain,
    }
    if op not in table: raise KeyError(f"unknown or non-primitive operator: {op}")
    return table[op](*args, **kwargs)
