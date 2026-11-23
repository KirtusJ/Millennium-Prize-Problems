"""Exact block algebra, incidence counts and free covariance quadrature."""
from fractions import Fraction
from math import ceil, pi

import numpy as np
from numpy.polynomial.legendre import leggauss


def box_checks():
    for width in (1,2,4,9,16):
        box = np.ones(width,dtype=np.int64)
        rows = [np.ones(1,dtype=np.int64)]
        for _ in range(6):
            rows.append(np.convolve(rows[-1],box))
        shift = np.zeros(width+1,dtype=np.int64)
        shift[0],shift[-1] = 1,-1
        first, second = rows[6], rows[3]
        for _ in range(3):
            first = np.convolve(first,[1,-1])
            second = np.convolve(second,shift)
        np.testing.assert_array_equal(first,second)
        for n in range(4):
            moment = sum(int(v)*k**n for k,v in enumerate(first))
            assert moment==(0 if n<3 else -6*width**6)
        if width==4:
            assert sum(abs(first))==264
    print("Five exact block convolutions and their first four moments agree")


def path_check():
    # Count the derivative incidence two independent ways. Time-first paths have
    # identical spatial costs no matter where their slice lies on the time axis.
    edges = {}
    fees = {}
    path_total = Fraction(0)
    edge_weights = {}
    for t in (-29,0,41):
        for p in np.ndindex(5,5,5):
            x = tuple(i-2 for i in p)
            weight = Fraction(2+sum((i+1)*v*v for i,v in enumerate(x)),17)
            pos = [0,0,0]
            path_cost = Fraction(0)
            for axis,target in enumerate(x):
                move = 1 if target>0 else -1
                for _ in range(abs(target)):
                    old = tuple(pos)
                    pos[axis] += move
                    start = min(old,tuple(pos))
                    key = (t,start,axis)
                    fee = Fraction(1+(sum(abs(i) for i in start)+axis)%3,3)
                    fees[key] = fee
                    edges[key] = edges.get(key,Fraction(0))+weight
                    path_cost += fee
            path_total += weight*path_cost
            edge_weights[t,x] = weight
    counted = sum(fees[k]*total for k,total in edges.items())
    bound = sum(v*sum(abs(i) for i in x) for (t,x),v in edge_weights.items())
    assert counted==path_total and counted<=bound and max(fees.values())==1
    print(f"375 spatial paths, direct and transposed sums {counted}, upper bound {bound}")


def quadrature(width, cutoff, order):
    # Coordinates p=R*q, integrated on the positive octant by evenness.
    end = min(cutoff, pi*width) if width else cutoff
    panels = ceil(end/pi)
    x,w = leggauss(order)
    p = ((np.arange(panels)[:,None]+(1+x)/2)*end/panels).ravel()
    w = np.tile(w*end/(2*panels),panels)
    if width:
        sincbox = np.sinc(p/(2*pi))/np.sinc(p/(2*pi*width))
        lattice_p = 2*width*np.sin(p/(2*width))
    else:
        sincbox = np.sinc(p/(2*pi))
        lattice_p = p
    measure = w*sincbox**12
    transverse = lattice_p[:,None]**2+lattice_p[None,:]**2
    xy = measure[:,None]*measure[None,:]*transverse
    times = np.array([0.,.125,.25,.5,1.,2.])
    result = np.zeros(len(times))
    for pz,wz in zip(lattice_p,measure):
        radius = np.sqrt(transverse+pz*pz)
        if width:
            energy = 2*width*np.arcsinh(radius/(2*width))
            denominator = 2*radius*np.sqrt(1+(radius/(2*width))**2)
        else:
            energy = radius
            denominator = 2*radius
        base = wz*pz**6*xy/denominator
        result += [np.sum(base*np.exp(-t*energy)) for t in times]
    return result/pi**3


def free_checks():
    # All finite boxes through R=16 use their full Brillouin zones.
    continuum = quadrature(0,24*pi,16)
    np.testing.assert_allclose(continuum,quadrature(0,16*pi,16),rtol=2e-8)
    coupling = .5/continuum[0]
    def connected(C):
        D = 1+2*coupling*C[0]
        return np.expm1(-1.5*np.log1p(-(2*coupling*C/D)**2))/D**3
    for width in (2,4,8,16,0):
        values = quadrature(width,24*pi,16) if width else continuum
        refined = quadrature(width,24*pi,20)
        np.testing.assert_allclose(values,refined,rtol=2e-10)
        B = connected(values)
        # y=exp(-R*E/8); for R=2,4 this includes fractional free lags.
        witness = -B[2]+B[1]-.09*B[0]
        print(f"R={width if width else 'infinity'} C(0)={values[0]:.10g} "
              f"B(R)/B(0)={B[4]/B[0]:.9g} quadratic witness / variance={witness/B[0]:.9g}")
    assert witness/B[0]>.05
    print(f"fixed test parameter s={coupling:.9g}; finite-to-continuum comparisons are quadrature")


if __name__ == "__main__":
    box_checks()
    path_check()
    free_checks()
