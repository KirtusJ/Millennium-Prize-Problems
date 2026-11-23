"""Wilson radial quadrature and quaternion controls for the path in (3)."""
from itertools import combinations
from math import exp, pi, sin, sinh
from scipy.integrate import quad


def radial_checks(beta):
    s = beta ** -0.5
    # The variable is the jump angle divided by s. The omitted tail beyond
    # 40 is Gaussian-small using 1-cos(d) >= 2*d*d/pi**2.
    stop = min(pi / s, 40)

    def density(z):
        return (sin(s * z) / s) ** 2 * exp(-2 * (sin(s * z / 2) / s) ** 2)

    norm = quad(density, 0, stop)[0]
    jump = quad(lambda z: density(z) * 2 * (sinh(z / 8)) ** 2, 0, stop)[0] / norm
    # Haar probability of a ball, times the worst Wilson density at 3s/2.
    # This is a direct lower bound for one link at each interior path step.
    ball = quad(lambda z: (sin(s * z) / s) ** 2, 0, 0.25)[0]
    passage = ball / norm * exp(-2 * (sin(0.75 * s) / s) ** 2)
    return jump / 0.25 ** 2, passage


def cross_cost(beta, vectors):
    def squared_cross(x, y):
        return sum((x[i] * y[j] - x[j] * y[i]) ** 2
                   for i, j in combinations(range(3), 2))

    return 2 * beta * sum(squared_cross(x, y) for x, y in combinations(vectors, 2))


if __name__ == "__main__":
    for beta in (64, 4096, 262144):
        s = beta ** -0.5
        error, step = radial_checks(beta)
        # Equatorial active link and two orthogonal transverse deviations.
        t = sin(s / 4)
        middle = cross_cost(beta, [(1, 0, 0), (0, t, 0), (0, 0, t)])
        # Flipping two links about orthogonal axes at the same time instead
        # produces two orthogonal imaginary unit vectors at the midpoint.
        bad = cross_cost(beta, [(1, 0, 0), (0, 1, 0), (0, 0, 0)])
        assert 1 < error < 2 and step > 0.001
        assert 0.24 < middle < 0.26 and bad == 2 * beta
        print(f"beta={beta:6}  tilt/a^2={error:.6f}  step={step:.7f}"
              f"  sequential V={middle:.7f}  simultaneous V={bad:.0f}")
