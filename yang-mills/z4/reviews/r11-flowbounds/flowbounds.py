"""flowbounds.py -- r11-flowbounds, builder. Spatially flowed free lattice Maxwell benchmark.

Usage: python3 flowbounds.py <run_tag> [Nmax]
Writes results_<run_tag>.json (mode "x": never overwritten). Deterministic (no randomness; seed fixed at 0 anyway).

Object (l = 1 throughout, b = l/N):
  a_b(k) = P33(khat) (khat/2) e^{-2 s khat^2},  C_{b,s}(t) = (2/l^6) sum_{k,k'} |fhat_b(k+k')|^2 a_b(k) a_b(k') e^{-t(khat+khat')}
  computed in position space by FFT: D_t(x) = l^-3 sum_k e^{ik.bx} a_b(k)e^{-t khat}; C = 2 b^6 sum_xy f f D^2.
  Continuum C_s(t): same code with khat -> |k|, sum over a large box of n (Gaussian-truncated), f sampled
  on a fine grid (f entire => aliasing of ftilde ~ 1e-60, negligible).
f(y) = exp(0.8cos2pi y1 + 0.3 sin4pi y1 + 0.6 cos(2pi y2 - 0.4) + 0.5 sin2pi y3 + 0.3 cos 2pi(y1-y3)) -- non-symmetric, f>0.

PREDICATES (fixed before the first run):
 P0  position-space FFT value == momentum double sum at N=8 (s=0.005, t=0.05 and t=0): rel. diff <= 1e-10
     (tolerance: floating round-off of ~1e5 summands at 1e-16, with margin).
 P1  for all (N,s,t): v1(s,t) <= C_{b,s}(t) <= V(s), when b <= b0 (hypothesis tested per case, count qualifying).
 P1b for cases with N >= 2M(s)+1 and b<=b0: v2(s,t) <= C_{b,s}(t).
 P1c intermediate chain: C <= (2/l^3) Phi_b T_b (exact lattice T_b, exact Phi_b=b^3 sum f^2) <= V (tightness measured only).
 P2  for all (N,s), t=0: M1 <= M1bound, M2 <= M2bound, M0 >= v(s,0), hence M1/M0 <= R1(s), M2/M0 <= R2(s).
 P3  for all (N,s,t) with b<=b0: |C_{b,s}(t) - C_s(t)| <= K(s,t) b^2 (B2 theorem).
 P3b (added after the smoke run, before the main run) Parseval-form B2 bound:
     |C_{b,s}(t) - C_s(t)| <= K1 b^2 + K2 e^{-s/b^2} (both explicit), for all qualifying cases.
 P4  error ratio e_N/e_{2N} (e_N = C_{b,s}-C_s) in [3,5] when sqrt(s)*N >= 2 for the coarser N (count qualifying).
     Also successive-difference ratio (C_{N/2}-C_N)/(C_N-C_{2N}) in [3,5] when sqrt(s)*N/2 >= 2.
     Tolerance: e_N = c2 b^2 (1 + delta), delta ~ c4/c2 * b^2/s with |c4/c2| <~ 1 (next Taylor term of 2sin(x/2)
     relative x^2/80, and of the flow exponent 2s khat^2 relative b^2 k^2/12 at k^2~1/s), so |delta|<=1/4 at
     sqrt(s)/b>=2 and the ratio 4(1+delta)/(1+delta/4) lies in [3.2,4.8]; [3,5] adds margin.
 P5  claimed constant: R(s) = C_s(0) s^{5/2} / (sqrt(pi)/(640 pi^2) int f^2) -> 1. Predicate: |R(s)-1| decreasing as
     s decreases over s in {0.02,0.005,0.002,0.001,0.0005,0.00025} and |R-1| <= 0.05 at s=0.00025.
     (Tolerance: local-approximation correction ~ s * <|grad f|^2>/<f^2> ~ s*(2pi)^2*O(1) ~ 1-4% at the smallest s.)
 P6  measured only: s^{5/2} V(s), s^{1/2} R1(s), s R2(s) and s^{5/2} v2(s,0) as s decreases (scaling).
"""
import sys, json, math
import numpy as np

