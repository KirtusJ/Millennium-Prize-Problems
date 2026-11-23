"""curv_test.py -- TEST (iii) of PROOF.md step S6 (averaged curvature) for SU(2) Wilson LGT.

Setup. SU(2), metric <X,Y> = -Tr(XY), orthonormal e_a = i sigma_a/sqrt2, Ric = 1 (SZZ (4.8), N/2).
Lattice: periodic L^d (default d=4). Wilson weight exp(-V), V = -(bW/2) sum_p Re Tr Q_p (bW = conventional
beta = 4*beta_SZZ). Coordinates U_e -> exp(t_e.e) U_e. Bakry-Emery matrix B(U) = I + Hess V(U) (dimension 3|E|).
Horizontal = orthogonal complement of infinitesimal gauge directions. lam_full = min eig B,
lam_hor = min eig of B restricted to horizontal space (the quantity of PROOF.md step S2).

PREDICATES (fixed before the first run):
 C0 (control, known answer): at the all-identity configuration lam_full = lam_hor = 1 within 1e-9
    (tolerance: double-precision eigensolver on a matrix of norm <= 12 bW + 1).
 C1 (control): analytic Hessian equals central finite differences (h = 1e-4) on one random configuration,
    max abs difference <= 1e-5 * max(1,bW) (tolerance: FD truncation O(h^2 * bW) + rounding O(eps/h^2) ~ 1e-8).
 C2 (control): at bW = 0.5 the MC plaquette <Re Tr Q/2> agrees with the strong-coupling value I2(bW)/I1(bW)
    within 0.01 (tolerance: O(bW^4) corrections + MC error with ~10^4 plaquette samples; my estimate).
 C3 (control, SZZ (4.2)): ||Hess V||_op <= 12 bW (= 8(d-1)N beta_SZZ for d=4,N=2) on every sample, slack 1e-9.
 T1 (step S5): at the configuration "all links 1 except one link = -1", lam_hor <= 1 - bW for every bW >= 1
    in the list. (Expectation: the 6 plaquettes at Q=-1 give a direction with Hess ~ -bW or worse.)
 T2 (step S6, the CLAIMED averaged-curvature premise, small-volume form): on equilibrium samples,
    at bW = 4.0 and bW = 6.0, lam_hor >= 0.5 on at least 90% of samples.
 T3 (step S6): mean lam_hor at bW = 6.0 >= mean lam_hor at bW = 2.5.
 Measured only: lam_full, lam_hor, fraction of plaquettes with Re Tr Q < 0, per bW.
Seeds fixed (numpy default_rng(seed)). Output opened with mode "x".
Usage: python3 curv_test.py OUTFILE [L] [nsamp] [betas comma-separated]
"""
import sys, math, time, json
import numpy as np

def iv(n, x):  # modified Bessel I_n by series
    return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(60))

def null_space(A, rcond=1e-9):
    u, sv, vt = np.linalg.svd(A)
    r = int((sv > rcond * sv.max()).sum()) if sv.size else 0
    return vt[r:].conj().T

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
E = [1j * s / math.sqrt(2) for s in (s1, s2, s3)]
I2 = np.eye(2, dtype=complex)

def expsu2(t):
    r = np.linalg.norm(t)
    if r == 0: return I2.copy()
    th = r / math.sqrt(2); n = t / r
    return math.cos(th) * I2 + 1j * math.sin(th) * (n[0] * s1 + n[1] * s2 + n[2] * s3)

def coords(Z):  # z_a = -Tr(Z e_a)
    return np.array([-np.trace(Z @ e).real for e in E])

def dag(A): return A.conj().T

def to_su2(M):  # quaternion projection [[a,b],[-b*,a*]], normalized (A sum of SU(2) elements has this form exactly)
    a = (M[0, 0] + M[1, 1].conj()) / 2; b = (M[0, 1] - M[1, 0].conj()) / 2
    n = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
    return np.array([[a, b], [-b.conjugate(), a.conjugate()]]) / n

