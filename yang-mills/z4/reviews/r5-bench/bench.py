"""B1/B2 benchmark: C_b(t) = 2 b^6 sum_{x,y} f(bx) f(by) D_t(x-y)^2 for free lattice Maxwell, by FFT.

Parameters (fixed, no randomness): ell = 1, N in {16, 32, 64, 128}, b = 1/N, R in {0.1, 0.05}.
f(x) = sum_{n in {-1,0,1}^3} exp(-|x - c - n|^2/(2R^2)), c = (0.5,0.5,0.5), peak 1, evaluated at sites b*j.
(Periodization by the 27 nearest images; omitted images are < exp(-1.5^2/(2*0.1^2)) ~ 1e-49 relative.
B_3 sits at plaquette centres, offset b/2 from f's sample points; C depends on f only through |fhat(q)|^2
on the lattice, so that offset is irrelevant.)
D_t(r) = N^3 * ifftn(d), d(k) = ((k^1^2+k^2^2)/k^2)(k^/2)e^{-t k^}, d(0)=0.  C via cyclic convolution.
Exact t-derivatives: dC/dt = 2b^6 sum ff 2 D D1,  d2C/dt2 = 2b^6 sum ff (2 D1^2 + 2 D D2),
D1 = N^3 ifftn(-k^ d), D2 = N^3 ifftn(k^2 d).
t values: 0, 0.05, 0.1, 0.2 (requested) plus 0.5, 1, 2, 3 (to resolve the asymptotic decay rate).

PREDICATES (fixed before first run). Counts reported as met / failed / measured only.
 P1 (S1): r_N = C_{b}(0)/C_{2b}(0) at the two finest doublings (N=64/32, 128/64) lies in [24, 40]
     (interval given by the director's brief) and |r_128 - 32| < |r_64 - 32| (approaching 32).
     Fitted exponent p = log2(r) reported (measured only).  Per R.
 P2 (S2): for each t in {0.05, 0.1, 0.2}: with d1=|C32-C16|, d2=|C64-C32|, d3=|C128-C64|,
     d1/d2 and d2/d3 in [2, 8] (brief's interval; O(b^2) predicts 4).
     Agreement with continuum (child) value: |C_128 - C_cont| <= tol, tol = |C128 - C64| + child's own
     convergence uncertainty. Origin: for O(b^2) Richardson the remaining error of C128 is ~ d3/3; tol = 3x that.
     (Comparison done in compare.py after the child returns.)
 P3 (S3): tau in {0.05, 0.1}: M0=C(2tau), M1=-C'(2tau), M2=C''(2tau) exact.
     P3a: tau*M1/M0 <= C(tau)/(e C(2tau))       (S5(a) divided by M0)
     P3b: tau^2*M2/M0 <= 4 C(tau)/(e^2 C(2tau))  (S5(b) divided by M0)   -- all N.
     P3c: convergence: relative change of tau*M1/M0 and tau^2*M2/M0 between N=64 and 128 < 2 %.
          Tolerance origin: own expectation, O(b^2) with (pi b)^2 ~ 6e-4 times an O(10) constant from
          the dominant momenta ~ 1/tau; 2 % is a loose bound. Also the N=128 values of M0, M1, M2 are positive.
 P4 (S4): rate(t) = -C'(t)/C(t). Lowest two-photon energy in the box Emin = 2 k^(2pi,0,0) = 4 N sin(pi/N).
     P4a: rate(3) >= Emin (log-convexity of a positive atom sum: rate decreases toward lowest atom).
     P4b: rate(3)/Emin - 1 < 0.05 (own expectation: next level 2pi(1+sqrt2) is 2.6 higher; e^{-2.6*3} ~ 4e-4
          times a weight ratio of O(10-100)).
     P4c (literal S4 wording "lowest atom at or above 2*(2pi/ell)"): Emin >= 4 pi. Expected to FAIL by
          O(b^2) from below (sin x < x); recorded as measured with the sign of the deviation.
     rate(0.2) compared with 4pi: measured only.
Exit code: 0 always if the computation completes (predicate verdicts are in the result file); the PCP check
uses expect-exit 0. Result file never overwritten (results_bench_<k>.txt).
"""
import os, sys, json
import numpy as np

ell = 1.0
NS = [16, 32, 64, 128]
RS = [0.1, 0.05]
TS = [0.0, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0]

