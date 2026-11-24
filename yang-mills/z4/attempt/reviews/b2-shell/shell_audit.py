"""shell_audit.py -- b2-shell worker (T215). Own program; predicates fixed before first run.

Conventions. N = 2m. Periodic coordinate distance d(c) = min(c, 2m-c), c in {0..2m-1}.
Axial representation (spatial.md): c_j(r) = int (s^{r-1} + s^{N-r-1}) dnu_j(s), 1<=r<=N-1.
Exact arithmetic: fractions.Fraction for all counting and all inequalities at rational s.
Irrational constants e: rational brackets E_LO = 2718281/10^6 < e < E_HI = 2718282/10^6,
always used in the direction that makes the check sufficient (no tolerance).
Claim 6 uses decimal with 50 digits; tolerance 1e-30 for equality of closed forms
(source: 50-digit working precision, loss < 10 digits in these few operations).

PREDICATES (each "for all" predicate is first tested per case; counts reported):
P1  (d=3) for m=1..12, r=1..m: brute tie-shared weight of axis 1 == 8r^2+2/3 (r<m), 4m^2-2m+1/3 (r=m).
P1b (d=3) antipode count (2m)^3-(2m-1)^3 == number of sites with r(x)=m; and sum_r w_r == (8m^3-1)/3.
P5  (d=2) for m=1..12: brute weight == 4r (r<m), 2m-1/2 (r=m); shell totals 8r, 4m-1.
P2a for m=1..12 and s in grid G (rational, [0,1)): A_m(s) <= 8(1+s)/(1-s)^3 + 2/(3(1-s)).
P2b same grid: A_m(s) <= 16/(1-s)^3 ;  P2c: A_m(s) <= 2 sum w_r == (16m^3-2)/3 for s in [0,1].
P2d unfolded coefficients of A_m equal w_l (l<m), 2w_m (l=m), w_{2m-l} (l>m) and each <= 8l^2+2/3.
P2e A_m(s) <= 8 min(m^3, 2/(1-s)^3) on grid incl. s=1 (m^3 branch).
P2f sharpness: ratio A_m(1-m^{-1/2}) / (2 m^{3/2}) increases towards 8 for m = 4^k, k=1..10 and is < 8.
P2g chain check: random positive atomic nu_j (seed 20261124), C(x)=min_j c_j(d(x_j)) (satisfies
    |C(x)|<=c_j(d(x_j))): chi <= C(0) + sum_j sum_r w_r c_j(r) <= C(0) + 8 sum_j I_j, m=1..6.
P3  for m=1..12, s in G u {1}: I/(48 e) <= W <= 2 I where integrand-level W(s)=sum_{r<=m} r^2(s^{r-1}+s^{2m-r-1}),
    I(s)=min(m^3, 2/(1-s)^3) (m^3 at s=1).  P3b floor(z) >= z/2 for z>=1 and the e^{-1} step
    s^{r-1} >= 1/e for r<=floor(z), z=min(m,1/t).
P4  kernel f(s)=(1-s^L)/(1-s)=sum_{k<L} s^k, L=N-1, N=2..64 even: (1-1/e) min(L,1/(1-s)) <= f <= min(L,1/(1-s)).
P4b sum_{r=1}^{N-1}(s^{r-1}+s^{N-r-1}) == 2 f(s) exactly.
P4c examples on N=4,6,8 (3D): C=1_{x_j=0} and C=1_{x=0}+N^-2 are PSD (all Fourier eigenvalues >= -1e-9,
    tolerance: float64 FFT on <=512 entries), chi = N^2 resp. N+1, and plane identity holds with
    rho=0 resp. rho=delta_1/2 (D_j(r)=1 for r>=1).
P5b A2_m(s)=sum_r w2_r(s^{r-1}+s^{2m-r-1}) <= 4 min(m^2,(1-s)^{-2}) on grid, m=1..12.
P6  chi(N) brute (3D sum, N<=32) == closed form S_s S_q^2/N; limit 2 coth(1/2); 2coth(1/2) == 2tanh(1/2)coth^2(1/2);
    W(N)/N^2 tends to a positive constant (ratio W(2N)/W(N) -> 4) for N=16..512.
Output: results_shell.txt (mode "x"). Exit 0 iff every predicate met.
"""
import itertools, random, sys
from fractions import Fraction as F
from decimal import Decimal, getcontext

