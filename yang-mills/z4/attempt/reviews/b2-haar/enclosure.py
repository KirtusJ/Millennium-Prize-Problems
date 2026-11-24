"""enclosure.py -- rational enclosure of R'(L), L = 6, 12 (claim (d)), plus grid sanity check of (a)-(c).

Method: I_nu(k) = sum_m t_m, t_m = x^(2m+nu)/(m!(m+nu)!), x = k/2 (DLMF 10.25.2).
Partial sum S over m = 0..32 (33 terms, as in the auditors' claim), tail bound
  0 < sum_{m>=33} t_m <= t_33 / (1 - r),  r = x^2/(34*(34+nu)),
valid because t_{m+1}/t_m = x^2/((m+1)(m+1+nu)) is decreasing in m, so all later
ratios are <= r < 1 (checked).  Then I1 in [S1, S1+T1], I2 in [S2, S2+T2],
R in [S2/(S1+T1), (S2+T2)/S1], and p = 1 - 3R/L - R^2 is decreasing in R > 0,
so p(L) in [p(R_hi), p(R_lo)]. All exact (fractions.Fraction); tolerance: none (exact).

PREDICATES (fixed before first run):
 E1 (L=6):  enclosure [lo,hi] lies inside (0.036885895, 0.036885896) (strict).
 E2 (L=12): enclosure [lo,hi] lies inside (0.009918625, 0.009918626) (strict).
 E3 r < 1 for both L and both nu (tail bound hypothesis), reported per case (4 cases).
 E4 width of each enclosure < 1e-12 (my expectation, so the claimed 9-digit bounds are decidable).
 E5 (grid sanity, measured as a predicate on a finite grid only, NOT a proof):
    on k = j/20, j = 1..800 (k in (0,40]), computed with Decimal prec 80 from
    termwise-differentiated series (independent of the Riccati identities, 400 terms):
    p - q < 0, p' < 0, w' > 0, p > 0 at every grid point; report counts.
    Tolerance: values are compared with 0 directly; Decimal prec 80 with 400 terms;
    truncation error of the series at k=40: t_400 ~ 20^800/(400!)^2 < 1e-300, negligible; the
    smallest |quantity| on the grid is printed so the reader can see the margin vs 1e-60.
Result file enclosure_result.txt opened with mode "x".
"""
from fractions import Fraction as F
from math import factorial
from decimal import Decimal as D, getcontext
import sys

out = []
def rec(name, ok, info=""):
    out.append(f"{name}: {'MET' if ok else 'FAILED'} {info}"); print(out[-1])

def partial_and_tail(k, nu, nterms=33):
    x = F(k, 2)
    t = lambda m: x ** (2 * m + nu) / (factorial(m) * factorial(m + nu))
    S = sum(t(m) for m in range(nterms))
    r = x * x / ((nterms + 1) * (nterms + 1 + nu))
    assert r < 1
    T = t(nterms) / (1 - r)
    return S, T, r

claims = {6: (F("0.036885895"), F("0.036885896")), 12: (F("0.009918625"), F("0.009918626"))}
rcases = []
for idx, L in enumerate([6, 12]):
    S1, T1, r1 = partial_and_tail(L, 1)
    S2, T2, r2 = partial_and_tail(L, 2)
    rcases += [(L, 1, r1), (L, 2, r2)]
    Rlo, Rhi = S2 / (S1 + T1), (S2 + T2) / S1
    p = lambda R: 1 - 3 * R / L - R * R
    lo, hi = p(Rhi), p(Rlo)
    c_lo, c_hi = claims[L]
    rec(f"E{idx+1} L={L} enclosure inside claim", c_lo < lo and hi < c_hi,
        f"lo={float(lo):.15f} hi={float(hi):.15f} width={float(hi-lo):.3e} tails T1={float(T1):.3e} T2={float(T2):.3e}")
    rec(f"E4 L={L} width<1e-12", hi - lo < F(1, 10**12), f"width={float(hi-lo):.3e}")
rec("E3 r<1 all cases", all(r < 1 for _, _, r in rcases),
    f"{sum(r<1 for _,_,r in rcases)}/4 qualify; " + ", ".join(f"L={L},nu={nu}: r={float(r):.4f}" for L, nu, r in rcases))

# grid sanity
getcontext().prec = 80
NT = 400
def bessel_derivs(k, nu):
    """returns I, I', I'', I''' at k via termwise differentiation (Decimal)."""
    x = k / 2
    vals = [D(0)] * 4
    for m in range(NT):
        e = 2 * m + nu
        c = D(1) / (D(2) ** e * D(factorial(m)) * D(factorial(m + nu)))
        # d^j/dk^j k^e = e(e-1)..(e-j+1) k^(e-j)
        f = D(1)
        for j in range(4):
            if e - j < 0: break
            vals[j] += c * f * k ** (e - j)
            f *= (e - j)
    return vals
cnt = {"p-q<0": 0, "p'<0": 0, "w'>0": 0, "p>0": 0}
mins = {key: None for key in cnt}
npts = 800
for j in range(1, npts + 1):
    k = D(j) / D(20)
    a0, a1, a2, _ = bessel_derivs(k, 1)   # I1 and derivatives
    b0, b1, b2, _ = bessel_derivs(k, 2)   # I2 and derivatives
    R = b0 / a0
    Rp = (b1 * a0 - b0 * a1) / a0 ** 2
    # R'' via quotient rule: (N/Dn)'' with N=b0, Dn=a0
    Npp = b2; Dpp = a2
    Rpp = (Npp * a0 - b0 * Dpp) / a0 ** 2 - 2 * a1 * (b1 * a0 - b0 * a1) / a0 ** 3
    p, q = Rp, R / k
    wprime = 2 * k * p + k * k * Rpp
    for key, val, good in [("p-q<0", q - p, p - q < 0), ("p'<0", -Rpp, Rpp < 0),
                           ("w'>0", wprime, wprime > 0), ("p>0", p, p > 0)]:
        if good: cnt[key] += 1
        if mins[key] is None or val < mins[key]: mins[key] = val
rec("E5 grid sanity (finite grid only)", all(v == npts for v in cnt.values()),
    f"{npts} points qualify (k>0); counts " + ", ".join(f"{a}:{b}/{npts}" for a, b in cnt.items())
    + "; min margins " + ", ".join(f"{a}:{float(b):.3e}" for a, b in mins.items()))
# high-precision values of p(6), p(12) from the Decimal series for comparison
for L in (6, 12):
    a0, a1, _, _ = bessel_derivs(D(L), 1); b0, b1, _, _ = bessel_derivs(D(L), 2)
    out.append(f"info: R'({L}) = {(b1*a0-b0*a1)/a0**2:.25f} (Decimal, 400 terms)"); print(out[-1])
with open("enclosure_result.txt", "x") as fh:
    fh.write("\n".join(out) + "\n")
sys.exit(0 if all(("MET" in o) or o.startswith("info") for o in out) else 1)
