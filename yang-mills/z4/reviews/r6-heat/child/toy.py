"""TOY MODEL -- toy.py.  This is a TOY computation, not a proof of anything.

All predicates and tolerances below were fixed BEFORE the first run.
No randomness is used (everything is deterministic / exact DP), so no seeds.
Results go to results_<n>.txt with the smallest unused n (never overwritten).
Exit code 0 iff every pass/fail predicate passes; else exit 1 and list failures.

------------------------------------------------------------------------
PART A (TOY, exact optimization)
cost(x,L) = min_{m in Z, m>=1} [ x/m^2 + m^3 L ].
Continuous optimum: f(m) = x m^-2 + L m^3, f'(m)=0 <=> m*^5 = 2x/(3L).
  x m*^-2 = (3/2)^{2/5} x^{3/5} L^{2/5},  L m*^3 = (2/3)^{3/5} x^{3/5} L^{2/5}
  => K = (3/2)^{2/5} + (2/3)^{3/5} = (5/2)(2/3)^{3/5}  ~= 1.96013...
f is convex on m>0, so the integer min is at floor(m*) or ceil(m*) (or m=1).
Computed with mpmath at 250 digits (x up to 10^300).
[POST-RUN-1 REVISION, defect fix only: run 1 used 60 digits; for k>=145 the
 true excess ~3/(4 m*^2) ~ 10^(-0.4k) fell below working precision and the
 ratio rounded to 1-eps < 1, failing A1 spuriously.  Precision raised to 250
 digits (> 0.4*300+100).  Predicate and tol_A1 unchanged.  B1 NOT revised.]

 A1 (pass/fail): L=1, x=10^k, k=2..300.  For every x>=10^6:
     1 <= cost/(K x^{3/5}) <= 1 + tol_A1,  tol_A1 = 0.01.
     Source of tol: lower bound 1 is exact (continuous min <= integer min).
     With m = m*(1+d), cost/(K x^{3/5}) = (3/5)(1+d)^-2 + (2/5)(1+d)^3
     = 1 + 3 d^2 + O(d^3); best integer has |d| <= 1/(2 m*), and for x>=10^6
     m* >= (2e6/3)^{1/5} ~= 14.65, so the excess is <= 3/(4 m*^2) ~= 0.0035
     (+ O(d^3) ~ 1e-4).  tol 0.01 is ~3x that bound.  (k<6 are reported only.)
 A2 (pass/fail): L(x) = B + log(2+x), B = 1 + 6 c log(1/b), x = s/b^2,
     s=1, c=1  (so log(1/b) = (1/2) log x, B = 1 + 3 log x).
     Report r_k = log(cost)/log(x) at k in {3,6,12,50,100,300}.
     Predicate: g_k = |r_k - 3/5| strictly decreasing along that k list, AND
     g_300 < 0.05.  (0.05 is the threshold given in the statement; the
     expected g_300 ~ (log K + 0.4 log L)/log x ~ 0.006.)
 A3 (MEASURED ONLY, no pass/fail): c_up = 1/132000,
     U(x,B) = log(c_up * min(x^{3/5}, x/B)) / log x on the same trajectory
     and k list.  Report the first k in the list with U>=0 (and the first
     integer k in 2..300), and |U - 3/5| at k=300.

------------------------------------------------------------------------
PART B (TOY survival, d=1 analogue of Donsker-Varadhan, exponent 1/3)
Simple symmetric discrete-time walk on Z from 0; i.i.d. traps p=0.5 at
each site except the origin.  S(t) = E[(1-p)^{|R_t|-1}], R_t = range.
Exact DP over states (i,j) = (pos - min, max - pos); each step that visits a
new site multiplies the weight by q = 1-p.  S(t) = total weight.
The array is truncated at range-1 <= RMAX = 700: any discarded path has
already weight <= q^700 ~ 1e-211, so the truncation error on S(t) is
< 1e-200 for all t, far below S(2000) (expected ~1e-9..1e-12).

 B0 (pass/fail, exactness sanity check): DP equals brute-force enumeration
     of all 2^t paths for t = 1..14, relative error <= 1e-12
     (source: double rounding over <=14 steps, ~1e-15, with margin).
 B1 (pass/fail): least-squares slope of log(-log S(t)) vs log t over
     t in [500, 2000] (all integer t) lies within 0.06 of 1/3.
     Source of 0.06: finite-t corrections; -log S = a t^{1/3} + b log t + c
     + ..., and the b log t + c terms shift the local slope by
     O((b - (b log t + c)/3)/(a t^{1/3})); with a t^{1/3} ~ 10-20 at these t
     and |b|,|c| = O(1) this is a few hundredths.  Not revised.
     Local slopes (central difference over t/1.25..1.25t) are reported at
     several t (measured only).
"""
import math
import os
import sys
import itertools

