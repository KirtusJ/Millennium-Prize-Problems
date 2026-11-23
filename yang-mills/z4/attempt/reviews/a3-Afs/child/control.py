import numpy as np
t=np.linspace(0,np.pi,200001)
def I(n,x): return np.trapezoid(np.exp(x*np.cos(t))*np.cos(n*t),t)/np.pi
with open("control.txt","x") as f: f.write("%.6f\n"%(I(2,2)/I(1,2)))
