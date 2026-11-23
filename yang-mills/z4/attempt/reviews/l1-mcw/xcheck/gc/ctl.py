import numpy as np
x,w=np.polynomial.hermite_e.hermegauss(60); w=w/np.sqrt(2*np.pi)
f=0.5*x**2; m=(w*f).sum(); v=(w*f*f).sum()-m*m
open('control.txt','x').write("Var=%.6f mean=%.6f\n"%(v,m)); print(v,m)
