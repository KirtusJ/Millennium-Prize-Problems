"""Exact unit-ball moments and an independent finite-radius symbol calculation."""
from math import prod

import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.hermite import hermgauss


def ball_average(poly, variables):
    total = 0
    for powers, coefficient in sp.Poly(poly, *variables).terms():
        if any(p % 2 for p in powers):
            continue
        total += coefficient * 3 * prod(sp.factorial2(p-1) for p in powers) / (
            (sum(powers)+3)*sp.factorial2(sum(powers)+1))
    return sp.factor(total)


def exact():
    p = sp.symbols("x y z")
    s = sum(t*t for t in p)
    h = (1/sp.sqrt(2), -1/sp.sqrt(2), 0)
    q = sum(u*t**2 for u,t in zip(h,p))
    quartic = (s*q-9*sum(u*t**4 for u,t in zip(h,p)))/(216*sp.sqrt(3))
    cube = ball_average(q*q/108, p)
    filtered = ball_average(quartic**2, p)
    assert cube == sp.Rational(1,1890)
    return cube, filtered


def integrate(radius):
    # Integrate on a Euclidean ball. The shrinking spectral boundary has the same limit.
    z, weights = leggauss(14)
    radial, radial_weights = leggauss(10)
    phi = np.arange(40)*2*np.pi/40
    xy = np.sqrt(1-z*z)[:,None]
    directions = np.stack(np.broadcast_arrays(xy*np.cos(phi), xy*np.sin(phi), z[:,None]), -1)
    result = np.zeros(2)
    for node, weight in zip(radial, radial_weights):
        r = (1+node)/2
        k = radius*r*directions
        c = np.cos(k/2)
        mat = c[..., :, None]*c[..., None, :]
        for i in range(3):
            mat[...,i,i] = 0
        _, modes = np.linalg.eigh(mat)
        cube = modes[..., :, -1]*c
        filt = cube*(1+(1-np.cos(k))/3)
        for i, v in enumerate([cube, filt]):
            result[i] += 3*weight*r*r/4 * np.sum(weights[:,None]*(v[...,0]-v[...,1])**2/2)/40
    return result/np.array([radius**4,radius**8])


def gaussian_check(ball):
    # Gaussian with density proportional to exp(-|p|^2), so D=1.
    nodes, weights = hermgauss(8)
    x,y,z = np.meshgrid(nodes,nodes,nodes,indexing="ij")
    joint = np.einsum("i,j,k->ijk",weights,weights,weights)/np.pi**1.5
    poly = (-8*x**4+8*y**4+x*x*z*z-y*y*z*z)/(216*np.sqrt(6))
    measured = np.sum(joint*poly**2)
    assert np.isclose(measured, float(ball)*3465/16, rtol=1e-13, atol=0)


if __name__ == "__main__":
    expected = exact()
    gaussian_check(expected[1])
    print("exact averages", *expected)
    for r in (.4,.2,.1,.05):
        estimates = integrate(r)
        print(r, estimates)
    assert np.allclose(estimates, [float(v) for v in expected], rtol=.002, atol=0)
