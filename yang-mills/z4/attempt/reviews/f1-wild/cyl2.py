"""cyl2.py -- identical to cyl.py (same predicates P0..P4) plus one exact-symmetry move per sweep:
for U(1) every U_i(t), all t, multiplied by a uniform random phase e^{i a_i sigma_3} (a_i in [0,2pi));
for SU(2) every U_i(t), all t, multiplied by a random center element z_i = +-1. The action is invariant
(global center symmetry), so the move is exact (acceptance 1). Reason: cyl.py failed P0 because the global
U(1) angle (a zero mode) did not equilibrate under local Metropolis.

Original docstring:
cyl.py -- Metropolis Monte Carlo for 4D Wilson lattice gauge theory on the single-site
spatial cylinder (Z/1Z)^3 x (Z/TZ), G = SU(2) or U(1) (U(1) embedded as the subgroup
{cos th + i sin th sigma_3} of SU(2); identical code path, only the proposal axis differs).

Action S = beta * sum_P (1 - Re tr U_P / N) ; Re tr/N = q0 (quaternion real part) for both groups.
Spatial plaquettes (i<j): U_i U_j U_i^-1 U_j^-1 (side 1, x+e_i = x).
Temporal plaquettes:      U_i(t) U_0(t) U_i(t+1)^-1 U_0(t)^-1.
No gauge fixing. Updates: U_i at all t of one parity at once (they do not interact), U_0 all t at once.
R independent replicas vectorized (fixed seed); errors by jackknife over replicas.

Observables per time slice (gauge invariant):
  E(t)  = sum_{i<j} (1/2) tr(U_i U_j U_i^-1 U_j^-1)          center-even  (identically 3 for U(1))
  Q(t)  = sum_i ((1/2) tr U_i)^2 - 1/2 ... used as sum_i cos(2 th_i)-type: 2*(q0)^2-1 = chi-like     center-even
  Pl(t) = sum_i (1/2) tr U_i                                   center-odd
For U(1): Pl ~ sum cos th_i (exact rate -ln(I1/I0)), Q = sum cos 2th_i (exact rate -ln(I2/I0)).

PREDICATES (fixed before the first run; evaluated in analyse.py):
 P0 control (known answer): U(1), beta in {4,16}: effective mass of Pl at t=2 equals -ln(I1/I0) and of Q at
    t=2 equals -ln(I2/I0), each within 3 jackknife sigma. Tolerance source: statistics only, since for U(1)
    Pl and Q contain only the charges +-1, +-2 so the periodic correlator is an exact single cosh.
 P1 SU(2): center-even gap m_e(beta) (min over E and Q of the plateau value, rule below) for beta in
    {32,64,128,256}: least-squares exponent p of m_e ~ beta^-p lies in [0.25, 0.42]
    (prediction 1/3 from quartic commutator confinement of the toron valley; window chosen to exclude
    1/2 = harmonic fluctuation scale and 1 = abelian scaling).
 P2 for every beta in {8,16,32,64,128,256}: m_e^SU2(beta) > -ln(I2(beta)/I0(beta)) (the U(1) gap in the
    Z2-center-even sector), by more than 3 sigma.
 P3 m_e^SU2 * beta^(1/3) at beta=256 and beta=32 agree within 25% (tolerance: allows O(beta^-1/3)
    corrections, 32^-1/3 = 0.31, together with statistical error).
 P4 measured only: SU(2) center-odd effective mass (Pl) at each beta.
Plateau rule: m_eff(t) = acosh((C(t-1)+C(t+1))/(2C(t))); m := m_eff at the largest t <= T/4 whose
jackknife relative error is < 10% and for which all smaller t>=2 also qualify (first run of qualifying t).
"""
import sys, json, time
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

def qc(a):
    return a * np.array([1.0, -1.0, -1.0, -1.0])

def comm_re(x, y):  # (1/2) tr(x y x^-1 y^-1)
    return qmul(qmul(x, y), qmul(qc(x), qc(y)))[..., 0]

def proposal(rng, shape, eps, group):
    r = np.zeros(shape + (4,))
    r[..., 0] = 1.0
    if group == 'su2':
        r[..., 1:] = eps * rng.standard_normal(shape + (3,))
    else:
        r[..., 3] = eps * rng.standard_normal(shape)
    return r / np.linalg.norm(r, axis=-1, keepdims=True)

