"""Numerical pre-test of the Lean statements (seed 20261124).
Predicates (fixed before first run):
 N1 (L1a): for x in [0,1], r in [0,20]: x*(1-x**r) <= r*(1-x) + 1e-12.   (tol: float64 rounding, values O(1..20))
 N2 (L1b): if b <= 1-x + x(1-x^r)/g + k, g>0, r>=0, x in [0,1] then 1-x >= (b-k)/(1+r/g) - 1e-12.
     Cases: b drawn as RHS minus random slack (so hypothesis holds); count qualifying cases.
 N3 (L2): sequences with K_i>0 (also K_i in (0,1)), d_i >= (b_i-k_i)/K_i, b_i >= d_{i-1}-e_i:
     M_n d_n >= d_0 - sum_{i=1}^n M_{i-1}(e_i+k_i) - 1e-9 ; positive-part form needs d_n>=0.
     Also report whether the M_i-indexed variant fails (expected: fails at equality).
 N4 (L3): random finite-dim instances: orthonormal eigenbasis, lam>=0, P = coordinate-type projection,
     B projection with B P = 0 (B inside range Q), G=Q-B. gamma := largest admissible (min of form ratio),
     kappa := ||B S_tau B||, 1-b := ||P S_t P||. Check 1-||S_t|| >= (b-kappa)/(1+2a/(gamma t)) - 1e-9,
     and the three scalar consequences at v = lowest eigenvector.
"""
import numpy as np
rng=np.random.default_rng(20261124)
out=open("results_numtest.txt","x")
def log(s): print(s); out.write(s+"\n")
# N1
x=rng.uniform(0,1,200000); r=rng.uniform(0,20,200000)
x[:10]=0; x[10:20]=1; r[20:30]=0
v=x*(1-x**r)-r*(1-x); log(f"N1 cases {len(x)} max(lhs-rhs)={v.max():.3e} fail={(v>1e-12).sum()}")
# N2
g=rng.uniform(0.01,5,200000); k=rng.uniform(0,1,200000)
b=1-x+x*(1-x**r)/g+k-rng.exponential(0.1,200000)
qual=(b<=1-x+x*(1-x**r)/g+k).sum()
v=(b-k)/(1+r/g)-(1-x); log(f"N2 qualifying {qual}/{len(x)} max viol={v.max():.3e} fail={(v>1e-12).sum()}")
# N3
fails=0; failsMi=0; minsl=1e9; cases=0
for trial in range(20000):
    n=rng.integers(1,8); K=rng.uniform(0.3,4,n); e=rng.uniform(0,0.1,n); kp=rng.uniform(0,0.1,n)
    eq = trial%2==0
    d=[rng.uniform(0,1)]
    for i in range(n):
        bi=d[-1]-e[i]+(0 if eq else rng.exponential(0.05))
        di=max(bi-kp[i],0)/K[i]+(0 if eq else rng.exponential(0.05))
        d.append(di)
    M=np.concatenate([[1],np.cumprod(K)])
    rhs=d[0]-sum(M[i]*(e[i]+kp[i]) for i in range(n))  # M[i] = M_{(i+1)-1}
    rhsMi=d[0]-sum(M[i+1]*(e[i]+kp[i]) for i in range(n))
    cases+=1; sl=M[n]*d[n]-max(rhs,0); minsl=min(minsl,sl)
    if sl< -1e-9: fails+=1
    if M[n]*d[n]-max(rhsMi,0) < -1e-9: failsMi+=1
log(f"N3 cases {cases} fail(M_{{i-1}})={fails} minslack={minsl:.3e}; variant M_i fails={failsMi} (K_i in (0.3,4))")
# N4
fails=0; qual=0; minsl=1e9
for trial in range(3000):
    n=rng.integers(2,7)
    U,_=np.linalg.qr(rng.normal(size=(n,n)))
    lam=rng.exponential(1,n); lam[rng.integers(n)]*=rng.uniform(0,1)
    S=lambda s: U@np.diag(np.exp(-s*lam))@U.T
    k=rng.integers(1,n); Pb,_=np.linalg.qr(rng.normal(size=(n,k))); P=Pb@Pb.T; Q=np.eye(n)-P
    Qb=np.linalg.svd(Q)[0][:,:n-k]; m=rng.integers(0,n-k+1); C,_=np.linalg.qr(rng.normal(size=(n-k,n-k)))
    Bb=Qb@C[:,:m]; B=Bb@Bb.T; G=Q-B
    a=rng.uniform(0.05,3); t=rng.uniform(0.1,3); tau=rng.uniform(0,t)
    D=np.eye(n)-S(2*a)
    # largest gamma with D >= gamma G : generalized eig on range of G
    if m==n-k: continue
    Gb=Qb@C[:,m:]; Dr=Gb.T@np.linalg.inv(np.linalg.pinv(D) if False else np.linalg.inv(D))@Gb if False else None
    # gamma_max = 1/ lambda_max( Gb^T D^{-1} Gb )
    if np.min(np.linalg.eigvalsh(D))<1e-9: continue
    gam=1/np.max(np.linalg.eigvalsh(Gb.T@np.linalg.inv(D)@Gb))*rng.uniform(0.5,1)
    kap=np.linalg.norm(B@S(tau)@B,2); bb=1-np.linalg.norm(P@S(t)@P,2)
    qual+=1
    dd=1-np.linalg.norm(S(t),2)
    sl=dd-max(bb-kap,0)/(1+2*a/(gam*t)); minsl=min(minsl,sl)
    i0=np.argmin(lam); v=U[:,i0]; x=np.exp(-t*lam[i0])
    c1=gam*np.linalg.norm(G@v)**2 <= 1-np.exp(-2*a*lam[i0])+1e-9
    c2=np.linalg.norm(B@v)**2*np.exp(-tau*lam[i0]) <= kap+1e-9
    c3=1-bb >= x*(1-np.linalg.norm(Q@v)**2)-1e-9
    if sl<-1e-9 or not(c1 and c2 and c3): fails+=1
log(f"N4 qualifying {qual} fail={fails} minslack={minsl:.3e}")
