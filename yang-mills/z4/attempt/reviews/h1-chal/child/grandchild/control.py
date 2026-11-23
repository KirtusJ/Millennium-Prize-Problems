import numpy as np, math
x,w=np.polynomial.laguerre.laggauss(20)
gl=float(np.sum(w*x**2))
def I(n,x):
    return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(60))
r=I(1,2.0)/I(0,2.0)
open('control.txt','x').write(f"gauss_laguerre_x2exp(-x) {gl:.12f} (exact 2)\nI1(2)/I0(2) {r:.6f} (expected 0.697775)\n")
