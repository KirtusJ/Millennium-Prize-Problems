"""lemmaGD.py -- independent checks of Lemma G, Lemma D, Lemma H, Lemma 3 constants, Lemma R inequality.

PREDICATES (fixed before first run):
 G1  G(0) = 1/2 within 2e-3 (quadrature tolerance: midpoint grid M=128 vs M=192 difference is reported;
     tolerance chosen as 10x the expected O(h^2) error of a |k|-type cusp, h=2pi/128).
 G2  for all n in 1..16: G(n) > 0  (per-case count reported).
 G3  for all n in 2..16: G(n) <= G(n-1) (monotone).
 G4  fitted exponent p of G(n)~n^-p on n=8..16 lies in [3.5,4.5] (expectation 4 from continuum F-F ~ |x|^-4;
     tolerance: lattice + quadrature corrections at n<=16).
 G5  file's lower bound c n^-5 with c=(4/pi^2)(16/3)(1/sqrt3)^5 e^-1/(2 sinh 1)/(2pi)^3 holds: G(n) >= c n^-5, n=1..16.
 D1  C^N_pp (projection of e_p0 onto range of d restricted to links with an interior endpoint, box [-N,N]^4)
     is nondecreasing in N=1,2,3,4,6 and < G(0)=1/2.  Compared with file's M1 values 0.2917 (N=2), 0.4927 (N=4):
     |diff| <= 2e-3 (LSQR tol 1e-10; tolerance = rounding of the 4 digits quoted + slack).
 D2  C^6(p0,p1) within 2e-3 of file value 0.0681 (amended after scipy failure, before any result: N=6 now feasible).
 H1  Lemma H: d restricted to columns (Lambda'_R minus T_int) has trivial kernel for boxes of side s=3,4,5,6
     (box [0,s-1]^4, shell = boundary sites); measured by smallest singular value > 1e-8 (dense SVD, s<=4;
     for s=5,6 rank via sparse QR-free method: min eigenvalue of D^T D by eigsh, tolerance 1e-8).
 L3c D* = 48 + 3 log((pi/2)^{5/2} 2^{3/2}) - 3 log c_H equals 60.19 within 0.01 ; zhat(b) <= (pi/2)^{5/2} b^-3/2
     for b in {0.5,1,2,4,8,16,64} (quadrature); Haar(B_s) >= c_H s^3 for s in {0.1,0.5,1}.
 R1  Wick-with-constant-random-background ratio >= (G(n)/G(0))^2 for all n=1..16 and backgrounds
     f = 0, f = const (|f|=1,3), f random N(0,s^2 I_3) s=0.5,2 (exact formula, no sampling).
 R2  measured only: with a NON-constant background f_{p_n} = -f_{p0} (harmonic? no -- only a stress test),
     the ratio can be negative -> shows constancy of h in Lemma R is load-bearing.
Output: lemmaGD_results.txt (mode 'x').
"""
import numpy as np, sys, math, itertools
# (scipy unavailable: own COO matvec + CG; dense eigvalsh for Lemma H)
class COO:
    def __init__(s, data, ij, shape):
        s.d=np.array(data,float); s.r=np.array(ij[0]); s.c=np.array(ij[1]); s.shape=shape
    def mv(s,x): return np.bincount(s.r, s.d*x[s.c], minlength=s.shape[0])
    def rmv(s,y): return np.bincount(s.c, s.d*y[s.r], minlength=s.shape[1])
    def cols(s, keep):
        m=-np.ones(s.shape[1],int); m[keep]=np.arange(len(keep)); sel=m[s.c]>=0
        return COO(s.d[sel],(s.r[sel],m[s.c][sel]),(s.shape[0],len(keep)))
    def dense(s):
        A=np.zeros(s.shape); np.add.at(A,(s.r,s.c),s.d); return A
def cg_proj(D, e, tol=1e-12, itmax=20000):
    # solve D^T D A = D^T e (consistent, PSD) by CG; return D A = projection of e on range(D)
    b=D.rmv(e); x=np.zeros_like(b); r=b.copy(); p=r.copy(); rs=r@r; b0=rs
    for it in range(itmax):
        Ap=D.rmv(D.mv(p)); al=rs/(p@Ap); x+=al*p; r-=al*Ap; rn=r@r
        if rn<tol**2*b0: break
        p=r+(rn/rs)*p; rs=rn
    return D.mv(x), it
out = open(sys.argv[1], "x")
def P(*s):
    print(*s, file=out); out.flush()
fails = []; met = 0; meas = 0
def pred(name, ok, info):
    global met
    P(f"{name}: {'met' if ok else 'FAILED'} {info}")
    if ok: met += 1
    else: fails.append(name)

