"""Control: c* = int_0^pi sqrt(2*eps(a)) da, eps=2*asinh(sin a).
Predicate: result written to control.txt (4 decimals); Gauss-Legendre with a=pi(1-cos t)/2 (n=200 and n=400 agree to 1e-8, tolerance from quadrature convergence)."""
import numpy as np
def q(n):
    x,w=np.polynomial.legendre.leggauss(n); t=(x+1)*np.pi/2; w=w*np.pi/2
    a=np.pi*(1-np.cos(t))/2; da=np.pi/2*np.sin(t)
    return np.sum(w*da*np.sqrt(4*np.arcsinh(np.sin(a))))
c1,c2=q(200),q(400); print(c1,c2); assert abs(c1-c2)<1e-8
with open("control.txt","x") as f: f.write("%.4f\n"%c2)
