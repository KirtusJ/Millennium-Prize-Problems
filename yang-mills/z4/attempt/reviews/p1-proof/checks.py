"""checks.py -- small exact/numerical checks supporting sec_proof.tex (worker p1-proof, under T17).

Usage: python3 checks.py <result-file>     (result file opened with mode "x": never overwritten)
Seeds fixed: numpy default_rng(20261123).

PREDICATES (fixed before the first run):
 P1  Cube word identity. For the unit 3-cube with vertices {0,1}^3, take the six faces, each with its
     canonical boundary loop based at its lowest vertex v (v -> v+e_a -> v+e_a+e_b -> v+e_b -> v, a<b),
     conjugated by a monotone edge path from 000 to v. There EXIST an order, signs eps_f in {+1,-1} and a
     choice of monotone transports such that the product of the six conjugated loops reduces to the empty
     word in the free group on the 12 edges. Expected: yes. (exact; no tolerance)
 P2  For the identity found in P1, the signs eps_f agree with the boundary incidence numbers [c:f] of the
     cube up to one global sign. Expected: yes. (exact)
 P3  D* := 48 + 3 log((pi/2)^{5/2} 2^{3/2}) - 3 log c_H, c_H = 2 sin^2(1)/(3 pi), equals 60.19 within 0.005.
     Tolerance source: PROOF_B_v2.md prints two decimals.
 P4  zhat(b) = int exp(-b(1-cos a)) (2/pi) sin^2 a da <= (pi/2)^{5/2} b^{-3/2} for b in {0.5,1,2,5,10,100,1000},
     and Haar(B_s) = (2/pi) int_0^s sin^2 >= c_H s^3 for s in (0,1] (grid of 100). Expected: yes.
     Tolerance: 0 (strict inequality checked on values computed by 20000-point Simpson; quadrature error
     < 1e-10 is far below the margins, which are reported).
 P5  On the periodic lattice (Z/4)^4 the Hodge Laplacian dd* + d*d on 2-forms equals, componentwise, the
     scalar operator 8 - sum of the 8 neighbour shifts. Exact integer matrices; expected equal.
 P6  G(0) computed from the time-integrated formula on a midpoint grid of 160^3 points equals 1/2 within 1e-3.
     Tolerance source: my own estimate of midpoint error for an integrand with a |k| cone at k=0 (h^3 order
     times a small constant); 1e-3 is loose on purpose.
 P7  G(n) > 0 for n = 1..8 on the same grid. Expected yes. Measured only: pi^2 n^4 G(n) and n^2 (pi^2 n^4 G(n) - 1).
 P8  Wick formula. With xi^a_0, xi^a_n (a=1,2,3) centred Gaussian, variances 1/2, covariance g = 0.0688747 (=G(1)),
     colours independent, and an independent background f in R^3 with correlated colours
     (f = mean + Cholesky * N(0,1)), X_m = |xi_m + f|^2/2:
     Monte Carlo Cov(X0,Xn) agrees with (3/2) g^2 + g E|f|^2 + Var|f|^2/4 within 5 standard errors
     (SE from 20 batches), 2*10^6 samples. Also the ratio Cov/Var >= (g/G0)^2. Expected: yes.
"""
import sys, math, itertools
import numpy as np

