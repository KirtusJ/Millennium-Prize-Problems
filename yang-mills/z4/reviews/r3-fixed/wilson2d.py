"""wilson2d.py - W1/W2 of the builder brief, 2D Yang-Mills controls. Fixed before first run.

Conventions (hypothesis H, tested first):
  U(1):  c_r/c_0 = I_r(b)/I_0(b), b = N^2.   M_r(N) = -N^2 log(c_r/c_0).
  SU(2): spin j, c_j/c_0 = I_{2j+1}(b)/I_1(b), b = 4N^2 (dimension divided out).
  Z_n:   weight exp(b cos(2 pi k/n)); c_r = sum_k w_k cos(2 pi r k/n).
Wilson loop R x T, n = R*T*N^2 plaquettes (must be integer), W = (c_1/c_0)^n (free boundary /
infinite cylinder, vacuum projected outside). sigma_N(A) := -log W / A.

Predicates (tolerance sources in brackets):
 H : M_1(64) equals README 0.500061048820 (U1) and 0.375011444266 (SU2) to 1e-12
     [README prints 12 decimals: half-ulp 5e-13, doubled].
 Q : for-all hypothesis count: for N = 4..64 and A in {1/4,1/2,1}, report how many (N,A) have
     A*N^2 integer; predicates P1 below run only on those.
 P1: for every qualifying (N,A): |sigma_N(A) - M_1(N)| <= 1e-40 * M_1(N)
     [mp.dps = 60; 20 digits margin]. (Area law exact; sigma does not depend on A.)
 P2: sigma_N - sigma_inf > 0 for N=4,8,16,32,64 and the ratio of successive distances per doubling
     lies in [3,5]  [README's own approach band]; sigma_inf = 1/2 (U1), 3/8 (SU2) = gap*L, L=1.
 P3: Z_2 on b=N^2: 0 < sigma_N <= 1/(1+N^2) for N = 2..16 [proved bound z2_physical_gap_le
     with x = N^2], strictly decreasing; W(A=1) > 1 - 1e-10 at N=8 [README M(8)=3.3e-54 makes
     this loose]. Z_3 on b=N^2: sigma_N strictly decreasing over N=2,4,8,16, sigma_16 < 1e-100
     [README 1.31e-164].
 P4: Z_2 own trajectory b_N = artanh(exp(-1/(2N^2))): N^2(-log tanh b_N) = 1/2 to 1e-40 and
     b_N matches README 2.079, 2.773, 3.466, 4.159, 4.852 (N=4..64) to 5e-4 [3 printed decimals].
     Z_3 own trajectory (solve N^2(-log c1/c0)=1/2): measured only.
 P5: W2 observable f1 = (chi_1+chi_2)/sqrt2 (U1 charges 1,2; SU2 spins 1/2, 1); weights 1/2,1/2.
     First and second moments decrease strictly in N over N=4,8,16,32,64 (so bounded by N=4
     value) and |mom(64) - limit| < 1e-3 [O(1/N^2) rate, C~1 from README -> 2.4e-4, x4 margin].
     Limits: U1 mean 5/4, second 17/8; SU2 mean 11/16, second 73/128.
 P6: W2 observable f2 = heat-kernel delta at identity, width s = 1/4, centered (r=0 removed),
     normalized: weights |f_r|^2 ~ exp(-s r^2) (U1, r != 0), (2j+1)^2 exp(-s j(j+1)) (SU2, j>=1/2).
     Same predicates as P5, limits computed from M_r -> C_r/2 (U1 r^2/2, SU2 j(j+1)/2).
     Truncation |r| <= 40 / 2j <= 60: dropped weight < exp(-400) [bound on the tail].
 Measured only: N^2(sigma_N - sigma_inf) for SU2; Z_3 own trajectory b_N; correlators.
"""
import sys, json
import mpmath as mp
mp.mp.dps = 60
res = {"pred": {}, "data": {}}
met = failed = 0
def pred(name, ok, info=""):
    global met, failed
    res["pred"][name] = {"ok": bool(ok), "info": info}
    if ok: met += 1
    else: failed += 1
    print(("MET   " if ok else "FAIL  ") + name, info)

