"""Exact tetrahedral contractions and numerical ultraviolet limits (SciPy, SymPy)."""
import math
from itertools import combinations, permutations, product

from scipy.integrate import quad
from scipy.special import k1
from sympy import Matrix, eye, prod


def cycle_traces(vertices):
    pairs = list(combinations(range(4), 2))
    edges = {}
    for i, j in permutations(range(4), 2):
        vector = vertices[i] - vertices[j]
        reflection = eye(4) - 2 * vector * vector.T / vector.dot(vector)
        edges[i, j] = Matrix(6, 6, lambda a, b: reflection.extract(pairs[a], pairs[b]).det())
    traces = []
    for tail in permutations(range(1, 4)):
        cycle = (0, *tail)
        traces.append(prod(edges[i, j] for i, j in zip(cycle, cycle[1:] + (0,))).trace())
    return traces


def scaled_kernel(ell, power):
    """Return pi² r⁴ ell^power G_power(r) for Lambda=1 and log(M)=2."""
    lower = math.exp(2 - ell)

    def integrand(t):
        return (t*t*k1(t)/2) * (ell / (ell + math.log(t)))**power

    return sum(quad(integrand, a, b, epsabs=3e-13, epsrel=3e-12)[0]
               for a, b in [(lower, 1), (1, 10), (10, 100)])


def test_limits(ell, eta):
    # q=1, A=pi² sets C=1. A scalene triangle challenges common-edge substitutions.
    lens = (1.0, 1.25, 1.75)
    base, correction = [], []
    for length in lens:
        local = ell - math.log(length)
        base.append(scaled_kernel(local, 1) * ell / local)
        correction.append(eta * scaled_kernel(local, 2) * ell / local**2)
    pair = ((base[0]+correction[0])**2 + base[0]**2)/2
    # Sum the seven nonempty choices directly to avoid cancellation.
    triangle = ell * sum(math.prod((base, correction)[choice][i]
                                   for i, choice in enumerate(choices))
                         for choices in product((0, 1), repeat=3) if any(choices))
    return pair, triangle


if __name__ == "__main__":
    tetra = list(map(Matrix, [(1,1,1,0), (1,-1,-1,0), (-1,1,-1,0), (-1,-1,1,0)]))
    assert cycle_traces(tetra) == [0]*6
    assert cycle_traces([Matrix([i,0,0,0]) for i in range(4)]) == [6]*6
    print("Directed exterior-square traces: tetrahedron 6 x 0; collinear 6 x 6")
    for eta in (-0.5, 0, 0.75):
        for ell in (20, 100, 400):
            two, three = test_limits(ell, eta)
            print(f"eta={eta:g} log={ell} two={two:.9f} triangle={three:.9f}")
        assert abs(two-1) < 0.006 and abs(three-3*eta) < 0.015