np.random.seed(0)
L = 1.0
PI = math.pi
tag = sys.argv[1]
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 128
out = open(f"results_{tag}.json", "x")

def fgrid(M):
    y = np.arange(M) * (L / M)
    y1, y2, y3 = np.meshgrid(y, y, y, indexing="ij")
    tp = 2 * PI
    return np.exp(0.8*np.cos(tp*y1) + 0.3*np.sin(2*tp*y1) + 0.6*np.cos(tp*y2 - 0.4)
                  + 0.5*np.sin(tp*y3) + 0.3*np.cos(tp*(y1 - y3)))

# ---- measured properties of f (fine grid, spectral derivatives) ----
MF = 64
ff = fgrid(MF)
nf = np.fft.fftfreq(MF) * MF
K1, K2, K3 = np.meshgrid(2*PI*nf, 2*PI*nf, 2*PI*nf, indexing="ij")
Ksq = K1**2 + K2**2 + K3**2
def lap2(g):
    return np.real(np.fft.ifftn(Ksq**2 * np.fft.fftn(g)))
dV = (L / MF) ** 3
I1 = ff.sum() * dV                     # int f (trapezoid = spectral for periodic entire f)
I2 = (ff**2).sum() * dV                # int f^2
L1 = np.abs(ff).sum() * dV             # ||f||_1 (= int f, f>0)
D4 = np.abs(lap2(ff)).sum() * dV       # ||Delta^2 f||_1 (quadrature, measured)
D4sq = np.abs(lap2(ff**2)).sum() * dV  # ||Delta^2 f^2||_1
supf = ff.max()                        # measured sup (fine grid 64^3; f entire, grid max within ~1e-3 rel)
# sup check on finer 1-d style: refine with 96^3
supf = max(supf, fgrid(96).max()) * 1.01  # 1% safety margin (measured quantity)

# ---- S4 = sum_{m != 0} |m|^-4 rigorous-ish (exact partial sum + integral tail) ----
Ls = 60
m = np.arange(-Ls, Ls + 1, dtype=float)
M1_, M2_, M3_ = np.meshgrid(m, m, m, indexing="ij")
r2 = M1_**2 + M2_**2 + M3_**2
r2[Ls, Ls, Ls] = np.inf
S4low = float((r2**-2).sum())
a_ = math.sqrt(3) / 2; U = Ls + 0.5 - a_
S4up = S4low + 4*PI*(1/U + a_/U**2 + a_**2/(3*U**3))
S4 = S4up

b0 = min(L/3, 2*PI*(abs(I1)/(2*S4*D4))**0.25)
F = L1 + S4*(b0/PI)**4*D4                       # sup_q |fhat_b(q)| for b<=b0 (aliasing lemma 2a)
Phi_free = L**3 * supf**2                        # b^3 sum f^2 <= l^3 sup f^2 (no b condition)
Phi_sharp = I2 + S4*(b0/(2*PI))**4*D4sq          # aliasing lemma for f^2 at q=0
Phi = min(Phi_free, Phi_sharp)

# ---- rigorous theta bounds ----
def th0(c): return 1 + math.sqrt(PI/c)
def th(j, c):  # sum_m m^{2j} e^{-c m^2}, j>=1, upper bound (unimodal: integral + max)
    return math.gamma(j + 0.5) * c**(-(j + 0.5)) + 2*(j/(math.e*c))**j
def Ub(q, c):  # upper bound of sum_{n in Z^3, n!=0} |n|^q e^{-c|n|^2}; odd q via |n|^q <= |n|^{q+1}
    if q % 2: q += 1
    t0, t2 = th0(c), th(1, c)
    if q == 2: return 3*t2*t0**2
    t4 = th(2, c)
    if q == 4: return 3*t4*t0**2 + 6*t2**2*t0
    t6 = th(3, c)
    if q == 6: return 3*t6*t0**2 + 18*t4*t2*t0 + 6*t2**3
    raise ValueError

