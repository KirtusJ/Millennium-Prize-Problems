"""Test temporal plaquettes directly against the eight quaternion Fourier blocks."""
from itertools import product
from math import pi
import numpy as np
from scipy.integrate import quad

BITS = np.array(list(product((0, 1), repeat=3)))
SIGNS = 1 - 2 * BITS
FOURIER = (-1.) ** (BITS @ BITS.T) / np.sqrt(8)
NEIGHBORS = np.arange(8)[:, None] ^ (1 << np.arange(2, -1, -1))
BASIS = np.eye(4)


def matrices(q):
    z, w = q[..., 0] + 1j*q[..., 1], q[..., 2] + 1j*q[..., 3]
    return np.stack((z, w, -w.conj(), z.conj()), axis=-1).reshape(q.shape[:-1]+(2, 2))


def dagger(a):
    return a.conj().swapaxes(-1, -2)


def links(v):
    angles = np.linalg.norm(v, axis=1)/4
    return matrices(np.column_stack((np.cos(angles), v*(np.sinc(angles/np.pi)/4)[:, None])))


def action(left, right, g):
    sites = matrices(g)
    loops = left @ sites[NEIGHBORS] @ dagger(right) @ dagger(sites)[:, None]
    return np.sum(1-np.trace(loops, axis1=-2, axis2=-1).real/2)


def blocks(left, right):
    basis = matrices(BASIS)
    rotations = np.trace(dagger(basis)[None, :, None] @ left[:, None, None]
                         @ basis[None, None, :] @ dagger(right)[:, None, None],
                         axis1=-2, axis2=-1).real/2
    symmetric = (rotations + rotations.swapaxes(-1, -2))/2
    return 3*BASIS - np.einsum("ki,imn->kmn", SIGNS, symmetric), symmetric


def main():
    rng = np.random.default_rng(20261123)
    worst = 0.
    for scale in (.01, .25, 3., 9.):
        for _ in range(40):
            left, right = (links(rng.normal(size=(3, 3))*scale) for _ in range(2))
            g = rng.normal(size=(8, 4))
            g /= np.linalg.norm(g, axis=1)[:, None]
            h, b = blocks(left, right)
            modes = FOURIER @ g
            observed = action(left, right, g)
            expected = np.einsum("ki,kij,kj->", modes, h, modes)
            worst = max(worst, abs(expected-observed))
            values, vectors = np.linalg.eigh(h)
            k = np.argmin(values[:, 0])
            minimizer = ((-1.)**(BITS @ BITS[k]))[:, None] * vectors[k, :, 0]
            assert abs(action(left, right, minimizer)-8*values[k, 0]) < 2e-13
            u = modes[0]/np.linalg.norm(modes[0])
            soft = 8 * u @ h[0] @ u
            unperturbed = np.sum((2*BITS.sum(axis=1))[:, None]*modes**2)
            bound = np.linalg.norm(BASIS-b, ord=2, axis=(1, 2)).sum()
            assert abs(observed-soft-unperturbed) <= bound*unperturbed + 2e-13
    assert worst < 2e-13
    c = np.array([pi, pi, 0.])
    d = np.array([pi, -pi, 0.])
    axial = lambda a: links(np.column_stack((a, np.zeros((3, 2)))))
    h, _ = blocks(axial(c), axial(d))
    assert abs(8*np.linalg.eigvalsh(h).min()-8) < 1e-13

    # One moving boundary gives an exact finite-beta temperature rescaling.
    reference = links(np.zeros((3, 3)))
    axes = np.eye(3)
    for t in (.05, .3, 1.):
        left = links(t*axes)
        lhs = action(left, reference, g)
        rhs = 24*(1-np.cos(t/4)) + np.cos(t/4)*action(reference, reference, g)
        assert abs(lhs-rhs) < 2e-13
    # Exact global-mode integral, with a removable singularity at equal costs.
    for t in (0., 1e-7, .1, 2., 25., 100.):
        got = quad(lambda p: np.exp(-t*p), 0., 1.)[0]
        assert abs(got-(1 if t == 0 else -np.expm1(-t)/t)) < 1e-13
    print(f"160 non-Abelian background pairs, largest action error {worst:.3g}; "
          "all minima, remainder bounds and six orientation integrals passed")


if __name__ == "__main__":
    main()
