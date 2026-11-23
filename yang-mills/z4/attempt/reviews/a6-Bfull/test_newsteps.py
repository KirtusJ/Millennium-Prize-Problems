"""Test of the steps added in PROOF_B_v2 (a6-Bfull). One colour suffices (colours are independent copies).

PREDICATES (fixed before the first run):
 G1  G(0) = 1/2 within 2e-3. Tolerance: midpoint rule on M^3 grid, M=40; the integrand is Lipschitz-like
     ~|k| near 0, so error ~ M^-2 * O(1); we also report |G_M - G_{M/2*... }| as the estimate (M=40 vs 28).
 G2  G(n) > 0 for every n in 1..12 (count of qualifying cases reported). Lemma G of PROOF_B_v2.
 G3  G(n) <= G(0) for every n in 1..12.
 G4  G(n) >= Lb(n) := (4/pi^2)(16 r^5/3) e^-1 /(2 sinh 1) /(2pi)^3, r = 1/(sqrt(3) n), for n in 1..12
     (the explicit lower bound proved in Lemma G). Tolerance: none needed if G is >10x Lb; quadrature error 2e-3
     is reported alongside.
 M1  Sup formula / Dirichlet monotonicity: C^N(p0,p0) strictly increasing for N = 2,4,6 and < G(0) = 1/2.
     (Lemma D: the conditional variance is a sup over a growing family.) N even so p0 sits at the centre.
 M2  measured only: C^N(p0,p1) for N = 2,4,6 versus G(1).
 H1  Interior forest gauge (temporal links from interior sites, pointing +e0): the quadratic form
     Q = sum_p (dA)_p^2 on unpinned interior links (shell links = 0) is positive definite: min eigenvalue > 1e-9
     (tolerance: double precision, matrices of size <= 3000 with O(1) integer entries, eigvalsh backward error ~1e-12).
 H2  nullity of Q on ALL interior links (nothing pinned) == number of interior sites (gauge directions), for N=2,3,4.
 H3  measured only: pinning in addition the e1-links of the slice x0 = N//2 (a global axial tree's spatial part):
     report (#pinned - #interior sites) = number of pins that are physical constraints, not gauge choices.
Seeds: no randomness. Result file opened with mode "x".
"""
import sys, json, math, itertools
import numpy as np

out = sys.argv[1]
res = {"pred": {}, "measured": {}}

def G(n, M):
    k = (np.arange(M) + 0.5) * 2 * np.pi / M - np.pi
    k1, k2, k3 = np.meshgrid(k, k, k, indexing="ij")
    h1, h2, h3 = 4*np.sin(k1/2)**2, 4*np.sin(k2/2)**2, 4*np.sin(k3/2)**2
    m = np.arccosh(1 + (h1+h2+h3)/2)
    return float(np.mean((h1+h2) * np.exp(-m*n) / (2*np.sinh(m))))

G0, G0b = G(0, 40), G(0, 28)
res["measured"]["G0_M40"], res["measured"]["G0_M28"] = G0, G0b
res["pred"]["G1"] = abs(G0 - 0.5) < 2e-3
Gs = {n: G(n, 40) for n in range(0, 13)}
res["measured"]["G"] = Gs
ns = range(1, 13)
res["pred"]["G2"] = f"{sum(Gs[n] > 0 for n in ns)}/12"
res["pred"]["G3"] = f"{sum(Gs[n] <= Gs[0] for n in ns)}/12"
def Lb(n):
    r = 1/(math.sqrt(3)*n)
    return (4/math.pi**2)*(16*r**5/3)*math.exp(-1)/(2*math.sinh(1))/(2*math.pi)**3
res["measured"]["Lb"] = {n: Lb(n) for n in ns}
res["pred"]["G4"] = f"{sum(Gs[n] >= Lb(n) for n in ns)}/12"

def box(N):
    sites = list(itertools.product(range(N+1), repeat=4))
    interior = [x for x in sites if all(0 < c < N for c in x)]
    isint = set(interior)
    links = [(x, mu) for x in sites for mu in range(4) if x[mu] < N]
    ilinks = [l for l in links if l[0] in isint or tuple(c+(i == l[1]) for i, c in enumerate(l[0])) in isint]
    idx = {l: i for i, l in enumerate(ilinks)}
    plaqs = [(x, mu, nu) for x in sites for mu in range(4) for nu in range(mu+1, 4) if x[mu] < N and x[nu] < N]
    D = np.zeros((len(plaqs), len(ilinks)))
    pidx = {}
    for r, (x, mu, nu) in enumerate(plaqs):
        pidx[(x, mu, nu)] = r
        sh = lambda y, a: tuple(c+(i == a) for i, c in enumerate(y))
        for l, s in (((x, mu), 1), ((sh(x, mu), nu), 1), ((sh(x, nu), mu), -1), ((x, nu), -1)):
            if l in idx: D[r, idx[l]] += s
    return interior, ilinks, idx, D, pidx

def cov_center(N):
    interior, ilinks, idx, D, pidx = box(N)
    g = np.zeros((len(ilinks), len(interior)))
    for j, x in enumerate(interior):
        for mu in range(4):
            out_l = (x, mu)
            in_x = tuple(c-(i == mu) for i, c in enumerate(x))
            if out_l in idx: g[idx[out_l], j] -= 1
            if (in_x, mu) in idx: g[idx[(in_x, mu)], j] += 1
    M = D.T @ D + g @ g.T
    c = tuple([N//2]*4)
    c1 = tuple([N//2+1] + [N//2]*3)
    d0, d1 = D[pidx[(c, 1, 2)]], D[pidx[(c1, 1, 2)]]
    sol = np.linalg.solve(M, np.stack([d0, d1], 1))
    return float(d0 @ sol[:, 0]), float(d0 @ sol[:, 1])

C = {N: cov_center(N) for N in (2, 4, 6)}
res["measured"]["C_pp_pq"] = C
v = [C[N][0] for N in (2, 4, 6)]
res["pred"]["M1"] = bool(v[0] < v[1] < v[2] < 0.5)

H1, H2, H3 = [], [], {}
for N in (2, 3, 4):
    interior, ilinks, idx, D, pidx = box(N)
    Q = D.T @ D
    ev = np.linalg.eigvalsh(Q)
    nullity = int(np.sum(ev < 1e-9))
    H2.append(nullity == len(interior))
    pinned = {idx[(x, 0)] for x in interior}
    free = [i for i in range(len(ilinks)) if i not in pinned]
    H1.append(float(np.linalg.eigvalsh(Q[np.ix_(free, free)])[0]))
    extra = {idx[l] for l in ilinks if l[1] == 1 and l[0][0] == N//2}
    H3[N] = len(pinned | extra) - len(interior)
res["measured"]["H1_mineig"] = H1
res["pred"]["H1"] = f"{sum(e > 1e-9 for e in H1)}/3"
res["pred"]["H2"] = f"{sum(H2)}/3"
res["measured"]["H3_physical_pins"] = H3
with open(out, "x") as f:
    json.dump(res, f, indent=1, default=str)
print(json.dumps(res["pred"]))
print(json.dumps(res["measured"], default=str))
