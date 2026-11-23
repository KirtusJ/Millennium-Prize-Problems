"""Z4 challenger r6-heat: arithmetic checks of B4's stated constants. Deterministic (no randomness).

Predicates fixed BEFORE first run (source of each tolerance in brackets):
 P1 [README l.35-38] For x>=1 and m=2*ceil(x^(1/5)): m^2<=16 x^(2/5) and (m/2)^3>=x^(3/5).
    Grid: x = 10^(k/10), k=0..600. Exact inequality, float tolerance 1e-9 relative [double rounding].
 P2 [README l.31-37] 2^(5/2)[2^-((m/2)^3) + exp(-x/(2(5m^2+65536B)))] <= 2^(7/2) exp(-c min(x^(3/5), x/B)),
    c=1/132000, on grid x as P1 and B = 10^(j/4), j=0..40 (B in [1,1e10]). Compared in logs, tol 1e-9.
 P3 [wilson-law l.7-9] 3*pi^3*e^(1/2)/8 < 20 ; 20/8^3 < 1/16 ; 2^n*16^(-ceil(n/2)) <= 2^-n for n=1..200.
 P4 [wilson-law l.17-21] (64+48 r^2) <= 256 for r^2<=4 ; 256*64 = 16384 ; 2*2*16384 = 65536 (good-site
    algebra: total <= m^2 E + 2(2*16384 B E + 2 m^2 E) = (5m^2 + 65536 B)E).
 P5 [wilson-law l.24] free-boundary path: 2-2cos(pi/m) >= 4/m^2 for m=2..10^4 (exact inequality).
 P6 [wilson-law l.35-41] p_t(0)=[I0-type integral]^3 <= b^3 t^-3/2: check 1D factor
    (1/2pi)int e^{-2tau(1-cos k)}dk <= sqrt(pi)/(4 sqrt(tau)) for tau=t/b^2 in [0.5, 1e4] (quadrature
    tol 1e-10 [trapezoid on periodic analytic integrand is spectrally accurate]); and sqrt(pi)/4 <= 1.
 P7 [rare-cubes l.11-13] 6(1-cos(pi/(m+1))) <= 3 pi^2/m^2 for m=1..10^4.
 P8 [rare-cubes l.19] with m in [u/2,u], u=(x/L)^(1/5): x/m^2 + m^3 L <= 5 x^(3/5) L^(2/5) (exact algebra),
    checked on grid x as P1, L in {1,10,100}, requiring m>=1 (u>=2).
 P9 [hamiltonian l.20,26] 24*2^(3/2)/e <= 72 and 72/2 = 36 (gamma=1/(2 beta b) times 72 d^2 V b/s^2).
 Measured only (no pass/fail):
 M1 On beta = c0*log(1/b), c0=1, s=1, isotropic B=1+6beta: window for log(-log E F_s)/log x implied by
    the stated bounds, lower end log(c*x^(3/5) - log(2^(7/2)*V)) / log x with V=1, upper end
    log(5*C_L * x^(3/5) L^(2/5))/log x with L=B+log(2+x) and an unknown C_L set to 1 (the notes' C is unspecified).
 M2 Spectral threshold of positive-time.md in physical units, a=b: R_b = x^eta/a, for eta=0.3, 0.59, as b->0,
    and R_b*a (threshold in units of the cutoff 1/a).
"""
import math, sys, os

fails, met, measured = [], [], []
def pred(name, ok, info=""):
    (met if ok else fails).append(name + (": " + info if info else ""))

xs = [10 ** (k / 10) for k in range(0, 601)]
# P1
ok = True
for x in xs:
    m = 2 * math.ceil(x ** 0.2)
    if not (m * m <= 16 * x ** 0.4 * (1 + 1e-9) and (m / 2) ** 3 >= x ** 0.6 * (1 - 1e-9)):
        ok = False; bad = x; break
pred("P1", ok, "" if ok else f"x={bad}")
# P2
c = 1 / 132000
ok = True; worst = -1e300
for x in xs:
    m = 2 * math.ceil(x ** 0.2)
    for j in range(41):
        B = 10 ** (j / 4)
        t1 = -((m / 2) ** 3) * math.log(2)
        t2 = -x / (2 * (5 * m * m + 65536 * B))
        hi = max(t1, t2)
        lhs = 2.5 * math.log(2) + hi + math.log(math.exp(t1 - hi) + math.exp(t2 - hi))
        rhs = 3.5 * math.log(2) - c * min(x ** 0.6, x / B)
        worst = max(worst, lhs - rhs)
        if lhs > rhs + 1e-9 * max(1, abs(rhs)):
            ok = False
