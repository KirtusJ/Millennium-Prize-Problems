"""free.py -- free (per colour, unit coupling) flux kernel K_R(n) of a spatial R x R square on a
periodic L^4 torus, zero mode removed, Feynman gauge (gauge invariant result):
   K_R(n) = (1/L^4) sum_{k != 0} sum_mu |f_mu(k)|^2 cos(k_4 n) / khat^2 ,  khat^2 = sum 4 sin^2(k/2)
with f_mu the signed link indicator of the square's boundary (counterclockwise).
Writes results/free_<L>.txt (never overwritten; exit 3 if it exists).

PREDICATES (fixed before first run):
 F1 (control) L=8: K_1(0) = (1 - 8^-4)/2 to 1e-12 (exact equipartition identity quoted in README).
 F2 (control) L=48: K_1(n), K_2(n), n=1..3 equal README values (0.068875, 0.011153, 0.002262;
    0.264069, 0.061446, 0.017644) to 2e-6 absolute. Tolerance: README rounds to 6 decimals
    (+-5e-7) plus finite-volume image terms which we expect << 1e-6 at L=48; 2e-6 allows both.
    If F2 fails at 2e-6 the printed difference is kept and the cause stated.
 F3 the identity G(0) = 0.15493339 (README control) to 1e-4 at L=48 (finite-volume: G_L(0)
    approaches G(0) like 1/L^2 roughly... we only expect 1e-4 at L=48; measured only otherwise).
Outputs also K_R(0) = G0 for R=2 (needed for the free mean and variance), on L=8 and L=48.
"""
import sys, os
import numpy as np

def kernel(L, R, nmax=4):
    k = 2*np.pi*np.fft.fftfreq(L)
    k1, k2, k3, k4 = np.meshgrid(k, k, k, k, indexing="ij")
    kh2 = 4*(np.sin(k1/2)**2 + np.sin(k2/2)**2 + np.sin(k3/2)**2 + np.sin(k4/2)**2)
    kh2[0, 0, 0, 0] = np.inf
    a = np.arange(R)
    # dir 1 links: bottom (a,0) +, top (a,R) -. Fourier f(k)=sum f(x) e^{-ikx}; link at x
    e1 = np.exp(-1j*np.multiply.outer(k, a)).sum(-1)          # sum_a e^{-i k a}
    f1 = e1[:, None] * (1 - np.exp(-1j*k*R))[None, :]           # (k1,k2)
    f2 = (np.exp(-1j*k*R) - 1)[:, None] * e1[None, :]           # right (R,b) +, left (0,b) -
    w = (np.abs(f1)**2 + np.abs(f2)**2)[:, :, None, None]
    out = []
    for n in range(nmax+1):
        out.append(float((w*np.cos(k4*n)/kh2).sum().real / L**4))
    G0 = float((1/kh2).sum()/L**4)
    return out, G0

def main():
    os.makedirs("results", exist_ok=True)
    lines = []; ok = True
    readme = {1: [0.068875, 0.011153, 0.002262], 2: [0.264069, 0.061446, 0.017644]}
    for L in (8, 48):
        for R in (1, 2):
            K, G0 = kernel(L, R)
            lines.append("L=%d R=%d K(0..4)= %s   G_L(0)=%.8f" % (L, R, " ".join("%.7f" % x for x in K), G0))
            if L == 8 and R == 1:
                d = abs(K[0] - (1 - 8.0**-4)/2); p = d < 1e-12; ok &= p
                lines.append("F1 K1(0) vs (1-L^-4)/2 diff=%.2e %s" % (d, "MET" if p else "FAILED"))
            if L == 48:
                for n in (1, 2, 3):
                    d = abs(K[n] - readme[R][n-1]); p = d < 2e-6; ok &= p
                    lines.append("F2 R=%d n=%d K=%.7f readme=%.6f diff=%.1e %s" % (R, n, K[n], readme[R][n-1], d, "MET" if p else "FAILED"))
                if R == 1:
                    d = abs(G0 - 0.15493339)
                    lines.append("F3 G_48(0)=%.8f diff=%.1e %s" % (G0, d, "MET" if d < 1e-4 else "FAILED"))
                    ok &= d < 1e-4
    fn = "results/free_v1.txt"
    if os.path.exists(fn):
        print("refusing to overwrite", fn); sys.exit(3)
    open(fn, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