out = open(sys.argv[1], "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()

met = failed = measured = 0
def pred(name, ok, info=""):
    global met, failed
    if ok: met += 1
    else: failed += 1
    log(f"{name}: {'MET' if ok else 'FAILED'} {info}")

# ---------------- P1, P2: cube word identity ----------------
V = list(itertools.product((0, 1), repeat=3))
def add(v, a): w = list(v); w[a] += 1; return tuple(w)
edges = {}
for v in V:
    for a in range(3):
        if v[a] == 0:
            edges[(v, add(v, a))] = len(edges)
def step(u, w):  # generator for traversing u->w
    if (u, w) in edges: return (edges[(u, w)], 1)
    return (edges[(w, u)], -1)
def path_word(vs):
    return [step(vs[i], vs[i + 1]) for i in range(len(vs) - 1)]
def inv(word): return [(g, -e) for (g, e) in reversed(word)]
def reduce(word):
    st = []
    for x in word:
        if st and st[-1][0] == x[0] and st[-1][1] == -x[1]: st.pop()
        else: st.append(x)
    return st
def monotone_paths(v):
    ups = [a for a in range(3) if v[a] == 1]
    res = []
    for perm in itertools.permutations(ups):
        p = [(0, 0, 0)]
        for a in perm: p.append(add(p[-1], a))
        res.append(p)
    return res
faces = []  # (fixed axis, value, a, b, base v)
for ax in range(3):
    for val in (0, 1):
        a, b = [x for x in range(3) if x != ax]
        v = [0, 0, 0]; v[ax] = val; v = tuple(v)
        loop = [v, add(v, a), add(add(v, a), b), add(v, b), v]
        faces.append(dict(ax=ax, val=val, a=a, b=b, v=v, loop=path_word(loop)))
# incidence [c:f] for the cube with orientation e1^e2^e3: face x_ax=val with orientation e_a^e_b (a<b)
# boundary of e1e2e3 = sum_ax (-1)^ax (face(ax,1) - face(ax,0)) with remaining axes in increasing order
for f in faces:
    f["inc"] = (-1) ** f["ax"] * (1 if f["val"] == 1 else -1)
found = None
trans_choices = [monotone_paths(f["v"]) for f in faces]
for tr in itertools.product(*[range(len(t)) for t in trans_choices]):
    conj = []
    for i, f in enumerate(faces):
        W = path_word(trans_choices[i][tr[i]])
        conj.append((W, f["loop"]))
    for order in itertools.permutations(range(6)):
        for signs in itertools.product((1, -1), repeat=6):
            word = []
            for k in order:
                W, Lp = conj[k]
                word += W + (Lp if signs[k] == 1 else inv(Lp)) + inv(W)
            if not reduce(word):
                found = (tr, order, signs); break
        if found: break
    if found: break
pred("P1 cube word identity exists", found is not None, str(found))
if found:
    tr, order, signs = found
    names = {(0,0):"x1=0",(0,1):"x1=1",(1,0):"x2=0",(1,1):"x2=1",(2,0):"x3=0",(2,1):"x3=1"}
    for k in order:
        f = faces[k]
        log(f"   factor: face {names[(f['ax'],f['val'])]} base {f['v']} transport {trans_choices[k][tr[k]]} sign {signs[k]} incidence {f['inc']}")
    r = [signs[k] * faces[k]["inc"] for k in range(6)]
    pred("P2 signs = +-incidence", len(set(r)) == 1, f"ratios {r}")

# ---------------- P3 ----------------
cH = 2 * math.sin(1) ** 2 / (3 * math.pi)
Dstar = 48 + 3 * math.log((math.pi / 2) ** 2.5 * 2 ** 1.5) - 3 * math.log(cH)
pred("P3 D*", abs(Dstar - 60.19) <= 0.005, f"D* = {Dstar:.6f}, c_H = {cH:.6f}")

# ---------------- P4 ----------------
def simpson(fn, a, b, n=20000):
    x = np.linspace(a, b, n + 1); y = fn(x); h = (b - a) / n
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())
ok = True; margins = []
for bb in (0.5, 1, 2, 5, 10, 100, 1000):
    z = simpson(lambda a: np.exp(-bb * (1 - np.cos(a))) * (2 / np.pi) * np.sin(a) ** 2, 0, np.pi)
    ub = (np.pi / 2) ** 2.5 * bb ** -1.5
    margins.append(ub / z); ok &= z < ub
ok2 = True; m2 = []
for s in np.linspace(0.01, 1, 100):
    hb = (2 / np.pi) * (s / 2 - np.sin(2 * s) / 4)
    m2.append(hb / (cH * s ** 3)); ok2 &= hb >= cH * s ** 3
pred("P4 zhat bound", bool(ok), "ratios ub/z " + ", ".join(f"{m:.3f}" for m in margins))
pred("P4 Haar(B_s) bound", bool(ok2), f"min ratio {min(m2):.4f}")

# ---------------- P5: Hodge Laplacian on 2-forms, (Z/4)^4 ----------------
L = 4; D = 4
sites = list(itertools.product(range(L), repeat=D)); sidx = {s: i for i, s in enumerate(sites)}
def sh(x, mu, k=1): y = list(x); y[mu] = (y[mu] + k) % L; return tuple(y)
def forms(r): return [(x, c) for x in sites for c in itertools.combinations(range(D), r)]
F1, F2, F3 = forms(1), forms(2), forms(3)
i1 = {f: i for i, f in enumerate(F1)}; i2 = {f: i for i, f in enumerate(F2)}; i3 = {f: i for i, f in enumerate(F3)}
def dmat(Fr, Fs, ir):  # d: r-forms -> (r+1)-forms, (d w)_{c}(x) = sum_j (-1)^j (w_{c\c_j}(x+e_{c_j}) - w_{c\c_j}(x))
    M = np.zeros((len(Fs), len(Fr)), dtype=np.int64)
    for row, (x, c) in enumerate(Fs):
        for j, mu in enumerate(c):
            rest = tuple(v for v in c if v != mu)
            M[row, ir[(sh(x, mu), rest)]] += (-1) ** j
            M[row, ir[(x, rest)]] -= (-1) ** j
    return M
