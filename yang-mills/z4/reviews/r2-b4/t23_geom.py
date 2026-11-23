"""T2/T3 checks on periodic tori L=2,3,4 (Z4 challenger, own code).

Predicates (fixed before the first run):
 T2a  For L in {2,3,4}: the sets x+S, S={0,e1,e2,e3}, have 4 distinct sites, every site lies in
      exactly 4 of them, and sum_x h_x = (4/3) sum_y A_y as a multiset identity of coefficients
      (exact rationals), which with the rescaling (8k/3)(1/(2k)) = 4/3 gives the electric part.
 T2d  Every plaquette anchored at x (planes ij) touches only sites in x+S, where a link (y,a)
      belongs to site y; and each plaquette is anchored at exactly one x (sum of v_x = all faces once).
 T2b  Block spectrum: eigenvalues of h_x on the block are (1/3)*sum of 12 link Casimirs n(n+2);
      exact minimum over nonzero label vectors with n<=3 is 1, attained (exact integers).
 T2c  ||v_x|| <= 8z: |phi|<=1 on 3 faces times 8z/3 (exact), and sampled max of |sum phi| <= 3.
 T3a  For L in {2,3,4}: any two distinct xy plaquettes have distinct link sets, each containing a
      link not in the other (=> orthogonal under product Haar).
 T3a' Monte Carlo (seed 20261122, N=20000) at L=2: Gram matrix of the 8 xy traces F_x is identity
      within 5 standard errors; SE = 1/sqrt(N) since Var(F_x F_y)=1 (x!=y) and Var(F^2)=E F^4-1=1.
 T3b  Finite-difference Laplacian (h=1e-3, symmetric left-invariant second differences along
      i sigma_k) on each of the 4 links gives sum_e (-Delta_e) F = 12 F at 20 random points;
      tolerance 1e-5 relative (O(h^2)=1e-6 truncation, roundoff ~1e-16/h^2 = 1e-10). Energy 12/(2k)=6/k.
 T3c  Riemann sum: b^3 sum_{x in Z^3} f(bx)g(bx) for product bumps converges to the integral;
      measured only (errors for b=0.4,0.2,0.1 reported; predicate: error decreasing and < 1e-3 at b=0.1).
"""
import itertools, math, random, sys, os, json
from fractions import Fraction as Fr

def add(x, a, L, s=1):
    y = list(x); y[a] = (y[a]+s) % L; return tuple(y)

def faces(x, L):
    out = []
    for i, j in itertools.combinations(range(3), 2):
        out.append(((x, i), (add(x, i, L), j), (add(x, j, L), i), (x, j)))
    return out