out = open("results_shell.txt", "x")
fails = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
def pred(name, ok, info=""):
    log(("MET   " if ok else "FAILED"), name, info)
    if not ok: fails.append(name)

E_LO, E_HI = F(2718281, 10**6), F(2718282, 10**6)

def brute_weights(m, d):
    N = 2*m; w = {r: F(0) for r in range(1, m+1)}; cnt = {r: 0 for r in range(1, m+1)}
    for x in itertools.product(range(N), repeat=d):
        ds = [min(c, N-c) for c in x]; r = max(ds)
        if r == 0: continue
        cnt[r] += 1; k = ds.count(r)
        if ds[0] == r: w[r] += F(1, k)
    return w, cnt

def w3(m, r): return F(8*r*r) + F(2, 3) if r < m else F(4*m*m - 2*m) + F(1, 3)
def w2(m, r): return F(4*r) if r < m else F(2*m) - F(1, 2)

# ---- P1, P1b, P5
c1 = [0, 0]; c5 = [0, 0]; c1b = [0, 0]
for m in range(1, 13):
    W3, n3 = brute_weights(m, 3); W2, n2 = brute_weights(m, 2)
    for r in range(1, m+1):
        ok = W3[r] == w3(m, r); c1[0 if ok else 1] += 1
        if not ok: log("  P1 case fail m,r", m, r, W3[r], w3(m, r))
        ok = W2[r] == w2(m, r) and n2[r] == (8*r if r < m else 4*m-1); c5[0 if ok else 1] += 1
        if not ok: log("  P5 case fail m,r", m, r, W2[r], w2(m, r), n2[r])
    ok = n3[m] == (2*m)**3 - (2*m-1)**3 and sum(W3.values()) == F(8*m**3 - 1, 3)
    c1b[0 if ok else 1] += 1
    log(f"  m={m} antipode count {n3[m]} w_m={W3[m]} (2D w_m={W2[m]})")
pred("P1 3D weights", c1[1] == 0, f"cases met {c1[0]} failed {c1[1]}")
pred("P1b antipode count & total", c1b[1] == 0, f"cases met {c1b[0]} failed {c1b[1]}")
pred("P5 2D weights/totals", c5[1] == 0, f"cases met {c5[0]} failed {c5[1]}")

# ---- P2
G = [F(k, 64) for k in range(64)] + [F(1) - F(1, 10**k) for k in range(2, 7)]
def A(m, s, wf=w3): return sum(wf(m, r)*(s**(r-1) + s**(2*m-r-1)) for r in range(1, m+1))
c = {k: [0, 0] for k in "abce"}
for m in range(1, 13):
    for s in G + [F(1)]:
        a = A(m, s)
        if s < 1:
            for k, ok in (("a", a <= 8*(1+s)/(1-s)**3 + F(2, 3)/(1-s)), ("b", a <= 16/(1-s)**3),
                          ("e", a <= 8*min(F(m**3), 2/(1-s)**3))):
                c[k][0 if ok else 1] += 1
                if not ok: log("  P2", k, "fail", m, s)
        else:
            ok = a <= 8*m**3; c["e"][0 if ok else 1] += 1
        ok = a <= F(16*m**3 - 2, 3); c["c"][0 if ok else 1] += 1
for k in "abce": pred("P2" + k, c[k][1] == 0, f"cases met {c[k][0]} failed {c[k][1]}")
cd = [0, 0]
for m in range(1, 13):
    coef = {}
    for r in range(1, m+1):
        for e in (r-1, 2*m-r-1): coef[e+1] = coef.get(e+1, 0) + w3(m, r)
    for l in range(1, 2*m):
        want = w3(m, l) if l < m else (2*w3(m, m) if l == m else w3(m, 2*m-l))
        ok = coef.get(l, 0) == want and want <= 8*l*l + F(2, 3) and set(coef) == set(range(1, 2*m))
        cd[0 if ok else 1] += 1
