"""Independent matrix tests for the three conditional fixed-box criteria."""
from itertools import product

import numpy as np


def norm(matrix):
    return np.linalg.norm(matrix, ord=2)


def outer(vector):
    return np.outer(vector, vector)


def two_signs(s, lam, mu):
    x, y = np.array(list(product([-1., 1.], repeat=2))).T
    mass = (1 + s*x*y)/4
    root = np.sqrt(mass)
    const = outer(root)
    slow = outer(root*x)
    fast = np.eye(4) - const - slow
    # Rows of the physical Markov kernel act on unweighted functions.
    observed = outer(root*y)
    residual = np.eye(4) - const - observed
    centered = lam*slow + mu*fast
    transition = (centered + const) * root[None, :] / root[:, None]
    np.testing.assert_allclose(transition.sum(axis=1), 1.)
    np.testing.assert_allclose(mass @ transition, mass)
    assert transition.min() > -1e-14
    w = 1 - s*s
    np.testing.assert_allclose(1-norm(observed@centered@observed), 1-lam+(lam-mu)*w)
    np.testing.assert_allclose(norm(observed@centered@residual), (lam-mu)*s*np.sqrt(w))
    for m in [1, 3, 8]:
        power = np.linalg.matrix_power(centered, m)
        tail = np.linalg.solve(np.eye(4)-centered, power)
        np.testing.assert_allclose(norm(residual@power@residual), w*lam**m+(1-w)*mu**m, atol=2e-14)
        np.testing.assert_allclose(norm(residual@tail@residual),
                                   w*lam**m/(1-lam)+(1-w)*mu**m/(1-mu), atol=2e-12)


def reversible_control(rng):
    size = 8
    mass = rng.dirichlet(np.ones(size)*3)
    root = np.sqrt(mass)
    # A random reversible heat semigroup in stationary orthonormal coordinates.
    rates = rng.uniform(.01, 1., size=(size, size))
    conductance = rates + rates.T
    H = (np.diag(conductance.sum(axis=1)) - conductance)/np.outer(root, root)
    spec, basis = np.linalg.eigh(H)
    t = rng.uniform(.001, .04)
    lam = np.exp(-t*spec[1:])
    U = basis[:,1:]
    S = (U*lam) @ U.T
    categories = np.arange(size)//2
    Y = root[:,None]*np.eye(size//2)[categories]/np.sqrt(np.bincount(categories, weights=mass))
    P = Y@Y.T - outer(root)
    Q = np.eye(size)-Y@Y.T
    d, b = 1-max(lam), 1-norm(P@S@P)
    threshold = rng.uniform(.15, .9)
    c = 1-threshold
    m = int(rng.integers(1, 8))
    power = (U*lam**m)@U.T
    tail = (U*(lam**m/(1-lam)))@U.T
    factor = threshold**(1-m)
    theta = norm(Q@power@Q)
    eta = factor*norm(Q@tail@Q)
    assert min(c,d)+1e-12 >= min(c,b)/(1+eta)
    assert min(c,d)+1e-12 >= max(0,min(c,b)-factor*theta)
    # Smallest energy-projection constant on the prescribed slow band.
    inside = lam >= threshold
    if np.any(inside):
        normalized = U[:,inside]/np.sqrt(t*spec[1:][inside])
        cost = norm(normalized.T@Q@normalized)
    else:
        cost = 0.
    assert min(c,d)+1e-12 >= min(c,b)/(1+cost)
    # Test the finite-time witness using one exact slow mode and one mixed observable.
    for coeff in (np.eye(len(lam))[0], rng.normal(size=len(lam))):
        coeff = coeff/np.linalg.norm(coeff)
        filtered = U@(lam**m*coeff)
        b_replica = filtered@filtered - np.linalg.norm(P@filtered)**2
        np.testing.assert_allclose(b_replica, np.linalg.norm(Q@filtered)**2, atol=1e-14)
        lhs = max(0., np.sqrt(max(0., b_replica)) - threshold**m)**2
        temporal_difference = np.sum(coeff**2 * lam**(2*m) * (1-lam))
        assert lhs <= cost*(-np.log(threshold))/(1-threshold)*temporal_difference + 1e-12
    kernel = (power + outer(root))/np.outer(root, root)
    full_projection = Y@Y.T
    W = full_projection*root[None,:]/root[:,None]
    remainder = kernel-W@kernel-kernel@W.T+W@kernel@W.T
    np.testing.assert_allclose(remainder*np.outer(root,root), Q@power@Q,atol=1e-14)
    assert theta <= max(abs(remainder)@mass)+1e-13


if __name__=="__main__":
    rng = np.random.default_rng(714203)
    for _ in range(150):
        mu, lam = sorted(rng.uniform(.02,.99,2))
        two_signs(rng.uniform(.01,.99),lam,mu)
    for _ in range(500):
        reversible_control(rng)
    for L in (4,16,64):
        w,lam,mu = L**-2,1-L**-4,L**-6
        first = sum(w*lam**k+(1-w)*mu**k for k in range(1,5))
        tail = w*lam/(1-lam)+(1-w)*mu/(1-mu)
        print(f"L={L}: four measured lags {first:.8f}, entire sum {tail:.8f}")
    print("150 exactly solvable chains and 500 random semigroups passed.")
