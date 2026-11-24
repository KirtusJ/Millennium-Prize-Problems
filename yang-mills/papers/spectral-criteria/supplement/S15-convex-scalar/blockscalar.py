"""Block averages of a massless free scalar field on Z^d (fine mesh 1, blocks of side r): the two constants of the
bound of the fine detail by the energy.
  lambda_N = inf over fields n with zero mean on every block of <n, omega n>/<n, n>,  omega = (-Laplacian)^(1/2);
  kappa_free = sup over the same n of <n, omega n>/<n, omega^2 n>  (the exact free constant, one-particle).
Both are computed per coarse momentum k in the Brillouin zone of the coarse lattice (a grid of G^d points including
k = 0 and the zone boundary), where the constraint is one linear condition on the r^d aliases.
PREDICATES (fixed before the first run).
  B1 (theorem to be checked) lambda_N >= 2 sin(pi/(2r)) for every d, r, k computed.
  B2 (Cauchy-Schwarz) kappa_free <= 1/lambda_N at every k.
  B3 (control, k = 0, where the constraint removes exactly the zero alias) lambda_N(k=0) = 2 sin(pi/r) to 1e-12.
Reported: r * lambda_N (min over k) and kappa_free / r (max over k), and where the extremes sit.
Usage: python3 blockscalar.py OUT"""
import sys, itertools, numpy as np, scipy.linalg as sl
out=[]; B1=B2=B3=True
for d,rs,G in ((1,(2,3,4,6,8,16),65),(2,(2,3,4,6,8),17),(3,(2,3,4,6),7)):
    for r in rs:
        js=np.array(list(itertools.product(range(r),repeat=d)))
        best=(9e9,None); worst=(0,None)
        kk=np.linspace(0,np.pi/r,G)
        for kt in itertools.combinations_with_replacement(range(G),d):
            k=kk[list(kt)]; p=k[None,:]+2*np.pi*js/r
            om=2*np.sqrt((np.sin(p/2)**2).sum(axis=1))
            with np.errstate(divide='ignore',invalid='ignore'):
                S=np.prod(np.where(abs(np.exp(1j*p)-1)<1e-13,r,(1-np.exp(1j*p*r))/(1-np.exp(1j*p))),axis=1)
            s=S/np.linalg.norm(S); Q,_=np.linalg.qr(np.column_stack([s,np.eye(len(s))[:,:len(s)-1]]).astype(complex)); 
            Z=sl.null_space(s.conj()[None,:])            # orthonormal basis of the constraint space
            A=Z.conj().T@(om[:,None]*Z); A=(A+A.conj().T)/2; B=Z.conj().T@((om**2)[:,None]*Z); B=(B+B.conj().T)/2
            lam=np.linalg.eigvalsh(A)[0]
            kap=sl.eigvalsh(A,B)[-1] if np.linalg.eigvalsh(B)[0]>1e-12 else np.inf
            B1&=lam>=2*np.sin(np.pi/(2*r))-1e-10; B2&=kap<=1/lam+1e-10
            if all(t==0 for t in kt): B3&=abs(lam-2*np.sin(np.pi/r))<1e-12
            if lam<best[0]: best=(lam,k*r/np.pi)
            if kap>worst[0]: worst=(kap,k*r/np.pi)
        out.append("d=%d r=%2d: r*lambda_N = %.6f at k r/pi = %s ; r*2sin(pi/2r) = %.6f ; kappa_free/r = %.6f at k r/pi = %s ; 1/(r lambda_N) = %.6f"%(d,r,r*best[0],np.round(best[1],3),r*2*np.sin(np.pi/(2*r)),worst[0]/r,np.round(worst[1],3),1/(r*best[0]))); print(out[-1],flush=True)
for nm,v in (("B1",B1),("B2",B2),("B3",B3)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-3:]))
