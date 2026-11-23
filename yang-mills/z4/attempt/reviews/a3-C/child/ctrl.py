import numpy as np
t=np.linspace(0,12,2400001)
f=lambda x:np.exp(-x*np.cosh(t))*np.cosh(t)
def K1(x):
    y=np.exp(-x*np.cosh(t))*np.cosh(t); h=t[1]-t[0]
    return h*(y.sum()-0.5*(y[0]+y[-1]))
print("%.6f"%K1(1.0))
