"""oned_split.py -- worker o1-lower (T141). One-dimensional tunnelling model.

MODEL (discrete, exact algebra): N points x_i = -pi + 2 pi i/N on the circle, N % 4 == 0,
h = 2 pi/N.  eps(a) = 2 asinh|sin a|.  K_ij = h * sum_{k=-1,0,1} sqrt(beta/2pi) exp(-beta (x_i-x_j+2pi k)^2/2).
T_ij = e^{-eps_i/2} K_ij e^{-eps_j/2}.  sigma: i -> i + N/2.  A = {x in [-pi/2, pi/2)}.
Sector matrices on A: T+ = T_AA + R, T- = T_AA - R, R_ij = T_{i, sigma j}.  g = top eigvec of T+,
f = top eigvec of T- (= restrictions to A of the even / odd top eigenvectors).
Delta = lam_e - lam_o is computed from the EXACT identity  Delta <f,g>_A = 2 <f, R g>_A
(which is (I0) of TUNNEL_LOWER.md restricted to the half A) after conjugating by the weight
exp(sqrt(beta) Psi), Psi(x) = int_0^{|x|} sqrt(2 eps) (Agmon distance to the nearest well), so that
weighted eigenvectors are O(1) and tails are relatively accurate.

Bounds tested (TUNNEL_LOWER.md):
  LB  (I1)  = 2 sum_{f_i f_j<0} T_ij |f_i||f_j| / ||f||^2  = 2 <|f_A|, R |f_A|> / ||f_A||^2  when f_A >= 0.
  UB  (sign trial, TUNNEL_THEOREM sec.5) = 2 <g_A, R g_A>/||g_A||^2.
  SUB (comparison-principle subsolution, (I3)): phi = exp(-sqrt(beta) Psi_eta), Psi_eta = int_0^{|x|} sqrt(2(eps+eta));
        measured r_min = min over Omega = {eps >= eta} of (T phi)_i / (lam_e phi_i).

PREDICATES (fixed before the first run):
 P1 identity: at beta = 16 and 32 (direct subtraction resolvable: Delta ~ 1e-8 .. 1e-11),
    |Delta_id - Delta_direct| / Delta_direct < 1e-3.  Tolerance: direct subtraction loses
    ~1e-16/Delta relative => 1e-8 .. 1e-5; 1e-3 leaves margin.
 P2 sign hypothesis: f_A > 0 entrywise (needed only for the equality LB = 2<f,Rf>/|f|^2 form) -- per case.
 P3 LB <= Delta*(1+1e-9) for all beta (theorem (I1); tolerance = double rounding over ~1e3-term sums).
 P4 Delta <= UB*(1+1e-9) for all beta (theorem, sign trial).
 P5 (expectation) LB is sharp in exponent: log(Delta/LB)/sqrt(beta) < 0.05 for beta >= 1024.
 P6 (expectation) |-log(Delta)/sqrt(beta) - c*| < 0.3 at beta = 4096 and decreasing in beta over 256..4096.
 P7 (expectation, discretisation) |log Delta(h) - log Delta(h/2)| < 0.01*|log Delta| at beta = 256, 1024.
 P8 (expectation) subsolution: r_min >= 1 for eta = 0.25 at beta in {256,1024,4096}.
No randomness is used (seed fixed at 0 for form).  Output: results_<tag>.txt opened with mode "x".
"""
import sys, math
import numpy as np

np.random.seed(0)
CSTAR = None


def eps(a):
    return 2.0 * np.arcsinh(np.abs(np.sin(a)))


def cstar():
    a = np.linspace(0, math.pi, 200001)
    y = np.sqrt(2 * eps(a))
    return float(np.sum((y[1:] + y[:-1]) / 2) * (a[1] - a[0]))


def psi(x, eta=0.0, M=20001):
    """Psi_eta(x) = int_0^{|x|} sqrt(2(eps+eta)) for |x| <= pi/2, symmetric about pi/2 and pi beyond."""
    xx = np.abs(np.mod(x + math.pi, 2 * math.pi) - math.pi)   # in [0, pi]
    d = np.minimum(xx, math.pi - xx)                           # distance to nearest well in [0, pi/2]
    t = np.linspace(0, math.pi / 2, M)
    y = np.sqrt(2 * (eps(t) + eta))
    cum = np.concatenate([[0.0], np.cumsum((y[1:] + y[:-1]) / 2 * (t[1] - t[0]))])
    return np.interp(d, t, cum)


def build(beta, N):
    x = -math.pi + 2 * math.pi * np.arange(N) / N
    h = 2 * math.pi / N
    D = x[:, None] - x[None, :]
    K = np.zeros((N, N))
    for k in (-1, 0, 1):
        K += np.exp(-beta * (D + 2 * math.pi * k) ** 2 / 2)
    K *= h * math.sqrt(beta / (2 * math.pi))
    e = eps(x)
    T = np.exp(-e / 2)[:, None] * K * np.exp(-e / 2)[None, :]
    return x, T


def top(M):
    w, V = np.linalg.eig(M)
    k = np.argmax(w.real)
    v = V[:, k].real
    if v[np.argmax(np.abs(v))] < 0:
        v = -v
    return w[k].real, v


