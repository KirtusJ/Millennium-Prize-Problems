"""Control: Z(1) via periodic trapezoid (no scipy available). Predicate: matches 2*I1(1) series to 1e-12."""
import numpy as np, math
N=2000; t=2*np.pi*np.arange(N)/N
v=(2/np.pi)*0.5*np.sum(np.exp(np.cos(t))*np.sin(t)**2)*2*np.pi/N
ser=2*sum((0.5)**(2*k+1)/(math.factorial(k)*math.factorial(k+1)) for k in range(30))
print(v,ser,abs(v-ser))
assert abs(v-ser)<1e-12
open('control.txt','x').write('%.6f\n'%v)
