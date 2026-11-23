#!/usr/bin/env python3
"""mc3.py -- Monte Carlo for the one-site SU(2) Wilson model with D spatial directions
(D = 3 main, D = 2 control) on a periodic time circle of T slices.

MODEL. Variables U_i(t) in SU(2) (quaternions u0 + i u.sigma), i=1..D, t=0..T-1, temporal links W(t).
  S = beta sum_t [ sum_{i<j} (1 - 1/2 Tr U_i U_j U_i^-1 U_j^-1)(t) + sum_i (1 - 1/2 Tr U_i(t) W(t) U_i(t+1)^-1 W(t)^-1) ].
TEMPORAL LINKS: kept, in the maximal-tree gauge W(t)=1 for t=0..T-2, W(T-1)=P dynamical (Haar).
  (exact: the gauge orbit of any configuration meets this gauge with trivial Faddeev-Popov factor).
  1/2 Tr U_i U_j U_i^-1 U_j^-1 = 1 - 2 |u_i x u_j|^2  (checked in PRE1).

ALGORITHM (one sweep): for each direction i and time parity p:
  (a) heat-bath proposal from the temporal-staple weight exp(beta * 1/2 Tr U A) (Kennedy-Pendleton),
      accepted with min(1, exp(-dS_spatial))   [independence Metropolis, exact detailed balance];
  (b) overrelaxation U -> V^-1 U^-1 V^-1 (V = A/|A|), which keeps the temporal part, accepted with
      min(1, exp(-dS_spatial));
  then 4 Metropolis hits on P (left multiplication, step tuned during thermalisation only), and one
  global "valley" move per direction: U_i(t) -> R U_i(t) for all t at once (R random near 1, step tuned
  during thermalisation only), accepted with the full dS. Steps are frozen after thermalisation.
  NCH independent chains (vectorised), fixed seed derived from (D, beta, T, seed argument).
  Errors: jackknife over the NCH independent chains (each chain = one block).

OPERATORS (per time slice; s_i = |u_i|^2 = 1-Q_i, Q_i=u0_i^2, d_ij = u_i.u_j, c_ij = s_i s_j - d_ij^2):
  all are invariant under simultaneous conjugation and under each center flip U_i -> -U_i (PRE3).
  A1 : sum s_i, sum_{i<j} c_ij, sum s_i^2, sum_{i<j} d_ij^2            (vacuum subtracted)
  E  : components (f_1-f_2)/sqrt2, (f_1+f_2-2f_3)/sqrt6 with
       D=3: f_i in { s_i, s_i^2, sum_{j!=i} d_ij^2, sum_{j!=i} c_ij }
       D=2: single component (f_1-f_2)/sqrt2, f_i in { s_i, s_i^2, s_i^3, s_i d_12^2 }
  T2 : components (ij), g1 = u0_i u0_j d_ij (odd under reflection U_i->U_i^-1 and U_j->U_j^-1, even under
       center flips), g2 = g1 (s_i+s_j), g3 = g1 * sum_{k!=i,j} s_k [D=2: g1 s_1 s_2],
       g4 = u0_i u0_j sum_{k!=i,j} d_ik d_kj [D=2: g1 d_12^2]
  Correlators averaged over the components of each channel.

ANALYSIS. GEVP per channel, operators normalised to unit C_aa(0), t0 = max(1, round(xi0/2)),
  xi0 = beta^(1/3)/3 (the brief's estimate); lowest level lambda(t); m_eff(t) = ln(lambda(t)/lambda(t+1)),
  jackknife over chains. t_max = last t with jackknife relative error of lambda(t+1) < 0.2 (consecutive from t0+1).

PREDICATES (fixed before the first run; tolerances and their origin stated):
  PRE1  1/2 Tr(U_i U_j U_i^-1 U_j^-1) == 1 - 2|u_i x u_j|^2 on 1000 random pairs, max |dev| <= 1e-12
        (float64 rounding of ~20 flops).
  PRE2  KP sampler at k = 3: sample mean of x0 (N=2e5) within 4 sigma (sigma = sd/sqrt N) of the
        quadrature value of int x sqrt(1-x^2) e^{kx} / int sqrt(1-x^2) e^{kx}  (4 sigma: Gaussian, 6e-5).
  PRE3  every operator is unchanged (<=1e-12) under each center flip and under a random global conjugation;
        E/T2 components: the channel-averaged correlator sum_c O_c O_c is unchanged under a random
        permutation and reflections of the directions (<=1e-12); the action is invariant under a reflection.
  PLAT  (per channel, per beta) plateau criterion: L = max(3, round(xi0)); t_a = smallest t >= t0+1 with
        t_a+L-1 <= t_max such that over the window [t_a, t_a+L-1] chi2/dof of a constant (diagonal jackknife
        errors) <= 1.5 and |m_eff(t_a) - m_eff(t_a+L-1)| <= 2 sigma (jackknife sigma of the difference).
        m = error-weighted mean of m_eff over that window (weights from the full sample), error = jackknife.
        If no window qualifies: PLAT failed; m is then reported (measured only) as m_eff(t0+1).
  TLEN  T * m_lowest >= 20 (brief: T >= 20 correlation lengths).
  THERM first-half vs second-half mean of the A1 operator sum s_i agree within 3 sigma (jackknife over chains).
  TAU   number of measurements per chain >= 50 tau_int for each of the three monitored series
        (slice-averaged sum s_i, E component 1 op 1, T2 (12) op 1); tau_int by Sokal windowing, c = 6.
  CTRL  (analyse3.py) D=3, beta = 1, 2, 4: |m_E - m_exact| <= 3 sigma, m_exact = 2.876117, 1.621505, 0.96893
        (3 sigma: Gaussian, 0.3% two-sided). D=2, beta=256: |min channel m * beta^(1/3) - 1.887| <= 3 sigma.
  LIM   (analyse3.py) at the largest beta run (4096): |m beta^(1/3) / e - 1| <= 0.08 with e = 3.012539 for E
        and T2 and e = 3.602838 for A1 (0.08 ~ 1.3 beta^-1/3: the brief's correction order beta^-1/3 with
        coefficient <= 1.3; in 2D the deviation at beta=512 was 0.028 = 0.22 beta^-1/3).
  MONO  (analyse3.py) for E and T2: m beta^(1/3) moves toward e from beta=64 to the largest beta
        (|dev| at largest beta < |dev| at 64 by more than 2 sigma combined). Measured only for A1.
  The E-T2 splitting is measured only.

USAGE: python3 mc3.py D BETA T NCH NTHERM NMEAS SEED OUTPREFIX
  writes OUTPREFIX.json and OUTPREFIX.npz (both mode "x"); exit 0 if PRE1-3 hold (run predicates are
  recorded in the JSON, not in the exit code), exit 3 if PRE1-3 fail.
"""
import sys, json, math, time
import numpy as np

