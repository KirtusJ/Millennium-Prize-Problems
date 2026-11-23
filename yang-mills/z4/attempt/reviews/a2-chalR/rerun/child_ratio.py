"""R(m)=C(xi/2)/C(xi) for free lattice scalar, 3D periodic-trapezoid quadrature.
PREDICATES (fixed before first run):
 P0 continuum Rc by own quadrature agrees with 2*K1(.5)/K1(1)-type value computed by independent
    quadrature of K1 integral rep (tol 1e-6, quadrature error scale).
 P1 grid convergence: for each m, |R(N)-R(N2)|/R < 1e-6 where N2=1.25N (tol: aliasing e^{-N/xi}<=1e-7 plus fp).
 P2 boundedness: R(m) <= D=10 for every m tested (D chosen as ~2x Rc; my choice). Report #cases qualifying.
 P3 (my expectation) |R(m)-Rc| decreases monotonically as m decreases, and |R-Rc|/Rc<0.05 at smallest m.
 P4 R2 = R^2 (identity, tol 1e-12).
Grid: N = ceil(Nfac*xi) rounded even, midpoint-free trapezoid p=2pi k/N, octant symmetry.
"""
import numpy as np, sys, math
def omega_m(m): return math.acosh(1+m*m/2)
def C_pair(m,N,times):
    # trapezoid on torus N^3 using k in [0,N/2] with weights 1 (0,N/2 weight 1, others 2)
    h=N//2
    k=np.arange(h+1); w=np.where((k==0)|(k==h),1.0,2.0)
    s1=4*np.sin(np.pi*k/N)**2
    out=np.zeros(len(times))
    for i in range(h+1):
        a=m*m+s1[i]+s1[:,None]+s1[None,:]   # (h+1,h+1)
        om=np.arccosh(1+a/2)
        W=w[i]*w[:,None]*w[None,:]
        den=2*np.sinh(om)
        for j,t in enumerate(times):
            out[j]+=np.sum(W*np.exp(-t*om)/den)
    return out/N**3
def Rm(m,fac):
    xi=1/omega_m(m); N=int(math.ceil(fac*xi/2)*2); N=max(N,16)
    c=C_pair(m,N,[xi/2,xi]); return c[0]/c[1],c,N,xi
def simpson(f,a,b,n=200000):
    x=np.linspace(a,b,n+1); y=f(x); h=(b-a)/n
    return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
def J(a): # int_1^inf sqrt(E^2-1)e^{-aE}; sub E=cosh u: int sinh^2 u e^{-a cosh u}du
    return simpson(lambda u: np.sinh(u)**2*np.exp(-a*np.cosh(u)),0,60/ (1) if a>=1 else 60,400000)
if __name__=="__main__":
    ms=[float(x) for x in sys.argv[1:]] or [0.4,0.2,0.1,0.05,0.025]
    Rc=J(.5)/J(1.0)
    # independent: K1(a)=int_0^inf e^{-a cosh t}cosh t dt ; J(a)=K1(a)/a
    K1=lambda a: simpson(lambda t:np.exp(-a*np.cosh(t))*np.cosh(t),0,60,400000)
    Rc2=(K1(.5)/.5)/(K1(1.0)/1.0)
    print("Rc",repr(Rc),"Rc_K1",repr(Rc2),"P0",abs(Rc-Rc2)<1e-6,flush=True)
    for m in ms:
        r1,c1,N1,xi=Rm(m,14); r2,c2,N2,_=Rm(m,17.5)
        print(f"m={m} M={omega_m(m):.8g} xi={xi:.6g} N1={N1} N2={N2} R={r2:.9f} R1={r1:.9f} relgrid={abs(r1-r2)/r2:.2e} C(xi/2)={c2[0]:.6e} C(xi)={c2[1]:.6e} R2={r2*r2:.9f} P1={abs(r1-r2)/r2<1e-6}",flush=True)