pred("P2", ok, f"max(log lhs - log rhs)={worst:.3e}")
# P3
pred("P3a", 3 * math.pi ** 3 * math.e ** 0.5 / 8 < 20, f"{3*math.pi**3*math.e**0.5/8:.4f}")
pred("P3b", 20 / 512 < 1 / 16)
pred("P3c", all(n * math.log(2) - math.ceil(n / 2) * math.log(16) <= -n * math.log(2) + 1e-12 for n in range(1, 201)))
# P4
pred("P4", 64 + 48 * 4 <= 256 and 256 * 64 == 16384 and 4 * 16384 == 65536)
# P5
pred("P5", all(2 - 2 * math.cos(math.pi / m) >= 4 / m ** 2 for m in range(2, 10001)))
# P6
def oned(tau, N=4096):
    s = 0.0
    for i in range(N):
        k = -math.pi + 2 * math.pi * i / N
        s += math.exp(-2 * tau * (1 - math.cos(k)))
    return s / N
ok = True; worst = 0
for tau in [0.5, 1, 2, 5, 10, 100, 1000, 10000]:
    v = oned(tau); bnd = math.sqrt(math.pi) / (4 * math.sqrt(tau))
    worst = max(worst, v / bnd)
    if v > bnd + 1e-10: ok = False
pred("P6", ok and math.sqrt(math.pi) / 4 <= 1, f"max ratio integral/bound={worst:.4f}")
# P7
pred("P7", all(6 * (1 - math.cos(math.pi / (m + 1))) <= 3 * math.pi ** 2 / m ** 2 for m in range(1, 10001)))
# P8
ok = True
for x in xs:
    for L in (1, 10, 100):
        u = (x / L) ** 0.2
        if u < 2: continue
        for m in (math.floor(u), u / 2, u):
            if m < u / 2 - 1e-12: continue
            if x / m ** 2 + m ** 3 * L > 5 * x ** 0.6 * L ** 0.4 * (1 + 1e-9):
                ok = False
pred("P8", ok)
# P9
pred("P9", 24 * 2 ** 1.5 / math.e <= 72, f"{24*2**1.5/math.e:.3f}")

out = []
out.append("M1 window for log(-log EF)/log x on beta=log(1/b), s=V=1, isotropic (lower end from upper bound on EF)")
out.append(" b        x          lowerEnd   upperEnd(C=1)")
for e in [1, 2, 3, 6, 10, 20, 50, 100, 150]:
    lb = -e * math.log(10)  # log b
    logx = -2 * lb
    x = math.exp(logx) if logx < 700 else None
    B = 1 + 6 * (-lb)
    if x is None:
        # work in logs: c x^(3/5) dominates
        lo = (math.log(c) + 0.6 * logx) / logx
    else:
        v = c * min(x ** 0.6, x / B) - math.log(2 ** 3.5)
        lo = math.log(v) / logx if v > 0 else float('nan')
    L = B + math.log(2) + logx
    up = (math.log(5) + 0.6 * logx + 0.4 * math.log(L)) / logx
    out.append(f" 1e-{e:<4d} e^{logx:8.1f}  {lo:9.4f}  {up:9.4f}")
measured.append("M1")
out.append("M2 spectral threshold R=x^eta/a, a=b, s=1")
for eta in (0.3, 0.59):
    for e in (2, 4, 8):
        b = 10 ** -e; x = 1 / b ** 2
        out.append(f" eta={eta} b=1e-{e}: R={x**eta/b:.3e} (phys units 1/length), R*a={x**eta:.3e}")
measured.append("M2")

n = 1
while os.path.exists(f"results_constants_{n}.txt"): n += 1
with open(f"results_constants_{n}.txt", "x") as f:
    f.write("met:\n" + "\n".join(met) + "\nfailed:\n" + "\n".join(fails) + "\nmeasured:\n" + "\n".join(out) + "\n")
print(open(f"results_constants_{n}.txt").read())
print(f"met={len(met)} failed={len(fails)} measured={len(measured)}")
sys.exit(1 if fails else 0)
