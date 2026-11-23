"""Check the hard-mode sign with rationals and the winding coefficient numerically."""
from fractions import Fraction as F
from math import comb, isqrt

import numpy as np


def curvature_interval(n):
    """Enclose the exact N=2 or 3 shell sum using directed rational bounds."""
    if n not in (2, 3):
        raise ValueError("the shell reduction uses N=2 or 3")
    scale = 10**12
    lower = upper = F(0)
    cosine = F(-1) if n == 2 else F(-1, 2)
    for j in (1, 2, 3):
        s = j * (1 - cosine) / 2
        u = s * (1 + s)
        # Sum the three axial second derivatives, leaving 1/sqrt(u) out.
        coefficient = (3 - j + j*cosine)/2 - j*(1-cosine**2)*(1+2*s)/(8*u)
        coefficient *= F(comb(3, j)*(n-1)**j, 3*n)
        root = isqrt(u.numerator * scale**2 // u.denominator)
        endpoints = (coefficient*scale/root, coefficient*scale/(root+1))
        lower += min(endpoints)
        upper += max(endpoints)
    return lower, upper


def box_energy(n, angle):
    points = np.arange(n, dtype=np.longdouble)
    pi = np.arccos(np.longdouble(-1))
    k = 2*pi*points/n

    def dispersion(shift):
        a, b, c = (np.sin((k+t/n)/2)**2 for t in shift)
        return 2*np.arcsinh(np.sqrt(a[:, None, None]+b[None, :, None]+c[None, None, :]))

    return 2*n*np.sum(dispersion(angle)-dispersion((0, 0, 0)))


def winding_correction(angle, radius=50):
    axis = np.arange(-radius, radius+1, dtype=float)
    y, z = np.meshgrid(axis, axis, indexing="ij")
    total = 0.
    for x in axis:
        q = x*x+y*y+z*z
        q[q == 0] = np.inf
        angular = (x**4+y**4+z**4)/q**2
        total += np.sum((8*angular-4)*(1-np.cos(x*angle[0]+y*angle[1]+z*angle[2]))/q**3)
    return 2*total/np.pi**2


if __name__ == "__main__":
    for n, left, right in [(2, F(2545, 10**6), F(2546, 10**6)),
                           (3, F(-121253, 10**6), F(-121252, 10**6))]:
        lo, hi = curvature_interval(n)
        assert left < lo <= hi < right
        print(f"N={n}: {float(left):.6f} < a_N < {float(right):.6f}")
    for angle in ((1., 0., 0.), (.7, -.4, 1.1), (np.pi, np.pi, np.pi)):
        predicted = winding_correction(angle)
        values = [box_energy(n, angle) for n in (16, 32, 64, 128)]
        estimates = [n*n*(a-b)/.75 for n, a, b in zip((16, 32, 64), values, values[1:])]
        extrapolated = (4*estimates[-1]-estimates[-2])/3
        assert abs(extrapolated-predicted) < 8e-4
        print(angle, "winding", round(predicted, 6), "extrapolated", round(float(extrapolated), 6))
