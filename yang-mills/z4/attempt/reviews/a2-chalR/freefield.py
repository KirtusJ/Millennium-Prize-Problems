"""freefield.py -- a2-chalR, item A7 (independent recomputation of the child's result).

Lattice free scalar field on Z^4, cosh w(p) = 1 + (m^2 + sum 4 sin^2(p_i/2))/2,
gap M = w(0), xi = 1/M, psi = phi(0):
  C(n) = int_{[-pi,pi]^3} d^3p/(2pi)^3 exp(-n w(p)) / (2 sinh w(p)).
Method (different from a uniform grid): octant symmetry, per axis composite Gauss-Legendre
with geometric breakpoints 0, 2m, 4m, 8m, ..., pi; G nodes per panel. Accuracy estimate:
difference between G=8 and G=12.
Second observable psi2 = phi(0)^2 - <phi^2>: connected correlation 2 C(n)^2.

PREDICATES (fixed before first run):
 Q0  continuum prediction Rc = 2 K1(1/2)/K1(1) computed two ways (my quadrature of
     int_1^inf sqrt(E^2-1) e^{-sE} dE vs closed-form K1 via integral representation
     K1(s) = int_0^inf e^{-s cosh u} cosh u du) agree to 1e-8 (quadrature tolerance).
 Q1  for each m in {0.4,0.2,0.1,0.05,0.025,0.0125}: |R(G=8)-R(G=12)|/R < 1e-6 (grid convergence).
 Q2  R(m) <= 10 for all m listed ((C) holds with D=10; 10 chosen by me as "bounded").
 Q3  |R(0.0125) - Rc| / Rc < 1e-2 (approach to the continuum value).
 Q4  my R agrees with the child's reported R to 1e-5 relative (child's numbers typed in below
     from child/out1.txt, out2.txt; their claimed grid accuracy ~1.5e-7).
 Q5  R2(m) = R(m)^2 <= 100 for all m (psi = phi^2 also satisfies (C)).
Result file results_freefield.txt opened with mode "x".
"""
import math
import numpy as np

out = open("/home/user/z4-workers/a2-chalR/results_freefield.txt", "x")
fails = []


def say(s):
    print(s)
    out.write(s + "\n")


def pred(name, ok, info=""):
    say(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    if not ok:
        fails.append(name)


def axis_nodes(m, G):
    bps = [0.0]
    b = 2 * m
    while b < math.pi:
        bps.append(b)
        b *= 2
    bps.append(math.pi)
    x, w = np.polynomial.legendre.leggauss(G)
    X, W = [], []
    for a, c in zip(bps[:-1], bps[1:]):
        X.append(0.5 * (c - a) * x + 0.5 * (c + a))
        W.append(0.5 * (c - a) * w)
    return np.concatenate(X), np.concatenate(W)


def Cpair(m, ts, G):
    p, w = axis_nodes(m, G)
    s = 4 * np.sin(p / 2) ** 2
    q = s[:, None, None] + s[None, :, None] + s[None, None, :]
    W = w[:, None, None] * w[None, :, None] * w[None, None, :]
    om = np.arccosh(1 + (m * m + q) / 2)
    base = W / (2 * np.sinh(om)) / math.pi ** 3  # 8 octants * (1/(2pi)^3) = 1/pi^3
    return [float(np.sum(base * np.exp(-t * om))) for t in ts]


# continuum
def lap(s, n=2000000):
    u = (np.arange(n) + 0.5) / n
    E = 1 + 200 * u ** 2
    dE = 400 * u / n
    return float(np.sum(np.sqrt(E * E - 1) * np.exp(-s * E) * dE))


def K1(s, n=2000000):
    u = 30 * (np.arange(n) + 0.5) / n
    return float(np.sum(np.exp(-s * np.cosh(u)) * np.cosh(u)) * 30 / n)


Rc1 = lap(0.5) / lap(1.0)
Rc2 = 2 * K1(0.5) / K1(1.0)
pred("Q0", abs(Rc1 / Rc2 - 1) < 1e-8, f"Rc quad={Rc1:.9f} Rc K1={Rc2:.9f}")
Rc = Rc2
child = {0.4: 5.469064236, 0.2: 6.513378226, 0.1: 5.738552049, 0.05: 5.550620018,
         0.025: 5.515154247, 0.0125: 5.506742716}
q1 = q2 = q4 = q5 = True
R = {}
for m in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
    M = math.acosh(1 + m * m / 2)
    xi = 1 / M
    a = Cpair(m, [xi / 2, xi], 8)
    b = Cpair(m, [xi / 2, xi], 12)
    r8, r12 = a[0] / a[1], b[0] / b[1]
    R[m] = r12
    d = abs(r8 - r12) / r12
    say(f"m={m} xi={xi:.5f} C(xi/2)={b[0]:.6e} C(xi)={b[1]:.6e} R={r12:.9f} gridrel={d:.1e} R2={r12**2:.6f} child={child[m]} rel={abs(r12/child[m]-1):.1e}")
    q1 &= d < 1e-6
    q2 &= r12 <= 10
    q4 &= abs(r12 / child[m] - 1) < 1e-5
    q5 &= r12 ** 2 <= 100
pred("Q1", q1)
pred("Q2", q2, f"max R={max(R.values()):.6f}")
pred("Q3", abs(R[0.0125] - Rc) / Rc < 1e-2, f"R(0.0125)={R[0.0125]:.6f} Rc={Rc:.6f}")
pred("Q4", q4)
pred("Q5", q5)
say(f"FAILED PREDICATES: {fails}")
out.close()
