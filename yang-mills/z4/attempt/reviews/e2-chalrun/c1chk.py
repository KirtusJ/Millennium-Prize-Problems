"""c1chk.py -- independent recomputation of the one-loop SF coefficient c1(R;G).

Usage: python3 c1chk.py G d R [R ...]      (G in {su2,u1}); writes results/c1_<G>_d<d>_R<list>.txt (mode "x")
       python3 c1chk.py dense G d R        dense full-lattice cross-check of the Fourier code

Construction (mine, from the definitions in RUNNING.md sect. 1, not from the builder's program):
  U = exp(X) V, X = sum_a x_a T_a, T_a = i sigma_a/2 (SU(2)) or T = i (U(1)), <T_a,T_b> = delta_ab.
  S = sum_p (1 - (1/N) Re tr U_p) over plaquettes with >= 1 dynamical link.
  H = exact Hessian of S at V (per-plaquette second-order expansion of tr of a product of exponentials).
  D: X(x,mu) = w(x) - Ad_{V(x,mu)} w(x+mu); w=0 at x0=0, free at 1..T-1, one torus generator (T_3 or T)
     constant at x0=T (only in the p=0 block).
  Gamma1(eta) = 1/2 logdet(H + D D^dag) - logdet(D^dag D), summed over spatial momentum blocks.
  c1 = -Gamma1'(pi/4)/k, k = g0^2 beta dS0/deta (g0^2 beta = 4 for SU(2), 1 for U(1)); S0' by FD of the
  numerically computed S0 and compared to the closed form.
  Derivative: central differences h=2e-3 and 1e-3, Richardson (4 D(h/2) - D(h))/3.

PREDICATES (fixed before the first run):
  Q1 gradient of S at V: max |grad| <= 1e-13 (tolerance: double roundoff on O(1) sums, ~100 eps * #terms).
  Q2 max |H(p) D(p)| over p <= 1e-12 (same origin).
  Q3 min eig of A(p) = H(p)+D(p)D(p)^dag over all p > 0 at eta = pi/4 (reported); D^dag D(p) > 0.
  Q4 numerical k equals closed form -2c(d-1)R^{d-2} sin((pi-2eta)/R^2) to rel 1e-7 (FD error of S0').
  Q5 FD stability: |Richardson - D(h/2)| <= 1e-7 (relative to c1 ~ 0.3; expected h^2 term ~ 1e-7..1e-8).
  Q6 (comparison, SU(2) d=4) |c1 - table| <= half unit of last printed digit + 1e-7
      table: R=2 0.226403, 3 0.281797, 4 0.313012, 5 0.335656, 6 0.35422030, 8 0.38370429.
  Q7 (comparison, U(1) d=4) same, table: 0.228751 0.229316 0.233057 0.236059 0.238253 (R=2..6), 0.241119 (R=8).
  Q8 (U(1) only) trace formula tr[A^-1 H_t]/(2N_t) equals the FD value to 1e-7.
  Q9 (U(1) only) 0 < c1 <= 1/(2 cos(pi/(2R^2))).
  Q10 (dense mode) dense full-lattice c1 equals Fourier c1 to 1e-7.
v2 (after K3): Q8 trace divided by cos(theta) -- K3 used the background timelike Hessian, own defect.
No random numbers are used (seed fixed at 0 anyway).
"""
import sys, os, itertools, math
import numpy as np
np.random.seed(0)

def gens(G):
    if G == 'su2':
        s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
        return [1j * s / 2 for s in (s1, s2, s3)], 2, 4.0, s3, 2   # T, N, g0^2*beta, Q, index of torus generator
    T = [np.array([[1j]])]
    return T, 1, 1.0, np.array([[1.0 + 0j]]), 0

def expm_herm(M):  # exp of anti-hermitian matrix i*Herm
    w, U = np.linalg.eigh(-1j * M)
    return (U * np.exp(1j * w)) @ U.conj().T

