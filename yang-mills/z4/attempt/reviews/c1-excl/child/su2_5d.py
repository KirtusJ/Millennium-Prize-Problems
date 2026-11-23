"""SU(2) Wilson LGT, 5D, L=4 periodic. Checkerboard Metropolis (4 hits/sweep, eps=0.3), quaternion links.
PREDICATES (fixed before first run; tolerances are my own judgement, not derived):
 P1 (for all 12 runs) 0 < P <= 1 and finite. Hypothesis test: count runs qualifying.
 P2 gap<0.02 at beta=1.3 and at beta=2.2  (0.02 ~ several x expected stat error of ~0.003 from last-half blocks; my guess)
 P3 gap>0.03 AND gap>5*combined error at beta=1.6 or 1.7 (hysteresis seen)
 P4 max gap(1.6,1.7) > max gap(1.3,2.2)
 Everything else (the P values themselves) is MEASURED ONLY. Sweeps limited (NSW=200): short runs, Metropolis only.
Seeds fixed: seed = 1000+index. Results file opened mode 'x'."""
import numpy as np, json, sys, time
L=4; ND=5; NSW=200; EPS=0.3; HITS=4
def qm(a,b):
    a0,av=a[...,:1],a[...,1:]; b0,bv=b[...,:1],b[...,1:]
    return np.concatenate([a0*b0-(av*bv).sum(-1,keepdims=True), a0*bv+b0*av+np.cross(av,bv)],-1)
def cj(a): return a*np.array([1,-1,-1,-1.])
def nrm(a): return a/np.linalg.norm(a,axis=-1,keepdims=True)
def sh(U,mu,s): return np.roll(U,-s,axis=mu)   # U(x+s*mu)
def staple(U,mu):
    C=0
    for nu in range(ND):
        if nu==mu: continue
        C=C+qm(qm(sh(U[nu],mu,1),cj(sh(U[mu],nu,1))),cj(U[nu]))
        C=C+qm(qm(cj(sh(sh(U[nu],mu,1),nu,-1)),cj(sh(U[mu],nu,-1))),sh(U[nu],nu,-1))
    return C
def plaq(U):
    t=0;n=0
    for mu in range(ND):
        for nu in range(mu+1,ND):
            q=qm(qm(U[mu],sh(U[nu],mu,1)),qm(cj(sh(U[mu],nu,1)),cj(U[nu])))
            t+=q[...,0].mean();n+=1
    return t/n
idx=np.indices((L,)*ND).sum(0)
def sweep(U,beta,rng):
    for mu in range(ND):
        for par in (0,1):
            m=(idx%2==par)[...,None]
            C=staple(U,mu)
            for _ in range(HITS):
                R=nrm(np.array([1,0,0,0.])+EPS*rng.standard_normal(U[mu].shape))
                Un=nrm(qm(R,U[mu]))
                dS=-beta*(qm(Un,C)[...,0]-qm(U[mu],C)[...,0])
                acc=(rng.random(dS.shape)<np.exp(-dS))[...,None]&m
                U[mu]=np.where(acc,Un,U[mu])
def run(beta,hot,seed):
    rng=np.random.default_rng(seed)
    U=np.zeros((ND,)+(L,)*ND+(4,)); U[...,0]=1
    if hot: U=nrm(rng.standard_normal(U.shape))
    ps=[]
    for s in range(NSW):
        sweep(U,beta,rng); ps.append(plaq(U))
    return ps
if __name__=="__main__":
    betas=[1.3,1.5,1.6,1.7,1.9,2.2]; res={}; t0=time.time()
    for i,b in enumerate(betas):
        for j,hot in enumerate((0,1)):
            ps=np.array(run(b,hot,1000+2*i+j)); h=ps[NSW//2:]
            bl=h.reshape(10,-1).mean(1)
            res[f"{b}_{'hot' if hot else 'cold'}"]=dict(mean=float(h.mean()),err=float(bl.std(ddof=1)/np.sqrt(10)),std=float(h.std()),first=float(ps[0]),last=float(ps[-1]),traj=[float(x) for x in ps[::20]])
            print(b,'hot' if hot else 'cold',"P=%.4f +- %.4f"%(h.mean(),bl.std(ddof=1)/np.sqrt(10)),"t=%.0fs"%(time.time()-t0),flush=True)
    gaps={}
    for b in betas:
        c,h=res[f"{b}_cold"],res[f"{b}_hot"]
        gaps[b]=(abs(c['mean']-h['mean']),float(np.hypot(c['err'],h['err'])))
        print("beta",b,"gap %.4f err %.4f"%gaps[b])
    ok1=all(0<v['mean']<=1 and np.isfinite(v['mean']) for v in res.values())
    p2=gaps[1.3][0]<0.02 and gaps[2.2][0]<0.02
    p3=any(gaps[b][0]>0.03 and gaps[b][0]>5*gaps[b][1] for b in (1.6,1.7))
    p4=max(gaps[1.6][0],gaps[1.7][0])>max(gaps[1.3][0],gaps[2.2][0])
    print("P1",ok1,"(12/12 qualify)" if ok1 else "","P2",p2,"P3",p3,"P4",p4)
    with open("results.json","x") as f: json.dump(dict(res=res,gaps={str(k):v for k,v in gaps.items()},P1=ok1,P2=p2,P3=p3,P4=p4),f)
    sys.exit(0 if (ok1 and p2 and p3 and p4) else 1)