SIGN = np.array([1.0, -1.0, -1.0, -1.0])


def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
                     a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2),
                     a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3),
                     a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1)], -1)


def qc(a):
    return a * SIGN


def haar(rng, shape):
    x = rng.standard_normal(shape + (4,))
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


def near1(rng, shape, eps):
    x = np.concatenate([np.ones(shape + (1,)), eps * rng.standard_normal(shape + (3,))], -1)
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


def kp_x0(k, rng):
    n = k.size
    x0 = np.empty(n)
    todo = np.arange(n)
    it = 0
    while todo.size:
        it += 1
        kk = k[todo]
        m = todo.size
        if it <= 30:
            r1 = 1.0 - rng.random(m); r2 = rng.random(m); r3 = 1.0 - rng.random(m); r4 = rng.random(m)
            lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * kk)
            acc = r4 * r4 <= 1.0 - lam2
            x0[todo[acc]] = 1.0 - 2.0 * lam2[acc]
        else:  # fallback for tiny k: Haar x0 accepted with exp(k(x-1))
            y = haar(rng, (m,))[:, 0]
            acc = rng.random(m) < np.exp(kk * (y - 1.0))
            x0[todo[acc]] = y[acc]
        todo = todo[~acc]
    return x0


def plaq_formula(ui, uj):
    cr = np.cross(ui[..., 1:], uj[..., 1:])
    return 1.0 - 2.0 * np.sum(cr * cr, -1)


def plaq_direct(Ui, Uj):
    return qmul(qmul(qmul(Ui, Uj), qc(Ui)), qc(Uj))[..., 0]


