"""Z4 challenger check of D4 electric-scale, items E1 (rotor continuum), E2 (clocks), E3 (units/floor).

Independent of the sub-agent's slope fits (child/rotor.py): this program tests the CONTINUUM LIMIT
of the one-rotor ground state rather than log-log slopes. One rotor is NOT the cubic lattice vacuum.

Model (user's convention, NOT D4's kappa/4): H/kappa = n(n+2) + g on the diagonal, -g/2 off-diagonal,
character basis n = 2j >= 0, g = lambda/kappa. With m = n+1, y = m g^{-1/4}, the continuum limit is
g^{1/2} (-1/2 f'' + y^2) with Dirichlet f(0)=0; ground state f ~ y exp(-y^2/sqrt2), energy 3/sqrt2.

PREDICATES (fixed before first run):
 C0 control: g=0 ground state is chi_0 with E0 = 0 (tol 1e-12, float64 roundoff).
 P1 truncation: doubling the basis changes E0 by < 1e-10 at every g (float64 eigensolver accuracy, margin).
 P2 energy: E0/sqrt(g) within 2% of 3/sqrt(2) for g >= 1e3. Tolerance: leading lattice correction is
    O(g^{-1/4}) relative (discrete second difference + the -1 in m^2-1); at g=1e3, g^{-1/4}=0.18 times a
    small coefficient; 2% is my expectation, not a derived bound.
 P3 quantiles: for q in {0.9, 0.99}, |(N_q + 1) - y_q g^{1/4}| <= 1.5 for g >= 1e2, where y_q is the
    continuum quantile of f^2 dy (Gamma(3/2) in z = sqrt2 y^2). Tolerance: N_q is an integer (+-1) and the
    cell-to-point shift is 1/2.
 P4 dimension exponent: Dim_q = sum_{n<=N_q}(n+1)^2 divided by g^{3/4} varies by less than a factor 1.6
    over g in [1e3, 1e6] (integer N_q gives (1+1/N)^3 jitter; at N~10, ~1.33).
 P5 twirled entropy S_tw - (3/4) log g varies by < 0.15 over g in [1e3,1e6] (O(1) remainder converging;
    tolerance = my expectation of o(1) corrections of size g^{-1/4}).
 P6 (E3) lambda*h^2 = sqrt2/b exactly when kappa_D4 = 2/(beta b), lambda = beta/b, h = g^{-1/4}, g = beta^2/2
    (rel tol 1e-12) for a grid of (beta, b).
 P7 (E3) Jensen floor: for random positive measures on [0,inf) with mass w >= v and first moment <= M,
    sum w_k exp(-tau x_k) >= v exp(-tau M / v). 2000 random cases, seed 12345; rel tol 1e-12.
 P8 (E2) clock table: physical times t_mag = tau b/beta and t_mesh = tau b both -> 0 as b -> 0 for beta fixed
    and beta = c log(1/b) (measured; predicate: both < 1e-3 * tau at b = 1e-4, c = 1).
Results go to results_e1e3.txt; if it exists, a new numbered file is used (never overwrite).
"""
import math, os, sys
import numpy as np

def outfile(base="results_e1e3"):
    k = 0
    while True:
        p = f"{base}.txt" if k == 0 else f"{base}_{k}.txt"
        if not os.path.exists(p):
            return p
        k += 1

def ground(g, N):
    n = np.arange(N)
    Hm = np.diag(n * (n + 2) + g * 1.0) + np.diag(-g / 2 * np.ones(N - 1), 1) + np.diag(-g / 2 * np.ones(N - 1), -1)
    w, V = np.linalg.eigh(Hm)
    a = V[:, 0]
    a = a * np.sign(a[np.argmax(np.abs(a))])
    return w[0], a

def gamma32_cdf(z):
    return math.erf(math.sqrt(z)) - 2 * math.sqrt(z / math.pi) * math.exp(-z)

def yq(q):
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if gamma32_cdf(mid) < q: lo = mid
        else: hi = mid
    return math.sqrt(lo / math.sqrt(2))

out = []; fails = []; met = 0
def pred(name, ok, info):
    global met
    out.append(f"{name}: {'MET' if ok else 'FAILED'}  {info}")
    if ok: met += 1
    else: fails.append(name)

# C0
E, a = ground(0.0, 50)
pred("C0", abs(E) < 1e-12 and abs(abs(a[0]) - 1) < 1e-12, f"E0={E:.3e}, a0={a[0]:.12f}")

gs = [10 ** (k / 4) for k in range(0, 25)]  # 1 .. 1e6
rows = []; trunc_ok = True; maxdE = 0
for g in gs:
    N = int(40 + 12 * g ** 0.25)
    E, a = ground(g, N)
    E2, _ = ground(g, 2 * N)
    maxdE = max(maxdE, abs(E - E2)); trunc_ok &= abs(E - E2) < 1e-10
    p = a ** 2; c = np.cumsum(p); n = np.arange(N)
    Nq = {q: int(np.searchsorted(c, q)) for q in (0.9, 0.99)}
    Dim = {q: int(sum((k + 1) ** 2 for k in range(Nq[q] + 1))) for q in Nq}
    pp = p[p > 1e-300]; nn = n[p > 1e-300]
    Stw = float(-(pp * np.log(pp)).sum() + (pp * np.log((nn + 1.0) ** 2)).sum())
    rows.append((g, E, Nq, Dim, Stw, float((n * p).sum())))
pred("P1", trunc_ok, f"max |dE0| on doubling = {maxdE:.2e}")

