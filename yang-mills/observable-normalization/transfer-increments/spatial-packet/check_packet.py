"""Numerical checks of the growing packet in lattice and continuum momentum."""
from math import ceil, pi

import numpy as np
from numpy.polynomial.legendre import leggauss


def panel_nodes(panels, order, cap):
    x, weight = leggauss(order)
    width = cap/panels
    pts = ((np.arange(panels)[:,None] + (x+1)/2)*width).ravel()
    return pts, np.tile(weight*width/2, panels)


def covariance(u, weights, R, times):
    """Integrate in the positive octant with u=Rq or continuum momentum."""
    if R is None:
        h2 = u**2
        tent2 = np.sinc(u/(2*pi))**4
    else:
        h2 = (2*R*np.sin(u/(2*R)))**2
        tent2 = (np.sinc(u/(2*pi))/np.sinc(u/(2*pi*R)))**4
    w = weights*tent2/pi
    h12 = h2[:,None]+h2[None,:]
    w12 = w[:,None]*w[None,:]
    result = np.zeros(len(times))
    for z, hz2, wz in zip(u,h2,w):
        norm = np.sqrt(h12+hz2)
        if R is None:
            energy = norm
            denominator = 2*norm
        else:
            energy = 2*R*np.arcsinh(norm/(2*R))
            denominator = 2*norm*np.sqrt(1+(norm/(2*R))**2)
        density = wz*(2*np.sin(z/2))**6*w12*h12/denominator
        for i,time in enumerate(times):
            result[i] += np.sum(density*np.exp(-time*energy))
    return result


def tent_identity(R):
    # Real-space transform, including the three long spatial differences.
    x = np.arange(-R+1,R)
    a = (1-np.abs(x)/R)/R
    assert abs(a.sum()-1) < 2e-15
    span = x.size+3*R
    kernel = np.zeros(span)
    for j,b in enumerate([1,-3,3,-1]):
        kernel[j*R:j*R+x.size] += b*a
    xlong = np.arange(span)-(R-1)
    for q in np.linspace(-2.7,2.9,51):
        actual = np.sum(kernel*np.exp(1j*xlong*q))
        theory = (1-np.exp(1j*R*q))**3*(np.sinc(R*q/(2*pi))/np.sinc(q/(2*pi)))**2
        assert abs(actual-theory)<3e-13


if __name__ == "__main__":
    times = [0,1,2]
    for R in (2,4,8,16,32):
        tent_identity(R)
        value = covariance(*panel_nodes(R,12,pi*R),R,times)
        # Independently place points at midpoints of a uniform full-period grid.
        count = 20*R
        step = pi*R/count
        grid = (np.arange(count)+.5)*step
        check = covariance(grid,np.full(count,step),R,times)
        np.testing.assert_allclose(check,value,rtol=5e-8,atol=1e-12)
        d = 1+2*value[0]
        connected = d**-3*np.expm1(-1.5*np.log1p(-4*(value[1:]/d)**2))
        print(f"R={R:2} C(0,R,2R)={value}   connected(R,2R)={connected}")
    first = covariance(*panel_nodes(ceil(48/pi),14,48),None,[1,2])
    second = covariance(*panel_nodes(ceil(60/pi),20,60),None,[1,2])
    np.testing.assert_allclose(first,second,rtol=2e-10,atol=1e-13)
    assert np.max(abs(value[1:]/second-1)) < .01
    print("Continuum one-color C(1,2) =",second)
