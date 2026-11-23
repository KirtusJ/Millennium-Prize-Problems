"""negnum.py -- recompute every derived number printed in sec_negative.tex from source values.

Usage: python3 negnum.py <result_file>   (result file opened with mode "x"; never overwritten)
No randomness (no seed needed).

Predicates, fixed before the first run. Tolerance: half a unit in the last printed digit
of the number as printed in the paper/ledger (rounding tolerance; source: the printed digits).
 N1  q_i = R(1 step)/R(0) at N=6,8,12 equals 0.270, 0.323, 0.385 (ledger) to 5e-4.
 N2  xi_i = 1/(3.74 * a sqrt(sigma)) equals 0.72, 1.01, 1.40 (ledger) to 5e-3.
 N3  xi_i (1 - q_i) equals 0.53, 0.68, 0.86 (ledger) to 5e-3.
 N4  log-log slope of xi(1-q) against xi between the outer points equals 0.75 to 0.05
     (ledger says "roughly like xi^0.75"; tolerance 0.05 because "roughly" is two digits).
 N5  union of measured kappa_H ranges (builder + challenger, periodic) is [-2.30, -1.12]
     (exact on the printed numbers).
 N6  builder sample count with kappa_H measured at equilibrium (L=3: 8+8+4+4+4, L=4: 2+2) = 32.
 N7  c_j(beta) = I_{2j}(beta) - I_{2j+2}(beta) equals 2(2j+1) I_{2j+1}(beta)/beta and is > 0
     for j in {0,1/2,...,5}, beta in {0.5,1,2,4,8}: relative difference < 1e-12
     (tolerance: double rounding of a convergent series of positive terms, about 50 ulp).
 N8  normalized fourth cumulant of chi^2_k equals 12/k; equals 4 at k=3 (exact rationals).
 N9  one SU(2) plaquette at Q=-1: the three horizontal eigenvalues 1-2b equal 1-2*0.5=0 at b=1/2
     (the threshold beta_W = 1/2): exact arithmetic.
 N10 z_SU2(6)/z_U1(6) = 8.02/0.684 equals 11.7 to 0.05.
 N11 F(4)-F(3) at beta=2.4: 2.81-1.55 = 1.26, error sqrt(0.95^2+0.45^2) = 1.05 to 0.005,
     ratio 1.2 to 0.05.
 N12 vortex: Z2 beta=0.6 values roughly ~ L^2: F/L^2 at L=2,3,4 all within [0.8,1.0]
     (source says "approx 1.0 L^2"; tolerance chosen by me, own expectation).
 N13 1/(2 beta) at beta = 2.3 equals 0.217 to 5e-4.
 N14 glueball mass in lattice units 3.74 a sqrt(sigma) equals 1.4, 1.0, 0.7 to 0.05 (MATCHED reading 2).
Exit code 0 iff all predicates are met; 1 otherwise.
"""
import math
import sys
from fractions import Fraction


def bessel_i(nu, x, terms=200):
    t = (x / 2) ** nu / math.gamma(nu + 1)   # k = 0 term; later terms by recurrence
    s = t
    for k in range(1, terms):
        t *= (x / 2) ** 2 / (k * (k + nu))
        s += t
    return s


def main():
    out = open(sys.argv[1], "x")
    res = []

    def pred(name, ok, msg):
        res.append(ok)
        line = f"{name}: {'MET' if ok else 'FAILED'}  {msg}"
        print(line)
        out.write(line + "\n")

    asig = [0.3690, 0.2660, 0.1905]
    R0 = [3.751e-2, 3.615e-2, 3.233e-2]
    R1 = [1.012e-2, 1.166e-2, 1.245e-2]
    q = [r1 / r0 for r1, r0 in zip(R1, R0)]
    xi = [1 / (3.74 * a) for a in asig]
    p = [x * (1 - qq) for x, qq in zip(xi, q)]
    pred("N1", all(abs(a - b) <= 5e-4 for a, b in zip(q, [0.270, 0.323, 0.385])), f"q={q}")
    pred("N2", all(abs(a - b) <= 5e-3 for a, b in zip(xi, [0.72, 1.01, 1.40])), f"xi={xi}")
    pred("N3", all(abs(a - b) <= 5e-3 for a, b in zip(p, [0.53, 0.68, 0.86])), f"xi(1-q)={p}")
    slope = math.log(p[2] / p[0]) / math.log(xi[2] / xi[0])
    pred("N4", abs(slope - 0.75) <= 0.05, f"slope={slope:.4f}")
    lows = [-2.2, -2.30, -1.88, -1.58, -1.79, -1.96, -1.52, -1.93, -2.04, -1.77, -1.67]
    highs = [-1.5, -1.17, -1.60, -1.53, -1.46, -1.39, -1.12, -1.12, -1.55, -1.26, -1.15]
    pred("N5", (min(lows), max(highs)) == (-2.30, -1.12), f"union=[{min(lows)}, {max(highs)}]")
    pred("N6", 8 + 8 + 4 + 4 + 4 + 2 + 2 == 32, "8+8+4+4+4+2+2")
    worst = 0.0
    allpos = True
    for twoj in range(0, 11):
        for b in [0.5, 1, 2, 4, 8]:
            lhs = bessel_i(twoj, b) - bessel_i(twoj + 2, b)
            rhs = 2 * (twoj + 1) * bessel_i(twoj + 1, b) / b
            worst = max(worst, abs(lhs - rhs) / abs(rhs))
            allpos = allpos and rhs > 0
    pred("N7", worst < 1e-12 and allpos, f"max rel diff={worst:.2e}, all positive={allpos}")
    ok8 = True
    for k in range(1, 8):
        k2 = Fraction(2 * k)       # variance of chi^2_k
        k4 = Fraction(48 * k)      # fourth cumulant of chi^2_k
        ok8 = ok8 and k4 / k2 ** 2 == Fraction(12, k)
    pred("N8", ok8 and Fraction(48 * 3) / Fraction(6) ** 2 == 4, "kappa4/kappa2^2 = 12/k, =4 at k=3")
    pred("N9", 1 - 2 * Fraction(1, 2) == 0, "1-2b at b=1/2 is 0")
    pred("N10", abs(8.02 / 0.684 - 11.7) <= 0.05, f"{8.02/0.684:.3f}")
    d = 2.81 - 1.55
    e = math.hypot(0.95, 0.45)
    pred("N11", abs(d - 1.26) < 1e-9 and abs(e - 1.05) <= 0.005 and abs(d / e - 1.2) <= 0.05,
         f"diff={d:.3f} err={e:.4f} ratio={d/e:.3f}")
    r = [3.205 / 4, 8.244 / 9, 15.84 / 16]
    pred("N12", all(0.8 <= x <= 1.0 for x in r), f"F/L^2={r}")
    pred("N13", abs(1 / (2 * 2.3) - 0.217) <= 5e-4, f"{1/4.6:.5f}")
    gm = [3.74 * a for a in asig]
    pred("N14", all(abs(a - b) <= 0.05 for a, b in zip(gm, [1.4, 1.0, 0.7])), f"m_G a={gm}")
    out.write(f"met {sum(res)} failed {len(res)-sum(res)}\n")
    out.close()
    sys.exit(0 if all(res) else 1)


if __name__ == "__main__":
    main()
