"""f2-cross2 analysis (worker T239).  Usage: python3 -I src/analysis2.py COARSE FINE OUTFILE
COARSE/FINE = ensemble labels under results/ (c2, f2) or (c4, f4).  OUTFILE opened with mode "x" (never overwritten).

PREDICATES (fixed before any production run; same text as src/predicates.txt, abbreviated here):
Split: TRAIN = chains i%4 in {0,1}; HELD = i%4 in {2,3}.
P1 thermalisation per ensemble: |mean plaq hot - cold| < 3 combined SE (chain scatter) AND |first half - second half| < 3 SE.
P2 tau_int (Sokal window c=6) of per-measurement Wa1 and Pa1 pooled over chains < NMEAS/20.
Q1 reconciliation: lambda2 (G4: second largest eigenvalue of Jsym_ij/sqrt(v_i v_j), J pooled over lines/origins/chains)
   equals 1 - R_min over centred 4-bin functions of ONE line in the direction-pooled local law computed from the L-class
   indicator moments, to 1e-6 absolute. Measured only: comparison with G4's .06197(257) (side 5) and .00408(72) (side 10).
MAIN: classes L (local, same position), Z (zero momentum), P0,P1,P2 (lowest momentum 2pi/5 along k). On TRAIN:
   fine-optimal (min R_f), coarse-optimal (min R_c), ratio-optimal (min R_f/R_c, gradient search on the sphere from
   fixed starts, seed 239); reduced span: eigenvectors of (Vf/tr Vf + Vc/tr Vc) in the standardised basis with
   eigenvalue > 1e-9 * max. Plus named tests Wsum (fields 0-2) and Psum (3-5) in each class. Frozen; HELD values
   R_f, R_c, R_f/R_c, Var_f/Var_c, E_f/E_c with delete-one-chain jackknife per lattice, SE combined in quadrature on log.
D: a frozen test defeats alpha := HELD R_f/R_c + 2 SE < alpha. Report min over tests of (ratio + 2 SE).
S: slowest inherited mode on fine = 1 - R_f(fine-optimal, HELD) with SE; resolved := 1 - R_f - 2 SE > 0.
Tolerances: 3 SE (P1) my choice ~0.3% false alarm; NMEAS/20 (P2) => >= ~10 independent samples per chain;
   1e-6 (Q1) rounding/eigen-solver margin; 2 SE (D, S) from the brief / one-sided ~2.3%.
"""
import sys, numpy as np

ROOT = "/home/user/z4-workers/f2-cross2/results/"
K = 54
CLASSES = ["L", "Z", "P0", "P1", "P2"]
NAMES = (["w0", "w1", "w2", "p0", "p1", "p2"] + [f"rect{k}{o}" for k in range(3) for o in "ab"] +
         [f"chair{p}" for p in ["012", "021", "102", "120", "201", "210"]] +
         [f"hh{m}{n}" for m, n in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]] +
         [f"ww{m}{n}" for m, n in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]] +
         [f"w{m}^2" for m in range(3)] + [f"p{m}^2" for m in range(3)] + [f"w{m}p{m}" for m in range(3)] +
         ["p0p1", "p0p2", "p1p2"] + [f"ind{m}b{b}" for m in range(3) for b in range(4)])
assert len(NAMES) == K


def load(label):
    chains = []
    for i in range(16):
        L = open(f"{ROOT}{label}/chain-{i}.txt").read().splitlines()
        assert L[-1] == "END", (label, i)
        d = {"i": i, "J": np.zeros((4, 4))}
        for c in CLASSES:
            d[c] = {"S00": np.zeros((K, K)), "SL": np.zeros((K, K))}
        M = []
        for l in L:
            p = l.split(",")
            t = p[0]
            if t == "M":
                M.append(np.array(p[2:], float))
            elif t == "J":
                d["J"][int(p[1])] = np.array(p[2:], float)
            else:
                for c in CLASSES:
                    if t.startswith(c) and t[len(c):] in ("NS", "S1", "S00", "SL"):
                        k = t[len(c):]
                        if k == "NS": d[c]["NS"] = float(p[1])
                        elif k == "S1": d[c]["S1"] = np.array(p[1:], float)
                        else: d[c][k][int(p[1])] = np.array(p[2:], float)
        d["M"] = np.array(M)
        chains.append(d)
    return chains


