"""Even/odd top eigenvalues of T on the circle, b=16, full (unfolded) Nystrom.

Predicate: the two N values (200, 400) of -log(m), m=log(lambda_e/lambda_o),
agree to 1e-6.  Prints PASS/FAIL.
Usage: python3 run.py [outdir]   (files opened with mode "x"; use a fresh outdir to rerun)
"""
import sys, os, numpy as np

out = sys.argv[1] if len(sys.argv) > 1 else "."
os.makedirs(out, exist_ok=True)

# control: trapezoid and Gauss-Legendre for int_0^pi sin = 2
n = 2000
a = np.linspace(0, np.pi, n + 1)
trap = np.pi / n * (np.sin(a).sum() - 0.5 * (np.sin(a[0]) + np.sin(a[-1])))
xg, wg = np.polynomial.legendre.leggauss(40)
gauss = (np.pi / 2) * np.sum(wg * np.sin((np.pi / 2) * (xg + 1)))
with open(os.path.join(out, "control.txt"), "x") as f:
    f.write(f"trapezoid {trap!r}\ngauss {gauss!r}\n")

b = 16.0
def solve(N):
    M = 2 * N; h = 2 * np.pi / M
    x = h * np.arange(M)
    eps = 2 * np.arcsinh(np.abs(np.sin(x)))
    d = x[:, None] - x[None, :]
    K = sum(np.sqrt(b / (2 * np.pi)) * np.exp(-b * (d + 2 * np.pi * k) ** 2 / 2) for k in (-1, 0, 1))
    w = np.exp(-eps / 2)
    A = h * (w[:, None] * K * w[None, :])
    A = (A + A.T) / 2  # already symmetric; removes rounding asymmetry
    lam, V = np.linalg.eigh(A)
    le = lo = None
    for i in np.argsort(-lam):
        v = V[:, i]
        s = v[N:] if False else v[np.arange(M) + N - M * ((np.arange(M) + N) // M)]
        pe, po = np.linalg.norm(s - v), np.linalg.norm(s + v)
        if min(pe, po) > 1e-6 * np.linalg.norm(v):
            continue  # mixed (degenerate) vector, skip
        if pe < po and le is None: le = lam[i]
        if po < pe and lo is None: lo = lam[i]
        if le is not None and lo is not None: break
    m = np.log(le / lo)
    return le, lo, m, -np.log(m)

res = {N: solve(N) for N in (200, 400)}
lines = [f"N={N} lambda_e={r[0]!r} lambda_o={r[1]!r} m={r[2]!r} -log(m)={r[3]!r}" for N, r in res.items()]
diff = res[200][3] - res[400][3]
lines.append(f"difference -log m (N=200 minus N=400) = {diff!r}")
lines.append("predicate (|diff|<1e-6): " + ("PASS" if abs(diff) < 1e-6 else "FAIL"))
txt = "\n".join(lines) + "\n"
with open(os.path.join(out, "result.txt"), "x") as f:
    f.write(txt)
print(open(os.path.join(out, "control.txt")).read() + txt)
