"""Compact U(1) toy of u1toy.py / u1sector.py: the constant kappa = ||G H^-1 G|| in lattice units (a = 1), that is,
the best constant in G <= kappa H, by dense diagonalisation in each flux sector (H = -log That).
Expectation written before the first run (quadratic approximation, two-dimensional analogue of the free-theory
limit of the proposition on the fine detail and the energy): kappa -> 1/arcosh(3) + 1/(2 sqrt 2) = 0.9208 as
beta -> infinity; no expectation at finite beta except kappa < 1.
PREDICATES (fixed before the first run):
 D1 (control, known answer, first) with M = 1, beta = 1, n = 8: kappa = max over h != 0, |w_i| <= 2 of
    1/(-log(kappa_K(h,w)/kappa_K(0))) to 1e-9, kappa_K the Fourier multiplier.
 D2 (cross-check) in the sector w = (1,0): the top eigenvalue and the weight 1 - |<Omega, psi>|^2 agree with the
    iterative values of u1sector.Sec at the same beta and n, to 1e-8.
 D3 (convergence) relative change of kappa between the two grids given for a coupling below
    10 I_{n1/2}(beta)/I_0(beta), or 1e-6 if that is below 1e-7.
Reported: kappa per coupling, the sector that attains it, the values in the sectors computed.
Sectors: (0,0),(1,0),(1,1),(2,0),(2,1),(3,0) (others are images of these under the symmetries or have more flux).
Usage: python3 u1kappa.py OUT beta:n1:n2 ...   (OUT is not overwritten)"""
import sys, numpy as np, scipy.fft as sf, scipy.special as sp, scipy.linalg as sl
sys.argv_keep=sys.argv; sys.argv=['x']; import u1sector as u; sys.argv=sys.argv_keep
def dense(m,w):
    N=m.N; I=np.eye(N).reshape((N,)+(m.n,)*3)
    X=sf.ifftn(m.kap(w)[None]*sf.fftn(I*m.M[None],axes=(1,2,3)),axes=(1,2,3))*m.M[None]
    T=X.reshape(N,N).T/m.L0; return (T+T.conj().T)/2
def kappa_sector(m,w):
    ev,V=sl.eigh(dense(m,w)); ev=np.clip(ev,1e-300,None)
    if w==(0,0):
        i=np.argmax(ev); keep=np.ones(len(ev),bool); keep[i]=False; ev=ev[keep]; V=V[:,keep]
    c=V.conj().T@m.Om                                  # Q = I - |Om><Om|
    Hinv=1/(-np.log(np.minimum(ev,1-1e-15)))
    # Q H^-1 Q = V Hinv V* - (V Hinv c) Om* - Om (V Hinv c)* + Om (c* Hinv c) Om*
    A=(V*Hinv)@V.conj().T; b=V@(Hinv*c); s=np.real(np.vdot(c,Hinv*c))
    A=A-np.outer(b,m.Om)-np.outer(m.Om,b.conj())+s*np.outer(m.Om,m.Om)
    top=sl.eigh((A+A.conj().T)/2,eigvals_only=True,subset_by_index=[len(A)-1,len(A)-1])[0]
    return top, ev.max(), 1-abs(c[np.argmax(ev)])**2
if __name__=='__main__':
    out=[]; secs=[(0,0),(1,0),(1,1),(2,0),(2,1),(3,0)]
    m=u.Sec(1.0,8,magnetic=False); m.vacuum()
    ws=[(a,b) for a in range(-2,3) for b in range(-2,3)]; got=max(kappa_sector(m,w)[0] for w in ws)
    mask=(m.H[0]!=0)|(m.H[1]!=0)|(m.H[2]!=0); exact=max((1/(-np.log(m.kap(w)[mask]))).max() for w in ws)
    out.append("D1 control: %.10f exact %.10f : %s"%(got,exact,"MET" if abs(got-exact)<1e-9 else "FAILED"))
    out.append("expectation for large beta: %.4f"%(1/np.arccosh(3)+1/(2*np.sqrt(2))))
    D2=D3=True
    for spec in sys.argv[2:]:
        beta,n1,n2=spec.split(':'); beta=float(beta); res=[]
        for n in (int(n1),int(n2)):
            m=u.Sec(beta,n); m.vacuum(); r={w:kappa_sector(m,w) for w in secs}
            wb=max(r,key=lambda w:r[w][0]); res.append(r[wb][0])
            vals,vecs=m.top((1,0)); wt=1-abs(m.Om@vecs[:,0])**2
            d2=abs(vals[0]-r[(1,0)][1])<1e-8 and abs(wt-r[(1,0)][2])<1e-8; D2&=d2
            out.append("beta %.2f n %d: kappa = %.8f in sector %s ; by sector: %s%s"%(beta,n,r[wb][0],wb," ".join("%s %.6f"%(w,r[w][0]) for w in secs),"" if d2 else " D2-FAILED"))
        tolr=10*sp.iv(int(n1)//2,beta)/sp.iv(0,beta)
        if tolr<1e-7: tolr=1e-6
        rel=abs(res[0]-res[1])/res[1]; D3&=rel<tolr
        out.append("beta %.2f: relative change %.2e (tolerance %.2e)%s"%(beta,rel,tolr,"" if rel<tolr else " D3-FAILED"))
    out.append("D2 %s"%("MET" if D2 else "FAILED")); out.append("D3 %s"%("MET" if D3 else "FAILED"))
    open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out))
