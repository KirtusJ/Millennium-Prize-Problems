"""run_a2.py -- A2/A3: kappa_H on heat-bath thermalized SU(2) configurations.
usage: python3 run_a2.py L bc(p|o) nsamp betas...   -> result_a2_L{L}{bc}.txt (mode x)

Thermalization: cold start (U=1), Kennedy-Pendleton heat bath, NTH=300 sweeps, then NSEP=40 sweeps between samples.
Seed: 1000*L + (bc=='o') + round(beta).

Predicates (fixed before first run):
 C1 (control) strong coupling beta=0.5: <(1/2)ReTr Q> within 0.01 of I2(b)/I1(b)=0.12402 (single-plaquette value;
    tolerance = O(beta^5) lattice corrections ~ 1e-3 plus statistical error ~ 1/sqrt(nP*sweeps) ~ 3e-3).
 C2 (control) for beta>=12: |<(1/2)ReTr Q> - (1-3/(4beta))| <= 0.25 * 3/(4beta) (one-loop; the two-loop term
    is ~ +0.05/beta^2-ish and finite-volume zero-mode corrections O(1/V) ~ several % of 3/(4 beta) on L=3).
 T2' (the file's S6 statement, per sample): kappa_H >= 0.5.  The file reports this FAILS on every sample.
    I report per-sample how many qualify (rule 4).
 T2'' (file's numbers): every sample has kappa_H in [-2.4, -1.0] (the file's range -1.17..-2.30 widened by
    sampling spread). Measured; failure means disagreement with the file.
 Measured only (A3): IPR*nE of the lowest horizontal eigenvector (1=uniform, nE=single link),
    zero-momentum weight in Landau gauge, max plaquette deviation 1-(1/2)ReTrQ, number of horizontal
    eigenvalues < 0, and fraction of |v|^2 on the 24 links nearest... (links of plaquettes with deviation in top 1%).
"""
import sys, numpy as np, time
from lat import *

L = int(sys.argv[1]); bc = sys.argv[2]; ns = int(sys.argv[3]); betas = [float(b) for b in sys.argv[4:]]
lat = Lattice(L, periodic=(bc == 'p'))
out = open(f'result_a2_L{L}{bc}.txt', 'x')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
NTH, NSEP = 300, 40
say(f'L={L} bc={bc} nE={lat.nE} nS={lat.nS} nP={lat.nP} NTH={NTH} NSEP={NSEP}')
fails = []
xs, ys = lat.links[:, 0], lat.links[:, 1]

def zero_mom_weight(lat, v):
    D = 3; vv = v.reshape(lat.nE, D)
    w = 0.0
    for mu in range(lat.d):
        sel = lat.links[:, 2] == mu
        m = vv[sel].mean(0); w += sel.sum() * (m @ m)
    return w / (v @ v)

for beta in betas:
    rng = np.random.default_rng(1000 * L + (bc == 'o') + int(round(beta)))
    U = np.array([np.eye(2, dtype=complex)] * lat.nE)
    t0 = time.time()
    for _ in range(NTH):
        heatbath_sweep(lat, U, beta, rng)
    pl = []
    for s in range(ns):
        ps = []
        for _ in range(NSEP):
            heatbath_sweep(lat, U, beta, rng); ps.append(avg_plaq(lat, U, 2))
        pl += ps
        dev = 1 - np.trace(plaquettes(lat, U), axis1=1, axis2=2).real / 2
        r = kappa_H(lat, U, beta, 2, want_vec=True)
        v = r['vec']; ln = (v.reshape(lat.nE, 3) ** 2).sum(1)
        ipr = (ln ** 2).sum() / ln.sum() ** 2 * lat.nE
        top = lat.plaq[dev >= np.quantile(dev, 0.99)]
        tl = np.unique(top.ravel()); wtop = ln[tl].sum() / ln.sum()
        Ug = landau_gauge(lat, U, sweeps=60)
        rg = kappa_H(lat, Ug, beta, 2, want_vec=True)
        zm = zero_mom_weight(lat, rg['vec'])
        nneg = int((r['wH'] < 0).sum())
        q = np.trace(Ug, axis1=1, axis2=2).real.mean() / 2
        say(f'beta={beta} s={s} plaq={pl[-1]:.5f} kH={r["kH"]:.4f} kH(gauge-fixed)={rg["kH"]:.4f} kfull={r["kfull"]:.3f} '
            f'rankG={r["rankG"]} nneg={nneg} IPR*nE={ipr:.2f} zeroMomW={zm:.3f} maxdev={dev.max():.4f} '
            f'meandev={dev.mean():.4f} w_on_top1%links={wtop:.3f} (frac links {len(tl)/lat.nE:.3f}) landauReTr/2={q:.4f} '
            f'low5={np.round(r["wH"][:5],3).tolist()}')
        if not r['kH'] >= 0.5:
            fails.append(f'T2p beta={beta} s={s}')
        if not (-2.4 <= r['kH'] <= -1.0):
            fails.append(f'T2pp beta={beta} s={s} kH={r["kH"]:.3f}')
    m = np.mean(pl); se = np.std(pl) / np.sqrt(len(pl) / 10)
    if beta < 1:
        ref = 0.12402; ok = abs(m - ref) < 0.01; tag = 'C1'
    else:
        ref = 1 - 3 / (4 * beta); ok = abs(m - ref) <= 0.25 * 3 / (4 * beta) if beta >= 12 else None; tag = 'C2'
    say(f'{tag} beta={beta} <plaq>={m:.5f} +- {se:.5f} ref={ref:.5f} ' + ('PASS' if ok else ('FAIL' if ok is False else 'measured')) + f' time={time.time()-t0:.0f}s')
    if ok is False:
        fails.append(f'{tag} beta={beta}')
say('FAILED predicates:', fails)
sys.exit(0)
