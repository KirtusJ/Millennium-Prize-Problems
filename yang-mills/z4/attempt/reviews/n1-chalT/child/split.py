"""T136 splitting m = log(lam_e/lam_o) for the circle walk with eps=2 asinh|sin a|.
Reduction: sectors even under a->-a and even/odd under flip a->pi-a live on [0,pi/2],
midpoint grid a_i=(i+1/2)h, S=h w_i w_j [K(ai-aj)+K(ai+aj)], B=h w_i w_j [K(ai+aj-pi)+K(ai-aj-pi)],
A_e=S+B, A_o=S-B. Exact identity: lam_e-lam_o = 2<g_o,B g_e>/<g_o,g_e>, m=log1p(that/lam_o).
Eigenvectors by repeated squaring of the (PSD) matrix, rescaled each time (no eigenvalue difference).
PREDICATES (fixed before first run):
 P1 grid convergence: for each beta, |(-log m/sqrtb)(h) - (-log m/sqrtb)(h/2)| < 1e-3
    (source: the claim is quoted to 1e-3 relative scale; midpoint quadrature has O(h^2) error from the |a| kink of eps).
 P2 squaring convergence: log m with 60 vs 75 squarings agree to 1e-9 absolute (double rounding level 1e-13 expected).
 P3 beta=64 route check: identity-m vs decimal grandchild log m agree to 1e-6 absolute (mine: generous vs 1e-10 expected). Evaluated in report, not here.
 P4 claim: |c_fit - c*| < 0.03*c* using fit -log m = c sqrtb + b log b + c0 on 4 betas (my own choice; fit has 1 dof).
 P5 monotone: -log m/sqrtb increasing in beta (measured only).
"""
import numpy as np, json, sys, math
CSTAR=4.6054132
def K(x,beta):
    x=(x+np.pi)%(2*np.pi)-np.pi
    return math.sqrt(beta/(2*np.pi))*sum(np.exp(-beta*(x+2*np.pi*n)**2/2) for n in (-1,0,1))
def top(A,nsq):
    M=A/np.abs(A).max()
    for _ in range(nsq):
        M=M@M; M/=np.abs(M).max()
    j=np.argmax(np.diag(M)); v=M[:,j].copy(); v/=np.abs(v).max()
    lam=(v@(A@v))/(v@v); return lam,v
def logm(beta,n,nsq=60):
    h=(np.pi/2)/n; a=(np.arange(n)+.5)*h
    w=np.exp(-np.arcsinh(np.sin(a)))  # exp(-eps/2)
    ai=a[:,None]; aj=a[None,:]
    S=h*w[:,None]*w[None,:]*(K(ai-aj,beta)+K(ai+aj,beta))
    B=h*w[:,None]*w[None,:]*(K(ai+aj-np.pi,beta)+K(ai-aj-np.pi,beta))
    le,ge=top(S+B,nsq); lo,go=top(S-B,nsq)
    d=2*(go@B@ge)/(go@ge)
    return math.log(math.log1p(d/lo)), le, lo, d
if __name__=="__main__":
    out=open("split_results.json","x"); res={}
    for beta in (64,256,1024,4096):
        n1=math.ceil((np.pi/2)*5*math.sqrt(beta)); r={}
        for tag,n,ns in (("h",n1,60),("h/2",2*n1,60),("h_75sq",n1,75)):
            lm,le,lo,d=logm(beta,n,ns); r[tag]=dict(n=n,logm=lm,lam_e=le,lam_o=lo,delta=d,ratio=-lm/math.sqrt(beta))
            print(beta,tag,n,lm,-lm/math.sqrt(beta),flush=True)
        res[beta]=r
    json.dump(res,out,indent=1)
