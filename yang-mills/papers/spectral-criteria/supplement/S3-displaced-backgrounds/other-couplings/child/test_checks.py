"""PREDICATES (fixed before first run). Usage: test_checks.py <resultfile>
P1 heat bath vs exact single link: KP sample of w0 (alpha=beta, 400000 samples, seed 1); exact <w0>,<w0^2> by
   quadrature of density sin^2(chi) exp(alpha cos chi); PASS if |mean-exact| < 4 SE (SE = sample std/sqrt(N); 4 sigma ~ 6e-5 false-alarm rate).
P2 hot/cold agreement: one hot-start chain and one cold-start chain (seeds 2,3), 150 thermalisation + 150 measured sweeps
   of average plaquette; PASS if |diff of means| < 4*sqrt(se1^2+se2^2), se by 10 batch means over measured sweeps.
P3 gauge invariance: random gauge transform of a thermalised config leaves m1 and theta unchanged, max abs diff < 1e-10 (float round-off scale).
P4 cold start: avg plaquette == 1 and all theta == pi (W=I is at distance pi from -I; v1 wrongly expected 0) within 1e-12; unitarity after sweeps max| |q|-1 | < 1e-12.
P5 Haar control: P(theta<1.2) by MC (4e5 samples, seed 4) within 4 SE of 0.274469.
Exit 0 only if all pass."""
import sys, json, numpy as np
from lat import *
res = {}
rng = np.random.default_rng(1)
al = BETA
w = kp_w0(rng, np.full(400000, al))
chi = np.linspace(0, np.pi, 200001); d = np.sin(chi)**2*np.exp(al*np.cos(chi)); Z = np.trapezoid(d, chi)
e1 = np.trapezoid(d*np.cos(chi), chi)/Z; e2 = np.trapezoid(d*np.cos(chi)**2, chi)/Z
se1 = w.std()/np.sqrt(w.size); se2 = (w**2).std()/np.sqrt(w.size)
res['P1'] = dict(mean=w.mean(), exact=e1, se=se1, mean2=(w**2).mean(), exact2=e2, se2=se2,
                 ok=bool(abs(w.mean()-e1) < 4*se1 and abs((w**2).mean()-e2) < 4*se2))
def chain(seed, hot):
    r = np.random.default_rng(seed)
    U = haar(r, (4,)+DIMS) if hot else np.concatenate([np.ones((4,)+DIMS+(1,)), np.zeros((4,)+DIMS+(3,))], -1)
    for _ in range(150): sweep(U, r)
    ps = []
    for _ in range(150): sweep(U, r); ps.append(avg_plaq(U))
    ps = np.array(ps); b = ps.reshape(10, 15).mean(1)
    return U, ps.mean(), b.std(ddof=1)/np.sqrt(10)
Uh, mh, sh_ = chain(2, True); Uc, mc, sc = chain(3, False)
res['P2'] = dict(hot=mh, cold=mc, se_hot=sh_, se_cold=sc, ok=bool(abs(mh-mc) < 4*np.hypot(sh_, sc)))
m, th = marks(Uh)
G = haar(np.random.default_rng(5), DIMS)
m2, th2 = marks(gauge(Uh, G))
res['P3'] = dict(dm=float(abs(m-m2).max()), dth=float(abs(th-th2).max()), ok=bool(abs(m-m2).max() < 1e-10 and abs(th-th2).max() < 1e-10))
cold = np.concatenate([np.ones((4,)+DIMS+(1,)), np.zeros((4,)+DIMS+(3,))], -1)
mc_, thc = marks(cold)
nrm = max(abs(np.linalg.norm(Uh, axis=-1)-1).max(), abs(np.linalg.norm(Uc, axis=-1)-1).max())
res['P4'] = dict(plaq=avg_plaq(cold), maxdev_from_pi=float(abs(thc-np.pi).max()), unit_err=float(nrm), ok=bool(abs(avg_plaq(cold)-1) < 1e-12 and abs(thc-np.pi).max() < 1e-6 and nrm < 1e-12))
r = np.random.default_rng(4); a0 = haar(r, (400000,))[:, 0]; ind = (np.arccos(-a0) < 1.2)
pe = (1.2-np.sin(2.4)/2)/np.pi
res['P5'] = dict(mc=ind.mean(), se=ind.std()/np.sqrt(ind.size), exact=pe, ok=bool(abs(ind.mean()-pe) < 4*ind.std()/np.sqrt(ind.size)))
with open(sys.argv[1], 'x') as f: json.dump(res, f, indent=1)
print(json.dumps(res, indent=1)); sys.exit(0 if all(v['ok'] for v in res.values()) else 1)
