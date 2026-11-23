"""Truncated lattice sum G(t) (l = 1).

G(t) = l^-3 * sum_{k in (2 pi/l) Z^3, k != 0} |F(k)|^2 * ((k1^2+k2^2)/|k|^2) * (|k|/2) * exp(-t|k|)
F(k) = F1(k1) F1(k2),  F1(q) = 2 sin(qR/2)/q  (q != 0),  F1(0) = R.

Method: cube truncation |n_i| <= M, k_i = 2 pi n_i / l. The summand is even in each
component, so only the octant n_i >= 0 is summed with multiplicity 2 per nonzero
component (exact rewriting, not an approximation). Loop over n3, broadcast over (n1,n2).
For each (R,t) M starts at 16 and is doubled until the relative change between
G(M) and G(2M) is < 1e-6 (cap M_MAX = 1024). No randomness.

PREDICATES (fixed before the first run):
 P1 control: control.txt value equals x/(1-x)^2, x = e^-1, to |diff| <= 5e-7
    (tolerance = half a unit in the 6th decimal, i.e. the rounding of a 6-decimal answer).
 P2 truncation: for every (R,t) the last doubling gives relative change < 1e-6
    (tolerance given by the task statement).
 P3 positivity/monotonicity: G(t) > 0 and strictly decreasing in t for each R.
    Exact consequence of every term being >= 0 with exp(-t|k|) decreasing; no tolerance.
 P4 decay rate: r(t) = -d ln G/dt by central difference, step h = 0.01.
    r(t) is an exp(-t|k|)-weighted mean of |k| over terms with k1^2+k2^2 > 0, so
    exactly r(t) > 2 pi (smallest such |k|) and dr/dt = -Var <= 0, i.e. r(3) < r(2).
    FD error O(h^2 * r''') plus O(eps_G / h) with eps_G ~ 1e-6 relative ->
    allowed slack 1e-3 on both inequalities (r > 2pi - 1e-3, r(3) < r(2) + 1e-3).
Results are written to results_continuum.txt; the program refuses to overwrite it.
"""
import math
import os
import sys

import numpy as np

L = 1.0
RS = [0.25, 0.125]
TS = [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0]
H = 0.01
TOL = 1e-6
M0 = 16
M_MAX = 1024
OUT = "results_continuum.txt"


def F1sq(q, R):
    out = np.empty_like(q)
    nz = q != 0
    out[nz] = (2.0 * np.sin(q[nz] * R / 2.0) / q[nz]) ** 2
    out[~nz] = R * R
    return out


def G(t, R, M):
    n = np.arange(M + 1, dtype=np.float64)
    mult = np.where(n == 0, 1.0, 2.0)
    q = 2.0 * math.pi * n / L
    f2 = F1sq(q, R) * mult
    k1, k2 = np.meshgrid(q, q, indexing="ij")
    kp2 = k1 * k1 + k2 * k2
    A = np.outer(f2, f2) * kp2  # |F|^2 * kperp^2 * multiplicities(n1,n2)
    total = 0.0
    for i3 in range(M + 1):
        k3 = q[i3]
        kk = np.sqrt(kp2 + k3 * k3)
        with np.errstate(divide="ignore", invalid="ignore"):
            term = A * np.exp(-t * kk) / (2.0 * kk)
        if i3 == 0:
            term[0, 0] = 0.0  # k = 0 excluded (its weight kperp^2 is 0 anyway)
        total += mult[i3] * term.sum()
    return total / L ** 3


def converged(t, R):
    M = M0
    g = G(t, R, M)
    while True:
        M2 = 2 * M
        g2 = G(t, R, M2)
        rel = abs(g2 - g) / abs(g2)
        if rel < TOL or M2 >= M_MAX:
            return g2, M2, rel
        M, g = M2, g2


def main():
    if os.path.exists(OUT):
        print(f"refusing to overwrite {OUT}", file=sys.stderr)
        return 3
    ok = True
    x = math.exp(-1.0)
    exact = x / (1 - x) ** 2
    ctrl = float(open("control.txt").read().strip())
    p1 = abs(ctrl - exact) <= 5e-7
    print(f"P1 control {ctrl} vs exact {exact:.10f}: {'MET' if p1 else 'FAILED'}")
    ok &= p1

    lines = ["# R  t  G(t)  M_used  rel_change_last_doubling"]
    p2 = True
    p3 = True
    p4 = True
    rate_lines = []
    for R in RS:
        gs = []
        for t in TS:
            g, M, rel = converged(t, R)
            gs.append(g)
            p2 &= rel < TOL
            line = f"{R:<6} {t:<5} {g:.12e} {M:5d} {rel:.3e}"
            print(line, flush=True)
            lines.append(line)
        p3 &= all(v > 0 for v in gs) and all(a > b for a, b in zip(gs, gs[1:]))
        rates = {}
        for t in (2.0, 3.0):
            Mfd = 64
            gp, gm = G(t + H, R, Mfd), G(t - H, R, Mfd)
            r = -(math.log(gp) - math.log(gm)) / (2 * H)
            rates[t] = r
            rate_lines.append(f"# decay rate R={R} t={t}: -dlnG/dt = {r:.9f} (central diff h={H}, M={Mfd}); 2*pi = {2*math.pi:.9f}")
        p4 &= rates[2.0] > 2 * math.pi - 1e-3 and rates[3.0] > 2 * math.pi - 1e-3
        p4 &= rates[3.0] < rates[2.0] + 1e-3
    for rl in rate_lines:
        print(rl)
    lines += rate_lines
    lines.append(f"# P1 {'MET' if p1 else 'FAILED'}  P2 {'MET' if p2 else 'FAILED'}  P3 {'MET' if p3 else 'FAILED'}  P4 {'MET' if p4 else 'FAILED'}")
    print(lines[-1])
    ok &= p2 and p3 and p4
    with open(OUT, "x") as fh:
        fh.write("\n".join(lines) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
