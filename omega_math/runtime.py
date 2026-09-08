"""Reference semantics for the canonical Ω-Math operators."""
from .core import *
from collections import deque
from itertools import product


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

def sufficient(reduction, task, domain):
    vals = {}
    for x in domain:
        q = reduction(x); f = task(x)
        if q in vals and vals[q] != f: return False, (next(k for k in domain if reduction(k)==q and task(k)==vals[q]), x)
        vals[q] = f
    return True, None

def invariant(prop, transforms, domain):
    return all(prop(t(x)) == prop(x) for x in domain for t in transforms)

def quotient_distance(classes, base_distance):
    """Return the infimum representative distance for a finite quotient."""
    return {(a,b): min(base_distance(x,y) for x in a for y in b) for a in classes for b in classes}

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

def order(history): return tuple(range(len(history)))
def horizon(h):
    if h < 0: raise ValueError("horizon must be non-negative")
    return tuple(range(h+1))
def feedback(state, model, transition, inp=None):
    return transition(state, inp) if model(state) else state
def coarse(structure, criterion): return criterion(structure)
def retain(state, rule): return rule(state)

def execute(op, *args, **kwargs):
    table = {
        "DIST": dist, "INCIDENT": incident, "PATH": path, "PATH_EQ": path_eq,
        "CYCLE": cycle, "CONCAT": concat, "SIGN": sign_summary, "COMPARE": compare,
        "TRANSFORM": transform, "OBSERVE": observe, "EQUIV": equiv, "BEHAVIOR": behavior,
        "COST": cost, "REACH": reach, "BRANCH": branch, "INVARIANT": invariant,
        "QUOTIENT_DISTANCE": quotient_distance, "ORDER": order, "HORIZON": horizon,
        "FEEDBACK": feedback, "COARSE": coarse, "RETAIN": retain,
    }
    if op not in table: raise KeyError(f"unknown or non-primitive operator: {op}")
    return table[op](*args, **kwargs)
