"""High-precision -log m(beta) for the sigma-folded Gaussian-kernel transfer operator.

Usage: python3 hp.py BETA N   (grid: N points on [0,pi), h=pi/N; full circle 2N points)
       python3 hp.py 16 N --double   (plain double eigenvalue difference, check only)

PREDICATES FIXED BEFORE FIRST RUN
 P0 (method check, beta=16): HP -log m and plain-double -log m agree to 1e-6 (double resolves
    m~1e-8 to ~1e-8 relative; tolerance 1e-6 chosen as 100x that).
 P1 (grid): |(-log m)(N) - (-log m)(2N)| < 1e-3 (1e-3 = 4e-4*c*... chosen as 0.1% of a sqrt(beta)~O(10) scale).
 P2 (convergence of refinement): final Newton step in lambda < 1e-150 * (lambda_e-lambda_o).
 Q1: -log m <= c* sqrt(beta) + 3 log(beta) for all tested beta.
 Q2: (-log m)/sqrt(beta) strictly increasing in beta and < c*.
 Q3: LSQ fit a sqrt(beta)+b log(beta)+c : |a-c*| <= 0.2.
Method: fold by sigma (even/odd blocks on [0,pi) cyclic), conjugate by W=exp(-sqrt(beta) Phi),
 Newton refinement of the eigenpair in 300-digit Decimal (residual in Decimal, correction from a
 double-precision Jacobian inverse), kernel truncated at exp(-600) (band), eps_j is the double value
 (exact Decimal of it) -- the discrete model is defined with that eps.
Output: result file res_<beta>_<N>.txt (mode "x").
"""
import sys, math
import numpy as np
from decimal import Decimal as D, getcontext

getcontext().prec = 300
beta = int(sys.argv[1]); N = int(sys.argv[2]); dbl = '--double' in sys.argv
sb = math.sqrt(beta)


def pi_dec():
    getcontext().prec += 10
    def arctan_inv(x):
        x = D(x); t = 1 / x; s = t; k = 1; x2 = x * x
        while abs(t) > D(10) ** (-getcontext().prec):
            t = -t / x2; k += 2; s += t / k
        return s
    p = 4 * (4 * arctan_inv(5) - arctan_inv(239))
    getcontext().prec -= 10
    return +p

h_f = math.pi / N
xs = np.arange(N) * h_f
eps = 2 * np.arcsinh(np.abs(np.sin(xs)))

if dbl:
    M = 2 * N; X = np.arange(M) * h_f; E = 2 * np.arcsinh(np.abs(np.sin(X)))
    d = X[:, None] - X[None, :]
    K = sum(np.sqrt(beta / 2 / math.pi) * np.exp(-beta * (d + 2 * math.pi * k) ** 2 / 2) for k in (-1, 0, 1))
    A = h_f * np.exp(-E / 2)[:, None] * K * np.exp(-E / 2)[None, :]
    Ae = A[:N, :N] + A[:N, N:]; Ao = A[:N, :N] - A[:N, N:]
    le = np.linalg.eigvalsh(Ae)[-1]; lo = np.linalg.eigvalsh(Ao)[-1]
    m = math.log(le / lo)
    print(beta, N, "double", repr(le), repr(lo), "m", m, "-log m", -math.log(m))
    sys.exit()

# Phi on the cyclic block: distance to well 0 (cyclic mod pi)
fine = 64
tt = np.linspace(0, math.pi / 2, fine * (N // 2 + 1) + 1)
f = np.sqrt(2 * 2 * np.arcsinh(np.abs(np.sin(tt))))
cum = np.concatenate([[0], np.cumsum((f[1:] + f[:-1]) / 2 * np.diff(tt))])
dist = np.minimum(xs, math.pi - xs)
Phi = np.interp(dist, tt, cum)
W = np.exp(-sb * Phi)

PI = pi_dec(); h = PI / N
Ds = [(-D(float(e)) / 2).exp() for e in eps]          # exp(-eps/2)
pref = (D(beta) / (2 * PI)).sqrt()
cut = 600
qmax = int(math.sqrt(2 * cut / beta) / float(h)) + 2
Kt = [D(0)] * (N + 1)
for q in range(N + 1):
    if q <= qmax:
        ex = D(beta) * (q * h) ** 2 / 2
        if ex < cut: Kt[q] = pref * (-ex).exp()
Wd = [D(float(w)) for w in W]

def cyc(m):
    m %= 2 * N
    return min(m, 2 * N - m)

res = {}
for s in (+1, -1):
    rows = []
    Bd = np.zeros((N, N))
    for i in range(N):
        cols = []; vals = []
        for j in range(N):
            q1 = cyc(i - j); q2 = cyc(i - j - N)
            k = Kt[q1] + s * Kt[q2]
            if k == 0: continue
            v = h * Ds[i] * Ds[j] * k * Wd[j] / Wd[i]
            cols.append(j); vals.append(v); Bd[i, j] = float(v)
        rows.append((cols, vals))
    # initial double eigenpair: symmetrise B (B_ij = S_ij W_j/W_i with S symmetric)
    S = Bd * (W[:, None] / W[None, :])
    lam0 = np.linalg.eigvalsh((S + S.T) / 2)[-1]
    inv = np.linalg.inv(Bd - (lam0 * (1 + 1e-9)) * np.eye(N))
    u0 = np.ones(N)
    for _ in range(6):
        u0 = inv @ u0; u0 /= np.max(np.abs(u0))
    k0 = int(np.argmax(np.abs(u0))); u0 /= u0[k0]
    lam0 = float(u0 @ (Bd @ u0) / (u0 @ u0))
    J = np.zeros((N + 1, N + 1))
    J[:N, :N] = Bd - lam0 * np.eye(N); J[:N, N] = -u0; J[N, k0] = 1
    Jinv = np.linalg.inv(J)
    u = [D(float(x)) for x in u0]; lam = D(lam0)
    hist = []
    for it in range(40):
        r = []
        for i in range(N):
            cols, vals = rows[i]
            acc = D(0)
            for c, v in zip(cols, vals): acc += v * u[c]
            r.append(acc - lam * u[i])
        rf = np.array([float(x) for x in r] + [0.0])
        dl = -(Jinv @ rf)
        for i in range(N): u[i] += D(float(dl[i]))
        dlam = D(float(dl[N])); lam += dlam
        hist.append((it, float(np.max(np.abs(rf))), dlam))
        if abs(dlam) < D(10) ** -260 and np.max(np.abs(rf)) < 1e-250: break
    res[s] = (lam, hist)
    print("block", s, "iters", len(hist), "lam", str(lam)[:30], "last |dlam|", float(abs(hist[-1][2]) if hist[-1][2] != 0 else 0), flush=True)

le, lo = res[1][0], res[-1][0]
diff = le - lo
m = (le / lo).ln()
nlm = -(m.ln())
txt = ("beta %d N %d h %.10g\nlambda_e %s\nlambda_o %s\ndiff %s\nm %s\n-log m %s\n(-log m)/sqrt(beta) %s\n"
       "last_dlam_e %s last_dlam_o %s ratio_lastdlam_over_diff %s\n") % (
    beta, N, float(h), str(le)[:60], str(lo)[:60], "%.12E" % diff, "%.12E" % m, str(nlm)[:30],
    str(nlm / D(sb))[:30], "%.3E" % res[1][1][-1][2], "%.3E" % res[-1][1][-1][2],
    "%.3E" % (abs(max(res[1][1][-1][2], res[-1][1][-1][2], key=abs)) / diff))
with open("res_%d_%d.txt" % (beta, N), "x") as fh: fh.write(txt)
print(txt)
