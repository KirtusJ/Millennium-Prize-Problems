"""chal.py -- r10 challenger of PROOF_FREE_BOUNDS.md. Own program, numpy only, deterministic (no randomness).

Test function (no reflection symmetry, complex Fourier coefficients):
  g(u) = exp( sin(2pi u1 + 0.3) + 0.7 cos(2pi u2) sin(2pi u3 + 1) + 0.4 sin(2pi(u1 + 2 u2)) ),  f(y) = g(y/ell).

PREDICATES (fixed before first run):
 Q0  f is non-symmetric: max|Im fhat_b(q)| / max|fhat_b| > 1e-2 at N=6 (else the A1 test is void).
 Q1  (A1) momentum form (2/l^6) sum_{k,k' in BZ, each mode once} |fhat_b(k+k')|^2 w w e^{-t(kh+kh')}
     equals position form 2 b^6 sum f f D_t^2, rel. err <= 1e-10, for N in {6,8,9}, ell in {1, 0.7},
     t in {0.05,0.1,0.2}*ell.  Tolerance: float64 sums of <= 10^6 positive terms, error ~1e-13; 1e-10 margin.
 Q1b (A1/A2 wording) LITERAL reading "BZ = all reps with |k_i b| <= pi" (boundary k_i b = +-pi both counted)
     at even N: my EXPECTATION is that it disagrees with position space by > 1e-6 (i.e. the literal reading is wrong
     and the mode must be counted once).  Predicate: rel. deviation > 1e-6 for N=6 and N=8.
 Q2  (A2) aliasing: fhat_b(q) = sum_m ftilde(q + 2pi m/b) for all q, N in {6,9}, rel to max <= 1e-10
     (ftilde from a 96^3 grid; f is entire, aliasing error of grid is below 1e-14).
 Q3  (A2) decay |ftilde(p)| <= D4/|p|^4 for all p != 0 on the 96^3 grid (|p|_inf < 48*2pi/ell).
 Q4  (A2) (2a) F_b = max_q |fhat_b(q)| <= ||f||_1 + S4u (b/pi)^4 D4 and (2b) |fhat_b(0)| >= |int f| - S4u (b/2pi)^4 D4,
     N = 3..16 (S4u = 16.5791 upper bound for (2a), for (2b) also 16.5791 since it is subtracted).
 Q5  (A2) for even N, q_i b = pi: |q + 2pi m/b| >= pi|m|/b for all m in [-6,6]^3, both reps q_i = +-pi/b.
 Q6  (A3) integral: 4pi int_0^inf r^2 (r + sqrt3/2) e^{-a r} dr = 4pi(6/a^4 + sqrt3/a^3), rel 1e-8 (quadrature).
 Q7  (A3) lattice sum sum_{n!=0}|n| e^{-a|n|} <= G(a) for a in {0.2,0.4,0.8,1.6,4,10}.
 Q8  (A3) S_b(t) <= (pi/l) sum_{n!=0}|n|e^{-4t|n|/l}, and C_b(t) <= (2/l^6) F_b^2 S_b^2 (factor_upper), N in {6,8,9,12}.
 Q9  (A3/A4) final: C_b(tau) <= V(tau) and v(tau) <= C_b(2tau) for all cases with b <= b0 (count qualifying first),
     N in {6,8,9,12,16}, ell in {1,0.7}, tau in {0.05,0.1,0.3}*ell. D4 used = 1.01 * D4(96 grid) (see Q10).
 Q10 D4 grid convergence: |D4(96) - D4(48)| / D4(96) < 1e-3 (justifies 1% safety factor).
 Q11 (A4) P33 = 1 exactly (1e-15) at k = +-e1, +-e2 (2pi/l); the four-pair partial sum equals
     (2/l^6)|fhat(0)|^2 kappa_N^2 e^{-2t kappa_N} (rel 1e-12); kappa_N increasing for N = 3..400.
 Q12 (A4) endpoint minimum: min over N>=3 of kappa_N^2 e^{-2t kappa_N} >= m(t) for t in {0.05..2}.
 M1  measured only: number of distinct energies vs number of pairs (degeneracy) at N=6.
"""
import numpy as np, json, os, sys
pi = np.pi
S4U = 16.5791
res = {"pred": {}, "meas": {}}
def P(name, ok, info):
    res["pred"][name] = {"ok": bool(ok), "info": info}
    print(("PASS " if ok else "FAIL ") + name, info, flush=True)