class Model:
    def __init__(s, G, d, R, eta):
        s.G, s.d, s.R, s.T = G, d, R, R
        s.Tg, s.N, s.cfac, s.Q, s.itor = gens(G)
        s.nc = len(s.Tg)
        s.nrm = np.trace(s.Tg[0].conj().T @ s.Tg[0]).real
        phi, phip = -eta, -(math.pi - eta)
        s.phi = lambda x0: phi + (phip - phi) * x0 / s.T
        # local link indexing in a spatial cell
        s.lidx = {}
        for x0 in range(s.T):
            s.lidx[(x0, 0)] = len(s.lidx)
        for x0 in range(1, s.T):
            for k in range(1, d):
                s.lidx[(x0, k)] = len(s.lidx)
        s.nl = len(s.lidx)
        s.sidx = {x0: x0 - 1 for x0 in range(1, s.T)}   # interior sites
        s.ns = len(s.sidx)

    def V(s, x0, mu):
        if mu == 0:
            return np.eye(s.N, dtype=complex)
        return expm_herm(1j * s.phi(x0) * s.Q / s.R)

    def plaquettes(s):
        """yield list of 4 entries (x0, mu, shift(tuple), dagger) for plaquettes with base at spatial 0."""
        d = s.d
        z = (0,) * (d - 1)
        def e(k):
            v = [0] * (d - 1); v[k - 1] = 1; return tuple(v)
        out = []
        for mu, nu in itertools.combinations(range(d), 2):
            for x0 in range(0, s.T + 1):
                def site_plus(x0_, sh, dirn):
                    if dirn == 0: return x0_ + 1, sh
                    return x0_, tuple(a + b for a, b in zip(sh, e(dirn)))
                if mu == 0 and x0 > s.T - 1: continue
                if mu > 0 and (x0 == 0 or x0 == s.T):  # spatial plaquettes on the boundary: all fixed
                    continue
                x1 = site_plus(x0, z, mu); x2 = site_plus(x0, z, nu)
                L = [(x0, mu, z, False), (x1[0], nu, x1[1], False), (x2[0], mu, x2[1], True), (x0, nu, z, True)]
                out.append(L)
        return out

    def dyn(s, x0, mu):
        return s.lidx.get((x0, mu))

    def plaq_data(s):
        """per plaquette: action value, list of (local link idx, shift, grad(nc), and Hessian blocks)."""
        res = []
        for L in s.plaquettes():
            Ms = []; facs = []
            for (x0, mu, sh, dag) in L:
                v = s.V(x0, mu)
                Ms.append(v.conj().T if dag else v)
            # product P = F1 M1 F2 M2 F3 M3 F4 M4 with F=exp(sign X); for dagger, (e^X V)^dag = V^dag e^{-X}
            # order the factors as sequence of (kind,matrix)
            seq = []  # entries ('F', linkpos, sign) or ('M', matrix)
            for i, (x0, mu, sh, dag) in enumerate(L):
                if not dag:
                    seq.append(('F', i, +1)); seq.append(('M', Ms[i]))
                else:
                    seq.append(('M', Ms[i])); seq.append(('F', i, -1))
            def prod(insert):  # insert: dict pos-> matrix replacing F at link pos
                P = np.eye(s.N, dtype=complex)
                for it in seq:
                    if it[0] == 'M': P = P @ it[1]
                    else: P = P @ insert.get(it[1], np.eye(s.N))
                return P
            act = 1 - np.trace(prod({})).real / s.N
            dynl = [(i, s.dyn(x0, mu), sh) for i, (x0, mu, sh, dag) in enumerate(L) if s.dyn(x0, mu) is not None]
            if not dynl: continue
            sign = {i: (+1 if not L[i][3] else -1) for i in range(4)}
            grad = {}; hess = {}
            for (i, li, shi) in dynl:
                grad[i] = np.array([-sign[i] * np.trace(prod({i: s.Tg[a]})).real / s.N for a in range(s.nc)])
                for (j, lj, shj) in dynl:
                    Hb = np.zeros((s.nc, s.nc))
                    for a in range(s.nc):
                        for b in range(s.nc):
                            if i == j:
                                m = (s.Tg[a] @ s.Tg[b] + s.Tg[b] @ s.Tg[a]) / 2
                                Hb[a, b] = -np.trace(prod({i: m})).real / s.N
                            else:
                                Hb[a, b] = -sign[i] * sign[j] * np.trace(prod({i: s.Tg[a], j: s.Tg[b]})).real / s.N
                    hess[(i, j)] = Hb
            res.append((act, dynl, grad, hess, L))
        return res

    def ad(s, v):
        A = np.zeros((s.nc, s.nc))
        for a in range(s.nc):
            for b in range(s.nc):
                A[a, b] = np.trace(s.Tg[a].conj().T @ v @ s.Tg[b] @ v.conj().T).real / s.nrm
        return A

    def build(s, p, pdata, timelike_only=False):
        nc = s.nc
        n = s.nl * nc
        H = np.zeros((n, n), complex)
        for (act, dynl, grad, hess, L) in pdata:
            if timelike_only and L[0][1] != 0: continue
            for (i, li, shi) in dynl:
                for (j, lj, shj) in dynl:
                    ph = np.exp(1j * np.dot(p, np.subtract(shj, shi)))
                    H[li*nc:(li+1)*nc, lj*nc:(lj+1)*nc] += hess[(i, j)] * ph
        # D
        m = s.ns * nc + (1 if np.allclose(p, 0) else 0)
        D = np.zeros((n, m), complex)
        for (x0, mu), li in s.lidx.items():
            # X = w(x) - Ad_V w(x+mu)
            if 1 <= x0 <= s.T - 1:
                si = s.sidx[x0]
                D[li*nc:(li+1)*nc, si*nc:(si+1)*nc] += np.eye(nc)
            y0 = x0 + (1 if mu == 0 else 0)
            ad = s.ad(s.V(x0, mu))
            ph = 1.0 if mu == 0 else np.exp(1j * p[mu - 1])
            if 1 <= y0 <= s.T - 1:
                sj = s.sidx[y0]
                D[li*nc:(li+1)*nc, sj*nc:(sj+1)*nc] += -ad * ph
            elif y0 == s.T and np.allclose(p, 0):
                vec = np.zeros(nc); vec[s.itor] = 1.0
                D[li*nc:(li+1)*nc, m - 1] += -(ad @ vec)
        return H, D

    def momenta(s):
        ks = [2 * math.pi * j / s.R for j in range(s.R)]
        return [np.array(q) for q in itertools.product(ks, repeat=s.d - 1)]

