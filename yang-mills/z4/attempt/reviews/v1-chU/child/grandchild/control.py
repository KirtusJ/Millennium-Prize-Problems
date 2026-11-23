import numpy as np
N=2000
t=np.linspace(0,np.pi,N+1); f=np.sin(t)
v=(np.pi/N)*(f.sum()-0.5*(f[0]+f[-1]))
with open('control.txt','x') as o: o.write('%.6f\n'%v)
print(v)
