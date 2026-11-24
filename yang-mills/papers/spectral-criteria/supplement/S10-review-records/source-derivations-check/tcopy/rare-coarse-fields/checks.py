"""Independent quadratures and finite-state checks for the rare-set criterion."""
from functools import lru_cache
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full-complement"))
from disk import quotient


@lru_cache(maxsize=None)
def rule(order):
    return np.polynomial.legendre.leggauss(order)


def integral(theta, k, alpha, order):
    # Polar coordinates around the cap centre. At fixed radius the remaining
    # directional cosine is uniform on [-1,1] on the transverse two-sphere.
    nodes, weights = rule(order)
    r = (1 + nodes) * theta / 2
    v = k * np.sin(alpha) * np.sin(r)
    transverse = np.ones_like(v)
    nonzero = np.abs(v) > 1e-10
    transverse[nonzero] = -np.expm1(-2 * v[nonzero]) / (2 * v[nonzero])
    scaled = np.exp(-2 * k * np.sin((r-alpha)/2)**2) * transverse
    return theta / np.pi * np.dot(weights, np.sin(r)**2 * scaled)


def cap_checks():
    for beta in (0, 1, 3.399810242, 16, 64):
        k = 6 * beta
        norm = integral(np.pi, k, 0, 240)
        for theta in (.05, .2, .6):
            cap = integral(theta, k, 0, 240) / norm
            np.testing.assert_allclose(cap, integral(theta,k,0,160) /
                                       integral(np.pi,k,0,160), rtol=1e-10)
            haar = (theta - np.sin(theta)*np.cos(theta))/np.pi
            assert cap <= haar / norm + 1e-12
            assert cap <= np.pi**2 * np.sqrt(np.e)/4 * ((1+k)**.5 * theta)**3 + 1e-12
            for alpha in (0.1, .8, 1.9, np.pi):
                assert integral(theta, k, alpha, 240) / norm <= cap + 1e-12
            if beta == 0:
                np.testing.assert_allclose(cap, haar, atol=1e-12)
            if beta == 3.399810242:
                print(f"beta={beta}, theta={theta}, sharp one-link cap={cap:.9f}")


def matrix_checks():
    # A reversible Markov generator on three coarse labels, each with two fine states.
    rng = np.random.default_rng(75281)
    for i in range(120):
        pi = rng.dirichlet(np.full(6, 1.4))
        vacuum = np.sqrt(pi)
        edges = np.triu(rng.uniform(.01, 1, (6, 6)), 1)
        edges += edges.T.copy()
        lap = np.diag(edges.sum(axis=1)) - edges
        H = lap / np.outer(vacuum, vacuum)
        eigen, vectors = np.linalg.eigh(H)
        np.testing.assert_allclose(eigen[0], 0, atol=1e-9)
        assert eigen[1] > 0
        C = np.zeros((6, 3))
        for label in range(3):
            C[2*label:2*label+2, label] = vacuum[2*label:2*label+2]
        C /= np.linalg.norm(C, axis=0)
        centred_coarse = C @ C.T - np.outer(vacuum, vacuum)
        Q = np.eye(6) - C @ C.T
        bad = Q.copy()
        bad[:4] = 0
        good = Q - bad
        a, t, tau = .003, .15, .15 if i % 2 else .075
        def semigroup(time):
            return (vectors * np.exp(-time*eigen)) @ vectors.T
        inverse = (vectors[:, 1:] / (-np.expm1(-2*a*eigen[1:]))) @ vectors[:, 1:].T
        gamma = 1 / np.linalg.eigvalsh(good @ inverse @ good)[-1]
        assert np.linalg.eigvalsh(np.eye(6)-semigroup(2*a)-gamma*good)[0] > -1e-10
        b = 1 - np.linalg.eigvalsh(centred_coarse @ semigroup(t) @ centred_coarse)[-1]
        kappa = np.linalg.eigvalsh(bad @ semigroup(tau) @ bad)[-1]
        d = -np.expm1(-t*eigen[1])
        assert b-kappa <= d*(1+2*a/(gamma*t)) + 1e-11
    print("120 centered Markov spectral-window checks passed")


if __name__ == "__main__":
    cap_checks()
    matrix_checks()
    for beta in (16, 64, 256, 1024, 4096):
        result = quotient(beta, 384)[2]
        np.testing.assert_allclose(result, quotient(beta, 512)[2], atol=1e-11)
        print(f"disk beta={beta}, three-update quotient={result:.8f}")
