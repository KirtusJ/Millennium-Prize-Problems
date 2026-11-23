"""SU(2) Schroedinger-functional one-loop c1(R), dense full-lattice, own code.
Predicates fixed BEFORE first run (tolerances in brackets, origin stated):
 P1 |grad S at V|_max < 1e-6        [FD plaquette Hessian/grad error ~h^2 ~1e-8 (h=1e-4), roundoff 1e-16/h]
 P2 S(V) == 3R^4(1-cos((pi-2eta)/R^2)) to 1e-9   [float64 summation]
 P3 |H D|_max < 1e-6                [same FD origin]
 P4 min eig(H+DD^T) > 1e-6          [positivity; smallest physical eigenvalue expected O(0.01)]
 P5 D^T D full column rank (min eig>1e-8)
 P6 c1 from h=0.02 vs h=0.01 agree to 1e-3 relative (central diff, error ~h^2 Gamma''' ; Richardson reported)
Usage: sf1loop.py R outfile   (outfile opened with mode 'x')
"""
import sys, json, numpy as np, itertools
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def expsu2(x):  # x (...,3) -> exp(sum x_a i sigma_a/2)
    n=np.linalg.norm(x,axis=-1); c=np.cos(n/2); sn=np.where(n>1e-300,np.sin(n/2)/np.where(n>0,n,1),0.5)
    M=c[...,None,None]*np.eye(2)
    for a in range(3): M=M+1j*(sn*x[...,a])[...,None,None]*s[a]
    return M
def dag(M): return np.conj(np.swapaxes(M,-1,-2))
def Adj(V):  # R_ab = 1/2 tr(sigma_a V sigma_b V^dag)
    R=np.zeros(V.shape[:-2]+(3,3))
    for a in range(3):
        for b in range(3):
            R[...,a,b]=0.5*np.real(np.trace(s[a]@V@s[b]@dag(V),axis1=-2,axis2=-1))
    return R
def build(R,eta):
    L=R; shape=(R+1,L,L,L)
    V=np.zeros(shape+(4,2,2),complex)
    for x0 in range(R+1):
        phi=-eta-(np.pi-2*eta)*x0/R
        V[x0,...,0,:,:]=np.eye(2)
        for k in (1,2,3): V[x0,...,k,:,:]=np.diag([np.exp(1j*phi/R),np.exp(-1j*phi/R)])
    lid=-np.ones(shape+(4,),int); n=0
    for x in itertools.product(range(R+1),range(L),range(L),range(L)):
        for mu in range(4):
            if (mu==0 and x[0]<R) or (mu>0 and 1<=x[0]<=R-1): lid[x+(mu,)]=n; n+=1
    return V,lid,n
def sh(x,mu,R):
    y=list(x); y[mu]+=1
    if mu>0: y[mu]%=R
    return tuple(y)
def plaquettes(R,lid):
    P=[]
    for x in itertools.product(range(R+1),range(R),range(R),range(R)):
        for mu in range(4):
            for nu in range(mu+1,4):
                if (mu==0 and x[0]==R): continue
                l=[x+(mu,),sh(x,mu,R)+(nu,),sh(x,nu,R)+(mu,),x+(nu,)]
                if any(lid[t]>=0 for t in l): P.append(l)
    return P
def pact(X,Vs):  # X (N,4,3), Vs (N,4,2,2)
    U=expsu2(X)@Vs
    Up=U[:,0]@U[:,1]@dag(U[:,2])@dag(U[:,3])
    return 1-0.5*np.real(np.trace(Up,axis1=-2,axis2=-1))
def hessian(R,V,lid,n,P,h=1e-4):
    N=len(P); Vs=np.array([[V[t] for t in l] for l in P]); ids=np.array([[lid[t] for t in l] for l in P])
    def f(e): return pact(e.reshape(N,4,3),Vs)
    z=np.zeros((N,12)); H=np.zeros((3*n,3*n)); g=np.zeros(3*n)
    S=pact(z.reshape(N,4,3),Vs).sum()
    gl=np.zeros((N,12)); Hl=np.zeros((N,12,12))
    for i in range(12):
        ei=np.zeros(12); ei[i]=h
        gl[:,i]=(f(z+ei)-f(z-ei))/(2*h)
        for j in range(i,12):
            ej=np.zeros(12); ej[j]=h
            if i==j: Hl[:,i,i]=(f(z+ei)-2*f(z)+f(z-ei))/h**2
            else: Hl[:,i,j]=Hl[:,j,i]=(f(z+ei+ej)-f(z+ei-ej)-f(z-ei+ej)+f(z-ei-ej))/(4*h*h)
    for p in range(N):
        gi=[(3*ids[p,s]+a,3*s+a) for s in range(4) if ids[p,s]>=0 for a in range(3)]
        for (I,i) in gi:
            g[I]+=gl[p,i]
            for (J,j) in gi: H[I,J]+=Hl[p,i,j]
    return S,g,H
def Dmat(R,V,lid,n):
    nom=3*R**3*(R-1)+1; D=np.zeros((3*n,nom)); col={}
    c=0
    for x in itertools.product(range(1,R),range(R),range(R),range(R)):
        col[x]=c; c+=3
    T=c
    for x in itertools.product(range(R+1),range(R),range(R),range(R)):
        for mu in range(4):
            l=lid[x+(mu,)]
            if l<0: continue
            y=sh(x,mu,R); Ad=Adj(V[x+(mu,)])
            if x in col: D[3*l:3*l+3,col[x]:col[x]+3]+=np.eye(3)
            if y in col: D[3*l:3*l+3,col[y]:col[y]+3]-=Ad
            elif y[0]==R: D[3*l:3*l+3,T]-=Ad[:,2]
    return D
def gamma1(R,eta):
    V,lid,n=build(R,eta); P=plaquettes(R,lid)
    S,g,H=hessian(R,V,lid,n,P); D=Dmat(R,V,lid,n)
    A=H+D@D.T; DD=D.T@D
    chk=dict(S=S,S0=3*R**4*(1-np.cos((np.pi-2*eta)/R**2)),gradmax=np.abs(g).max(),HD=np.abs(H@D).max(),
      mineigA=np.linalg.eigvalsh(A)[0],mineigDD=np.linalg.eigvalsh(DD)[0],nlinks=n,nplaq=len(P),ncol=D.shape[1])
    sa=np.linalg.slogdet(A); sd=np.linalg.slogdet(DD)
    assert sa[0]>0 and sd[0]>0
    return 0.5*sa[1]-sd[1],chk
if __name__=="__main__":
    R=int(sys.argv[1]); out=sys.argv[2]; eta0=np.pi/4
    k=4*3*R**4*np.sin((np.pi-2*eta0)/R**2)*2/R**2
    res={"R":R,"k":k}
    G={}
    for h in (0.02,0.01):
        for sgn in (-1,1):
            G[(h,sgn)],ck=gamma1(R,eta0+sgn*h); res[f"chk_h{h}_{sgn}"]=ck; print(h,sgn,G[(h,sgn)],ck,flush=True)
    d={h:(G[(h,1)]-G[(h,-1)])/(2*h) for h in (0.02,0.01)}
    rich=(4*d[0.01]-d[0.02])/3
    res.update(dG_h02=d[0.02],dG_h01=d[0.01],dG_rich=rich,c1_h02=-d[0.02]/k,c1_h01=-d[0.01]/k,c1_rich=-rich/k)
    with open(out,"x") as f: json.dump(res,f,indent=1,default=float)
    print(json.dumps({k_:v for k_,v in res.items() if k_.startswith('c1') or k_=='k'}))