# quaternion SU(2): (a,b,c,d) = a + b i + c j + d k ; Tr U = 2a
def qm(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
            a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
def qinv(p): return (p[0], -p[1], -p[2], -p[3])
def haar(rng):
    v = [rng.gauss(0, 1) for _ in range(4)]; n = math.sqrt(sum(t*t for t in v)); return tuple(t/n for t in v)
def trace_face(U, f):
    (l1, l2, l3, l4) = f
    P = qm(qm(qm(U[l1], U[l2]), qinv(U[l3])), qinv(U[l4]))
    return 2*P[0]

def main(out):
    res = {}; fails = []
    for L in (2, 3, 4):
        sites = list(itertools.product(range(L), repeat=3))
        blocks = {x: [x] + [add(x, a, L) for a in range(3)] for x in sites}
        distinct = all(len(set(b)) == 4 for b in blocks.values())
        cover = {y: 0 for y in sites}
        coef = {y: Fr(0) for y in sites}
        for x, b in blocks.items():
            for y in b: cover[y] += 1; coef[y] += Fr(1, 3)
        ok_a = distinct and set(cover.values()) == {4} and set(coef.values()) == {Fr(4, 3)} \
            and Fr(8, 3)*Fr(1, 2) == Fr(4, 3)
        if not ok_a: fails.append(f"T2a L={L}")
        ok_d = True; seen = {}
        for x in sites:
            for f in faces(x, L):
                if not {y for (y, a) in f} <= set(blocks[x]): ok_d = False
                key = frozenset(f); seen[key] = seen.get(key, 0)+1
        if len(seen) != 3*L**3 or set(seen.values()) != {1}: ok_d = False
        if not ok_d: fails.append(f"T2d L={L}")
        # T3a
        xy = [frozenset(faces(x, L)[0]) for x in sites]
        ok3 = all(a != b and (a-b) and (b-a) for a, b in itertools.combinations(xy, 2))
        if not ok3: fails.append(f"T3a L={L}")
        res[f"L{L}"] = {"T2a": ok_a, "T2d": ok_d, "faces_distinct": len(seen), "T3a": ok3}
    # T2b exact block minimum: 12 links, labels n<=3; min of (1/3) sum n(n+2) over nonzero vectors
    cas = [n*(n+2) for n in range(4)]
    m = min(Fr(cas[n], 3) for n in range(1, 4))  # one nonzero label suffices for the minimum; sums only grow
    ok_b = (m == 1)
    if not ok_b: fails.append("T2b")
    res["T2b_block_min_excitation"] = str(m)
    # T2c and T3a' Monte Carlo at L=2
    rng = random.Random(20261122)
    L = 2; sites = list(itertools.product(range(L), repeat=3))
    links = [(x, a) for x in sites for a in range(3)]
    xyf = [faces(x, L)[0] for x in sites]
    N = 20000; G = [[0.0]*8 for _ in range(8)]; maxv = 0.0
    for _ in range(N):
        U = {l: haar(rng) for l in links}
        F = [trace_face(U, f) for f in xyf]
        for i in range(8):
            for j in range(8): G[i][j] += F[i]*F[j]
        s = sum(trace_face(U, f)/2 for f in faces(sites[0], L))
        maxv = max(maxv, abs(s))
    G = [[g/N for g in r] for r in G]
    tol = 5/math.sqrt(N)
    dev = max(abs(G[i][j]-(1.0 if i == j else 0.0)) for i in range(8) for j in range(8))
    if dev > tol: fails.append("T3a'")
    if maxv > 3: fails.append("T2c")
    res["T3a_prime_MC"] = {"N": N, "max_dev_from_identity": dev, "tol_5SE": tol}
    res["T2c"] = {"bound": "8z/3*3*max|phi|=8z", "sampled_max_abs_sum_phi": maxv}
    # T3b finite-difference Laplacian
    h = 1e-3; gens = [(math.cos(h), math.sin(h), 0, 0), (math.cos(h), 0, math.sin(h), 0), (math.cos(h), 0, 0, math.sin(h))]
    worst = 0.0
    f0 = xyf[0]
    for _ in range(20):
        U = {l: haar(rng) for l in links}
        F = trace_face(U, f0); lap = 0.0
        for l in f0:
            for g in gens:
                Up = dict(U); Up[l] = qm(U[l], g)
                Um = dict(U); Um[l] = qm(U[l], qinv(g))
                lap += (trace_face(Up, f0) - 2*F + trace_face(Um, f0))/h**2
        worst = max(worst, abs(-lap - 12*F)/max(1.0, abs(F)))
    if worst > 1e-5: fails.append("T3b")
    res["T3b_rel_err_casimir12"] = worst
    # T3c Riemann sum with bump f(x)=prod psi(x_i), g(x)=prod psi(x_i-0.3), psi(t)=exp(-1/(1-t^2))
    def psi(t): return math.exp(-1/(1-t*t)) if abs(t) < 1 else 0.0
    def one_d(b, sh):
        n = int(2/b)+2
        return b*sum(psi(b*k)*psi(b*k-sh) for k in range(-n, n+1))
    exact1 = one_d(1e-4, 0.3)
    errs = {}
    for b in (0.4, 0.2, 0.1):
        errs[b] = abs(one_d(b, 0.3)**3 - exact1**3)
    ok_c = errs[0.4] >= errs[0.2] >= errs[0.1] and errs[0.1] < 1e-3
    if not ok_c: fails.append("T3c")
    res["T3c_riemann_errors"] = {str(k): v for k, v in errs.items()}; res["T3c_integral"] = exact1**3
    res["failed"] = fails
    if os.path.exists(out): sys.exit("refuse to overwrite " + out)
    with open(out, "w") as fh: json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1)); sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main(sys.argv[1])
