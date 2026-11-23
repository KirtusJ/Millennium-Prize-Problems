"""Control: I_3(4)/I_1(4) by trapezoid on (1/pi)int_0^pi exp(x cos t)cos(nt)dt."""
import numpy as np
def I(n,x,N=20000):
    t=np.linspace(0,np.pi,N+1); w=np.ones(N+1); w[[0,-1]]=.5
    return (w*np.exp(x*np.cos(t))*np.cos(n*t)).sum()/N
print("%.6f"%(I(3,4)/I(1,4)))
