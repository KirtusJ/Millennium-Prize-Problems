"""Fit -log m = c sqrt(b) + bb log(b) + c0. Predicates P4 (|c-c*|<0.03 c*), P5 (ratio increasing). Also naive eigh check at beta=64 (P6, measured only:
naive lam_e-lam_o vs identity delta; expected agreement only to ~1e-16/2e-14 ~ 1e-2 relative)."""
import json, math, numpy as np
from split import K, CSTAR
r=json.load(open("split_results.json")); bs=[64,256,1024,4096]
def fit(tag, extrap):
    y=[]
    for b in bs:
        lh=r[str(b)]["h"]["logm"]; l2=r[str(b)]["h/2"]["logm"]
        y.append(-(l2+(l2-lh)/3 if extrap else l2))
    y=np.array(y); X=np.array([[math.sqrt(b),math.log(b),1] for b in bs])
    s=np.linalg.solve(X[:3],y[:3]) if False else np.linalg.lstsq(X,y,rcond=None)[0]
    print(tag,"ratios",[round(v/math.sqrt(b),6) for v,b in zip(y,bs)],"fit c,b,c0=",s,"resid",X@s-y)
    X2=np.array([[math.sqrt(b),1] for b in bs]); s2=np.linalg.lstsq(X2,y,rcond=None)[0]; print("  2-param (no log) c,c0=",s2)
    X3=X[1:]; s3=np.linalg.solve(X3,y[1:]); print("  3 largest betas exact solve c,b,c0=",s3)
    return s[0]
c1=fit("h/2 grid",False); c2=fit("Richardson h^2",True)
print("P4 met?",abs(c1-CSTAR)<0.03*CSTAR,abs(c2-CSTAR)<0.03*CSTAR,"c*",CSTAR)
rat=[-r[str(b)]["h/2"]["logm"]/math.sqrt(b) for b in bs]; print("P5 increasing",all(np.diff(rat)>0), "gap to c*",[CSTAR-x for x in rat])
# naive check beta=64, n=63
beta=64;n=63;h=(np.pi/2)/n;a=(np.arange(n)+.5)*h;w=np.exp(-np.arcsinh(np.sin(a)));ai=a[:,None];aj=a[None,:]
S=h*w[:,None]*w[None,:]*(K(ai-aj,beta)+K(ai+aj,beta));B=h*w[:,None]*w[None,:]*(K(ai+aj-np.pi,beta)+K(ai-aj-np.pi,beta))
le=np.linalg.eigvalsh(S+B)[-1];lo=np.linalg.eigvalsh(S-B)[-1]
print("naive lam_e-lam_o",le-lo,"identity 2.0944291372358195e-14 ; naive log m",math.log((le-lo)/lo))