class Lat:
    def __init__(s, L, d=4):
        s.L, s.d = L, d
        s.sites = [tuple(x) for x in np.ndindex(*([L] * d))]
        s.sidx = {x: i for i, x in enumerate(s.sites)}
        s.nl = len(s.sites) * d
        s.U = np.tile(I2, (s.nl, 1, 1))
        s.plaq = []  # (l1,l2,l3,l4) with Q = U1 U2 U3^dag U4^dag
        for x in s.sites:
            for mu in range(d):
                for nu in range(mu + 1, d):
                    s.plaq.append((s.li(x, mu), s.li(s.sh(x, mu), nu), s.li(s.sh(x, nu), mu), s.li(x, nu)))
        s.lp = [[] for _ in range(s.nl)]
        for pi, p in enumerate(s.plaq):
            for k, l in enumerate(p): s.lp[l].append((pi, k))
    def sh(s, x, mu, k=1):
        y = list(x); y[mu] = (y[mu] + k) % s.L; return tuple(y)
    def li(s, x, mu): return s.sidx[x] * s.d + mu
    def Q(s, p):
        U = s.U; return U[p[0]] @ U[p[1]] @ dag(U[p[2]]) @ dag(U[p[3]])
    def staple(s, l):
        # sum A with Re Tr(U_l A) = sum over plaquettes containing l of Re Tr Q_p
        U = s.U; A = np.zeros((2, 2), complex)
        for pi, k in s.lp[l]:
            p = s.plaq[pi]; u = [U[j] for j in p]
            # Q = u0 u1 u2^d u3^d ; ReTrQ = ReTr(U_l * rest) with rest cyclic
            if k == 0: A += u[1] @ dag(u[2]) @ dag(u[3])
            elif k == 1: A += dag(u[2]) @ dag(u[3]) @ u[0]
            elif k == 2: A += dag(dag(u[3]) @ u[0] @ u[1])  # ReTr(u2^d M) = ReTr(u2 M^d), M = u3^d u0 u1
            else: A += dag(u[0] @ u[1] @ dag(u[2]))
        return A
    def heatbath(s, bW, rng):
        for l in range(s.nl):
            A = s.staple(l)
            k = math.sqrt(max(np.linalg.det(A).real, 0.0))
            if k < 1e-12:
                x = rng.normal(size=4); x /= np.linalg.norm(x)
            else:
                W = to_su2(A); a = bW * k
                while True:
                    u = rng.random()
                    x0 = 1 + math.log(1 - u * (1 - math.exp(-2 * a))) / a
                    if rng.random() < math.sqrt(max(0.0, 1 - x0 * x0)): break
                v = rng.normal(size=3); v *= math.sqrt(max(0, 1 - x0 * x0)) / np.linalg.norm(v)
                x = np.array([x0, *v])
                X = x[0] * I2 + 1j * (x[1] * s1 + x[2] * s2 + x[3] * s3)
                s.U[l] = to_su2(X @ dag(W)); continue
            s.U[l] = x[0] * I2 + 1j * (x[1] * s1 + x[2] * s2 + x[3] * s3)
    def plaq_mean(s):
        q = np.array([np.trace(s.Q(p)).real / 2 for p in s.plaq]); return q.mean(), (q < 0).mean()

def plaq_hess(u, bW):
    """12x12 Hessian of -(bW/2) ReTr(E1 u0 E2 u1 u2^d E3^-1 u3^d E4^-1)."""
    S = [u[0], u[1] @ dag(u[2]), dag(u[3]), I2]  # segments after slots 0..3
    sg = [1, 1, -1, -1]
    H = np.zeros((12, 12))
    def seg(i, j):  # product of segments from slot i to slot j (exclusive), cyclic
        M = I2.copy(); k = i
        while True:
            M = M @ S[k]; k = (k + 1) % 4
            if k == j: return M
    for i in range(4):
        Qi = seg(i, i)
        for a in range(3):
            for b in range(3):
                H[3*i+a, 3*i+b] = np.trace(0.5 * (E[a] @ E[b] + E[b] @ E[a]) @ Qi).real
        for j in range(i + 1, 4):
            A = seg(i, j); B = seg(j, i)
            for a in range(3):
                for b in range(3):
                    v = sg[i] * sg[j] * np.trace(E[a] @ A @ E[b] @ B).real
                    H[3*i+a, 3*j+b] = v; H[3*j+b, 3*i+a] = v
    return -(bW / 2) * H

def plaq_g(u, t, bW):
    e = [expsu2(t[3*k:3*k+3]) for k in range(4)]
    v = [e[0] @ u[0], e[1] @ u[1], e[2] @ u[2], e[3] @ u[3]]
    return -(bW / 2) * np.trace(v[0] @ v[1] @ dag(v[2]) @ dag(v[3])).real

def full_hess(lat, bW):
    n = 3 * lat.nl; H = np.zeros((n, n))
    for p in lat.plaq:
        h = plaq_hess([lat.U[j] for j in p], bW)
        idx = np.concatenate([np.arange(3*l, 3*l+3) for l in p])
        H[np.ix_(idx, idx)] += h
    return H

def gauge_basis(lat):
    n = 3 * lat.nl; G = []
    for x in lat.sites:
        for a in range(3):
            g = np.zeros(n)
            for mu in range(lat.d):
                l = lat.li(x, mu); g[3*l:3*l+3] += np.eye(3)[a]
                l2 = lat.li(lat.sh(x, mu, -1), mu); g[3*l2:3*l2+3] -= coords(lat.U[l2] @ E[a] @ dag(lat.U[l2]))
            G.append(g)
    return np.array(G).T

def lams(lat, bW):
    H = full_hess(lat, bW); B = np.eye(H.shape[0]) + H
    lf = np.linalg.eigvalsh(B)[0]
    N = null_space(gauge_basis(lat).T, rcond=1e-9)
    lh = np.linalg.eigvalsh(N.T @ B @ N)[0]
    hn = np.abs(np.linalg.eigvalsh(H)).max()
    return lf, lh, hn

