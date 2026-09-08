"""Run finite executable verification records for Ω-Math v0.9.

This runner mirrors the frozen finite claims of experiments 010-012.
It prints PASS/FAIL records and exits non-zero on failure.
"""
from itertools import product


def reach(edges, enabled, horizon):
    current = {0}
    seen = {0}
    for _ in range(horizon):
        nxt = {b for a, b in edges if (a, b) in enabled and a in current}
        seen |= nxt
        current = nxt
        if not current:
            break
    return seen


def experiment_010():
    edges = {(0, 1), (1, 2), (2, 3), (0, 3)}
    assert reach(edges, {(0, 1), (1, 2), (2, 3)}, 1) == {0, 1}
    assert reach(edges, edges, 1) == {0, 1, 3}
    assert reach(edges, edges - {(1, 2)}, 3) == {0, 1, 3}


def experiment_011():
    edges = ((0, 1), (1, 2), (2, 3), (0, 3))
    for lm in range(16):
        loc = {edges[i] for i in range(4) if lm & (1 << i)}
        for am in range(16):
            adm = {edges[i] for i in range(4) if am & (1 << i)}
            eff = loc & adm
            for h in range(4):
                assert reach(set(edges), loc & adm, h) == reach(set(edges), eff, h)


def experiment_012():
    states = list(product((0, 1), repeat=2))
    functions = list(product(states, repeat=4))
    assert len(functions) == 256
    identical = 0
    interventionally_distinct = 0
    for f1 in functions:
        m1 = dict(zip(states, f1))
        for f2 in functions:
            m2 = dict(zip(states, f2))
            for s in states:
                t1 = (s, m1[s], m1[m1[s]])
                t2 = (s, m2[s], m2[m2[s]])
                if t1 != t2:
                    continue
                identical += 1
                x, y = s
                different_after_intervention = False
                for v in (0, 1):
                    if m1[(v, y)] != m2[(v, y)]:
                        different_after_intervention = True
                    if m1[(x, v)] != m2[(x, v)]:
                        different_after_intervention = True
                if different_after_intervention:
                    interventionally_distinct += 1
    assert identical == 28672
    assert interventionally_distinct == 25344


def main():
    checks = [("010 locality/admissibility/boundary", experiment_010),
              ("011 interaction/reduction", experiment_011),
              ("012 causal intervention", experiment_012)]
    for name, fn in checks:
        fn()
        print(f"PASS {name}")
    print("PASS Ω-Math v0.9 executable verification suite")


if __name__ == "__main__":
    main()
