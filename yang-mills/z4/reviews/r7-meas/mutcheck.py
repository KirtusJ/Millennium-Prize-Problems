"""Numerical status of the mutated statements (finite atom measures).
Predicates fixed before first run:
 P1 (a) with constant e holds on 2000 random atom sets (seed 7, E in [0,20], w in [0,1], tau in [0.05,5]),
    tolerance 1e-12 relative (double rounding; bound is sharp at an atom at 1/tau).
 P2 mutation e->2 is TRUE: same 2000 sets satisfy it (2<e makes the bound weaker).
 P3 mutation e->3 is FALSE: nu = delta_{1/tau}, tau=1 violates it (lhs e^-2 = 0.1353 > e^-1/3 = 0.1226).
 P4 (b) without support is FALSE: nu = delta_{-1}, tau=1: lhs e^2 = 7.389 > 4 e^-1 = 1.472.
 P5 (b) with support holds on the same 2000 sets (tolerance 1e-12 relative).
Writes mutcheck_result.txt; refuses to overwrite.
"""
import math, random, os, sys
out = "mutcheck_result.txt"
if os.path.exists(out): sys.exit("result exists, not overwriting")
random.seed(7); e = math.e
def C(ws, Es, t): return sum(w*math.exp(-t*E) for w, E in zip(ws, Es))
def lhs_a(ws, Es, tau): return sum(w*E*math.exp(-2*tau*E) for w, E in zip(ws, Es))
def lhs_b(ws, Es, tau): return sum(w*E*E*math.exp(-2*tau*E) for w, E in zip(ws, Es))
ok1 = ok2 = ok5 = 0; N = 2000
for _ in range(N):
    n = random.randint(1, 8); Es = [random.uniform(0, 20) for _ in range(n)]
    ws = [random.random() for _ in range(n)]; tau = random.uniform(0.05, 5)
    c = C(ws, Es, tau)
    ok1 += lhs_a(ws, Es, tau) <= c/(e*tau)*(1+1e-12)
    ok2 += lhs_a(ws, Es, tau) <= c/(2*tau)*(1+1e-12)
    ok5 += lhs_b(ws, Es, tau) <= 4*c/(e*e*tau*tau)*(1+1e-12)
l3, r3 = lhs_a([1], [1.0], 1.0), C([1], [1.0], 1.0)/3
l4, r4 = lhs_b([1], [-1.0], 1.0), 4*C([1], [-1.0], 1.0)/e**2
res = [f"P1 {'MET' if ok1==N else 'FAILED'} {ok1}/{N}", f"P2 {'MET' if ok2==N else 'FAILED'} {ok2}/{N}",
       f"P3 {'MET' if l3>r3 else 'FAILED'} lhs={l3:.6f} rhs={r3:.6f}",
       f"P4 {'MET' if l4>r4 else 'FAILED'} lhs={l4:.6f} rhs={r4:.6f}", f"P5 {'MET' if ok5==N else 'FAILED'} {ok5}/{N}"]
open(out, "w").write("\n".join(res)+"\n"); print("\n".join(res))
