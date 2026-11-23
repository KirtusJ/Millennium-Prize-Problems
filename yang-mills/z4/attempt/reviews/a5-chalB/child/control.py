"""Predicate: <cos a> at beta=1 under density (2/pi) sin^2 a e^{cos a}, Gauss-Legendre 400 nodes;
must agree with I_2(1)/I_1(1) from the power series to 1e-9 (tolerance: quadrature error of an analytic
integrand, far below 1e-6 print precision). Writes control.txt (mode x)."""
import numpy as np, math
x,w=np.polynomial.legendre.leggauss(400); a=(x+1)*math.pi/2; w=w*math.pi/2
d=np.sin(a)**2*np.exp(np.cos(a)); q=(w*d*np.cos(a)).sum()/(w*d).sum()
def I(n,z): return sum((z/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(40))
ex=I(2,1)/I(1,1)
assert abs(q-ex)<1e-9,(q,ex)
with open("control.txt","x") as f: f.write("%.6f\n"%q)
print(q,ex)
