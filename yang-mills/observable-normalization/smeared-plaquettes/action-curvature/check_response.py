"""Check an isolated Wilson rotor and a narrow-response family independently."""
import numpy as np
from scipy.linalg import eigh_tridiagonal


def rotor(size, g):
    n = np.arange(size)
    levels, vectors = eigh_tridiagonal(n*(n+2) + g, np.full(size-1, -g/2))
    vacuum = vectors[:, 0]
    trace_state = np.zeros(size)
    trace_state[:-1] += vacuum[1:]
    trace_state[1:] += vacuum[:-1]
    action = 1 - (vacuum @ trace_state)/2
    weights = (vectors[:, 1:].T @ trace_state)**2
    excitation = levels[1:] - levels[0]
    return action, weights.sum(), weights @ excitation, weights @ (1/excitation)


def scan(size, G):
    nodes, weights = np.polynomial.legendre.leggauss(24)
    g = G*(1.5 + nodes/2)
    data = np.array([rotor(size, t) for t in g])
    weights = weights/2
    integral = G*(weights @ data[:, 3])
    budget = 2*(rotor(size, G)[0] - rotor(size, 2*G)[0])
    if abs(integral - budget) > 2e-11:
        raise AssertionError((size, G, integral, budget))
    center = 1.5*G
    h = center*1e-4
    slope = (rotor(size, center+h)[0] - rotor(size, center-h)[0])/(2*h)
    if not np.isclose(-2*slope, rotor(size, center)[3], rtol=5e-7, atol=1e-14):
        raise AssertionError("curvature normalization")
    var, first, inv = data[:, 1:].T
    if np.any(var**2 > first*inv + 1e-12):
        raise AssertionError("inverse interpolation")
    r = np.sqrt(G)
    return np.array([r*integral, np.sqrt(weights @ ((G*var)**2)),
                     weights @ (first/(r*var)), weights @ (r*inv/var)])


def crossing(G):
    r, epsilon, center = np.sqrt(G), G**-2., 1.5*G
    ident, x, z = np.eye(2), np.array([[0., 1.], [1., 0.]]), np.diag([1., -1.])
    magnetic1 = (ident+z)/r
    magnetic2 = np.diag([1/r, 0])
    electric1 = r*(ident+x)
    electric2 = np.array([[epsilon, epsilon], [epsilon, center/r+epsilon]])
    # Diagonalize each factor before forming product spectral weights. This resolves
    # the small splitting even when the common additive energy is very large.
    states = []
    for electric, magnetic in ((electric1, magnetic1), (electric2, magnetic2)):
        h = electric + center*magnetic
        energy, basis = np.linalg.eigh(h - h.trace()*ident/2)
        states.append((energy[1]-energy[0], (basis[:, 1] @ (-2*magnetic) @ basis[:, 0])**2))
    (fast, wf), (slow, ws) = states
    fraction = ws/(ws+wf)
    if not np.allclose([fast/r, slow/epsilon, fraction], [np.sqrt(13), 2, 13/29]):
        raise AssertionError((G, states, fraction))
    return fraction


if __name__ == "__main__":
    for G in (16, 64, 256, 1024):
        smaller, larger = scan(64, G), scan(128, G)
        if not np.allclose(smaller, larger, rtol=2e-8, atol=2e-10):
            raise AssertionError((G, smaller, larger))
        print(G, *(f"{v:.9g}" for v in larger), f"{crossing(G):.9g}")