def mats(chains, c):
    ns = sum(ch[c]["NS"] for ch in chains)
    S00 = sum(ch[c]["S00"] for ch in chains) / ns
    SL = sum(ch[c]["SL"] for ch in chains) / ns
    if c in ("L", "Z"):
        mu = sum(ch[c]["S1"] for ch in chains) / ns
    else:  # momentum projections: expectation zero by translation invariance; no subtraction
        mu = np.zeros(K)
    C0 = S00 - np.outer(mu, mu)
    CL = SL - np.outer(mu, mu)
    C0 = (C0 + C0.T) / 2
    return C0, C0 - (CL + CL.T) / 2   # V, E


def quant(a, chains, c):
    V, E = mats(chains, c)
    v = a @ V @ a; e = a @ E @ a
    return v, e, e / v


def jk(fun, chains):
    vals = np.array([fun([ch for ch in chains if ch is not x]) for x in chains])
    n = len(chains)
    return fun(chains), np.sqrt((n - 1) / n * ((vals - vals.mean(axis=0)) ** 2).sum(axis=0))


def split(chains):
    return [c for c in chains if c["i"] % 4 in (0, 1)], [c for c in chains if c["i"] % 4 in (2, 3)]


def tau_int(x):
    x = x - x.mean(); n = len(x)
    f = np.fft.rfft(x, 2 * n); acf = np.fft.irfft(f * np.conj(f))[:n]; acf /= acf[0]
    tau = 0.5
    for w in range(1, n):
        tau += acf[w]
        if w >= 6 * tau: break
    return tau


def p1p2(chains, out, label):
    res = []
    m = np.array([c["M"][:, 0].mean() for c in chains])
    hot = m[[c["i"] % 2 == 1 for c in chains]]; cold = m[[c["i"] % 2 == 0 for c in chains]]
    se = np.sqrt(hot.var(ddof=1) / len(hot) + cold.var(ddof=1) / len(cold))
    ok1 = abs(hot.mean() - cold.mean()) < 3 * se
    h = len(chains[0]["M"]) // 2
    dif = np.array([c["M"][:h, 0].mean() - c["M"][h:, 0].mean() for c in chains])
    ok2 = abs(dif.mean()) < 3 * dif.std(ddof=1) / np.sqrt(len(dif))
    out(f"[{label}] P1 hot-cold {hot.mean()-cold.mean():.3e} vs 3SE {3*se:.3e}: {'MET' if ok1 else 'FAILED'}; "
        f"half diff {dif.mean():.3e} vs 3SE {3*dif.std(ddof=1)/np.sqrt(len(dif)):.3e}: {'MET' if ok2 else 'FAILED'}")
    res += [ok1, ok2]
    nm = len(chains[0]["M"])
    for col, nmn in ((1, "Wa1"), (2, "Pa1")):
        t = np.mean([tau_int(c["M"][:, col]) for c in chains])
        ok = t < nm / 20
        out(f"[{label}] P2 tau_int({nmn}) = {t:.2f} (limit {nm/20:.0f}): {'MET' if ok else 'FAILED'}")
        res.append(ok)
    return res


def g4_lambda2(chains):
    J = sum(c["J"] for c in chains); Js = (J + J.T) / 2; v = Js.sum(1)
    M = Js / np.sqrt(np.outer(v, v))
    return np.sort(np.linalg.eigvalsh(M))[-2]


def pooled_min_R(chains):
    """1 - min R over centred 4-bin functions of one line, direction-pooled local law, from L-class raw moments."""
    ns = sum(ch["L"]["NS"] for ch in chains)
    S00 = sum(ch["L"]["S00"] for ch in chains) / ns; SL = sum(ch["L"]["SL"] for ch in chains) / ns
    S1 = sum(ch["L"]["S1"] for ch in chains) / ns
    m = sum(S1[42 + 4 * mu:46 + 4 * mu] for mu in range(3)) / 3
    M2 = sum(S00[42 + 4 * mu:46 + 4 * mu, 42 + 4 * mu:46 + 4 * mu] for mu in range(3)) / 3
    ML = sum(SL[42 + 4 * mu:46 + 4 * mu, 42 + 4 * mu:46 + 4 * mu] for mu in range(3)) / 3
    ML = (ML + ML.T) / 2
    V = M2 - np.outer(m, m); C = ML - np.outer(m, m)
    w, U = np.linalg.eigh(V); keep = w > 1e-9 * w.max(); W = U[:, keep] / np.sqrt(w[keep])
    return np.linalg.eigvalsh(W.T @ C @ W).max()