def rU1(r, N): b = mp.mpf(N)**2; return mp.besseli(r, b)/mp.besseli(0, b)
def rSU2(twoj, N): b = 4*mp.mpf(N)**2; return mp.besseli(twoj+1, b)/mp.besseli(1, b)
def MU1(r, N): return -mp.mpf(N)**2*mp.log(rU1(r, N))
def MSU2(twoj, N): return -mp.mpf(N)**2*mp.log(rSU2(twoj, N))

# H
pred("H_U1", abs(MU1(1,64)-mp.mpf("0.500061048820")) < 1e-12, mp.nstr(MU1(1,64),15))
pred("H_SU2", abs(MSU2(1,64)-mp.mpf("0.375011444266")) < 1e-12, mp.nstr(MSU2(1,64),15))

# Q + P1
areas = [mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(1)]
qual = [(N, A) for N in range(4, 65) for A in areas if mp.isint(A*N*N)]
print("Q: qualifying (N,A):", len(qual), "of", 61*3)
res["data"]["Q"] = [len(qual), 61*3]
for g, rho, M in (("U1", rU1, MU1), ("SU2", rSU2, MSU2)):
    worst = 0
    for N, A in qual:
        n = int(A*N*N); W = rho(1, N)**n
        s = -mp.log(W)/A; m = M(1, N)
        worst = max(worst, abs(s-m)/m)
    pred("P1_"+g, worst <= 1e-40, "max rel dev %s over %d cases" % (mp.nstr(worst,3), len(qual)))

Ns = [4, 8, 16, 32, 64]
for g, M, sinf in (("U1", MU1, mp.mpf(1)/2), ("SU2", MSU2, mp.mpf(3)/8)):
    d = [M(1, N)-sinf for N in Ns]
    ratios = [d[i]/d[i+1] for i in range(4)]
    res["data"]["sigma_"+g] = {N: mp.nstr(M(1,N),15) for N in Ns}
    res["data"]["N2dist_"+g] = {N: mp.nstr(N*N*dd,12) for N, dd in zip(Ns, d)}
    print(g, "sigma:", [mp.nstr(M(1,N),13) for N in Ns])
    print(g, "N^2(sigma-sinf):", [mp.nstr(N*N*dd,10) for N, dd in zip(Ns, d)])
    pred("P2_"+g, all(x > 0 for x in d) and all(3 <= r <= 5 for r in ratios),
         "ratios " + str([mp.nstr(r,5) for r in ratios]))

# Z_n
def zn_ratio(n, b, r=1):
    ks = range(n); w = [mp.exp(b*mp.cos(2*mp.pi*k/n)) for k in ks]
    return mp.fsum(w[k]*mp.cos(2*mp.pi*r*k/n) for k in ks)/mp.fsum(w)
mp.mp.dps = 400   # Z_n sigma at N=16 is ~1e-220: need many digits for 1 - rho
z2 = [(N, -N*N*mp.log(mp.tanh(mp.mpf(N)**2))) for N in [2, 4, 8, 16]]
ok = all(0 < s <= 1/(1+mp.mpf(N)**2) for N, s in z2) and all(z2[i][1] > z2[i+1][1] for i in range(3))
W8 = mp.tanh(mp.mpf(64))**64
pred("P3_Z2", ok and W8 > 1-mp.mpf(10)**-10, str([(N, mp.nstr(s,4)) for N, s in z2]) + " W(N=8,A=1)=1-" + mp.nstr(1-W8,3))
z3 = [(N, -N*N*mp.log(zn_ratio(3, mp.mpf(N)**2))) for N in [2, 4, 8, 16]]
pred("P3_Z3", all(z3[i][1] > z3[i+1][1] for i in range(3)) and z3[3][1] < mp.mpf(10)**-100,
     str([(N, mp.nstr(s,4)) for N, s in z3]))
