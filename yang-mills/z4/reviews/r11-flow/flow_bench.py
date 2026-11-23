"""
flow_bench.py  (r11-flow, Part A4).  Free lattice Maxwell, spatially flowed B_3, sharp time.

Conventions (flow_proof.md section 1): lattice flow dA/ds = -(1/b^2) C^T C A (C = lattice curl on
links -> plaquettes), i.e. the gradient flow of (1/2) sum theta_p^2 with lattice flow time s/b^2.
On transverse modes A_s(k) = exp(-s khat^2) A(k); B^s = exp(-s khat^2) B; two-point function
carries exp(-2 s khat^2).  u(k) = w(k) exp(-2 s khat^2), w(k) = P33(k) khat/2  (H1 of the r9 proof).
Var_b = (2/l^6) sum_q |fhat_b(q)|^2 (u*u)(q);  M1 = (2/l^6) sum_q |fhat|^2 2 (u*(u khat))(q);
M2 = (2/l^6) sum_q |fhat|^2 [2 (u*(u khat^2)) + 2 ((u khat)*(u khat))](q).   <B_s^2> = l^-3 sum_k u(k).
Case: l = 1, f = periodized Gaussian of width R = 0.1 (peak 1), s in {0.002, 0.005, 0.01},
N in {16, 24, 32, 48, 64, 96}.  The theorems' constants are evaluated for b <= b0 = 1/16.

PREDICATES (fixed before the first run):
 P0a  momentum formula for Var equals the position-space Wick sum 2 b^6 sum f f (D^s)^2, N = 8,
      each s: rel. err <= 1e-10 (tolerance: double-precision roundoff over 8^6 terms ~1e-13, margin 1e3).
 P0b  flow-factor derivation: on N = 4, random links A, flowing A by exp(-(s/b^2) C^T C) and taking
      theta_12 equals multiplying the Fourier modes of theta_12 by exp(-s khat^2): max abs err <= 1e-10
      (roundoff, matrix exponential of a 192x192 symmetric matrix).
 P1   v0 <= Var_b <= V0 for every s, N (theorem 1).                                      [18 cases]
 P2   M1 <= M1up and M2 <= M2up for every s, N (theorem 2).                              [18 cases]
 P3   B2low <= <B_s^2> <= B2up for every s, N (theorem 3).                               [18 cases]
 P4   convergence: |X_96 - X_64| / |X_96| <= 3 * b_64^2 / (6 s) for X in {Var, M1, M2, <B^2>}
      (tolerance: lattice dispersion khat^2 = k^2 - b^2 sum k_i^4 /12 + ...; at the flow scale
      k^2 ~ 1/s the relative change of the exponent 2 s khat^2 is ~ b^2/(6 s); margin 3).  [12 cases]
 P5   <B_s^2>: Richardson (N = 64, 96, error ~ b^2) agrees with 1/(48 pi^2 s^2) within 1%
      (finite-volume images are ~exp(-l^2/(8 s)) <= e^-12; remainder b^4/s^2 <= 0.3%).  [3 cases]
 P6   negative control s = 0: local exponent d log Var / d log b between N = 48 and 96 within
      0.05 of -5 (S1': ratios per halving 32.31, 32.08, 32.02 reported).                 [1 case]
 P7   window: E* = 2 M1up / v0 is finite and the exact spectral weight of the N = 16 vector in
      [0, E*] is >= v0 / 2 (double sum over pairs k, k').                               [3 cases]
 Measured only: limits (Richardson), looseness ratios V0/Var, Var/v0, M1up/M1, M2up/M2, B2up/B,
      B/B2low, ratio of Var to the asymptotic (sqrt(pi)/(640 pi^2)) int f^2 s^-5/2.
"""
import json, os, sys, math
import numpy as np
from math import gamma, pi, e, sqrt

L = 1.0; R = 0.1
SS = [0.002, 0.005, 0.01]
NS = [16, 24, 32, 48, 64, 96]
A_int = (2 * pi) ** 1.5 * R ** 3          # int f
A2_int = pi ** 1.5 * R ** 3               # int f^2
N0 = 16                                    # b0 = 1/16

