#!/usr/bin/env python3
"""mcp.py -- l1-mcw (T123): copy of mcbox.py (k1-mc8) with added channels PS, PA, PE (scaled spatial plaquette
energy beta*sum_x(1-P) per slice: single plane / A1 sum / E) and per-measurement single spatial plaquette moments
sp1=<beta(1-P)>, sp2=<(beta(1-P))^2> (averaged over all spatial plaquettes of the lattice). Nothing else changed.

mcbox.py -- k1-mc8 (T117). SU(2) Wilson action on a periodic L^3 x T lattice, L in {1, 2}.

MODEL. S = beta * sum_{x, mu<nu} (1 - 1/2 Re Tr U_p(x; mu,nu)), all 6 orientations, every (site, mu<nu)
  a distinct plaquette (for L=2 the plaquettes based at x and at x+nu=x-nu are both counted, as the brief says).
  Links stored as unit quaternions (u0, u1, u2, u3) = u0 + i u.sigma, so 1/2 Tr U = u0. No gauge fixing.

ALGORITHM. One sweep =
  (a) one heat-bath pass (Kennedy-Pendleton) over all links, direction by direction, checkerboard parity
      (t+x+y+z) mod 2;
  (b) NOR overrelaxation passes U -> V^-1 U^-1 V^-1 (V = staple/|staple|);
  (c) if COLL=1: collective moves: for each spatial direction i and each slice c (x_i = c), every i-link on
      that slice (all t, all transverse positions) is multiplied on the left by M(x) = V(x)^-1 g V(x), where g is
      one random SU(2) element near 1 (g and g^-1 equally likely, conjugation-invariant density) per chain and
      V(x) = parallel transporter from the reference site (t=0, x_i=c, transverse 0) to x along time first,
      then j, then k (it uses no i-links, so the proposal is symmetric; in a maximal-tree gauge M = g, which is
      the brief's "common g").  Metropolis with the exact action change. NCOLL hits per (i,c). Step size
      tuned toward 50 % acceptance during the first half of thermalisation only, then frozen.
  For L = 2 the action is linear in each link, so (a),(b) are exact without accept/reject.
  For L = 1 (control c1) a spatial link appears twice in its own spatial plaquettes and a temporal link twice
  in its temporal plaquettes: spatial links use the heat-bath / overrelaxation proposal built from the
  temporal staple only (independent of the link) and are accepted with exp(-dS_spatial) (exact detailed
  balance: independence / involution proposal), temporal links use 4 Metropolis hits (step tuned in
  thermalisation) with the exact local dS.
  NCH independent chains, vectorised; fixed seed derived from (seed, L, beta, T, COLL).

OPERATORS (per time slice, averaged over the L^3 spatial sites = zero momentum):
  L_i(x) = product of the L links in direction i starting at x (winding loop); P_i = 1/2 Tr L_i; q_i = <P_i^2>_x.
  pl_i = average spatial plaquette in the plane perpendicular to i.  W+_ij, W-_ij = (1/2 Tr L_i L_j)^2,
  (1/2 Tr L_i L_j^-1)^2 at the same base site.
  E  (2 components (f1-f2)/sqrt2, (f1+f2-2f3)/sqrt6), f_i in { q_i, <P_i^4>, pl_i }
  T2 (3 components ij), g in { <W+_ij - W-_ij>, <(W+_ij - W-_ij)(P_i^2+P_j^2)>, <(W+_ij - W-_ij) P_k^2> }
  A1 { sum q_i, sum <P_i^4>, sum pl_i, sum_{i<j} <W+_ij + W-_ij> }
  Correlators C_ab(t) (vacuum subtracted per chain set in the analysis), summed over components / ncomp.

PRE-TESTS (exit 3 if any fails; tolerance 1e-11 = float64 rounding of ~1e3 flops):
  PRE1 every operator invariant under each of the 3L center flips (i-links on slice x_i=c times -1),
       and under a random gauge transformation;
  PRE2 channel-summed operator products sum_c O_c,a O_c,b invariant under a random permutation of the three
       axes and under a reflection x_1 -> -x_1 (U_1(x) -> U_1(Rx - e1)^-1); action invariant under both;
  PRE3 (L=2) heat-bath/overrelaxation consistency: the staple formula for dS equals the direct plaquette dS
       for a random update (<= 1e-10); KP sampler <x0> at k=3 within 4 sigma of quadrature (4 sigma: Gaussian).
  PRE4 collective-move transporter covariance: dS of a collective move is unchanged under a random gauge
       transformation of the configuration (with g conjugated by the gauge element at the reference site).

RUN PREDICATES (recorded in the JSON; analysis predicates are in analyse.py):
  THERM  first-half vs second-half chain-set means of the plaquette and of sum q_i agree within 3 sigma
         (jackknife over chains; 3 sigma Gaussian 0.3 %).
  TAU    N_meas >= 100 tau_int for the monitored series sum_i q_i, E (q-component 1), T2 (12, op 1)
         (brief: N_meas >= 100 tau_int). tau_int: Sokal window c = 6, autocorrelation averaged over chains.
  NCH    >= 16 independent chains (brief).

USAGE: python3 mcbox.py L BETA T NCH NTHERM NMEAS NOR COLL SEED OUTPREFIX
  writes OUTPREFIX.json, OUTPREFIX.npz (mode "x"). Exit 0 if pre-tests pass, 3 otherwise.
"""
import sys, json, math, time
import numpy as np

