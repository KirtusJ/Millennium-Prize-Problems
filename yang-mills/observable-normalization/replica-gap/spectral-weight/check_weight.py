"""Measure the centered total plaquette on the independently recoupled theta graph."""
from math import log1p
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_band import two_squares


def observables(matrix, w, hamiltonian):
    val, eig = eigh(matrix)
    if not hamiltonian:
        val, eig = val[::-1], eig[:, ::-1]
    probe = w @ eig[:,0]
    probe -= eig[:,0]*(probe @ eig[:,0])
    prob = (eig.T @ probe)**2/(probe @ probe)
    # The first symmetric state is lowest at small nonzero coupling.
    if hamiltonian:
        return val[1]-val[0], sum(prob[2:])
    ratios = val[2:]/val[1]
    errors = [prob[2:] @ (ratios**n*(1-ratios))/(prob[1]+prob[2:]@(ratios**(n+1)))
              for n in (0,1,2)]
    return sum(prob[2:]), *(log1p(e) for e in errors)


def coefficients(gamma, degree):
    u,v = ive([2,3],gamma)/ive(1,gamma)
    r = u**4
    x = np.array([v**4/r,u**6/r,u**6*v/r])
    c = (1+r)/(1-r)
    w = np.array([1/4,degree/8,3*degree/8])*(((1+x)/(1-x)-c)/2)**2
    return np.array([sum(w), *(w @ ((1-x)*x**n) for n in (0,1,2))])


def check():
    states,(wv,vec) = two_squares(4)
    w = (vec*wv) @ vec.T
    for gamma in (1.,3.,6.):
        rho = ive(np.arange(1,6),gamma)/ive(1,gamma)
        diag = np.array([rho[a]**3*rho[b]**3*rho[c] for a,b,c in states])
        expected = coefficients(gamma,1)
        rows = []
        for s in (.012,.006):
            def readings(z):
                half = (vec*np.exp(z*wv/2)) @ vec.T
                return np.array(observables((half*diag) @ half,w,False))
            rows.append((readings(s)+readings(-s))/(2*s*s))
        measured = (4*rows[1]-rows[0])/3
        print(f"gamma {gamma:g}  predicted {expected}  measured {measured}")
        assert np.max(abs(measured-expected)) < 1e-7
    # Continuous-time Hamiltonian. Energies are in units of 1/kappa.
    bare = np.array([(3*a*(a+2)+3*b*(b+2)+c*(c+2))/2 for a,b,c in states])
    rows = []
    for z in (.06,.03):
        def change(s):
            m,weight = observables(np.diag(bare)-s*w,w,True)
            return np.array([m-6,weight])/s**2
        rows.append((change(z)+change(-z))/2)
    measured = (4*rows[1]-rows[0])/3
    expected = np.array([13/280,1/(4*15**2)+1/(8*6**2)+3/(8*42**2)])
    assert np.max(abs(measured-expected))<1e-7
    print(f"theta Hamiltonian mass shift and leakage {measured}  targets {expected}")
    for gamma in (100., 1000., 10000.):
        print(f"cubic Wilson leakage/gamma^2 at {gamma:g}: "
              f"{coefficients(gamma,12)[0]/gamma**2:.9f}; Hamiltonian {1999/44100:.9f}")


if __name__ == "__main__":
    np.set_printoptions(precision=9)
    check()