def reduced_basis(Vf, Vc):
    s = np.sqrt(np.maximum(np.diag(Vf) / np.trace(Vf) + np.diag(Vc) / np.trace(Vc), 0))
    nz = s > 1e-12 * s.max()
    D = np.zeros_like(s); D[nz] = 1 / s[nz]
    A = (Vf / np.trace(Vf) + Vc / np.trace(Vc)) * np.outer(D, D)
    w, U = np.linalg.eigh(A); keep = w > 1e-9 * w.max()
    return (D[:, None] * U[:, keep])       # columns: K-vectors spanning the retained space


def gen_min(E, V, B):
    Vr = B.T @ V @ B; Er = B.T @ E @ B
    w, U = np.linalg.eigh(Vr); keep = w > 1e-9 * w.max(); W = U[:, keep] / np.sqrt(w[keep])
    ev, X = np.linalg.eigh(W.T @ Er @ W)
    return B @ (W @ X[:, 0]), ev[0]


def ratio_min(Ef, Vf, Ec, Vc, B, starts, rng):
    mats_ = [B.T @ M @ B for M in (Ef, Vf, Ec, Vc)]

    def g(y):
        q = [y @ M @ y for M in mats_]
        return np.log(q[0]) - np.log(q[1]) - np.log(q[2]) + np.log(q[3]), q

    def grad(y, q):
        return 2 * (mats_[0] @ y / q[0] - mats_[1] @ y / q[1] - mats_[2] @ y / q[2] + mats_[3] @ y / q[3])

    pinv = np.linalg.pinv(B)
    ys = [pinv @ a for a in starts] + [rng.standard_normal(B.shape[1]) for _ in range(12)]
    best = None
    for y in ys:
        y = y / np.linalg.norm(y); val, q = g(y); step = 0.1
        for it in range(1500):
            gr = grad(y, q); gr -= (gr @ y) * y
            if np.linalg.norm(gr) < 1e-10: break
            while step > 1e-14:
                yn = y - step * gr; yn /= np.linalg.norm(yn); vn, qn = g(yn)
                if np.all(np.array(qn) > 0) and vn < val - 1e-4 * step * (gr @ gr):
                    y, val, q = yn, vn, qn; step *= 1.5; break
                step *= 0.5
            else:
                break
        if best is None or val < best[0]: best = (val, y)
    return B @ best[1], np.exp(best[0])


