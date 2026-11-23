"""Check the magnetic factor order and moving resolvent shift on noncommuting matrices."""
import numpy as np
from scipy.linalg import expm


def check_pair(kinetic, potential):
    identity = np.eye(len(kinetic))
    c = 2 + np.linalg.norm(potential, 2)
    a = 1/(40*c)
    free_step = expm(-a*kinetic)
    free_difference = (identity - free_step)/a
    multiplier = expm(-a*potential/2)
    potential_step = (expm(a*potential)-identity)/a
    difference = (identity - multiplier @ free_step @ multiplier)/a
    hamiltonian = kinetic + potential
    x = np.linalg.inv(free_difference + c*identity)
    y = np.linalg.inv(kinetic + c*identity)
    u = np.linalg.inv(free_difference + c*identity + potential)
    v = np.linalg.inv(hamiltonian + c*identity)
    magnetic = multiplier @ (free_difference + c*identity + (1+a*c)*potential_step) @ multiplier
    correct = (identity-u@potential) @ (x-y) @ (identity-potential@v)
    reversed_order = (identity-potential@u) @ (x-y) @ (identity-v@potential)
    exact = max(np.linalg.norm(difference+c*identity-magnetic, 2), np.linalg.norm(u-v-correct, 2))
    wrong = np.linalg.norm(u-v-reversed_order, 2)
    e = min(np.linalg.eigvalsh(difference)[0], np.linalg.eigvalsh(hamiltonian)[0])
    ratio = 0.
    for eta in (0.1, 1., 10., 100.):
        for operator in (difference, hamiltonian):
            bound = max(1., (c+e)/eta)
            factor = (operator+c*identity) @ np.linalg.inv(operator+(eta-e)*identity)
            ratio = max(ratio, np.linalg.norm(factor, 2)/bound)
    return exact, wrong, ratio


if __name__ == "__main__":
    rng = np.random.default_rng(4242)
    results = []
    for _ in range(40):
        x = rng.normal(size=(5, 5))
        y = rng.normal(size=(5, 5))
        results.append(check_pair(x.T@x, y.T@y))
    exact, wrong, ratio = np.max(results, axis=0)
    assert exact < 1e-10 and wrong > 1e-7 and ratio < 1+1e-11
    print(f"40 noncommuting 5x5 pairs; ordered residual {exact:.3e}; "
          f"reversed residual {wrong:.3e}; max shift-factor norm/envelope {ratio:.9f}")
