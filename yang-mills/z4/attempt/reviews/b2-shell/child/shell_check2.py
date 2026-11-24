"""P2'(d,m): sum_r w_r == ((2m)^d - 1)/d exactly (symmetry: nonzero sites total weight (2m)^d-1, split equally over d axes). Exact, no tolerance. Corrects P2 of shell_check.py (own expectation error)."""
import itertools, sys
from fractions import Fraction as F
open(sys.argv[1],"x").close()
ok=0;bad=0
for d in (3,2):
  for m in range(1,13):
    n=2*m;dist=[min(c,n-c) for c in range(n)];t=F(0)
    for x in itertools.product(range(n),repeat=d):
        if not any(x):continue
        ds=[dist[c] for c in x];r=max(ds)
        if ds[0]==r:t+=F(1,ds.count(r))
    if t==F(n**d-1,d):ok+=1
    else:bad+=1;print("FAIL",d,m,t)
print("P2' ok",ok,"bad",bad)
