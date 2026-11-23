"""Character-basis control on one isolated SU(2) plaquette, in units kappa=1."""
import numpy as np
from scipy.linalg import eigh_tridiagonal


def trace_action(state):
    result = np.zeros_like(state)
    result[1:] += state[:-1]
    result[:-1] += state[1:]
    return result


def moments(size, coupling):
    n = np.arange(size)
    casimir = n * (n + 2)
    energies, vectors = eigh_tridiagonal(
        casimir + coupling, np.full(size - 1, -coupling / 2)
    )
    omega = vectors[:, 0]
    trace_state = trace_action(omega)
    centered = trace_state - (omega @ trace_state) * omega
    weight = (vectors.T @ centered) ** 2
    excitation = energies - energies[0]
    kinetic = (omega**2 @ casimir) / 4
    first = weight @ excitation
    second = weight @ excitation**2
    direct_first = 4 - trace_state @ trace_state
    commutator = casimir * trace_state - trace_action(casimir * omega)
    direct_second = commutator @ commutator
    a = 9 / (8 * (1 + kinetic))
    d = (6 + 8 * np.sqrt(kinetic)) ** 2
    low, high = a / 16, 4 * d / a
    band_weight = weight[(excitation >= low) & (excitation <= high)].sum()
    s, t = 0.2, 0.1
    difference = weight @ (np.exp(-t * excitation) * np.expm1(-s * excitation) ** 2)
    floor = a / (2 * high) * np.exp(-t * high) * np.expm1(-s * low) ** 2
    if (abs(first - direct_first) > 1e-9 or abs(second - direct_second) > 1e-8
            or first < a or second > d or band_weight < a / (2 * high)
            or difference < floor):
        raise AssertionError((size, coupling, first, second, band_weight, difference))
    return np.array([first, second, band_weight, difference])


def main():
    for coupling in (0, 1, 16, 256):
        smaller = moments(48, coupling)
        larger = moments(96, coupling)
        if not np.allclose(smaller, larger, rtol=1e-9, atol=1e-10):
            raise AssertionError((coupling, smaller, larger))
        print(coupling, *[f"{value:.9g}" for value in larger])
    if not np.allclose(moments(96, 0)[:3], [3, 9, 1]):
        raise AssertionError("free plaquette")


if __name__ == "__main__":
    main()
