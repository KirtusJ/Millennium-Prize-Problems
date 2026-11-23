"""Check based fillings in the periodic link multigraph, including parallel links."""
from itertools import permutations, product
from random import Random

GROUP = list(permutations(range(3)))
ONE = (0, 1, 2)


def mul(a, b):
    return tuple(a[b[i]] for i in ONE)


def inv(a):
    return tuple(a.index(i) for i in ONE)


def shifted(x, i, L):
    return tuple((v+1) % L if k == i else v for k, v in enumerate(x))


def walk(links, path, L, x=(0, 0, 0, 0)):
    val = ONE
    for i in path:
        val = mul(val, links[x, i])
        x = shifted(x, i, L)
    return x, val


def tree_path(x):
    return [i for i, n in enumerate(x) for _ in range(n)]


def fill(links, path, target, L, expected):
    original_endpoint, original = walk(links, path, L)
    factors = ONE
    faces = set()
    for k, wanted in enumerate(target):
        pos = path.index(wanted, k)
        while pos > k:
            a, b = path[pos-1:pos+1]
            x, prefix = walk(links, path[:pos-1], L)
            i, j = sorted((a, b))
            key = (x, i, j)
            assert key not in faces
            faces.add(key)
            _, ij = walk(links, [i, j], L, x)
            _, ji = walk(links, [j, i], L, x)
            h = mul(ij, inv(ji))
            if a > b:
                h = inv(h)
            factors = mul(factors, mul(mul(prefix, h), inv(prefix)))
            path[pos-1:pos+1] = [b, a]
            pos -= 1
    endpoint, final = walk(links, target, L)
    assert path == target and original_endpoint == endpoint
    assert factors == mul(original, inv(final))
    assert len(faces) == expected
    return factors, len(faces)


def check(L):
    rng = Random(1929 + L)
    sites = list(product(range(L), repeat=4))
    links = {(x, i): rng.choice(GROUP) for x in sites for i in range(4)}
    anchor = [walk(links, [i]*L, L)[1] for i in range(4)]
    total = 0
    for x in sites:
        before = tree_path(x)
        _, gx = walk(links, before, L)
        for i in range(4):
            wrap = x[i] == L-1
            y = shifted(x, i, L)
            _, gy = walk(links, tree_path(y), L)
            target = ([i]*L if wrap else []) + tree_path(y)
            n = sum(x[i+1:]) + (L*sum(x[:i]) if wrap else 0)
            factors, used = fill(links, before+[i], target, L, n)
            fixed = mul(mul(gx, links[x, i]), inv(gy))
            assert factors == (mul(fixed, inv(anchor[i])) if wrap else fixed)
            total += used
    for i in range(4):
        for j in range(i+1, 4):
            _, used = fill(links, [i]*L+[j]*L, [j]*L+[i]*L, L, L**2)
            total += used
    assert total == 6*L**4*(L-1)+6*L**2
    print(f"L={L}: {4*L**4} link paths, six commutators, {total} unit-square swaps")


if __name__ == "__main__":
    for side in range(1, 6):
        check(side)
