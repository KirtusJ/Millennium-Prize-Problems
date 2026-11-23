"""lat3.py -- transfer-matrix spectrum, SU(2) Wilson LGT on the 1x1x1xZ lattice (three spatial links), center-even sector.
T = e^{-V/2} K e^{-V/2}, V = sum_{i<j} V_ij, V_ij = beta(1 - 1/2 Tr comm(U_i,U_j)) = 2 beta s_i^2 s_j^2 (1-u_ij^2),
s_i = sin a_i, u_ij = n_i.n_j (D2 of NUMERICS_2DIR, re-verified in xquad.py Q0).
K diagonal in Peter-Weyl basis: per link (2/beta) e^{-beta} I_{n+1}(beta) (n=2j); normalised by n=0 -> I_{n+1}/I_1.
Basis: F_{n1l1}F_{n2l2}F_{n3l3} x (3j-coupled Y_{l1}Y_{l2}Y_{l3} to 0), F_{nl} ~ sin^l a C^{(l+1)}_{n-l}(cos a), n_i <= N.
Center-even: all n_i even. Exact symmetries used as sectors: l_i parities (U_i -> U_i^{-1}); images of (001),(110) counted x3.
e^{-V/2} = prod_{i<j} e^{-V_ij/2} exactly (multiplication operators commute). Each E_ij = P e^{-V_ij/2} P is computed exactly
up to quadrature: Legendre expansion in u_ij (k even), pair coupled to the spectator's l (ang.pairA, Edmonds 7.1.6).
Matrix diagonalised: M = K^{1/2} A A^T K^{1/2}, A = E12 E13 E23 (equals K^{1/2} e^{-V} K^{1/2} as N -> inf; at finite N it is
NOT a compression of T: convergence in N is checked, not assumed).
Quadrature: a: Gauss-Chebyshev-U with MA nodes; u: Gauss-Legendre 64 nodes.
Bessel: power series (beta <= 32, n <= 40: series of positive terms, no cancellation).
Usage: python3 lat3.py MODE BETA N MA OUTFILE    MODE in {full, v0, dec}  (v0: V=0;  dec: E13=E23=1, third link decoupled)
PREDICATES (fixed before first run):
 L1 (v0) eigenvalues -ln(lambda/lambda0) equal the sorted sums of -ln(I_{n_i+1}/I_1) over basis states, max err < 1e-12
    (tolerance: double rounding of products of numbers O(1)).
 L2 (dec, sector (000)) the lowest levels include the 2-direction values of NUMERICS_2DIR: beta=2: 1.63761996 (m_e),
    beta=4: 0.76319885, within 1e-4 at N=8 (tolerance: truncation, their N was much larger; measured diff is reported).
 L3 (full) M symmetric to 1e-12 and positive semidefinite (min eigenvalue > -1e-12 lambda0).
 L4 (full, analyse) m_e changes by < 1e-3 between N and N+2 for the beta declared converged; otherwise only measured.
 L5 (full) MA -> MA+16 changes m_e by < 1e-9 (quadrature).
"""
import sys, json, math, time
import numpy as np
from ang import pairA

def besI(n, x):
    t=(x/2)**n/math.factorial(n); s=0.0
    for m in range(400):
        s+=t; t*=(x/2)**2/((m+1)*(m+1+n))
        if t<1e-18*s: break
    return s

def Fbasis(N, a):
    """F[(n,l)] on grid a, orthonormal wrt (2/pi) sin^2 a da (normalised on the exact grid)."""
    c=np.cos(a); out={}
    for l in range(N+1):
        lam=l+1; C=[np.ones_like(c), 2*lam*c]
        for m in range(1,N-l): C.append((2*(m+lam)*c*C[m]-(m+2*lam-1)*C[m-1])/(m+1))
        for n in range(l,N+1): out[(n,l)]=np.sin(a)**l*C[n-l]
    return out

