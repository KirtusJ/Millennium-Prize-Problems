"""box_mc.py -- e2-chalBgen own Monte Carlo of the minimal box R_1 = [-1,1]^4 with trivial shell.

Model. Only the 8 links at the interior site x0 are free. Write h_a (a = +-mu, 8 "arms") for the
holonomy from x0 along arm a (h_{+mu}=U_{x0,mu}, h_{-mu}=U_{x0-e_mu,mu}^{-1}). Every plaquette of P_R
has holonomy conjugate to h_a h_b^{-1} with a,b on different axes (24 plaquettes; the 4 collinear
pairs are not plaquettes). S = sum s(h_a h_b^{-1}), s(U) = 1 - Re Tr rho(U)/N_rho. No gauge fixing
(O_p is gauge invariant; gauge freedom at x0 is h_a -> g h_a).
Prediction from THEOREM_B_GENERAL.md (N4) / general.tex 'Check': E O_p -> (d/2) C_pp, C_pp = 7/24,
i.e. 7d/48, d = dim G. (7/24 re-derived independently: Foster's theorem on K_{2,2,2,2}.)

Groups (all rho as matrices):
  U1      : rho = e^{it},                       N=1, d=1, pred 7/48
  U1_15   : rho = e^{it} + e^{5it},             N=2, d=1, pred 7/48   (deep local minima of s)
  SU3     : fundamental,                        N=3, d=8, pred 7/6
  U1xSU2  : charge-3 char + SU(2) fundamental,  N=3, d=4, pred 7/12   (not faithful: kernel Z_3; rho(G) has d=4)
  O2      : defining 2x2,                       N=2, d=1, pred 7/48   (moves between components included)
Update: Metropolis, proposal h -> exp(eps X) h, X Gaussian in the Lie algebra (symmetric w.r.t. Haar);
for O2 also h -> r h with r a Haar-random reflection (an involution, symmetric), and a global
left multiplication of all arms by one random reflection (exact gauge symmetry, Delta S = 0).
Independent chains C=64, seed fixed per (group, beta).

PREDICATES (fixed before first run):
  P1[G] (beta=300): |mean O_p - 7d/48| <= 4*sigma + 0.25*d/beta.
     sigma = standard error from chain-to-chain spread (64 independent chains, each its own mean).
     0.25*d/beta: my own finite-beta allowance; source: builder's SU(3) value at beta=75 (1.17198) is
     0.0053 above 7/6, i.e. a 1/beta coefficient ~0.4 for d=8 (0.05 per colour); 0.25 per colour is 5x that.
  P2[O2] (beta=300): fraction of samples whose arms do NOT all lie in one component of O(2) == 0
     (expectation: such configurations have at least 12 plaquettes in the reflection component, s=1 there).
  M (measured only): beta=1200 means; per-plaquette spread; acceptance rates; O2 global-flip count.
Output: results_box_mc.txt, opened with mode 'x'.
"""
import numpy as np, sys, time

