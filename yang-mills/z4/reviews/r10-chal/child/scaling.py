"""Scaling test of C_b(t) and claimed bounds V, v in the side length ell.

PREDICATES (fixed before first run):
 P1: For each N in {6,9,12}, tau-fraction s in {0.05,0.1,0.3}, and lambda = ell/1 for
     ell in {0.5, 2}: C_b(s*ell) computed for f_ell equals lambda^-2 * C_b(s*1) for f_1,
     and likewise for C_b(2 s ell); relative tolerance 1e-10.
 P2: V(tau) and v(tau) (and b0/ell) scale exactly as lambda^-2 (b0 as lambda);
     relative tolerance 1e-12.
 P3: In every case (ell,N,tau) with b <= b0: v(tau) <= C_b(2 tau) and C_b(tau) <= V(tau).
     Cases with b > b0 are reported as measured-only (no pass/fail).
No randomness is used (deterministic; seed fixed to 0 anyway).
Result file: results_runK.json with the first K not yet present (never overwritten).
"""
import json, os, sys
import numpy as np

np.random.seed(0)
S4 = 16.5791
ELLS = [0.5, 1.0, 2.0]
NS = [6, 9, 12]
SFRAC = [0.05, 0.1, 0.3]


def g(u1, u2, u3):
    tp = 2 * np.pi
    return np.exp(np.sin(tp * u1 + 0.3) + 0.7 * np.cos(tp * u2) * np.sin(tp * u3 + 1)
                  + 0.4 * np.sin(tp * (u1 + 2 * u2)))


def unit_integrals(M):
    """Return (int g, int |g|, int |Lap_u^2 g|) over the unit cube, M^3 grid, spectral."""
    u = np.arange(M) / M
    U1, U2, U3 = np.meshgrid(u, u, u, indexing="ij")
    G = g(U1, U2, U3)
    q = 2 * np.pi * np.fft.fftfreq(M, d=1.0 / M)
    Q1, Q2, Q3 = np.meshgrid(q, q, q, indexing="ij")
    lap2 = np.real(np.fft.ifftn((Q1**2 + Q2**2 + Q3**2) ** 2 * np.fft.fftn(G)))
    return G.mean(), np.abs(G).mean(), np.abs(lap2).mean()


def Cb(ell, N, t):
    b = ell / N
    n = np.arange(N)
    k1d = 2 * np.pi * n / ell
    kh1 = (2 / b) * np.sin(k1d * b / 2)
    K1, K2, K3 = np.meshgrid(kh1, kh1, kh1, indexing="ij")
    kh2 = K1**2 + K2**2 + K3**2
    kh = np.sqrt(kh2)
    W = np.zeros_like(kh)
    m = kh2 > 0
    W[m] = (K1[m]**2 + K2[m]**2) / kh2[m] * kh[m] / 2 * np.exp(-t * kh[m])
    # D(b x) = ell^-3 sum_k exp(2 pi i n.x/N) W(k) = ell^-3 N^3 ifftn(W)
    D = np.fft.ifftn(W) * N**3 / ell**3
    assert np.max(np.abs(D.imag)) < 1e-9 * np.max(np.abs(D.real))
    D2 = (D.real) ** 2
    u = n / N
    U1, U2, U3 = np.meshgrid(u, u, u, indexing="ij")
    f = g(U1, U2, U3).ravel()  # f_ell(b x) = g(x/N)
    X = np.stack(np.meshgrid(n, n, n, indexing="ij"), -1).reshape(-1, 3)
    diff = (X[:, None, :] - X[None, :, :]) % N
    D2xy = D2[diff[..., 0], diff[..., 1], diff[..., 2]]
    return 2 * b**6 * float(f @ D2xy @ f)


def Gfun(a):
    return 4 * np.pi * np.exp(np.sqrt(3) * a / 2) * (6 / a**4 + np.sqrt(3) / a**3)