def g(u1, u2, u3):
    return np.exp(np.sin(2*pi*u1 + 0.3) + 0.7*np.cos(2*pi*u2)*np.sin(2*pi*u3 + 1) + 0.4*np.sin(2*pi*(u1 + 2*u2)))

def grid_f(N):
    u = np.arange(N)/N
    U1, U2, U3 = np.meshgrid(u, u, u, indexing="ij")
    return g(U1, U2, U3)

def fhat_b(N, ell):
    # fhat_b(q) at q = 2pi n/ell, n mod N: b^3 sum_x f(bx) e^{-i q.bx} = b^3 * fftn
    b = ell/N
    return b**3*np.fft.fftn(grid_f(N))

def kgrid(N, ell):
    n = np.fft.fftfreq(N, 1.0/N)  # integer reps in BZ, each once (for even N: -N/2 only)
    b = ell/N
    K = np.meshgrid(*(2*pi*n/ell,)*3, indexing="ij")
    kh = [(2/b)*np.sin(Ki*b/2) for Ki in K]
    kh2 = kh[0]**2 + kh[1]**2 + kh[2]**2
    with np.errstate(invalid="ignore", divide="ignore"):
        P33 = (kh[0]**2 + kh[1]**2)/kh2
        khat = np.sqrt(kh2)
        w = P33*khat/2
    w[0, 0, 0] = 0.0; P33[0, 0, 0] = 0.0
    return K, khat, w, P33

def C_pos(N, ell, t):
    b = ell/N
    K, khat, w, _ = kgrid(N, ell)
    u = w*np.exp(-t*khat)
    # D(x) = l^-3 sum_k e^{ik.bx} u(k) = l^-3 * N^3 * ifftn(u)
    D = (N**3/ell**3)*np.fft.ifftn(u)
    assert np.max(np.abs(D.imag)) < 1e-9*np.max(np.abs(D.real))
    D = D.real
    F = grid_f(N)
    # sum_{x,y} f(x) f(y) D(x-y)^2 via circular correlation
    D2 = D**2
    conv = np.fft.ifftn(np.fft.fftn(F)*np.conj(np.fft.fftn(F))).real  # sum_y f(y+r) f(y)
    return 2*b**6*np.sum(conv*D2)

def C_pos_direct(N, ell, t):
    # brute force double loop over positions (no FFT for the f-sum), for N<=9
    b = ell/N
    K, khat, w, _ = kgrid(N, ell)
    u = w*np.exp(-t*khat)
    D = ((N**3/ell**3)*np.fft.ifftn(u)).real
    F = grid_f(N).ravel()
    idx = np.array(np.unravel_index(np.arange(N**3), (N,)*3)).T
    tot = 0.0
    for a in range(N**3):
        r = (idx[a] - idx) % N
        tot += F[a]*np.sum(F*D[r[:, 0], r[:, 1], r[:, 2]]**2)
    return 2*b**6*tot