pred("P2d unfolding", cd[1] == 0, f"cases met {cd[0]} failed {cd[1]}")
# sharpness (float; ratio only; uses closed form of the finite sums)
prev = 0; okf = True
for k in range(1, 11):
    m = 4**k; t = m**-0.5; s = 1 - t
    a = sum(w3(m, r).__float__()*(s**(r-1) + s**(2*m-r-1)) for r in range(1, m+1)) if m <= 4**7 else None
    if a is None:  # closed form for large m: sum_{l} coef_l s^{l-1}; use numpy-free float loop
        a = 0.0; p = 1.0
        for l in range(1, 2*m):
            cl = float(w3(m, l)) if l < m else (2*float(w3(m, m)) if l == m else float(w3(m, 2*m-l)))
            a += cl*p; p *= s
    ratio = a / (2*m**1.5)
    log(f"  sharp m={m} ratio={ratio:.6f}")
    okf = okf and prev <= ratio < 8; prev = ratio
pred("P2f sharpness monotone <8", okf, f"last ratio {prev:.6f}")
# chain check
rng = random.Random(20261124); cg = [0, 0]
for m in range(1, 7):
    N = 2*m
    nus = [[(F(rng.randint(0, 100), 100), F(rng.randint(1, 50), 100)) for _ in range(3)] for j in range(3)]
    cj = [[None] + [sum(wt*(s**(r-1) + s**(N-r-1)) for s, wt in nus[j]) for r in range(1, N)] for j in range(3)]
    C0 = max(cj[j][1] for j in range(3))  # C(0) >= c_j(1) is the only constraint used; take C(0)=max c_j(1)
    chi = C0
    for x in itertools.product(range(N), repeat=3):
        ds = [min(c_, N-c_) for c_ in x]
        if max(ds) == 0: continue
        chi += min(cj[j][ds[j]] for j in range(3) if ds[j] > 0) if any(ds) else 0
    rhs1 = C0 + sum(w3(m, r)*cj[j][r] for j in range(3) for r in range(1, m+1))
    I = sum(wt*(min(F(m**3), 2/(1-s)**3) if s < 1 else F(m**3)) for j in range(3) for s, wt in nus[j])
    ok = chi <= rhs1 <= C0 + 8*I; cg[0 if ok else 1] += 1
    log(f"  chain m={m}: chi={float(chi):.4f} shell={float(rhs1):.4f} 8I-bound={float(C0+8*I):.4f}")
pred("P2g chain", cg[1] == 0, f"cases met {cg[0]} failed {cg[1]}")

# ---- P3
c3 = [0, 0]; c3b = [0, 0]; worst_lo = None; worst_hi = None
for m in range(1, 13):
    for s in G + [F(1)]:
        Wv = sum(r*r*(s**(r-1) + s**(2*m-r-1)) for r in range(1, m+1))
        I = F(m**3) if s == 1 else min(F(m**3), 2/(1-s)**3)
        ok = I <= 48*E_LO*Wv and Wv <= 2*I; c3[0 if ok else 1] += 1
        if not ok: log("  P3 fail", m, s, float(Wv), float(I))
        lo = float(Wv/I); hi = float(Wv/I)
        worst_lo = lo if worst_lo is None else min(worst_lo, lo); worst_hi = hi if worst_hi is None else max(worst_hi, hi)
        t = 1 - s; z = F(m) if t == 0 else min(F(m), 1/t); fz = z.numerator // z.denominator
        # e-step: s^{fz-1} >= 1/e  <=>  e * s^{fz-1} >= 1 ; sufficient with E_LO
        ok = fz >= z/2 and (s**(fz-1))*E_LO >= 1 if not (s == 0 and fz == 1) else True
        c3b[0 if ok else 1] += 1
        if not ok: log("  P3b fail", m, s, fz, float(z))
pred("P3 two-sided W vs I", c3[1] == 0, f"cases met {c3[0]} failed {c3[1]}; min W/I={worst_lo:.5f} (1/(48e)={1/(48*2.718281828):.5f}) max W/I={worst_hi:.5f}")
pred("P3b floor and e-step", c3b[1] == 0, f"cases met {c3b[0]} failed {c3b[1]}")

# ---- P4
c4 = [0, 0]; c4b = [0, 0]
for N in range(2, 65, 2):
    L = N - 1
    for s in G:
        f = sum(s**k for k in range(L)); mn = min(F(L), 1/(1-s))
        ok = (1 - 1/E_HI)*mn <= f <= mn; c4[0 if ok else 1] += 1
        if not ok: log("  P4 fail", N, s, float(f), float(mn))
        ok = sum(s**(r-1) + s**(N-r-1) for r in range(1, N)) == 2*f; c4b[0 if ok else 1] += 1