SG = np.array([1.0, -1.0, -1.0, -1.0])
BETA_OP = 1.0


def qm(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 + a2*b0 + a3*b1 - a1*b3,
                     a0*b3 + a3*b0 + a1*b2 - a2*b1], -1)


def qc(a):
    return a * SG


def tr0(a, b):  # 1/2 Tr (a b)
    return a[..., 0]*b[..., 0] - np.sum(a[..., 1:]*b[..., 1:], -1)


def haar(rng, shape):
    x = rng.standard_normal(shape + (4,))
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


def near1(rng, shape, eps):
    x = np.concatenate([np.ones(shape + (1,)), eps * rng.standard_normal(shape + (3,))], -1)
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


def kp_x0(k, rng):
    n = k.size; x0 = np.empty(n); todo = np.arange(n); it = 0
    while todo.size:
        it += 1; kk = k[todo]; m = todo.size
        if it <= 40:
            r1 = 1.0 - rng.random(m); r2 = rng.random(m); r3 = 1.0 - rng.random(m); r4 = rng.random(m)
            lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2 * np.log(r3)) / (2*kk)
            acc = r4*r4 <= 1.0 - lam2
            x0[todo[acc]] = 1.0 - 2.0*lam2[acc]
        else:
            y = haar(rng, (m,))[:, 0]
            acc = rng.random(m) < np.exp(kk*(y - 1.0))
            x0[todo[acc]] = y[acc]
        todo = todo[~acc]
    return x0


# U shape (R, 4, T, L, L, L, 4); a link field F_mu has shape (R, T, L, L, L, 4), lattice axis of mu = 1+mu
def sh(F, mu, s):
    return np.roll(F, -s, axis=1 + mu)


def plaq(U, mu, nu):
    """1/2 Tr U_p(x; mu, nu), shape (R,T,L,L,L)."""
    a = qm(U[:, mu], sh(U[:, nu], mu, 1))
    b = qm(U[:, nu], sh(U[:, mu], nu, 1))
    return tr0(a, qc(b))


def action(U, beta, dirs=None):
    S = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            if dirs is not None and mu not in dirs and nu not in dirs:
                continue
            S = S + beta * (1 - plaq(U, mu, nu)).sum(axis=(1, 2, 3, 4))
    return S


