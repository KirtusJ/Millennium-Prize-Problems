"""One-site SU(2) gauge model, 3 spatial dirs, periodic T slices, beta=64, T=34. Metropolis, numpy only.
Usage: python3 mc.py tune | python3 mc.py run NSWEEP
PREDICATES (fixed before first run):
 P1 step size: tune on separate pilot seed; choose eps among grid with acceptance closest to 0.45; require acc in [0.30,0.60]
    (source: standard Metropolis rule of thumb; no stronger tolerance justified).
 P2 thermalisation: discard first NTH=3000 sweeps; require mean of tau=0 corr observable (<s>) in 1st vs 2nd half of
    remaining run to agree within 3 sigma (sigma from chain-to-chain spread, 32 chains).
 P3 autocorrelation: tau_int (Madras-Sokal, window c=6) of the per-sweep observable corr(tau=1) of O_a/O_b average,
    chain-averaged; require NSWEEP_after_burn >= 50*tau_int (error on tau ~ sqrt(2/50) ~20%).
 P4 chains: 32 independent chains (>=16 required), jackknife delete-one-chain.
 P5 plateau: m_eff(t)=ln(D(t)/D(t+1)), D=C(t)-C(t+1). Plateau = first t0>=1 such that m_eff(t0),m_eff(t0+1),m_eff(t0+2)
    all defined (D>0), each jackknife rel. error <25%, and chi2/dof of the 3 points around their error-weighted mean (diagonal
    errors) <= 2. m = weighted mean; error = delete-one-chain jackknife of that same window-mean. If none: FAIL reported.
 P6 sampler check (grandchild): heat-bath-like known-answer check by sub-agent (my sampler here is Metropolis; check
    instead that detailed balance holds via P2 + that <s> is stable against eps).
Seeds fixed. Output files opened with mode 'x'.
"""
import sys, time, numpy as np
beta = 64.0; T = 34; C = 32; NTH = 3000
def qmul(a, b):
    a0, av = a[..., :1], a[..., 1:]; b0, bv = b[..., :1], b[..., 1:]
    return np.concatenate([a0*b0 - (av*bv).sum(-1, keepdims=True),
                           a0*bv + b0*av + np.cross(av, bv)], -1)
def cj(a): return a*np.array([1., -1, -1, -1])
def sc(a, b, c, d): return qmul(qmul(a, b), qmul(c, d))[..., 0]
def randq(rng, shape, eps):
    v = eps*rng.standard_normal(shape+(3,)); n = np.linalg.norm(v, axis=-1, keepdims=True)+1e-300
    return np.concatenate([np.cos(n), np.sin(n)*v/n], -1)
def haar(rng, shape):
    q = rng.standard_normal(shape+(4,)); return q/np.linalg.norm(q, axis=-1, keepdims=True)
def local(V, i, U, W):
    """local action/beta of link i for candidate V (C,T,4) at all t"""
    s = 0
    for j in range(3):
        if j != i: s = s + 1 - sc(V, U[j], cj(V), cj(U[j]))
    s = s + 1 - sc(V, W, cj(np.roll(U[i], -1, 1)), cj(W))
    Wm = np.roll(W, 1, 1)
    s = s + 1 - sc(np.roll(U[i], 1, 1), Wm, cj(V), cj(Wm))
    return s
def sweep(U, W, rng, eps, stats):
    even = (np.arange(T) % 2 == 0)
    for i in range(3):
        for p in (0, 1):
            m = even if p == 0 else ~even
            V = qmul(U[i], randq(rng, (C, T), eps))
            dS = beta*(local(V, i, U, W) - local(U[i], i, U, W))
            acc = (rng.random((C, T)) < np.exp(-dS)) & m[None, :]
            U[i] = np.where(acc[..., None], V, U[i]); stats[0] += acc[:, m].sum(); stats[1] += C*m.sum()
    # W(T-1)
    Wn = qmul(W[:, -1], randq(rng, (C,), eps))
    def lw(w):
        s = 0
        for i in range(3): s = s + 1 - sc(U[i][:, -1], w, cj(U[i][:, 0]), cj(w))
        return s
    acc = rng.random(C) < np.exp(-beta*(lw(Wn)-lw(W[:, -1])))
    W[:, -1] = np.where(acc[:, None], Wn, W[:, -1])
def observ(U):
    s = np.stack([1 - U[i][..., 0]**2 for i in range(3)])  # (3,C,T)
    return np.stack([(s[0]-s[1])/np.sqrt(2), (s[0]+s[1]-2*s[2])/np.sqrt(6)], 1)  # (C,2,T)
def corr(O):  # periodic cross-correlation averaged over t'
    F = np.fft.rfft(O, axis=-1)
    return np.fft.irfft(F.conj()*F, n=T, axis=-1)/T  # (C,2,T)
def init(seed):
    rng = np.random.default_rng(seed)
    U = haar(rng, (3, C, T)); W = np.zeros((C, T, 4)); W[..., 0] = 1
    return rng, U, W
if sys.argv[1] == 'tune':
    out = open('tune.txt', 'x'); res = []
    for eps in (0.04, 0.06, 0.08, 0.11, 0.15, 0.2):
        rng, U, W = init(999); st = [0, 0]; t0 = time.time()
        for n in range(600):
            if n == 400: st = [0, 0]
            sweep(U, W, rng, eps, st)
        a = st[0]/st[1]; res.append((abs(a-0.45), eps)); mean_s = (1-U[...,0]**2).mean()
        line = f"eps={eps} acc={a:.3f} <s>={mean_s:.5f} time/600sw={time.time()-t0:.1f}s"
        print(line); out.write(line+"\n")
    e = min(res)[1]; out.write(f"CHOSEN eps={e}\n"); print("CHOSEN", e)
else:
    NS = int(sys.argv[2]); eps = float(sys.argv[3])
    rng, U, W = init(2024); st = [0, 0]
    for n in range(NTH): sweep(U, W, rng, eps, st)
    st = [0, 0]; Csum = np.zeros((C, 2, T)); Osum = np.zeros((C, 2)); ser = np.zeros((NS, C, 3))
    for n in range(NS):
        sweep(U, W, rng, eps, st); O = observ(U); cr = corr(O)
        Csum += cr; Osum += O.mean(-1)
        ser[n, :, 0] = cr[:, :, 1].mean(1); ser[n, :, 1] = cr[:, :, 0].mean(1); ser[n, :, 2] = (1-U[..., 0]**2).mean((0, 2))
    np.savez_compressed(open('run_data.npz','xb'), Csum=Csum, Osum=Osum, ser=ser, acc=st[0]/st[1], NS=NS, eps=eps)
    print("done acc", st[0]/st[1])
