"""Independent Haar-volume checks for the fundamental SU(3) and weighted circles."""
from fractions import Fraction
from math import cos, pi, sin, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def fundamental_su3(t):
    # Orthonormal coordinates in theta_1 + theta_2 + theta_3 = 0.
    def angular(phi):
        unit = [cos(phi)/sqrt(2)+sin(phi)/sqrt(6),
                -cos(phi)/sqrt(2)+sin(phi)/sqrt(6), -2*sin(phi)/sqrt(6)]
        def deficit(r):
            return 2*sum(sin(r*x/2)**2 for x in unit)/3
        radius = brentq(lambda r: deficit(r)-t, 0, 2*sqrt(6*t), xtol=1e-15)
        def radial(q):
            r = q*radius
            delta = np.prod([(2*sin(r*(unit[i]-unit[j])/2))**2
                             for i,j in [(0,1),(0,2),(1,2)]])
            return q*delta*radius**2/t**4
        return quad(radial, 0, 1, epsabs=1e-11)[0]
    return quad(angular, 0, 2*pi, epsabs=1e-10)[0]/(6*(2*pi)**2*sqrt(3))


def circle_volume(k):
    # Exact lengths of constant-sign intervals, in units of one full turn.
    def cuts(m):
        return {Fraction(2*j+1,2*m) for j in range(m)}
    cuts_all = sorted({Fraction(0),Fraction(1)} | cuts(k-1) | cuts(k+1))
    total = Fraction(0)
    for a,b in zip(cuts_all,cuts_all[1:]):
        mid = (a+b)/2
        flips = sum(int(m*mid + Fraction(1,2)) for m in (k-1,k+1))
        if flips%2 == 0:
            total += b-a
    return total


def subgroup_ball_checks():
    tested = 0
    for order, weights in [(17,(1,)), (32,(1,)), (89,(1,7)), (211,(1,50))]:
        theta = 2*pi*np.arange(order)/order
        radii = np.sqrt(sum(2*np.sin(w*theta/2)**2 for w in weights)/len(weights))
        ambient_dimension = 2*len(weights)**2
        for r in (0.013, 0.1, 0.25, 0.55):
            small_count = np.count_nonzero(radii <= r)
            for scale in (1.1, 2, 3.5, 8):
                large_count = np.count_nonzero(radii <= scale*r)
                assert large_count <= (1+2*scale)**ambient_dimension * small_count
                tested += 1
    print(tested, 'finite-subgroup chordal ball comparisons')


if __name__ == '__main__':
    subgroup_ball_checks()
    for k in range(1,101):
        expected = Fraction(1,2) if k%2 else Fraction(k*k-2,2*(k*k-1))
        assert circle_volume(k) == expected
    print('100 exact weighted-circle volumes, including k=1')
    leading = 9*sqrt(3)/(8*pi)
    for t in [.01,.001,.0001]:
        value = fundamental_su3(t)
        slope = (value/leading-1)/t
        assert abs(slope+.2) < t
        print(f't={t:g}, V(t)/t^4={value:.10f}, relative slope={slope:.8f}')
