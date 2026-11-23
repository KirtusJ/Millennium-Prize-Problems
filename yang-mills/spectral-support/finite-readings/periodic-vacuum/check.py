"""Finite transfer controls and the fixed four-lag contrast on stored chain means."""
import argparse
import hashlib
import io
import json
import math
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from zipfile import ZipFile

import numpy as np

HERE = Path(__file__).resolve().parent
Z4 = HERE.parents[2] / "z4/attempt/reviews/i1-mc3/xcheck/b4.json"
Z4_HASH = "e7c072e172214de75ac31c1195373692e97267059f31c72f1b3c2e116591e0be"
G4_HASH = "279fd2d20c36f3cb1c9bfc1729adaf171785d1ac2ccb8b0d618415b3c19bd952"


def kernel(q, r, T, t):
    return (r + 1/r - q - 1/q) * (1-q) * q**t * (1-q**(T-2*t-1))


def envelope(r, T, t, cells):
    """Rational upper enclosures for the two suprema on [r,1]."""
    assert 0 < r < 1 and 1 <= t and T >= 2*t+2 and cells > 0
    hv = he = F(0)
    for k in range(cells):
        a = r + (1-r)*k/cells
        b = r + (1-r)*(k+1)/cells
        top = (r + 1/r - b - 1/b) * (1-a) * b**t * (1-a**(T-2*t-1))
        hv = max(hv, top)
        he = max(he, top/(1+a**T))
    return hv, he


def finite_controls():
    T, t, r = 8, 2, F(1, 3)
    hv, he = envelope(r, T, t, 64)
    cases = 0
    # Independently form the complete thermal trace at each lag. A signs a
    # symmetric tridiagonal-plus-corner observable with zero diagonal.
    for roots in [(F(1), F(1, 2), F(1, 4)), (F(1), F(1, 4), F(1, 8)),
                  (F(1), F(1, 2), F(1, 2)), (F(1), r, F(1, 9))]:
        Z = sum(v**T for v in roots)
        p = [v**T/Z for v in roots]
        for a, b, c in product((-1, 0, 1), repeat=3):
            A = [(0,a,b), (a,0,c), (b,c,0)]
            def trace(s):
                return sum(ri**(T-s) * rj**s * A[i][j]**2
                           for i,ri in enumerate(roots) for j,rj in enumerate(roots))/Z
            d = [trace(s)-trace(s+1) for s in range(t-1,t+2)]
            value = (r+1/r)*d[1]-d[0]-d[2]
            paired = sum(p[i]*A[i][j]**2*kernel(roots[j]/roots[i],r,T,t)
                         for i in range(3) for j in range(i+1,3))
            assert value == paired
            mu = sum(A[0][j]**2 for j in (1,2) if roots[j] > r)
            norm2 = max(sum(map(abs,row)) for row in A)**2
            assert value <= hv*p[0]*mu + he*(1-p[0])*norm2
            if roots[1] <= r:
                tail = (sum(roots)-1)*r**(T-1)
                assert 1-p[0] <= tail/(1+tail)
            if roots[1:] == (F(1,4),F(1,8)) and (a,b,c) == (0,0,1):
                assert value > 0 and mu == 0
            cases += 1
    # Independent magnetic factors on a two-point space, electric Markov
    # operator [[3,1],[1,3]]/4. Evaluate the upper rank-one eigenvalue
    # comparison and trace cancellation by Rayleigh quotient, all rational.
    for x, y in product(range(1, 9), repeat=2):
        spatial = F(x*x+y*y, 2)
        rayleigh = F(3*x**4 + 2*x*x*y*y + 3*y**4, 4*(x*x+y*y))
        trace = F(3*(x*x+y*y), 4)
        assert rayleigh >= spatial and trace/spatial == F(3,2)
    print(f"{cases} exact spectral controls and 64 magnetic comparisons passed")


def fixed_contrasts(chains, T):
    t = 2
    for r in (F(2,5), F(1,3)):
        hv, he = envelope(r, T, t, 1024)
        diffs = chains[:, :-1]-chains[:, 1:]
        w = float(r+1/r)*diffs[:,t]-diffs[:,t-1]-diffs[:,t+1]
        mean = w.mean()
        se = w.std(ddof=1)/math.sqrt(len(w))
        # Three estimated SE serve only as a reproducible sensitivity margin.
        qmin = 3*(mean-3*se)/float(he)
        if qmin >= 1:
            consequence = "excited-only allowance exceeded for every occupation"
        elif qmin > 0:
            gap = math.log(1727*(1-qmin)/qmin)/(T-1)
            consequence = f"q_req={qmin:.6f}  g_max={gap:.6f}"
        else:
            consequence = "no positive margin"
        print(f"T={T:2d} r={r} W={mean:+.9f} SE={se:.9f} "
              f"He<={float(he):.8f} (rounded)  {consequence}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("g4_zip", type=Path, help="pinned joint-refinement/z4-controls.zip")
    args = parser.parse_args()
    finite_controls()
    blob = Z4.read_bytes()
    assert hashlib.sha256(blob).hexdigest() == Z4_HASH
    doc = json.loads(blob)
    rows = np.asarray(doc["sOO"])
    # Q=1-s. The two raw tensor components lack factors 1/sqrt(2), 1/sqrt(6).
    fixed_contrasts((rows[:,0,0]/2 + rows[:,1,1]/6)/2, doc["T"])
    blob = args.g4_zip.read_bytes()
    assert hashlib.sha256(blob).hexdigest() == G4_HASH
    with ZipFile(io.BytesIO(blob)) as z:
        for base in ("d3_b4", "d3_b4_T48"):
            meta = json.loads(z.read(f"rerun/{base}.json"))
            with np.load(io.BytesIO(z.read(f"rerun/{base}.npz")), allow_pickle=False) as a:
                rows = a["C_E"][:,:,0,0,:].sum(axis=0)/a["nmeas"].sum()
            assert rows.shape == (meta["NCH"], meta["T"]//2+1)
            fixed_contrasts(rows, meta["T"])


if __name__ == "__main__":
    main()
