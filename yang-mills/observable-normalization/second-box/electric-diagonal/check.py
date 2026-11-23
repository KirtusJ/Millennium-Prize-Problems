"""Independent centered-chart and off-diagonal electric kernel controls."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

import numpy as np
import sympy as sp
from scipy.special import ive, ndtri
from scipy.stats import qmc


def covariance_check(length, dimensions):
    sites = list(product(range(length), repeat=dimensions))
    edges = []
    for x in sites:
        for axis in range(dimensions):
            y = list(x)
            y[axis] = (y[axis] + 1) % length
            edges.append((sites.index(x), sites.index(tuple(y))))
    n = len(sites)
    incidence = sp.zeros(len(edges),n)
    for j,(x,y) in enumerate(edges):
        incidence[j,x], incidence[j,y] = 1,-1
    zero_projection = sp.ones(n)/n
    green = (incidence.T*incidence+zero_projection).inv()-zero_projection
    g = green[0,0]
    assert all(green[i,i]==g for i in range(n))
    diffs = [g-green[x,y] for x,y in edges]
    assert 2*sum(diffs)==n-1
    return 3*Q(len(edges),8)-3*g+3*sum(v*v for v in diffs)/2


def orbit_weight(beta, fields, neighbors):
    # Product of quaternion Haar factors, zero-mode determinant, and exact
    # scalar-coordinate action on the common northern hemisphere.
    radius2 = np.einsum("nxc,nxc->nx",fields,fields)/beta
    assert radius2.max() < 1
    q = np.sqrt(1-radius2)
    log_weight = (3*np.log(q.mean(axis=1)) - np.log(q).sum(axis=1)
                  - beta/2*np.sum((q[:,:,None]-q[:,neighbors])**2,axis=(1,2)))
    return np.mean(np.exp(log_weight))


def log_slice_density(angle):
    # Three mutually orthogonal, equal constant link angles. The even
    # orbit derivative for axis i has transverse eigenvalue (r/2)cot(r/2).
    t = angle/2
    h = t/np.tan(t) if t else 1.
    out = 48*np.log(np.sinc(t/np.pi))
    for mask in range(1,8):
        bits = np.array([(mask >> i) & 1 for i in range(3)])
        out += np.log(h+(1-h)*bits/sum(bits)).sum()
    return out


def integration_check():
    n = np.arange(8)
    degree = np.array([int(k).bit_count() for k in n[1:]])
    walsh = np.array([[(-1)**int(k & x).bit_count() for k in n[1:]] for x in n])/sqrt(8)
    neighbors = n[:,None] ^ (1 << np.arange(3))
    samples = qmc.Sobol(21,scramble=True,seed=291).random_base2(15)
    fields = walsh @ (ndtri(samples).reshape(-1,7,3)/np.sqrt(4*degree[:,None]))
    for r in (0.,1.,2.):
        target = 149/16 - 13*r*r/48 + r**4/16
        values = []
        for beta in (256.,1024.,4096.):
            t = r/(2*np.sqrt(beta))
            c = np.cos(t)
            exact_link_ratio = sqrt(2*np.pi*beta)*ive(1,beta)
            # 1-cos(t) = 2 sin(t/2)^2 avoids subtraction from unity.
            log_ratio = (np.log(orbit_weight(beta*c,fields,neighbors)) - 10.5*np.log(c)
                         -24*np.log(exact_link_ratio) + .5*log_slice_density(2*t)
                         +3*r*r-48*beta*np.sin(t/2)**2)
            values.append(beta*np.expm1(log_ratio))
        extrapolated = (4*values[-1]-values[-2])/3
        assert abs(extrapolated-target)<.012
        print(f"r={r:g}: beta-scaled corrections {np.round(values,6)}, target {target:.8f}")


if __name__ == "__main__":
    assert covariance_check(2,3)==Q(149,16)
    assert covariance_check(2,1)==Q(9,16)
    print("Fixed-graph coefficients at L=2,3,4 in two dimensions:",
          [str(covariance_check(n,2)) for n in (2,3,4)])
    integration_check()
