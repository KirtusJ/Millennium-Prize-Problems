"""Lattice correlator: position-space vs momentum-space representation, and N-scan.

Definitions (ell = 1, b = ell/N, R = 0.1):
  khat_i = (2/b) sin(k_i b/2), khat = |khat_vec|, w(k) = ((khat_1^2+khat_2^2)/khat^2) * khat/2, k != 0
  D_t(r) = ell^-3 sum_{k!=0} exp(i k.r) w(k) exp(-t khat)
  f(y)   = sum_{m in Z^3} exp(-|y - m ell|^2 / (2 R^2))    (images m in {-2..2}^3; rest < e^-50)
  C_pos(t) = 2 b^6 sum_{x,y} f(bx) f(by) D_t(x-y)^2
  C_mom(t) = (2/ell^6) sum_{k,k'!=0} |fhat(k+k')|^2 w(k) w(k') exp(-t(khat+k'hat)),
             fhat(q) = b^3 sum_x f(bx) exp(-i q.bx)

PREDICATES (fixed before the first run):
  P1: N = 8, t in {0.05, 0.1, 0.2}. C_pos by brute-force double sum over all (x,y) site pairs
      (D_t on the lattice via inverse FFT), C_mom by brute-force double sum over all (k,k') != 0.
      Predicate: |C_pos - C_mom| / |C_mom| < 1e-10 for every t.
      Why 1e-10: the identity is algebraically exact on the finite lattice (Parseval on Z_N^3),
      so the only discrepancy is float64 rounding. Both sides are sums of ~2.6e5 non-negative
      terms (no cancellation), so the expected relative error is ~1e-14..1e-13; 1e-10 leaves a
      wide margin for rounding while any real error (wrong factor of b, ell, 2, sign of k,
      missing term) gives O(1e-3) or larger discrepancies.
  P2: N in {16, 24, 32, 48, 64}, t in {0.05, 0.1, 0.2}: C_b(t) via FFT,
      C = 2 b^6 sum_z A(z) D_t(z)^2, A = autocorrelation of f on the lattice.
      Predicate: every value is finite and > 0.
  Exit code 0 iff all predicates hold. No randomness is used.

Results are written to a new file results_<tag>.txt (opened with mode 'x': never overwrites).
Usage: python corr_check.py <tag>
"""
import sys
import numpy as np

ELL = 1.0
R = 0.1
TS = (0.05, 0.1, 0.2)


def lattice(N):
    b = ELL / N
    n = np.arange(N)
    k1 = 2 * np.pi * n / ELL
    kh1 = (2.0 / b) * np.sin(k1 * b / 2)
    KX, KY, KZ = np.meshgrid(kh1, kh1, kh1, indexing="ij")
    khat2 = KX**2 + KY**2 + KZ**2
    khat = np.sqrt(khat2)
    w = np.zeros_like(khat)
    nz = khat2 > 0
    w[nz] = (KX[nz]**2 + KY[nz]**2) / khat2[nz] * khat[nz] / 2
    # f on sites
    y1 = b * n
    Y = np.meshgrid(y1, y1, y1, indexing="ij")
    F = np.zeros((N, N, N))
    for m1 in range(-2, 3):
        for m2 in range(-2, 3):
            for m3 in range(-2, 3):
                d2 = (Y[0] - m1 * ELL)**2 + (Y[1] - m2 * ELL)**2 + (Y[2] - m3 * ELL)**2
                F += np.exp(-d2 / (2 * R**2))
    return b, khat, w, nz, F


def D_lattice(N, khat, w, t):
    G = w * np.exp(-t * khat)  # zero at k = 0 since w(0) = 0
    D = np.fft.ifftn(G) * N**3 / ELL**3
    assert np.max(np.abs(D.imag)) < 1e-9 * max(1.0, np.max(np.abs(D.real)))
    return D.real


def C_pos_brute(N, b, khat, w, F, t):
    D = D_lattice(N, khat, w, t)
    idx = np.indices((N, N, N)).reshape(3, -1).T  # all sites
    Ff = F.reshape(-1)
    tot = 0.0
    for i, x in enumerate(idx):
        d = (x[None, :] - idx) % N
        Dxy = D[d[:, 0], d[:, 1], d[:, 2]]
        tot += Ff[i] * np.sum(Ff * Dxy**2)
    return 2 * b**6 * tot


def C_mom_brute(N, b, khat, w, nz, F, t):
    fhat = b**3 * np.fft.fftn(F)  # fhat at q = 2 pi n / ell, index n mod N
    P = np.abs(fhat)**2
    nlist = np.indices((N, N, N)).reshape(3, -1).T[nz.reshape(-1)]
    g = (w * np.exp(-t * khat))[nz]
    tot = 0.0
    for i, n1 in enumerate(nlist):
        s = (n1[None, :] + nlist) % N
        tot += g[i] * np.sum(g * P[s[:, 0], s[:, 1], s[:, 2]])
    return 2 / ELL**6 * tot


def C_fft(N, b, khat, w, F, t):
    D = D_lattice(N, khat, w, t)
    A = np.fft.ifftn(np.abs(np.fft.fftn(F))**2).real  # A(z) = sum_y F(y+z) F(y)
    return 2 * b**6 * np.sum(A * D**2)


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "run1"
    out = []
    ok = True
    out.append("P1: N=8 brute force, position vs momentum")
    N = 8
    b, khat, w, nz, F = lattice(N)
    for t in TS:
        cp = C_pos_brute(N, b, khat, w, F, t)
        cm = C_mom_brute(N, b, khat, w, nz, F, t)
        cf = C_fft(N, b, khat, w, F, t)
        rel = abs(cp - cm) / abs(cm)
        relf = abs(cf - cm) / abs(cm)
        good = rel < 1e-10
        ok &= good
        out.append(f"  t={t:<5} C_pos={cp:.15e} C_mom={cm:.15e} rel={rel:.3e} "
                   f"(fft rel={relf:.3e}) {'PASS' if good else 'FAIL'}")
    out.append("P2: C_b(t) via FFT")
    out.append("  N    " + "  ".join(f"t={t:<20}" for t in TS))
    for N in (16, 24, 32, 48, 64):
        b, khat, w, nz, F = lattice(N)
        vals = [C_fft(N, b, khat, w, F, t) for t in TS]
        good = all(np.isfinite(v) and v > 0 for v in vals)
        ok &= good
        out.append(f"  {N:<4} " + "  ".join(f"{v:.15e}  " for v in vals) + (" PASS" if good else " FAIL"))
    out.append("ALL PREDICATES " + ("PASS" if ok else "FAIL"))
    text = "\n".join(out) + "\n"
    with open(f"results_{tag}.txt", "x", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
