"""Gaussian two-particle Rayleigh quotients. Lengths in units of R."""
import mpmath as mp


def minimum(count):
    widths = [1 + 3 * mp.mpf(i) / max(1, count - 1) for i in range(count)]
    cov = mp.matrix(count)
    energy = mp.matrix(count)
    for i, a in enumerate(widths):
        for j, b in enumerate(widths):
            cov[i, j] = mp.gamma(mp.mpf("2.5")) / (2 * (a + b)**mp.mpf("2.5"))
            energy[i, j] = 2 / (a + b)**3
    inv = mp.cholesky(cov)**-1
    values, vectors = mp.eigsy(inv * energy * inv.T)
    c = inv.T * vectors[:, 0]
    cost = sum(abs(z) for z in c)
    assert abs((c.T * cov * c)[0] - 1) < mp.mpf("1e-40")
    assert mp.mpf(5)/3 * (5 / cost**2)**mp.mpf(".2") <= values[0]
    return values[0], cost, widths, c


def periodic_check(side, widths, coefficients):
    """Zero total momentum, truncate at |R k| <= 8 for this numerical control."""
    step = 2 * mp.pi / side
    limit = int(8 / step)
    max_shell = int((8 / step)**2)
    # Convolve the one-coordinate sum of squares to get shell multiplicities.
    squares = [0] * (limit**2 + 1)
    for i in range(-limit, limit + 1):
        squares[i*i] += 1
    shells = {0: 1}
    for _ in range(3):
        counts = {}
        for shell, count in shells.items():
            for i in range(limit + 1):
                key = shell + i*i
                if key > max_shell:
                    break
                counts[key] = counts.get(key, 0) + count * squares[i*i]
        shells = counts
    norm = energy = mp.mpf(0)
    for shell, count in shells.items():
        r = step * mp.sqrt(shell)
        amplitude = mp.fsum(c * mp.exp(-s*r*r) for s, c in zip(widths, coefficients))
        weight = count * r*r * amplitude**2
        norm += weight
        energy += 2*r * weight
    return energy / norm


if __name__ == "__main__":
    for n in (1, 2, 4, 8, 12, 16):
        with mp.workdps(80):
            first = minimum(n)[:2]
        with mp.workdps(110):
            value, cost, widths, coefficients = minimum(n)
            result = (value, cost)
            assert all(abs(a/b - 1) < mp.mpf("1e-35") for a,b in zip(first, result))
            print(n, *(mp.nstr(x, 12) for x in result))
            if n == 4:
                for side in (16, 32, 64):
                    measured = periodic_check(side, widths, coefficients)
                    assert measured >= 4*mp.pi/side
                    print("box", side, mp.nstr(measured, 12))
