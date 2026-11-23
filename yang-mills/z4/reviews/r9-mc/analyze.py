"""analyze.py TAG -- analysis of runs/*/blk_*.npz from mc.py. Writes results/analysis_TAG.txt
(never overwritten: exit 3 if it exists). Exit 0 iff every pass/fail predicate below is met
(or not evaluable for lack of data); exit 1 otherwise. ALL lattice numbers are MEASURED ONLY
(Monte Carlo, one lattice size 8^4, few seeds).

Errors: per-config series are binned into bins of B configs, B = 50 by default (rule fixed
before the run: B=50 unless fewer than 20 bins result, then B = N//20); jackknife over bins
for all derived quantities. A table of the error of plaq and of C_1(1) versus B = 1..200 is
printed to show whether B=50 is on the plateau (measured only).

PREDICATES (fixed before the first run):
 P1a beta=2.2, 2.3, 2.5: |plaq - lit| <= 3 sigma + 0.001, lit = 0.5688, 0.6024, 0.6522 (values
     quoted in the brief and matching my memory; I am sure of them to about +-0.001 only, and
     8^4 finite-volume shifts are expected below that; hence the additive 0.001).
 P1b beta=0.5: |plaq - I2(beta)/I1(beta)| <= 3 sigma + 2e-4. I2/I1 is the one-plaquette
     (leading strong-coupling) value; first closed-surface correction is O(u^5), u=0.124,
     ~3e-5 times a combinatorial factor, bounded here by 2e-4 (my estimate, not a theorem).
     Measured only: comparison with beta/4 - beta^3/96 (series of I2/I1) and with the brief's
     beta/4 - (beta/4)^3/6.
 P1c beta=8: |plaq - (1 - 3/(4 beta))| <= 3 sigma + 0.4/beta^2 (second-order coefficient for
     SU(2) is ~0.15 by my memory, uncertain; 0.4 bounds it). Measured only: beta^2 (1-3/(4b)-plaq).
 P1d seeds: for beta 2.3 and 8, plaquettes of the two seeds agree within 3 combined sigma.
 P1e thermalization: per run, mean plaq of first and second half of the measured series agree
     within 3 combined sigma.
 P2  beta=8, R=1: C(1)/C_free(1) in [0.7, 1.3] with C_free from the L=8 torus kernel, provided
     the ratio's jackknife error is < 0.1 ("resolved"); otherwise reported as NOT RESOLVED.
 P3  beta=2.3 (and 2.5): ratios measured/free for C(n), rho(n)=C/<W>^2, C/VarW: no window.
"""
import sys, os, glob
import numpy as np

K8 = {1: [0.4998779, 0.0687686, 0.0110993, 0.0023373], 2: [1.3671134, 0.2621250, 0.0602586, 0.0179905]}
KINF = {1: [0.5, 0.068875, 0.011153, 0.002262], 2: [1.36931, 0.264069, 0.061446, 0.017644]}

def load(pattern):
    cols = []
    seg = []
    for d in sorted(glob.glob(pattern)):
        fs = sorted(glob.glob(os.path.join(d, "blk_*.npz")))
        if not fs:
            continue
        X = []
        for f in fs:
            z = np.load(f)
            X.append(np.column_stack([z["plaq"], z["m1"], z["m2"], z["c1"], z["c2"]]))
        seg.append(np.vstack(X))
    return seg

def bins(seg, B):
    out = []
    for X in seg:
        nb = len(X) // B
        if nb:
            out.append(X[:nb*B].reshape(nb, B, -1).mean(1))
    return np.vstack(out) if out else None

def jack(bm, f):
    n = len(bm); tot = bm.sum(0)
    full = f(tot / n)
    js = np.array([f((tot - bm[i]) / (n - 1)) for i in range(n)])
    err = np.sqrt((n - 1) / n * ((js - js.mean(0))**2).sum(0))
    return full, err

def I_ratio(x):
    def I(nu, x):
        s = 0.0; t = (x/2)**nu / np.prod(np.arange(1, nu+1)); k = 0
        while True:
            s += t; k += 1; t *= (x/2)**2 / (k*(k+nu))
            if t < 1e-18: return s
    return I(2, x) / I(1, x)

def derived(beta):
    def f(v):
        out = [v[0]]
        for R in (1, 2):
            m = v[1 if R == 1 else 2]; c = v[3:7] if R == 1 else v[7:11]
            var = c[0] - m*m
            out += [m, var]
            for n in (1, 2, 3):
                C = c[n] - m*m
                Cf = 1.5 * K8[R][n]**2 / beta**2
                out += [C, C/Cf, (C/m**2)/Cf, (C/var)/(K8[R][n]**2/K8[R][0]**2)]
        return np.array(out)
    return f

