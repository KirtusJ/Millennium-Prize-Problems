"""Referee checks (predicates fixed before first run).
P1 budget: exact Fractions, i=1..60: d_i == (b_i-kappa_i)/K_i ; sum_{i<=n} M_{i-1}kappa_i == d0(1-2^-n); M_n<=e; d_n decreasing to 0.
P2 p_k(theta): values at beta=3.399810242 round to 0.00307,0.156,0.935; envelope >= p_k on grid; p_k nondecreasing in k.
P3 R'(6) in (0.036885895,0.036885896); p<q, p'<0, w'>0 on grid k in (0,60]; R'(6)/beta^2 values.
P4 t:inh random finite-dim: d >= (b-kappa)_+/(1+2a/(gamma t)) - 1e-10 (roundoff of eigensolver ~1e-13), hypothesis per instance: gamma>0.
P5 toy Z3 gauge theory 1+1 dim, 2 spatial sites, T=3: brute-force E[f(x0)g(x1)] == trace formula with gauge-averaged kernel K;
   K has zero eigenvalues (not injective); temporal-gauge L0 strictly positive but trace formula with L0 fails for periodic measure.
P6 cap lemma: tilted probability of cap centred at angle phi from v <= that centred at v (2D quadrature over polar angles).
"""
import numpy as np, itertools, math
from fractions import Fraction as F
print("== P1")
d0=F(1,2); M=[F(1)]; d=[d0]; s=F(0); ok=True; sk=F(0)
for i in range(1,61):
    K=1+F(1,2**i); M.append(M[-1]*K); b=d[i-1]; kap=d[i-1]/2
    di=d0/(2**i*M[i]); ok&=(di==(b-kap)/K); d.append(di); s+=M[i-1]*kap; sk+=kap
    ok&=(s==d0*(1-F(1,2**i)))
print("equality all steps & partial sums = d0(1-2^-n):",ok,"M_60=",float(M[60]),"sum kappa=",float(sk),"d_60=",float(d[60]))
print("== P2")
def pk(k,th,n=200001):
    r=np.linspace(0,np.pi,n); w=np.sin(r)**2*np.exp(k*(np.cos(r)-1))
    c=np.concatenate([[0],np.cumsum((w[1:]+w[:-1])/2)*(r[1]-r[0])]); return np.interp(th,r,c)/c[-1]
beta=3.399810242
print([float(pk(6*beta,t)) for t in (0.05,0.2,0.6)])
bad=0;tot=0
for k in [0,0.1,1,5,20.4,100,1000]:
    for th in np.linspace(0,np.pi,60):
        tot+=1; env=min(1,np.pi**2*math.sqrt(math.e)/4*(1+k)**1.5*th**3)
        if pk(k,th)>env+1e-9: bad+=1
print("envelope violations",bad,"of",tot)
ks=[0,0.5,1,2,5,10,20,50]; mon=all(pk(ks[i],th)<=pk(ks[i+1],th)+1e-9 for i in range(len(ks)-1) for th in np.linspace(0.05,3.1,30))
print("monotone in k:",mon)
print("== P3")
def I(nu,k,terms=80):
    return sum(F(1,math.factorial(m)*math.factorial(m+nu))*(F(k)/2)**(2*m+nu) for m in range(terms))
R6=I(2,6)/I(1,6); p6=1-3*R6/6-R6*R6; print("R'(6)=%.12f"%float(p6))
def If(nu,k): 
    t=(k/2)**nu/math.factorial(nu); s=t; m=0
    while t>1e-18*s: m+=1; t*=(k/2)**2/(m*(m+nu)); s+=t
    return s
Rf=lambda k: If(2,k)/If(1,k); pf=lambda k:1-3*Rf(k)/k-Rf(k)**2
v=[0,0,0];n=0
for k in np.linspace(0.05,60,4000):
    R=Rf(k);p=pf(k);q=R/k;pp=-(2*R+3/k)*p+3*R/k**2;w=k*k*p;wp=3*R-(2*R+1/k)*w;n+=1
    v[0]+=not p<q; v[1]+=not pp<0; v[2]+=not wp>0
