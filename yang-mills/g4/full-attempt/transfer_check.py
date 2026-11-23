"""Independent finite transfer calculations for the magnetic perturbation. Requires NumPy."""
from itertools import product
from math import exp, factorial, fsum, log, sqrt
import json
import numpy as np


def bessel(order, g):
    term = (g/2)**order / factorial(order)
    terms = [term]
    for k in range(1, 500):
        term *= (g/2)**2 / (k*(k+order))
        terms.append(term)
        if term < 1e-17*max(terms):
            break
    return fsum(terms)


def su2_ratios(g):
    den = bessel(1, g)
    return bessel(2, g)/den, bessel(3, g)/den


def predicted(q, t, neighbors):
    lam = q**4
    def response(x):
        return (lam+x)/(lam-x)
    h = (1+lam)/(1-lam)
    adjacent = (response(q**6) + 3*response(q**6*t))/4
    assert adjacent > h
    return -(response(t**4) - 2*h + 2*neighbors*(adjacent-h))/8


def curvature(gap):
    def even_difference(b):
        return ((gap(b)-gap(0)) + (gap(-b)-gap(0))) / (2*b*b)
    return (4*even_difference(0.002) - even_difference(0.004)) / 3


def square(g, cutoff):
    # Characters chi_0,...,chi_(cutoff-1). Multiplication by chi_1 is the path adjacency.
    adjacency = np.diag(np.ones(cutoff-1), 1) + np.diag(np.ones(cutoff-1), -1)
    w, basis = np.linalg.eigh(adjacency)
    kinetic = np.array([(bessel(k+1, g)/bessel(1, g))**4 for k in range(cutoff)])
    def gap(b):
        side = (basis * np.exp(b*w/4)) @ basis.T
        vals = np.linalg.eigvalsh((side * kinetic) @ side)
        return log(vals[-1]/vals[-2])
    return curvature(gap)


def tetra_product(a, b):
    # Integer coordinates are twice the quaternion coordinates.
    w,x,y,z = a
    s,u,v,t = b
    parts = (w*s-x*u-y*v-z*t, w*u+x*s+y*t-z*v,
             w*v-x*t+y*s+z*u, w*t+x*v-y*u+z*s)
    assert all(k % 2 == 0 for k in parts)
    return tuple(k//2 for k in parts)


def tetra_pair(g):
    group = [tuple(sign*2 if j==i else 0 for j in range(4))
             for i in range(4) for sign in (1, -1)] + list(product((-1,1), repeat=4))
    index = {v:i for i,v in enumerate(group)}
    mul = np.array([[index[tetra_product(a,b)] for b in group] for a in group])
    inv = np.array([index[(a,-x,-y,-z)] for a,x,y,z in group])
    scalar = np.array([u[0]/2 for u in group])
    weight = np.exp(g*scalar)
    weight /= weight.sum()
    q = float(weight @ scalar)
    t = float(weight @ (4*scalar**2 - 1))/3
    one = weight[mul[:,inv]]
    evals = np.linalg.eigvalsh(one)
    assert abs(evals[-2]-q)<1e-12 and abs(evals[-1]-1)<1e-12
    k3 = (one @ one @ one)[:,index[(2,0,0,0)]]

    size = len(group)
    states = np.arange(size)
    labels = np.full((size,size), -1)
    representatives, masses = [], []
    for a,b in product(range(size), repeat=2):
        if labels[a,b]>=0:
            continue
        conj_a, conj_b = mul[mul[states,a],inv], mul[mul[states,b],inv]
        orbit = set(zip(conj_a.tolist(),conj_b.tolist()))
        for x,y in orbit:
            labels[x,y]=len(masses)
        representatives.append((a,b))
        masses.append(len(orbit)/size**2)
    kernel = []
    for a,b in representatives:
        # Shared link first on both oriented loops. Each remaining arm has three independent increments.
        law_a = k3[mul[inv[:,None],mul[states,inv[a]][None,:]]]
        law_b = k3[mul[inv[:,None],mul[states,inv[b]][None,:]]]
        joint = (law_a.T * weight) @ law_b
        kernel.append(np.bincount(labels.ravel(), weights=joint.ravel(), minlength=len(masses)))
    kernel = np.array(kernel)
    root = np.sqrt(masses)
    sym = kernel * root[:,None] / root[None,:]
    assert np.max(np.abs(sym - sym.T)) < 1e-12
    assert np.max(np.abs(kernel.sum(axis=1) - 1)) < 1e-12
    A = np.array([scalar[a]+scalar[b] for a,b in representatives])
    def gap(b):
        side = np.exp(b*A/2)
        vals = np.linalg.eigvalsh(side[:,None]*sym*side[None,:])
        return log(vals[-1]/vals[-2])
    assert abs(gap(0)+4*log(q)) < 2e-10
    return len(masses), curvature(gap), predicted(q,t,1)


def run():
    rows = []
    for g in (1.3, 2.2, 4.0):
        q,t = su2_ratios(g)
        first, second = square(g,12), square(g,18)
        target = predicted(q,t,0)
        assert max(abs(first-target),abs(second-target)) < 2e-6
        states, measured, calculated = tetra_pair(g)
        assert abs(measured-calculated) < 3e-6
        rows.append({"g":g, "SU2_square":round(target,7), "SU2_measured":round(second,7),
                     "tetra_pair":round(calculated,7), "tetra_measured":round(measured,7),
                     "tetra_orbits":states,"cubic_SU2_coefficient":round(predicted(q,t,12),7)})
    return rows


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
