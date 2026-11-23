"""Follow-up after P2 convergence predicate failed (kink of eps at a=0,pi gives O(h^2) error).
Predicate: add N=1024; Richardson (h^2) extrapolation of N=512,1024 and of 256,512; report. Result opened 'x'."""
import numpy as np
exec(open('run.py').read().split("R=[]")[0].split("beta=16.")[1].join(["beta=16.",""])) if False else None
beta=16.
def run(N):
    h=2*np.pi/N; a=-np.pi+h*np.arange(N); eps=2*np.arcsinh(np.abs(np.sin(a)))
    d=a[:,None]-a[None,:]
    k=sum(np.exp(-beta*(d+2*np.pi*j)**2/2) for j in range(-2,3))*np.sqrt(beta/(2*np.pi))
    e=np.exp(-eps/2); M=e[:,None]*k*h*e[None,:]; n=N//2
    A=M[:n,:n]; B=M[:n,n:]
    le=np.linalg.eigh(A+B)[0][-1]; lo=np.linalg.eigh(A-B)[0][-1]
    return le-lo
D=[run(N) for N in (256,512,1024)]
f=lambda D:-np.log(D)/4
L=["-logD/sqrtb N=256,512,1024: "+", ".join("%.8f"%f(x) for x in D)+"  Delta: "+", ".join("%.8e"%x for x in D)]
for i in (0,1):
    Dr=(4*D[i+1]-D[i])/3; L.append("Richardson(h^2) from pair %d: Delta=%.8e -logD/sqrtb=%.8f"%(i,Dr,f(Dr)))
s="\n".join(L)+"\n"; print(s)
with open('report_extra.md','x') as g: g.write(s)
