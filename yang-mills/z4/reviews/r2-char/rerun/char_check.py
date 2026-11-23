"""char_check.py -- characters of G = Z_2 x Z_4 diagonalise the convolution cube T^3.

Predicates (fixed BEFORE the first run):
  H : exactly 8 characters psi_{k,l}, k in 0..1, l in 0..3; each multiplicative
      psi(g+h) = psi(g) psi(h) on all 64 pairs (|diff| <= TOL_UNIT); pairwise distinct
      (max_g |psi - phi| > 0.5; distinct characters differ by >= sqrt(2) somewhere).
      Report count qualifying (must be 8).
  P1: for each psi, ||T^3 psi - c_psi^3 psi||_inf <= TOL_BIG.
  P2: |Im c_psi| <= TOL_SMALL and |c_psi - sum_y w(y) Re psi(y)| <= TOL_SMALL.
  P3: sorted eigenvalues of T^3 (own Jacobi solver; T^3 is real symmetric since w is even)
      match sorted Re(c_psi^3) entrywise within TOL_EIG.
  P4: T^3 (matrix power) equals the explicit kernel
      K3[x][z] = sum_{g1,g2} w(g1) w(g2-g1) w(x-z-g2), entrywise within TOL_BIG.
Tolerances (no numpy available -> pure Python doubles, eps = 2.22e-16):
  TOL_UNIT  = 1e-12 : products of two unit complex numbers from cmath.exp, error ~ few eps.
  TOL_SMALL = 1e-12 * S1, S1 = sum|w| <= 12 : sums of 8 terms of size <= 1.5, error ~ 8 eps * S1.
  TOL_BIG   = 1e-10 * S1^3 : triple sums of <= 512 products, error ~ 512 * 3 eps * S1^3 ~ 3e-13 S1^3;
              1e-10 leaves ~300x headroom.
  TOL_EIG   = 1e-9 * S1^3 : Jacobi stopped at off-diagonal Frobenius <= 1e-15 * ||A||_F, eigenvalue
              error bounded by that plus rotation round-off (~ n^2 eps ||A||).
Seed: random.seed(20261122). Exit 0 iff H, P1..P4 all hold.
"""
import cmath, math, os, random, sys

random.seed(20261122)
G = [(a, b) for a in range(2) for b in range(4)]
idx = {g: i for i, g in enumerate(G)}
add = lambda g, h: ((g[0] + h[0]) % 2, (g[1] + h[1]) % 4)
neg = lambda g: ((-g[0]) % 2, (-g[1]) % 4)
sub = lambda g, h: add(g, neg(h))

w = {}
for g in G:
    if g not in w:
        w[g] = random.uniform(0.5, 1.5)
        w[neg(g)] = w[g]
assert all(w[g] == w[neg(g)] for g in G)

S1 = sum(abs(v) for v in w.values())
TOL_UNIT, TOL_SMALL, TOL_BIG, TOL_EIG = 1e-12, 1e-12 * S1, 1e-10 * S1 ** 3, 1e-9 * S1 ** 3

n = 8
T = [[w[sub(x, z)] for z in G] for x in G]
def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
T3 = matmul(matmul(T, T), T)

def psi_fn(k, l):
    return lambda g: cmath.exp(2j * math.pi * (k * g[0] / 2 + l * g[1] / 4))
chars = [((k, l), psi_fn(k, l)) for k in range(2) for l in range(4)]

out = []
log = out.append
log(f"seed 20261122; w = {[round(w[g], 6) for g in G]}; S1 = {S1:.6f}")
log(f"tolerances: UNIT {TOL_UNIT:.1e} SMALL {TOL_SMALL:.2e} BIG {TOL_BIG:.2e} EIG {TOL_EIG:.2e}")

# H
mult_ok = []
worst_mult = 0.0
for _, p in chars:
    e = max(abs(p(add(g, h)) - p(g) * p(h)) for g in G for h in G)
    worst_mult = max(worst_mult, e)
    mult_ok.append(e <= TOL_UNIT)
min_sep = min(max(abs(chars[i][1](g) - chars[j][1](g)) for g in G)
              for i in range(n) for j in range(i + 1, n))
distinct = min_sep > 0.5
count = sum(mult_ok) if distinct else 0
H = len(chars) == 8 and count == 8 and distinct
log(f"H : {len(chars)} characters, {count} qualifying, worst mult err {worst_mult:.2e}, min sep {min_sep:.4f} -> {'PASS' if H else 'FAIL'}")

# P1, P2
cs = []
p1w = p2w = 0.0
for (kl, p) in chars:
    c = sum(w[y] * p(neg(y)) for y in G)
    cs.append(c)
    v = [p(g) for g in G]
    Tv = [sum(T3[i][j] * v[j] for j in range(n)) for i in range(n)]
    p1w = max(p1w, max(abs(Tv[i] - c ** 3 * v[i]) for i in range(n)))
    cre = sum(w[y] * p(y).real for y in G)
    p2w = max(p2w, abs(c.imag), abs(c - cre))
P1 = p1w <= TOL_BIG
P2 = p2w <= TOL_SMALL
log(f"P1: max ||T^3 psi - c^3 psi||_inf = {p1w:.2e} -> {'PASS' if P1 else 'FAIL'}")
log(f"P2: max(|Im c|, |c - sum w Re psi|) = {p2w:.2e} -> {'PASS' if P2 else 'FAIL'}")
log("    c_psi = " + ", ".join(f"{kl}:{c.real:.6f}" for (kl, _), c in zip(chars, cs)))

# P3: cyclic Jacobi on symmetric T3
def jacobi(A):
    A = [row[:] for row in A]
    fro = math.sqrt(sum(x * x for r in A for x in r))
    for _ in range(100):
        off = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off <= 1e-15 * fro:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                th = (A[q][q] - A[p][p]) / (2 * A[p][q])
                t = (1 if th >= 0 else -1) / (abs(th) + math.sqrt(th * th + 1))
                c = 1 / math.sqrt(t * t + 1); s = t * c
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p], A[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k], A[q][k] = c * apk - s * aqk, s * apk + c * aqk
    return sorted(A[i][i] for i in range(n)), off
sym_err = max(abs(T3[i][j] - T3[j][i]) for i in range(n) for j in range(n))
ev, off = jacobi(T3)
pred = sorted((c ** 3).real for c in cs)
p3w = max(abs(a - b) for a, b in zip(ev, pred))
P3 = p3w <= TOL_EIG and sym_err <= TOL_BIG
log(f"P3: asymmetry {sym_err:.2e}, Jacobi off {off:.2e}, max |eig - c^3| = {p3w:.2e} -> {'PASS' if P3 else 'FAIL'}")
log("    eig(T^3) = " + ", ".join(f"{e:.6f}" for e in ev))

# P4
p4w = 0.0
for x in G:
    for z in G:
        k3 = sum(w[g1] * w[sub(g2, g1)] * w[sub(sub(x, z), g2)] for g1 in G for g2 in G)
        p4w = max(p4w, abs(k3 - T3[idx[x]][idx[z]]))
P4 = p4w <= TOL_BIG
log(f"P4: max |K3 - T^3| = {p4w:.2e} -> {'PASS' if P4 else 'FAIL'}")

ok = H and P1 and P2 and P3 and P4
log(f"ALL: {'PASS' if ok else 'FAIL'}")
k = 1
while os.path.exists(f"results_{k}.txt"):
    k += 1
fn = f"results_{k}.txt"
with open(fn, "x", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out)); print(f"written {fn}")
sys.exit(0 if ok else 1)