def run(beta, hfac):
    N = int(math.ceil(2 * math.pi * math.sqrt(beta) / hfac / 4.0)) * 4
    x, T = build(beta, N)
    A = np.arange(N // 4, 3 * N // 4)
    sA = (A + N // 2) % N
    TAA = T[np.ix_(A, A)]
    R = T[np.ix_(A, sA)]
    sb = math.sqrt(beta)
    P = psi(x[A])
    Wl = np.exp(sb * (P[:, None] - P[None, :]))
    lam_e, gw = top((TAA + R) * Wl)
    lam_o, fw = top((TAA - R) * Wl)
    # unweighted vectors: g = e^{-sb P} gw ; work with logs to be safe
    s = np.exp(-sb * P)
    g = gw * s
    f = fw * s
    fg = float(np.sum(f * g))
    Delta = 2 * float(f @ R @ g) / fg
    fpos = bool(np.all(f > 0))
    af = np.abs(f)
    # LB from (I1) on the full circle: sum over f_i f_j < 0 of T|f||f| *2 / ||f||^2, f_full odd
    ffull = np.zeros(N); ffull[A] = f; ffull[sA] = -f
    S = np.sign(ffull)
    neg = (S[:, None] * S[None, :]) < 0
    aff = np.abs(ffull)
    LB = 2 * float(np.sum(T * neg * aff[:, None] * aff[None, :])) / float(np.sum(ffull ** 2))
    UB = 2 * float(g @ R @ g) / float(g @ g)
    direct = lam_e - lam_o
    # subsolution check, eta = 0.25, on the full circle
    eta = 0.25
    Pe = psi(x, eta)
    ratio = (T * np.exp(-sb * (Pe[None, :] - Pe[:, None]))).sum(axis=1) / lam_e
    Om = eps(x) >= eta
    rmin = float(ratio[Om].min())
    return dict(beta=beta, N=N, hfac=hfac, lam_e=lam_e, lam_o=lam_o, direct=direct, Delta=Delta,
                LB=LB, UB=UB, fpos=fpos, rmin=rmin, gcut_rel=float(np.log(g[np.argmin(np.abs(x[A] - math.pi / 2 + 1e-12))] if False else g[-1]) - np.log(g.max())))


def main():
    tag = sys.argv[1]
    betas = [float(b) for b in sys.argv[2].split(",")]
    hfacs = [float(v) for v in sys.argv[3].split(",")]
    cs = cstar()
    out = open(f"results_{tag}.txt", "x")
    def w(s):
        print(s); out.write(s + "\n"); out.flush()
    w(f"c* = {cs:.7f}")
    w("beta N hfac lam_e Delta_id Delta_direct LB UB Delta/LB UB/Delta -logD/sqrtb fApos rmin(eta=.25) -log(g_cut/gmax)/sqrtb")
    rows = []
    for b in betas:
        for hf in hfacs:
            r = run(b, hf)
            rows.append(r)
            w(f"{b:g} {r['N']} {hf:g} {r['lam_e']:.12f} {r['Delta']:.6e} {r['direct']:.6e} {r['LB']:.6e} {r['UB']:.6e} "
              f"{r['Delta']/r['LB']:.4f} {r['UB']/r['Delta']:.4f} {-math.log(r['Delta'])/math.sqrt(b):.5f} {r['fpos']} {r['rmin']:.5f} {-r['gcut_rel']/math.sqrt(b):.5f}")
    # predicates
    res = []
    def pred(name, ok, info):
        res.append(ok); w(f"{name}: {'MET' if ok else 'FAILED'}  {info}")
    by = {(r['beta'], r['hfac']): r for r in rows}
    h0 = hfacs[0]
    for b in (16.0, 32.0):
        if (b, h0) in by:
            r = by[(b, h0)]; rel = abs(r['Delta'] - r['direct']) / abs(r['direct'])
            pred(f"P1 beta={b:g}", rel < 1e-3, f"rel={rel:.2e}")
    n2 = sum(r['fpos'] for r in rows); w(f"P2 hypothesis f_A>0 qualifies in {n2}/{len(rows)} cases")
    pred("P2", n2 == len(rows), f"{n2}/{len(rows)}")
    pred("P3", all(r['LB'] <= r['Delta'] * (1 + 1e-9) for r in rows), "LB<=Delta all cases")
    pred("P4", all(r['Delta'] <= r['UB'] * (1 + 1e-9) for r in rows), "Delta<=UB all cases")
    big = [r for r in rows if r['beta'] >= 1024]
    if big:
        pred("P5", all(math.log(r['Delta'] / r['LB']) / math.sqrt(r['beta']) < 0.05 for r in big),
             ",".join(f"{math.log(r['Delta']/r['LB'])/math.sqrt(r['beta']):.4f}" for r in big))
    seq = [by[(b, h0)] for b in (256.0, 1024.0, 4096.0) if (b, h0) in by]
    if len(seq) == 3:
        dev = [abs(-math.log(r['Delta']) / math.sqrt(r['beta']) - cs) for r in seq]
        pred("P6", dev[-1] < 0.3 and dev[0] > dev[1] > dev[2], ",".join(f"{d:.4f}" for d in dev))
    if len(hfacs) > 1:
        for b in (256.0, 1024.0):
            if (b, hfacs[0]) in by and (b, hfacs[1]) in by:
                l1 = math.log(by[(b, hfacs[0])]['Delta']); l2 = math.log(by[(b, hfacs[1])]['Delta'])
                pred(f"P7 beta={b:g}", abs(l1 - l2) < 0.01 * abs(l1), f"dlog={l1-l2:.2e}")
    s8 = [r for r in rows if r['beta'] in (256.0, 1024.0, 4096.0)]
    if s8:
        pred("P8", all(r['rmin'] >= 1 for r in s8), ",".join(f"{r['beta']:g}:{r['rmin']:.4f}" for r in s8))
    w(f"SUMMARY met={sum(res)} failed={len(res)-sum(res)}")
    out.close()


if __name__ == "__main__":
    main()
