"""Quick SU(2) Wilson Monte Carlo on a spatial N1xN2xN3 periodic box with T time slices (j1-box, T107).

Action beta * sum_P (1 - (1/2) Re Tr U_P), isotropic, periodic. Local Metropolis (multi-hit), vectorised over
links of one direction and one site parity (no plaquette contains two distinct candidate links; for extent-1
directions the doubled link is handled by computing the change of every affected plaquette exactly).

Observable: W_i(t) = holonomy along spatial direction i (averaged over transverse positions of (1/2)Tr W_i),
s_i = ((1/2) Tr W_i)^2 (even under every slice center flip), E channel O_a = s_1 - s_2, O_b = s_1 + s_2 - 2 s_3.
Connected correlator averaged over time origins and the two E components; effective mass from the differenced
correlator D(t) = C(t) - C(t+1): m_eff(t) = ln D(t)/D(t+1). Errors: jackknife over 20 blocks of the
measurement series. tau_int of the slice-summed O_a by the Sokal window (c=6).

Predicates fixed before the first run:
 CTRL (pipeline control, one site N=(1,1,1), beta=4, T=32): known E-channel gap 0.96893 (MC_three_dir.md,
   exact diagonalisation quoted there). Met if |m_eff(t) - 0.96893| <= 3 sigma_jack for t = 2 (tolerance:
   statistical only; systematic excited-state contamination at t=2 judged small since the next E level is
   >1.18 above... not known to me, hence a failed CTRL counts as a defect of MY method, not of the target).
 BOX (2x2x2, beta=256): MEASURED ONLY. Prediction (leading order) m = 3.012539 * 256^(-1/3) / 2 = 0.23664.
   No pass/fail predicate; reported with tau_int and plateau values; not reported as a number if
   tau_int * 50 > number of measurements (TAU rule) or if no two consecutive m_eff agree within 1 sigma.
Fixed seed per run (argument).
"""
import sys, time
import numpy as np


def qmul(a, b):
    a0, av = a[..., :1], a[..., 1:]
    b0, bv = b[..., :1], b[..., 1:]
    return np.concatenate([a0 * b0 - np.sum(av * bv, -1, keepdims=True),
                           a0 * bv + b0 * av - np.cross(av, bv)], -1)


def qconj(a):
    return a * np.array([1., -1., -1., -1.])


def plaq_energy(U, mu, nu):
    # 1 - P0 for P_{mu nu}(x) = U_mu(x) U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
    a = qmul(U[mu], np.roll(U[nu], -1, axis=mu))
    b = qmul(U[nu], np.roll(U[mu], -1, axis=nu))
    return 1.0 - np.sum(a * b, -1)  # Re of a b^dag = a . b


def run(shape, T, beta, nsweep, ntherm, seed, eps, hits=3, every=1):
    rng = np.random.default_rng(seed)
    dims = (T,) + tuple(shape)
    ext = dims
    U = np.zeros((4,) + dims + (4,)); U[..., 0] = 1.0
    grid = np.indices(dims).sum(0) % 2
    acc_tot = 0; prop_tot = 0
    meas = []
    t0 = time.time()
    for sweep in range(nsweep + ntherm):
        for mu in range(4):
            for par in (0, 1):
                mask = (grid == par)
                for _ in range(hits):
                    R = np.zeros(dims + (4,)); R[..., 0] = 1.0
                    R[..., 1:] = eps * rng.normal(size=dims + (3,))
                    R /= np.linalg.norm(R, axis=-1, keepdims=True)
                    new = np.where(mask[..., None], qmul(R, U[mu]), U[mu])
                    Un = U.copy(); Un[mu] = new
                    dS = np.zeros(dims)
                    for nu in range(4):
                        if nu == mu:
                            continue
                        dE = plaq_energy(Un, mu, nu) - plaq_energy(U, mu, nu)
                        dS += dE
                        if ext[nu] > 1:
                            dS += np.roll(dE, 1, axis=nu)
                    accept = mask & (rng.random(dims) < np.exp(-beta * np.clip(dS, -50, None)))
                    U[mu] = np.where(accept[..., None], new, U[mu])
                    acc_tot += accept.sum(); prop_tot += mask.sum()
            U[mu] /= np.linalg.norm(U[mu], axis=-1, keepdims=True)
        if sweep >= ntherm and sweep % every == 0:
            s = []
            for i in (1, 2, 3):
                W = U[i]
                for k in range(1, ext[i]):
                    W = qmul(W, np.roll(U[i], -k, axis=i))
                tr = W[..., 0]  # (1/2) Tr W at every base point; average over all spatial points
                s.append(np.mean(tr.reshape(T, -1) ** 2, axis=1))
            s = np.array(s)  # (3, T)
            meas.append(np.stack([s[0] - s[1], s[0] + s[1] - 2 * s[2]]))
    return np.array(meas), acc_tot / prop_tot, time.time() - t0


