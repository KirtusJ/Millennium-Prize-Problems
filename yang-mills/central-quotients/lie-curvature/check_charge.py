"""Independent defining-matrix tests of charge parity and imaginary Wilson traces."""
import numpy as np
from scipy.linalg import expm
from check_algebra import basis, comm
from check_singlets import covariance


def check(n):
    t = basis(n)
    d = len(t)
    a = np.einsum("abij,cji->abc", t[:, None] @ t+t @ t[:, None], t).imag/n
    bracket = np.einsum("abij,cij->abc", comm(t[:, None], t), t.conj()).real/n
    np.testing.assert_allclose(a, a.transpose(2, 1, 0), atol=3e-14)
    np.testing.assert_allclose(np.einsum("aac->c", a), 0, atol=3e-14)
    np.testing.assert_allclose(np.vdot(a, bracket), 0, atol=3e-13)
    total = np.vdot(a, a).real
    np.testing.assert_allclose(total, 2*d*(n*n-4))
    odd = {}
    for i, j, k in zip(*np.nonzero(abs(a) > 1e-12)):
        slot = tuple(sorted((i, j, k)))
        odd[slot] = odd.get(slot, 0)+a[i, j, k]/12
    observed = covariance(odd, odd, 0.5, 0.5)
    np.testing.assert_allclose(observed, total/192, atol=1e-13)
    print("SU", n, "symmetric norm, odd local variance, odd/even ratio", total,
          observed, total/np.vdot(bracket, bracket).real)
    return t


def trace_remainder(t):
    n = len(t[0])
    rng = np.random.default_rng(817)
    x, y, z = [np.einsum("a,aij->ij", rng.normal(size=len(t)), t) for _ in range(3)]
    def readings(x, y, z):
        return np.array([np.vdot(comm(x, y), z).real/n, np.trace((x @ y+y @ x) @ z).imag/n])
    exact = readings(x, y, z)
    np.testing.assert_allclose(readings(x.conj(), y.conj(), z.conj()), exact*[1, -1])
    assert min(abs(exact)) > 0.01
    leading = np.trace(x @ x @ x).imag/(6*n)
    errors = []
    for beta in (64., 256., 1024., 4096.):
        u = expm(x/np.sqrt(beta))
        measurement = beta**1.5*np.trace(u).imag/n
        np.testing.assert_allclose(beta**1.5*np.trace(u.conj()).imag/n, -measurement)
        errors.append(abs(measurement-leading))
    assert all(0.24 < b/a < 0.26 for a, b in zip(errors, errors[1:]))
    print("SU3 imaginary trace leading value, successive absolute errors", leading, errors)


if __name__ == "__main__":
    for size in (2, 3, 4):
        generators = check(size)
        if size == 3:
            trace_remainder(generators)
