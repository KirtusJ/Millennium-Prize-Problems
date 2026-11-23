"""Integrate the finite-radius quartic-symbol window using spherical quadrature."""
import numpy as np
from numpy.polynomial.legendre import leggauss

D = 7/768


def orientation(k):
    t = 2*np.cos(k/2)
    matrix = 2*t[..., :, None]*t[..., None, :]
    diag = 50/3 - np.sum(4*np.sin(k/2)**2, axis=-1)
    for i in range(3):
        matrix[..., i, i] = diag
    levels, modes = np.linalg.eigh(matrix)
    return levels[..., -1], modes[..., :, -1]


def normalized_integrals(r):
    z, wz = leggauss(16)
    phi = 2*np.pi*np.arange(48)/48
    z, phi = np.broadcast_arrays(z[:, None], phi)
    directions = np.stack((np.sqrt(1-z*z)*np.cos(phi),
                           np.sqrt(1-z*z)*np.sin(phi), z), axis=-1)
    lo = np.zeros_like(z)
    hi = np.full_like(z, 2*r)
    for _ in range(42):
        mid = (lo+hi)/2
        top, _ = orientation(mid[..., None]*directions)
        accepted = (98/3-top) <= 256*D*r*r
        lo, hi = np.where(accepted, mid, lo), np.where(accepted, hi, mid)
    radius = (hi+lo)/2
    nodes, weights = leggauss(12)
    out = np.zeros(3)
    for node, weight in zip(nodes, weights):
        s = radius*(1+node)/2
        k = s[..., None]*directions
        _, v = orientation(k)
        # Common phases cancel in absolute squares. The contrast is (1,-1,0)/sqrt(2).
        based = v*np.exp(0.5j*k)
        cube = v*np.cos(k/2)
        unit_weight = s*s*radius/2*weight*wz[:, None]*(2*np.pi/48)
        for i, a in enumerate((based, cube, np.cos(k/2)/np.sqrt(3))):
            out[i] += np.sum(unit_weight*np.abs(a[...,0]-a[...,1])**2/2)
    return out / (4*np.pi/3) / np.array([r**5, r**7, r**7])


if __name__ == "__main__":
    target = np.array([1/60, 1/1890, 1/3360])
    for r in (0.4, 0.2, 0.1, 0.05):
        result = normalized_integrals(r)
        print(f"r={r:g}", result)
    assert np.max(abs(result/target-1)) < 0.003
    assert abs(result[2]/target[1]-1) > 0.4
