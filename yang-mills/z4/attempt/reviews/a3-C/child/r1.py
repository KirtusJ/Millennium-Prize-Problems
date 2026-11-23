"""R1/R2 lattice vs continuum. Predicates fixed before first run:
P1 control.txt == 0.601907 (K_1(1)).
P2 per xi: R1 at resolutions N=80 and N=120 agree to rel 1e-9 (tolerance = stated difference; origin: smooth integrand, Gauss-Legendre in s with k=pi s^4 map, expected spectral convergence).
P3 R1 bounded: 1<R1<10 for all 6 xi.
P4 rel. deviation |R1/R1c-1| strictly decreases with xi over the 5 consecutive pairs.
P5 deviation at xi=128 < 1% (own expectation, lattice artefacts O(1/xi) at fixed n/xi).
P6 R2 == R1^2 to 1e-12 (identity, C2=2G^2).
Result file opened with mode 'x'. No randomness (no seed needed)."""
import numpy as np, sys
t=np.linspace(0,14,2800001); h=t[1]-t[0]
def K1(x):
    y=np.exp(-x*np.cosh(t))*np.cosh(t); return h*(y.sum()-0.5*(y[0]+y[-1]))
def Gs(xi,N):
    M2=2*(np.cosh(1/xi)-1)
    x,w=np.polynomial.legendre.leggauss(N); s=(x+1)/2; w=w/2
    k=np.pi*s**4; dk=4*np.pi*s**3*w   # octant [0,pi]^3; factor 8/(2pi)^3
    S=4*np.sin(k/2)**2
    p2=S[:,None,None]+S[None,:,None]+S[None,None,:]
    om=np.arccosh(1+(M2+p2)/2)
    W=dk[:,None,None]*dk[None,:,None]*dk[None,None,:]
    out=[]
    for n in (xi//2,xi):
        out.append(8/(2*np.pi)**3*np.sum(W*np.exp(-n*om)/(2*np.sinh(om))))
    return out
ctl=float(open("control.txt").read()); res=[]
Rc=2*K1(0.5)/K1(1.0)
lines=[f"control K1(1)={ctl}  P1 {'met' if '%.6f'%ctl=='0.601907' else 'FAILED'}",f"continuum 2K1(1/2)/K1(1)={Rc:.8f}",
"xi R1(N=80) R1(N=120) |diff|/R1  R2  reldev"]
devs=[];ok2=True;ok3=True;ok6=True
for xi in (4,8,16,32,64,128):
    a=Gs(xi,80); b=Gs(xi,120)
    ra=a[0]/a[1]; rb=b[0]/b[1]; d=abs(ra-rb)/rb; R2=(b[0]*b[0]*2)/(b[1]*b[1]*2)
    dev=rb/Rc-1; devs.append(abs(dev))
    ok2&=d<1e-9; ok3&=1<rb<10; ok6&=abs(R2-rb*rb)<1e-12*R2
    lines.append(f"{xi} {ra:.10f} {rb:.10f} {d:.2e} {R2:.8f} {dev:+.6e}")
dec=[devs[i+1]<devs[i] for i in range(5)]
lines+= [f"P2 {'met' if ok2 else 'FAILED'}",f"P3 {'met' if ok3 else 'FAILED'}",
 f"P4 decreasing pairs {sum(dec)}/5 -> {'met' if all(dec) else 'FAILED'}",
 f"P5 {'met' if devs[-1]<0.01 else 'FAILED'} (dev={devs[-1]:.3e})",f"P6 {'met' if ok6 else 'FAILED'}"]
if len(sys.argv)>1:
    with open(sys.argv[1],"x") as f: f.write("\n".join(lines)+"\n")
print("\n".join(lines))
