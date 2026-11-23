"""Check the local Gaussian frequencies against derivatives of Wilson plaquettes."""
from itertools import product
import numpy as np
from scipy.linalg import eigvalsh

BITS = np.array(list(product((0, 1), repeat=3)))
NEXT = np.arange(8)[:, None] ^ (1 << np.arange(2, -1, -1))
I2 = np.eye(2, dtype=complex)
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def adj(m):
    return m.conj().swapaxes(-1, -2)


def plaquettes(links):
    loops = [links[:, i] @ links[NEXT[:, i], j] @ adj(links[NEXT[:, j], i])
             @ adj(links[:, j]) for i, j in ((0, 1), (1, 2), (2, 0))]
    p = np.stack(loops)
    return np.stack((p[..., 0, 0].real, p[..., 0, 0].imag,
                     p[..., 0, 1].real, p[..., 0, 1].imag), axis=-1).ravel()


def tangent(links):
    # Each oriented link occurs at most once in each period-two plaquette.
    # The odd part of a one-link rotation at angles +/-1 is exactly sinusoidal.
    columns = []
    for site, axis, spin in product(range(8), range(3), range(3)):
        values = []
        for sign in (-1, 1):
            moved = links.copy()
            rot = np.cos(.5)*I2 + 1j*sign*np.sin(.5)*PAULI[spin]
            moved[site, axis] = rot @ links[site, axis]
            values.append(plaquettes(moved))
        columns.append((values[1]-values[0])/(4*np.sin(.5)))
    return np.stack(columns, axis=1)


def main():
    rng = np.random.default_rng(20261123)
    quats = rng.normal(size=(8, 4))
    quats /= np.linalg.norm(quats, axis=1, keepdims=True)
    gauge = quats[:, 0, None, None]*I2 + 1j*np.einsum("xc,cij->xij", quats[:, 1:], PAULI)
    worst = 0.
    for c in (np.zeros(3), [2*np.pi, 0, 2*np.pi], [np.pi, 0, 0], [.4, -1.2, 2.3]):
        c = np.array(c)
        phases = np.exp(1j*c/4)
        uniform = np.tile(np.stack([np.diag([a, a.conj()]) for a in phases]), (8,1,1,1))
        sectors = [np.linalg.norm(np.sin(np.pi*BITS/2 + q*c/4), axis=1) for q in (-1, 0, 1)]
        expected = np.sort(np.r_[np.zeros(24), np.repeat(np.concatenate(sectors), 2)])
        for links in (uniform, gauge[:, None] @ uniform @ adj(gauge[NEXT])):
            observed = np.sort(np.linalg.svd(tangent(links), compute_uv=False))
            worst = max(worst, np.max(np.abs(observed-expected)))
        print(f"C={c}; positive rank {sum(expected>1e-10)}, frozen energy {sum(np.arcsinh(expected)):.10f}")
    assert worst < 3e-13, worst
    # The offset translates the oscillator without changing its full-line norm.
    x = np.linspace(-18, 18, 451)
    delta = x[1]-x[0]
    conv = np.exp(-(x[:,None]-x)**2/8)/np.sqrt(8*np.pi)*delta
    for sigma in (.4, 1., np.sqrt(3.)):
        for offset in (0., 1.):
            weight = np.exp(-(offset + sigma*x)**2/4)
            matrix = conv * weight[:,None] * weight
            top = eigvalsh(matrix, subset_by_index=(len(x)-1, len(x)-1))[0]
            assert abs(top - np.exp(-np.arcsinh(sigma))) < 1e-10, top
    print(f"Eight Wilson derivatives, max singular-value error {worst:.3g}; six oscillator checks passed")


if __name__ == "__main__":
    main()
