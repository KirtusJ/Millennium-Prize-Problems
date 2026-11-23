"""Director Z4 | Yang-Mills | exact two-dimensional control for the scaling trajectory.

Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada.
Program drafted with assistance from Claude (Anthropic), acting as Director Z4.

WHAT IS COMPUTED
Lattice gauge theory with the Wilson plaquette weight on a cylinder: the space is a
circle of N links of length a = L/N, time advances in steps of a. Gauge-invariant
states are class functions of the holonomy. With the plaquette weight expanded in
irreducible characters, w(U) = sum_r d_r c_r(beta) chi_r(U), gluing the N plaquettes
of one time slab gives the transfer operator diagonal in characters with eigenvalue
c_r(beta)^N. The gap in lattice units is m = -N log(c_1/c_0) for the lowest
non-trivial character, and the gap in physical units is M = m / a.
Conventions: L = 1, g = 1; U(1): w = exp(beta cos theta), beta = 1/(g a)^2 = N^2;
SU(2): w = exp((beta/2) Tr U), beta = 4/(g a)^2 = 4 N^2; Z_n: w = exp(beta cos(2 pi j/n)),
beta = N^2 (the same trajectory as U(1)). Zero is not a member of any tested N.
Continuum values (heat-kernel, g^2 L C_2 / 2): U(1) charge 1: 1/2; SU(2) spin 1/2: 3/8.

PREDICATES (fixed before the first run)
 H  (hypothesis test, per case) the character coefficients used are the Haar integrals
    of the weight: closed forms (Bessel I_n; I_{2j+1}) agree with direct quadrature of
    exp(beta(cos-1)) against the character to relative 1e-25 at 40 digits working
    precision. Basis of the tolerance: 15 digits of guard below the 40 carried.
    The number of cases that qualify is reported; a case that fails H is excluded
    from P1..P3 and listed.
 P1 U(1): M(N) > 1/2 for every tested N, and D(N) = N^2 (M(N) - 1/2) - 1/4 shrinks
    by a factor in [3, 5] at each doubling of N. Basis: a correction of order N^-2
    to D gives the factor 4; the window is +-25 per cent of 4 and the factors are
    reported so that the window can be judged.
 P2 SU(2): M(N) > 3/8 for every tested N and M(N) - 3/8 shrinks by a factor in
    [3, 5] at each doubling. Same basis (leading correction of order N^-2).
 P3 Adverse control, Z_n for n in {2, 3, 5} on the U(1) trajectory beta = N^2:
    M(N) is strictly decreasing over the tested N and M(N) / A_n(N) lies within
    1e-6 of 1 at the largest N, where A_n(N) = N^2 k_n d_n exp(-N^2 d_n),
    d_n = 1 - cos(2 pi / n), k_2 = 1, k_n = 2 otherwise. Basis: the next term of
    the expansion is smaller by exp(-N^2 e_n) with e_n the next spacing of the
    cosine levels, far below 1e-6 at the largest N; the ratio is reported.
    Meaning if met: a finite gauge group on the Yang-Mills trajectory has physical
    gap tending to zero, not to a positive number.
Tested N: 4, 8, 16, 32, 64 (P1, P2); 2, 4, 8, 16 (P3).

OUTPUT  two_dim_control_result.json, refused if it exists. No random numbers.
RERUN   python -I two_dim_control.py <mpmath site directory>
"""
import json, os, sys
sys.path.append(sys.argv[1])
import mpmath as mp

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "two_dim_control_result.json")
if os.path.exists(OUT):
    sys.exit("result file exists; refusing to overwrite")

def s(x, n=30):
    return mp.nstr(x, n)

res = {"program": "two_dim_control.py", "dps": mp.mp.dps, "argv": sys.argv[1:2] and ["<mpmath site directory>"],
       "H": [], "P1": {}, "P2": {}, "P3": {}, "verdicts": {}}

# ---------- H: closed forms against Haar quadrature (scaled by exp(-beta)) ----------
def u1_closed(n, b):  return mp.besseli(n + 1, b) * mp.exp(-b)
def u1_quad(n, b):
    f = lambda t: mp.exp(b * (mp.cos(t) - 1)) * mp.cos(n * t)
    w = 6 / mp.sqrt(b)                      # the weight is below exp(-18) outside |t| < w
    pts = [-mp.pi, -w, 0, w, mp.pi] if w < mp.pi else [-mp.pi, 0, mp.pi]
    return mp.quad(f, pts) / (2 * mp.pi)
def su2_closed(twoj, b):                    # c_j = 2 I_{2j+1}(b) / b
    return 2 * mp.besseli(twoj + 1, b) / b * mp.exp(-b)
def su2_quad(twoj, b):                      # Haar on classes: (2/pi) sin^2 phi dphi
    d = twoj + 1
    f = lambda p: mp.exp(b * (mp.cos(p) - 1)) * mp.sin(d * p) * mp.sin(p)
    w = 6 / mp.sqrt(b)
    pts = [0, w, mp.pi] if w < mp.pi else [0, mp.pi]
    return (2 / mp.pi) * mp.quad(f, pts) / d