def corr(meas, tmax):
    # meas: (Nm, 2, T)
    x = meas - meas.mean(axis=(0, 2), keepdims=True)
    T = x.shape[2]
    C = np.array([np.mean(x * np.roll(x, -t, axis=2)) for t in range(tmax + 3)])
    return C


def tau_int(series, c=6.0):
    x = series - series.mean(); n = len(x)
    f = np.fft.rfft(x, 2 * n); ac = np.fft.irfft(f * np.conj(f))[:n] / np.arange(n, 0, -1)
    ac /= ac[0]; tau = 0.5
    for W in range(1, n):
        tau += ac[W]
        if W >= c * tau:
            break
    return tau


def analyse(meas, tmax, nb=20):
    Nm = len(meas); bs = Nm // nb
    def meff(m):
        C = corr(m, tmax); D = C[:-1] - C[1:]
        with np.errstate(all="ignore"):
            return np.log(D[:-1] / D[1:])[:tmax + 1]
    full = meff(meas)
    jk = np.array([meff(np.concatenate([meas[:b * bs], meas[(b + 1) * bs:nb * bs]])) for b in range(nb)])
    err = np.sqrt((nb - 1) * np.nanmean((jk - jk.mean(0)) ** 2, axis=0))
    tau = tau_int(meas[:, 0, :].sum(1))
    return full, err, tau


if __name__ == "__main__":
    mode = sys.argv[1]; seed = int(sys.argv[2]); out = sys.argv[3]
    if mode == "ctrl":
        shape, T, beta, nsw, nth, eps = (1, 1, 1), 32, 4.0, int(sys.argv[4]), 200, 0.6
        pred = 0.96893
    else:
        shape, T, beta, nsw, nth, eps = (2, 2, 2), int(sys.argv[5]), 256.0, int(sys.argv[4]), 300, float(sys.argv[6])
        pred = 3.012539 * beta ** (-1 / 3) / 2
    meas, acc, dt = run(shape, T, beta, nsw, nth, seed, eps)
    tmax = 10 if mode == "ctrl" else 14
    m, e, tau = analyse(meas, tmax)
    lines = [f"mode={mode} shape={shape} T={T} beta={beta} sweeps={nsw} therm={nth} seed={seed} eps={eps} acc={acc:.3f} time={dt:.1f}s",
             f"tau_int(O_a slice sum)={tau:.2f} sweeps, Nmeas={len(meas)}, Nmeas/tau={len(meas)/tau:.1f}",
             f"prediction={pred:.5f}"]
    for t in range(len(m)):
        lines.append(f"t={t} m_eff={m[t]:.5f} +- {e[t]:.5f}   m*beta^(1/3)={m[t]*beta**(1/3):.4f}")
    verdict = ""
    if mode == "ctrl":
        ok = abs(m[2] - pred) <= 3 * e[2]
        verdict = f"CTRL {'MET' if ok else 'FAILED'}: m_eff(2)={m[2]:.5f}+-{e[2]:.5f} vs {pred}"
    else:
        verdict = "BOX measured only"
    lines.append(verdict)
    txt = "\n".join(lines)
    print(txt)
    with open(out, "x") as fh:
        fh.write(txt + "\n")
    np.save(out + ".npy", meas)
    sys.exit(0)
