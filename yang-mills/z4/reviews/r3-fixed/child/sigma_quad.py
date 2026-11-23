"""sigma_quad.py -- string-tension-like quantity by direct Haar quadrature (no Bessel functions).

Method: periodic trapezoid rule with M nodes on [0, 2pi), mp.dps = 50.
  U(1):  c_r = (1/M) sum w(t_k) cos(r t_k),  w = exp(beta (cos t - 1)), beta = N^2
         sigma_U1 = -N^2 log(c_1/c_0)
  SU(2): Haar (2/pi) sin^2 t dt on [0,pi] == (1/pi) sin^2 t dt on [0,2pi)
         c_0 = <w>, c_half = <w * 2cos t>/2, beta = 4N^2,
         sigma_SU2 = -N^2 log(c_half/c_0)
(The common factor exp(-beta) cancels in the ratios.)

Predicates tested (declared before first run):
 P1 node-count agreement: for every N and group, |sigma(M=4096) - sigma(M=8192)| < 1e-30.
    Justification: trapezoid error for an entire periodic integrand ~ relative Fourier
    coefficient at order M ~ exp(-M^2/(2 beta)); worst case beta=16384, M=4096 -> exp(-512),
    so the only residual is roundoff at dps=50 (~1e-45 relative, amplified by N^2 <= 4096
    and by 1/(1-ratio) ~ beta in the log -> still << 1e-30).
 P2 independent cross-check: at N=4 both sigmas agree with mpmath.quad (tanh-sinh) to < 1e-25.
 P3 sanity: c_0 > 0, 0 < c_1/c_0 < 1 and 0 < c_half/c_0 < 1 for all N.
Exit code 0 iff all predicates pass. Results are written to a NEW file results_quad.txt
(refuses to overwrite; then writes results_quad_<n>.txt).
"""
import os, sys
from mpmath import mp, mpf, exp, cos, sin, pi, log, quad, nstr

mp.dps = 50
NS = [4, 8, 16, 32, 64]
M1, M2 = 4096, 8192
TOL1, TOL2 = mpf('1e-30'), mpf('1e-25')

def trap(M, beta):
    s0 = s1 = sq0 = sq1 = mpf(0)
    for k in range(M):
        t = 2 * pi * k / M
        c = cos(t)
        w = exp(beta * (c - 1))
        s0 += w; s1 += w * c
        s2 = 1 - c * c  # sin^2 t
        sq0 += w * s2; sq1 += w * s2 * c
    return s0 / M, s1 / M, sq0 / M, sq1 / M  # U1 c0, U1 c1, (SU2 sums without 1/pi... common factor)

def sig_u1(N, M):
    c0, c1, _, _ = trap(M, mpf(N) ** 2)
    return -N**2 * log(c1 / c0), c1 / c0

def sig_su2(N, M):
    _, _, q0, q1 = trap(M, 4 * mpf(N) ** 2)
    # c0 = (2/pi)... both scale identically; c_half/c0 = <w*2cos t>/2 / <w> = q1/q0
    r = (q1 * 2 / 2) / q0
    return -N**2 * log(r), r

def quad_check(N):
    b = mpf(N) ** 2
    c0 = quad(lambda t: exp(b * (cos(t) - 1)), [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
    c1 = quad(lambda t: exp(b * (cos(t) - 1)) * cos(t), [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2 * pi)
    b2 = 4 * b
    d0 = quad(lambda t: exp(b2 * (cos(t) - 1)) * sin(t) ** 2, [0, pi / 2, pi]) * 2 / pi
    d1 = quad(lambda t: exp(b2 * (cos(t) - 1)) * sin(t) ** 2 * 2 * cos(t), [0, pi / 2, pi]) * 2 / pi / 2
    return -N**2 * log(c1 / c0), -N**2 * log(d1 / d0)

lines, failed = [], []
lines.append(f"mp.dps={mp.dps}  nodes M1={M1}, M2={M2}")
lines.append(f"{'N':>3} {'sigma_U1':>18} {'|dM| U1':>10} {'sigma_SU2':>18} {'|dM| SU2':>10}")
for N in NS:
    u_a, ru = sig_u1(N, M1); u_b, _ = sig_u1(N, M2)
    s_a, rs = sig_su2(N, M1); s_b, _ = sig_su2(N, M2)
    du, ds = abs(u_a - u_b), abs(s_a - s_b)
    lines.append(f"{N:>3} {float(u_b):>18.12f} {nstr(du, 3):>10} "
                 f"{float(s_b):>18.12f} {nstr(ds, 3):>10}")
    if not (du < TOL1): failed.append(f"P1 U1 N={N} diff={nstr(du,5)}")
    if not (ds < TOL1): failed.append(f"P1 SU2 N={N} diff={nstr(ds,5)}")
    if not (0 < ru < 1 and 0 < rs < 1): failed.append(f"P3 N={N} ratios {ru} {rs}")
    if N == 4:
        qu, qs = quad_check(4)
        lines.append(f"    P2 quad check N=4: |U1 diff|={nstr(abs(qu-u_b),3)} |SU2 diff|={nstr(abs(qs-s_b),3)}")
        if not (abs(qu - u_b) < TOL2 and abs(qs - s_b) < TOL2):
            failed.append(f"P2 N=4 quad mismatch U1 {nstr(abs(qu-u_b),5)} SU2 {nstr(abs(qs-s_b),5)}")
lines.append("FAILED: " + ("; ".join(failed) if failed else "none") )
out = "\n".join(lines)

fn = "results_quad.txt"; n = 1
while os.path.exists(fn):
    fn = f"results_quad_{n}.txt"; n += 1
with open(fn, "x") as f:
    f.write(out + "\n")
print(out); print("written", fn)
sys.exit(1 if failed else 0)
