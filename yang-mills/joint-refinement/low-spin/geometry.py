"""Verify the spatial plaquette incidence and the seam estimate without Wilson sampling."""
from fractions import Fraction
from itertools import combinations, product


def shift(site, direction, n):
    out = list(site)
    out[direction] = (out[direction]+1) % n
    return tuple(out)


def selected(site, direction, n):
    grade = sum(site) % n
    erased = any(site[d] % 2 for d in range(3) if d != direction)
    return erased and grade % 2 == 0 and grade//2 % 3 == direction


def check(n):
    sites = list(product(range(n), repeat=3))
    edges = {(x,d) for x in sites for d in range(3) if selected(x,d,n)}
    for x in sites:
        for i,j in combinations(range(3),2):
            face = {(x,i), (x,j), (shift(x,i,n),j), (shift(x,j,n),i)}
            assert len(edges & face) <= 1
            # Partition at odd coordinates into length-two segments, the
            # shortest admitted case. Either edge may precede its partner.
            witnesses = []
            for p,d in face:
                if not any(p[q]%2 for q in range(3) if q != d):
                    continue
                left = list(p)
                left[d] = (p[d] - int(p[d]%2 == 0))%n
                left = tuple(left)
                pair = {(left,d),(shift(left,d,n),d)}
                assert len(pair & face)==1
                witnesses.append(pair)
            assert witnesses
    # A temporal plaquette uses the same spatial edge at consecutive times.
    assert all(t+1 not in {0,n} for t in (0,n))
    counts = []
    for axis in range(3):
        for x in sites:
            if x[axis] == 0 and any(c % 2 for c in x):
                p = x
                labels = []
                for _ in range(n):
                    labels.append(int((p,axis) in edges))
                    p = shift(p,axis,n)
                counts.append(sum(labels))
                twice = labels*2
                for start in range(n):
                    for length in range(2,n+1,2):
                        assert sum(twice[start:start+length]) >= length//6-1
    assert len(counts) == 9*n*n//4 and min(counts) == n//6
    print(n, "winding paths", len(counts), "private links", min(counts), max(counts))


def example():
    # At beta=7/2 bound D/L-1 <= exp(M*2u/(1-u))-1 <= h/(1-h).
    n = 2040
    z = Fraction(14,15)**(n//6)
    u = (1+z)/(1-z)**3-1
    h = (9*n*n//4)*2*u/(1-u)
    assert 0 < h < 1 and h/(1-h) < Fraction(1,100)
    print("N=2040 at beta=7/2: winding theta <", float(h/(1-h)))


if __name__ == "__main__":
    for side in (6,8,10,12,18,24):
        check(side)
    example()
