"""Check the full four-torus cochain and period conditions over two finite fields."""
from itertools import combinations, product
import numpy as np


def cell_list(L, k):
    return [(v, dirs) for v in product(range(L), repeat=4)
            for dirs in combinations(range(4), k)]


def forward(v, axis, L):
    out = list(v)
    out[axis] = (out[axis]+1) % L
    return tuple(out)


def coboundary(L, k):
    small = {c:i for i, c in enumerate(cell_list(L, k))}
    large = cell_list(L, k+1)
    matrix = np.zeros((len(large), len(small)), dtype=int)
    for row, (v, dirs) in enumerate(large):
        for r, axis in enumerate(dirs):
            rest = dirs[:r]+dirs[r+1:]
            sign = (-1)**r
            matrix[row, small[forward(v, axis, L), rest]] += sign
            matrix[row, small[v, rest]] -= sign
    return matrix


def rank(matrix, p):
    a = matrix.copy() % p
    r = 0
    for j in range(a.shape[1]):
        candidates = np.flatnonzero(a[r:, j])
        if not candidates.size:
            continue
        pivot = r + candidates[0]
        a[[pivot, r]] = a[[r, pivot]]
        a[r] = a[r]*pow(int(a[r,j]), -1, p) % p
        a[r+1:] = (a[r+1:] - a[r+1:,j,None]*a[r]) % p
        r += 1
    return r


def check(L, p):
    d1, d2 = coboundary(L, 1), coboundary(L, 2)
    coords = cell_list(L, 2)
    periods = np.array([[int(axes==ij and all(v[k]==0 for k in range(4) if k not in ij))
                         for v, axes in coords] for ij in combinations(range(4), 2)])
    assert not (d2 @ d1).any() and not (periods @ d1).any()
    exact = rank(d1, p)
    cycles = len(coords)-rank(d2, p)
    trivial_sector = len(coords)-rank(np.vstack([d2, periods]), p)
    assert trivial_sector == exact and cycles-exact == 6
    # A seam sheet representing one unit of flux attains the L^2 support bound.
    sheet = np.array([int(axes==(0, 1) and v[0]==v[1]==0) for v,axes in coords])
    assert not (d2 @ sheet).any() and list(periods @ sheet)==[1,0,0,0,0,0]
    assert sheet.sum()==L**2
    print(f"L={L} p={p} exact={exact} closed={cycles} zero_period={trivial_sector} sheet={sheet.sum()}")


if __name__ == "__main__":
    for size, modulus in product((2, 3), (2, 3)):
        check(size, modulus)
