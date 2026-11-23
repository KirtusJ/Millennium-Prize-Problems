"""Control. Predicates: |int x^2 e^-x - 2|<1e-12 ; I1(2)/I0(2) = 0.697775 to 6 dp (known 0.6977746579...)."""
import numpy as np
x,w=np.polynomial.laguerre.laggauss(20); a=(w*x**2).sum()
t=(np.arange(4000)+.5)*np.pi/4000
I=lambda n:(np.exp(2*(np.cos(t)-1))*np.cos(n*t)).mean()
b=I(1)/I(0)
assert abs(a-2)<1e-12 and abs(b-0.6977746579)<1e-6,(a,b)
open('control.txt','x').write('%.6f\n%.6f\n'%(a,b))