import mpmath as mp
import numpy as np

mp.mp.dps = 250  # POST-RUN-1 DEFECT FIX: 60 digits < excess ~10^(-0.4k) at k>=145
HERE = os.path.dirname(os.path.abspath(__file__))
out_lines = []
failures = []


def say(s=""):
    print(s)
    out_lines.append(s)


# ---------------- Part A ----------------
K = mp.mpf(5) / 2 * (mp.mpf(2) / 3) ** (mp.mpf(3) / 5)
K_alt = (mp.mpf(3) / 2) ** (mp.mpf(2) / 5) + (mp.mpf(2) / 3) ** (mp.mpf(3) / 5)
assert abs(K - K_alt) < mp.mpf(10) ** -50


def cost(x, L):
    ms = (2 * x / (3 * L)) ** (mp.mpf(1) / 5)
    cands = {max(1, int(mp.floor(ms))), max(1, int(mp.ceil(ms))), 1}
    return min(x / mp.mpf(m) ** 2 + mp.mpf(m) ** 3 * L for m in cands)


say("TOY MODEL results (toy.py)")
say("K = (5/2)(2/3)^(3/5) = (3/2)^(2/5)+(2/3)^(3/5) = %s" % mp.nstr(K, 20))
say()
say("== A1 (L=1) ==")
TOL_A1 = 0.01
worst = (0, None)
a1_ok = True
for k in range(2, 301):
    x = mp.mpf(10) ** k
    r = cost(x, mp.mpf(1)) / (K * x ** (mp.mpf(3) / 5))
    if k >= 6:
        if not (r >= 1 and r <= 1 + TOL_A1):
            a1_ok = False
            failures.append("A1: k=%d ratio=%s" % (k, mp.nstr(r, 12)))
        if r - 1 > worst[0]:
            worst = (r - 1, k)
    if k in (2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 300):
        say("  k=%3d ratio=%s" % (k, mp.nstr(r, 12)))
say("  max excess over k>=6: %s at k=%s ; tol=%g -> A1 %s"
    % (mp.nstr(worst[0], 6), worst[1], TOL_A1, "MET" if a1_ok else "FAILED"))

say()
say("== A2 / A3 (trajectory s=1, c=1, L = B + log(2+x)) ==")
KLIST = [3, 6, 12, 50, 100, 300]
c, s, c_up = mp.mpf(1), mp.mpf(1), mp.mpf(1) / 132000


def traj(k):
    x = mp.mpf(10) ** k
    b = mp.sqrt(s / x)
    B = 1 + 6 * c * mp.log(1 / b)
    L = B + mp.log(2 + x)
    r = mp.log(cost(x, L)) / mp.log(x)
    U = mp.log(c_up * min(x ** (mp.mpf(3) / 5), x / B)) / mp.log(x)
    return x, B, L, r, U


say("  %4s %12s %16s %12s %16s %12s" % ("k", "L", "logcost/logx", "|r-3/5|", "U", "|U-3/5|"))
gaps = []
Us = {}
for k in KLIST:
    x, B, L, r, U = traj(k)
    g = abs(r - mp.mpf(3) / 5)
    gaps.append(g)
    Us[k] = U
    say("  %4d %12s %16s %12s %16s %12s" % (k, mp.nstr(L, 8), mp.nstr(r, 10), mp.nstr(g, 6),
                                          mp.nstr(U, 10), mp.nstr(abs(U - mp.mpf(3) / 5), 6)))
dec = all(gaps[i + 1] < gaps[i] for i in range(len(gaps) - 1))
a2_ok = dec and gaps[-1] < 0.05
if not dec:
    failures.append("A2: gap not strictly decreasing: %s" % [mp.nstr(g, 6) for g in gaps])
