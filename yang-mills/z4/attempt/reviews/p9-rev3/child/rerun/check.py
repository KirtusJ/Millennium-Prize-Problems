"""Periodic time lattice Z/NZ toy check. Predicates stated BEFORE running:
(a) N=2: theta (s -> -s mod 2) is the identity on slices: expected 0->0, 1->1  => True.
(b) theta tau = tau^{-1} theta on 200 random polynomials F at random U, |diff|<=1e-9.
    Expected True for every N (N=2 and N=6): both sides evaluate F at the same
    permuted argument, V_s = U_{-(s+1) mod N}. Tolerance 1e-9 only covers float
    roundoff (expected diff is exactly 0 since only argument permutation, no arithmetic
    difference; polynomial evaluation order is identical).
(c) N=2: tau^2 is the identity (V_s=U_{s+2 mod 2}=U_s) => True.
Fixed seed 12345. Results written with open mode 'x' (never overwrites).
Run: python3 check.py
"""
import random
SEED = 12345
TOL = 1e-9

def make_poly(rng, N, nterms=5, maxdeg=3):
    terms = []
    for _ in range(nterms):
        c = rng.uniform(-2, 2)
        exps = [rng.randint(0, maxdeg) for _ in range(N)]
        terms.append((c, exps))
    def F(U):
        t = 0.0
        for c, e in terms:
            p = c
            for i, k in enumerate(e):
                p *= U[i] ** k
            t += p
        return t
    return F

def tau(F, N):      # (tau F)(U) = F(V), V_s = U_{s+1}
    return lambda U: F([U[(s + 1) % N] for s in range(N)])
def tauinv(F, N):   # V_s = U_{s-1}
    return lambda U: F([U[(s - 1) % N] for s in range(N)])
def theta(F, N):    # W_s = U_{-s}
    return lambda U: F([U[(-s) % N] for s in range(N)])

def check_b(N, rng):
    worst = 0.0
    for _ in range(200):
        F = make_poly(rng, N)
        U = [rng.uniform(-1.5, 1.5) for _ in range(N)]
        lhs = theta(tau(F, N), N)(U) if False else None
        # (theta tau F) = theta applied to (tau F)
        lhs = theta(tau(F, N), N)(U)
        rhs = tauinv(theta(F, N), N)(U)
        worst = max(worst, abs(lhs - rhs))
    return worst <= TOL, worst

def check_c(rng):
    N = 2
    worst = 0.0
    for _ in range(200):
        F = make_poly(rng, N)
        U = [rng.uniform(-1.5, 1.5) for _ in range(N)]
        worst = max(worst, abs(tau(tau(F, N), N)(U) - F(U)))
    return worst <= TOL, worst

rng = random.Random(SEED)
out = []
m = {s: (-s) % 2 for s in range(2)}
out.append(f"(a) N=2 theta map on slices: {m}; identity: {all(k == v for k, v in m.items())}")
ok, w = check_b(2, rng)
out.append(f"(b) N=2 theta tau = tau^-1 theta, 200 polys: {ok}, max|diff|={w:.3g}, tol={TOL}")
ok, w = check_c(rng)
out.append(f"(c) N=2 tau^2 = identity (200 polys, also slice map s->s+2 mod 2 = {[(s+2)%2 for s in range(2)]}): {ok}, max|diff|={w:.3g}")
ok, w = check_b(6, rng)
out.append(f"(b') N=6 theta tau = tau^-1 theta, 200 polys: {ok}, max|diff|={w:.3g}, tol={TOL}")
txt = "\n".join(out) + "\n"
print(txt)
with open("results.txt", "x") as f:
    f.write(txt)