from math import comb
def Ugen(q, c):  # generic: sum_{n!=0} |n|^q e^{-c|n|^2} <= sum over compositions of (q/2) of multinomial * prod theta
    if q % 2: q += 1
    p = q//2
    def T(j): return th0(c) if j == 0 else th(j, c)
    tot = 0.0
    for p1 in range(p+1):
        for p2 in range(p+1-p1):
            p3 = p - p1 - p2
            mult = math.factorial(p)//(math.factorial(p1)*math.factorial(p2)*math.factorial(p3))
            tot += mult*T(p1)*T(p2)*T(p3)
    return tot

def bounds(s, t):
    c = 64*s/L**2
    A0 = 0.25*(2*PI/L)**2*Ub(2, c); A2 = 0.25*(2*PI/L)**4*Ub(4, c); A4 = 0.25*(2*PI/L)**6*Ub(6, c)
    V = (2/L**3)*Phi*A0          # t-independent (C decreasing in t)
    k3 = 3*math.sqrt(3)/L; k2p = 2*PI/L
    mt = min(k3**2*math.exp(-2*t*k3), k2p**2*math.exp(-2*t*k2p))
    v1 = (1/(2*L**6))*I1**2*mt*math.exp(-4*s*k2p**2)
    Mcut = math.ceil(L/(PI*math.sqrt(s)))
    n = np.arange(-Mcut, Mcut+1, dtype=float)
    n1, n2, n3 = np.meshgrid(n, n, n, indexing="ij")
    kk1, kk2, kk3 = (2*PI/L)*n1, (2*PI/L)*n2, (2*PI/L)*n3
    ksq = kk1**2 + kk2**2 + kk3**2; ksq[Mcut, Mcut, Mcut] = 1.0
    term = (kk1**2 + kk2**2)**2/ksq*np.exp(-2*t*np.sqrt(ksq) - 4*s*ksq)
    term[Mcut, Mcut, Mcut] = 0
    v2 = (1/(2*L**6))*I1**2*(16/PI**6)*float(term.sum())
    M1b = (4/L**3)*Phi*math.sqrt(A0*A2); M2b = (4/L**3)*Phi*(math.sqrt(A0*A4) + A2)
    # B2 constant
    c2 = 32*s/L**2; c3 = 16*s/L**2
    Sa = (PI/L)*Ub(2, c2); Sas = (PI/L)*Ub(2, c3)
    q = 2*PI/L
    Sh = (1/24)*(1.5*q**3*Ub(4, c2) + (t/2)*q**4*Ub(4, c2) + 2*s*q**5*Ub(6, c2))
    Kal = (F + L1)*S4*D4*b0**2/PI**4*Sa**2
    Kterm = 2*L1**2*Sh*Sa
    Ktail = 2*(F**2 + 2*L1**2)*Sas*Sa/(math.e*s)
    K = (2/L**6)*(Kal + Kterm + Ktail)
    # Parseval form: K1 b^2 + K2 e^{-s/b^2}
    Sa2 = (PI/L)**2*Ugen(2, 64*s/L**2)          # sum abar^2
    Sas2 = (PI/L)**2*Ugen(2, 32*s/L**2)         # sum abar*^2 (half exponent)
    Sh2 = (3/576)*(2.25*q**6*Ugen(6, 64*s/L**2) + (t**2/4)*q**8*Ugen(8, 64*s/L**2)
                   + 4*s**2*q**10*Ugen(10, 64*s/L**2))
    K1 = (2/L**6)*((F + L1)*S4*D4*b0**2/PI**4*Sa**2 + 2*L**3*I2*math.sqrt(Sh2*Sa2))
    K2 = (2/L**6)*2*L**3*(Phi + 2*I2)*math.sqrt(Sas2*Sa2)
    return dict(V=V, v1=v1, v2=v2, Mcut=Mcut, A0=A0, A2=A2, A4=A4, M1b=M1b, M2b=M2b, K=K, K1=K1, K2=K2,
                K_parts=[(2/L**6)*Kal, (2/L**6)*Kterm, (2/L**6)*Ktail])

