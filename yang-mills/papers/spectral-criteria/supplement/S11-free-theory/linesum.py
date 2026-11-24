"""Free theory: a lower bound for the one-step constant of line-sum blocking, proposed by a reviewing model.
For coarse links that are sums of r fine links, at the axial soft momentum k = (k_1, 0, 0) with polarisation e_2,
the aliases (k_1 + 2 pi l / r, 0, 2 pi j / r) all carry the multiplier r, and a trial vector in the fine detail gives
   sup_N c_{r,N}  >=  S_r = sum over (l, j) != (0, 0), 0 <= l, j < r, of 1 / sinh w_{lj},
   cosh w_{lj} = 1 + 2 sin^2(pi l / r) + 2 sin^2(pi j / r),   hence  c_r / r >= (r^2 - 1)/(r sqrt 24).
PREDICATES (fixed before the first run):
 S1 (known answers, values reported by the reviewer) S_r / r = 0.4556, 1.4169, 3.4263, 7.4675, 31.7289, 128.7775
    for r = 2, 4, 8, 16, 64, 256, each to 5e-5.
 S2 S_r / r >= (r^2 - 1)/(r sqrt 24) for those r.
 S3 the constants computed in onestep_result.txt at the lowest axial momentum of side 1024 r (r = 2, 3, 4, 6, 8)
    are at least S_r (1 - 1e-3) (the bound is the limit of small momentum) and exceed it by less than 2 per cent
    (so the trial vector is nearly optimal).
 S4 S_2 / 2 equals (2/sqrt 8 + 1/sqrt 24)/2, half the constant of the remark on the low-energy weight.
Output linesum_result.txt (not overwritten). Command: python3 linesum.py"""
import numpy as np, re
def S(r):
    l=np.arange(r); c=1+2*np.sin(np.pi*l/r)[:,None]**2+2*np.sin(np.pi*l/r)[None,:]**2; c[0,0]=np.inf
    return (1/np.sqrt(c**2-1)).sum()
out=[]; ref={2:0.4556,4:1.4169,8:3.4263,16:7.4675,64:31.7289,256:128.7775}
S1=all(abs(S(r)/r-v)<5e-5 for r,v in ref.items()); S2=all(S(r)/r>=(r*r-1)/(r*np.sqrt(24)) for r in ref)
out.append("S_r / r: "+" ".join("r=%d %.4f"%(r,S(r)/r) for r in ref)); out.append("simplified bound: "+" ".join("r=%d %.4f"%(r,(r*r-1)/(r*np.sqrt(24))) for r in ref))
comp={}
for line in open('onestep_result.txt'):
    mm=re.match(r"r=(\d+) N=\d+ lowest axial momentum: c=([\d.]+)",line)
    if mm: comp[int(mm.group(1))]=float(mm.group(2))
S3=all(comp[r]>=S(r)*(1-1e-3) and comp[r]<=S(r)*1.02 for r in comp)
out.append("computed against bound: "+" ".join("r=%d %.4f/%.4f"%(r,comp[r],S(r)) for r in sorted(comp)))
S4=abs(S(2)/2-(2/np.sqrt(8)+1/np.sqrt(24))/2)<1e-12
for nm,v in zip(("S1","S2","S3","S4"),(S1,S2,S3,S4)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open('linesum_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
