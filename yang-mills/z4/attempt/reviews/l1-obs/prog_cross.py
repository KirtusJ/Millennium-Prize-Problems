"""l1-obs: order of the slow/hard cross term in one plaquette.
Links exp(h X_i + s z_l), s=h^{3/2}, beta=h^-3, plaquette P=U1(x)U2(x+e1)U1(x+e2)^-1 U2(x)^-1, Z=z1(x)+z2(x+e1)-z1(x+e2)-z2(x).
Y = beta|ImP|^2/(1+ReP).
PREDICATE Q1 (fixed before run): D(h) = (Y - |Z|^2/2)/h^{1/2} - 2 Z.(X1xX2) satisfies |D| -> 0 with ratio |D(h)|/|D(h/100)| in [5,20]
  (next corrections O(h^{1/2}) relative: factor 10 per factor 100 in h; tol factor 2) for h=1e-2,1e-4,1e-6 (seed 7 for z).
MEASURED: D at each h; the coefficient 2Z.(X1xX2).
"""
import numpy as np, math, sys
def qmul(p,q):
    a1,b1=p[0],p[1:];a2,b2=q[0],q[1:]
    return np.concatenate([[a1*a2-b1@b2],a1*b2+a2*b1+np.cross(b1,b2)])
def qexp(v):
    r=np.linalg.norm(v);return np.concatenate([[math.cos(r)],math.sin(r)/r*v])
def qinv(q):return q*np.array([1,-1,-1,-1])
rng=np.random.default_rng(7);z=rng.normal(size=(4,3))  # z1(x),z2(x+e1),z1(x+e2),z2(x)
X1=np.array([.7,-.2,.4]);X2=np.array([-.3,.9,.5])
Z=z[0]+z[1]-z[2]-z[3];lead=2*Z@np.cross(X1,X2);Ds=[]
for h in (1e-2,1e-4,1e-6):
    s=h**1.5
    P=qmul(qmul(qexp(h*X1+s*z[0]),qexp(h*X2+s*z[1])),qmul(qinv(qexp(h*X1+s*z[2])),qinv(qexp(h*X2+s*z[3]))))
    Y=h**-3*(P[1:]@P[1:])/(1+P[0]);D=(Y-Z@Z/2)/h**.5-lead;Ds.append(abs(D))
    print(f"h={h:g}: Y={Y:.12f} |Z|^2/2={Z@Z/2:.12f} (Y-|Z|^2/2)/sqrt(h)={(Y-Z@Z/2)/h**.5:.8f} 2Z.(X1xX2)={lead:.8f} D={D:.3e}")
r1,r2=Ds[0]/Ds[1],Ds[1]/Ds[2];ok=5<=r1<=20 and 5<=r2<=20
print(f"Q1: {'MET' if ok else 'FAILED'} ratios {r1:.2f} {r2:.2f}");print(f"COUNTS met={int(ok)} failed={int(not ok)} measured=1")
sys.exit(0 if ok else 1)