if not gaps[-1] < 0.05:
    failures.append("A2: gap at k=300 = %s >= 0.05" % mp.nstr(gaps[-1], 6))
say("  A2: decreasing=%s, gap(300)=%s < 0.05 -> A2 %s"
    % (dec, mp.nstr(gaps[-1], 6), "MET" if a2_ok else "FAILED"))
first_list = next((k for k in KLIST if Us[k] >= 0), None)
first_int = next((k for k in range(2, 301) if traj(k)[4] >= 0), None)
say("  A3 (measured only): first k in list with U>=0: %s ; first integer k: %s ; "
    "|U-3/5| at k=300 = %s" % (first_list, first_int, mp.nstr(abs(Us[300] - mp.mpf(3) / 5), 8)))

# ---------------- Part B ----------------
say()
say("== Part B (d=1 trapping toy, p=0.5) ==")
q = 0.5
RMAX = 700
TMAX = 2000


def dp_survival(T, rmax=RMAX):
    N = rmax + 1
    P = np.zeros((N, N))
    P[0, 0] = 1.0
    S = [1.0]
    for _ in range(T):
        new = np.zeros_like(P)
        new[:-1, 1:] += 0.5 * P[1:, :-1]          # left, old site
        new[0, 1:] += 0.5 * q * P[0, :-1]         # left, new site (i==0)
        new[1:, :-1] += 0.5 * P[:-1, 1:]          # right, old site
        new[1:, 0] += 0.5 * q * P[:-1, 0]         # right, new site (j==0)
        P = new
        S.append(P.sum())
    return S


def brute(t):
    tot = 0.0
    for steps in itertools.product((-1, 1), repeat=t):
        pos = lo = hi = 0
        for st in steps:
            pos += st
            lo, hi = min(lo, pos), max(hi, pos)
        tot += q ** (hi - lo)
    return tot / 2 ** t


Ssmall = dp_survival(14, rmax=30)
b0_err = max(abs(Ssmall[t] - brute(t)) / brute(t) for t in range(1, 15))
b0_ok = b0_err <= 1e-12
if not b0_ok:
    failures.append("B0: DP vs brute rel err %g" % b0_err)
say("  B0: max rel err DP vs brute force (t=1..14) = %.3e -> B0 %s"
    % (b0_err, "MET" if b0_ok else "FAILED"))

S = dp_survival(TMAX)
for t in (10, 100, 500, 1000, 2000):
    say("  S(%d) = %.6e   -log S = %.6f" % (t, S[t], -math.log(S[t])))
ts = np.arange(500, 2001)
y = np.log(-np.log(np.array([S[t] for t in ts])))
slope = np.polyfit(np.log(ts), y, 1)[0]
b1_ok = abs(slope - 1 / 3) <= 0.06
if not b1_ok:
    failures.append("B1: fitted slope %.5f, |slope-1/3|=%.5f > 0.06" % (slope, abs(slope - 1 / 3)))
say("  local slopes d log(-log S)/d log t (central, t/1.25..1.25t), measured only:")
for t in (40, 100, 200, 400, 800, 1200, 1600):
    t1, t2 = int(round(t / 1.25)), int(round(t * 1.25))
    ls = (math.log(-math.log(S[t2])) - math.log(-math.log(S[t1]))) / (math.log(t2) - math.log(t1))
    say("    t=%5d  slope=%.5f" % (t, ls))
say("  B1: LSQ slope over t in [500,2000] = %.5f ; |slope-1/3| = %.5f ; tol 0.06 -> B1 %s"
    % (slope, abs(slope - 1 / 3), "MET" if b1_ok else "FAILED"))

say()
if failures:
    say("FAILURES:")
    for f in failures:
        say("  " + f)
else:
    say("ALL PASS/FAIL PREDICATES MET (A1, A2, B0, B1). A3 measured only.")

n = 1
while os.path.exists(os.path.join(HERE, "results_%d.txt" % n)):
    n += 1
with open(os.path.join(HERE, "results_%d.txt" % n), "x", encoding="utf-8") as fh:
    fh.write("\n".join(out_lines) + "\n")
print("wrote results_%d.txt" % n)
sys.exit(1 if failures else 0)
