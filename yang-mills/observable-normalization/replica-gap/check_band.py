"""Cross-check the anisotropic SU(2) band by recoupling two neighboring squares."""
from functools import cache
from itertools import product
from math import log, sqrt

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive, roots_chebyu
from sympy import Rational
from sympy.physics.wigner import wigner_6j


@cache
def loop_element(a, b, c, new_a, new_c):
    # b is the spectator arm. Identical endpoint recouplings give a square.
    spins = [Rational(j, 2) for j in (a, c, b, new_c, new_a, 1)]
    racah = float(wigner_6j(*spins))
    return sqrt((a+1)*(new_a+1)*(c+1)*(new_c+1))*racah**2


def two_squares(cutoff):
    states = [(a,b,c) for a,b in product(range(cutoff+1), repeat=2)
              for c in range(abs(a-b), a+b+1, 2) if c <= cutoff]
    w = np.zeros((len(states), len(states)))
    for i,(a,b,c) in enumerate(states):
        for j,(d,e,f) in enumerate(states):
            if abs(c-f) != 1:
                continue
            if b == e and abs(a-d) == 1:
                w[i,j] += loop_element(a,b,c,d,f)/2
            if a == d and abs(b-e) == 1:
                w[i,j] += loop_element(b,a,c,e,f)/2
    assert np.allclose(w,w.T,atol=1e-14,rtol=0)
    return states, eigh(w)


def predictions(gamma, neighbors):
    u,v = ive([2,3],gamma)/ive(1,gamma)
    r = u**4
    f = lambda k: (r+k)/(r-k)
    c = f(r*r)
    g = (f(u**6)+3*f(u**6*v))/4
    assert g > c
    return (2*c-f(v**4)-2*neighbors*(g-c))/4, (g-c)/6


def read_gap(gamma, states, magnetic, sigma):
    rho = ive(np.arange(1,2+max(max(x) for x in states)),gamma)/ive(1,gamma)
    electric = np.array([rho[a]**3*rho[b]**3*rho[c] for a,b,c in states])
    vals,vec = magnetic
    root = np.sqrt(electric)[:,None]*vec
    top = eigh((root*np.exp(sigma*vals))@root.T, eigvals_only=True,
               subset_by_index=(len(states)-2,len(states)-1))
    return log(top[-1]/top[-2])


def check():
    configs = [two_squares(j) for j in (3, 5)]
    for gamma in (0.6,2.,6.):
        reference, _ = predictions(gamma,1)
        rows = []
        for states, magnetic in configs:
            vals = []
            for step in (0.02,0.01):
                gap = lambda s: read_gap(gamma,states,magnetic,s)
                vals.append((gap(step)+gap(-step)-2*gap(0.))/step**2)
            rows.append((4*vals[1]-vals[0])/3)
        assert max(abs(v-reference) for v in rows)<3e-7
        print(f"two adjacent squares, gamma={gamma:g}, predicted {reference:.9f}, "
              f"cutoffs 3,5 {rows[0]:.9f} {rows[1]:.9f}")
    for gamma in (0.1,1.,2.,8.,100.):
        kappa, dispersion = predictions(gamma,12)
        print(f"cubic lattice gamma={gamma:g}, gap curvature {kappa:.9f}, "
              f"dispersion coefficient {dispersion:.9f}")
    # Character integration independent of the Bessel ratios used above.
    x,w = roots_chebyu(128)
    for gamma in (0.3,2.,10.):
        prob = w*np.exp(gamma*x)
        prob /= prob.sum()
        u,v = ive([2,3],gamma)/ive(1,gamma)
        assert abs(prob@x-u)<3e-14
        assert abs(prob@(x*x)-(1+3*v)/4)<3e-14
        assert prob@(x*x) > (prob@x)**2
    for step in (0.02,0.01):
        v = np.array([step,2*step,-step])
        t = 2*np.cos(v/2)
        incidence = np.array([[0,t[2],t[1]],[t[2],0,t[0]],[t[1],t[0],0]])
        slope = (16-np.linalg.eigvalsh(incidence.T@incidence)[-1])/(v@v)
        assert abs(slope-4/3)<3e-4
        print(f"spatial symbol, step {step}, quadratic slope {slope:.9f}")


if __name__ == "__main__":
    check()
