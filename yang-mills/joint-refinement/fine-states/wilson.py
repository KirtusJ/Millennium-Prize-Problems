"""Local spin-tail certificate and a compact interacting SU(2) plaquette control."""
from fractions import Fraction as F
from math import factorial
import numpy as np
from scipy.special import ive


def exp_upper(x):
    end = int(x) + 40
    return (sum(x**j / factorial(j) for j in range(end + 1))
            + x**(end+1) / factorial(end+1) / (1 - x / (end+2)))


def cutoff(side, beta):
    # For each omitted n, successive factorial-envelope terms have ratio beta/(2n+4).
    prefactor = 3 * side**3 * exp_upper(8 * beta)
    for n in range(1, 2000):
        omitted = prefactor * (beta/2)**n / factorial(n+1)
        if beta < 2*n+4 and omitted <= F(1, side**3):
            return n-1, float(omitted)
    raise ValueError("increase the search range")


def norm(a):
    return float(np.linalg.norm(a, 2))


def plaquette(nodes, beta=1.6, steps=4, last=2):
    # Character quadrature for one open square modulo vertex gauge.
    theta = np.arange(1, nodes+1)*np.pi/(nodes+1)
    degrees = np.arange(nodes)
    chars = np.sqrt(2/(nodes+1))*np.sin(theta[:, None]*(degrees+1))
    np.testing.assert_allclose(chars.T @ chars, np.eye(nodes), atol=5e-14)
    magnetic = np.exp(-beta*(1-np.cos(theta))/2)
    kinetic = (ive(degrees+1, beta)/ive(1, beta))**4
    full = magnetic[:, None]*chars*np.sqrt(kinetic)
    transfer = full @ full.T
    eigen, states = np.linalg.eigh(transfer)
    vacuum = states[:, -1]
    h = transfer/eigen[-1]
    s = np.linalg.matrix_power(h, steps)
    coarse = vacuum*(np.cos(theta) > 0)
    coarse -= vacuum @ coarse * vacuum
    coarse /= np.linalg.norm(coarse)
    p = np.outer(coarse, coarse)
    q = np.eye(nodes)-p-np.outer(vacuum, vacuum)
    x = full[:, :last+1]/np.sqrt(eigen[-1])
    hlow = x @ x.T
    eps = kinetic[last+1]/eigen[-1]
    assert norm(h-hlow) <= eps+1e-13
    frame, _ = np.linalg.qr(np.column_stack((vacuum, coarse)), mode="complete")
    fine = frame[:, 2:]
    vec, singular, _ = np.linalg.svd(fine.T @ x, full_matrices=False)
    retained = fine @ vec[:, singular > np.finfo(float).eps*nodes]
    r = retained @ retained.T
    tail = q-r
    assert norm(hlow @ tail) < 1e-12
    a, b, eta = norm(p @ s @ p), norm(q @ s @ q), norm(p @ s @ q)
    assert norm(tail @ s @ tail) <= eps**2 + 3e-14
    assert b <= norm(r @ s @ r) + eps**2 + 3e-14
    assert eta**2 <= norm(p @ s @ r)**2 + a*eps**2 + 3e-14
    gram, vectors = np.linalg.eigh(x.T @ x)
    z = x @ ((vectors*gram**((steps-1)/2)) @ vectors.T)
    gp, gq = z.T @ p @ z, z.T @ q @ z
    np.testing.assert_allclose(z @ z.T, np.linalg.matrix_power(hlow, steps), atol=1e-14)
    assert abs(b-norm(gq)) <= steps*eps+1e-13
    sqrt_vals, u = np.linalg.eigh(gq)
    root = (u*np.sqrt(np.maximum(0, sqrt_vals))) @ u.T
    eta_low = np.sqrt(norm(root @ gp @ root))
    assert abs(eta_low-eta) <= steps*eps+1e-13
    assert eta > 1e-8 and abs(eta_low-norm(p @ z @ z.T @ q)) < 1e-13
    return b, eta, eps


if __name__ == "__main__":
    for size in (5, 6, 7, 8, 10):
        print("N, cutoff, relative error upper", size, *cutoff(size, F(7, 2)))
    for nodes in (48, 96, 192):
        print("plaquette nodes, b, eta, one-step error upper", nodes, *plaquette(nodes))