d1 = dmat(F1, F2, i1); d2 = dmat(F2, F3, i2)
H = d1 @ d1.T + d2.T @ d2
S = np.zeros_like(H)
for row, (x, c) in enumerate(F2):
    S[row, row] += 2 * D
    for mu in range(D):
        S[row, i2[(sh(x, mu), c)]] -= 1; S[row, i2[(sh(x, mu, -1), c)]] -= 1
pred("P5 Hodge Laplacian = scalar Laplacian componentwise", bool(np.array_equal(H, S)), f"size {H.shape}, d2 d1 = 0: {not np.any(d2 @ d1)}")
measured += 0

# ---------------- P6, P7: G(n) ----------------
N = 160
k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
kh = lambda x: 4 * np.sin(x / 2) ** 2
num = kh(K1) + kh(K2); a = num + kh(K3)
m = np.arccosh(1 + a / 2); sm = np.sinh(m)
G = lambda n: float(np.mean(num * np.exp(-m * n) / (2 * sm)))
G0 = G(0)
pred("P6 G(0)=1/2", abs(G0 - 0.5) <= 1e-3, f"G(0) = {G0:.7f}")
Gs = [G(n) for n in range(1, 9)]
pred("P7 G(n)>0, n=1..8", all(g > 0 for g in Gs), "")
for n, g in zip(range(1, 9), Gs):
    measured += 2
    log(f"   measured n={n}: G={g:.8f}  pi^2 n^4 G = {math.pi**2*n**4*g:.5f}  n^2(pi^2n^4G-1) = {n*n*(math.pi**2*n**4*g-1):.4f}")

# ---------------- P8: Wick formula ----------------
rng = np.random.default_rng(20261123)
g, G0t = 0.0688747, 0.5
nS, nB = 2_000_000, 20
cov = np.array([[G0t, g], [g, G0t]]); Lc = np.linalg.cholesky(cov)
fm = np.array([0.3, -0.2, 0.5]); Lf = np.array([[0.8, 0, 0], [0.5, 0.6, 0], [-0.3, 0.2, 0.4]])
covs = []; vars_ = []
for b in range(nB):
    n_ = nS // nB
    xi = rng.standard_normal((n_, 3, 2)) @ Lc.T          # colour a: (xi0, xin)
    f = fm + rng.standard_normal((n_, 3)) @ Lf.T
    X0 = 0.5 * ((xi[:, :, 0] + f) ** 2).sum(1); Xn = 0.5 * ((xi[:, :, 1] + f) ** 2).sum(1)
    covs.append(np.cov(X0, Xn)[0, 1]); vars_.append(X0.var())
covs = np.array(covs); vars_ = np.array(vars_)
# exact moments of f
Cf = Lf @ Lf.T; Ef2 = fm @ fm + np.trace(Cf)
Varf2 = 2 * np.trace(Cf @ Cf) + 4 * fm @ Cf @ fm     # Var |f|^2 for Gaussian f
th_cov = 1.5 * g * g + g * Ef2 + 0.25 * Varf2
th_var = 1.5 * G0t ** 2 + G0t * Ef2 + 0.25 * Varf2
se = covs.std(ddof=1) / math.sqrt(nB); sev = vars_.std(ddof=1) / math.sqrt(nB)
pred("P8 Wick Cov", abs(covs.mean() - th_cov) <= 5 * se, f"MC {covs.mean():.5f} +- {se:.5f}, formula {th_cov:.5f}")
pred("P8 Wick Var", abs(vars_.mean() - th_var) <= 5 * sev, f"MC {vars_.mean():.5f} +- {sev:.5f}, formula {th_var:.5f}")
pred("P8 ratio >= (g/G0)^2", th_cov / th_var >= (g / G0t) ** 2, f"ratio {th_cov/th_var:.5f} vs {(g/G0t)**2:.5f}")

log(f"COUNTS met {met}, failed {failed}, measured only {measured}")
out.close()
sys.exit(0 if failed == 0 else 1)
