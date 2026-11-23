"""Checks for the p8-rev2 revision (T56). Predicates fixed before the first run.

P1 (C1) Path x0-x1-x2, 50 random SU(2) draws (seed 2026). Convention (U^g)_xy = g_x U_xy g_y^{-1}.
    Corrected recursion g_y = g_x U_xy: max over draws and both tree links of ||U^g - 1||_F <= 1e-12.
    Tolerance: double-precision roundoff of 3 products of 2x2 unitaries (~1e-15), with 1000x margin.
P2 (C1) Printed recursion g_y = U_yx^{-1} g_x: first link identity (<=1e-12) in all draws, second link
    deviation > 1e-6 in at least 49 of 50 draws (generic non-commutation). Expected to hold (defect of printed text).
P3 (C8) Six angles pi/3: product exp(i*sum) = 1 within 1e-12, sum = 2pi within 1e-12, s = 1-cos(pi/3) = 1/2 within 1e-12.
P4 (C8) For 200000 random 6-vectors of angles in (-pi,pi] (seed 7) with sum = 2 pi m, m != 0 (case count reported):
    max_p |theta_p| >= pi/3 - 1e-12 in every qualifying case.
P5 (C7/C8) Exponent arithmetic: tail exp(D - t/8) at t = beta/2 equals exp(D - beta/16); at t = beta*eta/K^2 equals
    exp(D - beta*eta/(8K^2)); relative error <= 1e-14 over 1000 random (D, beta, eta, K) (seed 11).
P6 (C3) Reviewer example: eigenvalues 1, e^-m, e^-2m; psi in e^-2m mode. For m in {0.1,0.01,0.001}, c=1/2:
    C(xi) = e^-2 (rel 1e-12), C(c xi)/C(xi) = e^{2(1-c)} = e (rel 1e-12), i.e. (C) holds with K_C = e independent of m.
P7 (C2) Toy self-adjoint T on R^5 with eigenvalues 1 (Omega), 0.6, -0.5, 0.3, 0 (kernel), random orthonormal basis
    (seed 3). With H = -1/2 log T^2 on ran T: ||e^{-H}|Omega^perp|| = ||T|Omega^perp|| (1e-12); for random psi (projected to
    ran T), <psi,T^n psi> = <psi,e^{-nH}psi> at n = 2,4,6 (1e-12) and differs at n = 1,3 by more than 1e-3.
P8 (C10) sign representation of Z2: delta = min_{g!=1}(1 - Re chi(g)/N) = 2, so beta*delta/2 = beta.
P9 (C11) 260+290+290 = 840 and 1500 - 10 = 1490.
"""
import json, math, numpy as np
res = {}
rng = np.random.default_rng(2026)
def su2(r):
    a = r.normal(size=4); a /= np.linalg.norm(a)
    return np.array([[a[0]+1j*a[3], a[2]+1j*a[1]], [-a[2]+1j*a[1], a[0]-1j*a[3]]])
I = np.eye(2); inv = np.linalg.inv
new_dev = 0.0; old_first = 0.0; old_second_big = 0
for _ in range(50):
    U01, U12 = su2(rng), su2(rng)
    g0 = I; g1 = g0 @ U01; g2 = g1 @ U12
    new_dev = max(new_dev, np.linalg.norm(g0@U01@inv(g1)-I), np.linalg.norm(g1@U12@inv(g2)-I))
    h0 = I; h1 = inv(inv(U01)) @ h0; h2 = inv(inv(U12)) @ h1
    old_first = max(old_first, np.linalg.norm(h0@U01@inv(h1)-I))
    if np.linalg.norm(h1@U12@inv(h2)-I) > 1e-6: old_second_big += 1