def staple(U, mu, nus):
    A = 0.0
    Um = U[:, mu]
    for nu in nus:
        Un = U[:, nu]
        up = qm(qm(sh(Un, mu, 1), qc(sh(Um, nu, 1))), qc(Un))
        Unm = sh(Un, nu, -1)
        dn = qm(qm(qc(sh(Unm, mu, 1)), qc(sh(Um, nu, -1))), Unm)
        A = A + up + dn
    return A


def wind(U, i):
    L = U.shape[3]
    W = U[:, i].copy()
    for s in range(1, L):
        W = qm(W, sh(U[:, i], i, s))
    return W


def operators(U):
    """returns dict ch -> (R, T, ncomp, nop)"""
    Ls = [wind(U, i) for i in (1, 2, 3)]
    P = [l[..., 0] for l in Ls]
    ax = (2, 3, 4)
    q = [np.mean(p*p, axis=ax) for p in P]
    q4 = [np.mean(p**4, axis=ax) for p in P]
    pl = [np.mean(plaq(U, 2, 3), axis=ax), np.mean(plaq(U, 1, 3), axis=ax), np.mean(plaq(U, 1, 2), axis=ax)]
    f = np.stack([np.stack(q, -1), np.stack(q4, -1), np.stack(pl, -1)], -1)  # (R,T,3dir,3op)
    e1 = (f[:, :, 0] - f[:, :, 1]) / math.sqrt(2)
    e2 = (f[:, :, 0] + f[:, :, 1] - 2*f[:, :, 2]) / math.sqrt(6)
    E = np.stack([e1, e2], 2)
    T2c = []; wp_sum = 0.0
    for (i, j, k) in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        wp = tr0(Ls[i], Ls[j])**2; wm = tr0(Ls[i], qc(Ls[j]))**2
        d = wp - wm
        wp_sum = wp_sum + np.mean(wp + wm, axis=ax)
        T2c.append(np.stack([np.mean(d, axis=ax), np.mean(d*(P[i]**2 + P[j]**2), axis=ax),
                             np.mean(d*P[k]**2, axis=ax)], -1))
    T2 = np.stack(T2c, 2)
    A1 = np.stack([sum(q), sum(q4), sum(pl), wp_sum], -1)[:, :, None, :]
    # l1-mcw addition: scaled spatial plaquette energy summed over the L^3 sites of a slice,
    # O_i = beta * sum_x (1 - P_jk(x)), plane jk perpendicular to i (pl_i is the site average). BETA_OP global.
    nsite = U.shape[3]**3
    Oe = [BETA_OP * nsite * (1.0 - p) for p in pl]
    PS = np.stack(Oe, -1)[:, :, :, None]                       # 3 components (one per plane), 1 op
    PA = (Oe[0] + Oe[1] + Oe[2])[:, :, None, None]             # A1
    PE = np.stack([(Oe[0] - Oe[1]) / math.sqrt(2), (Oe[0] + Oe[1] - 2*Oe[2]) / math.sqrt(6)], -1)[:, :, :, None]
    return {'A1': A1, 'E': E, 'T2': T2, 'PS': PS, 'PA': PA, 'PE': PE}


def gauge_tr(U, G):
    """U_mu(x) -> G(x) U_mu(x) G(x+mu)^-1; G shape (R,T,L,L,L,4)"""
    V = U.copy()
    for mu in range(4):
        V[:, mu] = qm(qm(G, U[:, mu]), qc(sh(G, mu, 1)))
    return V


def transporter(U, i, c):
    """V(x) for x on slice x_i = c, as a full-lattice field (only slice entries used). Path: time from t=0 at
    transverse 0, then direction j, then k (j<k the two other spatial directions)."""
    R, _, T, L = U.shape[:4]
    j, k = [d for d in (1, 2, 3) if d != i]
    V = np.zeros((R, T, L, L, L, 4)); V[..., 0] = 1.0
    def idx(t, xi, aj, ak):
        s = [slice(None), t, 0, 0, 0]
        s[1 + i] = xi; s[1 + j] = aj; s[1 + k] = ak
        return tuple(s)
    cur = np.zeros((R, 4)); cur[:, 0] = 1.0
    for t in range(T):
        base = cur.copy()
        for aj in range(L):
            bj = base.copy()
            for ak in range(L):
                V[idx(t, c, aj, ak)] = bj
                if ak < L - 1:
                    bj = qm(bj, U[(slice(None), k) + idx(t, c, aj, ak)[1:]])
            if aj < L - 1:
                base = qm(base, U[(slice(None), j) + idx(t, c, aj, 0)[1:]])
        if t < T - 1:
            cur = qm(cur, U[(slice(None), 0) + idx(t, c, 0, 0)[1:]])
    return V


