"""Character components of the one-plaquette nonlinear magnetic prediction in the Haar vacuum."""
import math
import numpy as np
from scipy.special import ive, roots_legendre


def coefficients(n,order):
    q4=3-2*math.sqrt(2)
    th,w=roots_legendre(order)
    th=(th+1)*math.pi/2
    w=w*math.pi/2
    v,uv=roots_legendre(order)
    upper=n+16
    u=(v+1)*upper/2
    weight=uv*upper/2*(n*ive(n,2*u)/u)*np.exp(-4*u)/q4**n
    assert abs(sum(weight)-1)<1e-10
    t2=np.tan(th/2)**2
    response=np.sum(weight[None,:]/(1+t2[:,None]*np.exp(-8*u)[None,:]),axis=1)
    base=(4/math.pi)*(1-np.cos(th))**2*w*response**2
    return np.array([np.sum(base*np.sin((j+1)*th)/np.sin(th)) for j in range(4)])


def run():
    q4=3-2*math.sqrt(2)
    q12=7-4*math.sqrt(3)
    for n in (1,2,4,8,16,32):
        small,large=coefficients(n,320),coefficients(n,640)
        error=max(abs(small-large))
        assert error<5e-4
        assert -large[1]>(1-(q12/q4)**n)/8
        print(f"n={n}: c[0:4]/q4^(2n) = "+" ".join(f"{x:.8f}" for x in large)+f", quadrature change {error:.3g}")
    assert max(abs(large-np.array([6,-8,8,-8])))<.001


if __name__=="__main__":
    run()
