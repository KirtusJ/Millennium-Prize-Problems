"""Evaluate two-slice Gaussian polynomial readings directly from component moments."""
from collections import Counter, defaultdict
from functools import lru_cache
import numpy as np
from check_algebra import basis, comm


def polynomials(t):
    n, d = t.shape[1], len(t)
    f = (np.einsum("abij,cij->abc", comm(t[:, None], t), t.conj())/n).real
    cubic, norm, h = defaultdict(float), defaultdict(float), defaultdict(float)
    for a, b, c in zip(*np.nonzero(abs(f) > 1e-12)):
        cubic[a, d+b, 2*d+c] += f[a, b, c]
    for a in range(2*d):
        norm[a, a] = 0.5
    for c in range(d):
        terms = list(zip(*np.nonzero(abs(f[:, :, c]) > 1e-12)))
        for a, b in terms:
            for u, v in terms:
                h[tuple(sorted((a, d+b, u, d+v)))] += f[a, b, c]*f[u, v, c]
    return cubic, norm, {k: v for k, v in h.items() if abs(v) > 1e-12}


def covariance(p, q, variance, cross):
    @lru_cache(None)
    def moment(i, j):
        if i+j == 0:
            return 1.
        if (i+j) % 2:
            return 0.
        if i == 0:
            return (j-1)*variance*moment(0, j-2)
        same = (i-1)*variance*moment(i-2, j) if i >= 2 else 0
        other = j*cross*moment(i-1, j-1) if j else 0
        return same+other

    def terms(poly):
        return [(v, Counter(k)) for k, v in poly.items()]
    x, y = terms(p), terms(q)

    def single(term):
        return sum(a*np.prod([moment(n, 0) for n in cnt.values()]) for a, cnt in term)
    mixed = 0.
    for a, ax in x:
        for b, bx in y:
            value = a*b
            for z in ax.keys() | bx.keys():
                value *= moment(ax.get(z, 0), bx.get(z, 0))
                if value == 0:
                    break
            mixed += value
    return mixed-single(x)*single(y)


if __name__ == "__main__":
    for n in (2, 3):
        T, Q, H = polynomials(basis(n))
        v, x = 1.25, 0.5
        c, d = 2*n*n, n*n-1
        qt = covariance(Q, Q, v, x)
        hh = covariance(H, H, v, x)
        qh = covariance(Q, H, v, x)
        tt = covariance(T, T, v, x)
        determinant = qt*hh-qh*qh
        np.testing.assert_allclose([tt, hh, determinant],
                                   [d*c*x**3, 4*d*c*c*v*v*x*x+3*d*c*c*x**4, 3*tt*tt])
        # Deliberately keep the covariance of Q and H out of the determinant.
        assert qt*hh/tt**2 > 10
        local = covariance(H, H, 0.5, 0.5)/4
        np.testing.assert_allclose(local/(d*c/8)**2, 7/d)
        print("SU", n, "local variance/mean squared", local/(d*c/8)**2,
              "single-separation determinant ratio", determinant/tt**2,
              "omitted cross-reading", qt*hh/tt**2)
