import numpy as np
# <a0> = I2(1)/I1(1); series for I_n and independent quadrature
from math import factorial
def I(n,x): return sum((x/2)**(2*k+n)/(factorial(k)*factorial(k+n)) for k in range(30))
print("series %.6f"%(I(2,1)/I(1,1)))
x=np.linspace(-1,1,2000001); w=np.sqrt(1-x*x)*np.exp(x)
print("quad   %.6f"%(np.trapezoid(x*w,x)/np.trapezoid(w,x)))
