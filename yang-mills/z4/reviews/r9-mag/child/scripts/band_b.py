"""Random-measure and extremal check of item (b), plus task-3 endpoint comparison.
Predicates (fixed before running; seed 20261123):
 B1: >= 10000 random discrete measures (1-4 atoms on [0,inf)) satisfy exactly the hypotheses
     M1 >= (2k/9)M0, M1 >= A > 0, M2 <= D.
 B2: every qualifying measure has nu([k/18, 4D/A]) >= A^2/(8D) (relative tol 1e-12).
 B3: every qualifying measure has 4D/A > k/18 (expected automatic: 4D/A >= 8k/9).
 B4: the minimum of nu([L,U])/(A^2/(8D)) found by optimizing over 3-atom measures
     (atom just below L, atom in band, atom above U; exact LP vertex enumeration on grids)
     is >= 1. Expectation: strictly > 1 (bound not tight), value unknown a priori.
 B5: generic random-search 3-atom optimizer never finds a ratio below the B4 minimum minus 1e-9.
 B6: with B(g)=min(g,17sqrt(g)/8+3/16), A=9k/(8(1+B)): k/18 < A/16 exactly for g<17/64 on a log grid
     of g in [1e-4,1e4] (hand prediction: old edge higher at small g).
 B7 (exploratory, expectation uncertain): A/(4K_F) <= k/18 for all g >= 17/64, K_F=min(4,8B/g).
Exit 0 iff B1-B6 hold (B7 reported only).
"""
import numpy as np, sys
rng = np.random.default_rng(20261123)
res = {}
# ---- B1-B3
n_try = 0; n_q = 0; worst = np.inf; b2 = True; b3 = True
while n_q < 20000 and n_try < 2_000_000:
    n_try += 1
    m = rng.integers(1, 5)
    E = rng.exponential(rng.uniform(0.1, 10), m) * (rng.random(m) < 0.9)
    w = rng.exponential(1.0, m)
    M0, M1, M2 = w.sum(), (w*E).sum(), (w*E*E).sum()
    if M1 <= 0: continue
    k = rng.uniform(0, 1.2) * 9*M1/(2*M0)
    A = rng.uniform(0.01, 1) * M1
    D = M2 * (1 + rng.exponential(rng.choice([0.01, 1.0])))
    if not (k > 0 and M1 >= 2*k/9*M0 and M1 >= A > 0 and M2 <= D): continue
    n_q += 1
    L, U = k/18, 4*D/A
    nu = w[(E >= L) & (E <= U)].sum()
    r = nu / (A*A/(8*D)); worst = min(worst, r)
    b2 &= nu >= A*A/(8*D)*(1-1e-12); b3 &= U > L
res['B1'] = n_q >= 10000; res['B2'] = b2; res['B3'] = b3
print(f"B1 qualifying {n_q} of {n_try} draws"); print(f"   min ratio in random sample: {worst:.6f}")
# ---- B4 exact LP over 3 atoms: positions (l just below L, e in [L,U], E > U); minimise band mass w
def lp_min(L, A, D, l, e, Ep):
    # vars x=(b,w,p)>=0 ; constraints: G x >= h
    G = np.array([[l, e, Ep],                    # M1 >= A
                  [-l*l, -e*e, -Ep*Ep],          # -M2 >= -D
                  [l-4*L, e-4*L, Ep-4*L],        # M1 - 4L M0 >= 0   (2k/9 = 4L)
                  [1,0,0],[0,1,0],[0,0,1]], float)
    h = np.array([A, -D, 0, 0, 0, 0], float)
    best = np.inf
    from itertools import combinations
    for c in combinations(range(6), 3):
        Gs = G[list(c)]
        if abs(np.linalg.det(Gs)) < 1e-14: continue
        x = np.linalg.solve(Gs, h[list(c)])
        if np.all(G @ x >= h - 1e-10*np.maximum(1, abs(h))):
            best = min(best, x[1])
    return best
