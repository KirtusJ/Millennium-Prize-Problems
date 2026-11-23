"""Verify all spatial faces and all link velocities on periodic quarter-flux fields."""
from itertools import combinations, product


def check(side):
    sites = list(product(range(side), repeat=3))
    axes = range(3)
    velocity = {(x, i): 0 for x in sites for i in axes}
    sine = (0, 1, 0, -1)

    def step(x, i):
        y = list(x)
        y[i] = (y[i] + 1) % side
        return tuple(y)

    def exponent(x, i):
        if i == 0 and x[0] == side-1:
            return -side*x[1]
        return x[0] if i == 1 else 0

    for x in sites:
        for i, j in combinations(axes, 2):
            edges = [(x, i, 1), (step(x, i), j, 1),
                     (step(x, j), i, -1), (x, j, -1)]
            flux = sum(s*exponent(y, k) for y, k, s in edges) % 4
            assert flux == int((i, j) == (0, 1))
            for y, k, s in edges:
                velocity[y, k] += s*sine[flux]
    assert all(v == 0 for v in velocity.values())
    print(f"L={side}: {3*side**3} oriented faces, {len(velocity)} zero velocities")


if __name__ == "__main__":
    for side in (4, 6, 8, 10):
        check(side)