res["data"]["Z2_b=N2"] = [(N, mp.nstr(s,5)) for N, s in z2]; res["data"]["Z3_b=N2"] = [(N, mp.nstr(s,5)) for N, s in z3]
mp.mp.dps = 60
readme = [2.079, 2.773, 3.466, 4.159, 4.852]
bs = [mp.atanh(mp.exp(-1/(2*mp.mpf(N)**2))) for N in Ns]
sig = [-N*N*mp.log(mp.tanh(b)) for N, b in zip(Ns, bs)]
pred("P4_Z2own", all(abs(s-mp.mpf(1)/2) < 1e-40 for s in sig) and all(abs(b-x) < 5e-4 for b, x in zip(bs, readme)),
     "b_N=" + str([mp.nstr(b,6) for b in bs]))
z3b = [mp.findroot(lambda b: -N*N*mp.log(zn_ratio(3, b)) - mp.mpf(1)/2, bb) for N, bb in zip(Ns, bs)]
res["data"]["Z3_own_b"] = {N: mp.nstr(b,8) for N, b in zip(Ns, z3b)}
print("Z3 own trajectory b_N (measured):", res["data"]["Z3_own_b"],
      "b_N - (2/3)log(N):", [mp.nstr(b-mp.mpf(2)/3*mp.log(N),6) for N, b in zip(Ns, z3b)])

# W2
def moments(levels):  # list of (weight, M)
    Z = mp.fsum(w for w, _ in levels)
    return mp.fsum(w*M for w, M in levels)/Z, mp.fsum(w*M*M for w, M in levels)/Z
s = mp.mpf(1)/4
obs = {
 "f1_U1": (lambda N: [(mp.mpf(1)/2, MU1(1,N)), (mp.mpf(1)/2, MU1(2,N))],
           [(mp.mpf(1)/2, mp.mpf(1)/2), (mp.mpf(1)/2, mp.mpf(2))]),
 "f1_SU2": (lambda N: [(mp.mpf(1)/2, MSU2(1,N)), (mp.mpf(1)/2, MSU2(2,N))],
            [(mp.mpf(1)/2, mp.mpf(3)/8), (mp.mpf(1)/2, mp.mpf(1))]),
 "f2_U1": (lambda N: [(2*mp.exp(-s*r*r), MU1(r,N)) for r in range(1,41)],
           [(2*mp.exp(-s*r*r), mp.mpf(r*r)/2) for r in range(1,41)]),
 "f2_SU2": (lambda N: [((tj+1)**2*mp.exp(-s*tj*(tj+2)/4), MSU2(tj,N)) for tj in range(1,61)],
            [((tj+1)**2*mp.exp(-s*tj*(tj+2)/4), mp.mpf(tj*(tj+2))/8) for tj in range(1,61)]),
}
for name, (lev, lim) in obs.items():
    L1, L2 = moments(lim)
    m = [moments(lev(N)) for N in Ns]
    dec = all(m[i][0] > m[i+1][0] and m[i][1] > m[i+1][1] for i in range(4))
    close = abs(m[-1][0]-L1) < 1e-3 and abs(m[-1][1]-L2) < 1e-3
    res["data"][name] = {"limits": [mp.nstr(L1,12), mp.nstr(L2,12)],
                         "moments": {N: [mp.nstr(a,12), mp.nstr(b,12)] for N, (a, b) in zip(Ns, m)}}
    pred("P5_"+name if name.startswith("f1") else "P6_"+name, dec and close,
         "lim (%s, %s); N=4 (%s, %s); N=64 (%s, %s)" % tuple(mp.nstr(x,8) for x in (L1, L2, m[0][0], m[0][1], m[-1][0], m[-1][1])))
    # ground-state energy of f: lowest atom
    res["data"][name]["lowest_atom_64"] = mp.nstr(lev(64)[0][1], 12)

res["counts"] = {"met": met, "failed": failed, "measured_only": 3}
out = sys.argv[1]
import os
assert not os.path.exists(out), "result file exists; never overwritten"
with open(out, "w", encoding="utf-8") as fh: json.dump(res, fh, indent=1, sort_keys=True, default=str)
print("met %d failed %d measured-only 3" % (met, failed))
sys.exit(0 if failed == 0 else 1)
