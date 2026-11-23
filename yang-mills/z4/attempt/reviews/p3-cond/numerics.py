"""numerics.py -- numerical checks of elementary claims in sec_reduction.tex (p3-cond, T21).

Predicates (fixed before the first run):
 N1  rank of the six matrices L_mn = E_mn - E_nm (0<=m<n<=3) equals 6.
 N2  for each of the 6 planes (m,n) there is a permutation matrix s in W4 with s e1 = e_m, s e2 = e_n,
     and ||s R12(phi) s^-1 - R_mn(phi)||_max <= 1e-12 for phi = 1.0.  (tolerance: float64 round-off headroom)
 N3  |W4| = 384 and W4 contains a matrix of determinant -1.
 N4  Kronecker, theta = 1: for each phi in {0.5, 1.7, 3.0, 4.4, 6.0}, min_{1<=n<=10000} dist(n*theta, phi mod 2pi) < 1e-3.
     (1e-3 is my choice; by the three-gap theorem the gaps after 1e4 steps are O(1e-3).)
 N5  for 1000 random atomic measures (seed 20261123) on [m, inf), m = 1/xi, and c in {0.25, 0.5, 0.75}:
     C(c xi)/C(xi) >= e^{1-c} * (1 - 1e-12).   [remark D >= e^{1-c}]
 N6  same measures: mu((K,inf)) <= ratio * e^{-(1-c)K} * (1+1e-12) for K in {0,1,2,5,10}, and
     int E dmu <= log(ratio)/(1-c) * (1+1e-12) + 1e-12.   [(R2)]
 N7  arithmetic used for E0': for k = 1..30, D = 1..6, M = Dk+1:  (4k)^M / M! <= (4e)^M ;
     |S^{4k-1}| = 2 pi^{2k}/Gamma(2k) <= 3 pi^{2k};  4k(4k+1) >= 20;  48e/20 <= 7.
"For all" predicates report the number of qualifying cases.
"""
import itertools, math
import numpy as np

out = open("numerics.out", "x")
def w(s):
    print(s); out.write(s + "\n")

res = {}
# N1
L = []
for m, n in itertools.combinations(range(4), 2):
    A = np.zeros((4, 4)); A[m, n] = 1; A[n, m] = -1; L.append(A)
rank = np.linalg.matrix_rank(np.array([a.ravel() for a in L]))
res["N1"] = rank == 6; w(f"N1 rank={rank} -> {res['N1']}")

# W4
W4 = []
for perm in itertools.permutations(range(4)):
    for signs in itertools.product([1, -1], repeat=4):
        M = np.zeros((4, 4))
        for i, p in enumerate(perm):
            M[p, i] = signs[i]
        W4.append(M)
def R(m, n, phi):
    A = np.eye(4); c, s = math.cos(phi), math.sin(phi)
    A[m, m] = c; A[n, n] = c; A[n, m] = s; A[m, n] = -s
    return A
# N2
ok2 = 0
for m, n in itertools.combinations(range(4), 2):
    found = False
    for s in W4:
        if np.allclose(s[:, 1], np.eye(4)[m]) and np.allclose(s[:, 2], np.eye(4)[n]) and abs(np.linalg.det(s) - 1) < 1e-9 or \
           (np.allclose(s[:, 1], np.eye(4)[m]) and np.allclose(s[:, 2], np.eye(4)[n])):
            if all(x in (0, 1) for x in s.ravel()):  # permutation matrix
                err = np.abs(s @ R(1, 2, 1.0) @ s.T - R(m, n, 1.0)).max()
                found = err <= 1e-12
                w(f"N2 plane ({m},{n}) err={err:.2e}")
                break
    ok2 += found
res["N2"] = ok2 == 6; w(f"N2 {ok2}/6 qualify -> {res['N2']}")
# N3
dets = [round(np.linalg.det(s)) for s in W4]
res["N3"] = len(W4) == 384 and -1 in dets; w(f"N3 |W4|={len(W4)} det-1 present={-1 in dets} -> {res['N3']}")
# N4
ns = np.arange(1, 10001) * 1.0
ok4 = 0
for phi in [0.5, 1.7, 3.0, 4.4, 6.0]:
    d = np.abs(((ns - phi + math.pi) % (2 * math.pi)) - math.pi).min()
    ok4 += d < 1e-3; w(f"N4 phi={phi} min dist={d:.2e}")
res["N4"] = ok4 == 5; w(f"N4 {ok4}/5 -> {res['N4']}")
# N5, N6
rng = np.random.default_rng(20261123)
ok5 = ok6 = tot = 0
minratio = {}
for trial in range(1000):
    xi = 10 ** rng.uniform(0, 3)
    natoms = rng.integers(1, 8)
    E = 1 + rng.exponential(rng.uniform(0.1, 5), natoms)   # energies in units of the gap, >= 1
    E[0] = 1.0 if rng.random() < 0.3 else E[0]
    wts = rng.uniform(0.01, 1, natoms)
    for c in (0.25, 0.5, 0.75):
        tot += 1
        Cc = (wts * np.exp(-c * E)).sum(); C1 = (wts * np.exp(-E)).sum()
        ratio = Cc / C1
        minratio[c] = min(minratio.get(c, 1e300), ratio / math.exp(1 - c))
        ok5 += ratio >= math.exp(1 - c) * (1 - 1e-12)
        mu = wts * np.exp(-E) / C1
        good = all(mu[E > K].sum() <= ratio * math.exp(-(1 - c) * K) * (1 + 1e-12) for K in (0, 1, 2, 5, 10))
        good = good and (mu * E).sum() <= math.log(ratio) / (1 - c) * (1 + 1e-12) + 1e-12
        ok6 += good
res["N5"] = ok5 == tot; res["N6"] = ok6 == tot
w(f"N5 {ok5}/{tot} qualify; min ratio/e^(1-c) by c: {minratio} -> {res['N5']}")
w(f"N6 {ok6}/{tot} qualify -> {res['N6']}")
# N7
ok7 = tot7 = 0
for k in range(1, 31):
    for D in range(1, 7):
        M = D * k + 1; tot7 += 1
        lhs = M * math.log(4 * k) - math.lgamma(M + 1); rhs = M * math.log(4 * math.e)
        ok7 += lhs <= rhs
    tot7 += 2
    ok7 += (math.log(2) + 2 * k * math.log(math.pi) - math.lgamma(2 * k)) <= math.log(3) + 2 * k * math.log(math.pi)
    ok7 += 4 * k * (4 * k + 1) >= 20
tot7 += 1; ok7 += 48 * math.e / 20 <= 7
res["N7"] = ok7 == tot7; w(f"N7 {ok7}/{tot7} qualify -> {res['N7']}")
met = sum(res.values()); w(f"SUMMARY met={met} failed={len(res)-met} measured_only=0")
out.close()
raise SystemExit(0 if met == len(res) else 1)