L = 1.0; A = 1.0
summary = []
for D in [0.5, 1.0, 2.0, 5.0, 20.0, 100.0]:
    U = 4*D/A; w0 = A*A/(8*D); best = (np.inf, None)
    l = L*(1-1e-9)
    es = np.unique(np.concatenate([np.geomspace(L, U, 400), [L, U]]))
    Es = U*(1+1e-9) + np.concatenate([[0], np.geomspace(1e-6, 1e3, 200)])*U
    for e in es:
        for Ep in Es:
            v = lp_min(L, A, D, l, e, Ep)
            if v < best[0]: best = (v, (e, Ep))
    # refine around best
    e_b, E_b = best[1]
    for e in np.linspace(max(L, e_b*0.97), min(U, e_b*1.03), 301):
        for Ep in np.linspace(E_b, E_b*1.05+1e-12, 51):
            v = lp_min(L, A, D, l, e, Ep)
            if v < best[0]: best = (v, (e, Ep))
    summary.append((D, best[0]/w0, best[1]))
    print(f"B4 L=1 A=1 D={D}: min nu/w = {best[0]/w0:.6f} at band atom e={best[1][0]:.5f}, upper atom E={best[1][1]:.5f} (U={U})")
r4 = min(s[1] for s in summary); res['B4'] = r4 >= 1
print(f"   overall min ratio over D grid: {r4:.6f}")
# ---- B5 generic random search
b5 = True; gmin = np.inf
for D in [0.5, 1.0, 2.0, 5.0, 20.0, 100.0]:
    U = 4*D; w0 = 1/(8*D); target = [s[1] for s in summary if s[0]==D][0]
    for _ in range(200000 // 6):
        E = np.exp(rng.uniform(np.log(1e-3), np.log(50*U), 3)); w = np.exp(rng.uniform(-12, 3, 3))
        M0, M1, M2 = w.sum(), (w*E).sum(), (w*E*E).sum()
        s = 1.0/M1  # rescale weights so M1 = A = 1 (scaling weights keeps ratio condition)
        w = w*s; M0, M2 = M0*s, M2*s
        if not (1 >= 4*1.0*M0 - 1e-15 and M2 <= D): continue
        r = w[(E >= 1) & (E <= U)].sum()/w0; gmin = min(gmin, r)
        if r < target - 1e-9: b5 = False
res['B5'] = b5; print(f"B5 generic random search min ratio: {gmin:.6f}")
# ---- B6/B7
gs = np.geomspace(1e-4, 1e4, 4001); k = 1.0
B = np.minimum(gs, 17*np.sqrt(gs)/8 + 3/16); Aq = 9*k/(8*(1+B))
old = Aq/16; new = k/18; KF = np.minimum(4, 8*B/gs); kf = Aq/(4*KF)
res['B6'] = bool(np.all((new < old) == (gs < 17/64)))
b7 = bool(np.all(kf[gs >= 17/64] <= new))
cross = gs[np.argmax(~(new < old))]
print(f"B6 first g with k/18 >= A/16: {cross:.5f} (17/64={17/64:.5f}); at g=1e-4: A/16={old[0]:.5f}k vs k/18={new:.5f}k")
print(f"B7 (report only) A/(4K_F)<=k/18 for g>=17/64: {b7}; max A/(4K_F)/(k/18) over g>=17/64: {(kf[gs>=17/64]/new).max():.4f};"
      f" over all g: {(kf/new).max():.4f}; large-g A/(4K_F)={kf[-1]:.5f}k")
for g in [0.01, 0.1, 17/64, 1, 10, 100, 1e4]:
    Bg = min(g, 17*g**.5/8+3/16); Ag = 9/(8*(1+Bg)); KFg = min(4, 8*Bg/g)
    print(f"   g={g:<9.4g} A/16={Ag/16:.5f}  A/(4K_F)={Ag/(4*KFg):.5f}  k/18={1/18:.5f}")
for kk in ['B1','B2','B3','B4','B5','B6']: print(kk, 'PASS' if res[kk] else 'FAIL')
sys.exit(0 if all(res[kk] for kk in ['B1','B2','B3','B4','B5','B6']) else 1)