def operators(U):
    """U: (..., D, 4). returns dict channel -> array (..., ncomp, nop)."""
    D = U.shape[-2]
    u0 = U[..., 0]
    uv = U[..., 1:]
    s = np.sum(uv * uv, -1)                         # (..., D)
    d = np.einsum('...ia,...ja->...ij', uv, uv)     # (..., D, D)
    c = s[..., :, None] * s[..., None, :] - d * d
    pairs = [(i, j) for i in range(D) for j in range(i + 1, D)]
    A1 = np.stack([s.sum(-1),
                   sum(c[..., i, j] for i, j in pairs),
                   (s * s).sum(-1),
                   sum(d[..., i, j] ** 2 for i, j in pairs)], -1)[..., None, :]
    if D == 3:
        dd = d * d
        offd = dd.sum(-1) - np.einsum('...ii->...i', dd)
        coff = c.sum(-1) - np.einsum('...ii->...i', c)
        f = np.stack([s, s * s, offd, coff], -1)    # (..., D, nop)
        e1 = (f[..., 0, :] - f[..., 1, :]) / math.sqrt(2)
        e2 = (f[..., 0, :] + f[..., 1, :] - 2 * f[..., 2, :]) / math.sqrt(6)
        E = np.stack([e1, e2], -2)
        T2c = []
        for i, j in pairs:
            k = 3 - i - j
            g1 = u0[..., i] * u0[..., j] * d[..., i, j]
            T2c.append(np.stack([g1, g1 * (s[..., i] + s[..., j]), g1 * s[..., k],
                                 u0[..., i] * u0[..., j] * d[..., i, k] * d[..., k, j]], -1))
        T2 = np.stack(T2c, -2)
    else:
        d12 = d[..., 0, 1]
        f = np.stack([s, s * s, s ** 3, s * (d12 * d12)[..., None]], -1)
        E = ((f[..., 0, :] - f[..., 1, :]) / math.sqrt(2))[..., None, :]
        g1 = u0[..., 0] * u0[..., 1] * d12
        T2 = np.stack([g1, g1 * (s[..., 0] + s[..., 1]), g1 * s[..., 0] * s[..., 1], g1 * d12 * d12], -1)[..., None, :]
    return {'A1': A1, 'E': E, 'T2': T2}


def spatial_local(Ui, Uall, i, beta):
    """beta * sum_{j!=i} 2|u_i x u_j|^2 at the same slices. Ui (...,4), Uall (...,D,4)."""
    D = Uall.shape[-2]
    tot = 0.0
    for j in range(D):
        if j == i:
            continue
        cr = np.cross(Ui[..., 1:], Uall[..., j, 1:])
        tot = tot + np.sum(cr * cr, -1)
    return 2.0 * beta * tot


def action(U, P, beta):
    """total action per chain. U (R,T,D,4), P (R,4)."""
    R, T, D, _ = U.shape
    S = np.zeros(R)
    for i in range(D):
        for j in range(i + 1, D):
            S += beta * (1 - plaq_formula(U[:, :, i], U[:, :, j])).sum(1)
    W = np.zeros((R, T, 4)); W[..., 0] = 1.0; W[:, T - 1] = P
    for i in range(D):
        Un = np.roll(U[:, :, i], -1, axis=1)
        tr = qmul(qmul(qmul(U[:, :, i], W), qc(Un)), qc(W))[..., 0]
        S += beta * (1 - tr).sum(1)
    return S


def pretests(rng):
    res = {}
    A = haar(rng, (1000,)); B = haar(rng, (1000,))
    res['PRE1_maxdev'] = float(np.max(np.abs(plaq_formula(A, B) - plaq_direct(A, B))))
    res['PRE1'] = bool(res['PRE1_maxdev'] <= 1e-12)
    k = 3.0
    x = kp_x0(np.full(200000, k), rng)
    # quadrature in angle: x = cos th, sqrt(1-x^2)dx = sin^2 th dth
    th = np.linspace(0, np.pi, 200001)
    w = np.sin(th) ** 2 * np.exp(k * np.cos(th))
    exact = np.trapezoid(np.cos(th) * w, th) / np.trapezoid(w, th)
    sig = x.std() / math.sqrt(x.size)
    res['PRE2_mean'] = float(x.mean()); res['PRE2_exact'] = float(exact); res['PRE2_z'] = float((x.mean() - exact) / sig)
    res['PRE2'] = bool(abs(res['PRE2_z']) <= 4)
    ok = True; maxdev = 0.0
    for D in (2, 3):
        U = haar(rng, (5, D))
        ops = operators(U)
        for i in range(D):
            U2 = U.copy(); U2[:, i] *= -1
            o2 = operators(U2)
            for ch in ops:
                maxdev = max(maxdev, np.max(np.abs(o2[ch] - ops[ch])))
        g = haar(rng, (5, 1))
        o2 = operators(qmul(qmul(g, U), qc(g)))
        for ch in ops:
            maxdev = max(maxdev, np.max(np.abs(o2[ch] - ops[ch])))
        perm = rng.permutation(D)
        U3 = U[:, perm].copy()
        refl = rng.integers(0, 2, D)
        for i in range(D):
            if refl[i]:
                U3[:, i] = qc(U3[:, i])
        o3 = operators(U3)
        for ch in ops:
            sq = np.einsum('rca,rcb->rab', ops[ch], ops[ch]); sq3 = np.einsum('rca,rcb->rab', o3[ch], o3[ch])
            maxdev = max(maxdev, np.max(np.abs(sq - sq3)))
        # action invariance under reflection of direction 0 (with P -> P, needs U(t) -> U(t)^-1 everywhere)
        Uc = haar(rng, (2, 6, D)); Pc = haar(rng, (2,))
        Ur = Uc.copy(); Ur[:, :, 0] = qc(Ur[:, :, 0])
        maxdev = max(maxdev, np.max(np.abs(action(Uc, Pc, 1.3) - action(Ur, Pc, 1.3))))
    res['PRE3_maxdev'] = float(maxdev)
    res['PRE3'] = bool(maxdev <= 1e-12)
    return res