# ---------- Lemma G -------------
def Gn(n, M):
    k = (np.arange(M) + 0.5) * 2 * np.pi / M - np.pi
    k1 = 4 * np.sin(k / 2) ** 2
    tot = 0.0
    for i in range(M):  # k1 slice
        a1 = k1[i]
        A2, A3 = np.meshgrid(k1, k1, indexing="ij")
        ksp = a1 + A2 + A3
        m = np.arccosh(1 + ksp / 2)
        tot += np.sum((a1 + A2) * np.exp(-m * n) / (2 * np.sinh(m)))
    return tot / M ** 3
Gs = {}
for n in range(0, 17):
    g1 = Gn(n, 128); g2 = Gn(n, 192)
    Gs[n] = g2
    P(f"G({n}) M=128 {g1:.7f}  M=192 {g2:.7f}  diff {g2-g1:.2e}")
pred("G1", abs(Gs[0] - 0.5) < 2e-3, f"G(0)={Gs[0]:.6f}")
q = sum(Gs[n] > 0 for n in range(1, 17)); pred("G2", q == 16, f"{q}/16 positive")
q = sum(Gs[n] <= Gs[n-1] for n in range(2, 17)); pred("G3", q == 15, f"{q}/15 monotone")
ns = np.arange(8, 17); p = -np.polyfit(np.log(ns), np.log([Gs[n] for n in ns]), 1)[0]
pred("G4", 3.5 <= p <= 4.5, f"fitted p={p:.3f}")
r = 1 / math.sqrt(3); c5 = (4 / math.pi**2) * (16 * r**5 / 3) * math.exp(-1) / (2 * math.sinh(1)) / (2 * math.pi) ** 3
q = sum(Gs[n] >= c5 * n ** -5 for n in range(1, 17)); pred("G5", q == 16, f"{q}/16; c={c5:.3e}, G(16)/(c 16^-5)={Gs[16]/(c5*16**-5):.3e}")
P("c(n)=(G(n)/G0)^2: " + " ".join(f"{n}:{(Gs[n]/Gs[0])**2:.3e}" for n in range(1, 17)))

# ---------- lattice helpers -------------
def build(sites_set, linkset):
    lidx = {l: i for i, l in enumerate(sorted(linkset))}
    return lidx
def box_D(N, center=True, s=None):
    """returns site set, interior, shell, link list Lambda' (links with an interior endpoint), plaquette rows."""
    if center:
        rng = range(-N, N + 1); inner = lambda x: max(abs(c) for c in x) < N
    else:
        rng = range(0, s); inner = lambda x: all(0 < c < s - 1 for c in x)
    sites = list(itertools.product(rng, repeat=4)); S = set(sites)
    E = lambda v, mu: tuple(v[i] + (1 if i == mu else 0) for i in range(4))
    Lp = []
    for x in sites:
        for mu in range(4):
            y = E(x, mu)
            if y in S and (inner(x) or inner(y)): Lp.append((x, mu))
    lidx = {l: i for i, l in enumerate(Lp)}
    rows = {}; data = []; ri = []; ci = []
    for x in sites:
        for mu in range(4):
            for nu in range(mu + 1, 4):
                ls = [((x, mu), 1), ((E(x, mu), nu), 1), ((E(x, nu), mu), -1), ((x, nu), -1)]
                if not all(E(E(x, mu), nu) in S for _ in [0]): continue
                if any(l in lidx for l, _ in ls):
                    r = rows.setdefault((x, mu, nu), len(rows))
                    for l, sg in ls:
                        if l in lidx: ri.append(r); ci.append(lidx[l]); data.append(sg)
    D = COO(data, (ri, ci), (len(rows), len(Lp)))
    return D, rows, lidx, inner
def Cpq(N, p, q):
    D, rows, lidx, _ = box_D(N)
    e = np.zeros(D.shape[0]); e[rows[p]] = 1.0
    proj, it = cg_proj(D, e)
    if q not in rows: return proj @ e, float('nan')
    eq = np.zeros(D.shape[0]); eq[rows[q]] = 1.0
    return proj @ e, proj @ eq
p0 = ((0, 0, 0, 0), 1, 2); p1 = ((1, 0, 0, 0), 1, 2)
Cs = {}
for N in (1, 2, 3, 4, 6):
    cpp, cp1 = Cpq(N, p0, p1); Cs[N] = cpp
    P(f"C^{N}_pp={cpp:.5f}  C^{N}(p0,p1)={cp1:.5f}")
