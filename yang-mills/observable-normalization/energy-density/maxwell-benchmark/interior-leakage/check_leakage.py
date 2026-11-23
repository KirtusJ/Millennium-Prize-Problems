"""Finite-order quadrature of the free magnetic law, k=1, clocks in [1, 4]."""
from math import ceil, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss


def integrate_nodes(left, right, m, order):
    cell_count = ceil((right-left)*sqrt(m)/3)
    abscissa, weights = leggauss(order)
    cell_width = (right-left)/cell_count
    points = left + cell_width*(np.arange(cell_count)[:, None]+(1+abscissa)/2)
    return points.ravel(), np.tile(weights*cell_width/2, cell_count)


def squared_field(momentum, center, m):
    h = 3/(2*(m-1))
    def half_phase(p):
        return np.arctan2(np.sqrt(-np.expm1(-h*p*p)), np.exp(-h*p*p/2))
    phase, shift = half_phase(momentum), half_phase(center)
    def fejer(x):
        return (np.sinc(m*x/np.pi)/np.sinc(x/np.pi))**2
    return np.exp(-2*momentum**2)*(fejer(phase-shift)+fejer(phase+shift))**4


def readings(target, m, order, delta=0.1):
    # Symmetry gives z >= 0. Constants cancel in the normalized measure.
    z, wz = integrate_nodes(0, 1, m, order)
    slopes = np.array([2.0, 5.0, 12.0])
    time = slopes*np.log(m)
    norm = leakage = 0.
    laplace = np.zeros((len(time), 2))
    for left, right in [(1., 1+delta), (1+delta, 12.)]:
        energies, we = integrate_nodes(left, right, m, order)
        for start in range(0, len(energies), 64):
            e = energies[start:start+64, None]
            p, q = (e+z)/2, (e-z)/2
            weight = (e**2-1)**2+(1-z**2)**2
            energy_mass = (weight*squared_field(p,target/2,m)*
                           squared_field(q,target/2,m)) @ wz
            energy_mass *= we[start:start+64]
            norm += energy_mass.sum()
            if left == 1.:
                leakage += energy_mass.sum()
            # Subtract the threshold from the exponent for stable ratios.
            shifted = np.exp(-(e-1)*time)*energy_mass[:,None]
            laplace[:,0] += shifted.sum(axis=0)
            laplace[:,1] += (shifted*np.exp(-(e-1))).sum(axis=0)
    return np.r_[leakage/norm, 1-np.log(laplace[:,1]/laplace[:,0])]


if __name__ == "__main__":
    for target in (1.5, 2.5, 4.0):
        for m in (256, 1024, 4096):
            first, second = (readings(target,m,order) for order in (12,18))
            assert np.allclose(first,second,rtol=2e-8,atol=1e-55), (first,second)
            exponent = 3.5 if target <= 2 else 7
            print(f"E0={target:g} m={m:4} scaled leakage={second[0]*m**exponent:.7g}"
                  f"   effective energies at c=(2,5,12): {np.round(second[1:],6)}")
