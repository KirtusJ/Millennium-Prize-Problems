"""Follow-up to directstep.py, in which D1 FAILED (result kept in directstep_result.txt; D2 to D5 were met).
Diagnosis: D1 was evaluated as (1 - b) exp(t u) - ||Pv||^2 with b = 1 - ||P exp(-tH) P|| in floating point. When
the norm is below rounding, 1 - b is exactly 0 while exp(t u) is huge or overflows, so the comparison is between
0 or 'not a number' and a positive quantity. The inequality itself was not at fault. Here the three inequalities
are compared in logarithms with the norms themselves, and instances whose norm ||P exp(-tH) P|| or
||B exp(-sH) B|| is below 1e-250 are skipped and counted.
PREDICATE (fixed before the first run), 20000 instances, seed 22:
 E1 for a random unit vector v in the span of the eigenvectors with energy <= u (u an eigenvalue):
    log ||Pv||^2 <= log ||P exp(-tH) P|| + t u + 1e-9,  log ||Bv||^2 <= log ||B exp(-sH) B|| + s u + 1e-9,
    ||Gv||^2 <= ||G E([0,u]) G|| + 1e-12.
Output directstep2_result.txt (not overwritten). Command: python3 directstep2.py"""
import numpy as np
rng=np.random.default_rng(22); fail=0; skip=0; worst=-np.inf; nrm=lambda M: np.linalg.norm(M,2)
for it in range(20000):
    n=int(rng.integers(4,22)); lo=10**rng.uniform(-3,1); ev=np.sort(lo*10**rng.uniform(0,rng.uniform(0.3,3),size=n)); ev[0]=lo
    U,_=np.linalg.qr(rng.normal(size=(n,n))); W,_=np.linalg.qr(U+10**rng.uniform(-3,0.5)*rng.normal(size=(n,n))) if rng.random()<0.6 else np.linalg.qr(rng.normal(size=(n,n)))
    r=int(rng.integers(1,n-1)); sB=int(rng.integers(1,n-r)) if n-r>1 else 0
    P=W[:,:r]@W[:,:r].T; B=W[:,r:r+sB]@W[:,r:r+sB].T; G=np.eye(n)-P-B; t=10**rng.uniform(-2,2); s=t*rng.uniform(0.01,1.0)
    pn=nrm(P@(U*np.exp(-t*ev))@U.T@P); bn=nrm(B@(U*np.exp(-s*ev))@U.T@B) if sB else 1.0
    if pn<1e-250 or bn<1e-250: skip+=1; continue
    k=int(rng.integers(0,n)); u=ev[k]; V=U[:,:k+1]; c=rng.normal(size=k+1); v=V@(c/np.linalg.norm(c)); F=np.linalg.eigvalsh(V.T@G@V).max()
    e1=np.log(max(v@P@v,1e-300))-np.log(pn)-t*u; e2=(np.log(max(v@B@v,1e-300))-np.log(bn)-s*u) if sB else -1.0; e3=v@G@v-F
    worst=max(worst,e1,e2); fail+=(e1>1e-9) or (e2>1e-9) or (e3>1e-12)
out=["instances 20000, skipped %d, failures %d, largest excess in logarithm %.3e"%(skip,fail,worst),"E1 %s"%("MET" if fail==0 else "FAILED")]
open('directstep2_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