def main():
    cl, fl, outf = sys.argv[1], sys.argv[2], sys.argv[3]
    fo = open(outf, "x")

    def out(s):
        print(s); fo.write(s + "\n"); fo.flush()

    out(__doc__.strip().splitlines()[0]); out(f"pair coarse={cl} fine={fl}")
    C = load(cl); F = load(fl)
    out(f"chains: {len(C)}, {len(F)}; NMEAS {len(C[0]['M'])}, {len(F[0]['M'])}")
    met = failed = 0
    for lab, ch in ((cl, C), (fl, F)):
        for r in p1p2(ch, out, lab):
            met += r; failed += (not r)
    # Q1
    out("\n== Q1 reconciliation: G4 four-bin statistic (all 16 chains; jackknife over chains) and HELD ==")
    for lab, ch in ((cl, C), (fl, F)):
        lam, lse = jk(g4_lambda2, ch)
        alt = pooled_min_R(ch)
        ok = abs(lam - alt) < 1e-6
        met += ok; failed += (not ok)
        lamh, lseh = jk(g4_lambda2, split(ch)[1])
        out(f"[{lab}] lambda2(J) = {lam:.6f} +- {lse:.6f} (all 16) ; HELD {lamh:.6f} +- {lseh:.6f} ; "
            f"1-Rmin(pooled local indicators) = {alt:.6f}; |diff| = {abs(lam-alt):.2e}: {'MET' if ok else 'FAILED'}")
        J = sum(c["J"] for c in ch); out(f"[{lab}] pooled J =\n{J.astype(int)}")
    out("G4 reference (measurements.md, 2l, 4 streams x 128 meas): side 5 .06197 +- .00257 ; side 10 .00408 +- .00072")

    Ct, Ch = split(C); Ft, Fh = split(F)
    rng = np.random.default_rng(239)
    tests = []
    for c in CLASSES:
        Vf, Ef = mats(Ft, c); Vc, Ec = mats(Ct, c)
        B = reduced_basis(Vf, Vc)
        af, rf = gen_min(Ef, Vf, B); ac, rc = gen_min(Ec, Vc, B)
        ar, rr = ratio_min(Ef, Vf, Ec, Vc, B, [af, ac], rng)
        out(f"\n[{c}] reduced span dim {B.shape[1]} of {K}; TRAIN: min R_f {rf:.5f}, min R_c {rc:.5f}, min R_f/R_c {rr:.5f}")
        aW = np.zeros(K); aW[0:3] = 1; aP = np.zeros(K); aP[3:6] = 1
        for nm, a in ((f"{c}:fine-opt", af), (f"{c}:coarse-opt", ac), (f"{c}:ratio-opt", ar), (f"{c}:Wsum", aW), (f"{c}:Psum", aP)):
            if quant(a, Fh, c)[0] <= 0 or quant(a, Ch, c)[0] <= 0:
                out(f"{nm}: zero variance in this class (skipped)"); continue
            tests.append((nm, c, a))
    out("\n== MAIN: frozen tests evaluated on HELD (8+8 chains), delete-one-chain jackknife ==")
    out(f"{'test':18s} {'R_fine':>18s} {'R_coarse':>18s} {'R_f/R_c':>18s} {'Var_f/Var_c':>12s} {'E_f/E_c':>10s} {'ratio+2SE':>10s} {'1-R_f':>18s}")
    rows = []
    for nm, c, a in tests:
        f_f = lambda ch: np.array(quant(a, ch, c))
        (vf, ef, rf), (svf, sef, srf) = jk(f_f, Fh)
        (vc, ec, rc), (svc, sec, src) = jk(f_f, Ch)
        rat = rf / rc; srat = rat * np.sqrt((srf / rf) ** 2 + (src / rc) ** 2)
        rows.append((nm, rf, srf, rc, src, rat, srat, vf / vc, ef / ec))
        out(f"{nm:18s} {rf:9.5f}({srf:.5f}) {rc:9.5f}({src:.5f}) {rat:9.5f}({srat:.5f}) {vf/vc:12.5g} {ef/ec:10.5g} {rat+2*srat:10.5f} {1-rf:9.5f}({srf:.5f})")
    out("\n== PREDICATE D (defeat of quotient comparison with constant alpha: ratio + 2SE < alpha) ==")
    best = min(rows, key=lambda r: r[5] + 2 * r[6])
    m = best[5] + 2 * best[6]
    out(f"min over {len(rows)} frozen tests of ratio+2SE = {m:.5f} ({best[0]}): " +
        (f"defeats every alpha > {m:.5f} (alpha < 1 defeated)" if m < 1 else "no alpha <= 1 is defeated"))
    out("\n== PREDICATE S (slowest inherited mode on fine: 1 - R_f of the fine-optimal tests, HELD) ==")
    for r in rows:
        if r[0].endswith("fine-opt"):
            res = (1 - r[1]) - 2 * r[2] > 0
            out(f"{r[0]:18s} 1-R_f = {1-r[1]:.5f} +- {r[2]:.5f} : {'RESOLVED' if res else 'not resolved'} ; coarse 1-R_c = {1-r[3]:.5f} +- {r[4]:.5f}")
    allr = max(rows, key=lambda r: (1 - r[1]) / r[2])
    out(f"largest significance of 1-R_f among all frozen tests: {allr[0]} {(1-allr[1]):.5f} +- {allr[2]:.5f}")
    out(f"\nPredicates (P1,P2,Q1 gated): met {met}, failed {failed}; D and S are measured with expectation (see report)")
    fo.close()


if __name__ == "__main__":
    main()
