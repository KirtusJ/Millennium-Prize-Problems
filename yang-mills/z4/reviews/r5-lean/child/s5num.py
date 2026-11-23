"""s5num.py -- numerical test of heat-kernel tail bounds (seed 12345).

Setup: finite atoms, w_i >= 0, E_i >= 0, C(t) = sum_i w_i exp(-t E_i), tau > 0.

Predicates (fixed BEFORE the first run):
 (a) A := sum w E exp(-2 tau E)      <= C(tau)/(e tau)
 (b) B := sum w E^2 exp(-2 tau E)    <= 4 C(tau)/(e^2 tau^2)
 (d) E0 > 0: D := sum_{E>E0} w exp(-2 tau E) <= exp(-tau E0) C(tau)
     (E0: one draw log-uniform in [1e-3,1e3], plus each positive atom energy)
 (e) hypotheses C(2tau) >= v > 0, C(tau) <= V, E0 = log(2V/v)/tau:
     F := sum_{E<=E0} w exp(-2 tau E) >= v/2

A predicate "LHS <= RHS" counts as MET iff LHS <= RHS*(1+TOL) + ABS,
(for (e): LHS >= RHS*(1-TOL) - ABS).
TOL = 1e-12. Source: float64 unit roundoff u = 2^-53 ~ 1.1e-16; each sum has
<= 20 terms, each term a few flops plus exp (error ~ a few ulp), so the
relative error of a sum of nonnegative terms is <= ~(n+5)u ~ 3e-15; 1e-12
leaves a ~300x margin. ABS = 1e-300 guards the case where both sides are 0
(e.g. all weights zero), so 0 <= 0 is met. Max ratio LHS/RHS is reported
over cases with RHS > 0 (for (e): RHS/LHS reported as ratio v/2 / F).
"""
import math, os, sys
import numpy as np

TOL = 1e-12
ABS = 1e-300
N = 2000
rng = np.random.default_rng(12345)
out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

stats = {k: dict(q=0, met=0, fail=0, maxr=0.0) for k in "abde"}
def rec(k, met, ratio):
    s = stats[k]; s["q"] += 1
    if met: s["met"] += 1
    else: s["fail"] += 1
    if ratio is not None and math.isfinite(ratio): s["maxr"] = max(s["maxr"], ratio)

e = math.e
for _ in range(N):
    n = int(rng.integers(1, 21))
    w = rng.uniform(0, 1, n); w[rng.uniform(size=n) < 0.15] = 0.0
    E = 10 ** rng.uniform(-3, 3, n); E[rng.uniform(size=n) < 0.15] = 0.0
    tau = 10 ** rng.uniform(-2, 2)
    Ct = float(np.sum(w * np.exp(-tau * E)))
    C2 = float(np.sum(w * np.exp(-2 * tau * E)))
    A = float(np.sum(w * E * np.exp(-2 * tau * E))); RA = Ct / (e * tau)
    rec("a", A <= RA * (1 + TOL) + ABS, A / RA if RA > 0 else None)
    B = float(np.sum(w * E**2 * np.exp(-2 * tau * E))); RB = 4 * Ct / (e**2 * tau**2)
    rec("b", B <= RB * (1 + TOL) + ABS, B / RB if RB > 0 else None)
    # (d): E0 log-uniform around atom scale; also try each atom energy as E0
    E0s = [10 ** rng.uniform(-3, 3)] + [x for x in E if x > 0]
    for E0 in E0s:
        D = float(np.sum((w * np.exp(-2 * tau * E))[E > E0])); RD = math.exp(-tau * E0) * Ct
        rec("d", D <= RD * (1 + TOL) + ABS, D / RD if RD > 0 else None)
    # (e)
    if C2 > 0:
        v = C2 * (1 - rng.uniform(0, 1))  # in (0, C2]
        V = Ct * rng.uniform(1, 3)
        if v > 0 and C2 >= v and Ct <= V:
            E0 = math.log(2 * V / v) / tau
            F = float(np.sum((w * np.exp(-2 * tau * E))[E <= E0]))
            rec("e", F >= (v / 2) * (1 - TOL) - ABS, (v / 2) / F if F > 0 else math.inf)

p("s5num results  seed=12345  N=%d  TOL=%g" % (N, TOL))
p("claim  qualifying  met  failed  max_ratio")
for k in "abde":
    s = stats[k]
    p("(%s)    %6d  %6d  %4d   %.15f" % (k, s["q"], s["met"], s["fail"], s["maxr"]))
p("note (d): qualifying = atom sets x E0 values (1 random + each positive atom energy)")
p("note (e): ratio = (v/2)/LHS; <=1 means met")

# maximisers via grid + golden refinement
def argmax(f, lo, hi):
    xs = np.linspace(lo, hi, 200001); i = int(np.argmax(f(xs)))
    a, b = xs[max(i-1,0)], xs[min(i+1,len(xs)-1)]
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        c, d = b - g*(b-a), a + g*(b-a)
        if f(c) > f(d): b = d
        else: a = c
    x = (a+b)/2; return x, float(f(x))
x1, m1 = argmax(lambda x: x*np.exp(-x), 0, 50)
x2, m2 = argmax(lambda x: x**2*np.exp(-x), 0, 50)
p("max x e^-x   at x=%.10f value=%.17g  e^-1 =%.17g  rel diff=%.3e" % (x1, m1, math.exp(-1), m1/math.exp(-1)-1))
p("max x^2e^-x  at x=%.10f value=%.17g  4e^-2=%.17g  rel diff=%.3e" % (x2, m2, 4*math.exp(-2), m2/(4*math.exp(-2))-1))
for tau in (0.01, 1.0, 37.0):
    E1 = 1/tau; ra = (E1*math.exp(-2*tau*E1)) / (math.exp(-tau*E1)/(e*tau))
    E2 = 2/tau; rb = (E2**2*math.exp(-2*tau*E2)) / (4*math.exp(-tau*E2)/(e**2*tau**2))
    p("sharpness tau=%g: (a) single atom E=1/tau ratio=%.17g ; (b) single atom E=2/tau ratio=%.17g" % (tau, ra, rb))

fails = sum(stats[k]["fail"] for k in "abde")
p("TOTAL FAILURES:", fails)
here = os.path.dirname(os.path.abspath(__file__))
fn = os.path.join(here, "results.txt"); i = 2
while os.path.exists(fn):
    fn = os.path.join(here, "results_%d.txt" % i); i += 1
with open(fn, "x", encoding="utf-8") as f: f.write("\n".join(out) + "\n")
print("wrote", fn)
sys.exit(1 if fails else 0)
