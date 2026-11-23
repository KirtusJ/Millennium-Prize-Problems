"""SU(2) one-link heat density bound check.

p(theta) = sum_{n>=0} (n+1) exp(-s*lam_n) chi_n(theta), chi_n = sin((n+1)t)/sin(t).
Normalization A: lam_n = n(n+2)          (s*lam evaluated as n(n+2) at s=2kappa)
Normalization B: lam_n = n(n+2)/4        (spin j(j+1), n=2j)

Fixed choices (set before first run):
  grid: theta_k = k*pi/N, k=0..N, N=20000 (both endpoints included; endpoint
        characters use exact limits chi_n(0)=n+1, chi_n(pi)=(-1)^n (n+1)).
  truncation: include terms n=0..n_max, n_max = first n>=1 with
        (n+1)^2 exp(-lam_n) < 1e-30 (bound on |term| at any theta), plus that n.
  precision: mpmath mp.dps = 30.

Predicates (fixed before first run):
  P_a : for normalization A, 2/3 <= min_grid p and max_grid p <= 4/3.
  P_b : T := sum_{n>=1}(n+1)^2 e^{-n(n+2)} satisfies T <= 4/(e^3-4) and 4/(e^3-4) < 1/3.
  P_c : |integral_0^pi p(t) (2/pi) sin^2 t dt - 1| < 1e-12 (normalization A, mpmath.quad).
  P_d1: for normalization B, 2/3 <= min p and max p <= 4/3.
  P_d2: for normalization B, min p > 0.
Exit code: 0 if the computation completes (predicate outcomes are reported, not
encoded in the exit code). Results go to a new file; refuses to overwrite.
"""
import os
import sys
from mpmath import mp, mpf, exp, sin, pi, quad, nstr

mp.dps = 30
N = 20000
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_heat_bound_v1.txt")


def nmax_for(lam):
    n = 1
    while (n + 1) ** 2 * exp(-lam(n)) >= mpf("1e-30"):
        n += 1
    return n


def make_p(lam):
    nm = nmax_for(lam)
    w = [(n + 1) * exp(-lam(n)) for n in range(nm + 1)]

    def p(t, k=None):
        if k == 0:
            return sum(w[n] * (n + 1) for n in range(nm + 1))
        if k == N:
            return sum(w[n] * (-1) ** n * (n + 1) for n in range(nm + 1))
        st = sin(t)
        return sum(w[n] * sin((n + 1) * t) / st for n in range(nm + 1))

    return p, nm


def scan(p):
    vals = [(p(pi * k / N, k), k) for k in range(N + 1)]
    mn = min(vals)
    mx = max(vals)
    return mn, mx


def main():
    if os.path.exists(OUT):
        print("refusing to overwrite", OUT)
        sys.exit(3)
    lines = []
    lamA = lambda n: mpf(n * (n + 2))
    lamB = lambda n: mpf(n * (n + 2)) / 4

    pA, nmA = make_p(lamA)
    (mnA, kmnA), (mxA, kmxA) = scan(pA)
    Pa = mnA >= mpf(2) / 3 and mxA <= mpf(4) / 3
    lines.append(f"(a) norm A n(n+2): truncation n<= {nmA}; min p = {nstr(mnA,15)} at theta = {nstr(pi*kmnA/N,10)} (k={kmnA}); max p = {nstr(mxA,15)} at theta = {nstr(pi*kmxA/N,10)} (k={kmxA}); P_a = {Pa}")

    T = sum((n + 1) ** 2 * exp(-lamA(n)) for n in range(1, nmA + 1))
    bound = 4 / (exp(3) - 4)
    Pb = T <= bound and bound < mpf(1) / 3
    lines.append(f"(b) tail T = {nstr(T,15)}; 4/(e^3-4) = {nstr(bound,15)}; 1/3 = {nstr(mpf(1)/3,15)}; P_b = {Pb}")

    I = quad(lambda t: pA(t) * (2 / pi) * sin(t) ** 2, [0, pi / 2, pi])
    Pc = abs(I - 1) < mpf("1e-12")
    lines.append(f"(c) Haar integral = {nstr(I,20)}; |I-1| = {nstr(abs(I-1),5)}; P_c = {Pc}")

    pB, nmB = make_p(lamB)
    (mnB, kmnB), (mxB, kmxB) = scan(pB)
    Pd1 = mnB >= mpf(2) / 3 and mxB <= mpf(4) / 3
    Pd2 = mnB > 0
    lines.append(f"(d) norm B n(n+2)/4: truncation n<= {nmB}; min p = {nstr(mnB,15)} at theta = {nstr(pi*kmnB/N,10)} (k={kmnB}); max p = {nstr(mxB,15)} at theta = {nstr(pi*kmxB/N,10)} (k={kmxB}); P_d1 = {Pd1}; P_d2 = {Pd2}")

    txt = "\n".join(lines) + "\n"
    with open(OUT, "x", encoding="utf-8") as f:
        f.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