def fgrid(N):
    b = L / N
    x = np.arange(N) * b
    g1 = sum(np.exp(-(x - 0.5 * L - m * L) ** 2 / (2 * R * R)) for m in (-2, -1, 0, 1, 2))
    return np.einsum('i,j,k->ijk', g1, g1, g1)

def khat_arrays(N):
    b = L / N
    n = np.fft.fftfreq(N, d=1.0 / N)       # -N/2 .. N/2-1 : each mode once (review note 1)
    k = 2 * pi * n / L
    kh = (2 / b) * np.sin(k * b / 2)
    K1, K2, K3 = np.meshgrid(kh, kh, kh, indexing='ij')
    kh2 = K1 ** 2 + K2 ** 2 + K3 ** 2
    return K1, K2, K3, kh2

def u_arrays(N, s):
    K1, K2, K3, kh2 = khat_arrays(N)
    kh = np.sqrt(kh2)
    with np.errstate(invalid='ignore', divide='ignore'):
        P33 = np.where(kh2 > 0, (K1 ** 2 + K2 ** 2) / np.where(kh2 > 0, kh2, 1), 0.0)
    w = P33 * kh / 2
    u = w * np.exp(-2 * s * kh2)
    u[0, 0, 0] = 0.0
    return u, kh

def conv(a, c):
    return np.real(np.fft.ifftn(np.fft.fftn(a) * np.fft.fftn(c)))

def observables(N, s):
    b = L / N
    f = fgrid(N)
    # fhat_b(q) = b^3 sum_x f(bx) e^{-i q b x}; |.|^2 is all that is needed
    fh2 = np.abs(b ** 3 * np.fft.fftn(f)) ** 2
    u, kh = u_arrays(N, s)
    # (u*u)(q) = sum_k u(k) u(q-k): cyclic convolution on the momentum grid
    uu = conv(u, u); uuk = conv(u, u * kh); uuk2 = conv(u, u * kh ** 2); ukuk = conv(u * kh, u * kh)
    pre = 2 / L ** 6
    Var = pre * np.sum(fh2 * uu)
    M1 = pre * np.sum(fh2 * 2 * uuk)
    M2 = pre * np.sum(fh2 * (2 * uuk2 + 2 * ukuk))
    B2 = np.sum(u) / L ** 3
    Pb = b ** 3 * np.sum(f ** 2)
    fh0 = b ** 3 * np.sum(f)
    return dict(Var=Var, M1=M1, M2=M2, B2=B2, P=Pb, fhat0=fh0)

def var_position(N, s):
    b = L / N
    f = fgrid(N).ravel()
    u, kh = u_arrays(N, s)
    D = np.real(np.fft.ifftn(u)) * N ** 3 / L ** 3   # D(r) = l^-3 sum_k e^{ik r} u(k)
    idx = np.array(np.unravel_index(np.arange(N ** 3), (N, N, N))).T
    tot = 0.0
    for i in range(N ** 3):
        d = (idx - idx[i]) % N
        tot += f[i] * np.sum(f * D[d[:, 0], d[:, 1], d[:, 2]] ** 2)
    return 2 * b ** 6 * tot

def flow_factor_check(N=4, s=0.003, seed=11):
    b = L / N
    rng = np.random.default_rng(seed)
    nl = 3 * N ** 3
    def lid(x, i): return i * N ** 3 + ((x[0] % N) * N + (x[1] % N)) * N + (x[2] % N)
    def pid(x, p): return p * N ** 3 + ((x[0] % N) * N + (x[1] % N)) * N + (x[2] % N)
    pairs = [(0, 1), (1, 2), (0, 2)]
    C = np.zeros((3 * N ** 3, nl))
    for x0 in range(N):
        for x1 in range(N):
            for x2 in range(N):
                x = np.array([x0, x1, x2])
                for p, (i, j) in enumerate(pairs):
                    ei = np.eye(3, dtype=int)[i]; ej = np.eye(3, dtype=int)[j]
                    r = pid(x, p)
                    C[r, lid(x, i)] += 1; C[r, lid(x + ei, j)] += 1
                    C[r, lid(x + ej, i)] -= 1; C[r, lid(x, j)] -= 1
    Lap = C.T @ C
    ev, V = np.linalg.eigh(Lap)
    A = rng.normal(size=nl)
    As = V @ (np.exp(-(s / b ** 2) * ev) * (V.T @ A))
    th12_flow = (C @ As)[:N ** 3].reshape(N, N, N)
    th12 = (C @ A)[:N ** 3].reshape(N, N, N)
    _, _, _, kh2 = khat_arrays(N)
    th12_mult = np.real(np.fft.ifftn(np.fft.fftn(th12) * np.exp(-s * kh2)))
    return float(np.max(np.abs(th12_flow - th12_mult)))