res['P1'] = dict(max_dev=new_dev, met=new_dev <= 1e-12)
res['P2'] = dict(first_link_dev=old_first, second_link_failures=old_second_big, met=old_first <= 1e-12 and old_second_big >= 49)
th = [math.pi/3]*6
prod = np.exp(1j*sum(th))
res['P3'] = dict(prod_dev=abs(prod-1), sum_dev=abs(sum(th)-2*math.pi), s_dev=abs(1-math.cos(math.pi/3)-0.5),
                 met=abs(prod-1) <= 1e-12 and abs(sum(th)-2*math.pi) <= 1e-12 and abs(1-math.cos(math.pi/3)-0.5) <= 1e-12)
r4 = np.random.default_rng(7); q = 0; viol = 0
for _ in range(200000):
    t = r4.uniform(-math.pi, math.pi, 6)
    m = round(t.sum()/(2*math.pi))
    t[5] = 2*math.pi*m - t[:5].sum()   # force sum = 2 pi m
    if not (-math.pi < t[5] <= math.pi) or m == 0: continue
    q += 1
    if np.abs(t).max() < math.pi/3 - 1e-12: viol += 1
res['P4'] = dict(qualifying=q, violations=viol, met=(q > 0 and viol == 0))
r5 = np.random.default_rng(11); worst = 0.0
for _ in range(1000):
    D, beta, eta, K = r5.uniform(0, 70), r5.uniform(1, 1e3), r5.uniform(1e-3, 2), r5.uniform(1, 50)
    tail = lambda t: D - t/8
    worst = max(worst, abs(tail(beta/2)-(D-beta/16))/abs(D-beta/16), abs(tail(beta*eta/K**2)-(D-beta*eta/(8*K**2)))/abs(D-beta*eta/(8*K**2)))
res['P5'] = dict(max_rel=worst, met=worst <= 1e-14)
ok6 = True; vals = []
for m in (0.1, 0.01, 0.001):
    xi = 1/m; C = lambda n: math.exp(-2*m*n)
    a, b = C(xi), C(xi/2)/C(xi); vals.append((m, a, b))
    ok6 &= abs(a/math.exp(-2)-1) <= 1e-12 and abs(b/math.e-1) <= 1e-12
res['P6'] = dict(values=vals, met=ok6)
r7 = np.random.default_rng(3)
Q, _ = np.linalg.qr(r7.normal(size=(5, 5))); ev = np.array([1, .6, -.5, .3, 0.])
T = Q @ np.diag(ev) @ Q.T; Om = Q[:, 0]; Pperp = np.eye(5) - np.outer(Om, Om)
Pran = Q[:, :4] @ Q[:, :4].T
expH = Q[:, :4] @ np.diag(np.abs(ev[:4])) @ Q[:, :4].T    # e^{-H} = |T| on ran T
n1 = np.linalg.norm(T @ Pperp, 2); n2 = np.linalg.norm(expH @ Pperp, 2)
psi = Pran @ Pperp @ r7.normal(size=5)
even = max(abs(psi@np.linalg.matrix_power(T, n)@psi - psi@np.linalg.matrix_power(expH, n)@psi) for n in (2, 4, 6))
odd = min(abs(psi@np.linalg.matrix_power(T, n)@psi - psi@np.linalg.matrix_power(expH, n)@psi) for n in (1, 3))
res['P7'] = dict(norm_T=n1, norm_expH=n2, even_dev=even, odd_min_diff=odd, met=abs(n1-n2) <= 1e-12 and even <= 1e-12 and odd > 1e-3)
delta = min(1 - (-1)/1 for g in [-1])
res['P8'] = dict(delta=delta, met=delta == 2)
res['P9'] = dict(sum=260+290+290, n8=1500-10, met=(260+290+290 == 840 and 1500-10 == 1490))
res['summary'] = dict(met=sum(v['met'] for k, v in res.items() if k.startswith('P')), failed=[k for k, v in res.items() if k.startswith('P') and not v['met']])
with open('results_check_rev.json', 'x') as f:
    json.dump(res, f, indent=1, default=float)
print(json.dumps(res['summary'], default=float))
raise SystemExit(0 if not res['summary']['failed'] else 1)
