"""Predicates fixed BEFORE first run (tolerances: FD h=1e-3 -> truncation ~h^2*|f''''|~1e-6*beta/12, roundoff ~eps*beta/h^2~1e-9; tol 1e-5 on eigenvalues).
P1 (a) Q=-1 config, beta=1: eig B = {1-2b x3, 1 x9} within 1e-5.
P2 (a) same, beta=3: {-5 x3, 1 x9} within 1e-5.
P3 (a) random config (seed 12345), beta=3: max|H(h)-H(2h)|/3 (Richardson error est) < 1e-4, and Richardson-corrected vs H(h) agree 1e-4.
P4 (b) U=1 lattice, beta=1: all eig(Hess V) >= -1e-5; report zero count (|eig|<1e-5).
P5 (b) random config (seed 777): symmetry error of gradient-differenced Hessian (non-symmetric-by-construction scheme) < 1e-5; report min eig B.
Plaquette (b) convention: Q = U_{x,1} U_{x+e1,2} U_{x+e2,1}^-1 U_{x,2}^-1 (the prompt's x+1, x+2 read as x+e1, x+e2).
Output file opened mode 'x'."""
import numpy as np, sys
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def expm(t):
    n=np.linalg.norm(t)
    if n==0: return np.eye(2,dtype=complex)
    th=n/np.sqrt(2); N=sum(t[a]/n*s[a] for a in range(3))
    return np.cos(th)*np.eye(2)+1j*np.sin(th)*N
def inv(U): return U.conj().T
def randSU2(rng):
    q=rng.normal(size=4); q/=np.linalg.norm(q)
    return q[0]*np.eye(2)+1j*sum(q[a+1]*s[a] for a in range(3))
def pert(U,t): return [expm(t[3*e:3*e+3])@U[e] for e in range(len(U))]
def Vplaq(U,beta):
    Q=U[0]@U[1]@inv(U[2])@inv(U[3]); return -beta/2*np.trace(Q).real
plaqs=[]
def idx(x,y,mu): return 2*((x%2)*2+(y%2))+mu   # mu 0,1
def Vlat(U,beta):
    v=0
    for x in range(2):
        for y in range(2):
            Q=U[idx(x,y,0)]@U[idx(x+1,y,1)]@inv(U[idx(x,y+1,0)])@inv(U[idx(x,y,1)])
            v+=np.trace(Q).real
    return -beta/2*v
def hess(f,U,h):
    n=3*len(U); H=np.zeros((n,n))
    def F(i,si,j,sj):
        t=np.zeros(n); t[i]+=si*h; t[j]+=sj*h; return f(pert(U,t))
    for i in range(n):
        for j in range(i,n):
            H[i,j]=H[j,i]=(F(i,1,j,1)-F(i,1,j,-1)-F(i,-1,j,1)+F(i,-1,j,-1))/(4*h*h)
    return H
def hess_grad(f,U,h):
    n=3*len(U)
    def g(t0):
        G=np.zeros(n)
        for i in range(n):
            tp=t0.copy();tp[i]+=h;tm=t0.copy();tm[i]-=h
            G[i]=(f(pert(U,tp))-f(pert(U,tm)))/(2*h)
        return G
    H=np.zeros((n,n))
    for j in range(n):
        tp=np.zeros(n);tp[j]=h;tm=np.zeros(n);tm[j]=-h
        H[:,j]=(g(tp)-g(tm))/(2*h)   # not symmetric by construction
    return H
out=open(sys.argv[1],"x")
def P(*a):
    m=" ".join(str(x) for x in a); print(m); out.write(m+"\n"); out.flush()
np.set_printoptions(precision=8,linewidth=200,suppress=True)
h=1e-3; I=np.eye(2,dtype=complex)
# (a)
Uq=[-I,I.copy(),I.copy(),I.copy()]
for beta,pred in [(1,"P1"),(3,"P2")]:
    B=np.eye(12)+hess(lambda U:Vplaq(U,beta),Uq,h)
    ev=np.linalg.eigvalsh(B); exp=np.sort(np.array([1-2*beta]*3+[1]*9))
    err=np.abs(ev-exp).max()
    P(pred,"beta",beta,"eig",ev,"max|eig-claim|",err,"PASS" if err<1e-5 else "FAIL")
rng=np.random.default_rng(12345); Ur=[randSU2(rng) for _ in range(4)]
f=lambda U:Vplaq(U,3.0)
H1=hess(f,Ur,h);H2=hess(f,Ur,2*h);HR=(4*H1-H2)/3;Hg=hess_grad(f,Ur,h)
P("P3 random plaquette: max|H(h)-H(2h)|/3 =",np.abs(H1-H2).max()/3,"max|H(h)-HR|=",np.abs(H1-HR).max(),"max|H(h)-Hgrad(h)|=",np.abs(H1-Hg).max(),
  "PASS" if np.abs(H1-H2).max()/3<1e-4 and np.abs(H1-HR).max()<1e-4 else "FAIL")
P("  min eig B (random plaq, beta=3) H1/HR:",np.linalg.eigvalsh(np.eye(12)+H1)[0],np.linalg.eigvalsh(np.eye(12)+HR)[0])
# (b)
U0=[I.copy() for _ in range(8)]
H0=hess(lambda U:Vlat(U,1.0),U0,h); ev=np.linalg.eigvalsh(H0)
P("P4 lattice U=1 beta=1 HessV eigs",ev,"min",ev[0],"zeros(|e|<1e-5):",int((abs(ev)<1e-5).sum()),"PASS" if ev[0]>=-1e-5 else "FAIL")
rng=np.random.default_rng(777); Ul=[randSU2(rng) for _ in range(8)]
fl=lambda U:Vlat(U,1.0)
Hs=hess(fl,Ul,h); Hn=hess_grad(fl,Ul,h)
sym=np.abs(Hn-Hn.T).max()
P("P5 lattice random: sym err of gradient-differenced Hessian",sym,"; max|Hsym-Hn|",np.abs(Hs-Hn).max(),"; sym err of 4-point scheme",np.abs(Hs-Hs.T).max(),
  "min eig B:",np.linalg.eigvalsh(np.eye(24)+Hs)[0],"(from Hn sym part:",np.linalg.eigvalsh(np.eye(24)+(Hn+Hn.T)/2)[0],")","PASS" if sym<1e-5 else "FAIL")