def C_mom(N, ell, t, literal=False):
    b = ell/N
    fh = fhat_b(N, ell)
    if not literal:
        reps = [np.fft.fftfreq(N, 1.0/N).astype(int)]*3
    else:
        r = np.arange(-(N//2), N//2 + 1)  # for even N both -N/2 and +N/2
        reps = [r]*3
    n = np.array(np.meshgrid(*reps, indexing="ij")).reshape(3, -1).T
    k = 2*pi*n/ell
    kh = (2/b)*np.sin(k*b/2)
    kh2 = np.sum(kh**2, axis=1)
    nz = kh2 > 1e-300
    n, kh, kh2 = n[nz], kh[nz], kh2[nz]
    khat = np.sqrt(kh2)
    w = (kh[:, 0]**2 + kh[:, 1]**2)/kh2*khat/2
    u = w*np.exp(-t*khat)
    tot = 0.0
    for i in range(len(n)):
        s = (n[i] + n) % N
        tot += u[i]*np.sum(np.abs(fh[s[:, 0], s[:, 1], s[:, 2]])**2*u)
    return 2/ell**6*tot

def fine_coeffs(M, ell):
    # ftilde(p) = int_T f e^{-ip.y} dy for p = 2pi m/ell, from M^3 grid (trapezoid = exact up to aliasing)
    return (ell/M)**3*np.fft.fftn(grid_f(M))

def norms(M, ell):
    F = grid_f(M)
    m = np.fft.fftfreq(M, 1.0/M)
    Kx = np.meshgrid(*(2*pi*m/ell,)*3, indexing="ij")
    k2 = Kx[0]**2 + Kx[1]**2 + Kx[2]**2
    L2 = np.fft.ifftn(k2**2*np.fft.fftn(F)).real
    h3 = (ell/M)**3
    return {"intf": h3*F.sum(), "L1": h3*np.abs(F).sum(), "D4": h3*np.abs(L2).sum()}

if __name__ == "__main__":
    out = sys.argv[1]
    assert not os.path.exists(out), "result file exists; never overwrite"

    # Q0
    fh6 = fhat_b(6, 1.0)
    r0 = np.max(np.abs(fh6.imag))/np.max(np.abs(fh6))
    P("Q0_nonsymmetric", r0 > 1e-2, {"max|Im|/max": r0})

    # Q1, Q1b
    worst = 0.0; rows = []
    for ell in (1.0, 0.7):
        for N in (6, 8, 9):
            for tt in (0.05, 0.1, 0.2):
                t = tt*ell
                cp = C_pos(N, ell, t); cm = C_mom(N, ell, t)
                e = abs(cp - cm)/abs(cp); worst = max(worst, e)
                rows.append([ell, N, t, cp, cm, e])
    # one fully direct position-space check (no FFT in the x,y sum) at N=6 and 9
    for N in (6, 9):
        cpd = C_pos_direct(N, 1.0, 0.1); cm = C_mom(N, 1.0, 0.1)
        e = abs(cpd - cm)/cpd; worst = max(worst, e); rows.append([1.0, N, 0.1, cpd, cm, e, "direct"])
    P("Q1_momentum_rep", worst <= 1e-10, {"worst_rel": worst, "cases": len(rows)})
    res["meas"]["Q1_rows"] = rows
    devs = {}
    for N in (6, 8):
        cp = C_pos(N, 1.0, 0.1); cl = C_mom(N, 1.0, 0.1, literal=True)
        devs[N] = (cl - cp)/cp
    P("Q1b_literal_BZ_double_count_disagrees", all(abs(d) > 1e-6 for d in devs.values()), {"rel_dev": devs})

    # norms and D4
    n48 = norms(48, 1.0); n96 = norms(96, 1.0)
    d4c = abs(n96["D4"] - n48["D4"])/n96["D4"]
    P("Q10_D4_grid", d4c < 1e-3, {"D4_48": n48["D4"], "D4_96": n96["D4"], "rel": d4c, "intf": n96["intf"], "L1": n96["L1"]})

    # Q2 aliasing and Q3 decay (ell = 1)
    M = 96; ft = fine_coeffs(M, 1.0)
    werr = 0.0
    for N in (6, 9):
        fh = fhat_b(N, 1.0)
        m = np.arange(M); cls = m % N
        al = np.zeros((N, N, N), complex)
        # sum over fine modes congruent mod N (fine index m represents p = 2pi m/ell with m in fftfreq sense; m mod N is same)
        mm = np.fft.fftfreq(M, 1.0/M).astype(int) % N
        for a in range(N):
            for b_ in range(N):
                for c in range(N):
                    al[a, b_, c] = ft[np.ix_(mm == a, mm == b_, mm == c)].sum()
        werr = max(werr, np.max(np.abs(al - fh))/np.max(np.abs(fh)))
    P("Q2_aliasing", werr <= 1e-10, {"max_rel": werr, "note": "M=96 requires N | 96? no: congruence classes mod N of integer modes; valid since f entire, |ftilde| at |m|~48 negligible"})
    mf = np.fft.fftfreq(M, 1.0/M)
    Km = np.meshgrid(*(2*pi*mf,)*3, indexing="ij")
    pn = np.sqrt(Km[0]**2 + Km[1]**2 + Km[2]**2)
    D4 = n96["D4"]
    msk = pn > 0
    ratio = np.max(np.abs(ft[msk])*pn[msk]**4/D4)
    P("Q3_decay", ratio <= 1.0, {"max |ftilde||p|^4/D4": ratio})

    # Q4
    q4 = []; ok4 = True
    D4u = 1.01*D4
    for N in range(3, 17):
        b = 1.0/N; fh = fhat_b(N, 1.0)
        Fb = np.max(np.abs(fh)); up = n96["L1"] + S4U*(b/pi)**4*D4u
        f0 = abs(fh[0, 0, 0]); lo = abs(n96["intf"]) - S4U*(b/(2*pi))**4*D4u
        ok4 &= (Fb <= up) and (f0 >= lo)
        q4.append([N, Fb, up, f0, lo])
    P("Q4_2a_2b", ok4, {"rows[N,Fb,up,f0,lo]": q4})

    # Q5 boundary
    ok5 = True; minr = 1e9
    rng = np.arange(-6, 7)
    mg = np.array(np.meshgrid(rng, rng, rng, indexing="ij")).reshape(3, -1).T
    mg = mg[np.any(mg != 0, axis=1)]
    for N in (4, 6, 8, 10):
        b = 1.0/N
        for s1 in (1, -1):
            for q23 in ([pi/b*s1, 0.3], [-pi/b, pi/b]):
                q = np.array([s1*pi/b, q23[0], q23[1]])
                lhs = np.linalg.norm(q + 2*pi*mg/b, axis=1); rhs = pi*np.linalg.norm(mg, axis=1)/b
                minr = min(minr, np.min(lhs/rhs)); ok5 &= np.all(lhs >= rhs*(1 - 1e-14))
    P("Q5_boundary_alias_ineq", ok5, {"min lhs/rhs": minr})

    # Q6 integral
    ok6 = True; q6 = []
    for a in (0.2, 1.0, 3.0):
        r = np.linspace(0, 80/a, 400001); y = r**2*(r + np.sqrt(3)/2)*np.exp(-a*r)
        I = 4*pi*np.trapezoid(y, r); J = 4*pi*(6/a**4 + np.sqrt(3)/a**3)
        ok6 &= abs(I - J)/J < 1e-8; q6.append([a, I, J])
    P("Q6_integral", ok6, q6)

    # Q7 lattice sum
    def G(a): return 4*pi*np.exp(np.sqrt(3)*a/2)*(6/a**4 + np.sqrt(3)/a**3)
    def latsum(a):
        L = int(np.ceil(36/a)) + 2
        r = np.arange(-L, L + 1)
        tot = 0.0
        n2 = (r[:, None]**2 + r[None, :]**2).astype(float)
        for n3 in r:
            nn = np.sqrt(n2 + n3**2)
            tot += np.sum(nn*np.exp(-a*nn))
        return tot
    q7 = []; ok7 = True
    for a in (0.2, 0.4, 0.8, 1.6, 4.0, 10.0):
        s = latsum(a); q7.append([a, s, G(a), G(a)/s]); ok7 &= s <= G(a)
    P("Q7_lattice_sum", ok7, q7)

    # Q8, Q9
    ok8 = True; q8 = []
    for N in (6, 8, 9, 12):
        for t in (0.05, 0.1, 0.3):
            ell = 1.0; K, khat, w, _ = kgrid(N, ell)
            Sb = np.sum(w*np.exp(-t*khat)); bound = pi/ell*latsum(4*t/ell)
            Fb = np.max(np.abs(fhat_b(N, ell))); C = C_pos(N, ell, t)
            fu = 2/ell**6*Fb**2*Sb**2
            ok8 &= (Sb <= bound) and (C <= fu); q8.append([N, t, Sb, bound, C, fu])
    P("Q8_Sb_and_factor_upper", ok8, q8)

    q9 = []; qual = 0; ok9 = True; notq = []
    for ell in (1.0, 0.7):
        nm = {"intf": n96["intf"]*ell**3, "L1": n96["L1"]*ell**3, "D4": D4u*ell**-1}  # exact scaling of f(y/ell)
        b0 = min(ell/3, 2*pi*(abs(nm["intf"])/(2*S4U*nm["D4"]))**0.25)
        F = nm["L1"] + S4U*(b0/pi)**4*nm["D4"]
        k3 = 3*np.sqrt(3)/ell
        def m(t): return min(k3**2*np.exp(-2*t*k3), (2*pi/ell)**2*np.exp(-4*pi*t/ell))
        for N in (6, 8, 9, 12, 16):
            b = ell/N
            for tt in (0.05, 0.1, 0.3):
                tau = tt*ell
                V = 2/ell**6*F**2*(pi/ell)**2*G(4*tau/ell)**2
                v = 2/ell**6*nm["intf"]**2/4*m(2*tau)
                C1 = C_pos(N, ell, tau); C2 = C_pos(N, ell, 2*tau)
                row = [ell, N, tau, b, b0, v, C2, C1, V]
                if b <= b0:
                    qual += 1; ok9 &= (v <= C2) and (C1 <= V); q9.append(row)
                else:
                    notq.append(row + [v <= C2, C1 <= V])
    P("Q9_final_bracket", ok9 and qual > 0, {"qualifying": qual, "of": 30, "rows": q9})
    res["meas"]["Q9_nonqualifying_b_gt_b0"] = notq

    # Q11
    ok11 = True; info11 = []
    for N in (3, 4, 6, 9):
        ell = 1.0; b = ell/N; K, khat, w, P33 = kgrid(N, ell)
        kap = 2*N/ell*np.sin(pi/N)
        for idx in [(1, 0, 0), (N - 1, 0, 0), (0, 1, 0), (0, N - 1, 0)]:
            ok11 &= abs(P33[idx] - 1) < 1e-15 and abs(w[idx] - kap/2) < 1e-12*kap
        t = 0.1; fh0 = abs(fhat_b(N, ell)[0, 0, 0])
        four = 4*2/ell**6*fh0**2*(kap/2)**2*np.exp(-2*t*kap)
        claim = 2/ell**6*fh0**2*kap**2*np.exp(-2*t*kap)
        ok11 &= abs(four - claim) <= 1e-12*claim
        info11.append([N, kap, P33[0, 0, 1] if N > 1 else None])
    Ns = np.arange(3, 401); kaps = 2*Ns*np.sin(pi/Ns)
    ok11 &= bool(np.all(np.diff(kaps) > 0))
    P("Q11_lower_pairs", ok11, {"rows[N,kappa,P33(e3)]": info11, "kappa3": kaps[0], "3sqrt3": 3*np.sqrt(3)})

    ok12 = True; q12 = []
    k3 = 3*np.sqrt(3)
    for t in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        mn = np.min(kaps**2*np.exp(-2*t*kaps)); mt = min(k3**2*np.exp(-2*t*k3), (2*pi)**2*np.exp(-4*pi*t))
        ok12 &= mn >= mt*(1 - 1e-14); q12.append([t, mn, mt])
    P("Q12_endpoint_min", ok12, q12)

    # M1 degeneracy
    K, khat, w, _ = kgrid(6, 1.0)
    kh = khat.ravel()[1:]
    E = np.add.outer(kh, kh).ravel()
    res["meas"]["M1_pairs_vs_distinct_E"] = [len(E), len(np.unique(np.round(E, 10)))]
    print("M1", res["meas"]["M1_pairs_vs_distinct_E"])

    with open(out, "w") as fp:
        json.dump(res, fp, indent=1, default=float)
    nf = sum(1 for v in res["pred"].values() if not v["ok"])
    print("met", len(res["pred"]) - nf, "failed", nf)
    sys.exit(0)
