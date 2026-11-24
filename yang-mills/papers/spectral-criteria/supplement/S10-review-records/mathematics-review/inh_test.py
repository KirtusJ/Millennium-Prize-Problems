"""Numerical test of Theorem t:inh (main.tex, fourth draft, sha256 aaec6bca...).
PREDICATES (fixed before the first run):
 P1 For every qualifying instance (hypothesis check: lambda_min(I-A^2-gamma G) >= -1e-10 with gamma>1e-9,
    0<=A<=I, P,B,G mutually orthogonal projections, P+B+G=I), slack = (1-||A^m||) - (b-kappa)_+/(1+2/(m gamma)) >= -1e-9,
    with gamma the LARGEST admissible (bisection), kappa=||B A^j B||, b=1-||P A^m P|| (tightest data).
 P2 Same on the forced families: A with a kernel; ||A||=1; both; A=0; m=j=1.
 P3 Random-restart local search (coordinate perturbation) for the minimum slack in dims 2..4, m=j=1 and m=2,j=1: min >= -1e-9.
 P4 Lemma l:scal on a grid x in [0,1], rho in {0, 2/m}: x(1-x^rho) <= rho(1-x) + 1e-15.
Tolerances: double-precision eigen-solvers on matrices of norm <=1 (error ~1e-14); 1e-9 leaves a margin.
Seed 20261124. Arguments: none. Output: results_inh.txt (refuses to overwrite)."""
import numpy as np, os, sys
OUT='results_inh.txt'
if os.path.exists(OUT): sys.exit('refuse to overwrite '+OUT)
rng=np.random.default_rng(20261124)
def orth(n): 
    q,_=np.linalg.qr(rng.normal(size=(n,n))); return q
def maxgamma(A,G):
    X=np.eye(len(A))-A@A
    f=lambda g: np.linalg.eigvalsh(X-g*G)[0]
    if np.linalg.norm(G)<1e-12: return 1.0   # G=0: any gamma; use 1 (and also try large)
    if f(1e-9)< -1e-12: return 0.0
    lo,hi=0.0,1.0
    if f(1.0)>=-1e-13: return 1.0
    for _ in range(60):
        mid=(lo+hi)/2
        if f(mid)>=-1e-13: lo=mid
        else: hi=mid
    return lo
def slack(lam,O,V,p,r,m,j):
    n=len(lam); A=(O*lam)@O.T; A=(A+A.T)/2
    P=V[:,:p]@V[:,:p].T; B=V[:,p:p+r]@V[:,p:p+r].T; G=np.eye(n)-P-B
    g=maxgamma(A,G)
    if g<=1e-9: return None
    if np.linalg.eigvalsh(np.eye(n)-A@A-g*G)[0] < -1e-10: return None
    Am=np.linalg.matrix_power(A,m); Aj=np.linalg.matrix_power(A,j)
    kap=np.linalg.norm(B@Aj@B,2); b=1-np.linalg.norm(P@Am@P,2)
    return (1-np.linalg.norm(Am,2)) - max(b-kap,0)/(1+2/(m*g)), g,kap,b
res=[]; log=[]
def family(name,gen,N):
    tot=0;qual=0;mn=np.inf;arg=None;pos=0
    for _ in range(N):
        lam,O,V,p,r,m,j=gen(); tot+=1
        s=slack(lam,O,V,p,r,m,j)
        if s is None: continue
        qual+=1
        if s[3]-s[2]>1e-6: pos+=1
        if s[0]<mn: mn=s[0];arg=(m,j,len(lam),p,r)+tuple(round(float(z),6) for z in s[1:])
    log.append(f'{name}: instances {tot}, qualifying {qual}, with b>kappa {pos}, min slack {mn:.3e}, at (m,j,n,p,r,gamma,kappa,b)={arg}')
    return mn
