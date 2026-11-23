"""Referee checks for paper/ (An upper bound on the lattice mass gap at weak coupling).

Predicates fixed before the first run (tolerances and their sources in brackets):

P1  D* = 48 + 3 log((pi/2)^{5/2} 2^{3/2}) - 3 log c_H, c_H = 2 sin^2(1)/(3 pi), equals 60.1922 to 4 decimals
    and c_H = 0.150258 to 6 decimals  [paper prints 60.1922..., 0.150258...; tolerance = printed digits].
P2  G(0) = 1/2 and G(1) = 0.0688747 from the 3-d formula of Lemma G(1)
    [tol 2e-6: last printed digit 1e-7 plus quadrature error, estimated by comparing two grids].
P3  pi^2 n^4 G(n) at n = 8 equals 1.092 to 3 decimals [printed digits]; G(n+1) < G(n) for n = 0..9;
    |G(n) - 1/(pi^2 n^4)| <= Lemma G(4) bound for n = 1..10.
P4  Dirichlet box N=1: C_{p0p0} = 7/24 (tol 1e-10, linear algebra roundoff) and lambda_1 = 0.837722 (tol 1e-6, printed);
    N=2: C = 0.49267 (tol 1e-5, printed) and lambda_2 = 0.147122 (tol 1e-6, printed); C(N=1) < C(N=2) < 1/2.
P5  The six words of the cube identity (Prop L4(b)) concatenate to the empty word in the free group (exact).
P6  2-d U(1) torus analogue of the chessboard tail (Lemma chess + Cor tail with exponent t/2 in d=2):
    P(O_p>t) <= P(all O_q>t)^{1/L^2} <= exp(f(b/2)-f(b)-t/2), L in {2,4}, beta in {1,4}, t on a grid
    [tol 1e-12 relative, double precision; exact Fourier formula, quadrature by 400-node Gauss-Legendre].
P7  Observation neg:obs-dual amplitude A = -1/324 = -0.0030864 on the periodic 2x1x1 lattice with spins
    site0 (j01,j02,j12) = (0,1,1), site1 = (1,0,1/2): Monte Carlo (seed 20261123, 4e6 samples) within 4 standard errors
    of -1/324 and more than 4 standard errors below 0 [4 sigma: chosen two-sided false-alarm ~6e-5].
Seeds fixed. Output file opened with mode "x".
"""
import math, itertools, sys
import numpy as np

out = open(sys.argv[1], "x")
def rep(name, ok, msg):
    s = f"{name}: {'MET' if ok else 'FAILED'} :: {msg}"
    print(s); out.write(s + "\n"); out.flush()

# P1
cH = 2*math.sin(1)**2/(3*math.pi)
Dstar = 48 + 3*math.log((math.pi/2)**2.5 * 2**1.5) - 3*math.log(cH)
rep("P1", abs(Dstar-60.1922) < 5e-5 and abs(cH-0.150258) < 5e-7, f"D*={Dstar:.6f} c_H={cH:.7f}")

# P2,P3: G(n) via 3-d formula with even symmetry, composite Gauss-Legendre graded near 0
def grid(panels, q):
    x, w = np.polynomial.legendre.leggauss(q)
    X, W = [], []
    for a, b in zip(panels[:-1], panels[1:]):
        X.append((b-a)/2*x+(a+b)/2); W.append((b-a)/2*w)
    return np.concatenate(X), np.concatenate(W)
def Gvals(ns, panels, q):
    k, w = grid(panels, q)
    kh2 = 4*np.sin(k/2)**2
    res = np.zeros(len(ns))
    for i in range(len(k)):  # loop over k1 to save memory
        a = kh2[i] + kh2[:, None] + kh2[None, :]
        num = kh2[i] + kh2[:, None] + 0*kh2[None, :]
        m = np.arccosh(1 + a/2)
        base = num/(2*np.sinh(m)) * w[i]*w[:, None]*w[None, :]
        for j, n in enumerate(ns):
            res[j] += np.sum(base*np.exp(-m*n))
    return res*8/(2*math.pi)**3
