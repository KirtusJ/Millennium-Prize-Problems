"""Control: integral of x^2 e^x on [0,1] by Gauss-Legendre n=20; predicate: matches e-2 to 1e-6."""
import numpy as np
x,w=np.polynomial.legendre.leggauss(20); x=(x+1)/2; v=(w/2*x**2*np.exp(x)).sum()
assert abs(v-(np.e-2))<1e-6
with open('control.txt','x') as f: f.write("%.6f\n"%v)