TOL_H = mp.mpf(10) ** -25
NS = [4, 8, 16, 32, 64]
qual_u1, qual_su2 = [], []
for N in NS:
    b = mp.mpf(N) ** 2
    ok = True
    for n in (0, 1):
        c, q = u1_closed(n, b), u1_quad(n, b)
        rel = abs(c - q) / abs(c); ok &= rel < TOL_H
        res["H"].append({"group": "U(1)", "N": N, "beta": s(b), "label": n, "rel_diff": s(rel, 5), "met": bool(rel < TOL_H)})
    if ok: qual_u1.append(N)
    b = 4 * mp.mpf(N) ** 2
    ok = True
    for twoj in (0, 1):
        c, q = su2_closed(twoj, b), su2_quad(twoj, b)
        rel = abs(c - q) / abs(c); ok &= rel < TOL_H
        res["H"].append({"group": "SU(2)", "N": N, "beta": s(b), "label": "2j=%d" % twoj, "rel_diff": s(rel, 5), "met": bool(rel < TOL_H)})
    if ok: qual_su2.append(N)
res["H_qualify"] = {"U(1)": qual_u1, "SU(2)": qual_su2, "of": NS}

def doubling_factors(vals):
    return [vals[i] / vals[i + 1] for i in range(len(vals) - 1)]

# ---------- P1: U(1) ----------
M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(1, mp.mpf(N) ** 2) / mp.besseli(0, mp.mpf(N) ** 2)) for N in qual_u1}
D = [abs(mp.mpf(N) ** 2 * (M[N] - mp.mpf(1) / 2) - mp.mpf(1) / 4) for N in qual_u1]
fac = doubling_factors(D)
res["P1"] = {"N": qual_u1, "M": [s(M[N]) for N in qual_u1], "D": [s(d, 12) for d in D], "factors": [s(f, 8) for f in fac]}
p1 = len(qual_u1) >= 2 and all(M[N] > mp.mpf(1) / 2 for N in qual_u1) and all(3 <= f <= 5 for f in fac)

# ---------- P2: SU(2) ----------
M2 = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, 4 * mp.mpf(N) ** 2) / mp.besseli(1, 4 * mp.mpf(N) ** 2)) for N in qual_su2}
E = [M2[N] - mp.mpf(3) / 8 for N in qual_su2]
fac2 = doubling_factors(E)
res["P2"] = {"N": qual_su2, "M": [s(M2[N]) for N in qual_su2], "M_minus_3_8": [s(e, 12) for e in E], "factors": [s(f, 8) for f in fac2]}
p2 = len(qual_su2) >= 2 and all(e > 0 for e in E) and all(3 <= f <= 5 for f in fac2)

# ---------- P3: Z_n adverse control ----------
mp.mp.dps = 400                             # the ratio differs from 1 by as little as exp(-256 d_n)
p3 = True
for n in (2, 3, 5):
    d = 1 - mp.cos(2 * mp.pi / n); k = 1 if n == 2 else 2
    Ms, ratios = [], []
    for N in (2, 4, 8, 16):
        b = mp.mpf(N) ** 2
        lam = lambda kk: mp.fsum(mp.exp(b * (mp.cos(2 * mp.pi * j / n) - 1)) * mp.cos(2 * mp.pi * j * kk / n) for j in range(n))
        Mn = -b * mp.log(lam(1) / lam(0))
        A = b * k * d * mp.exp(-b * d)
        Ms.append(Mn); ratios.append(Mn / A)
    dec = all(Ms[i] > Ms[i + 1] for i in range(3))
    near = abs(ratios[-1] - 1) < mp.mpf(10) ** -6
    p3 &= dec and near
    res["P3"]["Z_%d" % n] = {"N": [2, 4, 8, 16], "M": [s(x, 12) for x in Ms], "M_over_A": [s(x, 15) for x in ratios],
                             "strictly_decreasing": bool(dec), "ratio_within_1e-6_at_N16": bool(near)}

h_all = all(h["met"] for h in res["H"])
res["verdicts"] = {"H_all_cases": "MET" if h_all else "FAILED", "P1": "MET" if p1 else "FAILED",
                   "P2": "MET" if p2 else "FAILED", "P3": "MET" if p3 else "FAILED"}
with open(OUT, "x", encoding="utf-8", newline="\n") as f:
    json.dump(res, f, indent=1, sort_keys=True); f.write("\n")
for k, v in res["verdicts"].items(): print(k, v)
print("H qualify", res["H_qualify"])
print("P1 factors", res["P1"]["factors"], "M", res["P1"]["M"][-1])
print("P2 factors", res["P2"]["factors"], "M", res["P2"]["M"][-1])
for n in (2, 3, 5): print("P3 Z_%d" % n, res["P3"]["Z_%d" % n]["M"], res["P3"]["Z_%d" % n]["M_over_A"][-1])
sys.exit(0 if (h_all and p1 and p2 and p3) else 1)
