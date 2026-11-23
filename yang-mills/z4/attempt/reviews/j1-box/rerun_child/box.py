"""PREDICATES (fixed before first run), per box in {(2,2,2),(3,2,2),(3,3,3)} and s in {0.3,0.1}:
P1 slice dim (= ker d^T, dim of A orthogonal to range(d)) == 2n+1.
P2 P(A'-A)=A'-A for slice vectors (max err < 1e-10)  [tolerance: float64 SVD, cond ~1e1]
P3 Q block matrix Qcc' = -Qcc (Q depends only on c-c'): max abs dev < 1e-9*max|Q|.
P4 Qcc = (kappa/s^2) I3 (isotropic, off-diagonals < 1e-9 rel).
P5 kappa == n to rel 1e-9. Tolerances: double precision with matrices <=81 dim -> errors ~1e-13; 1e-9 leaves margin.
P6 M positive definite on nonconstant slice (min eig > 1e-8) so Gaussian integral converges.
Q defined by integral ~ exp(-Q/2), Q = v^T Qm v, v=(c,c'), c in R^3 with A[x,i]=c_i.
Method: explicit matrices, Schur complement over nonconstant (a,a'). Seeds: none needed (deterministic).
"""
import numpy as np, itertools, sys
def build(N):
    n=N[0]*N[1]*N[2]; idx=lambda x:int(np.ravel_multi_index([x[k]%N[k] for k in range(3)],N))
    sites=list(itertools.product(*[range(m) for m in N]))
    sh=lambda x,i:tuple(x[k]+(k==i) for k in range(3))
    var=lambda x,i:3*idx(x)+i
    d=np.zeros((3*n,n))
    for x in sites:
        for i in range(3):
            d[var(x,i),idx(sh(x,i))]+=1; d[var(x,i),idx(x)]-=1
    rows=[]
    for x in sites:
        for i,j in [(0,1),(0,2),(1,2)]:
            r=np.zeros(3*n); r[var(x,i)]+=1; r[var(sh(x,i),j)]+=1; r[var(sh(x,j),i)]-=1; r[var(x,j)]-=1; rows.append(r)
    C=np.array(rows); return n,d,C.T@C
def run(N,s,out):
    n,d,M=build(N); m=3*n
    U,S,Vt=np.linalg.svd(d,full_matrices=True); r=int((S>1e-10).sum())
    assert r==n-1
    slice_B=U[:,r:]; dim=slice_B.shape[1]
    Pr=U[:,:r]@U[:,:r].T
    # constants
    Uc=np.zeros((m,3))
    for i in range(3): Uc[i::3,i]=1
    # nonconstant slice basis: slice minus constants
    Q_,_=np.linalg.qr(Uc/np.sqrt(n)); 
    Bn=slice_B-Q_@(Q_.T@slice_B); u,sv,_=np.linalg.svd(Bn,full_matrices=False); Nb=u[:,sv>1e-8]
    p2=np.abs((np.eye(m)-Pr)@Nb-Nb).max(); p2=max(p2,np.abs((np.eye(m)-Pr)@Uc-Uc).max())
    Mn=Nb.T@M@Nb; p6=np.linalg.eigvalsh(Mn).min()
    # variables v=(c,c',a,a'); A=Uc c+Nb a
    T=np.zeros((2*m,6+2*Nb.shape[1])); k=Nb.shape[1]
    T[:m,:3]=Uc; T[m:,3:6]=Uc; T[:m,6:6+k]=Nb; T[m:,6+k:]=Nb
    D=np.hstack([-np.eye(m),np.eye(m)])  # A'-A
    H=0.5*T.T@np.block([[M,0*M],[0*M,M]])@T+ (T.T@D.T@D@T)/s**2   # exponent = 1/2 v^T H v
    Hcc=H[:6,:6];Hca=H[:6,6:];Haa=H[6:,6:]
    Qm=Hcc-Hca@np.linalg.solve(Haa,Hca.T)
    a=Qm[:3,:3];b=Qm[:3,3:]
    kap=a[0,0]*s**2
    res=dict(box=N,s=s,n=n,dim=dim,nonconst_dim=k,p2=p2,minMn=p6,
      p3=np.abs(a+b).max()/np.abs(Qm).max(),p4=np.abs(a-a[0,0]*np.eye(3)).max()/a[0,0],kappa=kap,kappa_over_n=kap/n)
    out.write(repr(res)+"\n"+"Qm=\n"+np.array2string(Qm,precision=6,suppress_small=True)+"\n"); 
    ok=dict(P1=dim==2*n+1,P2=p2<1e-10,P3=res['p3']<1e-9,P4=res['p4']<1e-9,P5=abs(kap/n-1)<1e-9,P6=p6>1e-8)
    out.write("PRED "+repr(ok)+"\n\n"); print(N,s,res['kappa'],ok); return ok
with open("result_box.txt","x") as f:
    allok=True
    for N in [(2,2,2),(3,2,2),(3,3,3)]:
        for s in (0.3,0.1): allok&=all(run(N,s,f).values())
    f.write("ALLPASS %s\n"%allok)
sys.exit(0 if allok else 1)