pred("P4 kernel bounds", c4[1] == 0, f"cases met {c4[0]} failed {c4[1]}")
pred("P4b kernel identity", c4b[1] == 0, f"cases met {c4b[0]} failed {c4b[1]}")
import numpy as np
c4c = [0, 0]
for N in (4, 6, 8):
    x = np.indices((N, N, N))
    ex1 = (x[0] == 0).astype(float)
    ex2 = ((x[0] == 0) & (x[1] == 0) & (x[2] == 0)).astype(float) + N**-2
    for name, Cx, chi_w, Dr in (("1_{x_j=0}", ex1, N**2, [N**2] + [0]*(N-1)), ("delta+N^-2", ex2, N+1, [2] + [1]*(N-1))):
        ev = np.fft.fftn(Cx).real; psd = ev.min() >= -1e-9
        chi = Cx.sum(); D = [Cx[r].sum() for r in range(N)]
        rho_term = 0 if name.startswith("1_") else 2*0.5*(N-1)  # 2*int f drho, f(1)=L
        ok = psd and abs(chi-chi_w) < 1e-9 and np.allclose(D, Dr) and abs(D[0] + rho_term - chi) < 1e-9
        c4c[0 if ok else 1] += 1
        log(f"  ex N={N} {name}: min eig {ev.min():.3g} chi={chi:.4f} D0={D[0]:.4f} D1={D[1]:.4f}")
pred("P4c scope examples", c4c[1] == 0, f"cases met {c4c[0]} failed {c4c[1]}")

# ---- P5b
c5b = [0, 0]
for m in range(1, 13):
    for s in G:
        a = A(m, s, w2); ok = a <= 4*min(F(m*m), 1/(1-s)**2); c5b[0 if ok else 1] += 1
pred("P5b 2D hybrid kernel", c5b[1] == 0, f"cases met {c5b[0]} failed {c5b[1]}")

# ---- P6
getcontext().prec = 50
def kern(a, N): return [(a**r + a**(N-r))/(1 + a**N) for r in range(N)]
one = Decimal(1); q = (-one).exp()
h = one/2; coth = (h.exp() + (-h).exp())/(h.exp() - (-h).exp()); tanh = 1/coth
pred("P6 2coth(1/2)==2tanh(1/2)coth^2(1/2)", abs(2*coth - 2*tanh*coth*coth) < Decimal("1e-30"), f"2coth(1/2)={2*coth:.10f}")
c6 = [0, 0]; Ws = {}
for N in (16, 32, 64, 128, 256, 512):
    s = (-one/N).exp(); ks, kq = kern(s, N), kern(q, N)
    Ss, Sq = sum(ks), sum(kq); chi = Ss*Sq*Sq/N
    closed = (1+s)/(1-s)*(1-s**N)/(1+s**N) * ((1+q)/(1-q)*(1-q**N)/(1+q**N))**2 / N
    ok = abs(chi - closed) < Decimal("1e-30")
    if N <= 32:
        ksf = np.array([float(v) for v in ks]); kqf = np.array([float(v) for v in kq])
        Cx = (np.einsum('a,b,c->abc', ksf, kqf, kqf) + np.einsum('a,b,c->abc', kqf, ksf, kqf) + np.einsum('a,b,c->abc', kqf, kqf, ksf))/(3*N)
        ok = ok and abs(Cx.sum() - float(chi)) < 1e-9 and np.fft.fftn(Cx).real.min() >= -1e-9
    m = N//2
    W = sum(r*r*(ks[r] + 2*kq[r]) for r in range(1, m+1))/(3*N); Ws[N] = W
    c6[0 if ok else 1] += 1
    log(f"  N={N} chi={chi:.6f} W={W:.4f} W/N^2={W/N/N:.6f}")
pred("P6 chi brute==closed", c6[1] == 0, f"cases met {c6[0]} failed {c6[1]}")
r_last = Ws[512]/Ws[256]
pred("P6 W quadratic growth", abs(float(r_last) - 4) < 0.01, f"W(512)/W(256)={r_last:.5f}")
log(f"SUMMARY met {sum(1 for _ in [])} -- see lines; failed predicates: {fails}")
out.close()
sys.exit(1 if fails else 0)