def tau_int(series, c=6.0):
    """series (R, N): autocorrelation averaged over chains; Sokal window."""
    x = series - series.mean(1, keepdims=True)
    N = x.shape[1]
    f = np.fft.rfft(x, n=2 * N, axis=1)
    ac = np.fft.irfft(f * np.conj(f), axis=1)[:, :N].mean(0)
    ac = ac / ac[0]
    tau = 0.5
    for W in range(1, N):
        tau += ac[W]
        if W >= c * tau:
            break
    return float(tau), int(W)


def main():
    D = int(sys.argv[1]); beta = float(sys.argv[2]); T = int(sys.argv[3]); NCH = int(sys.argv[4])
    NTH = int(sys.argv[5]); NME = int(sys.argv[6]); seed = int(sys.argv[7]); out = sys.argv[8]
    assert T % 2 == 0
    fj = open(out + '.json', 'x'); fz = open(out + '.npz', 'xb')
    rng = np.random.default_rng([seed, D, int(round(beta * 1000)), T])
    t_start = time.time()
    pre = pretests(rng)
    if not (pre['PRE1'] and pre['PRE2'] and pre['PRE3']):
        json.dump({'pre': pre}, fj, indent=1); fj.close(); fz.close(); sys.exit(3)

    U = np.zeros((NCH, T, D, 4)); U[..., 0] = 1.0
    P = np.zeros((NCH, 4)); P[:, 0] = 1.0
    epsP = 0.3; epsG = 0.3 * beta ** (-1.0 / 3) / math.sqrt(T)
    tidx = np.arange(T)
    stats = {'hb_acc': [0, 0], 'or_acc': [0, 0], 'P_acc': [0, 0], 'G_acc': [0, 0]}

    def link_update(i, p, overrelax):
        nonlocal U
        t = tidx[p::2]
        tp = (t + 1) % T; tm = (t - 1) % T
        Ui = U[:, t, i]
        Wt = np.zeros((NCH, t.size, 4)); Wt[..., 0] = 1.0
        Wm = Wt.copy()
        Wt[:, t == T - 1] = P[:, None]
        Wm[:, tm == T - 1] = P[:, None]
        B = qmul(qmul(Wt, qc(U[:, tp, i])), qc(Wt))
        C = qmul(qmul(qc(Wm), qc(U[:, tm, i])), Wm)
        A = B + C
        a = np.linalg.norm(A, axis=-1)
        a = np.maximum(a, 1e-300)
        V = A / a[..., None]
        if overrelax:
            Un = qmul(qmul(qc(V), qc(Ui)), qc(V))
            key = 'or_acc'
        else:
            x0 = kp_x0((beta * a).ravel(), rng).reshape(a.shape)
            n = rng.standard_normal(a.shape + (3,)); n /= np.linalg.norm(n, axis=-1, keepdims=True)
            X = np.concatenate([x0[..., None], np.sqrt(np.maximum(0, 1 - x0 * x0))[..., None] * n], -1)
            Un = qmul(X, qc(V))
            key = 'hb_acc'
        Uo = U[:, t]
        dS = spatial_local(Un, Uo, i, beta) - spatial_local(Ui, Uo, i, beta)
        acc = np.log(rng.random(dS.shape)) < -dS
        Unew = np.where(acc[..., None], Un, Ui)
        Un2 = Unew / np.linalg.norm(Unew, axis=-1, keepdims=True)
        U[:, t, i] = Un2
        stats[key][0] += int(acc.sum()); stats[key][1] += acc.size

    def ptrace():
        tot = np.zeros(NCH)
        for i in range(D):
            tot += qmul(qmul(qmul(U[:, T - 1, i], P), qc(U[:, 0, i])), qc(P))[..., 0]
        return tot

    def P_update(nhit):
        nonlocal P
        for _ in range(nhit):
            old = ptrace()
            Po = P.copy()
            P = qmul(near1(rng, (NCH,), epsP), P)
            new = ptrace()
            acc = np.log(rng.random(NCH)) < beta * (new - old)
            P = np.where(acc[:, None], P, Po)
            stats['P_acc'][0] += int(acc.sum()); stats['P_acc'][1] += NCH

    def global_move(i):
        nonlocal U
        S0 = action(U, P, beta)
        Uo = U[:, :, i].copy()
        Rm = near1(rng, (NCH,), epsG)
        U[:, :, i] = qmul(Rm[:, None], Uo)
        S1 = action(U, P, beta)
        acc = np.log(rng.random(NCH)) < -(S1 - S0)
        U[:, :, i] = np.where(acc[:, None, None], U[:, :, i], Uo)
        stats['G_acc'][0] += int(acc.sum()); stats['G_acc'][1] += NCH

    def sweep():
        for i in range(D):
            for p in (0, 1):
                link_update(i, p, False)
        for i in range(D):
            for p in (0, 1):
                link_update(i, p, True)
        P_update(4)
        for i in range(D):
            global_move(i)

    # thermalisation with step tuning (tuning stops at the end of thermalisation)
    for it in range(NTH):
        for k in ('P_acc', 'G_acc'):
            stats[k] = [0, 0]
        sweep()
        if it < NTH // 2:
            ra = stats['P_acc'][0] / max(1, stats['P_acc'][1])
            epsP *= 1.1 if ra > 0.5 else 0.9
            ga = stats['G_acc'][0] / max(1, stats['G_acc'][1])
            epsG *= 1.1 if ga > 0.5 else 0.9
            epsP = min(epsP, 3.0); epsG = min(epsG, 3.0)
    for k in stats:
        stats[k] = [0, 0]
    t_therm = time.time() - t_start

    TM = T // 2 + 1
    chans = ['A1', 'E', 'T2']
    acc_C = {}; acc_M = {}
    o0 = operators(U)
    for ch in chans:
        nc, nop = o0[ch].shape[-2:]
        acc_C[ch] = np.zeros((2, NCH, nop, nop, TM))
        acc_M[ch] = np.zeros((2, NCH, nc, nop))
    mon = np.zeros((3, NCH, NME))
    for m in range(NME):
        sweep()
        half = 0 if m < NME // 2 else 1
        ops = operators(U)  # (R,T,nc,nop)
        for ch in chans:
            O = ops[ch]
            Of = np.fft.rfft(O, axis=1)
            cr = np.fft.irfft(np.einsum('rwca,rwcb->rabw', np.conj(Of), Of), n=T, axis=-1)
            acc_C[ch][half] += cr[..., :TM] / (T * O.shape[2])
            acc_M[ch][half] += O.mean(1)
        mon[0, :, m] = ops['A1'][:, :, 0, 0].mean(1)
        mon[1, :, m] = ops['E'][:, :, 0, 0].mean(1)
        mon[2, :, m] = ops['T2'][:, :, 0, 0].mean(1)
    t_total = time.time() - t_start
    taus = [tau_int(mon[k]) for k in range(3)]
    res = {'D': D, 'beta': beta, 'T': T, 'NCH': NCH, 'NTHERM': NTH, 'NMEAS': NME, 'seed': seed,
           'pre': pre, 'epsP': epsP, 'epsG': epsG,
           'acc': {k: v[0] / max(1, v[1]) for k, v in stats.items()},
           'tau_int': {'sum_s': taus[0], 'E1': taus[1], 'T2_12': taus[2]},
           'time_therm_s': t_therm, 'time_total_s': t_total}
    res['TAU'] = bool(all(NME >= 50 * t[0] for t in taus))
    np.savez(fz, **{f'C_{ch}': acc_C[ch] for ch in chans}, **{f'M_{ch}': acc_M[ch] for ch in chans},
             mon=mon, nmeas=np.array([NME // 2, NME - NME // 2]))
    fz.close()
    json.dump(res, fj, indent=1); fj.close()
    print(json.dumps(res))


if __name__ == '__main__':
    main()