def run(group, beta, T, R, ntherm, nmeas, seed):
    rng = np.random.default_rng(seed)
    U = np.zeros((R, T, 4, 4)); U[..., 0] = 1.0   # U[:, t, mu], mu=0 temporal, 1..3 spatial
    eps = {'s': 0.5, 0: 0.5}
    acc = {'s': [0, 0], 0: [0, 0]}

    def local_s(Ui, i, X, idx):
        # action-relevant part (sum of Re tr/N) for candidate X at link i, times idx
        s = 0.0
        for j in (1, 2, 3):
            if j != i:
                s = s + comm_re(X, U[:, idx, j])
        tp = (idx + 1) % T; tm = (idx - 1) % T
        U0 = U[:, idx, 0]; U0m = U[:, tm, 0]
        s = s + qmul(qmul(qmul(X, U0), qc(U[:, tp, i])), qc(U0))[..., 0]
        s = s + qmul(qmul(qmul(U[:, tm, i], U0m), qc(X)), qc(U0m))[..., 0]
        return s

    def local_0(Y, idx):
        s = 0.0
        tp = (idx + 1) % T
        for i in (1, 2, 3):
            s = s + qmul(qmul(qmul(U[:, idx, i], Y), qc(U[:, tp, i])), qc(Y))[..., 0]
        return s

    def sweep(nhit=2):
        for i in (1, 2, 3):
            for par in (0, 1):
                idx = np.arange(par, T, 2)
                for _ in range(nhit):
                    X = U[:, idx, i]
                    Xn = qmul(proposal(rng, X.shape[:-1], eps['s'], group), X)
                    dS = -beta * (local_s(None, i, Xn, idx) - local_s(None, i, X, idx))
                    a = rng.random(dS.shape) < np.exp(np.minimum(0.0, -dS))
                    U[:, idx, i] = np.where(a[..., None], Xn, X)
                    acc['s'][0] += a.sum(); acc['s'][1] += a.size
        idx = np.arange(T)
        for _ in range(nhit):
            Y = U[:, :, 0]
            Yn = qmul(proposal(rng, Y.shape[:-1], eps[0], group), Y)
            dS = -beta * (local_0(Yn, idx) - local_0(Y, idx))
            a = rng.random(dS.shape) < np.exp(np.minimum(0.0, -dS))
            U[:, :, 0] = np.where(a[..., None], Yn, Y)
            acc[0][0] += a.sum(); acc[0][1] += a.size
        # exact global center move
        if group == 'su2':
            z = rng.choice([-1.0, 1.0], size=(R, 1, 3, 1))
            U[:, :, 1:] = U[:, :, 1:] * z
        else:
            ang = rng.uniform(0, 2 * np.pi, size=(R, 1, 3))
            ph = np.zeros((R, 1, 3, 4)); ph[..., 0] = np.cos(ang); ph[..., 3] = np.sin(ang)
            U[:, :, 1:] = qmul(np.broadcast_to(ph, U[:, :, 1:].shape), U[:, :, 1:])

    for k in range(ntherm):
        sweep()
        if k % 50 == 49 and k < ntherm * 0.8:   # tune only during thermalization
            for key in eps:
                r = acc[key][0] / max(1, acc[key][1])
                eps[key] *= np.clip(r / 0.5, 0.7, 1.4)
                acc[key] = [0, 0]
    acc = {'s': [0, 0], 0: [0, 0]}
    # accumulate correlators per replica
    obs_sum = {k: np.zeros((R, T)) for k in 'EQP'}
    corr = {k: np.zeros((R, T)) for k in 'EQP'}
    for k in range(nmeas):
        sweep()
        E = (comm_re(U[:, :, 1], U[:, :, 2]) + comm_re(U[:, :, 1], U[:, :, 3]) + comm_re(U[:, :, 2], U[:, :, 3]))
        q0 = U[:, :, 1:, 0]
        Q = (2 * q0**2 - 1).sum(-1)
        Pl = q0.sum(-1)
        for key, o in (('E', E), ('Q', Q), ('P', Pl)):
            obs_sum[key] += o
            F = np.fft.rfft(o, axis=1)
            corr[key] += np.fft.irfft(F * np.conj(F), n=T, axis=1) / T
    out = {'group': group, 'beta': beta, 'T': T, 'R': R, 'ntherm': ntherm, 'nmeas': nmeas, 'seed': seed,
           'eps': {str(k): float(v) for k, v in eps.items()},
           'acc': {str(k): acc[k][0] / max(1, acc[k][1]) for k in acc}}
    for key in 'EQP':
        out['mean_' + key] = (obs_sum[key].mean(1) / nmeas).tolist()      # per replica
        out['corr_' + key] = (corr[key] / nmeas).tolist()                  # per replica, <o(t0)o(t0+t)>
    return out

if __name__ == '__main__':
    group, beta, T, R, ntherm, nmeas, seed, outf = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
    t0 = time.time()
    res = run(group, beta, T, R, ntherm, nmeas, seed)
    res['seconds'] = time.time() - t0
    with open(outf, 'x') as f:
        json.dump(res, f)
    print(outf, 'done in %.1fs' % res['seconds'], 'acc', res['acc'], 'eps', res['eps'])
