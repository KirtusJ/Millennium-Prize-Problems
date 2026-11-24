"""Predicates (fixed before first run):
P1(d,m,r): brute-force w_r (axis 1 weight from sites with r(x)=r, exact Fractions) == claimed value.
 d=3: 8r^2+2/3 (r<m); w_m = 4m^2-2m+1/3.   d=2: 4r (r<m); w_m = 2m-1/2.
P2(d,m): sum_r w_r == (total weight)/d by symmetry, i.e. (2m)^d-(2m-1)^d over d (exact).
Hypothesis for 'for all' (rule 4): every case has 1<=r<=m; count of qualifying cases reported.
Tolerance: none, exact rational equality. Result file opened with mode 'x'.
"""
import itertools, json, sys
from fractions import Fraction as F
out = open(sys.argv[1], "x")
met = fail = 0; p2ok = p2bad = 0; cases = 0
for d in (3, 2):
    for m in range(1, 13):
        n = 2*m
        dist = [min(c, n-c) for c in range(n)]
        w = {}
        for x in itertools.product(range(n), repeat=d):
            if not any(x): continue
            ds = [dist[c] for c in x]; r = max(ds)
            if ds[0] == r:
                k = sum(1 for v in ds if v == r)
                w[r] = w.get(r, 0) + F(1, k)
        for r in range(1, m+1):
            if d == 3:
                claim = 4*m*m - 2*m + F(1,3) if r == m else 8*r*r + F(2,3)
            else:
                claim = 2*m - F(1,2) if r == m else F(4*r)
            b = w.get(r, F(0)); cases += 1
            ok = b == claim
            met += ok; fail += (not ok)
            out.write(json.dumps(dict(d=d,m=m,r=r,brute=str(b),claim=str(claim),ok=ok))+"\n")
            if not ok: print("FAIL", d, m, r, b, claim)
        tot = sum(w.values()); exp = F(n**d-(n-1)**d, d)
        if tot == exp: p2ok += 1
        else: p2bad += 1; print("P2 FAIL", d, m, tot, exp)
print(f"cases={cases} met={met} failed={fail} qualifying(1<=r<=m)={cases} P2 ok={p2ok} bad={p2bad}")
