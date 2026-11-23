"""Private-link geometry and mixed magnetic derivatives on periodic SU(2) cubes."""
from collections import defaultdict
from itertools import combinations, product
import numpy as np


def faces(side):
    def step(x, direction):
        out = list(x)
        out[direction] = (out[direction]+1) % side
        return tuple(out)

    return [[((x, a), 1), ((step(x, a), b), 1),
             ((step(x, b), a), -1), ((x, b), -1)]
            for x in product(range(side), repeat=3) for a, b in combinations(range(3), 2)]


def incidence(words):
    touching = defaultdict(set)
    for p, word in enumerate(words):
        for e, _ in word:
            touching[e].add(p)
    neighbors = [set.union(*(touching[e] for e, _ in word)) for word in words]
    return touching, neighbors


def opposite(word, e):
    return next(other for other, _ in word if other != e and other[1] == e[1])


def geometry(side):
    words = faces(side)
    touching, neighbors = incidence(words)
    clashes = sum(touching[opposite(words[p], e)].intersection(star) != {p}
                  for e, star in touching.items() for p in star)
    near = max(len(set.union(*(neighbors[j] for j in n))) for n in neighbors)
    assert all(len(star) == 4 for star in touching.values())
    if (side == 2) != (clashes > 0) or near > 145:
        raise AssertionError((side, clashes, near))
    return clashes, near


IDENTITY = np.eye(2, dtype=complex)
GENERATORS = 1j*np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])/2
BASIS = [IDENTITY, *(2*g for g in GENERATORS)]


def gradient(word, e, links):
    values = []
    for generator in GENERATORS:
        mat = IDENTITY
        for link, sign in word:
            factor = links[link]
            if link == e:
                factor = generator @ factor
            mat = mat @ (factor if sign > 0 else factor.conj().T)
        values.append(mat.trace().real)
    return np.array(values)


def action(words, links):
    value = 0.
    for word in words:
        mat = IDENTITY
        for e, sign in word:
            mat = mat @ (links[e] if sign > 0 else links[e].conj().T)
        value += 1 - mat.trace().real/2
    return value


def displace(links, velocities, h):
    out = links.copy()
    for e, v in velocities.items():
        speed = np.linalg.norm(v)/2
        if speed:
            gen = np.einsum("i,ijk->jk", v, GENERATORS)
            out[e] = (np.cos(h*speed)*IDENTITY + np.sin(h*speed)/speed*gen) @ links[e]
    return out


def numerical():
    words = faces(4)
    stars, nb = incidence(words)
    rng = np.random.default_rng(407)
    links = {}
    for e in stars:
        v = rng.normal(size=4)
        links[e] = np.einsum("i,ijk->jk", v/np.linalg.norm(v), BASIS)
    worst = 0.
    for e, star in list(stars.items())[:24]:
        for p in star:
            private = opposite(words[p], e)
            derivatives = []
            for basis in BASIS:
                adjusted = {**links, private: basis}
                derivatives.append(gradient(words[p], e, adjusted))
                for q in star - {p}:
                    assert np.array_equal(gradient(words[q], e, links), gradient(words[q], e, adjusted))
            rows = np.array(derivatives).T
            worst = max(worst, np.linalg.norm(rows @ rows.T - np.eye(3)))
    if worst > 1e-12:
        raise AssertionError(worst)

    def mixed(p, q, h):
        # These faces are disjoint, so each chosen velocity is constant in the other flow.
        vp = {e: gradient(words[p], e, links) for e, _ in words[p]}
        vq = {e: gradient(words[q], e, links) for e, _ in words[q]}
        assert vp.keys().isdisjoint(vq)
        return sum(a*b*action(words, displace(displace(links, vp, a*h), vq, b*h))
                   for a, b in product((-1, 1), repeat=2))/(4*h*h)

    two = set.union(*(nb[j] for j in nb[0])) - nb[0]
    far = set(range(len(words))) - two - nb[0]
    # Face indices follow lexicographic coordinate order, then plane order.
    near_test = min(two)
    far_test = min(far)
    fine = mixed(0, near_test, 0.001)
    coarse = mixed(0, near_test, 0.002)
    remote = mixed(0, far_test, 0.001)
    if abs(fine) < 1e-4 or abs(fine-coarse) > 2e-5 or abs(remote) > 1e-6:
        raise AssertionError((fine, coarse, remote))
    print("projection residual", f"{worst:.4g}")
    print("mixed potential derivative at distances two and above two", f"{fine:.8g}", f"{remote:.3g}")


if __name__ == "__main__":
    for side in (2, 3, 4, 5):
        print("side, private-link conflicts, largest two-step neighborhood", side, *geometry(side))
    numerical()
