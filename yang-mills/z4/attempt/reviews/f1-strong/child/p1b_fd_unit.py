"""P1b (replaces failed F1/F2 of p1; failure was my own step-size expectation). Predicates fixed before run:
 F1b: unit-norm t,t' (|t|=|t'|=1), central FD of V along exp-geodesics, h=1e-3: max error over 20 pairs at each of
      3 random U and pi-flux < 1e-5. Tolerance: truncation ~ h^2 * |V''''| ~ 1e-6 * O(10).
 F2b: error with h=5e-4 is smaller than with h=1e-3 by factor in [2.5,6] (h^2 scaling -> genuine truncation not bug), or both <1e-8.
 F3b: qform vs Hmat to 1e-10 (carried)."""
import numpy as np, sys, lgt
from lgt import *
def Vfd(U,t): return lgt.Vact(expm_su2(t.reshape(64,3))@U)
def fdH(U,t,tp,h):
    return (Vfd(U,h*(t+tp))-Vfd(U,h*(t-tp))-Vfd(U,h*(-t+tp))+Vfd(U,-h*(t+tp)))/(4*h*h)
rng=np.random.default_rng(777); out=open('results/p1b.txt','x'); ok=True
cases=[randU(rng) for _ in range(3)]+[piflux()]
for k,U in enumerate(cases):
    H=Hmat(U); e1=e2=0
    for _ in range(20):
        t=rng.normal(size=192);t/=np.linalg.norm(t);tp=rng.normal(size=192);tp/=np.linalg.norm(tp)
        ex=t@H@tp; e1=max(e1,abs(fdH(U,t,tp,1e-3)-ex)); e2=max(e2,abs(fdH(U,t,tp,5e-4)-ex))
    r=e1/e2 if e2>0 else 0
    p=e1<1e-5 and (2.5<=r<=6 or e1<1e-8)
    out.write(f"case{k} err(h=1e-3)={e1:.2e} err(h=5e-4)={e2:.2e} ratio={r:.2f} {'PASS' if p else 'FAIL'}\n"); ok&=p
out.write("ALL PASS\n" if ok else "SOME FAIL\n"); out.close(); print(open('results/p1b.txt').read()); sys.exit(0 if ok else 1)
