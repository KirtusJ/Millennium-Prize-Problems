"""Statement A random test. Predicates fixed BEFORE first run:
 Q1 (qualifying): gamma>0, gamma = 1/lambda_max(M^{-1/2} G M^{-1/2}), M=I-S_2a (M PD since lambda_min(H)>0).
 Q2 (cross-check): bisection gamma_b agrees with gamma to rel 1e-6 (tolerance: bisection 200 steps; eigvalsh error ~1e-12*cond).
 F  (failure of claim): slack = d*(1+2a/(gamma t)) - (b-kappa) < -1e-9 (and also d < max(b-kappa,0)/(1+..) - 1e-9).
    Tolerance 1e-9: float64 eps~1e-16 times cond numbers up to ~1e4 from near-singular M; no tolerance is applied to the min-slack report itself.
 Seed 195, N=3000 cases; dims 3..8; 1/3 of cases have tiny smallest eigenvalue of H (shift 1e-9..1e-6, H projected so lam_min tiny).
 rank P>=1, rank B>=1, rank G>=1 (rp+rb<=n-1). a in [1e-3,2] (log-uniform), t in [0.05,3], tau~U(0,t].
"""
import numpy as np, sys
rng=np.random.default_rng(195)
N=3000; nq=0; fails=[]; minslack=np.inf; bis_bad=0; minrec=None
def fexp(H,s):
    w,V=np.linalg.eigh(H); return (V*np.exp(-s*w))@V.T
with open("A_cases.csv","x") as out:
    out.write("i,n,rp,rb,a,t,tau,lam,gamma,kappa,b,d,slack\n")
    for i in range(N):
        n=int(rng.integers(3,9))
        M0=rng.normal(size=(n,n)); H=M0@M0.T/n
        if i%3==0:  # tiny smallest eigenvalue
            w,V=np.linalg.eigh(H); w=w-w[0]+10**rng.uniform(-9,-6); H=(V*w)@V.T
        else: H=H+10**rng.uniform(-6,-1)*np.eye(n)
        H=(H+H.T)/2
        rp=int(rng.integers(1,n-1)); rb=int(rng.integers(1,n-rp))
        Q,_=np.linalg.qr(rng.normal(size=(n,n)))
        P=Q[:,:rp]@Q[:,:rp].T; B=Q[:,rp:rp+rb]@Q[:,rp:rp+rb].T
        G=np.eye(n)-P-B
        a=10**rng.uniform(-3,np.log10(2)); t=rng.uniform(0.05,3); tau=t*(1-rng.uniform(0,1))
        h,V=np.linalg.eigh(H); lam=h[0]
        M=(V*(-np.expm1(-2*a*h)))@V.T
        mw,mV=np.linalg.eigh(M); Mih=(mV/np.sqrt(mw))@mV.T
        ev=np.linalg.eigvalsh(Mih@G@Mih)[-1]
        gamma=1/ev if ev>0 else 0
        if gamma<=0: continue
        # bisection cross-check
        lo,hi=0,gamma*4
        for _ in range(200):
            mid=(lo+hi)/2
            if np.linalg.eigvalsh(M-mid*G)[0]>=0: lo=mid
            else: hi=mid
        if abs(lo-gamma)>1e-6*gamma: bis_bad+=1
        nq+=1
        kappa=np.linalg.norm(B@fexp(H,tau)@B,2)
        b=1-np.linalg.norm(P@fexp(H,t)@P,2)
        d=-np.expm1(-t*lam)
        slack=d*(1+2*a/(gamma*t))-(b-kappa)
        slack2=d-max(b-kappa,0)/(1+2*a/(gamma*t))
        out.write(f"{i},{n},{rp},{rb},{a:.6g},{t:.6g},{tau:.6g},{lam:.6g},{gamma:.6g},{kappa:.9g},{b:.9g},{d:.9g},{slack:.6g}\n")
        if slack<minslack: minslack=slack; minrec=(i,n,rp,rb,a,t,tau,lam,gamma,kappa,b,d)
        if slack<-1e-9 or slack2<-1e-9: fails.append((i,slack,slack2))
print("seed 195 N",N,"qualifying",nq,"failures",len(fails),"bisection_mismatch",bis_bad)
print("min slack d*(1+2a/(gamma t))-(b-kappa) = %.6e"%minslack, "at case",minrec)
print("fails:",fails[:10])
