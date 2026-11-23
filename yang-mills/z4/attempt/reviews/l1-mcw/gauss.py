#!/usr/bin/env python3
"""gauss.py -- l1-mcw (T123). Exact Gaussian (quadratic Wilson action) plaquette-energy correlator on 2^3 x T.

theta = B A (B: plaquette-link incidence, every (site, mu<nu) a distinct plaquette, L=2 periodic).
Per colour <theta_p theta_q> = Pi_pq / beta, Pi = projector onto range(B) (computed by SVD; rank checked
against 4V - (V-1) - 4 = 3V - 3: gauge orbits V-1 and 4 constant-field directions span ker B).
C_XY(t) = (3/2) sum_{p in X(t), q in Y(0)} Pi_pq^2 (3 colours, Wick); averaged over the T time origins.
Single plaquette: mean (3/2) Pi_pp, variance (3/2) Pi_pp^2.

PREDICATES (fixed before first run):
 G1 rank(B) == 3V - 3 (exact integer).
 G2 trace(Pi) == rank (tolerance 1e-8: float64 SVD on ~10^4 x 10^4, rounding ~1e-12 per entry).
 G3 the spatial and temporal mean single-plaquette energies average (over all 6V plaquettes) to
    (3/2) rank / (6V) to 1e-10 (identity: sum_p Pi_pp = rank).
 G4 for T >= 32 the large-t ratio C(t+1)/C(t) of the box single-orientation operator at t = 3..5 equals
    exp(-2 arccosh 3) = exp(-3.52549435) to 1e-3 relative (the first two-photon level on 2^3 if the auditor
    is right; tolerance: next level 1.763+2.292 suppresses by e^{-0.53 t} ~ 0.2 at t=3 times weight ratio,
    so 1e-3 may FAIL at t=3 -- I report per t).
USAGE: python3 gauss.py OUT.json T [T ...]
"""
import sys, json, math
import numpy as np


def build(T, L=2):
    V = T * L ** 3
    def site(t, x, y, z):
        return (((t % T) * L + x % L) * L + y % L) * L + z % L
    def link(s, mu):
        return 4 * s + mu
    coords = [(t, x, y, z) for t in range(T) for x in range(L) for y in range(L) for z in range(L)]
    rows = []; meta = []
    for (t, x, y, z) in coords:
        c = [t, x, y, z]
        for mu in range(4):
            for nu in range(mu + 1, 4):
                cm = list(c); cm[mu] += 1
                cn = list(c); cn[nu] += 1
                r = np.zeros(4 * V)
                r[link(site(*c), mu)] += 1; r[link(site(*cm), nu)] += 1
                r[link(site(*cn), mu)] -= 1; r[link(site(*c), nu)] -= 1
                rows.append(r); meta.append((t, mu, nu))
    return np.array(rows), meta, V


def main():
    out = open(sys.argv[1], 'x')
    res = {}
    for T in map(int, sys.argv[2:]):
        B, meta, V = build(T)
        U, s, Vt = np.linalg.svd(B, full_matrices=False)
        rank = int(np.sum(s > 1e-9 * s.max()))
        Q = U[:, :rank]
        Pi = Q @ Q.T
        meta = np.array(meta)
        tt = meta[:, 0]; mu = meta[:, 1]; nu = meta[:, 2]
        spatial = mu > 0
        # planes: plane perpendicular to i: (2,3)->1, (1,3)->2, (1,2)->3
        plane = np.where(spatial, 6 - mu - nu, 0)
        d = np.diag(Pi)
        r = {'T': T, 'V': V, 'rank': rank, 'G1': bool(rank == 3 * V - 3), 'trace': float(d.sum()),
             'G2': bool(abs(d.sum() - rank) < 1e-8),
             'mean_spatial_single': float(1.5 * d[spatial].mean()), 'mean_temporal_single': float(1.5 * d[~spatial].mean()),
             'var_spatial_single': float(1.5 * np.mean(d[spatial] ** 2)),
             'G3': bool(abs(1.5 * d.mean() - 1.5 * rank / (6 * V)) < 1e-10)}
        P2 = Pi ** 2
        TM = T // 2 + 1
        # operator index sets: O_i(t)
        def idx(t, i):
            return np.where((tt == t) & spatial & (plane == i))[0]
        Cpp = np.zeros((3, 3, TM))
        for t0 in range(T):
            for t in range(TM):
                for i in range(3):
                    for j in range(3):
                        Cpp[i, j, t] += 1.5 * P2[np.ix_(idx((t0 + t) % T, i + 1), idx(t0, j + 1))].sum()
        Cpp /= T
        CS = np.mean([Cpp[i, i] for i in range(3)], 0)
        CA = Cpp.sum((0, 1))
        e1 = np.array([1, -1, 0]) / math.sqrt(2); e2 = np.array([1, 1, -2]) / math.sqrt(6)
        CE = 0.5 * (np.einsum('i,ijt,j->t', e1, Cpp, e1) + np.einsum('i,ijt,j->t', e2, Cpp, e2))
        for nm, C in (('PS', CS), ('PA', CA), ('PE', CE)):
            r[nm + '_C0'] = float(C[0]); r[nm + '_R'] = [float(x) for x in C / C[0]]
            with np.errstate(all='ignore'):
                r[nm + '_meff'] = [float(x) for x in np.log(C[:-1] / C[1:])]
        E1 = 2 * math.acosh(3)
        r['E1_auditor'] = E1
        r['G4_per_t'] = {t: bool(abs(CS[t + 1] / CS[t] / math.exp(-E1) - 1) < 1e-3) for t in (3, 4, 5) if t + 1 < TM}
        r['PS_weight_est'] = [float(CS[t] * math.exp(E1 * t) / CS[0]) for t in range(1, min(7, TM))]
        r['PA_weight_est'] = [float(CA[t] * math.exp(E1 * t) / CA[0]) for t in range(1, min(7, TM))]
        r['PE_weight_est'] = [float(CE[t] * math.exp(E1 * t) / CE[0]) for t in range(1, min(7, TM))]
        res[T] = r
        print(json.dumps(r), flush=True)
    json.dump(res, out, indent=1); out.close()


if __name__ == '__main__':
    main()