def fgrid(N, R):
    b = ell / N
    x = np.arange(N) * b
    g1 = np.zeros(N)
    for n in (-1, 0, 1):
        g1 += np.exp(-(x - 0.5 - n)**2 / (2 * R**2))
    # the 3D Gaussian sum over n in {-1,0,1}^3 factorizes exactly into a product of 1D sums
    return g1[:, None, None] * g1[None, :, None] * g1[None, None, :]

def compute(N, R):
    b = ell / N
    m = np.fft.fftfreq(N) * N
    kh = (2 / b) * np.sin(np.pi * m / N)
    K1, K2, K3 = np.meshgrid(kh, kh, kh, indexing='ij')
    k2 = K1**2 + K2**2 + K3**2
    khat = np.sqrt(k2)
    proj = np.zeros_like(k2); nz = k2 > 0
    proj[nz] = (K1[nz]**2 + K2[nz]**2) / k2[nz]
    f = fgrid(N, R)
    Ff = np.fft.fftn(f)
    def ffsum(G):
        return float(np.sum(f * np.real(np.fft.ifftn(np.fft.fftn(G) * Ff))))
    out = {}
    for t in TS:
        d = proj * khat / 2 * np.exp(-t * khat) / ell**3
        D = np.real(np.fft.ifftn(d)) * N**3
        D1 = np.real(np.fft.ifftn(-khat * d)) * N**3
        D2 = np.real(np.fft.ifftn(k2 * d)) * N**3
        C = 2 * b**6 * ffsum(D * D)
        dC = 2 * b**6 * ffsum(2 * D * D1)
        d2C = 2 * b**6 * ffsum(2 * D1 * D1 + 2 * D * D2)
        out[t] = (C, dC, d2C)
    return out

