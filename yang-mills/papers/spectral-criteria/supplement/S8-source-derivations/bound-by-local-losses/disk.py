"""Compact SU(2) disk: conditional pair variance at central boundary and traceless mark."""
import numpy as np


def quotient(beta, order):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    angle=np.pi*(1+nodes)/2
    haar=weights*np.sin(angle)**2
    haar/=haar.sum()
    cost=2*np.sin(angle/2)**2

    def pair_statistics(k):
        # E and Var of 1-Re(U) remain well-conditioned for large tilt.
        tilted=haar[None,:]*np.exp(-k[:,None]*cost[None,:])
        norm=tilted.sum(axis=1)
        tilted/=norm[:,None]
        mean=tilted@cost
        variance=np.sum(tilted*(cost[None,:]-mean[:,None])**2,axis=1)
        return k+np.log(norm),1-mean,variance

    s=np.sin(angle/2)
    k=2*beta*np.cos(angle/2)
    plus,r,dr=pair_statistics(k)
    minus,_,_=pair_statistics(2*beta*s)
    logw=plus+minus
    mass=haar*np.exp(logw-logw.max())
    mass/=mass.sum()
    j=mass@((1-s*s/3)*r/k+(s*s/3)*dr)
    var=j+mass@(r*r*s*s/3)
    return np.array([var,j,j/(3*var)])


if __name__=="__main__":
    for beta in (1,4,16,64,256,1024):
        v=quotient(beta,192)
        np.testing.assert_allclose(v,quotient(beta,256),rtol=3e-9,atol=3e-12)
        print(f"beta={beta:4} variance={v[0]:.8f} J12={v[1]:.8f} ratio={v[2]:.8f} beta*ratio={beta*v[2]:.8f}")
    print("limiting beta*ratio",5/(3*np.sqrt(2)))
