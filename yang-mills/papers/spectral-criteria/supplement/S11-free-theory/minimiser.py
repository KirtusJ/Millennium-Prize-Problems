"""Free theory, blocking factor 2: wider test of the statement, not proved in the paper, that the mixing rate is
smallest at the lowest axial coarse momentum. The rate at a coarse momentum depends on the side N only through the
momentum k = 2 pi q / N, so a side tests the momenta of all its divisors.
PREDICATES (fixed before the first run):
 Z1 side 256: over all coarse momenta q in {0..127}^3 (by symmetry: q1 >= q2 >= q3), the smallest rate is attained
    at q = (1,0,0), and no other class is within 1e-12 of it.
 Z2 small momenta in all directions: at side 2^20, for every q with 0 <= q3 <= q2 <= q1 <= 8, q != 0,
    rate(q) >= rate(1,0,0) - 1e-12.
 Z3 along the axis at side 256: rate(j,0,0) >= rate(1,0,0) for j = 1..127, and the rate is non-decreasing in j
    for j = 1..64 (reported; if it fails the first j where it decreases is printed).
No random numbers. Output minimiser_result.txt (not overwritten). Command: python3 minimiser.py"""
import numpy as np, itertools
src=open('matrixbridge.py').read(); exec(src[src.index("def omega"):src.index("out=[];res={}")])
out=[]
N=256; best=[]; 
for q1 in range(N//2):
    for q2 in range(q1+1):
        for q3 in range(q2+1):
            if q1==0: continue
            best.append((blk(N,(q1,q2,q3))[0],(q1,q2,q3)))
best.sort(); out.append("side 256: %d classes; five smallest rates: %s"%(len(best)," ".join("%.9f %s"%b for b in best[:5])))
Z1=best[0][1]==(1,0,0) and best[1][0]-best[0][0]>1e-12; out.append("Z1 %s"%("MET" if Z1 else "FAILED"))
N=2**20; g0=blk(N,(1,0,0))[0]; worst=(np.inf,None)
for q1 in range(1,9):
    for q2 in range(q1+1):
        for q3 in range(q2+1):
            g=blk(N,(q1,q2,q3))[0]
            if (q1,q2,q3)!=(1,0,0) and g-g0<worst[0]: worst=(g-g0,(q1,q2,q3))
out.append("side 2^20: rate(1,0,0) = %.9f ; smallest excess over it among the other small momenta: %.3e at %s"%(g0,worst[0],worst[1]))
Z2=worst[0]>=-1e-12; out.append("Z2 %s"%("MET" if Z2 else "FAILED"))
ax=[blk(256,(j,0,0))[0] for j in range(1,128)]
dec=[j+1 for j in range(1,64) if ax[j]<ax[j-1]-1e-13]
Z3=min(ax)>=ax[0]-1e-13; out.append("axis, side 256: rate at j=1,2,4,8,16,32,64,127: %s ; first decrease for j<=64: %s"%(" ".join("%.6f"%ax[j-1] for j in (1,2,4,8,16,32,64,127)),dec[0] if dec else "none"))
out.append("Z3 %s (monotone up to 64: %s)"%("MET" if Z3 else "FAILED","yes" if not dec else "no"))
open('minimiser_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