def gen_generic(mj=None,kernel=False,top=False,zero=False,alignG=False):
    def g():
        n=int(rng.integers(2,8)); p=int(rng.integers(0,n+1)); r=int(rng.integers(0,n-p+1))
        if mj: m,j=mj
        else:
            m=int(rng.integers(1,9)); j=int(rng.integers(1,m+1))
        lam=rng.uniform(0,1,n)**rng.choice([0.2,1,3])
        if kernel: lam[:int(rng.integers(1,n))]=0
        if top: lam[-1]=1.0
        if zero: lam[:]=0
        O=orth(n); V=orth(n)
        if alignG and top:
            # make the eigenvector of eigenvalue 1 lie in ran(P+B) so that gamma>0 is possible
            v=O[:,-1]; k=p+r
            if k==0: p=1;k=1
            W=orth(n); c=rng.normal(size=k); 
            M=np.column_stack([v]+[W[:,i] for i in range(n-1)]); Q,_=np.linalg.qr(M)
            # first k columns span contains v; rotate inside the first k columns so v is spread over P and B
            Rk=orth(k); V=Q.copy(); V[:,:k]=Q[:,:k]@Rk
        return lam,O,V,p,r,m,j
    return g
mins=[]
mins.append(family('generic',gen_generic(),40000))
mins.append(family('m=j=1',gen_generic(mj=(1,1)),40000))
mins.append(family('kernel',gen_generic(kernel=True),40000))
mins.append(family('kernel,m=j=1',gen_generic(mj=(1,1),kernel=True),40000))
mins.append(family('||A||=1 generic position (expected: few qualify)',gen_generic(top=True),20000))
mins.append(family('||A||=1 aligned',gen_generic(top=True,alignG=True),40000))
mins.append(family('||A||=1 aligned,kernel,m=j=1',gen_generic(mj=(1,1),kernel=True,top=True,alignG=True),40000))
mins.append(family('A=0',gen_generic(zero=True),5000))
# P3 local search
def search(m,j,restarts=300,steps=400):
    best=np.inf;barg=None
    for _ in range(restarts):
        n=int(rng.integers(2,5)); p=int(rng.integers(1,n)); r=int(rng.integers(0,n-p+1))
        lam=rng.uniform(0,1,n); SO=rng.normal(size=(n,n)); SV=rng.normal(size=(n,n))
        def ev(lam,SO,SV):
            O,_=np.linalg.qr(SO); V,_=np.linalg.qr(SV); s=slack(np.clip(lam,0,1),O,V,p,r,m,j)
            return (np.inf,) if s is None else s
        cur=ev(lam,SO,SV); sc=0.3
        for _ in range(steps):
            l2=lam+sc*rng.normal(size=n)*rng.integers(0,2,n); O2=SO+sc*rng.normal(size=(n,n)); V2=SV+sc*rng.normal(size=(n,n))
            c=ev(l2,O2,V2)
            if c[0]<cur[0]: lam,SO,SV,cur=l2,O2,V2,c
            else: sc=max(sc*0.98,1e-4)
        if cur[0]<best: best=cur[0];barg=(n,p,r)+tuple(round(float(z),6) for z in cur[1:])
    log.append(f'search m={m},j={j}: min slack {best:.3e} at (n,p,r,gamma,kappa,b)={barg}')
    return best
mins.append(search(1,1)); mins.append(search(2,1)); mins.append(search(4,2,restarts=100))
# P4
xs=np.linspace(0,1,100001); bad=0
for m in range(1,65):
    rho=2/m
    if np.any(xs*(1-xs**rho) > rho*(1-xs)+1e-15): bad+=1
if np.any(xs*(1-xs**0.0)>1e-15): bad+=1
log.append(f'P4 lemma l:scal grid violations: {bad}')
log.append('P1-P3 '+('PASS' if min(mins)>=-1e-9 else 'FAIL')+f' (global min slack {min(mins):.3e}); P4 '+('PASS' if bad==0 else 'FAIL'))
open(OUT,'x').write('\n'.join(log)+'\n'); print('\n'.join(log))
