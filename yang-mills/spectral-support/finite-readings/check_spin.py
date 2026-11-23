"""Exact Sturm brackets on one physical cycle and numerical multi-link tail controls."""
from fractions import Fraction as F
from math import prod

import numpy as np
from scipy.linalg import eigh


def sturm(x, dimension):
    # Leading determinants of 2*denominator*(H-x) have integral coefficients.
    d, m = x.denominator, x.numerator
    previous, value = 0, 1
    changes = 0
    for n in range(dimension):
        diagonal = 2*(d*(n*(n+2)+1)-m)
        previous, value = value, diagonal*value-d*d*previous
        if not value:
            raise ArithmeticError("leading minor vanishes; choose another endpoint")
        changes += previous*value < 0
    return changes


def bracket(index, dimension, decimals):
    scale = 10**decimals
    low, high = -scale, 6*scale
    while high-low > 1:
        middle = (low+high)//2
        # A zero pivot at an intermediate grid point does not invalidate
        # the final bracketing test. Try a neighboring grid point instead.
        for trial in (middle, middle+1, middle-1):
            if not low < trial < high:
                continue
            try:
                number = sturm(F(trial, scale), dimension)
                break
            except ArithmeticError:
                continue
        else:
            raise ArithmeticError("unresolved grid point")
        if number <= index:
            low = trial
        else:
            high = trial
    assert sturm(F(low, scale), dimension) == index
    assert sturm(F(high, scale), dimension) == index+1
    return F(low, scale), F(high, scale)


def exact_cycle():
    j = 8
    # Remove the constant 1 when applying the tail lemma. A two-character
    # trial and ||W||<=1 give an excitation-energy cap of 5.
    def tail(k):
        return prod((F(1, n*(n+2)-5) for n in range(2, k+1)), start=F(1))
    t, u = tail(j), tail(j+1)
    error = (5*u*u+t*u/2)/(1-u*u)
    lo0, hi0 = bracket(0, j+1, 12)
    lo1, hi1 = bracket(1, j+1, 12)
    lower, upper = lo1-hi0-error, hi1-lo0+error
    print("single square at g=1, highest label 8; rational Ritz brackets")
    print("ground", lo0, hi0, "excited", lo1, hi1)
    print("common Ritz error <=", error)
    scale = 10**12
    print("infinite-cycle gap, outward integer endpoints over 10^12:",
          (lower*scale).__floor__(), (upper*scale).__ceil__())
    assert upper-lower < F(3, scale)
    return lower, upper


def coupled_links():
    n = 9
    labels = np.arange(n)
    diag = np.diag(labels*(labels+2))
    step = (np.diag(np.ones(n-1), 1)+np.diag(np.ones(n-1), -1))/2
    lam = 0.7
    h = np.kron(diag, np.eye(n))+np.kron(np.eye(n), diag)-lam*np.kron(step, step)
    energies, vectors = eigh(h)
    s = 6.5
    subspace = vectors[:, energies <= energies[0]+s]
    spins = np.indices((n, n)).reshape(2, -1)
    assert subspace.shape[1] == 4
    tails = [1.]
    for k in range(1, n):
        den = k*(k+2)-s
        tails.append(min(1., tails[-1]*lam/den) if den > 0 else 1.)
        for label in spins:
            actual = np.linalg.norm(subspace[label >= k], 2)
            assert actual <= tails[-1]+2e-14
    for j in (2, 3, 4, 5):
        selected = (spins <= j).all(axis=0)
        cutoff = np.linalg.eigvalsh(h[np.ix_(selected, selected)])[:4]
        defect = np.max(cutoff-energies[:4])
        lost = 2*tails[j+1]**2
        error = (s*lost+2*lam*tails[j]*tails[j+1])/(1-lost)
        assert -1e-12 <= defect <= error+1e-12
        print(f"coupled two-label control, J={j}, rank=4, Ritz error={defect:.4e}, bound={error:.4e}")
    # A non-fundamental multiplier that jumps directly from 0 to 2 defeats
    # the two-step recurrence derived from nearest-neighbor representation support.
    jumped = np.diag([0., 3., 8.])
    jumped[0, 2] = jumped[2, 0] = .1
    _, vectors = eigh(jumped)
    assert abs(vectors[2, 0]) > (.1/3)*(.1/8)
    print("Two-label jump rejected the nearest-neighbor tail estimate.")


if __name__ == "__main__":
    exact_cycle()
    coupled_links()