def coll_propose(U, i, c, g):
    L = U.shape[3]
    V = transporter(U, i, c)
    M = qm(qm(qc(V), g[:, None, None, None, None, :]), V)
    Un = U.copy()
    s = [slice(None)] * 6; s[1 + i] = c; s = tuple(s)
    Un[:, i][s] = qm(M[s], U[:, i][s])
    return Un


def tau_int(series, c=6.0):
    x = series - series.mean(1, keepdims=True)
    N = x.shape[1]
    f = np.fft.rfft(x, n=2*N, axis=1)
    ac = np.fft.irfft(f*np.conj(f), axis=1)[:, :N].mean(0)
    if ac[0] <= 0:
        return 0.5, 0
    ac = ac / ac[0]
    tau = 0.5
    for W in range(1, N):
        tau += ac[W]
        if W >= c*tau:
            break
    return float(tau), int(W)


def pretests(rng, L, beta):
    res = {}; dev = 0.0
    T = 6; R = 2
    U = haar(rng, (R, 4, T, L, L, L))
    ops = operators(U)
    for i in (1, 2, 3):
        for c in range(L):
            V = U.copy(); s = [slice(None)] * 6; s[1 + i] = c; s = tuple(s)
            V[:, i][s] *= -1
            o = operators(V)
            for ch in ops:
                dev = max(dev, np.max(np.abs(o[ch] - ops[ch])))
    G = haar(rng, (R, T, L, L, L))
    UG = gauge_tr(U, G)
    o = operators(UG)
    for ch in ops:
        dev = max(dev, np.max(np.abs(o[ch] - ops[ch])))
    res['PRE1_dev'] = float(dev); res['PRE1'] = bool(dev <= 1e-11)
    # PRE2: permutation of axes and reflection
    dev2 = 0.0
    S0 = action(U, 1.0)
    perm = [0] + list(1 + rng.permutation(3))   # new direction d' = old direction perm[d']
    Up = np.empty_like(U)
    for d in range(4):
        Up[:, d] = np.transpose(U[:, perm[d]], (0, perm[0] + 1, perm[1] + 1, perm[2] + 1, perm[3] + 1, 5))
    def chsq(o):
        return {ch: np.einsum('rtca,rtcb->rtab', o[ch], o[ch]) for ch in o}
    a = chsq(ops); b = chsq(operators(Up))
    for ch in a:
        dev2 = max(dev2, np.max(np.abs(a[ch] - b[ch])))
    dev2 = max(dev2, np.max(np.abs(action(Up, 1.0) - S0)))
    # reflection x1 -> -x1 : U'_1(x) = U_1(Rx - e1)^-1, U'_d(x) = U_d(Rx)
    def refl(F):
        return np.roll(np.flip(F, axis=2), 1, axis=2)  # x -> -x mod L along axis 2 (x1)
    Ur = np.empty_like(U)
    for d in range(4):
        Ur[:, d] = refl(U[:, d])
    Ur[:, 1] = qc(sh(Ur[:, 1], 1, 1))
    b = chsq(operators(Ur))
    for ch in a:
        dev2 = max(dev2, np.max(np.abs(a[ch] - b[ch])))
    dev2 = max(dev2, np.max(np.abs(action(Ur, 1.0) - S0)))
    res['PRE2_dev'] = float(dev2); res['PRE2'] = bool(dev2 <= 1e-11)
    ok3 = True
    if L == 2:
        mu = 2; A = staple(U, mu, [n for n in range(4) if n != mu])
        par = parity(T, L)
        Un = U.copy(); Xn = haar(rng, (R, T, L, L, L))
        Un[:, mu] = np.where((par == 0)[None, ..., None], Xn, U[:, mu])
        dS_direct = action(Un, 1.0) - action(U, 1.0)
        dS_st = -np.sum(np.where((par == 0)[None], tr0(Xn - U[:, mu], A), 0), axis=(1, 2, 3, 4))
        res['PRE3_staple_dev'] = float(np.max(np.abs(dS_direct - dS_st)))
        ok3 = res['PRE3_staple_dev'] <= 1e-10
    k = 3.0
    x = kp_x0(np.full(200000, k), rng)
    th = np.linspace(0, np.pi, 200001); w = np.sin(th)**2*np.exp(k*np.cos(th))
    ex = np.sum(np.cos(th)*w)/np.sum(w)
    z = (x.mean() - ex)/(x.std()/math.sqrt(x.size))
    res['PRE3_KP_z'] = float(z)
    res['PRE3'] = bool(ok3 and abs(z) <= 4)
    # PRE4: collective move dS gauge covariance
    g = near1(rng, (R,), 0.5)
    i, c = 2, L - 1
    dS = action(coll_propose(U, i, c, g), 1.0) - S0
    G = haar(rng, (R, T, L, L, L)); UG = gauge_tr(U, G)
    s = [slice(None), 0, 0, 0, 0]; s[1 + i] = c
    gG = qm(qm(G[tuple(s)], g), qc(G[tuple(s)]))
    dSG = action(coll_propose(UG, i, c, gG), 1.0) - action(UG, 1.0)
    res['PRE4_dev'] = float(np.max(np.abs(dS - dSG))); res['PRE4'] = bool(res['PRE4_dev'] <= 1e-10)
    return res


