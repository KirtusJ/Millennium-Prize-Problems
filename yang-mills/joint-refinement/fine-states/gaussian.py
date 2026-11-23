"""Fixed-physical-time straight-link blocking in the nonzero-mode Wilson Gaussian."""
from itertools import product
from math import asinh, exp, pi, sqrt
import numpy as np


def transverse(symbol):
    frame, _ = np.linalg.qr(symbol[..., None], mode="complete")
    return frame[..., 1:]


def check(n):
    assert n >= 4 and n % 2 == 0
    m = n//2
    aliases = pi*np.array(list(product((0, 1), repeat=3)))
    b = eta = 0.
    for k in product(np.fft.fftfreq(m)*m, repeat=3):
        p = 2*pi*np.array(k)/n
        modes = p + aliases
        symbols = np.expm1(1j*modes)
        mass = np.sum(abs(symbols)**2, axis=1)
        omega = 2*np.arcsinh(np.sqrt(mass)/2)
        if k == (0, 0, 0):
            b = max(b, exp(-n*min(omega[1:])))
            continue
        cframe = transverse(np.expm1(2j*p))
        fine = transverse(symbols)
        filters = (1+np.exp(1j*modes))[..., None]*fine
        rows = (cframe.conj().T @ filters)/np.sqrt(2*np.sinh(omega))[:, None, None]
        block = np.hstack(list(rows))
        _, singular, rows_orth = np.linalg.svd(block, full_matrices=False)
        assert min(singular) > 0
        q = np.eye(16)-rows_orth.conj().T @ rows_orth
        time = np.repeat(np.exp(-n*omega), 2)
        bb = max(np.linalg.eigvalsh((q*time) @ q))
        mix = np.linalg.norm((rows_orth*time) @ q, 2)
        if k == (1, 0, 0) and n > 4:
            # The coarse y-polarization sees four aliases. Its row has no z component.
            active = aliases[:,1] == 0
            weights = 1/np.sinh(omega[active])
            weights /= weights.sum()
            scalar_time = np.exp(-n*omega[active])
            lost = 1-weights[0]
            variance = np.dot(weights,(scalar_time-np.dot(weights,scalar_time))**2)
            unit = np.zeros((8,2),dtype=complex)
            unit[0] = fine[0,1,:].conj()
            np.testing.assert_allclose(np.linalg.norm(q @ unit.ravel())**2,lost,atol=2e-14)
            coarse_y = (np.eye(16)-q) @ unit.ravel()
            coarse_y /= np.linalg.norm(coarse_y)
            np.testing.assert_allclose(np.linalg.norm(q @ (time*coarse_y))**2,variance,atol=2e-16)
            assert bb >= scalar_time[0]*lost-1e-14 and mix**2 >= variance-1e-15
        b = max(b, bb)
        eta = max(eta, mix)
    envelope = (sqrt(56/(sqrt(3)*np.e*n))+exp(-n*asinh(1/sqrt(2))))**2
    rho = exp(-n*asinh(np.sin(pi/n)))
    assert 0 < b <= envelope and 0 < eta <= rho*sqrt(b)
    return b, eta, envelope, rho*sqrt(b)


if __name__ == "__main__":
    for n in (8, 16, 32, 64):
        print("N, all-chaos b, first-chaos eta, analytic b ceiling, all-chaos eta ceiling",
              n, *check(n))
