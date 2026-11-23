import numpy as np, itertools, sys
S=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
E=[1j*s/np.sqrt(2) for s in S]
I2=np.eye(2,dtype=complex)
def expm(c):  # exp(sum c_a e_a)
    n=np.linalg.norm(c)
    if n==0: return I2
    r=n/np.sqrt(2); T=sum(ca*e for ca,e in zip(c,E))
    return np.cos(r)*I2+np.sin(r)/r*T
def dag(A): return np.conj(A.swapaxes(-1,-2))
def make_V(plaqs):  # plaqs: list of 4 link indices (a,b,c,d): Q=Ua Ub Uc^-1 Ud^-1
    P=np.array(plaqs)
    def V(U):  # U: (nl,2,2)
        Q=U[P[:,0]]@U[P[:,1]]@dag(U[P[:,2]])@dag(U[P[:,3]])
        return -0.5*np.einsum('pii->',Q).real
    return V
def hessian(V,U0,h=1e-3):
    nl=len(U0); n=3*nl
    def pert(ts):  # ts: list of (index,amount)
        U=U0.copy(); c={}
        for i,a in ts: c.setdefault(i//3,np.zeros(3))[i%3]+=a
        for l,v in c.items(): U[l]=expm(v)@U[l]
        return U
    H=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            if i==j:
                v=(V(pert([(i,2*h)]))-2*V(U0)+V(pert([(i,-2*h)])))/(4*h*h)
            else:
                v=(V(pert([(i,h),(j,h)]))-V(pert([(i,h),(j,-h)]))-V(pert([(i,-h),(j,h)]))+V(pert([(i,-h),(j,-h)])))/(4*h*h)
            H[i,j]=H[j,i]=v
    return H
def control():
    U=np.array([I2,-I2,I2,I2]); V=make_V([[0,1,2,3]])
    w=np.linalg.eigvalsh((lambda H:(H+H.T)/2)(hessian(V,U)))
    return w
def lattice():
    sites=list(itertools.product([0,1],repeat=4))
    sid={s:k for k,s in enumerate(sites)}
    lid=lambda x,mu:sid[x]*4+mu
    flip=lambda x,mu:tuple(b^(k==mu) for k,b in enumerate(x))
    U=np.zeros((64,2,2),complex)
    for x in sites:
        for mu in range(4):
            U[lid(x,mu)]=(-1)**(sum(x[:mu]))*I2
    pl=[]
    for x in sites:
        for mu in range(4):
            for nu in range(mu+1,4):
                pl.append([lid(x,mu),lid(flip(x,mu),nu),lid(flip(x,nu),mu),lid(x,nu)])
    return sites,sid,flip,U,pl
def summ(w,k=5):
    return w[:k],w[-3:]
def mult(w,tol=1e-5):
    out=[];
    for x in w:
        if out and abs(x-out[-1][0])<tol: out[-1][1]+=1
        else: out.append([x,1])
    return out
if __name__=="__main__":
    wc=control()
    ok=np.allclose(np.sort(wc),[-2]*3+[0]*9,atol=1e-6)
    with open('control_check.txt','x') as f:
        f.write("control eigenvalues: %s\nPASS=%s\n"%(np.array2string(wc,precision=9),ok))
    print("control",ok,wc)
    if not ok: sys.exit("control failed")
    sites,sid,flip,U,pl=lattice(); V=make_V(pl)
    # check all plaquettes -1
    Q=[U[a]@U[b]@dag(U[c])@dag(U[d]) for a,b,c,d in pl]
    assert all(np.allclose(q,-I2) for q in Q)
    H=hessian(V,U); H=(H+H.T)/2
    w,vec=np.linalg.eigh(H)
    G=np.zeros((192,48))
    for x in sites:
        for mu in range(4):
            e=sid[x]*4+mu; y=sid[flip(x,mu)]
            for a in range(3):
                G[3*e+a,3*sid[x]+a]+=1; G[3*e+a,3*y+a]-=1
    u,s,vt=np.linalg.svd(G,full_matrices=True)
    r=int((s>1e-9).sum()); Pm=u[:,r:]
    Hh=Pm.T@H@Pm; wh=np.linalg.eigvalsh((Hh+Hh.T)/2)
    gl=np.linalg.norm(H@u[:,:r])
    with open('results.txt','x') as f:
        f.write("h=1e-3, central FD polarization, 192x192\nsym asym check done by symmetrization\n")
        f.write("full smallest5 %s\nfull largest3 %s\nc_full=%.8f\n"%(w[:5],w[-3:],-w[0]))
        f.write("full multiplicities (val,mult): %s\n"%[(round(a,6),b) for a,b in mult(w)])
        f.write("gauge rank %d, horizontal dim %d, |H*gauge|=%.2e\n"%(r,192-r,gl))
        f.write("horiz smallest5 %s\nhoriz largest3 %s\nc_horiz=%.8f\n"%(wh[:5],wh[-3:],-wh[0]))
        f.write("horiz multiplicities: %s\n"%[(round(a,6),b) for a,b in mult(wh)])
    print(open('results.txt').read())
