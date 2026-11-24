"""Discrete time: the transfer operator of a scalar lattice field with a convex interaction,
  T = exp(-a W/2) exp(a Laplacian/2) exp(-a W/2),  W = (1/2)<phi, K phi> + V(phi),
normalised to That = T / (top eigenvalue) in the vacuum representation; P = functions of the block variables B phi
times the vacuum, Q = I - P on the centred functions, N = ker B.
Statement under test: for every convex V,   I - That^2 >= gamma_0 Q   with the free value
  1/gamma_0 = 1 + sup over n in N of <n, (a^2 A2)^-1 n> / <n, 2 wt n>,
  wt = (K + a^2 K^2/4)^(1/2),  A2 = 1/a + a K/2 + wt.
gamma_opt = 1/||Q (I - That^2)^-1 Q|| is computed by dense diagonalisation of T on a grid (rotated coordinates in
which the block variables are grid axes).
 System A: two sites, K = m^2 + k[[1,-1],[-1,1]], block variable phi1 + phi2; grid 72 x 72 on [-7.5, 7.5]^2.
 System B: three sites, open chain, block variables phi1 + phi2 and phi3; grid 22^3 on [-4.6, 4.6]^3 (coarse).
m^2 = 0.25, k = 1; time steps a = 1 and a = 0.5.
PREDICATES (fixed before the first run).
 Controls (free field). The value of gamma_0 was derived by two routes before fixing it: from the proposition on the
 directional form with the fibre covariance as weight, and from the one-particle contraction r = (a A2)^-1 of the
 Gaussian model, for which 1/gamma_opt = sup over n in N of <n, wt (1 - r^2)^-1 n>/<n, wt n>; the two agree by
 a^2 A2^2 - 1 = 2 a^2 wt A2.
  D1 system A, V = 0: gamma_opt = gamma_0 = 1 - r(m^2 + 2k)^2 to relative 1e-5, for both a.
  D2 system B, V = 0: gamma_opt = gamma_0 to relative 5e-3 (the grid is coarse), for both a.
 The statement:
  D3 for each convex V in {quartic 0.1, 1, 10; cosh; (phi1-phi2)^4; (phi1+phi2)^4; |phi1|+|phi2|} and both a:
     gamma_opt >= gamma_0 (1 - 1e-5) in system A and gamma_opt >= gamma_0 (1 - 5e-3) in system B.
 Expectation outside the hypothesis:
  X1 for V = lam ((phi1 - phi2)^2 - v^2)^2 with (lam, v) = (0.25, 2): gamma_opt < gamma_0 in system A.
Usage: python3 convexstep.py OUT"""
import sys, numpy as np
m2=0.25; k=1.0
def setup(which,n,L,a):
    x=np.linspace(-L,L,n); h=x[1]-x[0]
    g1=np.exp(-(x[:,None]-x[None,:])**2/(2*a))/np.sqrt(2*np.pi*a)*h
    if which=='A':
        Y,Z=np.meshgrid(x,x,indexing='ij'); phis=((Y+Z)/np.sqrt(2),(Y-Z)/np.sqrt(2)); K=m2*np.eye(2)+k*np.array([[1,-1],[-1,1.]]); e=np.array([1,-1])/np.sqrt(2)
        Gk=np.kron(g1,g1); shape=(n,n)
    else:
        Y,Z,W=np.meshgrid(x,x,x,indexing='ij'); phis=((Y+Z)/np.sqrt(2),(Y-Z)/np.sqrt(2),W); K=m2*np.eye(3)+k*np.array([[1,-1,0],[-1,2,-1],[0,-1,1.]]); e=np.array([1,-1,0])/np.sqrt(2)
        Gk=np.kron(np.kron(g1,g1),g1); shape=(n,n,n)
    w,U=np.linalg.eigh(K); f=lambda fn: (U*fn(w))@U.T
    wt=f(lambda t: np.sqrt(t+a*a*t*t/4)); A2=np.eye(len(e))/a+a*K/2+wt
    z=(e@np.linalg.solve(a*a*A2,e))/(2*e@wt@e)
    quad=0.5*sum(K[i,j]*phis[i]*phis[j] for i in range(len(e)) for j in range(len(e)))
    return dict(phis=phis,quad=quad,Gk=Gk,shape=shape,g0=1/(1+z),a=a)
def gamma_opt(S,V):
    a=S['a']; D=np.exp(-0.5*a*(S['quad']+V)).ravel(); T=(D[:,None]*S['Gk'])*D[None,:]; T=(T+T.T)/2
    ev,Vv=np.linalg.eigh(T); ev=ev[::-1]; Vv=Vv[:,::-1]; Om=np.abs(Vv[:,0]); lam=np.clip(ev[1:]/ev[0],0,None); Vv=Vv[:,1:]
    A=Om.reshape(S['shape']); nrm=np.sqrt((A*A).sum(axis=1,keepdims=True)); F=A/np.where(nrm>0,nrm,1)
    def P(M): X=M.reshape(S['shape']+(-1,)); return (F[...,None]*(F[...,None]*X).sum(axis=1,keepdims=True)).reshape(M.shape)
    Wd=Vv*(1-lam**2)**-0.5              # columns: eigenvectors scaled; Q R Q = (Q Wd)(Q Wd)^T
    QW=Wd-P(Wd); QW-=np.outer(Om,Om@QW)
    s=np.linalg.svd(QW,compute_uv=False)[0]
    return 1/s**2, 1-lam[0]**2
cases=[("free",lambda p: 0*p[0],True),("quartic 0.1",lambda p: 0.1*sum(q**4 for q in p),True),("quartic 1",lambda p: sum(q**4 for q in p),True),
 ("quartic 10",lambda p: 10*sum(q**4 for q in p),True),("cosh",lambda p: sum(np.cosh(q)-1 for q in p),True),("(phi1-phi2)^4",lambda p: (p[0]-p[1])**4,True),
 ("(phi1+phi2)^4",lambda p: (p[0]+p[1])**4,True),("|phi1|+|phi2|",lambda p: abs(p[0])+abs(p[1]),True),
 ("fine double well 0.25, 2",lambda p: 0.25*((p[0]-p[1])**2-4)**2,False)]
out=[]; D1=D2=D3=True; X1=True
for which,n,L,tol in (('A',72,7.5,1e-5),('B',22,4.6,5e-3)):
    for a in (1.0,0.5):
        S=setup(which,n,L,a); out.append("system %s, a = %.1f: gamma_0 = %.8f"%(which,a,S['g0'])); print(out[-1],flush=True)
        for name,Vf,convex in cases:
            if which=='B' and not convex: continue
            g,full=gamma_opt(S,Vf(S['phis'])); line="  %-26s gamma_opt %.8f  ratio to gamma_0 %.6f  (1 - lambda_1^2 = %.6f)"%(name,g,g/S['g0'],full)
            if name=="free":
                ok=abs(g/S['g0']-1)<tol; line+=" control %s"%("MET" if ok else "FAILED")
                if which=='A': D1&=ok
                else: D2&=ok
            if convex:
                ok=g>=S['g0']*(1-tol); D3&=ok; line+="" if ok else " D3-FAILED"
            else: X1&=g<S['g0']
            out.append(line); print(line,flush=True)
for nm,v in (("D1",D1),("D2",D2),("D3",D3)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
out.append("X1 %s"%("as expected" if X1 else "NOT as expected"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-4:]))