def correlator(N, s, t, continuum=False):
    """Return C, M1, M2 (t-derivative moments at given t), T (= l^-3 sum a^2 e^{-2t w}), Phi_b."""
    b = L/N
    n = np.fft.fftfreq(N)*N
    k = 2*PI*n/L
    kh = k if continuum else (2/b)*np.sin(k*b/2)
    h1, h2, h3 = np.meshgrid(kh, kh, kh, indexing="ij")
    hsq = h1**2 + h2**2 + h3**2
    h = np.sqrt(hsq)
    hsq0 = hsq.copy(); hsq0[0, 0, 0] = 1.0
    a = (h1**2 + h2**2)/hsq0*(h/2)*np.exp(-2*s*hsq - t*h)
    a[0, 0, 0] = 0.0
    fx = fgrid(N)
    Fq = np.fft.fftn(fx)
    pref = N**3/L**3
    D0 = np.real(np.fft.ifftn(a))*pref
    D1 = np.real(np.fft.ifftn(a*h))*pref
    D2 = np.real(np.fft.ifftn(a*hsq))*pref
    absF2 = np.abs(Fq)**2
    def quad(G):
        return 2*b**6*float(np.real(np.sum(absF2*np.fft.fftn(G))))/N**3
    C = quad(D0*D0); M1 = quad(2*D0*D1); M2 = quad(2*D0*D2 + 2*D1*D1)
    T = float((a**2).sum())/L**3
    Phib = b**3*float((fx**2).sum())
    fhat0 = b**3*float(fx.sum())
    return C, M1, M2, T, Phib, fhat0

def momentum_direct(N, s, t):
    b = L/N
    n = np.fft.fftfreq(N)*N
    k = 2*PI*n/L
    kh = (2/b)*np.sin(k*b/2)
    h1, h2, h3 = np.meshgrid(kh, kh, kh, indexing="ij")
    hsq = h1**2 + h2**2 + h3**2; h = np.sqrt(hsq); hsq[0, 0, 0] = 1
    a = (h1**2 + h2**2)/hsq*(h/2)*np.exp(-2*s*h**2); a[0, 0, 0] = 0
    fh = b**3*np.fft.fftn(fgrid(N))  # fhat_b(q) at q index; fhat_b(k+k') index (i+i') mod N
    idx = np.arange(N)
    tot = 0.0
    af = a.ravel(); hf = h.ravel()
    I, J, Kx = np.meshgrid(idx, idx, idx, indexing="ij")
    I, J, Kx = I.ravel(), J.ravel(), Kx.ravel()
    for p in range(N**3):
        if af[p] == 0: continue
        q = ((I + I[p]) % N, (J + J[p]) % N, (Kx + Kx[p]) % N)
        tot += float(np.sum(np.abs(fh[q])**2*af*af[p]*np.exp(-t*(hf + hf[p]))))
    return 2/L**6*tot

res = dict(f="exp(0.8cos2pi y1+0.3sin4pi y1+0.6cos(2pi y2-0.4)+0.5sin2pi y3+0.3cos2pi(y1-y3))",
           inputs=dict(I1=I1, I2=I2, L1=L1, D4=D4, D4sq=D4sq, supf_with_margin=supf, S4low=S4low,
                       S4up=S4up, b0=b0, F=F, Phi_free=Phi_free, Phi_sharp=Phi_sharp, Phi=Phi))
print(json.dumps(res["inputs"]), flush=True)
pred = {}
def record(name, ok, info):
    pred.setdefault(name, {"met": 0, "failed": 0, "qualifying": 0, "fail_cases": []})
    pred[name]["qualifying"] += 1
    if ok: pred[name]["met"] += 1
    else:
        pred[name]["failed"] += 1; pred[name]["fail_cases"].append(info)

# P0
for t in (0.0, 0.05):
    Cf = correlator(8, 0.005, t)[0]; Cm = momentum_direct(8, 0.005, t)
    rel = abs(Cf - Cm)/abs(Cm)
    record("P0", rel <= 1e-10, dict(t=t, Cf=Cf, Cm=Cm, rel=rel))
    res.setdefault("P0", []).append(dict(t=t, C_fft=Cf, C_mom=Cm, rel=rel))

