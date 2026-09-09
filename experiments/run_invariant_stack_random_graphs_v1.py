"""Independent invariant-stack check on random directed graphs.

Important: signed pairwise orientation is NOT relabelling-invariant because
its sign convention depends on the arbitrary ordering i<j. The invariant
quantities are magnitude statistics (mean absolute asymmetry and RMS).
"""
from __future__ import annotations
import numpy as np

SEED = 20260909

def floyd_warshall(w: np.ndarray) -> np.ndarray:
    d = w.copy()
    np.fill_diagonal(d, 0.0)
    for k in range(len(d)):
        d = np.minimum(d, d[:, k, None] + d[None, k, :])
    return d

def signature(d: np.ndarray) -> tuple[float, float, float]:
    vals=[]
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            den=d[i,j]+d[j,i]
            if np.isfinite(den) and den>0:
                vals.append((d[i,j]-d[j,i])/den)
    a=np.asarray(vals)
    return float(a.mean()), float(np.abs(a).mean()), float(np.sqrt(np.mean(a*a)))

def main() -> None:
    rng=np.random.default_rng(SEED)
    records=[]
    for n in (8,12,20,32):
        for rep in range(25):
            a=(rng.random((n,n))<0.22) & (~np.eye(n,dtype=bool))
            for i in range(n):
                a[i,(i+1)%n]=True
            w=np.where(a,rng.uniform(.2,2.0,(n,n)),np.inf)
            d=floyd_warshall(w)
            base=signature(d)
            p=rng.permutation(n)
            rel=signature(d[np.ix_(p,p)])
            scaled=signature(d*17.3)
            rev=signature(d.T)
            assert np.allclose(base[1:],rel[1:])
            assert np.allclose(base[1:],scaled[1:])
            assert np.isclose(rev[0],-base[0])
            assert np.allclose(rev[1:],base[1:])
            records.append((n,base,rel,scaled,rev))
    print(f"graphs={len(records)}")
    print("magnitude_relabel_invariance=PASS")
    print("magnitude_positive_scale_invariance=PASS")
    print("direction_reversal_signed_flip=PASS")
    print("direction_reversal_magnitude_invariance=PASS")
    print(f"mean_abs_range=({min(r[1][1] for r in records):.9f},{max(r[1][1] for r in records):.9f})")
    print("INDEPENDENT_RANDOM_GRAPH_STACK=PASS")
    print("NOTE=signed_mean_is_not_label_invariant; magnitude statistics are the invariant object")

if __name__ == "__main__":
    main()
