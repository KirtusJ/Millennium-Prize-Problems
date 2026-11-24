"""A non-Gaussian, compact test of the weighted (directional) form of the sufficient condition in the remark on
Hypothesis h:mix. It is a toy with two U(1) links, not a gauge theory and not evidence about SU(2).
Model. X = (x_1, x_2), Y = (y_1, y_2), each entry a unit vector in R^2 with angle th_e (for X) or a_e (for Y).
Joint density  phi(X) exp(beta (x_1.y_1 + x_2.y_2)) phi(Y) / Z  with respect to the product of arc lengths;
phi = exp(random trigonometric polynomial of degree <= 2 in the two angles), symmetric joint law as in the paper.
Coarse field C = th_1 + th_2 (mod 2 pi). Fibre: th_1 = t, th_2 = c - t; unit tangent in R^4:
tau = (-sin th_1, cos th_1, sin th_2, -cos th_2)/sqrt 2.  Sigma_x = Cov(Y | X = x), a 4x4 matrix.
Quantities at a coarse value c:
 rho2  = squared maximal correlation of X and Y given C = c (second singular value of the conditional kernel)
 Pc    = Poincare constant of the fibre law, Var(h) <= Pc E|grad h|^2, |grad h|^2 = (dh/dt)^2 / 2
 Lc    = sup_x ||Sigma_x||          Dc = sup_x tau^T Sigma_x tau
 Pw    = best constant in Var(h) <= Pw E[ |grad h|^2 / (tau^T Sigma_x tau) ]
 B(z)  = z/(1+z)
PREDICATES (fixed before the first run), for every instance (seeds 0..5, beta in {0.5, 2, 5}, c in {0, 1.3, 3.0}):
 W1 rho2 <= B(beta^2 Pw) + tol
 W2 B(beta^2 Pw) <= B(beta^2 Pc Dc) + tol <= B(beta^2 Pc Lc) + 2 tol
 W3 (identity used in the proof) at three points x and a random trigonometric g: the numerical derivative of
    h(x) = E[g(Y)|X=x] along tau equals beta Cov(g(Y), tau.Y | X=x) to 1e-6 (central difference, step 1e-4).
 Control (known answer, answered first): with phi = 1 the components of Y given X are independent von Mises
    vectors and tau^T Sigma_x tau = I_1(beta)/(beta I_0(beta)) at every x; checked to 1e-10 at beta = 2.
tol = 1e-7. Basis: the integrands are analytic and periodic, so the trapezoid rule converges geometrically; the
program recomputes every quantity on a grid of 48 instead of 64 points per angle and reports the largest change,
which must itself be below tol (reported as W0).
Seeds fixed. Output weightedtoy_result.txt (not overwritten). Command: python3 weightedtoy.py"""
import numpy as np, scipy.linalg as sl, scipy.special as sp
def trig(rng):
    co=rng.normal(size=(5,5))*0.35
    return lambda a,b: sum(co[i+2,j+2]*np.cos(i*a+j*b+ (i*3+j)*0.7) for i in range(-2,3) for j in range(-2,3))
def setup(n,beta,lphi):
    ang=2*np.pi*np.arange(n)/n; A,Bg=np.meshgrid(ang,ang,indexing='ij')
    phiY=np.exp(lphi(A,Bg)); Yv=np.stack([np.cos(A),np.sin(A),np.cos(Bg),np.sin(Bg)],-1).reshape(-1,4)
    return ang,phiY.reshape(-1),Yv,A.reshape(-1),Bg.reshape(-1)
def condY(beta,th1,th2,phiY,A,Bg):
    w=np.exp(beta*(np.cos(th1-A)+np.cos(th2-Bg)-2))*phiY; return w/w.sum(),w.sum()