def main():
    I96 = unit_integrals(96)
    I64 = unit_integrals(64)
    I128 = unit_integrals(128)
    rows = []
    for ell in ELLS:
        intf = ell**3 * I96[0]
        L1 = ell**3 * I96[1]
        D4 = I96[2] / ell  # ell^3 * ell^-4 * mean|Lap_u^2 g|
        b0 = min(ell / 3, 2 * np.pi * (abs(intf) / (2 * S4 * D4)) ** 0.25)
        F = L1 + S4 * (b0 / np.pi) ** 4 * D4
        k3 = 3 * np.sqrt(3) / ell
        mfun = lambda t: min(k3**2 * np.exp(-2 * t * k3), (2 * np.pi / ell) ** 2 * np.exp(-4 * np.pi * t / ell))
        for N in NS:
            b = ell / N
            for s in SFRAC:
                tau = s * ell
                C1 = Cb(ell, N, tau)
                C2 = Cb(ell, N, 2 * tau)
                V = 2 / ell**6 * F**2 * (np.pi / ell) ** 2 * Gfun(4 * tau / ell) ** 2
                v = 2 / ell**6 * intf**2 / 4 * mfun(2 * tau)
                rows.append(dict(ell=ell, N=N, s=s, tau=tau, b=b, b0=b0, qualifies=bool(b <= b0),
                                 C_tau=C1, C_2tau=C2, V=V, v=v,
                                 lower_ok=bool(v <= C2), upper_ok=bool(C1 <= V),
                                 F=F, intf=intf, L1=L1, D4=D4))
    # P1, P2
    base = {(r["N"], r["s"]): r for r in rows if r["ell"] == 1.0}
    p1_fail, p2_fail, p1_maxrel, p2_maxrel = 0, 0, 0.0, 0.0
    for r in rows:
        if r["ell"] == 1.0:
            continue
        lam = r["ell"]
        r0 = base[(r["N"], r["s"])]
        for key in ["C_tau", "C_2tau"]:
            rel = abs(r[key] - lam**-2 * r0[key]) / abs(lam**-2 * r0[key])
            p1_maxrel = max(p1_maxrel, rel)
            p1_fail += rel > 1e-10
        for key, p in [("V", -2), ("v", -2), ("b0", 1)]:
            rel = abs(r[key] - lam**p * r0[key]) / abs(lam**p * r0[key])
            p2_maxrel = max(p2_maxrel, rel)
            p2_fail += rel > 1e-12
    q = [r for r in rows if r["qualifies"]]
    p3_fail = sum((not r["lower_ok"]) or (not r["upper_ok"]) for r in q)
    out = dict(
        unit_integrals={"M64": [float(x) for x in I64], "M96": [float(x) for x in I96], "M128": [float(x) for x in I128]},
        P1=dict(pass_=bool(p1_fail == 0), failures=int(p1_fail), max_rel=p1_maxrel),
        P2=dict(pass_=bool(p2_fail == 0), failures=int(p2_fail), max_rel=p2_maxrel),
        P3=dict(qualifying=len(q), failures=int(p3_fail), pass_=bool(p3_fail == 0),
                nonqualifying=len(rows) - len(q)),
        rows=rows)
    k = 1
    while os.path.exists(f"results_run{k}.json"):
        k += 1
    with open(f"results_run{k}.json", "x") as fh:
        json.dump(out, fh, indent=1)
    print(f"wrote results_run{k}.json")
    print("P1", out["P1"]); print("P2", out["P2"]); print("P3", out["P3"])
    print("unit integrals M64/96/128:", I64, I96, I128)
    for r in rows:
        print(f"ell={r['ell']:<4} N={r['N']:<3} tau={r['tau']:.3f} b={r['b']:.4f} b0={r['b0']:.4f} "
              f"C(tau)={r['C_tau']:.6e} V={r['V']:.4e} C(2tau)={r['C_2tau']:.6e} v={r['v']:.4e} "
              f"q={r['qualifies']} lo={r['lower_ok']} up={r['upper_ok']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