y90, y99 = yq(0.9), yq(0.99)
out.append(f"continuum quantiles y_0.9={y90:.6f} y_0.99={y99:.6f}; 3/sqrt2={3/math.sqrt(2):.6f}")
out.append("g | E0/sqrt g | N90 | (N90+1)/g^.25 | N99 | (N99+1)/g^.25 | Dim90/g^.75 | Dim99/g^.75 | S_tw | S_tw-.75 log g | <n>/g^.25")
for g, E, Nq, Dim, S, mn in rows:
    out.append(f"{g:10.3g} | {E/math.sqrt(g):.5f} | {Nq[0.9]:3d} | {(Nq[0.9]+1)/g**.25:.4f} | {Nq[0.99]:3d} | {(Nq[0.99]+1)/g**.25:.4f} | "
               f"{Dim[0.9]/g**.75:.4f} | {Dim[0.99]/g**.75:.4f} | {S:.4f} | {S-.75*math.log(g):.4f} | {mn/g**.25:.4f}")

big = [r for r in rows if r[0] >= 1e3 - 1e-9]
dev = max(abs(r[1] / math.sqrt(r[0]) - 3 / math.sqrt(2)) / (3 / math.sqrt(2)) for r in big)
pred("P2", dev < 0.02, f"max rel dev of E0/sqrt g from 3/sqrt2 for g>=1e3: {dev:.4f}")
d3 = max(max(abs(r[2][0.9] + 1 - y90 * r[0] ** .25), abs(r[2][0.99] + 1 - y99 * r[0] ** .25)) for r in rows if r[0] >= 1e2 - 1e-9)
pred("P3", d3 <= 1.5, f"max |N_q+1 - y_q g^1/4| for g>=1e2: {d3:.3f}")
for q in (0.9, 0.99):
    vals = [r[3][q] / r[0] ** .75 for r in big]
    pred(f"P4(q={q})", max(vals) / min(vals) < 1.6, f"Dim/g^0.75 range [{min(vals):.3f},{max(vals):.3f}] ratio {max(vals)/min(vals):.3f}")
sv = [r[4] - .75 * math.log(r[0]) for r in big]
pred("P5", max(sv) - min(sv) < 0.15, f"S_tw - 0.75 log g range [{min(sv):.4f},{max(sv):.4f}]")
# slopes (measured only)
def slope(xs, ys):
    X = np.log(xs); Y = np.log(ys); return float(np.polyfit(X, Y, 1)[0])
sel = [r for r in rows if 1e2 - 1e-9 <= r[0] <= 1e4 + 1e-6]
out.append(f"MEASURED slopes g in [1e2,1e4]: N90+1 {slope([r[0] for r in sel],[r[2][0.9]+1 for r in sel]):.3f}, "
           f"N99+1 {slope([r[0] for r in sel],[r[2][0.99]+1 for r in sel]):.3f}, Dim90 {slope([r[0] for r in sel],[r[3][0.9] for r in sel]):.3f}, "
           f"Dim99 {slope([r[0] for r in sel],[r[3][0.99] for r in sel]):.3f}, <n>+1 {slope([r[0] for r in sel],[r[5]+1 for r in sel]):.3f}, "
           f"dS_tw/dlog g {float(np.polyfit(np.log([r[0] for r in sel]),[r[4] for r in sel],1)[0]):.3f}")

# P6
worst = 0
for beta in (1.5, 3, 10, 100):
    for b in (1e-1, 1e-3, 1e-6):
        kap = 2 / (beta * b); lam = beta / b; g = lam / kap; h = g ** -0.25
        worst = max(worst, abs(lam * h * h - math.sqrt(2) / b) / (math.sqrt(2) / b))
        assert abs(g - beta ** 2 / 2) < 1e-9 * g
pred("P6", worst < 1e-12, f"max rel err of lambda h^2 vs sqrt2/b: {worst:.2e} (beta drops out: probe energy scale is 1/b)")

# P7
rng = np.random.default_rng(12345); bad = 0
for _ in range(2000):
    k = rng.integers(1, 6); x = rng.exponential(rng.uniform(0.1, 5), k); w = rng.uniform(0, 1, k)
    v = rng.uniform(0.01, 1) * w.sum(); M = (w * x).sum() * rng.uniform(1, 3); tau = rng.uniform(0, 5)
    lhs = (w * np.exp(-tau * x)).sum(); rhs = v * math.exp(-tau * M / v)
    bad += lhs < rhs * (1 - 1e-12)
pred("P7", bad == 0, f"{2000-bad}/2000 cases qualify and satisfy the Jensen floor")

# P8
out.append("E2 clock table (tau=1): b | t_mag(beta=2) | t_mesh | t_mag(beta=log 1/b) | lambda b (beta=log1/b) | mesh energy*b")
for b in (1e-2, 1e-4, 1e-8):
    L = math.log(1 / b)
    out.append(f"{b:.0e} | {b/2:.2e} | {b:.2e} | {b/L:.2e} | {L:.2f} | 1")
pred("P8", 1e-4 / 2 < 1e-3 and 1e-4 < 1e-3 and 1e-4 / math.log(1e4) < 1e-3, "both clocks vanish in physical time at b=1e-4")

out.append(f"COUNTS: met {met}, failed {len(fails)}, measured only: slopes + clock table; failed list {fails}")
p = outfile()
open(p, "w").write("\n".join(out) + "\n")
print("\n".join(out)); print("written", p)
sys.exit(0 if not fails else 1)
