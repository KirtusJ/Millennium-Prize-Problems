"""Read back every time entry of exact realizations and challenge false gap fits."""
from pathlib import Path
import sys
from random import Random

import sympy as sp

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from moments import Incompatible, even_completion, lobatto_completion, odd_completion, psd

R = sp.Rational


def observations(atoms, degree):
    return [sum((u**k*weight for u, weight in atoms), sp.zeros(atoms[0][1].rows)).applyfunc(sp.expand)
            for k in range(degree+1)]


def verify(model, blocks):
    assert all(model.reading(i) == value for i, value in enumerate(blocks))
    assert psd(model.metric) and psd(model.vacuum) and psd(model.zero_atom)
    assert model.metric.rank() == model.metric.rows
    assert (model.transfer.H*model.metric-model.metric*model.transfer).applyfunc(sp.expand).is_zero_matrix


def rejects(action):
    try:
        action()
    except Incompatible:
        return
    raise AssertionError("an impossible completion passed")


def free_cycle():
    u, v, q = R(1, 8), R(1, 256), R(1, 16)
    plus = sp.Matrix([1, 1])
    minus = sp.Matrix([8, -8])
    blocks = observations([(u, plus*plus.H), (v, minus*minus.H)], 5)
    projected = sp.Matrix([R(1, 2), R(1, 2)])
    score = projected.H*(-blocks[2]+(1+q)*blocks[1]-q*blocks[0])*projected
    assert score[0] == R(7, 128) and 4*score[0]/(1-q)**2 == R(56, 225)
    for channel in (0, 1):
        diagonal = [sp.Matrix([b[channel, channel]]) for b in blocks]
        for degree, fit in ((2, even_completion), (3, odd_completion), (3, lobatto_completion)):
            verify(fit(diagonal[:degree+1], q), diagonal[:degree+1])
        a, b = R(1, 1024), R(133, 2552)
        gapped = observations([(a, sp.Matrix([R(984064, 16705)])),
                               (b, sp.Matrix([R(101761, 16705)]))], 2)
        assert 0 < a < b < q and gapped == diagonal[:3]
    for degree, fit in ((2, even_completion), (3, odd_completion), (3, lobatto_completion)):
        rejects(lambda: fit(blocks[:degree+1], q))
        verify(fit(blocks[:degree+1], u), blocks[:degree+1])
    print("SU(2): both individual channels fit q=1/16; joint reading fails at degrees 2 and 3.")
    print("Polarized excess 7/128; certified raw mass at least 56/225 strictly between q and 1.")


def endpoints():
    # The sole channel has transfer mean 1/2. Maximizing the vacuum at low=0
    # gives zero transfer on its orthogonal complement. A positive lower bound
    # constructs a finite Hamiltonian with exactly the same two observations.
    data = [sp.Matrix([1]), sp.Matrix([R(1, 2)])]
    first = odd_completion(data, R(1, 2))
    verify(first, data)
    assert not first.has_finite_energies() and first.vacuum[0] == R(1, 2)
    second = odd_completion(data, R(1, 2), low=R(1, 4))
    verify(second, data)
    assert second.has_finite_energies() and second.vacuum[0] == R(1, 3)
    zero_data = observations([(0, sp.eye(1))], 3)
    verify(odd_completion(zero_data, R(1, 2)), zero_data)
    rejects(lambda: odd_completion(zero_data, R(1, 2), low=R(1, 1024)))
    pure = observations([(1, sp.eye(2))], 5)
    for fit, stop in ((even_completion, 5), (odd_completion, 6), (lobatto_completion, 6)):
        model = fit(pure[:stop], R(1, 2))
        verify(model, pure[:stop])
        assert model.transfer.rows == 0
    print("Vacuum-only, null input subspaces and forced/optional zero transfer distinguished.")


def matrix_cases():
    # A complex off-diagonal and a repeated probe force both polarization
    # and kernel handling. Measure supports include both endpoints.
    a = sp.Matrix([1, sp.I, 1])
    b = sp.Matrix([1, 2, 1])
    c = sp.Matrix([1, 1-sp.I, 1])
    e = sp.Matrix([1, -1, 1])
    atoms = [(0, e*e.H), (R(1, 5), a*a.H), (R(2, 3), b*b.H), (1, c*c.H)]
    data = observations(atoms, 7)
    for degree in range(1, 8):
        tests = (odd_completion, lobatto_completion) if degree % 2 else (even_completion,)
        for fit in tests:
            verify(fit(data[:degree+1], R(2, 3)), data[:degree+1])
    rejects(lambda: even_completion(data[:7], R(1, 2)))
    rejects(lambda: odd_completion(data, R(1, 2)))
    rejects(lambda: lobatto_completion(data, R(1, 2)))
    corrupt = list(data[:3])
    corrupt[0] = -sp.eye(3)
    rejects(lambda: even_completion(corrupt, R(2, 3)))
    assert not psd(sp.Matrix([[0, sp.I], [-sp.I, 2]]))
    print("Exact complex rank-deficient matrices: 7 truncations reproduced; undersized bands and nonpositive input rejected.")


def crosscheck_constructions():
    rng = Random(65537)
    accepted = rejected = 0
    for _ in range(6):
        atoms = []
        for node in (0, R(1, 8), R(1, 3), R(2, 3), 1):
            v = sp.Matrix([rng.randrange(-2, 3)+sp.I*rng.randrange(-2, 3) for _ in range(2)])
            atoms.append((node, v*v.H))
        readings = observations(atoms, 5)
        for high in (R(1, 4), R(2, 5), R(3, 4)):
            for degree in (3, 5):
                outcomes = []
                for construction in (odd_completion, lobatto_completion):
                    try:
                        model = construction(readings[:degree+1], high)
                    except Incompatible:
                        outcomes.append(False)
                    else:
                        verify(model, readings[:degree+1])
                        outcomes.append(True)
                assert outcomes[0] == outcomes[1]
                if outcomes[0]:
                    accepted += 1
                else:
                    rejected += 1
    assert accepted and rejected
    print(f"Independent odd-order constructions agree on {accepted} accepted and {rejected} rejected rational trials.")


if __name__ == "__main__":
    free_cycle()
    endpoints()
    matrix_cases()
    crosscheck_constructions()
