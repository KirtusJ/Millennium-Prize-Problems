"""c1 for compact U(1) SF, d=4, T=R=2. numpy only.
Predicates fixed before running (PASS if all true):
 P1 ||H-H^T||_max < 1e-12
 P2 exact H matches finite-difference Hessian of S (max abs diff < 1e-5)
 P3 A=H+DD^T positive definite (all eigenvalues > 1e-9)
 P4 D has full column rank (9) 
 P5 Richardson c1 (h=1e-4,2e-4) vs each raw differ < 1e-6
 P6 |c1 - c1_alt| < 1e-6 ("agree")
 ||H D|| is reported only, not asserted.
Rerun: cd grandchild && OMP_NUM_THREADS=1 python3 c1.py
Results written to results_<tag>.txt (mode 'x', never overwritten).
"""
import numpy as np, itertools, sys, time
T=2; R=2; eta0=np.pi/4
sites=[(x0,)+s for x0 in range(T+1) for s in itertools.product(range(R),repeat=3)]
def shift(x,mu):
    y=list(x); y[mu]+=1
    if mu>0: y[mu]%=R
    return tuple(y)
def isdyn(x,mu): return (mu==0 and x[0]<T) or (mu>0 and 1<=x[0]<=T-1)
dyn=[(x,mu) for x in sites for mu in range(4) if isdyn(x,mu)]
idx={l:i for i,l in enumerate(dyn)}; N=len(dyn)
def phi_t(x0,eta):
    p=-eta; pp=-(np.pi-eta); return (p+(pp-p)*x0/T)/R
def bg(l,eta):
    x,mu=l
    return 0.0 if mu==0 else phi_t(x[0],eta)
def plaqs():
    out=[]
    for x in sites:
        for mu in range(4):
            for nu in range(mu+1,4):
                if mu==0 and x[0]>=T: continue
                ls=[(x,mu),(shift(x,mu),nu),(shift(x,nu),mu),(x,nu)]
                sg=[1,1,-1,-1]
                if any(isdyn(*l) for l in ls): out.append((mu,ls,sg))
    return out
P=plaqs()
def coeffs(ls,sg):
    a=np.zeros(N)
    for l,s in zip(ls,sg):
        if l in idx: a[idx[l]]+=s
    return a
Aco=[coeffs(ls,sg) for mu,ls,sg in P]
def theta0(ls,sg,eta): return sum(s*bg(l,eta) for l,s in zip(ls,sg))
def S(xv,eta):
    return sum(1-np.cos(theta0(ls,sg,eta)+a@xv) for (mu,ls,sg),a in zip(P,Aco))
def S0(eta): return S(np.zeros(N),eta)
def Hess(eta):
    H=np.zeros((N,N))
    for (mu,ls,sg),a in zip(P,Aco):
        H+=np.cos(theta0(ls,sg,eta))*np.outer(a,a)
    return H
# gauge map: w index: x0=1 sites 0..7 ; t index 8 ; x0=0 w=0
s1=[s for s in sites if s[0]==1]; wi={s:i for i,s in enumerate(s1)}
def wcol(x):
    if x[0]==0: return None
    if x[0]==T: return 8
    return wi[x]
D=np.zeros((N,9))
for (x,mu),i in idx.items():
    c=wcol(x); d=wcol(shift(x,mu))
    if c is not None: D[i,c]+=1
    if d is not None: D[i,d]-=1
def Gamma(eta):
    H=Hess(eta); A=H+D@D.T
    s,ld=np.linalg.slogdet(A); s2,ld2=np.linalg.slogdet(D.T@D)
    return 0.5*ld-ld2
res=[]
def rep(*a):
    s=' '.join(str(x) for x in a); print(s); res.append(s)
H=Hess(eta0); A=H+D@D.T
rep("N dyn links",N,"plaquettes",len(P),"rank D",np.linalg.matrix_rank(D))
p1=np.abs(H-H.T).max()<1e-12
rng=np.random.default_rng(1); e=1e-4
Hfd=np.zeros((N,N)); 
def Sx(v): return S(v,eta0)
for i in range(N):
    for j in range(i,N):
        ei=np.zeros(N); ej=np.zeros(N); ei[i]=e; ej[j]=e
        v=(Sx(ei+ej)-Sx(ei-ej)-Sx(-ei+ej)+Sx(-ei-ej))/(4*e*e)
        Hfd[i,j]=Hfd[j,i]=v
d2=np.abs(Hfd-H).max(); p2=d2<1e-5
ev=np.linalg.eigvalsh(A); p3=ev.min()>1e-9
p4=np.linalg.matrix_rank(D)==9
rep("||H D||_F =",np.linalg.norm(H@D),"max|H-H^T|=",np.abs(H-H.T).max(),"FD hess diff",d2,"min eig A",ev.min())
def c1(h):
    dG=(Gamma(eta0+h)-Gamma(eta0-h))/(2*h)
    k=(S0(eta0+h)-S0(eta0-h))/(2*h)
    return -dG/k,dG,k
c_a,dGa,ka=c1(1e-4); c_b,dGb,kb=c1(2e-4)
c1R=(4*c_a-c_b)/3
kan=48*np.sin(-np.pi/8)*0.5  # analytic dS0/deta
rep("h=1e-4 c1=%.9f dGamma=%.9f k=%.9f"%(c_a,dGa,ka))
rep("h=2e-4 c1=%.9f dGamma=%.9f k=%.9f"%(c_b,dGb,kb))
rep("k analytic (48*sin(delta)/2, delta=-pi/8) = %.9f"%kan)
rep("c1 Richardson = %.7f"%c1R)
p5=max(abs(c1R-c_a),abs(c1R-c_b))<1e-6
Ht=np.zeros((N,N)); Nt=0
for (mu,ls,sg),a in zip(P,Aco):
    if mu==0: Ht+=np.outer(a,a); Nt+=1
Nt_f=3*R**3*T
c_alt=np.trace(np.linalg.solve(A,Ht))/(2*Nt_f)
rep("timelike plaquettes",Nt,"N_t formula",Nt_f)
rep("c1_alt = %.7f"%c_alt)
p6=abs(c1R-c_alt)<1e-6
for n,p in zip(["P1 sym","P2 FDhess","P3 A posdef","P4 rank D","P5 Richardson","P6 c1==c1_alt"],[p1,p2,p3,p4,p5,p6]):
    rep(n,"PASS" if p else "FAIL")
rep("diff c1-c1_alt = %.3e"%(c1R-c_alt))
fn="results_%d.txt"%int(time.time())
with open(fn,'x') as f: f.write('\n'.join(res)+'\n')
print("wrote",fn)
