"""Functions of convexscalar.py (system and kappa), copied without change so that follow-up programs can import them."""
import sys, numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spl
m2=0.25; k=1.0
def lap1(n,h):
    c=np.array([-1,16,-30,16,-1])/(12*h*h)
    return sps.diags([c[0]*np.ones(n-2),c[1]*np.ones(n-1),c[2]*np.ones(n),c[3]*np.ones(n-1),c[4]*np.ones(n-2)],[-2,-1,0,1,2],format='csr')
def system(which,n,L):
    x=np.linspace(-L,L,n); h=x[1]-x[0]; I=sps.identity(n,format='csr'); D=lap1(n,h)
    if which=='A':
        Y,Z=np.meshgrid(x,x,indexing='ij'); p1=(Y+Z)/np.sqrt(2); p2=(Y-Z)/np.sqrt(2); phis=(p1,p2)
        K=m2*np.eye(2)+k*np.array([[1,-1],[-1,1.]]); e=np.array([1,-1])/np.sqrt(2)
        Lap=sps.kron(D,I)+sps.kron(I,D); shape=(n,n); fib=1
    else:
        Y,Z,W=np.meshgrid(x,x,x,indexing='ij'); p1=(Y+Z)/np.sqrt(2); p2=(Y-Z)/np.sqrt(2); phis=(p1,p2,W)
        K=m2*np.eye(3)+k*np.array([[1,-1,0],[-1,2,-1],[0,-1,1.]]); e=np.array([1,-1,0])/np.sqrt(2)
        Lap=sps.kron(sps.kron(D,I),I)+sps.kron(sps.kron(I,D),I)+sps.kron(sps.kron(I,I),D); shape=(n,n,n); fib=1
    quad=0.5*sum(K[i,j]*phis[i]*phis[j] for i in range(len(phis)) for j in range(len(phis)))
    w,U=np.linalg.eigh(K); om=(U*np.sqrt(w))@U.T
    return dict(phis=phis,quad=quad,Lap=Lap,shape=shape,fib=fib,lamN=e@om@e,free=(e@om@e)/(e@K@e),h=h)
def kappa(S,V):
    U=(S['quad']+V).ravel(); H=(-0.5*S['Lap']+sps.diags(U)).tocsc(); shape=S['shape']
    E0,Om=spl.eigsh(H,k=1,sigma=U.min()-1.0,which='LM'); E0=E0[0]; Om=np.abs(Om[:,0])
    A=Om.reshape(shape); nrm=np.sqrt((A*A).sum(axis=S['fib'],keepdims=True)); F=A/np.where(nrm>0,nrm,1)   # unit vector along the fibre axis for each value of the block variables
    def P(v): a=v.reshape(shape); return (F*(F*a).sum(axis=S['fib'],keepdims=True)).ravel()
    lu=spl.splu(H-(E0-1e-7)*sps.identity(H.shape[0],format='csc'))
    def Sop(v): g=v-P(v); return (lambda y: y-P(y))(lu.solve(g))
    mu=spl.eigsh(spl.LinearOperator(H.shape,matvec=Sop,dtype=float),k=1,which='LA',tol=1e-9,v0=np.random.default_rng(5).normal(size=H.shape[0]))[0][0]
    return mu,E0