def main():
    lines = []; tally = {"met": 0, "failed": 0, "measured": 0}
    def P(name, cond, text):
        tally["met" if cond else "failed"] += 1
        lines.append(f"{name}: {'MET' if cond else 'FAILED'}  {text}")
    def M(text):
        tally["measured"] += 1; lines.append("measured: " + text)
    data = {}
    for R in RS:
        for N in NS:
            data[(R, N)] = compute(N, R)
            print("done", R, N, flush=True)
    raw = {f"R={R},N={N}": {str(t): v for t, v in data[(R, N)].items()} for (R, N) in data}
    for R in RS:
        lines.append(f"\n===== R = {R} =====")
        lines.append("C_b(t):  N | " + " | ".join(f"t={t}" for t in TS))
        for N in NS:
            lines.append(f"  {N:4d} | " + " | ".join(f"{data[(R,N)][t][0]:.10e}" for t in TS))
        # P1
        C0 = [data[(R, N)][0.0][0] for N in NS]
        r = [C0[i + 1] / C0[i] for i in range(3)]
        lines.append("C_b(0)*b^5: " + ", ".join(f"N={N}: {C0[i]*(1/N)**5:.8e}" for i, N in enumerate(NS)))
        lines.append("ratios C_b(0)/C_2b(0): " + ", ".join(f"{x:.5f}" for x in r) + "  exponents: " + ", ".join(f"{np.log2(x):.5f}" for x in r))
        P(f"P1 R={R}", all(24 <= x <= 40 for x in r[1:]) and abs(r[2] - 32) < abs(r[1] - 32),
          f"r(64/32)={r[1]:.5f}, r(128/64)={r[2]:.5f}")
        p = np.polyfit(np.log([1 / N for N in NS[1:]]), np.log(C0[1:]), 1)[0]
        M(f"R={R} fitted exponent of C_b(0) in b over N=32..128: {p:.5f} (S1 says -5); log2 ratio finest {np.log2(r[2]):.5f}")
        # P2
        for t in [0.05, 0.1, 0.2]:
            C = [data[(R, N)][t][0] for N in NS]
            dd = [abs(C[i + 1] - C[i]) for i in range(3)]
            q = [dd[0] / dd[1], dd[1] / dd[2]]
            P(f"P2 R={R} t={t}", all(2 <= x <= 8 for x in q),
              f"C128={C[3]:.10e}, diffs={dd[0]:.3e},{dd[1]:.3e},{dd[2]:.3e}, ratios={q[0]:.3f},{q[1]:.3f}; "
              f"Richardson C*={C[3]+(C[3]-C[2])/3:.10e}, tol(|C128-C64|)={dd[2]:.3e}")
        # P3
        for tau in [0.05, 0.1]:
            a_l, b_l = [], []
            for N in NS:
                C_t, _, _ = data[(R, N)][tau]
                M0, dC, d2C = data[(R, N)][2 * tau]
                M1, M2 = -dC, d2C
                a, bb = tau * M1 / M0, tau**2 * M2 / M0
                ba, bbnd = C_t / (np.e * M0), 4 * C_t / (np.e**2 * M0)
                a_l.append(a); b_l.append(bb)
                P(f"P3a R={R} tau={tau} N={N}", a <= ba, f"tau*M1/M0={a:.6f} <= C(tau)/(e C(2tau))={ba:.6f}")
                P(f"P3b R={R} tau={tau} N={N}", bb <= bbnd, f"tau^2*M2/M0={bb:.6f} <= 4C(tau)/(e^2 C(2tau))={bbnd:.6f}")
            ra, rb = abs(a_l[3] / a_l[2] - 1), abs(b_l[3] / b_l[2] - 1)
            M0s = data[(R, 128)][2 * tau]
            P(f"P3c R={R} tau={tau}", ra < 0.02 and rb < 0.02 and M0s[0] > 0 and -M0s[1] > 0 and M0s[2] > 0,
              f"tau*M1/M0 by N: {', '.join(f'{x:.6f}' for x in a_l)}; tau^2*M2/M0: {', '.join(f'{x:.6f}' for x in b_l)}; rel change 64->128: {ra:.2e}, {rb:.2e}")
        # P4
        for N in NS:
            rates = {t: -data[(R, N)][t][1] / data[(R, N)][t][0] for t in TS if t > 0}
            Emin = 4 * N * np.sin(np.pi / N)
            lines.append(f"N={N}: Emin=4N sin(pi/N)={Emin:.8f} (4pi={4*np.pi:.8f}, rel {Emin/(4*np.pi)-1:+.3e}); rates: " +
                         ", ".join(f"t={t}:{v:.5f}" for t, v in rates.items()))
            if N == 128:
                P(f"P4a R={R} N=128", rates[3.0] >= Emin, f"rate(3)={rates[3.0]:.6f} >= Emin={Emin:.6f}")
                P(f"P4b R={R} N=128", rates[3.0] / Emin - 1 < 0.05, f"rate(3)/Emin-1={rates[3.0]/Emin-1:.3e}")
                M(f"R={R} N=128 rate(0.2)={rates[0.2]:.4f} vs 4pi={4*np.pi:.4f} (ratio {rates[0.2]/(4*np.pi):.3f})")
        Emins = [4 * N * np.sin(np.pi / N) for N in NS]
        P(f"P4c R={R} (literal S4: Emin >= 4pi)", all(E >= 4 * np.pi for E in Emins),
          "Emin/4pi-1 = " + ", ".join(f"{E/(4*np.pi)-1:+.3e}" for E in Emins) + "  (-(pi b)^2/6 predicted)")
    # B2 scaling
    lines.append("\n===== B2 scaling R=0.1 vs R=0.05 =====")
    for N in NS:
        lines.append(f"N={N}: C0 b^5 ratio R.1/R.05 = {data[(0.1,N)][0.0][0]/data[(0.05,N)][0.0][0]:.5f} (int f^2 ratio = 8)")
    for (t1, t2) in [(0.1, 0.05), (0.2, 0.1)]:
        rr = data[(0.05, 128)][t2][0] / data[(0.1, 128)][t1][0]
        M(f"N=128: C_R=.05(t={t2}) / C_R=.1(t={t1}) = {rr:.5f} (pure dimensional scaling R^-2 would give 4; ell fixed breaks it)")
    for t in [0.05, 0.1, 0.2]:
        rr = data[(0.1, 128)][t][0] / data[(0.05, 128)][t][0]
        M(f"N=128 same t={t}: C_R=.1/C_R=.05 = {rr:.5f}")
    lines.append(f"\nTALLY: met {tally['met']}, failed {tally['failed']}, measured only {tally['measured']}")
    text = "\n".join(lines)
    print(text)
    k = 1
    while os.path.exists(f"results_bench_{k}.txt"):
        k += 1
    open(f"results_bench_{k}.txt", "w").write(text + "\n")
    json.dump(raw, open(f"results_bench_{k}.json", "w"), indent=1)
    print("written", f"results_bench_{k}.txt")
    return 0

if __name__ == "__main__":
    sys.exit(main())