# ---------- proved constants (flow_proof.md) ----------
def theta(a): return 1 + sqrt(pi / a)
def Tm(m, a): return gamma(m + 0.5) / a ** (m + 0.5) + 2 * (m / (e * a)) ** m
def sum_khat2m(m, c):
    """bound for sum_{k in BZ} khat^{2m} exp(-c khat^2), m >= 1 (Lemma 2)."""
    a = 16 * c / L ** 2
    return 3 ** m * (2 * pi / L) ** (2 * m) * Tm(m, a) * theta(a) ** 2
def Uj(j, s): return 0.25 * sum_khat2m(j + 1, 4 * s)
def Pbound():
    th = sum(math.exp(-pi ** 2 * R ** 2 * N0 ** 2 * m * m) for m in range(-6, 7))
    return A2_int * th ** 3
def constants(s):
    P = Pbound()
    U0, U1, U2 = Uj(0, s), Uj(1, s), Uj(2, s)
    V0 = 2 / L ** 3 * P * U0
    M1up = 2 / L ** 3 * P * 2 * sqrt(U0 * U1)
    M2up = 2 / L ** 3 * P * (2 * sqrt(U0 * U2) + 2 * U1)
    k3 = 3 * sqrt(3) / L; k2p = 2 * pi / L
    mlow = min(k3 ** 2 * math.exp(-4 * s * k3 ** 2), k2p ** 2 * math.exp(-4 * s * k2p ** 2))
    v0 = 2 / L ** 6 * A_int ** 2 * mlow
    c = 2 * s; a = 16 * c / L ** 2
    B2up = 0.5 / L ** 3 * sqrt(sum_khat2m(1, c) * (theta(a) ** 3 - 1))
    M = N0 // 2 - 1
    n = np.arange(-M, M + 1); k = 2 * pi * n / L
    K1, K2, K3 = np.meshgrid(k, k, k, indexing='ij'); kk = np.sqrt(K1 ** 2 + K2 ** 2 + K3 ** 2)
    with np.errstate(invalid='ignore', divide='ignore'):
        h = np.where(kk > 0, (4 / pi ** 3) * (K1 ** 2 + K2 ** 2) / np.where(kk > 0, kk, 1) * np.exp(-2 * s * kk ** 2), 0)
    B2low = float(np.sum(h)) / L ** 3
    return dict(v0=v0, V0=V0, M1up=M1up, M2up=M2up, B2low=B2low, B2up=B2up, Estar=2 * M1up / v0)