Ns = [N for N in (8, 16, 32, 64, 128, 256) if N <= NMAX]
S = (0.002, 0.005, 0.02); Ts = (0.0, 0.05, 0.1)
rows = []
cont = {}
for s in S:
    for t in Ts:
        Cc, M1c, M2c, _, _, _ = correlator(128, s, t, continuum=True)
        cont[(s, t)] = Cc
        bd = bounds(s, t)
        res.setdefault("continuum", []).append(dict(s=s, t=t, C=Cc, M1=M1c, M2=M2c, **{k: bd[k] for k in ("V", "v1", "v2", "K", "K1", "K2", "K_parts", "M1b", "M2b", "Mcut")}))
        for N in Ns:
            b = L/N
            C, M1, M2, T, Phib, fh0 = correlator(N, s, t)
            r = dict(N=N, s=s, t=t, C=C, M1=M1, M2=M2, T=T, Phib=Phib, fhat0=fh0, err=C - Cc)
            rows.append(r)
            print(json.dumps(r), flush=True)
            if b <= b0:
                record("P1", bd["v1"] <= C <= bd["V"], r)
                record("P1_fhat0_half", fh0 >= I1/2, r)
                inter = (2/L**3)*Phib*T
                record("P1c", C <= inter*(1+1e-12) and inter <= bd["V"], dict(r, inter=inter, V=bd["V"]))
                if N >= 2*bd["Mcut"] + 1:
                    record("P1b", bd["v2"] <= C, dict(r, v2=bd["v2"]))
                record("P3", abs(C - Cc) <= bd["K"]*b**2, dict(r, Kb2=bd["K"]*b**2))
                kb = bd["K1"]*b**2 + bd["K2"]*math.exp(-s/b**2)
                record("P3b", abs(C - Cc) <= kb, dict(r, K1b2_K2e=kb))
                r["K1b2_K2e"] = kb
            if t == 0.0 and b <= b0:
                vv = max(bd["v1"], bd["v2"] if N >= 2*bd["Mcut"] + 1 else 0)
                record("P2", M1 <= bd["M1b"] and M2 <= bd["M2b"] and C >= vv,
                       dict(r, M1b=bd["M1b"], M2b=bd["M2b"], v=vv))
res["rows"] = rows
# P4
for s in S:
    for t in Ts:
        e = {r["N"]: r["err"] for r in rows if r["s"] == s and r["t"] == t}
        Cn = {r["N"]: r["C"] for r in rows if r["s"] == s and r["t"] == t}
        for N in Ns:
            if 2*N in e and math.sqrt(s)*N >= 2:
                ratio = e[N]/e[2*N]
                record("P4_err", 3 <= ratio <= 5, dict(s=s, t=t, N=N, ratio=ratio))
                res.setdefault("P4_err", []).append(dict(s=s, t=t, N=N, ratio=ratio))
            if N//2 in Cn and 2*N in Cn and math.sqrt(s)*N/2 >= 2:
                ratio = (Cn[N//2] - Cn[N])/(Cn[N] - Cn[2*N])
                record("P4_diff", 3 <= ratio <= 5, dict(s=s, t=t, N=N, ratio=ratio))
                res.setdefault("P4_diff", []).append(dict(s=s, t=t, N=N, ratio=ratio))
# P5 claimed constant
const = math.sqrt(PI)/(640*PI**2)*I2
P5 = []
for s, M in ((0.02, 32), (0.005, 48), (0.002, 64), (0.001, 64), (0.0005, 96), (0.00025, 128)):
    Cc = correlator(M, s, 0.0, continuum=True)[0]
    R = Cc*s**2.5/const
    bd = bounds(s, 0.0)
    P5.append(dict(s=s, M=M, C0=Cc, R=R, V_s52=bd["V"]*s**2.5, v2_s52=bd["v2"]*s**2.5,
                   R1_sqrt_s=bd["M1b"]/max(bd["v1"], bd["v2"])*math.sqrt(s),
                   R2_s=bd["M2b"]/max(bd["v1"], bd["v2"])*s,
                   M1M0_cont=None))
    print(json.dumps(P5[-1]), flush=True)
dev = [abs(p["R"] - 1) for p in P5]
record("P5", all(dev[i+1] < dev[i] for i in range(len(dev) - 1)) and dev[-1] <= 0.05, dict(dev=dev))
res["P5"] = P5
res["predicates"] = pred
json.dump(res, out, indent=1, default=float)
out.close()
print(json.dumps({k: (v["met"], v["failed"], v["qualifying"]) for k, v in pred.items()}))
sys.exit(0)