print("violations p<q,p'<0,w'>0:",v,"of",n)
for b in (3.276133577,3.399810242): print(b, float(p6)/b**2)
print("== P4")
rng=np.random.default_rng(1); viol=0; qual=0; tight=1e9
for trial in range(4000):
    n=int(rng.integers(3,9)); A=rng.normal(size=(n,n)); ev=rng.exponential(1.0,size=n)*rng.choice([0.01,1,5])
    if trial%3==0: ev[0]=40.0  # near-noninjective S
    Qm,_=np.linalg.qr(A); 
    S=lambda s:(Qm*np.exp(-s*ev))@Qm.T
    r=int(rng.integers(1,n)); X,_=np.linalg.qr(rng.normal(size=(n,n))); P=X[:,:r]@X[:,:r].T
    rb=int(rng.integers(0,n-r+1)); Bm=X[:,r:r+rb]@X[:,r:r+rb].T; G=np.eye(n)-P-Bm
    a=rng.uniform(0.05,1); t=rng.uniform(2*a,6); tau=rng.uniform(0.01,t)
    Mx=np.eye(n)-S(2*a); Gb=X[:,r+rb:]
    if Gb.shape[1]==0: gamma=1e6
    else:
        gamma=1/np.linalg.eigvalsh(Gb.T@np.linalg.inv(Mx)@Gb).max()  # largest gamma with Mx>=gamma G
    if not gamma>0: continue
    gamma*=rng.uniform(0.3,1); qual+=1
    kap=np.linalg.norm(Bm@S(tau)@Bm,2); b=1-np.linalg.norm(P@S(t)@P,2)
    dd=1-np.exp(-t*ev.min()); rhs=max(b-kap,0)/(1+2*a/(gamma*t))
    if dd<rhs-1e-10: viol+=1
    tight=min(tight,dd-rhs)
print("qualifying",qual,"violations",viol,"min slack",tight)
print("== P5")
n=3; beta_=0.7; w=lambda u: math.exp(beta_*math.cos(2*math.pi*(u%n)/n))
states=list(itertools.product(range(n),repeat=2)); idx={s:i for i,s in enumerate(states)}
def kfix(x,g,xp): # links l=0: site0->site1, l=1: site1->site0
    return w(x[0]+g[1]-xp[0]-g[0])*w(x[1]+g[0]-xp[1]-g[1])
K=np.array([[sum(kfix(x,g,xp) for g in states) for xp in states] for x in states])
L0=np.array([[kfix(x,(0,0),xp) for xp in states] for x in states])
rng=np.random.default_rng(2); f=rng.normal(size=9); g=rng.normal(size=9); T=3
num=0;den=0
for xs in itertools.product(states,repeat=T):
    for gs in itertools.product(states,repeat=T):
        wt=1
        for s in range(T): wt*=kfix(xs[s],gs[s],xs[(s+1)%T])
        den+=wt; num+=wt*f[idx[xs[0]]]*g[idx[xs[1]]]
bf=num/den
tr=lambda L: np.trace(np.diag(f)@L@np.diag(g)@L@L)/np.trace(L@L@L)
print("brute",bf,"trace with K",tr(K),"trace with L0",tr(L0))
print("eig K",np.round(np.linalg.eigvalsh(K),10)); print("eig L0 min",np.linalg.eigvalsh(L0).min())
print("== P6")
def capprob(k,phi,th,n=400):
    # S^3: u=(cos r, sin r cos s, ...) ; centre c=(cos phi, sin phi,0,0); measure sin^2 r sin s dr ds
    r=(np.arange(n)+.5)*np.pi/n; s=(np.arange(n)+.5)*np.pi/n; Rr,Ss=np.meshgrid(r,s,indexing='ij')
    dens=np.sin(Rr)**2*np.sin(Ss)*np.exp(k*(np.cos(Rr)-1)); dot=np.cos(Rr)*np.cos(phi)+np.sin(Rr)*np.cos(Ss)*np.sin(phi)
    return (dens*(dot>=np.cos(th))).sum()/dens.sum()
bad=0;tot=0
for k in (0.5,3,20):
    for th in (0.2,0.8,1.6,2.5):
        p0=capprob(k,0,th)
        for phi in (0.3,1,2,3.1):
            tot+=1; bad+=capprob(k,phi,th)>p0+2e-3   # tolerance: midpoint grid 400x400, indicator edge error ~1/n
print("cap violations",bad,"of",tot)
