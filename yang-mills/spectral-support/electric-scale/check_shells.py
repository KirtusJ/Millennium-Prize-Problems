"""Independent angular, sharpness and one-cycle controls. Requires SciPy."""
from math import cos, log, pi, sqrt
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import eval_gegenbauer, roots_gegenbauer, xlogy


def angular_blocks():
    for ell in range(7):
        alpha = ell + 1
        x, w = roots_gegenbauer(32, alpha)
        modes = []
        for k in range(12):
            p = eval_gegenbauer(k, alpha, x)
            modes.append(p / sqrt(w @ p**2))
        matrix = (np.array(modes) * (w * x)) @ np.array(modes).T
        expected = np.zeros_like(matrix)
        for k in range(11):
            n = k + ell
            value = sqrt(1 - ell * (ell + 1) / ((n + 1) * (n + 2))) / 2
            expected[k, k + 1] = expected[k + 1, k] = value
        np.testing.assert_allclose(matrix, expected, atol=2e-13)


def endpoint_checks():
    for J in [0, 1, 2, 7, 40]:
        d = J + 1
        theta = pi / (2 * J + 3)
        diag = np.ones(d)
        diag[-1] = 0.5
        off = np.full(d - 1, -0.5)
        low = eigh_tridiagonal(diag, off, eigvals_only=True)[0]
        np.testing.assert_allclose(low, 1 - cos(theta), atol=4e-15)
        hard = eigh_tridiagonal(np.ones(d), off, eigvals_only=True)[0]
        np.testing.assert_allclose(hard, 1 - cos(pi / (J + 2)), atol=4e-15)
        prefix = np.sin(theta * np.arange(1, d + 1))
        L = 1000
        full = np.r_[0, prefix, prefix[-1] * (1 - np.arange(1, L + 1) / L)]
        energy = np.diff(full) @ np.diff(full) / 2
        np.testing.assert_allclose(energy - low * (prefix @ prefix), prefix[-1]**2 / (2 * L))
    assert 4 / 5 > 1 - 2 / 5


def top_rank(probs, mult, q):
    density = probs / mult
    occupied = 0
    prior = 0.0
    for i in np.argsort(-density):
        if prior + probs[i] >= q:
            return occupied + int(np.ceil((q - prior) / density[i]))
        occupied += int(mult[i])
        prior += probs[i]
    raise AssertionError("missing probability")


def rotor(g):
    # One isolated four-link loop. Its radial Jacobi problem is a control geometry.
    count = int(12 * g**0.25) + 20
    n = np.arange(count)
    diag = n * (n + 2) + g
    off = np.full(count - 1, -g / 2)
    energies, vec = eigh_tridiagonal(diag, off)
    a = vec[:, 0]
    a *= np.sign(a[0])
    p = a**2
    eps = 1 - a[:-1] @ a[1:]
    K = p @ (n * (n + 2))
    A = np.r_[0, a, 0]
    np.testing.assert_allclose(np.sum(np.diff(A)**2), 2 * eps, atol=1e-13)
    for J in range(count - 1):
        assert p[:J + 1].sum() * (1 - cos(pi / (2 * J + 3))) <= eps + 1e-12
        assert p[J+1:].sum() * (J+1)*(J+3) <= K + 1e-11
    mult = (n + 1)**2
    rank = top_rank(p, mult, 0.9)
    entropy = -xlogy(p, p / mult).sum()
    C = 4 * sqrt(2) / (3 * pi)
    for r in [1, 2, 9, 20, rank]:
        # Sort individual degenerate block eigenvalues without expanding them.
        left, mass = r, 0.0
        for j in np.argsort(-p / mult):
            used = min(left, mult[j])
            mass += used * p[j] / mult[j]
            left -= used
            if not left:
                break
        assert mass <= 3 * (C * r)**(2 / 3) * eps + 1e-11
    twisted = a * (-1)**n
    weights = (vec.T @ twisted)**2
    frequencies = (energies - energies[0]) / g
    residual = sqrt(weights @ (frequencies - 2)**2)
    # A single defect face has V=2; Dirichlet truncation commutes with the twist.
    assert residual <= sqrt(8 * eps) + 1e-10
    assert weights[frequencies <= 1].sum() <= 8 * eps + 1e-10
    assert abs(weights @ np.exp(-frequencies) - np.exp(-2)) <= residual + 1e-11
    # Class probes act by the normalized character on each radial shell.
    h = g**-0.25
    rates = np.array([1, 2, 3])
    angles = h * rates
    multipliers = np.sinc((n[:, None]+1)*angles/pi) / np.sinc(angles/pi)
    centered = a[:, None]* (multipliers - p @ multipliers)
    coeff = vec.T @ centered
    gaps = energies - energies[0]
    gram = coeff.T @ coeff
    v = np.linalg.eigvalsh(gram)[0]
    assert v > 1e-12
    # The isolated cycle has one face incident on the link rather than four.
    moments = (coeff.T * gaps) @ coeff
    assert np.all(np.diag(moments) <= g*(1 - np.cos(angles))*(1-eps) + 1e-12)
    tau = 0.125
    time_gram = (coeff.T * np.exp(-tau*gaps/np.sqrt(g))) @ coeff
    assert np.linalg.eigvalsh(time_gram)[0] > 0
    norm = gram[0, 0]
    lower = norm*np.exp(-tau*moments[0,0]/(np.sqrt(g)*norm))
    assert time_gram[0,0] >= lower - 1e-13
    theta = 0.7
    fixed = np.sin((n+1)*theta)/((n+1)*np.sin(theta))
    fixed_var = p @ (fixed - p@fixed)**2
    print(f"class probes: min Gram={v:.6g}  min mesh-time Gram={np.linalg.eigvalsh(time_gram)[0]:.6g}"
          f"  fixed-angle var/h^2={fixed_var/h**2:.5f}")
    assert abs(a[-1]) < 1e-20
    print(f"g={g:6d}  median(n)/g^0.25={np.searchsorted(p.cumsum(),0.5)/g**0.25:.4f}  "
          f"r90/g^0.75={rank/g**0.75:.4f}  S-0.75log(g)={entropy-0.75*log(g):.5f}  "
          f"twist residual={residual:.6f}  microscopic C(1)={weights @ np.exp(-frequencies):.6f}")
    return entropy, rank, residual


if __name__ == "__main__":
    angular_blocks()
    endpoint_checks()
    samples = [rotor(g) for g in (16, 256, 4096, 65536)]
    s0, r0, e0 = samples[-2]
    s1, r1, e1 = samples[-1]
    assert abs((s1 - s0) / log(16) - 0.75) < 0.02
    assert abs(log(r1 / r0) / log(16) - 0.75) < 0.04
    assert e1 < e0
    print("Seven angular sectors, five endpoint sizes and four rotor couplings passed.")
