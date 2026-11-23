"""Smeared squared two-point function C(t) on the periodic unit box.

Method
------
d(k) = ((k1^2+k2^2)/|k|^2) (|k|/2) exp(-t|k|), k in 2pi Z^3, 0 < |k| <= K (spherical cutoff).
C(t) = 2 sum_{k,k'} d(k) d(k') W(k+k'),  W(q) = |fhat(q)|^2 = (2 pi R^2)^3 exp(-q^2 R^2)
(Gaussian FT; image corrections to fhat are O(exp(-1.5^2/(2R^2))) <= exp(-112), dropped).
Write S(p) = sum_k d(k) d(p-k) (a convolution).  Put d on an N^3 integer grid (n = k/2pi),
D(m) = sum_n d(n) e^{2 pi i n.m/N} (inverse FFT), then S = FFT(D^2)/N^3 is the CYCLIC
convolution, which equals the exact linear convolution whenever N >= 4*nmax+1
(nmax = floor(K/2pi)).  Then by Parseval C = (2/N^3) sum_m D(m)^2 w(m), w = N^3 IFFT(W).
W is assigned to grid momenta with |p_i| <= N/2; with N >= 4nmax+1 >= 2K/2pi the dropped
W tail is <= exp(-(N pi R)^2), negligible for all settings used.
Derivative: dC/dt = 2 sum d d' (-(|k|+|k'|)) W = (4/N^3) sum_m D(m) D1(m) w(m),
D1 = IFFT of -|k| d(k) (exact analytic derivative of the truncated sum); cross-checked
by a central finite difference with h = 1e-3 (error O(h^2) ~ 1e-6 relative).

Predicates (fixed before the first run)
---------------------------------------
P1 (K-convergence): for each (t, R), with three or more cutoffs K, the relative change
   |C(K_last) - C(K_prev)| / C(K_last) < 1e-10.  Source of tolerance: the truncation
   error scales like poly(K) exp(-2 t K) (both momenta near the cutoff) and becomes
   << 1e-10 for tK >= 15; the floor is double-precision FFT roundoff, ~1e-13..1e-12
   relative (all summands are positive, no cancellation), so 1e-10 leaves margin.
P2 (grid / aliasing): at the largest K, recomputing with a larger grid N2 > N changes C
   by relative < 1e-10 (same roundoff justification).  A deliberately small grid
   N_small = 2*nmax + 2*ceil(8/(2 pi R)) + 1 (no aliasing onto |p| < 8/R, where
   W/W(0) > e^-64) is also reported and must agree to < 1e-10 as well.
P3 (derivative): analytic -dlogC/dt and central FD (h=1e-3) agree to relative < 1e-5
   (FD truncation ~ h^2 * |C'''/C'| ~ 1e-6 for the decay rates seen here).
If a predicate fails, it is reported as FAIL; nothing is retuned silently.
Results go to results_<n>.txt with the first unused n (never overwritten). No randomness.
"""
import os
import sys
import time
import numpy as np

TWO_PI = 2 * np.pi


def good_size(n):
    """smallest even 2,3,5-smooth integer >= n"""
    m = n + (n % 2)
    while True:
        x = m
        for p in (2, 3, 5):
            while x % p == 0:
                x //= p
        if x == 1:
            return m
        m += 2


def grids(N):
    idx = np.fft.fftfreq(N, 1.0 / N)  # integers in [-N/2, N/2)
    return idx


