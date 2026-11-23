"""Finite graph, distribution and Gaussian checks for the slab proof attempt."""
from functools import cache
from itertools import combinations, product
from math import comb, exp, fsum, log, pi, sqrt
import json


def lattice_cycles(side, length):
    vertices = list(product(range(side),repeat=3))
    nbr = {}
    for v in vertices:
        nbr[v] = [tuple((x+step)%side if i==j else x for j,x in enumerate(v))
                  for i in range(3) for step in (-1,1)]
    def extend(path):
        if len(path)==length:
            return int(path[0] in nbr[path[-1]] and path[1] < path[-1])
        return sum(extend(path+(w,)) for w in nbr[path[-1]] if w>path[0] and w not in path)
    return sum(extend((v,)) for v in vertices)


def binomial_tv(count, corr):
    # The sufficient statistic in independent binary pairs is the count of matching signs.
    def log_pmf(k, p):
        return log(comb(count,k))+k*log(p)+(count-k)*log(1-p)
    return fsum(abs(exp(log_pmf(k,(1+corr)/2))-exp(log_pmf(k,0.5)))
                for k in range(count+1))/2


def eigen_checkerboard(side,m,a):
    # Compare every alias pair in the exact three-dimensional Fourier spectrum.
    from math import sin
    def omega(k):
        return sqrt(m*m+4*sum(sin(pi*x/side)**2 for x in k)/a**2)
    rho=max(abs(omega(k)-omega(tuple((x+side//2)%side for x in k)))/
            (omega(k)+omega(tuple((x+side//2)%side for x in k)))
            for k in product(range(side),repeat=3))
    edge=sqrt(m*m+12/a**2)
    assert abs(rho-(edge-m)/(edge+m))<1e-12
    return rho


def wick_coefficient(sites, edges):
    """Count labeled pairings with a prescribed graph and four fields per insertion."""
    pairs = tuple(combinations(range(sites), 2))

    @cache
    def count(degrees, remaining):
        if not any(degrees):
            return int(not any(remaining))
        i = next(k for k, degree in enumerate(degrees) if degree)
        total = 0
        for k, (left, right) in enumerate(pairs):
            if left != i or not remaining[k] or not degrees[right]:
                continue
            # Fix the first unpaired leg at i. Any remaining leg at right can partner it.
            child_degrees = list(degrees)
            child_edges = list(remaining)
            child_degrees[i] -= 1
            child_degrees[right] -= 1
            child_edges[k] -= 1
            total += degrees[right] * count(tuple(child_degrees), tuple(child_edges))
        return total

    return count((4,) * sites, tuple(edges.get(pair, 0) for pair in pairs))


def hidden_sector():
    states = tuple(product((-1, 1), repeat=2))
    snapshots = []
    for epsilon in (0.125, 0.025):
        slow = 1 - 2*epsilon
        kernel = [[(1 + 0.5*x*u)*(1 + slow*y*v)/4 for u,v in states] for x,y in states]
        basis = ([1.0]*4, [x for x,y in states], [y for x,y in states], [x*y for x,y in states])
        def step(f):
            return [sum(p*a for p,a in zip(row, f)) for row in kernel]
        for f, eigen in zip(basis, (1, 0.5, slow, 0.5*slow)):
            assert max(abs(a-eigen*b) for a,b in zip(step(f), f)) < 1e-13
        probe = [sqrt(1-epsilon**2)*x + epsilon*y for x,y in states]
        propagated = probe
        errors = []
        for n in range(181):
            observed = sum(a*b for a,b in zip(probe, propagated))/4
            assert abs(observed - (1-epsilon**2)*0.5**n - epsilon**2*slow**n) < 1e-13
            errors.append(abs(observed-0.5**n))
            propagated = step(propagated)
        assert max(errors) <= epsilon**2 + 1e-13
        snapshots.append(round(max(errors), 9))
    return snapshots


def run():
    counts = {str((L,k)):lattice_cycles(L,k) for L,k in ((3,3),(4,4),(6,4))}
    assert list(counts.values())==[27,240,648]
    tv=[binomial_tv(m,0.25) for m in (1,16,64,256)]
    assert all(a<b for a,b in zip(tv,tv[1:])) and tv[-1]>.94
    alias=[eigen_checkerboard(8,1,a) for a in (1,.5,.25,.125,.0625)]
    assert all(a<b for a,b in zip(alias,alias[1:]))
    wick = [wick_coefficient(2, {(0,1):4}),
            wick_coefficient(3, {(0,1):2,(0,2):2,(1,2):2}),
            wick_coefficient(4, {(0,1):2,(1,2):2,(2,3):2,(0,3):2})]
    assert wick == [24,1728,20736]
    return {"cycles":counts, "binary_TV":[round(x,7) for x in tv],
            "checkerboard":[round(x,7) for x in alias],"physical_slab":round(exp(-1),7),
            "wick_multiplicities":wick, "hidden_sector_max_errors":hidden_sector()}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