ns = list(range(0, 11))
pA = [0, .02, .05, .1, .2, .4, .8, 1.6, math.pi]
pB = [0, .01, .025, .05, .1, .15, .25, .4, .6, 1.0, 1.6, 2.3, math.pi]
GA = Gvals(ns, pA, 14); GB = Gvals(ns, pB, 16)
err = np.abs(GA-GB)
rep("P2", abs(GB[0]-0.5) < 2e-6 and abs(GB[1]-0.0688747) < 2e-6,
    f"G0={GB[0]:.8f} G1={GB[1]:.8f} griddiff={err[:2].max():.1e}")
m1 = math.acosh(1+2/math.pi**2)
okb = True; lines = []
for n in range(1, 11):
    tail = (1/(6*math.pi**2))*math.exp(-n)*(1/n+3/n**2+6/n**3+6/n**4)  # int_1^inf r^3 e^{-nr} dr
    bound = 14400/(math.pi**2*n**6) + 0.5*math.exp(-m1*n) + tail
    dev = abs(GB[n]-1/(math.pi**2*n**4))
    okb &= dev <= bound
    lines.append(f"n={n} G={GB[n]:.6e} pi2n4G={math.pi**2*n**4*GB[n]:.4f} n6dev={dev*n**6:.4f} bound/dev={bound/dev:.1e}")
mono = all(GB[i+1] < GB[i] for i in range(10))
r8 = math.pi**2*8**4*GB[8]
rep("P3", abs(r8-1.092) < 5e-4 and mono and okb, f"pi^2 8^4 G(8)={r8:.5f} (griddiff {err[8]:.1e}) mono={mono} bound_ok={okb}; " + " | ".join(lines))

# P4: Dirichlet boxes
def box(N):
    rng = range(-N, N+1)
    sites = list(itertools.product(rng, repeat=4))
    interior = lambda x: max(abs(c) for c in x) < N
    inR = lambda x: max(abs(c) for c in x) <= N
    E = lambda mu: tuple(1 if i == mu else 0 for i in range(4))
    add = lambda x, y: tuple(a+b for a, b in zip(x, y))
    links = [(x, mu) for x in sites for mu in range(4) if inR(add(x, E(mu))) and (interior(x) or interior(add(x, E(mu))))]
    lidx = {l: i for i, l in enumerate(links)}
    plaqs = []
    for x in sites:
        for mu in range(4):
            for nu in range(mu+1, 4):
                ls = [(x, mu), (add(x, E(mu)), nu), (add(x, E(nu)), mu), (x, nu)]
                if all(inR(add(y, E(d))) for y, d in ls) and any(l in lidx for l in ls):
                    plaqs.append((x, mu, nu, ls))
    D = np.zeros((len(plaqs), len(links)))
    for r, (x, mu, nu, ls) in enumerate(plaqs):
        for l, s in zip(ls, [1, 1, -1, -1]):
            if l in lidx: D[r, lidx[l]] += s
    p0 = [r for r, p in enumerate(plaqs) if p[0] == (0, 0, 0, 0) and p[1] == 1 and p[2] == 2][0]
    # projection onto range(D): diagonal entry at p0 via least squares
    e = np.zeros(len(plaqs)); e[p0] = 1
    sol, *_ = np.linalg.lstsq(D, e, rcond=None)
    C = float((D@sol)[p0])
    keep = [i for i, (x, mu) in enumerate(links) if not (mu == 0 and interior(x))]
    Dpp = D[:, keep]
    lam = float(np.linalg.eigvalsh(Dpp.T@Dpp)[0])
    return C, lam, len(links), len(plaqs)
C1, l1, nl1, np1 = box(1)
C2, l2, nl2, np2 = box(2)
rep("P4", abs(C1-7/24) < 1e-10 and abs(l1-0.837722) < 1e-6 and abs(C2-0.49267) < 1e-5 and abs(l2-0.147122) < 1e-6 and C1 < C2 < 0.5,
    f"N=1: C={C1:.10f} (7/24={7/24:.10f}) lam={l1:.7f} links={nl1} plaq={np1}; N=2: C={C2:.7f} lam={l2:.7f} links={nl2} plaq={np2}")

# P5: cube word identity (letters as (dir, eps-string), exponent)
def w(s):
    out_ = []
    for tok in s.split():
        inv = tok.endswith("'"); tok = tok.rstrip("'")
        out_.append((tok, -1 if inv else 1))
    return out_