def main():
    tag = sys.argv[1]
    fn = "results/analysis_%s.txt" % tag
    if os.path.exists(fn):
        print("refusing to overwrite", fn); sys.exit(3)
    out = []; ok = True
    def P(s): out.append(s); print(s)
    lit = {2.2: 0.5688, 2.3: 0.6024, 2.5: 0.6522}
    groups = [("0.5", "runs/b0p5"), ("2.2", "runs/b2p2"), ("2.3", "runs/b2p3s1*"), ("2.5", "runs/b2p5"), ("8.0", "runs/b8s2*")]
    for bs, pat in groups:
        beta = float(bs)
        seg = load(pat)
        if not seg:
            P("beta=%s: no data" % bs); continue
        N = sum(len(X) for X in seg)
        B = 50 if N // 50 >= 20 else max(1, N // 20)
        P("\n=== beta=%s  configs=%d (segments %s)  bin B=%d ===" % (bs, N, [len(X) for X in seg], B))
        # bin-size table
        row = []
        for Bt in (1, 5, 10, 25, 50, 100, 200):
            bm = bins(seg, Bt)
            if bm is None or len(bm) < 8: continue
            _, e = jack(bm, lambda v: np.array([v[0], v[3]-v[1]**2]))
            row.append("B=%d: %.1e/%.1e" % (Bt, e[0], e[1]))
        P("  binning, error of plaq / of VarW_1: " + " | ".join(row))
        row = []
        for Bt in (1, 5, 10, 25, 50, 100, 200):
            bm = bins(seg, Bt)
            if bm is None or len(bm) < 8: continue
            _, e = jack(bm, lambda v: np.array([v[4]-v[1]**2]))
            row.append("B=%d: %.2e" % (Bt, e[0]))
        P("  binning, error of C_1(1): " + " | ".join(row))
        bm = bins(seg, B)
        val, err = jack(bm, derived(beta))
        p, pe = val[0], err[0]
        P("  plaq = %.5f +- %.5f" % (p, pe))
        if beta in lit:
            d = abs(p - lit[beta]); tol = 3*pe + 0.001; m = d <= tol; ok &= m
            P("  P1a lit %.4f diff %.5f tol %.5f %s" % (lit[beta], d, tol, "MET" if m else "FAILED"))
        if beta == 0.5:
            ir = I_ratio(beta); d = abs(p - ir); tol = 3*pe + 2e-4; m = d <= tol; ok &= m
            P("  P1b I2/I1=%.6f diff %.6f tol %.6f %s" % (ir, d, tol, "MET" if m else "FAILED"))
            P("      measured only: beta/4-beta^3/96=%.6f (diff %.6f); brief's beta/4-(beta/4)^3/6=%.6f (diff %.6f, %.1f sigma)"
              % (beta/4 - beta**3/96, p-(beta/4 - beta**3/96), beta/4-(beta/4)**3/6, p-(beta/4-(beta/4)**3/6), (p-(beta/4-(beta/4)**3/6))/pe))
        if beta == 8.0:
            wc = 1 - 3/(4*beta); d = abs(p - wc); tol = 3*pe + 0.4/beta**2; m = d <= tol; ok &= m
            P("  P1c 1-3/(4b)=%.5f diff %.5f tol %.5f %s ; measured only beta^2(1-3/4b-plaq)=%.3f +- %.3f"
              % (wc, d, tol, "MET" if m else "FAILED", beta**2*(wc-p), beta**2*pe))
        if len(seg) == 2:
            a = [jack(bins([X], B), lambda v: v[:1]) for X in seg]
            d = abs(a[0][0][0]-a[1][0][0]); s = np.hypot(a[0][1][0], a[1][1][0]); m = d <= 3*s; ok &= m
            P("  P1d seeds %.5f+-%.5f vs %.5f+-%.5f : %.1f sigma %s" % (a[0][0][0], a[0][1][0], a[1][0][0], a[1][1][0], d/s, "MET" if m else "FAILED"))
        for X in seg:
            h = len(X)//2
            if h < 2*B: continue
            a = [jack(bins([Y], B), lambda v: v[:1]) for Y in (X[:h], X[h:])]
            d = abs(a[0][0][0]-a[1][0][0]); s = np.hypot(a[0][1][0], a[1][1][0]); m = d <= 3*s; ok &= m
            P("  P1e halves %.5f vs %.5f : %.1f sigma %s" % (a[0][0][0], a[1][0][0], d/s, "MET" if m else "FAILED"))
        i = 1
        for R in (1, 2):
            m, me = val[i], err[i]; var, ve = val[i+1], err[i+1]
            mf = 1 - 1.5*K8[R][0]/beta; vf = 1.5*K8[R][0]**2/beta**2
            P("  R=%d: <W>=%.5f+-%.5f (free LO %.4f, ratio %.3f)  VarW=%.3e+-%.1e (free LO %.3e, ratio %.3f+-%.3f)"
              % (R, m, me, mf, m/mf, var, ve, vf, var/vf, ve/vf))
            i += 2
            for n in (1, 2, 3):
                C, r1, r2, r3 = val[i:i+4]; Ce, e1, e2, e3 = err[i:i+4]
                Cf = 1.5*K8[R][n]**2/beta**2; Cfi = 1.5*KINF[R][n]**2/beta**2
                P("    n=%d C=%.3e+-%.1e  Cfree(L8)=%.3e (inf-vol %.3e)  C/Cfree=%.3f+-%.3f  rho/rho_free=%.3f+-%.3f  corr/corr_free=%.3f+-%.3f  (corr=%.4f)"
                  % (n, C, Ce, Cf, Cfi, r1, e1, r2, e2, r3, e3, C/var))
                if beta == 8.0 and R == 1 and n == 1:
                    if e1 < 0.1:
                        mm = 0.7 <= r1 <= 1.3; ok &= mm
                        P("    P2 C(1)/Cfree(1)=%.3f+-%.3f (resolution %.1f%%) %s" % (r1, e1, 100*e1, "MET" if mm else "FAILED"))
                    else:
                        P("    P2 NOT RESOLVED (error %.3f)" % e1)
                i += 4
    os.makedirs("results", exist_ok=True)
    open(fn, "w").write("\n".join(out) + "\n")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