def parity(T, L):
    t, x, y, z = np.meshgrid(np.arange(T), np.arange(L), np.arange(L), np.arange(L), indexing='ij')
    return (t + x + y + z) % 2


def main():
    L = int(sys.argv[1]); beta = float(sys.argv[2]); T = int(sys.argv[3]); NCH = int(sys.argv[4])
    NTH = int(sys.argv[5]); NME = int(sys.argv[6]); NOR = int(sys.argv[7]); COLL = int(sys.argv[8])
    seed = int(sys.argv[9]); out = sys.argv[10]
    global BETA_OP
    assert T % 2 == 0 and L in (1, 2)
    fj = open(out + '.json', 'x'); fz = open(out + '.npz', 'xb')
    rng = np.random.default_rng([seed, L, int(round(beta*100)), T, COLL])
    t0 = time.time()
    pre = pretests(rng, L, beta)   # with BETA_OP = 1 (absolute 1e-11 tolerance is for O(1) operator values)
    BETA_OP = beta
    if not all(pre[k] for k in ('PRE1', 'PRE2', 'PRE3', 'PRE4')):
        json.dump({'pre': pre}, fj, indent=1); fj.close(); fz.close(); print(pre); sys.exit(3)
    U = np.zeros((NCH, 4, T, L, L, L, 4)); U[..., 0] = 1.0
    par = parity(T, L)
    msk = [(par == p)[None, ..., None] for p in (0, 1)]
    mskb = [(par == p)[None] for p in (0, 1)]
    st = {'acc_L1sp': [0, 0], 'acc_L1t': [0, 0], 'acc_coll': [0, 0]}
    eps = {'coll': 0.5 * (beta * L**3)**-0.5, 't': 0.3}
    NCOLL = 2

    def ds_local_L1(Uo, Un, mu, spatial_only):
        """per-site dS for L=1 when links mu at one parity change (plaquettes based at x containing mu, and for
        temporal orientation also base x - e0 if mu spatial)."""
        d = 0.0
        for nu in range(4):
            if nu == mu:
                continue
            a, b = min(mu, nu), max(mu, nu)
            if spatial_only and (a == 0):
                continue
            dp = plaq(Uo, a, b) - plaq(Un, a, b)   # dS/beta = sum (P_old - P_new)
            d = d + dp
            if a == 0 and mu != 0:
                d = d + sh(dp, 0, -1)
        return beta * d

    def update(mu, p, mode):
        nonlocal U
        if L == 2:
            A = staple(U, mu, [n for n in range(4) if n != mu])
        else:
            if mu == 0:
                Uo = U.copy()
                for _ in range(4):
                    Un = U.copy()
                    Un[:, 0] = np.where(msk[p], qm(near1(rng, U[:, 0].shape[:-1], eps['t']), U[:, 0]), U[:, 0])
                    dS = ds_local_L1(U, Un, 0, False)
                    acc = (np.log(rng.random(dS.shape)) < -dS) & mskb[p]
                    U[:, 0] = np.where(acc[..., None], Un[:, 0], U[:, 0])
                    st['acc_L1t'][0] += int(acc.sum()); st['acc_L1t'][1] += int(mskb[p].sum()) * NCH
                return
            A = staple(U, mu, [0])
        a = np.maximum(np.linalg.norm(A, axis=-1), 1e-300)
        Vh = A / a[..., None]
        if mode == 'hb':
            x0 = kp_x0((beta*a).ravel(), rng).reshape(a.shape)
            n = rng.standard_normal(a.shape + (3,)); n /= np.linalg.norm(n, axis=-1, keepdims=True)
            X = np.concatenate([x0[..., None], np.sqrt(np.maximum(0, 1 - x0*x0))[..., None]*n], -1)
            Unew = qm(X, qc(Vh))
        else:
            Unew = qm(qm(qc(Vh), qc(U[:, mu])), qc(Vh))
        Unew /= np.linalg.norm(Unew, axis=-1, keepdims=True)
        if L == 2:
            U[:, mu] = np.where(msk[p], Unew, U[:, mu])
        else:
            Un = U.copy(); Un[:, mu] = np.where(msk[p], Unew, U[:, mu])
            dS = ds_local_L1(U, Un, mu, True)
            acc = (np.log(rng.random(dS.shape)) < -dS) & mskb[p]
            U[:, mu] = np.where(acc[..., None], Unew, U[:, mu])
            st['acc_L1sp'][0] += int(acc.sum()); st['acc_L1sp'][1] += int(mskb[p].sum()) * NCH

    def coll():
        nonlocal U
        for i in (1, 2, 3):
            for c in range(L):
                for _ in range(NCOLL):
                    S0 = action(U, beta, dirs=(i,))
                    Un = coll_propose(U, i, c, near1(rng, (NCH,), eps['coll']))
                    S1 = action(Un, beta, dirs=(i,))
                    acc = np.log(rng.random(NCH)) < -(S1 - S0)
                    U = np.where(acc[:, None, None, None, None, None, None], Un, U)
                    st['acc_coll'][0] += int(acc.sum()); st['acc_coll'][1] += NCH

    def sweep():
        for mu in range(4):
            for p in (0, 1):
                update(mu, p, 'hb')
        for _ in range(NOR):
            for mu in range(4):
                for p in (0, 1):
                    update(mu, p, 'or')
        if COLL:
            coll()
        if L == 1:
            for mu in range(4):   # reunitarise not needed for HB; guard rounding drift
                U[:, mu] /= np.linalg.norm(U[:, mu], axis=-1, keepdims=True)

    for it in range(NTH):
        for kk in st:
            st[kk] = [0, 0]
        sweep()
        if it < NTH // 2:
            if COLL:
                r = st['acc_coll'][0] / max(1, st['acc_coll'][1]); eps['coll'] *= 1.1 if r > 0.5 else 0.9
            if L == 1:
                r = st['acc_L1t'][0] / max(1, st['acc_L1t'][1]); eps['t'] *= 1.1 if r > 0.5 else 0.9
            eps['coll'] = min(eps['coll'], 3.0); eps['t'] = min(eps['t'], 3.0)
        if it % 50 == 0:
            U /= np.linalg.norm(U, axis=-1, keepdims=True)
    for kk in st:
        st[kk] = [0, 0]
    tth = time.time() - t0
    TM = T//2 + 1
    chans = ('A1', 'E', 'T2', 'PS', 'PA', 'PE')
    o = operators(U)
    C = {ch: np.zeros((2, NCH) + (o[ch].shape[-1],)*2 + (TM,)) for ch in chans}
    M = {ch: np.zeros((2, NCH, o[ch].shape[-2], o[ch].shape[-1])) for ch in chans}
    mon = np.zeros((4, NCH, NME)); sp1 = np.zeros((NCH, NME)); sp2 = np.zeros((NCH, NME))
    for m in range(NME):
        sweep()
        if m % 50 == 0:
            U /= np.linalg.norm(U, axis=-1, keepdims=True)
        h = 0 if m < NME//2 else 1
        o = operators(U)
        for ch in chans:
            O = o[ch]
            Of = np.fft.rfft(O, axis=1)
            cr = np.fft.irfft(np.einsum('rwca,rwcb->rabw', np.conj(Of), Of), n=T, axis=-1)
            C[ch][h] += cr[..., :TM] / (T * O.shape[2])
            M[ch][h] += O.mean(1)
        mon[0, :, m] = o['A1'][:, :, 0, 0].mean(1)
        mon[1, :, m] = o['E'][:, :, 0, 0].mean(1)
        mon[2, :, m] = o['T2'][:, :, 0, 0].mean(1)
        _e = np.stack([beta*(1-plaq(U, a, b)) for (a, b) in ((1, 2), (1, 3), (2, 3))])
        sp1[:, m] = _e.mean(axis=(0, 2, 3, 4, 5)); sp2[:, m] = (_e**2).mean(axis=(0, 2, 3, 4, 5))
        mon[3, :, m] = np.mean([plaq(U, a, b).mean(axis=(1, 2, 3, 4)) for a in range(4) for b in range(a+1, 4)], 0)
    taus = {nm: tau_int(mon[k]) for k, nm in enumerate(('sum_q', 'E1', 'T2_12', 'plaq'))}
    therm = {}
    for k, nm in ((0, 'sum_q'), (3, 'plaq')):
        a = mon[k, :, :NME//2].mean(1); b = mon[k, :, NME//2:].mean(1)
        d = a - b; z = d.mean() / (d.std(ddof=1)/math.sqrt(NCH))
        therm[nm] = float(z)
    res = {'L': L, 'beta': beta, 'T': T, 'NCH': NCH, 'NTHERM': NTH, 'NMEAS': NME, 'NOR': NOR, 'COLL': COLL,
           'seed': seed, 'pre': pre, 'eps': eps, 'acc': {k: v[0]/max(1, v[1]) for k, v in st.items()},
           'tau_int': taus, 'therm_z': therm,
           'plaq_mean': float(mon[3].mean()), 'plaq_err': float(mon[3].mean(1).std(ddof=1)/math.sqrt(NCH)),
           'time_therm_s': tth, 'time_total_s': time.time() - t0}
    res['THERM'] = bool(all(abs(z) <= 3 for z in therm.values()))
    res['TAU'] = bool(all(NME >= 100*taus[k][0] for k in ('sum_q', 'E1', 'T2_12')))
    res['NCH_rule'] = bool(NCH >= 16)
    np.savez(fz, **{f'C_{ch}': C[ch] for ch in chans}, **{f'M_{ch}': M[ch] for ch in chans}, mon=mon, sp1=sp1, sp2=sp2,
             nmeas=np.array([NME//2, NME - NME//2]))
    fz.close(); json.dump(res, fj, indent=1); fj.close()
    print(json.dumps(res))


if __name__ == '__main__':
    main()
