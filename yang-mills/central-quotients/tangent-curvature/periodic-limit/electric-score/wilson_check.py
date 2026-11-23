"""Two adjacent SU(2) squares, using seven independent stationary link pairs."""
import numpy as np
from scipy.special import iv
from scipy.stats import vonmises_fisher


def multiply(a, b):
    scalar = a[..., :1] * b[..., :1] - np.sum(a[..., 1:] * b[..., 1:], axis=-1, keepdims=True)
    vector = a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:] + np.cross(a[..., 1:], b[..., 1:])
    return np.concatenate((scalar, vector), axis=-1)


def trace(word):
    value = word[0]
    for link in word[1:]:
        value = multiply(value, link)
    return 2 * value[:, 0]


def square_readings(links):
    # Orient both words along the shared edge. SU(2) traces are real and
    # invariant under reversing the whole loop. Each private edge occurs once.
    return trace(links[[0, 1, 2, 3]]), trace(links[[0, 4, 5, 6]])


def run(g=7., batches=80, batch_size=2048):
    rng = np.random.default_rng(20261123)
    noise = vonmises_fisher([1., 0., 0., 0.], g)
    values = [[], []]
    for _ in range(batches):
        u = rng.normal(size=(7, batch_size, 4))
        u /= np.linalg.norm(u, axis=-1, keepdims=True)
        x, y = square_readings(u)
        w = u
        for rows in values:
            step = noise.rvs(size=7 * batch_size, random_state=rng).reshape(w.shape)
            w = multiply(w, step)
            a, b = square_readings(w)
            xp, xr = x * a, y * b
            rows.append([xp.mean(), (xp**2).mean(), (xp*xr).mean()])
    for n, rows in enumerate(values, 1):
        a, b = (iv(j, g)**n / iv(1, g)**n for j in (2, 3))
        expected = np.array([a**4, 1+b**4, a**6*(1+3*b)/4])
        estimate = np.mean(rows, axis=0)
        se = np.std(rows, axis=0, ddof=1) / np.sqrt(batches)
        print(n, "estimate", estimate, "expected", expected, "batch SE", se)
        if np.any(np.abs(estimate-expected) > 6*se):
            raise AssertionError("sample moment outside the six-standard-error control")


if __name__ == "__main__":
    run()
