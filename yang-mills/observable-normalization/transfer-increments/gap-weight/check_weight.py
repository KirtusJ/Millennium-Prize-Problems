"""Verify the three-state controls in state coordinates and in the energy basis."""
from math import exp, log, sqrt

import numpy as np
from scipy.linalg import expm


def parameters(n):
    return {
        "sharp": (n**-2, 1+2*log(1+n)),
        "bounded": (exp(-n/4), n),
        "tight": (n**-2, 1+3*log(n)),
        "slab": (n**-2, 1+log(log(n))),
    }


def state_control(n, p, high):
    vacuum = np.ones(3)/sqrt(3)
    fixed = np.array([1., -1., 0.])/sqrt(2)
    other = np.array([1., 1., -2.])/sqrt(6)
    fast = sqrt(1-p)*fixed + sqrt(p)*other
    generator = (np.eye(3)-np.outer(vacuum,vacuum)+(high-1)*np.outer(fast,fast))/n
    off_diagonal = ~np.eye(3, dtype=bool)
    assert np.all(generator[off_diagonal] < 0)
    step = expm(-generator)
    assert np.all(step > 0) and np.max(abs(step.sum(axis=1)-1)) < 1e-13
    assert np.allclose(np.linalg.eigvalsh(generator)*n, [0,1,high], atol=2e-13)
    cube = np.kron(step, np.kron(step,step))
    assert abs(-n*log(np.linalg.eigvalsh(cube)[-2])-1) < 5e-13
    def correlation(steps):
        propagated = np.linalg.matrix_power(step, steps//2) @ fixed
        return propagated @ propagated
    def spectral(time):
        return p*exp(-time)+(1-p)*exp(-time*high)
    ratio = correlation(n//2)/correlation(n)
    analytic = spectral(.5)/spectral(1)
    assert np.isclose(ratio, analytic, rtol=3e-7, atol=0), (ratio, analytic)
    return ratio


def check_smearing(n, p, high):
    # Form the Laplace readings directly for 35 different positive three-tap laws.
    def ratio(times, weights):
        energies = np.array([1., high])
        filt = np.exp(-np.outer(energies,times)) @ weights
        mass = np.array([p,1-p])*filt**2
        return (mass @ np.exp(-energies/2))/(mass @ np.exp(-energies))
    floor = ratio([2.], [1.])
    for left in range(1,6):
        for middle in range(1,8):
            assert ratio([0.,.5,2.],[left,middle,1.]) >= floor*(1-1e-14)
    return floor


if __name__ == "__main__":
    for n in (64,96,128):
        for name, (p, high) in parameters(n).items():
            ratio = state_control(n,p,high)
            if name == "sharp":
                assert np.isclose(ratio, exp(.5)*(1+n)/2, rtol=1e-11)
            if name == "slab":
                floor = check_smearing(n,p,high)
                print(f"xi={n} {name}: ratio={ratio:.9f}, latest-T=2 ratio={floor:.9f}")
            else:
                print(f"xi={n} {name}: ratio={ratio:.9f}")
