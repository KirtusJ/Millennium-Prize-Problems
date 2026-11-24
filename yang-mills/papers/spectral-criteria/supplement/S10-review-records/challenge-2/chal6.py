#!/usr/bin/env python3
"""chal6.py -- challenger program for Prop. p:pred, the text after it, and Remark r:lag.
Usage: python3 chal6.py SEED N_A N_C OUTFILE      (OUTFILE is opened with mode 'x': never overwritten)

PREDICATES, FIXED BEFORE THE FIRST RUN.  TOL = 1e-9 (basis: matrices of size <= 12, entries O(1),
conditioning of pi >= 1e-3; double rounding observed ~1e-13; the measured minimum margin is reported too,
so the tolerance can be judged against the separation).

Part (a): finite reversible chain K on n states (n in 2..12), stationary pi, random partition into cells
(cells of size one forced in 1/3 of instances), random good set of cells (empty in 1/8, everything in 1/8).
 A = K on L2(pi).  Two families: 'rev' (reversible, any sign of spectrum) and 'psd' (K = K0^2, so 0<=A<=I).
 rho(c) = second singular value of the normalised conditional joint law of (X,Y) given C(X)=c
          (centred maximal correlation; rho := 0 when X or Y is degenerate given c).
 gamma := 1 - max_{c in good} rho(c)^2 (gamma := 1 if good set empty).  HYPOTHESIS per instance: gamma is
 then the largest admissible value, so every instance qualifies with this gamma; we also count gamma > 0.
 A1  lambda_min( D^{1/2}(I - A^2 - gamma G^*G)D^{-1/2} ) >= -TOL             [the proposition]
 A2  same quadratic form on 20 random COMPLEX f, >= -TOL                      [complex f]
 A3  G = 1_good(C)(I-P) equals Q - B with B = chi(I-P), chi = indicator of the complement of the good set;
     B self-adjoint in L2(pi), B^2 = B, QB = B                                [identification with t:inh]
 A4  step used in proof: Var(E[f(X)|Y,C=c] | C=c) <= rho(c)^2 Var(f(X)|C=c) for random complex f, every c
 A5  (attack, expected to fail) proposition with gamma replaced by 1 - mean_c rho(c)^2 over good cells
 A6  (attack, expected to fail) proposition for a NON-reversible K with A f = E[f(Y)|X], form
     <f,(I - A^*A) f>_pi  -- tests whether exchangeability is used
 A7  (attack, expected to fail) proposition with rho(c) replaced by the UNconditional maximal correlation
     ... i.e. gamma' = 1 - (second eigenvalue modulus of A)^2
Part (b):
 B1  |corr(f(X), g(Y) | C=c)| <= rho(c) + TOL for random real f, g, every non-degenerate cell
 B2  (attack, expected to fail) |corr(f(X), g(X,Y) | C=c)| <= rho(c): g allowed to depend on both slices
 B3  (attack, expected to fail) unconditional |corr(f(X), g(Y))| <= min_c rho(c)
 B4  smallest example: two states, X=Y, P(X=1)=eps: mutual information -> 0 while rho = 1; and the lazy
     version A=(1-d)I+dE: MI <= h(eps), rho = 1-d.  Printed, not a pass/fail predicate.
Part (c): PSD contraction A on R^d (d in 3..9), projections P, B<=Q, G=Q-B, integers m>=j>=1, k in 1..3m.
 gamma* = 1/lambda_max(G (I-A^{2k})^{-1} G) (largest gamma for the lag-k hypothesis; needs ||A||<1, G != 0).
 HYPOTHESIS per instance: verified by lambda_min(I - A^{2k} - gamma G) >= -TOL; count qualifying.
 kappa = ||B A^j B||, b = 1 - ||P A^m P|| (sharpest values), also loosened values.
 C1  1 - ||A^m|| >= (b-kappa)_+ / (1 + 2k/(m gamma)) - TOL, gamma in {gamma*, gamma*/2}      [r:lag]
 C2  (attack, expected to fail) same with denominator 1 + 2/(m gamma)  (k dropped)
 C3  (attack) C1 with j > m allowed (j in m+1..3m): is j<=m needed?
 Families: 'random' and 'block' (A nearly block-diagonal w.r.t. P,B,G with slow G block, so b-kappa>0).
 Counted: instances with k>m, instances with b-kappa>0.
"""
import sys, json
import numpy as np

TOL = 1e-9


def rand_partition(rng, n, force_single):
    ncell = int(rng.integers(1, n + 1))
    lab = rng.integers(0, ncell, size=n)
    if force_single and n >= 2:
        lab[0] = ncell  # a cell of size one
    _, lab = np.unique(lab, return_inverse=True)
    return lab