def logdet_h(M):
    sgn, ld = np.linalg.slogdet(M)
    return ld

def gamma1(G, d, R, eta, checks=False, want_trace=False):
    m = Model(G, d, R, eta)
    pd = m.plaq_data()
    g1 = 0.0; info = {}
    if checks:
        # gradient: sum over translates -> per local link
        gr = np.zeros((m.nl, m.nc))
        for (act, dynl, grad, hess, L) in pd:
            for (i, li, sh) in dynl: gr[li] += grad[i]
        info['grad'] = np.abs(gr).max()
        info['HD'] = 0.0; info['mineigA'] = np.inf; info['mineigG'] = np.inf; info['herm'] = 0.0
    tr = 0.0
    for p in m.momenta():
        H, D = m.build(p, pd)
        A = H + D @ D.conj().T
        Gm = D.conj().T @ D
        g1 += 0.5 * logdet_h(A) - logdet_h(Gm)
        if checks:
            info['HD'] = max(info['HD'], np.abs(H @ D).max())
            info['herm'] = max(info['herm'], np.abs(H - H.conj().T).max())
            info['mineigA'] = min(info['mineigA'], np.linalg.eigvalsh(A).min())
            info['mineigG'] = min(info['mineigG'], np.linalg.eigvalsh(Gm).min())
        if want_trace:
            Ht, _ = m.build(p, pd, timelike_only=True)
            tr += np.trace(np.linalg.solve(A, Ht)).real
    S0 = m.R ** (d - 1) * sum(x[0] for x in pd)
    return g1, S0, info, tr, m

def c1(G, d, R):
    eta0 = math.pi / 4
    vals = {}
    for h in (2e-3, 1e-3):
        gp, sp, _, _, _ = gamma1(G, d, R, eta0 + h); gm, sm, _, _, _ = gamma1(G, d, R, eta0 - h)
        vals[h] = ((gp - gm) / (2 * h), (sp - sm) / (2 * h))
    dg = (4 * vals[1e-3][0] - vals[2e-3][0]) / 3
    ds = (4 * vals[1e-3][1] - vals[2e-3][1]) / 3
    cfac = gens(G)[2]
    k = cfac * ds
    kc = -2 * cfac * (d - 1) * R ** (d - 2) * math.sin((math.pi - 2 * eta0) / R ** 2)
    c = -dg / k
    c_h = -vals[1e-3][0] / k
    g0, S0, info, tr, m = gamma1(G, d, R, eta0, checks=True, want_trace=(G == 'u1'))
    Nt = (d - 1) * R ** (d - 1) * R
    return dict(c1=c, c1_h=c_h, k=k, kc=kc, info=info, trace=(tr / (2 * Nt * math.cos((math.pi - 2 * eta0) / R ** 2)) if G == 'u1' else None))  # v2: background timelike Hessian = cos(theta)*Maxwell H_t

TAB = {('su2', 4): {2: '0.226403', 3: '0.281797', 4: '0.313012', 5: '0.335656', 6: '0.35422030', 8: '0.38370429'},
       ('u1', 4): {2: '0.228751', 3: '0.229316', 4: '0.233057', 5: '0.236059', 6: '0.238253', 8: '0.241119'}}

