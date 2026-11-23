"""Predicate fixed before run: P6 lattice random (seed 777), beta=1: nested FD with inner step 1e-3 (gradient) and outer step 3e-3 (not symmetric by construction); sym err < 1e-5 (tol: truncation ~ (h_in^2+h_out^2)*|f''''| ~1e-5 scale, so 1e-4 is the honest bound; use 1e-4). Also P7: min eig of B from symmetrized part vs hess.py value -1.30789342 within 1e-4."""
import sys,numpy as np
sys.argv=[sys.argv[0],"/dev/null"]
src=open("hess.py").read().split("out=open")[0]
exec(src)
rng=np.random.default_rng(777); Ul=[randSU2(rng) for _ in range(8)]
fl=lambda U:Vlat(U,1.0); n=24; hi,ho=1e-3,3e-3
def g(t0):
    G=np.zeros(n)
    for i in range(n):
        tp=t0.copy();tp[i]+=hi;tm=t0.copy();tm[i]-=hi
        G[i]=(fl(pert(Ul,tp))-fl(pert(Ul,tm)))/(2*hi)
    return G
H=np.zeros((n,n))
for j in range(n):
    tp=np.zeros(n);tp[j]=ho;tm=np.zeros(n);tm[j]=-ho
    H[:,j]=(g(tp)-g(tm))/(2*ho)
sym=np.abs(H-H.T).max(); m=np.linalg.eigvalsh(np.eye(n)+(H+H.T)/2)[0]
f=open("results2.txt","x")
for l in ["P6 sym err %.3e %s"%(sym,"PASS" if sym<1e-4 else "FAIL"),"P7 min eig B %.8f diff vs -1.30789342 = %.2e %s"%(m,abs(m+1.3078934151668542),"PASS" if abs(m+1.3078934151668542)<1e-4 else "FAIL")]:
    print(l); f.write(l+"\n")
