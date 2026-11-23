"""gap_dh.py -- checks for gaps (3) Delta h  and (4) DG1/DG3 of tun_lower.tex.

Notation (tun_lower.tex Sec. 6): U_i=(x0_i,u_i), |u_i|=sin a_i, S^2=|u1|^2+|u2|^2, w=u1 x u2, W=|w|^2,
h(S)=1+sqrt(1+S^2)/S, A=1+2hS^2, e(S)=2 asinh S, b=sqrt(beta) w,
ell zeta = R1 zeta1 x u2 + u1 x R2 zeta2, R_i = x0_i I + [u_i]_x,  p = -(Psi' u1hat, Theta' u2hat),
kappa = Psi' cot a1 + Theta' cot a2,  sigma_w^2 = S^2-2W,  D_w = 1+2h sigma_w^2.
J = E exp(-h|b+ell zeta|^2 + p.zeta), zeta~N(0,I6), computed DIRECTLY by
   J = det(Q)^{-1/2} exp(v^T Q^{-1} v/2 - h|b|^2), Q=I+2h ell^T ell, v = p-2h ell^T b.
gap = [-e(S)+|p|^2/2] - [(h-2)|b|^2 + log J].

PREDICATES (fixed before first run). Sample: seed 20261123, N=200000 random configurations:
a1 uniform in [0.05, pi-0.05], a2 uniform in [0.001, pi-0.001] (half the samples with a2 in [0.001,0.3]),
u-directions uniform on S^2, beta = 10^U[1,8], Psi' in U[0,2], Theta' in U[0,1], |b| up to sqrt(beta)|w| as given.
  Q1 flat identity (h-2)(1+2S^2h)=h and log(1+2S^2h)=e(S)                     tol 1e-12 relative
  Q2 ell p = -kappa w                                                          tol 1e-12
  Q3 closed form  gap = 1/2 log(1-x) + 1/2 log(1+h x) + h x|b|^2/D_w + h(kappa^2/beta - 2 kappa/sqrt beta)|b|^2/D_w,
     x = 4hW/A, equals the direct gap                                         tol 1e-9 * (1+|terms|) (double rounding in logdet)
  Q4 D_w >= 1 (i.e. sigma_w^2 >= 0)                                            tol 0
  Q5 gap <= DG1' := 2h^2|b|^2/(beta A) + 4h^2|b|^4/(beta A D_w) + h kappa^2|b|^2/(beta D_w) + 2h|kappa||b|^2/(sqrt(beta) D_w)
  Q6 DG1' <= DG1 (stated, tun_lower.tex Lemma tu:L-gauss), on samples with sigma_w>0
  Q7 -gap3 <= DG3' := 2h|b|^2/(beta D_w) + 2h|kappa3||b|^2/(sqrt(beta) D_w)   (gap3: Theta'=0)
  Q8 DG3' <= DG3 (stated)
  tolerance for Q5-Q8: 1e-9*(1+|gap|) (rounding of Q3-type computation)
Delta h part, seed 7, N=200000: random U1,U2 (a_i as above), r_b = 10^U[-6,-0.3] (<= 0.5), xi_i uniform in ball |xi_i|<=r_b,
g_i=(sqrt(1-|xi_i|^2), xi_i), U_i' = U_i g_i (quaternion product), S'^2 from U'.
  H1 |S'^2-S^2| <= DS2 := 2 sum_i (sin a_i r_b + r_b^2)                         tol 1e-13
  H2 if DS2 < S^2: |h(S')-h(S)| <= DS2/(2 sm^2 sqrt(1+1/sm)), sm=S^2-DS2       tol 1e-12 relative
  H3 if r_b <= S/8: DS2 <= S^2/2 and |h(S')-h(S)| <= 4 r_b/S^2 + 4 sqrt2 r_b^2/S^3 <= 5 r_b/S^2   tol 1e-12 relative
Report counts of samples qualifying for each hypothesis. Output results/gap_dh.txt (mode "x").
"""
import math, sys, os
import numpy as np

def cross_mat(u):
    return np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])

def hS(S):
    return 1 + math.sqrt(1 + S * S) / S

def unit(rng):
    v = rng.normal(size=3); return v / np.linalg.norm(v)