def dense_c1(G, d, R):
    """Full-lattice dense construction: real basis, all spatial sites; independent of the Fourier phases."""
    eta0 = math.pi / 4
    def g1(eta):
        m = Model(G, d, R, eta); pd = m.plaq_data(); nc = m.nc
        cells = list(itertools.product(range(R), repeat=d - 1)); ci = {c: i for i, c in enumerate(cells)}
        nl = m.nl; n = len(cells) * nl * nc
        idx = lambda c, l: (ci[tuple(x % R for x in c)] * nl + l) * nc
        H = np.zeros((n, n))
        for c in cells:
            for (act, dynl, grad, hess, L) in pd:
                for (i, li, shi) in dynl:
                    for (j, lj, shj) in dynl:
                        a = idx(np.add(c, shi), li); b = idx(np.add(c, shj), lj)
                        H[a:a+nc, b:b+nc] += hess[(i, j)]
        ns = m.ns
        mm = len(cells) * ns * nc + 1
        D = np.zeros((n, mm))
        for c in cells:
            for (x0, mu), li in m.lidx.items():
                a = idx(c, li)
                if 1 <= x0 <= R - 1:
                    s0 = (ci[c] * ns + m.sidx[x0]) * nc
                    D[a:a+nc, s0:s0+nc] += np.eye(nc)
                y0 = x0 + (1 if mu == 0 else 0)
                cy = list(c)
                if mu > 0: cy[mu - 1] = (cy[mu - 1] + 1) % R
                ad = m.ad(m.V(x0, mu))
                if 1 <= y0 <= R - 1:
                    s1 = (ci[tuple(cy)] * ns + m.sidx[y0]) * nc
                    D[a:a+nc, s1:s1+nc] += -ad
                elif y0 == R:
                    vec = np.zeros(nc); vec[m.itor] = 1.0
                    D[a:a+nc, mm-1] += -(ad @ vec)
        return 0.5 * logdet_h(H + D @ D.T) - logdet_h(D.T @ D)
    vals = {}
    for h in (2e-3, 1e-3):
        vals[h] = (g1(eta0 + h) - g1(eta0 - h)) / (2 * h)
    dg = (4 * vals[1e-3] - vals[2e-3]) / 3
    cfac = gens(G)[2]
    kc = -2 * cfac * (d - 1) * R ** (d - 2) * math.sin((math.pi - 2 * eta0) / R ** 2)
    return -dg / kc

def main():
    os.makedirs('results', exist_ok=True)
    if sys.argv[1] == 'dense':
        G, d, R = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        cd = dense_c1(G, d, R); cf = c1(G, d, R)['c1']
        ok = abs(cd - cf) <= 1e-7
        with open(f'results/dense_{G}_d{d}_R{R}.txt', 'x') as f:
            line = f'{G} d={d} R={R} dense={cd:.10f} fourier={cf:.10f} diff={cd-cf:.2e} Q10={"MET" if ok else "FAILED"}'
            f.write(line + '\n'); print(line)
        return 0 if ok else 1
    G, d = sys.argv[1], int(sys.argv[2]); Rs = [int(r) for r in sys.argv[3:]]
    fn = f'results/c1_{G}_d{d}_R{"-".join(map(str, Rs))}_v2.txt'
    f = open(fn, 'x'); fails = 0
    def w(x):
        print(x, flush=True); f.write(x + '\n'); f.flush()
    for R in Rs:
        r = c1(G, d, R); inf = r['info']
        w(f'R={R} c1={r["c1"]:.10f} c1(h=1e-3 only)={r["c1_h"]:.10f} k={r["k"]:.8f} k_closed={r["kc"]:.8f} '
          f'grad={inf["grad"]:.1e} HD={inf["HD"]:.1e} herm={inf["herm"]:.1e} mineigA={inf["mineigA"]:.5f} mineigG={inf["mineigG"]:.5f}'
          + (f' trace_formula={r["trace"]:.10f}' if r['trace'] is not None else ''))
        preds = [('Q1', inf['grad'] <= 1e-13), ('Q2', inf['HD'] <= 1e-12), ('Q3', inf['mineigA'] > 0 and inf['mineigG'] > 0),
                 ('Q4', abs(r['k'] / r['kc'] - 1) <= 1e-7), ('Q5', abs(r['c1'] - r['c1_h']) <= 1e-7)]
        tab = TAB.get((G, d), {})
        if R in tab:
            s = tab[R]; nd = len(s.split('.')[1]); tol = 0.5 * 10 ** (-nd) + 1e-7
            preds.append(('Q6' if G == 'su2' else 'Q7', abs(r['c1'] - float(s)) <= tol))
            w(f'   table={s} diff={r["c1"]-float(s):+.2e} tol={tol:.1e}')
        if G == 'u1':
            preds.append(('Q8', abs(r['trace'] - r['c1']) <= 1e-7))
            preds.append(('Q9', 0 < r['c1'] <= 1 / (2 * math.cos(math.pi / (2 * R * R)))))
        for name, ok in preds:
            if not ok: fails += 1
        w('   ' + ' '.join(f'{n}={"MET" if ok else "FAILED"}' for n, ok in preds))
    w(f'failed predicates: {fails}')
    f.close()
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