def rev_chain(rng, n, psd):
    W = rng.random((n, n)) ** int(rng.integers(1, 6))
    W = W + W.T
    if rng.random() < 0.3:
        W += np.diag(rng.random(n) * n * rng.random())
    pi = W.sum(1); K = W / pi[:, None]; pi = pi / pi.sum()
    if psd:
        K = K @ K
    return K, pi


def rho_cell(J):
    """J: joint law (rows x in cell, cols y), normalised. second singular value."""
    px = J.sum(1); py = J.sum(0)
    keep = py > 1e-300
    J = J[:, keep]; py = py[keep]
    if len(px) < 2 or len(py) < 2:
        return 0.0
    M = J / np.sqrt(px)[:, None] / np.sqrt(py)[None, :]
    s = np.linalg.svd(M, compute_uv=False)
    return float(s[1]) if len(s) > 1 else 0.0


def part_a(rng, N, res):
    cnt = {k: [0, 0] for k in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3']}  # [tested, failed]
    qual = 0; gpos = 0; minmargin = np.inf; n_single = 0; n_empty = 0; n_all = 0
    worst = {}
    for it in range(N):
        n = int(rng.integers(2, 13))
        psd = bool(it % 2)
        K, pi = rev_chain(rng, n, psd)
        force_single = (it % 3 == 0)
        lab = rand_partition(rng, n, force_single)
        ncell = lab.max() + 1
        r = rng.random()
        if r < 0.125:
            good = np.zeros(ncell, bool); n_empty += 1
        elif r < 0.25:
            good = np.ones(ncell, bool); n_all += 1
        else:
            good = rng.random(ncell) < 0.5
        if any((lab == c).sum() == 1 for c in range(ncell)):
            n_single += 1
        Jfull = pi[:, None] * K
        rho = np.zeros(ncell)
        for c in range(ncell):
            idx = np.where(lab == c)[0]
            J = Jfull[idx, :]; J = J / J.sum()
            rho[c] = rho_cell(J)
        gamma = 1.0 - (max(rho[good]) ** 2 if good.any() else 0.0)
        qual += 1
        if gamma > 1e-6:
            gpos += 1
        # operators on L2(pi)
        P = np.zeros((n, n))
        for c in range(ncell):
            idx = np.where(lab == c)[0]
            P[np.ix_(idx, idx)] = pi[idx][None, :] / pi[idx].sum()
        I = np.eye(n); Q = I - P
        ind = good[lab].astype(float)
        G = np.diag(ind) @ Q
        chi = np.diag(1.0 - ind)
        B = chi @ Q
        D = np.diag(pi); Dh = np.diag(np.sqrt(pi)); Dhi = np.diag(1 / np.sqrt(pi))

        def form(Gam):
            Mx = D @ (I - K @ K) - Gam * (G.T @ D @ G)
            S = Dhi @ Mx @ Dhi
            return 0.5 * (S + S.T)
        lam = np.linalg.eigvalsh(form(gamma))[0]
        cnt['A1'][0] += 1
        minmargin = min(minmargin, lam)
        if lam < -TOL:
            cnt['A1'][1] += 1; worst.setdefault('A1', dict(it=it, lam=lam))
        # A2 complex f
        Mx = D @ (I - K @ K) - gamma * (G.T @ D @ G)
        bad = False
        for _ in range(20):
            f = rng.standard_normal(n) + 1j * rng.standard_normal(n)
            v = np.real(np.conj(f) @ Mx @ f)
            if v < -TOL * np.real(np.conj(f) @ D @ f):
                bad = True
        cnt['A2'][0] += 1; cnt['A2'][1] += bad
        # A3
        ok = (np.allclose(G, Q - B, atol=1e-12) and np.allclose(B @ B, B, atol=1e-12)
              and np.allclose(D @ B, (D @ B).T, atol=1e-12) and np.allclose(Q @ B, B, atol=1e-12))
        cnt['A3'][0] += 1; cnt['A3'][1] += (not ok)
        # A4, B1, B2
        f = rng.standard_normal(n) + 1j * rng.standard_normal(n)
        fr = rng.standard_normal(n); gr = rng.standard_normal(n); g2 = rng.standard_normal((n, n))
        badA4 = badB1 = badB2 = False; anyB = False
        for c in range(ncell):
            idx = np.where(lab == c)[0]
            J = Jfull[idx, :]; J = J / J.sum()
            px = J.sum(1); py = J.sum(0)
            fx = f[idx]; mean = px @ fx; var = px @ np.abs(fx - mean) ** 2
            pred = (J.T @ fx) / np.where(py > 0, py, 1)
            vpred = py @ np.abs(pred - mean) ** 2
            if vpred > rho[c] ** 2 * var + TOL:
                badA4 = True
            a = fr[idx] - px @ fr[idx]; bb = gr - py @ gr
            va = px @ a ** 2; vb = py @ bb ** 2
            if va > 1e-12 and vb > 1e-12:
                anyB = True
                cor = abs(a @ J @ bb) / np.sqrt(va * vb)
                if cor > rho[c] + TOL:
                    badB1 = True
                h = g2[idx, :]; hm = (J * h).sum(); vh = (J * (h - hm) ** 2).sum()
                if vh > 1e-12:
                    cor2 = abs((J * (a[:, None] * (h - hm))).sum()) / np.sqrt(va * vh)
                    if cor2 > rho[c] + TOL:
                        badB2 = True
        cnt['A4'][0] += 1; cnt['A4'][1] += badA4
        if anyB:
            cnt['B1'][0] += 1; cnt['B1'][1] += badB1
            cnt['B2'][0] += 1; cnt['B2'][1] += badB2
            a = fr - pi @ fr; bb = gr - pi @ gr
            cor = abs(a @ Jfull @ bb) / np.sqrt((pi @ a ** 2) * (pi @ bb ** 2))
            nondeg = [rho[c] for c in range(ncell) if (lab == c).sum() > 1]
            if nondeg:
                cnt['B3'][0] += 1; cnt['B3'][1] += bool(cor > min(nondeg) + TOL)
        # A5 mean rho^2
        if good.sum() >= 2:
            g5 = 1.0 - np.mean(rho[good] ** 2)
            cnt['A5'][0] += 1; cnt['A5'][1] += bool(np.linalg.eigvalsh(form(g5))[0] < -TOL)
        # A7 unconditional
        ev = np.sort(np.abs(np.linalg.eigvals(K)))[::-1]
        g7 = 1.0 - ev[1] ** 2
        if good.any():
            cnt['A7'][0] += 1; cnt['A7'][1] += bool(np.linalg.eigvalsh(form(g7))[0] < -TOL)
        # A6 non-reversible
        Kn = rng.random((n, n)) ** 3; Kn /= Kn.sum(1)[:, None]
        w, V = np.linalg.eig(Kn.T); pn = np.real(V[:, np.argmax(np.real(w))]); pn = pn / pn.sum()
        Jn = pn[:, None] * Kn; rn = np.zeros(ncell); Pn = np.zeros((n, n))
        for c in range(ncell):
            idx = np.where(lab == c)[0]
            Jc = Jn[idx, :]; rn[c] = rho_cell(Jc / Jc.sum())
            Pn[np.ix_(idx, idx)] = pn[idx][None, :] / pn[idx].sum()
        if good.any():
            gn = 1.0 - max(rn[good]) ** 2
            Gn = np.diag(ind) @ (I - Pn); Dn = np.diag(pn)
            Mn = Dn - Kn.T @ Dn @ Kn - gn * (Gn.T @ Dn @ Gn)
            S = np.diag(pn ** -0.5) @ Mn @ np.diag(pn ** -0.5)
            cnt['A6'][0] += 1; cnt['A6'][1] += bool(np.linalg.eigvalsh(0.5 * (S + S.T))[0] < -TOL)
    res['part_a'] = dict(instances=N, hypothesis_qualifying=qual, gamma_positive=gpos,
                         with_singleton_cell=n_single, good_empty=n_empty, good_everything=n_all,
                         A1_min_eigenvalue=float(minmargin),
                         predicates={k: dict(tested=int(v[0]), failed=int(v[1])) for k, v in cnt.items()},
                         first_failures={k: {a: float(b) for a, b in v.items()} for k, v in worst.items()})


def part_b4(res):
    out = []
    for eps in [0.5, 1e-1, 1e-2, 1e-3, 1e-6]:
        h = -(eps * np.log(eps) + (1 - eps) * np.log(1 - eps))
        for d in [0.0, 0.1]:
            pi = np.array([1 - eps, eps])
            K = (1 - d) * np.eye(2) + d * np.outer(np.ones(2), pi)
            J = pi[:, None] * K
            mi = float(sum(J[i, k] * np.log(J[i, k] / (pi[i] * pi[k])) for i in range(2) for k in range(2) if J[i, k] > 0))
            f = np.array([1.0, -1.0])
            loss = float(pi @ (f - pi @ f) ** 2 - pi @ ((K @ (f - pi @ f)) ** 2))  # <f,(I-A^2)f>, f centred
            out.append(dict(eps=eps, d=d, entropy_nats=float(h), mutual_information_nats=mi,
                            rho=rho_cell(J), loss_over_norm2=loss / float(pi @ (f - pi @ f) ** 2)))
    res['part_b4'] = out


def rand_proj(rng, d, r):
    if r == 0:
        return np.zeros((d, d))
    Qm, _ = np.linalg.qr(rng.standard_normal((d, d)))
    U = Qm[:, :r]
    return U, Qm


def part_c(rng, N, res):
    cnt = {k: [0, 0] for k in ['C1', 'C2', 'C3']}
    qual = 0; kgtm = 0; bpos = 0; minslack = np.inf; skipped = 0; bpos_kgtm = 0
    tight = None
    for it in range(N):
        d = int(rng.integers(3, 10))
        Qm, _ = np.linalg.qr(rng.standard_normal((d, d)))
        rp = int(rng.integers(1, d - 1)); rb = int(rng.integers(0, d - rp)); rg = d - rp - rb
        if rg == 0:
            skipped += 1; continue
        Up = Qm[:, :rp]; Ub = Qm[:, rp:rp + rb]; Ug = Qm[:, rp + rb:]
        P = Up @ Up.T; B = Ub @ Ub.T; G = Ug @ Ug.T
        m = int(rng.integers(1, 9)); j = int(rng.integers(1, m + 1)); k = int(rng.integers(1, 3 * m + 1))
        if it % 2 == 0:
            Mr = rng.standard_normal((d, d)); A = Mr @ Mr.T
            A = A / np.linalg.eigvalsh(A)[-1] * rng.uniform(0.05, 0.999)
        else:
            ev = np.concatenate([rng.uniform(0, 0.6, rp), rng.uniform(0, 0.3, rb),
                                 rng.uniform(0.0, 0.999, rg) ** rng.uniform(0.05, 1)])
            A0 = Qm @ np.diag(ev) @ Qm.T
            E = rng.standard_normal((d, d)); E = (E + E.T) * rng.uniform(0, 0.05)
            w, V = np.linalg.eigh(A0 + E)
            A = V @ np.diag(np.clip(w, 0, 0.9995)) @ V.T
        I = np.eye(d)
        mp = np.linalg.matrix_power
        M = I - mp(A, 2 * k); M = 0.5 * (M + M.T)
        gs = 1.0 / np.linalg.eigvalsh(G @ np.linalg.inv(M) @ G)[-1]
        nAm = np.linalg.norm(mp(A, m), 2)
        b = 1 - np.linalg.norm(P @ mp(A, m) @ P, 2)
        for gam in (gs, gs / 2):
            hyp = np.linalg.eigvalsh(0.5 * ((M - gam * G) + (M - gam * G).T))[0] >= -TOL
            if not hyp:
                skipped += 1; continue
            qual += 1
            kap = np.linalg.norm(B @ mp(A, j) @ B, 2)
            if k > m: kgtm += 1
            if b - kap > 0:
                bpos += 1
                if k > m: bpos_kgtm += 1
            rhs = max(b - kap, 0) / (1 + 2 * k / (m * gam))
            slack = (1 - nAm) - rhs
            if slack < minslack:
                minslack = slack; tight = dict(it=it, d=d, m=m, j=j, k=k, gamma=float(gam), b=float(b), kappa=float(kap), lhs=float(1 - nAm), rhs=float(rhs))
            cnt['C1'][0] += 1; cnt['C1'][1] += bool(slack < -TOL)
            rhs2 = max(b - kap, 0) / (1 + 2 / (m * gam))
            cnt['C2'][0] += 1; cnt['C2'][1] += bool((1 - nAm) - rhs2 < -TOL)
            j3 = int(rng.integers(m + 1, 3 * m + 1))
            kap3 = np.linalg.norm(B @ mp(A, j3) @ B, 2)
            rhs3 = max(b - kap3, 0) / (1 + 2 * k / (m * gam))
            cnt['C3'][0] += 1; cnt['C3'][1] += bool((1 - nAm) - rhs3 < -TOL)
    res['part_c'] = dict(instances=N, hypothesis_checks_qualifying=qual, skipped=skipped, with_k_gt_m=kgtm,
                         with_b_minus_kappa_positive=bpos, both=bpos_kgtm, C1_min_slack=float(minslack),
                         tightest=tight,
                         predicates={k: dict(tested=int(v[0]), failed=int(v[1])) for k, v in cnt.items()})


def main():
    seed, na, nc, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    fh = open(out, 'x')
    rng = np.random.default_rng(seed)
    res = dict(command=' '.join(['python3'] + sys.argv), seed=seed, TOL=TOL, numpy=np.__version__,
               control=dict(x=0.5, rho=3, lhs=0.5 * (1 - 0.5 ** 3), rhs=3 * (1 - 0.5)))
    part_a(rng, na, res)
    part_b4(res)
    part_c(rng, nc, res)
    json.dump(res, fh, indent=1); fh.close()
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