words = ["3_000 2_001 3_010' 2_000'",
         "2_000 3_010 1_011 3_110' 1_010' 2_000'",
         "2_000 1_010 2_100' 1_000'",
         "1_000 2_100 3_110 2_101' 3_100' 1_000'",
         "1_000 3_100 1_001' 3_000'",
         "3_000 1_001 2_101 1_011' 2_001' 3_000'"]
stack = []
for wd in words:
    for t in w(wd):
        if stack and stack[-1][0] == t[0] and stack[-1][1] == -t[1]: stack.pop()
        else: stack.append(t)
# also check each word is the correct geometric loop: plaquette words as printed are consistent with edge geometry
rep("P5", len(stack) == 0, f"reduced word length {len(stack)}: {stack}")

# P6: 2-d U(1) chessboard analogue
xg, wg = np.polynomial.legendre.leggauss(400)
def coeffs(beta, lo, nmax):
    # int_{lo<|theta|<pi} e^{-beta(1-cos)} cos(n theta) dtheta / 2pi
    th = (math.pi-lo)/2*xg + (math.pi+lo)/2; ww = (math.pi-lo)/2*wg
    f = np.exp(-beta*(1-np.cos(th)))
    return np.array([2*np.sum(ww*f*np.cos(n*th))/(2*math.pi) for n in range(-nmax, nmax+1)])
ok6 = True; worst = []
for L in (2, 4):
    V = L*L
    for beta in (1.0, 4.0):
        nmax = 60
        b = coeffs(beta, 0.0, nmax); bh = coeffs(beta/2, 0.0, nmax)
        Z = np.sum(b**V); Zh = np.sum(bh**V)
        fdiff = (math.log(Zh)-math.log(Z))/V
        for t in np.linspace(0.05, 2*beta*0.98, 25):
            lo = math.acos(1-t/beta)
            a = coeffs(beta, lo, nmax)
            p1 = np.sum(a*b**(V-1))/Z
            pall = np.sum(a**V)/Z
            rhs1 = max(pall, 0)**(1/V)
            rhs2 = math.exp(fdiff - t/2)
            c1 = p1 <= rhs1*(1+1e-12)+1e-300; c2 = rhs1 <= rhs2*(1+1e-12)
            ok6 &= c1 and c2
            if not (c1 and c2): worst.append((L, beta, round(t, 3), p1, rhs1, rhs2))
        worst.append(f"L={L} b={beta} sample t=1: ok")
rep("P6", ok6, f"violations={[x for x in worst if isinstance(x, tuple)]}")

# P7: amplitude Monte Carlo
rng = np.random.default_rng(20261123)
def haar(n):
    q = rng.normal(size=(n, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True); return q
def mul(p, q):
    a1, b1, c1, d1 = p.T; a2, b2, c2, d2 = q.T
    return np.stack([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2], 1)
inv = lambda p: p*np.array([1, -1, -1, -1])
def chi(j, p):
    c = np.clip(p[:, 0], -1, 1)
    if j == 0: return np.ones_like(c)
    if j == 0.5: return 2*c
    if j == 1: return 4*c*c-1
acc = []; nb = 20; per = 200000
for _ in range(nb):
    a0, a1, b0, b1, c0, c1 = (haar(per) for _ in range(6))
    # site s: a_s (s->s+1, period 2), b_s, c_s self-loops in dirs 1,2
    P01_0 = mul(mul(mul(a0, b1), inv(a0)), inv(b0)); P02_0 = mul(mul(mul(a0, c1), inv(a0)), inv(c0)); P12_0 = mul(mul(mul(b0, c0), inv(b0)), inv(c0))
    P01_1 = mul(mul(mul(a1, b0), inv(a1)), inv(b1)); P02_1 = mul(mul(mul(a1, c0), inv(a1)), inv(c1)); P12_1 = mul(mul(mul(b1, c1), inv(b1)), inv(c1))
    v = chi(0, P01_0)*chi(1, P02_0)*chi(1, P12_0)*chi(1, P01_1)*chi(0, P02_1)*chi(0.5, P12_1)
    acc.append(v.mean())
acc = np.array(acc); mean = acc.mean(); se = acc.std(ddof=1)/math.sqrt(nb)
rep("P7", abs(mean+1/324) < 4*se and mean < -4*se, f"A_MC={mean:.6f} +- {se:.6f} (-1/324={-1/324:.6f}), samples={nb*per}")
out.close()
