"""l1-obs v2 of P9 (first version failed: own expectation + cancellation).
PREDICATE P9b (fixed before run): constant-field plaquette, Y = beta|ImP|^2/(1+ReP) (exact identity for unit quaternion),
beta=h^-3. ratio Y/(2h|X1xX2|^2) - 1 is O(h^2): error ratio between h=0.1,0.01 and 0.01,0.001 both in [50,200]
[tol: factor 100 expected for pure h^2; +-factor 2 allows next order]. Also report the cross-term order h^{1/2}
(beta^{1/2} h^2 = h^{1/2}) measured only.
"""
import numpy as np, math, sys
def qmul(p,q):
    a1,b1=p[0],p[1:];a2,b2=q[0],q[1:]
    return np.concatenate([[a1*a2-b1@b2],a1*b2+a2*b1+np.cross(b1,b2)])
def qexp(v):
    r=np.linalg.norm(v);return np.concatenate([[math.cos(r)],math.sin(r)/r*v])
def qinv(q):return q*np.array([1,-1,-1,-1])
X1=np.array([.7,-.2,.4]);X2=np.array([-.3,.9,.5]);errs=[]
for h in (1e-1,1e-2,1e-3):
    U1,U2=qexp(h*X1),qexp(h*X2)
    P=qmul(qmul(U1,U2),qmul(qinv(U1),qinv(U2)))
    Y=h**-3*(P[1:]@P[1:])/(1+P[0]);ref=2*h*np.cross(X1,X2)@np.cross(X1,X2)
    errs.append(abs(Y/ref-1));print(f"h={h}: Y={Y:.10e} ref={ref:.10e} rel={Y/ref-1:.4e}  cross-term scale h^0.5={h**.5:.3e}")
r1,r2=errs[0]/errs[1],errs[1]/errs[2]
ok=50<=r1<=200 and 50<=r2<=200
print(f"P9b: {'MET' if ok else 'FAILED'} error ratios {r1:.2f} {r2:.2f}")
print(f"COUNTS met={int(ok)} failed={int(not ok)} measured=1")
sys.exit(0 if ok else 1)