def main():
    out = open(sys.argv[1], "x")
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    ns = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    betas = [float(b) for b in sys.argv[4].split(",")] if len(sys.argv) > 4 else [0.05, 0.5, 1.0, 2.0, 2.5, 3.0, 4.0, 6.0]
    def w(s): print(s); out.write(s + "\n"); out.flush()
    res = {"met": 0, "failed": 0}
    def pred(name, ok, info):
        res["met" if ok else "failed"] += 1; w(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    rng = np.random.default_rng(12345)
    w(f"curv_test L={L} d=4 nsamp={ns} betas={betas}")
    lat = Lat(L)
    # C0
    lf, lh, hn = lams(lat, 3.0)
    pred("C0", abs(lf - 1) < 1e-9 and abs(lh - 1) < 1e-9, f"identity config bW=3: lam_full={lf:.12f} lam_hor={lh:.12f}")
    # C1
    u = [expsu2(rng.normal(size=3) * 2) for _ in range(4)]; bW = 2.0; h = 1e-4
    Ha = plaq_hess(u, bW); Hf = np.zeros((12, 12))
    for i in range(12):
        for j in range(12):
            ei = np.eye(12)[i] * h; ej = np.eye(12)[j] * h
            Hf[i, j] = (plaq_g(u, ei + ej, bW) - plaq_g(u, ei - ej, bW) - plaq_g(u, -ei + ej, bW) + plaq_g(u, -ei - ej, bW)) / (4 * h * h)
    d1 = np.abs(Ha - Hf).max()
    pred("C1", d1 <= 1e-5 * max(1, bW), f"max|H_analytic - H_FD| = {d1:.2e}")
    # also check staple vs direct ReTr sum on random config
    lat.U = np.array([expsu2(rng.normal(size=3) * 2) for _ in range(lat.nl)])
    l = 5; A = lat.staple(l); direct = sum(np.trace(lat.Q(lat.plaq[pi])).real for pi, k in lat.lp[l])
    w(f"  staple check: ReTr(U A) = {np.trace(lat.U[l] @ A).real:.12f} direct = {direct:.12f}")
    stap_ok = abs(np.trace(lat.U[l] @ A).real - direct) < 1e-10
    # T1
    t1 = []
    for bW in betas:
        if bW < 1: continue
        lat.U = np.tile(I2, (lat.nl, 1, 1)); lat.U[0] = -I2
        lf, lh, hn = lams(lat, bW); t1.append(lh <= 1 - bW)
        w(f"  T1 case bW={bW}: lam_full={lf:.6f} lam_hor={lh:.6f} (1-bW={1-bW:.3f}, 1-2bW={1-2*bW:.3f})")
    pred("T1", all(t1), f"{sum(t1)}/{len(t1)} cases qualify")
    # MC
    summary = {}
    c3 = []
    for bW in betas:
        t0 = time.time()
        lat.U = np.tile(I2, (lat.nl, 1, 1))
        for _ in range(30): lat.heatbath(bW, rng)
        rows = []
        for sidx in range(ns):
            for _ in range(4): lat.heatbath(bW, rng)
            pm, fneg = lat.plaq_mean()
            lf, lh, hn = lams(lat, bW)
            c3.append(hn <= 12 * bW + 1e-9)
            rows.append((pm, fneg, lf, lh, hn))
        r = np.array(rows); summary[bW] = r
        w(f"bW={bW}: plaq={r[:,0].mean():.4f} fneg={r[:,1].mean():.4f} lam_full mean={r[:,2].mean():.4f} min={r[:,2].min():.4f} "
          f"lam_hor mean={r[:,3].mean():.4f} min={r[:,3].min():.4f} max={r[:,3].max():.4f} ||H||max={r[:,4].max():.3f} (12bW={12*bW:.2f}) [{time.time()-t0:.1f}s]")
        w("   lam_hor per sample: " + " ".join(f"{v:.3f}" for v in r[:, 3]))
    if 0.5 in summary:
        sc = iv(2, 0.5) / iv(1, 0.5); pm = summary[0.5][:, 0].mean()
        pred("C2", abs(pm - sc) < 0.01, f"plaq(0.5)={pm:.4f} vs I2/I1={sc:.4f}")
    pred("C3", all(c3), f"{sum(c3)}/{len(c3)} samples qualify")
    for bW in (4.0, 6.0):
        if bW in summary:
            q = summary[bW][:, 3] >= 0.5
            pred(f"T2[bW={bW}]", q.mean() >= 0.9, f"{q.sum()}/{len(q)} samples with lam_hor>=0.5")
    if 6.0 in summary and 2.5 in summary:
        pred("T3", summary[6.0][:, 3].mean() >= summary[2.5][:, 3].mean(), f"{summary[6.0][:,3].mean():.4f} vs {summary[2.5][:,3].mean():.4f}")
    w(f"staple consistency: {'ok' if stap_ok else 'BAD'}")
    w(f"COUNTS met={res['met']} failed={res['failed']}")
    out.close()

if __name__ == "__main__":
    main()
