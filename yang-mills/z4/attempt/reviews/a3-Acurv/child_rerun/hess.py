"""PCP child: lam(U,b)=min eig(I+Hess V), V=-(b/2)ReTr(U1U2U3^-1U4^-1), SU(2)^4, metric -Tr(XY).
Predicates fixed BEFORE first run (my expectations from hand derivation: at Q=-1 Hess V = -(b/2)|s1+s2-s3-s4|^2 per colour):
 P0: control d2/dt2 ReTr exp(tX) = -1 (FD agrees within 1e-6).
 P1: analytic Hessian == central-FD Hessian, max abs diff < 1e-5 at 20 random configs and at Q=-1 (FD h=1e-3: trunc ~h^2*f''''/12~1e-7, round ~eps/h^2~1e-10).
 P2: lam at Q=-1 equals 1-2b within 1e-8 (analytic, pure float64 roundoff ~1e-14) for b in {0.5,1,2,4}.
 P3: global min over configs equals 1-2b (Q1 value) within 1e-6 -- expectation uncertain; measured. Reported as min found (upper bound on true min).
 P4: horizontal min at Q=-1: gauge span rank 9 (stabiliser dim 3), horizontal dim 3, horizontal eigs equal 1 (Hess V vanishes on complement of
     (1,1,-1,-1) combos? gauge directions xi_x - xi_y... ) -- expectation: horizontal min = 1 -2b*? unknown; measured. Rank tolerance 1e-9 (SVD gap).
Results files opened mode 'x'. Seeds fixed (12345)."""
import numpy as np, sys, json

def expm(M):
    r2=-np.trace(M@M).real/2  # M^2=-(r^2/2) I -> here r2=r^2/2... 
    w=np.sqrt(max(r2,0.0))
    return np.cos(w)*np.eye(2)+(np.sinc(w/np.pi) if True else 1)*M
np.random.seed(12345)
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
E=[1j*x/np.sqrt(2) for x in s]
def ex(t): return expm(sum(t[a]*E[a] for a in range(3)))
def Qof(U): return U[0]@U[1]@np.linalg.inv(U[2])@np.linalg.inv(U[3])
def V(U,b): return -(b/2)*np.trace(Qof(U)).real
def Ad(g,X): return g@X@np.linalg.inv(g)
LINK=np.repeat(np.arange(4),3)
SAME=(LINK[:,None]==LINK[None,:]); LT=(LINK[:,None]<LINK[None,:])
EA=np.array(E)
def hessV(U,b):
    Q0=Qof(U); inv=np.linalg.inv
    Gs=[np.eye(2),U[0],U[0]@U[1]@inv(U[2]),Q0]; sg=[1,1,-1,-1]
    M=np.array([sg[k]*Gs[k]@EA[a]@inv(Gs[k]) for k in range(4) for a in range(3)])
    P=np.einsum('mij,njk,ki->mn',M,M,Q0).real
    H=np.where(SAME,0.5*(P+P.T),np.where(LT,P,P.T))
    return -(b/2)*H
def fdH(U,b,h=1e-3):
    def f(t): return V([ex(t[3*k:3*k+3])@U[k] for k in range(4)],b)
    H=np.zeros((12,12)); I=np.eye(12); f0=f(np.zeros(12))
    for i in range(12):
        H[i,i]=(f(h*I[i])-2*f0+f(-h*I[i]))/h**2
        for j in range(i):
            H[i,j]=H[j,i]=(f(h*(I[i]+I[j]))-f(h*(I[i]-I[j]))-f(h*(-I[i]+I[j]))+f(-h*(I[i]+I[j])))/(4*h*h)
    return H
def lam(U,b): return np.linalg.eigvalsh(np.eye(12)+hessV(U,b))[0]
def haar():
    q=np.random.randn(4);q/=np.linalg.norm(q)
    return np.array([[q[0]+1j*q[3],q[2]+1j*q[1]],[-q[2]+1j*q[1],q[0]-1j*q[3]]])
def hill(f):
    x=np.zeros(12); fx=f(x); st=0.5
    for it in range(1500):
        y=x+st*np.random.randn(12)/np.sqrt(12); fy=f(y)
        if fy<fx: x,fx=y,fy; st*=1.2
        else: st*=0.97
        if st<1e-10: break
    return fx
