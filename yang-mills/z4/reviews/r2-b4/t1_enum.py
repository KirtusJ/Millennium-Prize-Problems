"""T1: free electric spectrum on small periodic tori (Z4 challenger, own code).

Predicates (fixed before the first run):
 P1 hypothesis count: number of assignments n_e in {0,1,2} with sum n_e(n_e+2) <= 3*min(L,4)
    equals the closed form: L=2 (only labels 0/1, <=2 ones): 1+24+C(24,2)=301;
    L=3: 1 + 81 (single n=2) + 81 + C(81,2) + C(81,3) = 88723.
 P2 minimum cost over admissible NONEMPTY assignments == 3*min(L,4)  (6 at L=2, 9 at L=3).
 P3 attaining supports: L=2 -> exactly the 12 parallel-link pairs {(x,i),(x+e_i,i)} with n=1;
    L=3 -> exactly the 27 winding lines (3 links along one axis) with n=1.
 P4 no admissible nonempty assignment has cost < 3*min(L,4).
 P5 falsification control: a single link with n=1 and a single link with n=2 are inadmissible,
    and a nonwinding open path of 2 links is inadmissible.
 P6 independent girth (shortest cycle via edge deletion + BFS) == min(L,4) for L=2..6.
 Measured only: on L=2, minimum cost of an admissible assignment containing a label n=2,
    enumerated to cost <= 16 (mixed labels at degree>=3 vertices).
Admissibility: at each vertex the tensor product of spins n_e/2 of incident nonzero links
contains spin 0 (computed exactly by the Clebsch-Gordan range rule). Exact integer arithmetic,
so no tolerance is needed. No randomness.
"""
import itertools, math, sys, os, json
from collections import deque

def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    edges = []
    for x in sites:
        for a in range(3):
            y = list(x); y[a] = (y[a]+1) % L
            edges.append((x, tuple(y), a))
    return sites, edges

def admissible_vertex(labels):
    reach = {0}
    for n in labels:
        reach = {k for j in reach for k in range(abs(j-n), j+n+1, 2)}
    return 0 in reach

def admissible(assign, edges):
    inc = {}
    for e, n in assign.items():
        u, v, _ = edges[e]
        inc.setdefault(u, []).append(n)
        inc.setdefault(v, []).append(n)
    return all(admissible_vertex(ls) for ls in inc.values())

def cost(assign):
    return sum(n*(n+2) for n in assign.values())

def enumerate_assign(E, budget):
    """all assignments (dict edge->n, n in {1,2}) with cost <= budget"""
    out = [{}]
    def rec(start, cur, c):
        for e in range(start, E):
            for n in (1, 2):
                cc = c + n*(n+2)
                if cc <= budget:
                    cur[e] = n
                    out.append(dict(cur))
                    rec(e+1, cur, cc)
                    del cur[e]
    rec(0, {}, 0)
    return out

def girth(L):
    sites, edges = torus(L)
    adj = {s: [] for s in sites}
    for k, (u, v, a) in enumerate(edges):
        adj[u].append((v, k)); adj[v].append((u, k))
    best = 10**9
    for k, (u, v, a) in enumerate(edges):
        dist = {u: 0}; q = deque([u])
        while q:
            w = q.popleft()
            for nx, kk in adj[w]:
                if kk == k or nx in dist: continue
                dist[nx] = dist[w]+1; q.append(nx)
        if v in dist: best = min(best, dist[v]+1)
    return best

def main(out):
    res = {}; fails = []
    for L in (2, 3):
        sites, edges = torus(L); E = len(edges); thr = 3*min(L, 4)
        allA = enumerate_assign(E, thr)
        expect = 1+24+math.comb(24, 2) if L == 2 else 1+81+81+math.comb(81, 2)+math.comb(81, 3)
        adm = [A for A in allA if admissible(A, edges)]
        nonempty = [A for A in adm if A]
        mincost = min(cost(A) for A in nonempty) if nonempty else None
        attain = [A for A in nonempty if cost(A) == mincost]
        below = [A for A in nonempty if cost(A) < thr]
        if L == 2:
            want = set()
            for k, (u, v, a) in enumerate(edges):
                for k2, (u2, v2, a2) in enumerate(edges):
                    if k < k2 and a == a2 and u2 == v and v2 == u:
                        want.add(frozenset([k, k2]))
        else:
            want = set()
            for k, (u, v, a) in enumerate(edges):
                line = frozenset(k2 for k2, (u2, v2, a2) in enumerate(edges)
                                 if a2 == a and all(u2[b] == u[b] for b in range(3) if b != a))
                want.add(line)
        got = {frozenset(A) for A in attain}
        allones = all(set(A.values()) == {1} for A in attain)
        r = {"enumerated": len(allA), "expected_count": expect, "admissible_incl_empty": len(adm),
             "admissible_nonempty": len(nonempty), "min_cost": mincost, "threshold": thr,
             "n_attaining": len(attain), "expected_attaining": len(want),
             "attaining_equal_expected": got == want and allones, "below_threshold": len(below),
             "example_support": sorted(edges[k][:2] + (edges[k][2],) for k in next(iter(attain)))}
        res[str(L)] = r
        if len(allA) != expect: fails.append(f"P1 L={L}")
        if mincost != thr: fails.append(f"P2 L={L}")
        if not (got == want and allones): fails.append(f"P3 L={L}")
        if below: fails.append(f"P4 L={L}")
        # P5
        p = edges[0]
        q = next(k for k, e in enumerate(edges) if e[0] == p[1] and e[2] != p[2])
        if admissible({0: 1}, edges) or admissible({0: 2}, edges) or admissible({0: 1, q: 1}, edges):
            fails.append(f"P5 L={L}")
    # measured only: mixed labels on L=2
    sites, edges = torus(2)
    big = enumerate_assign(len(edges), 16)
    mixed = [A for A in big if 2 in A.values() and admissible(A, edges)]
    m = min(cost(A) for A in mixed) if mixed else None
    res["L2_mixed_measured"] = {"enumerated_cost_le_16": len(big), "admissible_with_n2": len(mixed),
                                "min_cost_with_n2": m}
    gs = {L: girth(L) for L in (2, 3, 4, 5, 6)}
    res["girth"] = gs
    if any(gs[L] != min(L, 4) for L in gs): fails.append("P6")
    res["failed"] = fails
    if os.path.exists(out):
        sys.exit("refuse to overwrite " + out)
    with open(out, "w") as f: json.dump(res, f, indent=1)
    print(json.dumps(res, indent=1)); sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main(sys.argv[1])
