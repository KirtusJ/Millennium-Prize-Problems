"""Width-only controls for discrete momenta and a normalized three-color-angle Gaussian step."""
from itertools import product
from math import pi
import numpy as np
from numpy.polynomial.hermite_e import hermegauss


def labels(side):
    n = np.arange(-(side//2),(side+1)//2)
    grid = np.stack(np.meshgrid(n,n,n,indexing="ij"),axis=-1).reshape(-1,3)
    return grid[np.any(grid,axis=1)]


def log_width(side, modes, shift):
    p = (2*pi*modes+shift)/side
    s = 4*(np.sin(p/2)**2).sum(axis=-1)
    return .5*(np.log(s)+np.log1p(s/4))


def cost(side, modes, alpha, d):
    if side:
        left = log_width(side,modes,alpha-d/2)
        right = log_width(side,modes,alpha+d/2)
    else:
        left = np.log(np.linalg.norm(2*pi*modes+alpha-d/2,axis=-1))
        right = np.log(np.linalg.norm(2*pi*modes+alpha+d/2,axis=-1))
    # Twice log(cosh((right-left)/2)), stable near equal widths.
    return 2*np.log1p(2*np.sinh((right-left)/4)**2)


def coefficient(side, modes):
    p=2*pi*modes/side
    s=4*(np.sin(p/2)**2).sum(axis=1)
    grad=(2*(s+2)/(s*(s+4)))[:,None]*np.sin(p)
    return (grad.T@grad)/(4*side**2)


def main():
    alpha=np.array([.4,-.2,.15])
    step=np.array([.13,.09,-.07])
    zero=np.zeros(3)
    for side in (2,3,8,16,32):
        modes=labels(side)
        k=coefficient(side,modes)
        np.testing.assert_allclose(k,np.eye(3)*k[0,0],rtol=1e-13,atol=1e-14)
        central=cost(side,modes,zero,step).sum()
        if side==2:
            assert abs(central)<1e-28
        half=cost(side,modes,zero,step/2).sum()
        extrapolated=(16*half-central)/3
        assert abs(extrapolated-step@k@step)<1e-9
        sub=(cost(side,modes,alpha,step)-cost(side,modes,zero,step)).sum()
        reversed_mid=(cost(side,modes,-alpha,step)-cost(side,modes,zero,step)).sum()
        np.testing.assert_allclose(sub,reversed_mid,atol=2e-14)
        print(f"L={side:2d}  k={k[0,0]:.10g}  subtracted cost={sub:.10g}")
    for cutoff in (8,16,32):
        n=labels(2*cutoff+1)
        c=(.5*(cost(0,n,alpha,step)+cost(0,n,-alpha,step))-cost(0,n,zero,step)).sum()
        print(f"continuum label cutoff {cutoff:2d}: {c:.10g}")

    nodes, weights=hermegauss(9)
    nodes3=np.array(list(product(nodes,repeat=3)))
    weights3=np.array([a*b*c for a,b,c in product(weights,repeat=3)])/(2*pi)**1.5
    side=4
    modes=labels(side)
    k=coefficient(side,modes)[0,0]
    variance=4/(32768*side)
    d=nodes3*np.sqrt(variance)
    assert np.linalg.norm(d,axis=1).max()<pi/4
    w=weights3*np.array([np.exp(-cost(side,modes,zero,x).sum()) for x in d])
    z=w.sum()
    cov=d.T@(w[:,None]*d)/z
    v_eff=variance/(1+2*k*variance)
    np.testing.assert_allclose(cov,np.eye(3)*v_eff,atol=5*variance**3)
    assert abs(z-(1+2*k*variance)**(-1.5)) < 5*variance**2
    print(f"Gaussian cubature Z={z:.12g}, covariance diagonal={cov[0,0]:.12g}")


if __name__=="__main__":
    main()