def window_weight(N, s, Estar):
    b = L / N
    f = fgrid(N)
    fh = b ** 3 * np.fft.fftn(f)
    u, kh = u_arrays(N, s)
    uf = u.ravel(); kf = kh.ravel()
    n = np.fft.fftfreq(N, d=1.0 / N).astype(int) % N
    I = np.array(np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')).reshape(3, -1)
    tot = 0.0; inside = 0.0
    fh2 = np.abs(fh) ** 2
    for a in range(N ** 3):
        if uf[a] == 0: continue
        q = (I + I[:, a:a + 1]) % N
        W = 2 / L ** 6 * fh2[q[0], q[1], q[2]] * uf[a] * uf
        E = kf[a] + kf
        tot += W.sum(); inside += W[E <= Estar].sum()
    return tot, inside

def main():
    run = sys.argv[1] if len(sys.argv) > 1 else 'run1'
    out = f'results_flow_{run}.json'
    if os.path.exists(out):
        print('refusing to overwrite', out); sys.exit(3)
    res = dict(cases={}, preds={}); met = failed = 0
    def pred(name, ok, info):
        nonlocal met, failed
        res['preds'][name] = dict(ok=bool(ok), info=info)
        if ok: met += 1
        else: failed += 1
        print(('MET   ' if ok else 'FAILED'), name, info)
    for s in SS:
        mom = observables(8, s)['Var']; pos = var_position(8, s)
        pred(f'P0a s={s}', abs(mom - pos) / abs(pos) <= 1e-10, f'rel={abs(mom-pos)/abs(pos):.2e}')
    err = flow_factor_check()
    pred('P0b', err <= 1e-10, f'maxerr={err:.2e}')
    for s in SS:
        c = constants(s); res['cases'][str(s)] = dict(constants=c, N={})
        for N in NS:
            o = observables(N, s); res['cases'][str(s)]['N'][N] = o
            pred(f'P1 s={s} N={N}', c['v0'] <= o['Var'] <= c['V0'], f"v0={c['v0']:.3e} Var={o['Var']:.6e} V0={c['V0']:.3e}")
            pred(f'P2 s={s} N={N}', o['M1'] <= c['M1up'] and o['M2'] <= c['M2up'],
                 f"M1={o['M1']:.4e}<= {c['M1up']:.3e}; M2={o['M2']:.4e}<= {c['M2up']:.3e}")
            pred(f'P3 s={s} N={N}', c['B2low'] <= o['B2'] <= c['B2up'], f"{c['B2low']:.4e}<= {o['B2']:.6e} <= {c['B2up']:.4e}")
        d = res['cases'][str(s)]['N']
        tol = 3 * (L / 64) ** 2 / (6 * s)
        for X in ('Var', 'M1', 'M2', 'B2'):
            rel = abs(d[96][X] - d[64][X]) / abs(d[96][X])
            pred(f'P4 s={s} {X}', rel <= tol, f'rel={rel:.3e} tol={tol:.3e}')
        rich = {X: (96 ** 2 * d[96][X] - 64 ** 2 * d[64][X]) / (96 ** 2 - 64 ** 2) for X in ('Var', 'M1', 'M2', 'B2')}
        res['cases'][str(s)]['richardson'] = rich
        exact = 1 / (48 * pi ** 2 * s ** 2)
        pred(f'P5 s={s}', abs(rich['B2'] / exact - 1) <= 0.01, f"B2_rich={rich['B2']:.6e} 1/(48pi^2s^2)={exact:.6e} ratio={rich['B2']/exact:.5f}")
        asym = sqrt(pi) / (640 * pi ** 2) * A2_int * s ** -2.5
        res['cases'][str(s)]['measured'] = dict(
            V0_over_Var=c['V0'] / rich['Var'], Var_over_v0=rich['Var'] / c['v0'], M1up_over_M1=c['M1up'] / rich['M1'],
            M2up_over_M2=c['M2up'] / rich['M2'], B2up_over_B2=c['B2up'] / rich['B2'], B2_over_B2low=rich['B2'] / c['B2low'],
            Var_over_asym=rich['Var'] / asym, tau_M1_over_Var=rich['M1'] / rich['Var'], s2B2=rich['B2'] * s * s,
            Estar=c['Estar'], true_2M1_over_Var=2 * rich['M1'] / rich['Var'])
        print('measured', s, res['cases'][str(s)]['measured'])
        tot, inside = window_weight(16, s, c['Estar'])
        pred(f'P7 s={s}', math.isfinite(c['Estar']) and inside >= c['v0'] / 2,
             f"E*={c['Estar']:.4e} weight_in={inside:.4e} total={tot:.4e} v0/2={c['v0']/2:.3e}")
    # negative control s = 0
    v48 = observables(48, 0.0)['Var']; v96 = observables(96, 0.0)['Var']
    v24 = observables(24, 0.0)['Var']
    ex = math.log(v96 / v48) / math.log(48 / 96)
    res['negative_control'] = dict(V24=v24, V48=v48, V96=v96, exponent=ex, ratio_48_96=v96 / v48)
    pred('P6 s=0', abs(ex + 5) <= 0.05, f'exponent={ex:.4f} ratio={v96/v48:.3f}')
    res['counts'] = dict(met=met, failed=failed)
    with open(out, 'w') as fh:
        json.dump(res, fh, indent=1, default=float)
    print(f'counts met={met} failed={failed} -> {out}')
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
