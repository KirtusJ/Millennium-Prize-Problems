"""Library: SU(2) Wilson LGT on (Z/2)^4. Hessian (analytic), quadratic form, gauge projector.
Convention: tangent t_e in su(2) coords (3 per link) in basis e_a=i sigma_a/sqrt2, U_e -> exp(s t_e)U_e.
Plaquette: Q(s)=exp(s a1)exp(s a2)exp(s a3)exp(s a4)Q, a1=t1, a2=Ad(U1)t2, a3=-Ad(U1U2U3^-1)t3, a4=-Ad(Q)t4;
d2 Re Tr Q = Re Tr[((sum a)^2 + sum_{i<j}[a_i,a_j]) Q];  V=-(beta/2) sum Re Tr Q, beta=1."""
import numpy as np
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
E=1j*sig/np.sqrt(2)
EE=np.einsum('kab,lbc->klac',E,E)
SITES=[tuple((s>>b)&1 for b in range(4)) for s in range(16)]
def sidx(x): return sum(b<<i for i,b in enumerate(x))
def flip(s,m): return s^(1<<m)
def lid(s,m): return s*4+m
PL=[]  # (l1,l2,l3,l4)
for s in range(16):
    for m in range(4):
        for n in range(m+1,4):
            PL.append((lid(s,m),lid(flip(s,m),n),lid(flip(s,n),m),lid(s,n)))
PL=np.array(PL)
def expm_su2(v):  # v (...,3) coords -> exp(sum v_a e_a)
    th=np.linalg.norm(v,axis=-1)/np.sqrt(2)  # sum v_a i sigma_a/sqrt2 = i th (n.sigma)
    th_s=np.where(th<1e-300,1,th); n=v/(np.sqrt(2)*th_s[...,None])
    ns=np.einsum('...a,aij->...ij',n,sig)
    return np.cos(th)[...,None,None]*np.eye(2)+1j*np.sin(th)[...,None,None]*ns
def inv(U): return np.conj(np.swapaxes(U,-1,-2))
def Ad(g): # (...,3,3): R_ab=-Tr(e_a g e_b g^-1)
    return np.real(-np.einsum('aij,...jk,bkl,...li->...ab',E,g,E,inv(g),optimize=True))
def randU(rng,n=64):
    q=rng.normal(size=(n,4)); q/=np.linalg.norm(q,axis=1)[:,None]
    return q[:,0,None,None]*np.eye(2)+1j*np.einsum('na,aij->nij',q[:,1:],sig)
def plaq_data(U):
    U1,U2,U3,U4=[U[...,PL[:,i],:,:] for i in range(4)]
    Q=U1@U2@inv(U3)@inv(U4)
    M=np.zeros(U.shape[:-3]+(96,4,3,3))
    M[...,0,:,:]=np.eye(3)
    M[...,1,:,:]=Ad(U1)
    M[...,2,:,:]=-Ad(U1@U2@inv(U3))
    M[...,3,:,:]=-Ad(Q)
    A=np.real(np.einsum('klab,...ba->...kl',EE,Q))
    return Q,M,A
def Gsym(A):
    I=(np.arange(4)[:,None]<np.arange(4)[None,:]).astype(float)
    G=A[...,None,None,:,:]*(1+I)[:,:,None,None]-I[:,:,None,None]*np.swapaxes(A,-1,-2)[...,None,None,:,:]
    # G[i,j,k,l]
    return G
def Hmat(U):
    Q,M,A=plaq_data(U); G=Gsym(A)
    Gs=(G+np.einsum('pijkl->pjilk',G))/2
    # y_{i,m}= sum_n M[p,i,m? ...]: a_i coord k = sum_m M[p,i,k,m] t_{l_i,m}
    Hl=-0.5*np.einsum('pikm,pijkl,pjln->pimjn',M,Gs,M)
    Hl2=Hl
    Hflat=np.zeros((192,192))
    idx=(PL[:,:,None]*3+np.arange(3)[None,None,:]).reshape(96,12)
    Hl12=Hl2.reshape(96,12,12)
    for p in range(96):
        Hflat[np.ix_(idx[p],idx[p])]+=Hl12[p]
    return (Hflat+Hflat.T)/2
def qform(U,T):
    """Hess V(t,t) for batch U (...,64,2,2), t (64,3)"""
    Q,M,A=plaq_data(U); G=Gsym(A)
    tl=T[PL]  # (96,4,3)
    y=np.einsum('...pikm,pim->...pik',M,tl)
    return -0.5*np.einsum('...pik,...pijkl,...pjl->...',y,G,y)
def Vact(U):
    Q,_,_=plaq_data(U); return -0.5*np.real(np.trace(Q,axis1=-2,axis2=-1)).sum(-1)
def gauge_basis(U):
    """returns 192 x r orthonormal basis of gauge directions"""
    B=np.zeros((192,48))
    for s in range(16):
        for m in range(4):
            e=lid(s,m); y=flip(s,m); R=Ad(U[e])
            for a in range(3):
                B[e*3:e*3+3,s*3+a]+=np.eye(3)[a]
                B[e*3:e*3+3,y*3+a]-=R[:,a]
    u,sv,vt=np.linalg.svd(B,full_matrices=True)
    r=int((sv>1e-9).sum()); return u[:,:r],u[:,r:],r
def piflux():
    U=np.zeros((64,2,2),complex)
    for s in range(16):
        x=SITES[s]
        sg=[1,(-1)**x[0],(-1)**(x[0]+x[1]),(-1)**(x[0]+x[1]+x[2])]
        for m in range(4): U[lid(s,m)]=sg[m]*np.eye(2)
    return U
def cH(U):
    H=Hmat(U); _,Z,r=gauge_basis(U)
    return -np.linalg.eigvalsh(Z.T@H@Z)[0]
def cfull(U): return -np.linalg.eigvalsh(Hmat(U))[0]
