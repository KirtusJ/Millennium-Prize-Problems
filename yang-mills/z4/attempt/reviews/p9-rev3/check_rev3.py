"""check_rev3.py -- index/support checks behind revision 3 edits (p9-rev3).

Predicates fixed before the first run:
 P1 (chess, for all k in {2,3,4,5}, all i in 0..k-1): with r = -2^i+1 and
    S_i = {t_1 in [-2^i+1, 0]} (mod L=2^k), (a) S_i subset H_+ = {r <= t_1 <= r+L/2-1} (mod L);
    (b) theta_r S_i := {2r-1-t_1} equals {t_1 in [-2^{i+1}+1, -2^i]} mod L;
    (c) theta_r S_i is disjoint from S_i; (d) after k steps the union is all of Z/LZ.
 P2 (chess, for all k in {2..5}, all r in Z/L, all t_j): the map vartheta_t composed with
    theta_r equals vartheta_{t'} as maps of sites mod L, with t'_j = 2r-1-t_j (exact integer check).
 P3 (tau, corrected convention, N in {4,6,8}, toy one variable per time slice):
    for all single-slice supports s in {0..N/2-1}: supp(tau F) = s+1 in A_+ = {0..N/2};
    old convention sends s=0 to N-1 (outside A_+) -- expected True (defect of printed text).
 P4 (tau): theta tau = tau^{-1} theta on 200 random polynomial F at 50 random U each
    (seed 20261123), N in {4,6,8}; tolerance 1e-12 (float64 rounding of products of O(1) numbers,
    a few ulps times number of terms).
 P5 (tau): tau^n of the slice-0 observable equals the slice-n observable for n=1..N-1.
Exit 0 iff all predicates hold.
"""
import random, sys, itertools

res = {}
fails = []

# P1
ok1 = True; cases1 = 0
for k in range(2, 6):
    L = 2 ** k
    S = {0}
    for i in range(k):
        r = -2 ** i + 1
        cases1 += 1
        expS = {x % L for x in range(-2 ** i + 1, 1)}
        a = S == expS and all(((t - r) % L) <= L // 2 - 1 for t in S)
        img = {(2 * r - 1 - t) % L for t in S}
        b = img == {x % L for x in range(-2 ** (i + 1) + 1, -2 ** i + 1)}
        c = not (img & S)
        if not (a and b and c):
            ok1 = False; fails.append(("P1", k, i, a, b, c))
        S = S | img
    if S != set(range(L)):
        ok1 = False; fails.append(("P1d", k))
res["P1"] = (ok1, cases1)

# P2: 1-d site maps
def vt(t, x, L):
    return (x + t) % L if t % 2 == 0 else (t + 1 - x) % L
ok2 = True; cases2 = 0
for k in range(2, 6):
    L = 2 ** k
    for r in range(L):
        for t in range(L):
            tp = (2 * r - 1 - t) % L
            cases2 += 1
            if any((2 * r - vt(t, x, L)) % L != vt(tp, x, L) for x in range(L)):
                ok2 = False; fails.append(("P2", k, r, t))
res["P2"] = (ok2, cases2)

# P3-P5: toy configuration U = (U_0..U_{N-1})
rng = random.Random(20261123)
ok3 = ok4 = ok5 = True; c3 = c4 = c5 = 0
for N in (4, 6, 8):
    shift_fwd = lambda U, n=1: [U[(s + n) % N] for s in range(N)]   # (U_{.+n e0})_s = U_{s+n}
    shift_bwd = lambda U: [U[(s - 1) % N] for s in range(N)]
    refl = lambda U: [U[(-s) % N] for s in range(N)]
    for s in range(N // 2):
        c3 += 1
        U = [0.0] * N; U[s] = 1.0
        F = lambda V, s=s: V[s]
        new = [j for j in range(N) if F(shift_fwd([1.0 if q == j else 0.0 for q in range(N)])) != 0]
        old = [j for j in range(N) if F(shift_bwd([1.0 if q == j else 0.0 for q in range(N)])) != 0]
        if new != [s + 1] or not (s + 1 <= N // 2):
            ok3 = False; fails.append(("P3new", N, s, new))
        if s == 0 and old != [N - 1]:
            ok3 = False; fails.append(("P3old", N, old))
    for _ in range(200):
        terms = [(rng.uniform(-1, 1), tuple(rng.randrange(N) for _ in range(rng.randint(1, 3)))) for _ in range(4)]
        F = lambda V, terms=terms: sum(c * __import__("math").prod(V[j] for j in idx) for c, idx in terms)
        for _ in range(50):
            U = [rng.uniform(-1, 1) for _ in range(N)]
            c4 += 1
            lhs = F(shift_fwd(refl(U)))          # theta(tau F)(U) = (tau F)(theta^*U) = F((theta^*U)_{.+e0})
            rhs = F(refl(shift_bwd(U)))          # tau^{-1}(theta F)(U) = (theta F)(U_{.-e0}) = F(theta^*(U_{.-e0}))
            if abs(lhs - rhs) > 1e-12:
                ok4 = False; fails.append(("P4", N, lhs, rhs))
    for n in range(1, N):
        c5 += 1
        U = [rng.uniform(-1, 1) for _ in range(N)]
        if shift_fwd(U, n)[0] != U[n]:
            ok5 = False; fails.append(("P5", N, n))
res["P3"] = (ok3, c3); res["P4"] = (ok4, c4); res["P5"] = (ok5, c5)

with open("check_rev3_result.txt", "x") as fh:
    for k, (ok, n) in res.items():
        line = f"{k}: {'MET' if ok else 'FAILED'} cases={n}"
        print(line); fh.write(line + "\n")
    fh.write(f"fails={fails[:20]}\n")
print("fails", fails[:10])
sys.exit(0 if all(ok for ok, _ in res.values()) else 1)
