"""T49 minimal-box O(2) scan.  Predicates fixed BEFORE first run:
P1 plaquette count with a free link is an integer; each free link lies in 6 plaquettes (expectation, x0 interior).
P2 gauge invariance: S(in=U h^-1, out=h U) == S(U) for random U, random h in O(2) (tol 1e-12, double rounding).
P3 pattern all(+1): min S < 1e-8 ; pattern all(-1): min S < 1e-8.
P4 for EVERY pattern, plaquettes with odd # of det=-1 links give s==1 exactly (tol 1e-12), so minS >= #odd.
P5 number of patterns with min S < 1e-8 equals 2 (expectation: only the two uniform patterns).
Note: scipy absent (env), own BFGS used; stop |g|<1e-7.
P6 for each pattern: minS == #odd within 1e-6 (expectation: even plaquettes can be zeroed). Hypothesis tested per pattern; count reported.
Tolerances: 1e-12 = float64 roundoff on few-term sums; 1e-8 / 1e-6 = BFGS gtol 1e-10 on quadratic-near-minimum S gives S error ~1e-12, margin for slow convergence.
Link = R(theta) diag(1,d). Seed 12345. Results written to results_*.txt mode x."""
import numpy as np, itertools, sys, time
from types import SimpleNamespace
def minimize(f,x,method=None,options=None):
    """own BFGS, central-difference gradient h=1e-6, Armijo backtracking; stop |g|<1e-7 (FD noise ~1e-10) or 300 its"""
    def g(x):
        e=np.eye(len(x))*1e-6
        return np.array([(f(x+e[i])-f(x-e[i]))/2e-6 for i in range(len(x))])
    n=len(x); H=np.eye(n); gx=g(x); fx=f(x)
    for it in range(300):
        if np.linalg.norm(gx)<1e-7: break
        p=-H@gx; t=1.0
        if p@gx>=0: H=np.eye(n); p=-gx
        while t>1e-12:
            fn=f(x+t*p)
            if fn<=fx+1e-4*t*(gx@p): break
            t*=0.5
        xn=x+t*p; gn=g(xn); sv=xn-x; yv=gn-gx
        if sv@yv>1e-12: r=1/(sv@yv); I=np.eye(n); H=(I-r*np.outer(sv,yv))@H@(I-r*np.outer(yv,sv))+r*np.outer(sv,sv)
        x,gx,fx=xn,gn,fn
    return SimpleNamespace(fun=fx,x=x)
rng=np.random.default_rng(12345)
x0=(1,1,1,1)
def add(x,m,s=1):
    y=list(x); y[m]+=s; return tuple(y)
free=[]  # index 0..3 incoming mu, 4..7 outgoing mu
for m in range(4): free.append((add(x0,m,-1),m))
for m in range(4): free.append((x0,m))
fidx={k:i for i,k in enumerate(free)}
plaq=[]
for x in itertools.product((0,1),repeat=4):
    for m in range(4):
        for n in range(m+1,4):
            ls=[(x,m),(add(x,m),n),(add(x,n),m),(x,n)]
            if any(l in fidx for l in ls): plaq.append([fidx.get(l,8) for l in ls])
plaq=np.array(plaq); NP=len(plaq)
def mats(th,d):
    c,s=np.cos(th),np.sin(th)
    M=np.zeros((9,2,2)); M[:8,0,0]=c; M[:8,1,0]=s; M[:8,0,1]=-s*d; M[:8,1,1]=c*d
    M[8]=np.eye(2); return M
def splaq(M):
    A,B,C,D=(M[plaq[:,i]] for i in range(4))
    Cinv=np.swapaxes(C,1,2); Dinv=np.swapaxes(D,1,2)
    U=A@B@Cinv@Dinv
    return 1-0.5*np.trace(U,axis1=1,axis2=2)
def S(th,d): return splaq(mats(th,d)).sum()
def odd_count(d):
    dd=np.append(d,1.0); return int((np.prod(dd[plaq],axis=1)<0).sum())
if __name__=="__main__":
    out=open("results_scan.txt","x"); 
    def w(s): print(s); out.write(s+"\n"); out.flush()
    t0=time.time()
    w(f"P1 plaquettes with free link: {NP}; per-link counts {[int((plaq==i).any(axis=1).sum()) for i in range(8)]}")
    # P2 gauge invariance on random full config (random links on the 8 free)
    mx=0
    for _ in range(20):
        th=rng.uniform(0,2*np.pi,8); d=rng.choice([-1.,1.],8)
        M=mats(th,d)[:8]
        a=rng.uniform(0,2*np.pi); h=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])@np.diag([1,rng.choice([-1,1])])
        M2=M.copy(); M2[:4]=M[:4]@h.T; M2[4:]=h@M[4:]   # h^-1=h^T
        mx=max(mx,abs(splaq(np.concatenate([M,np.eye(2)[None]])).sum()-splaq(np.concatenate([M2,np.eye(2)[None]])).sum()))
    w(f"P2 max |S-S_gauge| over 20 trials = {mx:.2e}  -> {'PASS' if mx<1e-12 else 'FAIL'}")
    nst=int(sys.argv[1]) if len(sys.argv)>1 else 4
    res={}; allmin=[]
    for pat in itertools.product((1.,-1.),repeat=8):
        d=np.array(pat); vals=[]
        # P4 check at random angles
        th=rng.uniform(0,2*np.pi,8); s=splaq(mats(th,d)); odd=(np.prod(np.append(d,1.)[plaq],axis=1)<0)
        assert np.all(abs(s[odd]-1)<1e-12), "P4 FAIL"
        for k in range(nst):
            r=minimize(lambda t:S(t,d),rng.uniform(0,2*np.pi,8),method="BFGS",options={"gtol":1e-10})
            vals.append(r.fun)
        res[pat]=(min(vals),sorted(set(np.round(vals,4))),odd_count(d))
    w(f"P4 PASS (odd plaquettes have s=1 exactly) for all 256 patterns; time {time.time()-t0:.1f}s")
    zero=[p for p,v in res.items() if v[0]<1e-8]
    w(f"P3 all+ min={res[(1.,)*8][0]:.2e}, all- min={res[(-1.,)*8][0]:.2e}")
    w(f"P5 patterns with min<1e-8: {len(zero)} -> {'PASS' if len(zero)==2 else 'FAIL'} ; {zero}")
    q=sum(1 for p,v in res.items() if abs(v[0]-v[2])<1e-6)
    w(f"P6 patterns with minS == #odd within 1e-6: {q}/256")
    w("TABLE pattern(d: in mu0..3 | out mu0..3) minS #odd localvalues")
    for p,v in res.items(): w(f"{''.join('+' if x>0 else '-' for x in p[:4])}|{''.join('+' if x>0 else '-' for x in p[4:])} {v[0]:.6f} {v[2]} {v[1]}")
    nz=sorted(set(round(v[0],4) for v in res.values() if v[0]>1e-8))
    w(f"distinct nonzero pattern minima (rounded 1e-4): {nz[:10]} ...; smallest {nz[0]}")
    locs=sorted(set(x for v in res.values() for x in v[1]))
    w(f"all distinct local values found (rounded 1e-4), n={len(locs)}: {locs[:15]}")
    # local minima within the all-plus pattern
    d=np.ones(8); lv=sorted(set(round(minimize(lambda t:S(t,d),rng.uniform(0,2*np.pi,8),method="BFGS",options={"gtol":1e-10}).fun,4) for _ in range(200)))
    w(f"all+ pattern, 200 starts, distinct end values: {lv}")
    w(f"time {time.time()-t0:.1f}s")
