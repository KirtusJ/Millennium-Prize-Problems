"""exact3d.py -- independent recomputation of the grandchild's exact 3D Z2 numbers.
Z2 LGT on periodic 2x2x2 (24 links, 24 plaquettes), weight exp(beta*sum sigma_P),
twist: flip coupling on the plaquettes of plane (0,1) with x0=x1=0 (2 plaquettes, x2=0,1).
Full enumeration of 2^24 configs. Predicate (fixed before run): |F - ref| < 1e-6 for
ref(0.3)=0.0325242683, ref(0.6)=0.6912790067 (grandchild values); tolerance = float64
summation error over 2^24 terms is << 1e-9, so 1e-6 is generous. Output mode "x"."""
import numpy as np, itertools, sys
L=2; sites=list(itertools.product(range(L),repeat=3))
idx=lambda x,m: (x[0]*4+x[1]*2+x[2])*3+m
plaq=[]; tw=[]
for x in sites:
    for a,b in ((0,1),(0,2),(1,2)):
        xa=list(x); xa[a]=(xa[a]+1)%L; xb=list(x); xb[b]=(xb[b]+1)%L
        plaq.append((idx(x,a),idx(xa,b),idx(xb,a),idx(x,b)))
        tw.append((a,b)==(0,1) and x[0]==0 and x[1]==0)
tw=np.array(tw); res={}
for beta in (0.3,0.6):
    Z=0.0; Zt=0.0
    for hi in range(256):
        c=(np.arange(1<<16,dtype=np.uint32))|(np.uint32(hi)<<16)
        s=[1-2*((c>>i)&1).astype(np.int8) for i in range(24)]
        P=np.stack([s[p[0]]*s[p[1]]*s[p[2]]*s[p[3]] for p in plaq]).astype(float)
        E=P.sum(0); Et=E-2*P[tw].sum(0)
        Z+=np.exp(beta*E).sum(); Zt+=np.exp(beta*Et).sum()
    res[beta]=-np.log(Zt/Z)
ref={0.3:0.0325242683,0.6:0.6912790067}
out=open("results_exact3d.txt","x")
ok=True
for b in res:
    m=abs(res[b]-ref[b])<1e-6; ok&=m
    out.write(f"beta={b} F={res[b]:.10f} ref={ref[b]} {'MET' if m else 'FAILED'}\n")
out.close(); sys.exit(0 if ok else 1)
