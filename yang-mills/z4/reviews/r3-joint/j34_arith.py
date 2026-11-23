"""Constant chains of README (J1), finite-volume-vacuum (J3), evolution (J4). Exact rationals / mpmath.

Predicates (fixed before first run):
 A1 J1 chain: 2a+3a+4a = 9a; with ac<=1/36, E<=c: 9a(c+E)<=1/2, |mu-E|<=9a*(2*2c)*(2c)=72ac^2,
    mu<=3c => a mu<=1/12, 72+2*9 = 90, gap 180.  Worst case over a grid of (ac, E/c, mu-side) done
    by evaluating the scalar inequalities at 2000 random points (seed 20261122). met/failed.
 A2 step-1 constant: (e^{aB}-1)/c <= 2a for B<=c, ac<=1 (grid, seed fixed). met/failed.
 A3 step-2: aB^2 + ac*2B <= 3ac^2 for B<=c. met/failed.
 A4 J3 schedule: a c <= 2^-n-8/4 and a c^2/d <= 2^-n-8 for random (t0,c,d,n) (seed fixed). met/failed.
 A5 J3: 72*2^-9 < 1 so that 9a <= rho/2 follows (needs 72ac^2/Delta <= 1). met/failed.
 A6 J3 two-state example: P=[[15/16,1/16],[1/16,15/16]], q uniform: eps = min P/q = 1/8, second
    eigenvalue 7/8 = 1-eps. met/failed.
 A7 J4: (2+2s)^2 <= 8(1+s^2); time-change constants 2/(1-1/12) <= 3 and 2*3/(1-1/12) <= 7. met/failed.
 A8 J4 implicit Euler scalar: sup_x ((1+x/k)^-k - e^-x) <= 2/k for k=1..60 (dense x grid). met/failed.
Tolerance: 1e-12 relative slack for float evaluations (double rounding); rationals exact.
"""
import sys, os, json, random, math
from fractions import Fraction as F

random.seed(20261122)
out = sys.argv[1]
if os.path.exists(out):
    print('refuse'); sys.exit(3)
R = {}
ok = True
for _ in range(2000):
    ac = random.uniform(1e-6, 1/36); c = 10 ** random.uniform(-3, 3); a = ac / c
    E = random.uniform(0, c)
    ok &= 9 * a * (c + E) <= 0.5 + 1e-12
    # worst mu allowed by |1/(c+mu)-1/(c+E)|<=9a on the high side
    inv = 1 / (c + E) - 9 * a
    mu = 1 / inv - c
    ok &= abs(mu - E) <= 72 * a * c * c * (1 + 1e-12) and mu <= 3 * c * (1 + 1e-12)
    ok &= a * mu <= 1 / 12 + 1e-12
    e = -math.log(1 - a * mu) / a
    ok &= abs(e - E) <= 90 * a * c * c * (1 + 1e-9)
R['A1'] = bool(ok)
ok = True
for _ in range(2000):
    c = 10 ** random.uniform(-3, 3); a = random.uniform(0, 1) / c; B = random.uniform(0, c)
    ok &= (math.expm1(a * B)) / c <= 2 * a * (1 + 1e-12)
R['A2'] = bool(ok)
ok = True
for _ in range(2000):
    c = 10 ** random.uniform(-3, 3); a = random.uniform(0, 1) / c; B = random.uniform(0, c)
    ok &= a * B * B + a * c * 2 * B <= 3 * a * c * c * (1 + 1e-12)
R['A3'] = bool(ok)
ok = True
for _ in range(2000):
    t0 = 10 ** random.uniform(-3, 3); c = 10 ** random.uniform(-3, 6); d = 10 ** random.uniform(-300, 2); n = random.randint(1, 40)
    a = t0 * 2.0 ** (-n - 8) / ((1 + t0 * c) ** 2 * (1 + 1 / (t0 * d)))
    ok &= a * c <= 2.0 ** (-n - 8) / 4 * (1 + 1e-12) and a * c * c / d <= 2.0 ** (-n - 8) * (1 + 1e-12)
R['A4'] = bool(ok)
R['A5'] = F(72, 2 ** 9) < 1
P = [[F(15, 16), F(1, 16)], [F(1, 16), F(15, 16)]]
eps = min(P[i][j] / F(1, 2) for i in range(2) for j in range(2))
lam2 = P[0][0] - P[0][1]
R['A6'] = (eps == F(1, 8) and lam2 == 1 - eps)
ok = all((2 + 2 * s) ** 2 <= 8 * (1 + s * s) + 1e-12 for s in [i / 100 for i in range(0, 10000)])
ok &= F(2) / (1 - F(1, 12)) <= 3 and F(2 * 3) / (1 - F(1, 12)) <= 7
R['A7'] = bool(ok)
ok = True; worst = 0
for k in range(1, 61):
    m = max((1 + x / k) ** -k - math.exp(-x) for x in [i / 200 for i in range(0, 200 * 60)])
    worst = max(worst, m * k)
    ok &= m <= 2 / k + 1e-12
R['A8'] = bool(ok); R['A8_max_k_times_err'] = worst
with open(out, 'x') as f:
    json.dump(R, f, indent=1)
print(R)
sys.exit(0 if all(v for k, v in R.items() if k.startswith('A') and isinstance(v, bool)) else 1)