ok = all(Cs[N] <= Cs[M] + 1e-9 for N,M in ((1,2),(2,3),(3,4),(4,6))) and Cs[6] < 0.5
pred("D1a", ok, "monotone and <1/2")
pred("D1b", abs(Cs[2] - 0.2917) <= 2e-3 and abs(Cs[4] - 0.4927) <= 2e-3 and abs(Cs[6]-0.4992)<=2e-3, f"N=2 {Cs[2]:.4f} vs 0.2917, N=4 {Cs[4]:.4f} vs 0.4927, N=6 {Cs[6]:.4f} vs 0.4992")
pred("D2", abs(cp1 - 0.0681) <= 2e-3, f"(file: C^6=0.0681) C^6(p0,p1)={cp1:.4f} G(1)={Gs[1]:.4f}")

# ---------- Lemma H -------------
for s in (3, 4, 5, 6):
    D, rows, lidx, inner = box_D(None, center=False, s=s)
    # T_int: links from interior sites in +e0 direction
    keep = [i for (x, mu), i in lidx.items() if not (mu == 0 and inner(x))]
    Dk = D.cols(np.array(sorted(keep))).dense()
    lam = np.linalg.eigvalsh(Dk.T @ Dk).min()
    pred(f"H1 s={s}", lam > 1e-8, f"unknowns={Dk.shape[1]} min eig Q={lam:.3e}")

# ---------- Lemma 3 constants -------------
cH = 2 * math.sin(1) ** 2 / (3 * math.pi)
Ds = 48 + 3 * math.log((math.pi / 2) ** 2.5 * 2 ** 1.5) - 3 * math.log(cH)
pred("L3c-D*", abs(Ds - 60.19) < 0.01, f"D*={Ds:.4f}")
a = (np.arange(200000) + 0.5) * math.pi / 200000; da = math.pi / 200000
okz = all(np.sum((2/math.pi)*np.sin(a)**2*np.exp(-b*(1-np.cos(a))))*da <= (math.pi/2)**2.5*b**-1.5 for b in (0.5,1,2,4,8,16,64))
okh = all((2/math.pi)*(s/2 - math.sin(2*s)/4) >= cH*s**3 for s in (0.1, 0.5, 1))
pred("L3c-bounds", okz and okh, f"zhat ok={okz} haar ok={okh}")
# finite-L 1/L terms: D_L(beta) - D* as function of L, beta (from the file's own bounds)
for beta in (1, 100, 1e4):
    for L in (2, 4, 8):
        up = 3 * (1 - 1 / L) * math.log((math.pi/2)**2.5 * (beta/2)**-1.5)
        lo = -48 + (3 + 1 / L) * math.log(cH * beta ** -1.5)
        meas += 1
        P(f"measured: beta={beta} L={L} bound D_L={up-lo:.3f} (D*={Ds:.3f})")

# ---------- Lemma R inequality -------------
def ratio(G, G0, Ef2, Varf2):
    return (1.5 * G**2 + G * Ef2 + 0.25 * Varf2) / (1.5 * G0**2 + G0 * Ef2 + 0.25 * Varf2)
okall = True; cnt = 0
for n in range(1, 17):
    c = (Gs[n] / Gs[0]) ** 2
    bgs = {"zero": (0, 0), "|f|=1": (1, 0), "|f|=3": (9, 0)}
    for s in (0.5, 2):  # f ~ N(0, s^2 I3): |f|^2 = s^2 chi2_3 ; E=3s^2, Var=6 s^4
        bgs[f"gauss s={s}"] = (3 * s * s, 6 * s ** 4)
    for k, (E2, V2) in bgs.items():
        rr = ratio(Gs[n], Gs[0], E2, V2); cnt += 1
        if rr < c * (1 - 1e-12): okall = False; P(f"R1 fail n={n} bg={k} ratio={rr} c={c}")
pred("R1", okall, f"{cnt} cases")
# stress: background with f_{pn} = -f_{p0} constant magnitude 3 (|f|^2 same at both, cross term sign flips)
# Cov = 1.5G^2 + G*E[f0.fn] + 1/4 Var|f|^2 ; with fn=-f0 deterministic: 1.5G^2 - 9G
for n in (1, 2, 4):
    rr = (1.5 * Gs[n]**2 - 9 * Gs[n]) / (1.5 * Gs[0]**2 + 9 * Gs[0]); meas += 1
    P(f"R2 measured: n={n} anti-correlated background ratio={rr:.4f} vs c(n)={(Gs[n]/Gs[0])**2:.4e}")
P(f"SUMMARY met={met} failed={len(fails)} measured_only={meas} fails={fails}")
out.close()
print(f"SUMMARY met={met} failed={len(fails)} measured_only={meas} fails={fails}")
sys.exit(0 if not fails else 1)