def compute(t, K, N, Rs, want_deriv=True):
    nmax = int(np.floor(K / TWO_PI))
    idx = grids(N)
    n1 = idx[:, None, None]
    n2 = idx[None, :, None]
    n3 = np.abs(idx[None, None, : N // 2 + 1])  # half spectrum (last axis), N even
    k2perp = (TWO_PI ** 2) * (n1 ** 2 + n2 ** 2)
    k2 = k2perp + (TWO_PI ** 2) * n3 ** 2
    kk = np.sqrt(k2)
    mask = (kk <= K) & (k2 > 0)
    with np.errstate(divide="ignore", invalid="ignore"):
        d = np.where(mask, (k2perp / np.where(k2 > 0, k2, 1.0)) * (kk / 2) * np.exp(-t * kk), 0.0)
    del k2perp, mask
    s = (N, N, N)
    # D(m) = sum_n d e^{+2pi i n m/N}; d is real and even -> Hermitian, D real (irfftn)
    D = np.fft.irfftn(d, s=s) * N ** 3
    D1 = None
    if want_deriv:
        D1 = np.fft.irfftn(-kk * d, s=s) * N ** 3
    del d, kk
    out = {}
    for R in Rs:
        W = (TWO_PI * R * R) ** 3 * np.exp(-k2 * R * R)
        w = np.fft.irfftn(W, s=s) * N ** 3
        del W
        C = 2.0 / N ** 3 * np.sum(D * D * w)
        dC = 4.0 / N ** 3 * np.sum(D * D1 * w) if want_deriv else None
        out[R] = (C, dC)
        del w
    return nmax, out


def next_results_path(base):
    n = 1
    while os.path.exists(os.path.join(base, f"results_{n}.txt")):
        n += 1
    return os.path.join(base, f"results_{n}.txt")


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    Rs = (0.1, 0.05)
    # cutoffs chosen so that t*K ~ 10, 15, 20 (plus one more for t=0.05 if feasible)
    plan = {0.2: [50.0, 75.0, 100.0, 125.0], 0.1: [100.0, 150.0, 200.0, 250.0], 0.05: [200.0, 300.0, 400.0, 500.0]}
    # (run 2: K=250 / K=500 added after run 1 failed P1; tolerance unchanged)
    lines = []
    ok_all = True

    def log(s=""):
        print(s)
        sys.stdout.flush()
        lines.append(s)

    log(__doc__.split("Predicates")[0].strip().splitlines()[0])
    log("numpy " + np.__version__)
    final = {}
    for t in (0.2, 0.1, 0.05):
        res = {R: [] for R in Rs}
        for K in plan[t]:
            nmax = int(np.floor(K / TWO_PI))
            N = good_size(4 * nmax + 1)
            t0 = time.time()
            _, out = compute(t, K, N, Rs, want_deriv=(t == 0.2))
            for R in Rs:
                res[R].append((K, N, out[R][0], out[R][1]))
            log(f"t={t} K={K:g} nmax={nmax} N={N} " +
                " ".join(f"C(R={R})={out[R][0]:.15e}" for R in Rs) + f"  [{time.time()-t0:.1f}s]")
        for R in Rs:
            Cl, Cp = res[R][-1][2], res[R][-2][2]
            rel = abs(Cl - Cp) / abs(Cl)
            p1 = rel < 1e-10
            ok_all &= p1
            log(f"  P1 t={t} R={R}: rel change last two K ({res[R][-2][0]:g}->{res[R][-1][0]:g}) = {rel:.3e} -> {'PASS' if p1 else 'FAIL'}")
        # P2 grid checks at largest K
        K = plan[t][-1]
        nmax = int(np.floor(K / TWO_PI))
        N = res[Rs[0]][-1][1]
        N2 = good_size(N + 32)
        _, out2 = compute(t, K, N2, Rs, want_deriv=False)
        for R in Rs:
            Cl = res[R][-1][2]
            rel = abs(out2[R][0] - Cl) / abs(Cl)
            p2 = rel < 1e-10
            ok_all &= p2
            log(f"  P2 t={t} R={R}: N={N} vs N2={N2}: C={out2[R][0]:.15e} rel={rel:.3e} -> {'PASS' if p2 else 'FAIL'}")
            Ns = 2 * nmax + 2 * int(np.ceil(8 / (TWO_PI * R))) + 1
            Ns = good_size(Ns)
            if Ns < N:
                _, outs = compute(t, K, Ns, (R,), want_deriv=False)
                rel = abs(outs[R][0] - Cl) / abs(Cl)
                p2b = rel < 1e-10
                ok_all &= p2b
                log(f"  P2b t={t} R={R}: small grid Ns={Ns}: C={outs[R][0]:.15e} rel={rel:.3e} -> {'PASS' if p2b else 'FAIL'}")
        for R in Rs:
            final[(t, R)] = res[R]

    # P3 derivative at t=0.2, largest K
    t = 0.2
    K = plan[t][-1]
    N = final[(t, Rs[0])][-1][1]
    h = 1e-3
    _, op = compute(t + h, K, N, Rs, want_deriv=False)
    _, om = compute(t - h, K, N, Rs, want_deriv=False)
    deriv = {}
    for R in Rs:
        C, dC = final[(t, R)][-1][2], final[(t, R)][-1][3]
        an = -dC / C
        fd = -(np.log(op[R][0]) - np.log(om[R][0])) / (2 * h)
        rel = abs(an - fd) / abs(an)
        p3 = rel < 1e-5
        ok_all &= p3
        deriv[R] = an
        log(f"  P3 R={R}: -dlogC/dt analytic={an:.12f} FD(h=1e-3)={fd:.12f} rel={rel:.2e} -> {'PASS' if p3 else 'FAIL'}")
        # K convergence of derivative
        prev = final[(t, R)][-2]
        anp = -prev[3] / prev[2]
        log(f"     analytic at K={prev[0]:g}: {anp:.12f}  rel change={abs(an-anp)/abs(an):.3e}")

    log("")
    log("FINAL TABLE  C(t)  (last K setting; rel change vs previous K)")
    for R in Rs:
        for t in (0.05, 0.1, 0.2):
            r = final[(t, R)]
            rel = abs(r[-1][2] - r[-2][2]) / r[-1][2]
            log(f"R={R:<5} t={t:<5} K={r[-1][0]:<6g} N={r[-1][1]:<4} C={r[-1][2]:.12e}  relchg={rel:.2e}")
        log(f"R={R:<5} -dlogC/dt at t=0.2 (analytic derivative of truncated sum) = {deriv[R]:.10f}")
    log("ALL PREDICATES: " + ("PASS" if ok_all else "FAIL"))
    path = next_results_path(base)
    with open(path, "x", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", path)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
