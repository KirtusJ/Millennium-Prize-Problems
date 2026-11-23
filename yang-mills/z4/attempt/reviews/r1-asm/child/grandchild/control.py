import numpy as np
x,w=np.polynomial.legendre.leggauss(200)
t=(x+1)*np.pi/2; w=w*np.pi/2
a=np.pi/2*(1-np.cos(t)); da=np.pi/2*np.sin(t)
c=np.sum(w*da*np.sqrt(4*np.arcsinh(np.sin(a))))
with open('control.txt','x') as f: f.write("c* = %.6f\n"%c)
print(c)