def quantities(n,beta,lphi,c):
    ang,phiY,Yv,A,Bg=setup(n,beta,lphi)
    t=ang; K=np.zeros((n,n*n)); dens=np.zeros(n); tst=np.zeros(n); nrm=np.zeros(n)
    for i,ti in enumerate(t):
        th1,th2=ti,c-ti; p,Z=condY(beta,th1,th2,phiY,A,Bg)
        fx=np.exp(lphi(np.array(th1),np.array(th2)))*Z      # density of X on the fibre (up to a constant)
        dens[i]=fx; K[i]=fx*p
        m=p@Yv; S=(Yv*p[:,None]).T@Yv-np.outer(m,m)
        tau=np.array([-np.sin(th1),np.cos(th1),np.sin(th2),-np.cos(th2)])/np.sqrt(2)
        tst[i]=tau@S@tau; nrm[i]=np.linalg.eigvalsh(S).max()
    K/=K.sum(); pt=K.sum(1); qy=K.sum(0)
    s=np.linalg.svd(K/np.sqrt(np.outer(pt,qy)),compute_uv=False); rho2=s[1]**2
    rho_=dens/dens.sum()
    # Rayleigh-Ritz in a trigonometric basis of degree < n/2 for  int w h'^2 = lam int rho h^2  (h centred)
    kk=np.arange(1,n//2); Bc=np.cos(np.outer(t,kk)); Bs=np.sin(np.outer(t,kk)); Bf=np.hstack([Bc,Bs])
    dB=np.hstack([-Bs*kk,Bc*kk]); Bf=Bf-(rho_@Bf)
    def gap(w):
        Sm=dB.T@(dB*(w*rho_)[:,None]); Mm=Bf.T@(Bf*rho_[:,None])
        return sl.eigh(Sm,Mm,eigvals_only=True,subset_by_index=[0,0])[0]
    Pc=1/gap(np.full(n,0.5)); Pw=1/gap(0.5/tst)
    return np.array([rho2,Pc,nrm.max(),tst.max(),Pw])
B=lambda z: z/(1+z)
out=[]; tol=1e-7
# control
ang,phiY,Yv,A,Bg=setup(64,2.0,lambda a,b:0*a); p,_=condY(2.0,0.4,1.1,phiY,A,Bg); m=p@Yv; S=(Yv*p[:,None]).T@Yv-np.outer(m,m)
tau=np.array([-np.sin(0.4),np.cos(0.4),np.sin(1.1),-np.cos(1.1)])/np.sqrt(2)
ctrl=abs(tau@S@tau-sp.iv(1,2.0)/(2.0*sp.iv(0,2.0))); out.append("control |tau.Sigma.tau - I1/(beta I0)| = %.2e %s"%(ctrl,"MET" if ctrl<1e-10 else "FAILED"))
W0=W1=W2=W3=True; worst0=0
for seed in range(6):
    rng=np.random.default_rng(seed); lphi=trig(rng); g=trig(rng)
    for beta in (0.5,2.0,5.0):
        for c in (0.0,1.3,3.0):
            q=quantities(64,beta,lphi,c); q48=quantities(48,beta,lphi,c); ch=np.abs(q-q48).max(); worst0=max(worst0,ch)
            rho2,Pc,Lc,Dc,Pw=q; b1,b2,b3=B(beta**2*Pw),B(beta**2*Pc*Dc),B(beta**2*Pc*Lc)
            w1=rho2<=b1+tol; w2=(b1<=b2+tol) and (b2<=b3+2*tol); W1&=w1; W2&=w2; W0&=ch<tol
            out.append("seed %d beta %.1f c %.1f rho2=%.6f B(Pw)=%.6f B(Pc Dc)=%.6f B(Pc Lc)=%.6f  beta*Pc=%.4f beta*Lc=%.4f beta*Dc=%.4f grid change %.1e %s%s"%(seed,beta,c,rho2,b1,b2,b3,beta*Pc,beta*Lc,beta*Dc,ch,"" if w1 else " W1-FAILED","" if w2 else " W2-FAILED"))
        ang,phiY,Yv,A,Bg=setup(64,beta,lphi); gy=g(A,Bg)
        for (th1,th2) in ((0.3,2.0),(4.0,5.5),(1.0,1.0)):
            tau=np.array([-np.sin(th1),np.cos(th1),np.sin(th2),-np.cos(th2)])/np.sqrt(2); e=1e-4
            hp=condY(beta,th1+e/np.sqrt(2),th2-e/np.sqrt(2),phiY,A,Bg)[0]@gy; hm=condY(beta,th1-e/np.sqrt(2),th2+e/np.sqrt(2),phiY,A,Bg)[0]@gy
            p=condY(beta,th1,th2,phiY,A,Bg)[0]; ty=Yv@tau; cov=p@(gy*ty)-(p@gy)*(p@ty)
            d=abs((hp-hm)/(2*e)-beta*cov); W3&=d<1e-6
            if d>=1e-6: out.append("W3-FAILED seed %d beta %.1f x=(%.1f,%.1f) diff %.2e"%(seed,beta,th1,th2,d))
out.append("largest grid change %.2e"%worst0)
for n,m in zip("W0 W1 W2 W3".split(),(W0,W1,W2,W3)): out.append("%s %s"%(n,"MET" if m else "FAILED"))
open('weightedtoy_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
