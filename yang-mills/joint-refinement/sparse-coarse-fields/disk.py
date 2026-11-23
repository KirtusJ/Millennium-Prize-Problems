"""Four-face SU(2) disk with boundary angle pi-c/beta and transverse reference."""
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=None)
def rule(order):
    return np.polynomial.legendre.leggauss(order)


def parameters(k, order):
    nodes, weights = rule(order)
    angles = np.pi*(1+nodes)/2
    haar = weights*np.sin(angles)**2
    cost = 2*np.sin(angles/2)**2
    tilt = haar*np.exp(-np.asarray(k)[...,None]*cost)
    norm = tilt.sum(axis=-1)
    tilt /= norm[...,None]
    mean_cost = tilt @ cost
    variance = (tilt * (cost-mean_cost[...,None])**2).sum(axis=-1)
    return k+np.log(norm/haar.sum()), 1-mean_cost, variance


def mark(beta, c, order, incl_order=40, radial_order=192):
    delta = c/beta
    assert 0 <= delta < np.pi
    t, wt = rule(order)
    t = np.pi*(t+1)/2
    u, wu = rule(incl_order)
    second_real = -np.cos(t)[:,None]*np.cos(delta) + np.sin(t)[:,None]*np.sin(delta)*u
    k2 = beta*np.sqrt(2*np.maximum(0,1+second_real))
    k1 = 2*beta*np.cos(t/2)
    log1, R, Rp = parameters(k1, radial_order)
    log2, _, _ = parameters(k2, radial_order)
    logs = log1[:,None]+log2
    mass = (np.sin(t)**2*wt)[:,None]*wu*np.exp(logs-logs.max())
    mass /= mass.sum()
    vx2 = np.sin(t/2)[:,None]**2*(1-u**2)/2
    j = np.sum(mass*((1-vx2)*(R/k1)[:,None]+vx2*Rp[:,None]))
    v = j+np.sum(mass*vx2*(R**2)[:,None])
    return np.array([v,beta*j/(3*v)])


def limit(c):
    h = c/np.sqrt(2)
    A = (1/np.tanh(h)-1/h)/h if h else 1/3
    return np.array([A/2,(2/A-1)/(3*np.sqrt(2))])


if __name__ == "__main__":
    for c in (0, 0.5, 1, 2, 4):
        expected = limit(c)
        for beta in (64, 512, 4096):
            actual = mark(beta,c,384)
            np.testing.assert_allclose(actual,mark(beta,c,512,incl_order=52,radial_order=228),atol=2e-9,rtol=2e-9)
            print(f"c={c:g} beta={beta} variance={actual[0]:.8f} beta*quotient={actual[1]:.8f}")
        np.testing.assert_allclose(actual,expected,rtol=.002)
        print("analytic limit", expected)