PAIRS = [(a, b) for a in range(8) for b in range(8) if a < b and a // 2 != b // 2]
assert len(PAIRS) == 24

def expm_ah(X):
    # exp of batch of anti-Hermitian (or real antisymmetric) matrices via eigh of the Hermitian iX
    H = 1j * X
    w, V = np.linalg.eigh(H)
    E = np.exp(-1j * w)
    return (V * E[..., None, :]) @ np.conj(np.swapaxes(V, -1, -2))

def group(name, rng):
    if name == 'U1':
        N, d = 1, 1
        def rnd_alg(C):
            return 1j * rng.standard_normal((C, 1, 1)) * np.ones((1, 1, 1))
    elif name == 'U1_15':
        N, d = 2, 1
        def rnd_alg(C):
            t = rng.standard_normal(C)
            X = np.zeros((C, 2, 2), complex); X[:, 0, 0] = 1j * t; X[:, 1, 1] = 5j * t
            return X / np.sqrt(13.0)
    elif name == 'SU3':
        N, d = 3, 8
        def rnd_alg(C):
            A = rng.standard_normal((C, 3, 3)) + 1j * rng.standard_normal((C, 3, 3))
            Hm = (A + np.conj(np.swapaxes(A, 1, 2))) / 2
            Hm -= np.trace(Hm, axis1=1, axis2=2)[:, None, None] * np.eye(3) / 3
            return 1j * Hm / np.sqrt(2)
    elif name == 'U1xSU2':
        N, d = 3, 4
        def rnd_alg(C):
            X = np.zeros((C, 3, 3), complex)
            X[:, 0, 0] = 3j * rng.standard_normal(C) / 3.0
            A = rng.standard_normal((C, 2, 2)) + 1j * rng.standard_normal((C, 2, 2))
            Hm = (A + np.conj(np.swapaxes(A, 1, 2))) / 2
            Hm -= np.trace(Hm, axis1=1, axis2=2)[:, None, None] * np.eye(2) / 2
            X[:, 1:, 1:] = 1j * Hm / np.sqrt(2)
            return X
    elif name == 'O2':
        N, d = 2, 1
        def rnd_alg(C):
            t = rng.standard_normal(C)
            X = np.zeros((C, 2, 2), complex); X[:, 0, 1] = -t; X[:, 1, 0] = t
            return X
    return N, d, rnd_alg

def s_of(U, N):
    return 1.0 - np.real(np.trace(U, axis1=-2, axis2=-1)) / N

def rand_reflection(C, rng):
    th = rng.uniform(0, 2 * np.pi, C)
    c, s = np.cos(th), np.sin(th)
    R = np.zeros((C, 2, 2), complex)
    R[:, 0, 0] = c; R[:, 0, 1] = s; R[:, 1, 0] = s; R[:, 1, 1] = -c
    return R

def run(name, beta, sweeps, therm, C, seed):
    rng = np.random.default_rng(seed)
    N, d, rnd_alg = group(name, rng)
    h = np.tile(np.eye(N, dtype=complex), (C, 8, 1, 1))
    eps = 1.0 / np.sqrt(beta)
    nb = {a: [b for b in range(8) if b // 2 != a // 2] for a in range(8)}
    def local(a, ha):
        tot = 0.0
        for b in nb[a]:
            tot = tot + s_of(ha @ np.conj(np.swapaxes(h[:, b], -1, -2)), N)
        return tot
    acc = 0; tries = 0; racc = 0; rtries = 0
    sums = np.zeros((C, 24)); mixed = 0; nsamp = 0; flips = 0
    for sw in range(therm + sweeps):
        for a in range(8):
            old = local(a, h[:, a])
            new_h = expm_ah(eps * rnd_alg(C)) @ h[:, a]
            new = local(a, new_h)
            ok = rng.random(C) < np.exp(-beta * (new - old))
            h[ok, a] = new_h[ok]; acc += ok.sum(); tries += C
            if name == 'O2':
                new_h = rand_reflection(C, rng) @ h[:, a]
                new = local(a, new_h)
                ok = rng.random(C) < np.exp(-beta * (new - old if False else new - local(a, h[:, a])))
                h[ok, a] = new_h[ok]; racc += ok.sum(); rtries += C
        if name == 'O2':
            R = rand_reflection(C, rng)
            h = R[:, None] @ h; flips += C
        if sw >= therm:
            O = np.stack([beta * s_of(h[:, a] @ np.conj(np.swapaxes(h[:, b], -1, -2)), N) for a, b in PAIRS], axis=1)
            sums += O; nsamp += 1
            if name == 'O2':
                det = np.real(np.linalg.det(h))
                mixed += int(np.sum(~(np.all(det > 0, axis=1) | np.all(det < 0, axis=1))))
    per_chain = sums.mean(axis=1) / nsamp
    per_plaq = sums.mean(axis=0) / nsamp
    m = per_chain.mean(); se = per_chain.std(ddof=1) / np.sqrt(C)
    return dict(N=N, d=d, mean=m, se=se, plaq_min=per_plaq.min(), plaq_max=per_plaq.max(),
                acc=acc / tries, racc=(racc / rtries if rtries else None), mixed=mixed,
                nsamp=nsamp * C, flips=flips)

if __name__ == '__main__':
    t0 = time.time()
    out = open('results_box_mc.txt', 'x')
    def W(s):
        print(s); out.write(s + '\n'); out.flush()
    fails = 0
    groups = ['U1', 'U1_15', 'O2', 'U1xSU2', 'SU3']
    W('group beta d pred mean se dev/se tol pass plaq[min,max] acc racc mixed')
    for gi, name in enumerate(groups):
        for beta, sweeps in [(300.0, 5000), (1200.0, 2500)]:
            r = run(name, beta, sweeps, 1000, 64, 1000 + 10 * gi + (1 if beta > 500 else 0))
            pred = 7 * r['d'] / 48
            tol = 4 * r['se'] + 0.25 * r['d'] / beta
            ok = abs(r['mean'] - pred) <= tol
            tag = 'P1' if beta == 300.0 else 'M'
            if tag == 'P1' and not ok: fails += 1
            W(f"{name} {beta:.0f} {r['d']} {pred:.5f} {r['mean']:.5f} {r['se']:.5f} {(r['mean']-pred)/r['se']:+.2f} {tol:.5f} "
              f"{tag}:{'MET' if ok else ('FAILED' if tag=='P1' else 'meas')} [{r['plaq_min']:.4f},{r['plaq_max']:.4f}] "
              f"{r['acc']:.3f} {r['racc']} {r['mixed']}/{r['nsamp']}")
            if name == 'O2' and beta == 300.0:
                ok2 = r['mixed'] == 0
                if not ok2: fails += 1
                W(f"P2 O2 mixed-component samples = {r['mixed']} of {r['nsamp']}: {'MET' if ok2 else 'FAILED'}; global reflection gauge moves applied: {r['flips']}")
            W(f"  elapsed {time.time()-t0:.1f}s")
    W(f"P-failures: {fails}")
    out.close()
    sys.exit(1 if fails else 0)
