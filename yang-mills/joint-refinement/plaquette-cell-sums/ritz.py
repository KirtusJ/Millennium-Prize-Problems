"""Check the conditional-variance form and the small-deficit partition enclosure."""
import numpy as np


def centered_spectrum(matrix, mass):
    stationary = np.sqrt(mass)
    return np.linalg.eigvalsh(matrix - np.outer(stationary, stationary))[-1]


def check(rng, nearly_disconnected):
    groups = np.repeat(np.arange(3), [2, 3, 4])
    membership = np.eye(3)[groups]
    if nearly_disconnected:
        mix = 10.0 ** rng.uniform(-11, -2)
        factors = (membership + mix) * rng.lognormal(0, .3, membership.shape)
    else:
        factors = rng.lognormal(0, .5, (len(groups), 6))
    joint = factors @ factors.T
    joint /= joint.sum()
    mass = joint.sum(axis=1)
    rows = joint / mass[:, None]
    cell_joint = membership.T @ joint @ membership
    cell_mass = cell_joint.sum(axis=1)
    root = np.sqrt(mass)
    matrix = joint / np.outer(root, root)
    projection_basis = root[:, None] * membership / np.sqrt(cell_mass)
    projection = projection_basis @ projection_basis.T
    cell_matrix = cell_joint / np.sqrt(np.outer(cell_mass, cell_mass))
    lam = centered_spectrum(matrix, mass)
    cell_lam = centered_spectrum(cell_matrix, cell_mass)

    log_spread = 0.
    pair_chi = 0.
    for index, group in enumerate(groups):
        within = groups == group
        ratio = rows[within] / rows[index]
        log_spread = max(log_spread, np.ptp(np.log(ratio), axis=1).max())
        chi_square = ((ratio - 1) ** 2) @ rows[index]
        pair_chi = max(pair_chi, np.dot(mass[within], chi_square) / cell_mass[group])
    identity = np.eye(len(groups))
    for u in [np.sinh(log_spread / 2) ** 2 / 2, pair_chi / 2]:
        residual = u * (identity - matrix @ matrix) - matrix @ (identity - projection) @ matrix
        assert np.linalg.eigvalsh(residual)[0] >= -2e-12 * (1 + u)
        denominator = 2 * (1 + u) - cell_lam + np.sqrt(cell_lam**2 + 4*u*(1+u))
        lower = 2 * (1 - cell_lam) / denominator
        assert 1 - lam + 2e-14 >= lower
        assert min(.5, 1 - lam) + 2e-14 >= min(.5, 1 - cell_lam) / (1 + 3*u)


if __name__ == "__main__":
    rng = np.random.default_rng(917033)
    for i in range(600):
        check(rng, i % 2 == 0)
    print("600 reversible partition checks passed for both row coefficients")
