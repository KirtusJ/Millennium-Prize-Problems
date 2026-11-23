"""T37 test of (A) ball-volume scaling and (B) Hessian form, SU(3) fund and U(1).
PREDICATES (fixed before first run):
 P1 U(1): V_MC(s) vs exact arccos(1-s)/pi, 4e6 samples, s in {.01,.02,.05,.1}: |err| < 5*sqrt(V(1-V)/n).
 P2 U(1): exact log-log slope over s in [1e-3,1e-2] within 0.02 of 0.5 (exact deviation is O(s)~0.005).
 P3 SU(3) Haar sanity: max|det-1|<1e-12; |E|trU|^2 - 1| < 5/sqrt(M).
 P4 SU(3) direct MC (M=4e6, seed 1): slope of V(s) over s in [0.02,0.12] within 0.3 of 4
    (a priori: O(s) exponent corrections + MC noise); c_hat=V/s^4 reported.
 P5 SU(3) Weyl formula (independent, Haar=(1/6)(2pi)^-2 |Delta|^2 dth1 dth2, th3=-th1-th2), box importance MC,
    1e6 pts per s, seed 2: agrees with direct MC within 5 combined sigma at s in {.05,.1,.15}; Weyl slope over s in [1e-3,1e-2] within 0.1 of 4;
    Weyl normalization (s=2: whole torus) integral = 1 within 5 sigma.
 P6 (B) U(1), SU(3): 30 random X each (seed 3), t in {1e-2,1e-3}: |f/t^2 - q|/q <= 2 t^2 ||X||_F^2 (quartic Taylor bound, const 2 generous); q>0.
 P7 (B) SU(3) median error ratio err(t=1e-1)/err(t=1e-2) in [50,200] (O(t^2) behaviour).
"""
import numpy as np, sys
def haar_su3(M, rng, chunk=500000):
    out=[]
    for _ in range(M//chunk):
        Z=(rng.standard_normal((chunk,3,3))+1j*rng.standard_normal((chunk,3,3)))/np.sqrt(2)
        Q,R=np.linalg.qr(Z)
        d=np.diagonal(R,axis1=1,axis2=2); Q=Q*(d/abs(d))[:,None,:]   # phase correction -> U(3) Haar
        det=np.linalg.det(Q); Q=Q/(det**(1/3))[:,None,None]            # principal cube root; maps U(3)->SU(3) Haar (each SU(3) elt has 3 preimages up to center, uniform)
        out.append(Q)
    return np.concatenate(out)
def fU(U,N): return 1-np.trace(U,axis1=-2,axis2=-1).real/N
def expmX(X,t):
    H=-1j*X; w,v=np.linalg.eigh(H); return (v*np.exp(1j*t*w))@v.conj().T
def slope(s,V): return np.polyfit(np.log(s),np.log(V),1)[0]
res={}
def rec(name,ok,msg): res[name]=ok; print(("PASS " if ok else "FAIL "),name,msg,flush=True)
# P1,P2
rng=np.random.default_rng(0); n=4_000_000
th=rng.uniform(-np.pi,np.pi,n); f1=1-np.cos(th)
ok=True; m=[]
for s in [.01,.02,.05,.1]:
    V=np.mean(f1<=s); ex=np.arccos(1-s)/np.pi; sg=np.sqrt(ex*(1-ex)/n); ok&=abs(V-ex)<5*sg; m.append((s,V,ex,sg))
rec("P1_U1_MC_vs_exact",ok,str(m))
ss=np.logspace(-3,-2,10); sl=slope(ss,np.arccos(1-ss)/np.pi); rec("P2_U1_slope",abs(sl-.5)<.02,f"slope={sl:.5f}")
# P3,P4
M=4_000_000; U=haar_su3(M,np.random.default_rng(1))
dd=np.abs(np.linalg.det(U)-1).max(); t2=np.mean(abs(np.trace(U,axis1=1,axis2=2))**2)
rec("P3_haar_sanity",dd<1e-12 and abs(t2-1)<5/np.sqrt(M),f"max|det-1|={dd:.2e} E|trU|^2={t2:.5f}")
fs=fU(U,3); del U
ss=np.logspace(np.log10(.02),np.log10(.12),8); Vd=np.array([np.mean(fs<=s) for s in ss]); cnt=Vd*M
sl4=slope(ss,Vd); rec("P4_SU3_direct_slope",abs(sl4-4)<.3,f"slope={sl4:.4f} counts={cnt.astype(int).tolist()} c_hat={(Vd/ss**4).round(4).tolist()}")
# P5 Weyl
rw=np.random.default_rng(2)
def weyl(s,n=1_000_000):
    a=np.arccos(1-3*s)   # 1-cos th_j <=3s for each j
    t1=rw.uniform(-a,a,n); t2=rw.uniform(-a,a,n); t3=-t1-t2
    f=(3-np.cos(t1)-np.cos(t2)-np.cos(t3))/3
    D=np.abs(np.exp(1j*t1)-np.exp(1j*t2))**2*np.abs(np.exp(1j*t1)-np.exp(1j*t3))**2*np.abs(np.exp(1j*t2)-np.exp(1j*t3))**2
    g=D*(f<=s)*(2*a)**2/(6*(2*np.pi)**2); return g.mean(),g.std()/np.sqrt(n)
# normalization over torus
n=4_000_000; t1=rw.uniform(-np.pi,np.pi,n); t2=rw.uniform(-np.pi,np.pi,n); t3=-t1-t2
D=np.abs(np.exp(1j*t1)-np.exp(1j*t2))**2*np.abs(np.exp(1j*t1)-np.exp(1j*t3))**2*np.abs(np.exp(1j*t2)-np.exp(1j*t3))**2
g=D/6; nm=g.mean(); ns=g.std()/np.sqrt(n); rec("P5a_weyl_norm",abs(nm-1)<5*ns,f"{nm:.5f}+-{ns:.5f}")
ok=True;m=[]
for s in [.05,.1,.15]:
    w,ws=weyl(s); d=np.mean(fs<=s); ds=np.sqrt(d*(1-d)/M); ok&=abs(w-d)<5*np.hypot(ws,ds); m.append((s,w,ws,d,ds))
rec("P5b_weyl_vs_direct",ok,str(m))
ss=np.logspace(-3,-2,8); Vw=np.array([weyl(s)[0] for s in ss]); sw=slope(ss,Vw)
rec("P5c_weyl_slope",abs(sw-4)<.1,f"slope={sw:.4f} c_hat(V/s^4)={(Vw/ss**4).round(3).tolist()}")
cw=[weyl(s,4_000_000)[0]/s**4 for s in (1e-3,1e-4)]; print("Weyl c_hat at s=1e-3,1e-4:",cw)
# P6,P7
rx=np.random.default_rng(3); ok6=True; ratios=[]; mx=[]
for N,kind in [(1,"U1"),(3,"SU3")]:
    for _ in range(30):
        A=rx.standard_normal((N,N))+1j*rx.standard_normal((N,N)); X=A-A.conj().T
        if N==3: X=X-np.trace(X)/3*np.eye(3)
        q=-np.trace(X@X).real/(2*N); F=np.linalg.norm(X)**2
        errs={}
        for t in (1e-1,1e-2,1e-3):
            errs[t]=abs(fU(expmX(X,t),N)/t**2-q)/q
        ok6&= q>0 and all(errs[t]<=2*t*t*F for t in (1e-2,1e-3)); mx.append((kind,max(errs[t]/(t*t*F) for t in (1e-2,1e-3))))
        if N==3: ratios.append(errs[1e-1]/errs[1e-2])
rec("P6_hessian",ok6,f"max err/(t^2 F) U1={max(v for k,v in mx if k=='U1'):.3f} SU3={max(v for k,v in mx if k=='SU3'):.3f}")
mr=np.median(ratios); rec("P7_ratio",50<=mr<=200,f"median ratio={mr:.1f}")
sys.exit(0 if all(res.values()) else 1)