def main():
    mode,beta,N,MA,out=sys.argv[1],float(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
    f=open(out,'x'); t0=time.time()
    k=np.arange(1,MA+1); a=k*np.pi/(MA+1); wa=2/(MA+1)*np.sin(a)**2
    Fd=Fbasis(N,a)
    for key in Fd: Fd[key]=Fd[key]/math.sqrt((wa*Fd[key]**2).sum())
    links=[(n,l) for n in range(0,N+1,2) for l in range(n+1)]; nL=len(links); li={x:i for i,x in enumerate(links)}
    Fm=np.array([Fd[x] for x in links])           # [nL, MA]
    Fp=(Fm[:,None,:]*Fm[None,:,:]*wa).reshape(nL*nL,MA)
    u,wu=np.polynomial.legendre.leggauss(64)
    s2=np.sin(a)**2; kmax=2*N
    Pk=np.array([np.polynomial.legendre.legval(u,[0]*kk+[1]) for kk in range(kmax+1)])
    expo=np.exp(-beta*s2[:,None,None]*s2[None,:,None]*(1-u**2)[None,None,:])   # e^{-V_ij/2}
    Tk={}
    for kk in range(0,kmax+1,2):
        g=(2*kk+1)/2*(expo*(wu*Pk[kk])).sum(-1)
        Tk[kk]=(Fp@g@Fp.T).reshape(nL,nL,nL,nL)       # [ia,ia',ib,ib']
    kap={n:besI(n+1,beta)/besI(1,beta) for n in range(0,N+1)}
    res={'mode':mode,'beta':beta,'N':N,'MA':MA,'sectors':{}}; ok=True
    for p,mult in [((0,0,0),1),((0,0,1),3),((1,1,0),3),((1,1,1),1)]:
        st=[(x,y,z) for x in links for y in links for z in links
            if (x[1]%2,y[1]%2,z[1]%2)==p and abs(x[1]-y[1])<=z[1]<=x[1]+y[1]]
        D=len(st); idx={s:i for i,s in enumerate(st)}
        Kd=np.array([kap[x[0]]*kap[y[0]]*kap[z[0]] for x,y,z in st])
        def pairmat(i,j,c):
            E=np.zeros((D,D))
            # group by spectator
            groups={}
            for r,s in enumerate(st): groups.setdefault(s[c],[]).append(r)
            for spec,rows in groups.items():
                L=spec[1]; rows=np.array(rows)
                ia=np.array([li[st[r][i]] for r in rows]); ib=np.array([li[st[r][j]] for r in rows])
                la=np.array([st[r][i][1] for r in rows]); lb=np.array([st[r][j][1] for r in rows])
                B=np.zeros((len(rows),len(rows)))
                for kk in Tk:
                    A=np.array([[pairA(int(la[x]),int(lb[x]),int(la[y]),int(lb[y]),L,kk) for y in range(len(rows))] for x in range(len(rows))])
                    if not A.any(): continue
                    B+=A*Tk[kk][ia[:,None],ia[None,:],ib[:,None],ib[None,:]]
                E[np.ix_(rows,rows)]=B
            return E
        if mode=='v0':
            M=np.diag(Kd)
        else:
            A=pairmat(0,1,2)
            if mode=='full': A=A@pairmat(0,2,1)@pairmat(1,2,0)
            Ks=np.sqrt(Kd); M=(Ks[:,None]*A)@(A.T*Ks[None,:])
        asym=float(np.abs(M-M.T).max()/np.abs(M).max()); ev=np.linalg.eigvalsh((M+M.T)/2)[::-1]
        res['sectors'][str(p)]={'dim':D,'mult':mult,'asym':asym,'lam':ev[:10].tolist(),'lam_min':float(ev[-1])}
        if mode=='v0':
            ex=np.sort(Kd)[::-1]; res['sectors'][str(p)]['L1err']=float(np.abs(-np.log(ev/ex[0])+np.log(ex/ex[0])).max())
        print(p,D,ev[:4],time.time()-t0,flush=True)
    lam0=max(v['lam'][0] for v in res['sectors'].values())
    lev=sorted([( -math.log(l/lam0),k) for k,v in res['sectors'].items() for l in v['lam'] if l>0])
    res['levels']=lev[:16]; res['m_e']=lev[1][0] if len(lev)>1 else None
    res['L3']=bool(all(v['asym']<1e-12 and v['lam_min']>-1e-12*lam0 for v in res['sectors'].values()))
    if mode=='v0':
        res['L1']=bool(max(v['L1err'] for v in res['sectors'].values())<1e-12); ok&=res['L1']
    if mode=='full': ok&=res['L3']
    if mode=='dec':
        e000=[-math.log(l/lam0) for l in res['sectors']['(0, 0, 0)']['lam']]
        ref={2.0:1.63761996,4.0:0.76319885}.get(beta)
        if ref is not None:
            d=min(abs(e-ref) for e in e000); res['L2_diff']=d; res['L2']=bool(d<1e-4); ok&=res['L2']
    res['time']=time.time()-t0
    print('m_e',res['m_e'],{k:v for k,v in res.items() if k[:1]=='L'}); print(lev[:8])
    json.dump(res,f,indent=1); f.close(); sys.exit(0 if ok else 1)
main()
