"""SU(2) Haar singlet projection of the finite-box oscillator partition function."""
from itertools import combinations_with_replacement
from math import pi, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss


def trace_rows(n, target_time=1.):
    m, b = n+1, n**(-.5)
    size = m*b
    k = max(1,round(target_time/b))
    period = k*b
    axis = (2*np.sin(np.pi*np.arange(m)/(2*m)))**2
    indices = np.array(list(combinations_with_replacement(range(m),3)))
    active = np.sum(indices>0,axis=1)
    indices = indices[active>=2]
    multiplicity = active[active>=2]-1
    a,j,c = indices.T
    permutations = np.where(a==c,1,np.where((a==j)|(j==c),3,6))
    weight = multiplicity*permutations
    omega = np.sqrt(np.sum(axis[indices],axis=1))
    q = np.exp(-k*2*np.arcsinh(omega/2))
    w = q/(1-q)**2
    susceptibility = np.dot(weight,w)
    log_partition = -3*np.dot(weight,np.log1p(-q))
    # Class angle φ, Haar 2 sin²φ / π. The two center peaks have equal mass.
    # Scale the quadrature coordinate so the shrinking peaks remain resolved.
    nodes,weights=leggauss(48)
    upper=min(.5*pi*sqrt(susceptibility),10.)
    phi=(1+nodes)*upper/(2*sqrt(susceptibility))
    sine2=np.sin(phi)**2
    values=np.array([np.exp(-np.dot(weight,np.log1p(4*w*s))) for s in sine2])
    ratio=4/pi*upper/(2*sqrt(susceptibility))*np.dot(weights,sine2*values)
    return [float(3*period**3*susceptibility/size**3),
            float(45*period**3*log_partition/(3*pi*pi*size**3)),
            float(8*sqrt(pi)*susceptibility**1.5*ratio)]


def run():
    rows={str(n):trace_rows(n) for n in (31,63,127)}
    assert all(abs(rows['127'][j]-1)<abs(rows['31'][j]-1) for j in range(3))
    assert abs(rows['127'][2]-1)<.02
    return rows