def log(*a):
    print(*a); open('notes.md','a').write(' '.join(map(str,a))+'\n')
out=open('results_hess.json','x')
R={}
# P0
X=1j*s[2]/np.sqrt(2); h=1e-3
d2=(np.trace(expm(h*X)).real-2*np.trace(expm(0*X)).real+np.trace(expm(-h*X)).real)/h**2
R['P0_fd']=d2; log('P0 control FD d2=',d2,'pass',abs(d2+1)<1e-6)
# P1
I2=np.eye(2); Uq=[-I2,I2,I2,I2]
mx=0
for i in range(20):
    U=[haar() for _ in range(4)]; b=1.7
    mx=max(mx,np.abs(hessV(U,b)-fdH(U,b)).max())
d=np.abs(hessV(Uq,2.0)-fdH(Uq,2.0)).max()
R['P1']=[mx,d]; log('P1 max|analytic-FD| random',mx,' at Q=-1',d,'pass',mx<1e-5 and d<1e-5)
# Q1
bs=[0.5,1,2,4]
R['Q1']={}
for b in bs:
    l=lam(Uq,b); R['Q1'][b]=l; log('Q1 b=',b,'lam=',l,'1-2b=',1-2*b,'P2 pass',abs(l-(1-2*b))<1e-8)
# Q2
R['Q2']={}
def par(t): return [ex(t[3*k:3*k+3])@U0[k] for k in range(4)]
for b in bs:
    best=(1e9,None)
    vals=[]
    for i in range(5000):
        U=[haar() for _ in range(4)]; l=lam(U,b); vals.append((l,i))
        if l<best[0]: best=(l,U)
    # local opt from 15 best starts + Q1 config perturbed
    vals.sort(key=lambda x:x[0])
    np.random.seed(777+int(b*10))
    starts=[]
    for _ in range(12):
        starts.append([haar() for _ in range(4)])
    starts.append([ex(0.05*np.random.randn(3))@u for u in Uq])
    lo=best[0]
    for U0 in starts+[best[1]]:
        lo=min(lo,hill(lambda t:lam(par(t),b)))
    R['Q2'][b]={'random_min':best[0],'local_min':lo,'Q1':1-2*b,'diff':lo-(1-2*b)}
    log('Q2 b=',b,'random min',best[0],'local min',lo,'Q1 value',1-2*b,'diff',lo-(1-2*b))
# Q3
def gauge_matrix(U):
    # xi in R^12 (corner x0..x3,3 comps); link k=(x,y): U1(0,1),U2(1,2),U3(3,2),U4(0,3)
    links=[(0,1),(1,2),(3,2),(0,3)]
    G=np.zeros((12,12))
    for k,(x,y) in enumerate(links):
        for a in range(3):
            # d/dxi_{x,a}: E_a ; d/dxi_{y,a}: -Ad_U E_a ; coordinates via -Tr(E_b Z)
            Z1=E[a]; Z2=-Ad(U[k],E[a])
            for b_ in range(3):
                G[3*k+b_,3*x+a]+=(-np.trace(E[b_]@Z1)).real
                G[3*k+b_,3*y+a]+=(-np.trace(E[b_]@Z2)).real
    return G
G=gauge_matrix(Uq); sv=np.linalg.svd(G,compute_uv=False)
log('Q3 gauge singular values',np.round(sv,10))
rank=int((sv>1e-9).sum()); log('rank',rank)
Uu,S,Vt=np.linalg.svd(G); Gc=Uu[:,rank:]  # complement of column span
R['Q3']={'rank':rank}
for b in bs:
    A=np.eye(12)+hessV(Uq,b); Hh=Gc.T@A@Gc; ev=np.linalg.eigvalsh(Hh)
    Aa=Uu[:,:rank].T@A@Uu[:,:rank]
    R['Q3'][b]={'horizontal_eigs':ev.tolist(),'gauge_min':float(np.linalg.eigvalsh(Aa)[0])}
    log('Q3 b=',b,'horizontal eigs',ev,'gauge-block min',np.linalg.eigvalsh(Aa)[0],'full lam',lam(Uq,b))
json.dump(R,out,default=float,indent=1); out.close()
