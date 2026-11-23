import numpy as np
# Gauss-Legendre on [0,pi]; sqrt singularity at endpoints handled by substitution a=pi*(1-cos t)/2... use a=pi*sin^2(u/..)
n=4000
x,w=np.polynomial.legendre.leggauss(n)
# substitute a = pi*(1-cos(pi s))/2, s in[0,1], da = pi^2/2 sin(pi s) ds ; smooths endpoint sqrt
s=(x+1)/2; ws=w/2
a=np.pi*(1-np.cos(np.pi*s)); a=a/2
da=np.pi**2/2*np.sin(np.pi*s)
v=np.sqrt(2*2*np.arcsinh(np.sin(a)))
print("%.6f"%np.sum(ws*da*v))