def qmul(a, b):
    a0, av = a; b0, bv = b
    return (a0 * b0 - av @ bv, a0 * bv + b0 * av + np.cross(av, bv))

def main():
    out = open(os.path.join("results", "gap_dh.txt"), "x")
    def rep(s):
        print(s); out.write(s + "\n")
    rng = np.random.default_rng(20261123)
    N = 200000
    cnt = dict(Q1=[0, 0], Q2=[0, 0], Q3=[0, 0], Q4=[0, 0], Q5=[0, 0], Q6=[0, 0], Q7=[0, 0], Q8=[0, 0])
    worst = {k: -np.inf for k in cnt}
    q6_qual = 0
    fails = []
    def mark(k, ok, margin, info):
        cnt[k][0 if ok else 1] += 1
        worst[k] = max(worst[k], margin)
        if not ok and len([f for f in fails if f[0] == k]) < 5:
            fails.append((k, info))
    for n in range(N):
        a1 = rng.uniform(0.05, math.pi - 0.05)
        a2 = rng.uniform(0.001, 0.3) if n % 2 else rng.uniform(0.001, math.pi - 0.001)
        n1, n2 = unit(rng), unit(rng)
        x01, x02 = math.cos(a1), math.cos(a2)
        u1, u2 = math.sin(a1) * n1, math.sin(a2) * n2
        beta = 10 ** rng.uniform(1, 8)
        Pp, Tp = rng.uniform(0, 2), rng.uniform(0, 1)
        S2 = u1 @ u1 + u2 @ u2; S = math.sqrt(S2)
        w = np.cross(u1, u2); W = w @ w
        h = hS(S); A = 1 + 2 * h * S2; eS = 2 * math.asinh(S)
        r1 = abs((h - 2) * A - h) / h; r1b = abs(math.log(A) - eS) / max(eS, 1e-300)
        mark("Q1", r1 < 1e-12 and r1b < 1e-12, max(r1, r1b), (a1, a2))
        R1 = x01 * np.eye(3) + cross_mat(u1); R2 = x02 * np.eye(3) + cross_mat(u2)
        ell = np.hstack([-cross_mat(u2) @ R1, cross_mat(u1) @ R2])
        b = math.sqrt(beta) * w; B2 = b @ b
        for which in ("full", "psi"):
            Tq = Tp if which == "full" else 0.0
            p = -np.concatenate([Pp * n1, Tq * n2])
            kappa = Pp * x01 / math.sin(a1) + Tq * x02 / math.sin(a2)
            if which == "full":
                r2 = np.linalg.norm(ell @ p + kappa * w)
                mark("Q2", r2 < 1e-12 * (1 + abs(kappa)), r2, (a1, a2))
            Q = np.eye(6) + 2 * h * ell.T @ ell
            v = p - 2 * h * ell.T @ b
            sign, logdet = np.linalg.slogdet(Q)
            logJ = -0.5 * logdet + 0.5 * v @ np.linalg.solve(Q, v) - h * B2
            gap = (-eS + p @ p / 2) - ((h - 2) * B2 + logJ)
            x = 4 * h * W / A
            sw2 = S2 - 2 * W; Dw = 1 + 2 * h * sw2
            terms = [0.5 * math.log1p(-x), 0.5 * math.log1p(h * x), h * x * B2 / Dw,
                     h * (kappa**2 / beta - 2 * kappa / math.sqrt(beta)) * B2 / Dw]
            closed = sum(terms)
            scale = 1 + sum(abs(t) for t in terms) + abs(logJ) + abs((h - 2) * B2)
            tol = 1e-9 * scale
            if which == "full":
                r3 = abs(closed - gap)
                mark("Q3", r3 <= tol, r3 / scale, (a1, a2, beta))
                mark("Q4", sw2 >= 0 and Dw >= 1, -sw2, (a1, a2))
                DG1p = 2 * h * h * B2 / (beta * A) + 4 * h * h * B2**2 / (beta * A * Dw) + h * kappa**2 * B2 / (beta * Dw) \
                    + 2 * h * abs(kappa) * B2 / (math.sqrt(beta) * Dw)
                mark("Q5", gap <= DG1p + tol, gap - DG1p, (a1, a2, beta, gap, DG1p))
                if sw2 > 0:
                    q6_qual += 1
                    DG1 = 2 * h * B2 / (beta * S2) + kappa**2 * B2 / (2 * beta * sw2) + abs(kappa) * B2 / (math.sqrt(beta) * sw2) \
                        + 4 * h * h * B2**2 / beta
                    mark("Q6", DG1p <= DG1 * (1 + 1e-12) + 1e-300, DG1p - DG1, (a1, a2, beta))
            else:
                DG3p = 2 * h * B2 / (beta * Dw) + 2 * h * abs(kappa) * B2 / (math.sqrt(beta) * Dw)
                mark("Q7", -gap <= DG3p + tol, -gap - DG3p, (a1, a2, beta, gap, DG3p))
                if sw2 > 0:
                    DG3 = h * (2 + 2 / S2) * B2 / beta + abs(kappa) * B2 / (math.sqrt(beta) * sw2)
                    mark("Q8", DG3p <= DG3 * (1 + 1e-12) + 1e-300, DG3p - DG3, (a1, a2, beta))
    rep(f"gap part: N={N}, Q6/Q8 hypothesis sigma_w>0 qualified in {q6_qual} of {N}")
    for k in cnt:
        rep(f"  {k}: met {cnt[k][0]}, failed {cnt[k][1]}, worst margin (positive = violation side) {worst[k]:.3e}")
    # Delta h part
    rng = np.random.default_rng(7)
    hc = dict(H1=[0, 0], H2=[0, 0], H3=[0, 0]); hq = dict(H2=0, H3=0); hw = {k: -np.inf for k in hc}
    for n in range(N):
        a = [rng.uniform(0.05, math.pi - 0.05), rng.uniform(0.001, 0.3) if n % 2 else rng.uniform(0.001, math.pi - 0.001)]
        if n % 5 == 0:
            a[0] = rng.uniform(0.001, 0.05)
        rb = 10 ** rng.uniform(-6, math.log10(0.5))
        U = [(math.cos(ai), math.sin(ai) * unit(rng)) for ai in a]
        Up = []
        for Ui in U:
            xi = unit(rng) * rb * rng.uniform() ** (1 / 3)
            gq = (math.sqrt(1 - xi @ xi), xi)
            Up.append(qmul(Ui, gq))
        S2 = sum(1 - Ui[0]**2 for Ui in U); S2p = sum(1 - Ui[0]**2 for Ui in Up)
        DS2 = 2 * sum(math.sin(ai) * rb + rb * rb for ai in a)
        e1 = abs(S2p - S2) - DS2
        ok = e1 <= 1e-13; hc["H1"][0 if ok else 1] += 1; hw["H1"] = max(hw["H1"], e1)
        if not ok and len(fails) < 40: fails.append(("H1", a, rb))
        S, Sp = math.sqrt(S2), math.sqrt(S2p)
        dh = abs(hS(Sp) - hS(S))
        if DS2 < S2:
            hq["H2"] += 1
            sm = S2 - DS2
            bnd = DS2 / (2 * sm * sm * math.sqrt(1 + 1 / sm))
            ok = dh <= bnd * (1 + 1e-12); hc["H2"][0 if ok else 1] += 1; hw["H2"] = max(hw["H2"], dh / bnd)
            if not ok and len(fails) < 40: fails.append(("H2", a, rb))
        if rb <= S / 8:
            hq["H3"] += 1
            b1 = 4 * rb / S2 + 4 * math.sqrt(2) * rb * rb / S**3
            ok = DS2 <= S2 / 2 and dh <= b1 * (1 + 1e-12) and b1 <= 5 * rb / S2 * (1 + 1e-12)
            hc["H3"][0 if ok else 1] += 1; hw["H3"] = max(hw["H3"], dh / b1)
            if not ok and len(fails) < 40: fails.append(("H3", a, rb))
    rep(f"Delta h part: N={N}; H2 hypothesis DS2<S^2 qualified {hq['H2']}; H3 hypothesis r_b<=S/8 qualified {hq['H3']}")
    for k in hc:
        rep(f"  {k}: met {hc[k][0]}, failed {hc[k][1]}, worst {'excess' if k=='H1' else 'ratio dh/bound'} {hw[k]:.3e}")
    rep(f"FAILED (first few): {fails}")
    out.close()
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
