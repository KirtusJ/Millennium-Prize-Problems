"""prog1_fibre.py -- referee test of Lemma F / Thm tu:U-F-master / Lemma tu:U-Frad / Lemma tu:U-R(4)
on the ACTUAL fibre operator F_a = e^{-V_a/2} K e^{-V_a/2} on L^2(SU(2)).

Two independent discretisations of ||F_a|| (top eigenvalue):
  (N) Nystrom on radial functions of r=x1^2+x2^2 in [0,1] using Lemma tu:U-Frad: after the angular
      integrals the radial kernel on L^2([0,1],dr) is
         F(r,r') = e^{-b s^2 r} (1/Z) I0(b sqrt(r r')) I0(b sqrt((1-r)(1-r'))) e^{-b s^2 r'},  Z=2 I1(b)/b
      (Haar: r uniform on [0,1] by (tu:U-eq-haar)). Gauss-Legendre in v, r=v^2.
  (L) Legendre matrix of Lemma tu:U-R(4): M_jk = sqrt(l_j) <P~_j, e^{-b s^2 (1-t)} P~_k>_{dt/2} sqrt(l_k),
      l_j = I_{2j+1}(b)/I_1(b).
Predicates (fixed before first run):
 P1 agreement: |eps_N - eps_L| <= 1e-6 * max(1,eps) for every case. Tolerance: both methods converge
    exponentially; each is run at two resolutions and the resolution change must be <= 1e-8 (P1c), so 1e-6
    leaves two orders of margin.
 P2 Cor tu:U-F-cor(a): eps_eff >= 0 (tolerance -1e-10, rounding).
 P3 Thm tu:U-F-master with tau=delta=b^(-1/3): eps_eff >= 2asinh(s) - log max(Min, A Mout). Hypothesis needs
    b>1, tau<1/5 (b>125), delta<=1: cases with b<=125 do not qualify and are counted separately.
 P4 Remark tu:U-R-rem (measured claim): b*(eps - eps_eff) = c(a) with c=0.98,0.95,0.86,0.76,0.68,0.65 at
    a=0.05,0.1,0.3,0.6,1.0,pi/2 for b=64,256,1024, "the same to within 2%". Predicate:
    |b(eps-eps_eff) - c(a)| <= 0.02*c(a) + 0.005 (2% claimed + half unit of the 2-digit value).
 P5 Remark tu:U-F-num (measured claim, b=4096, s>=0.1): -log sup_r B(r) - eps in [-4.1e-4, -2e-4], where B=F psi/psi,
    psi=e^{-b alpha r/2}; also sup B >= ||F|| must hold (Barta, Lemma tu:U-barta) -- P5a.
Result file opened with mode 'x'. Deterministic (no randomness).
"""
import numpy as np, math, sys

out = open(sys.argv[1], 'x')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.write(s + '\n'); out.flush()

def ive_asym(nu, x, K=12):
    x = np.asarray(x, float); s = np.ones_like(x); term = np.ones_like(x)
    for k in range(1, K + 1):
        term = term * (-(4 * nu * nu - (2 * k - 1) ** 2)) / (k * 8 * x)
        s = s + term
    return s / np.sqrt(2 * np.pi * x)
def ive0(x):
    x = np.asarray(x, float); out_ = np.empty_like(x)
    sm = x < 60
    out_[sm] = np.i0(x[sm]) * np.exp(-x[sm])
    out_[~sm] = ive_asym(0, x[~sm])
    return out_
def iven_ratio(b, nmax, M=1 << 15):
    # e^{-b} I_n(b) = (1/pi) int_0^pi e^{b(cos t-1)} cos(nt) dt, periodic trapezoid
    t = (np.arange(M) + 0.5) * np.pi / M
    e = np.exp(b * (np.cos(t) - 1))
    I = np.array([np.mean(e * np.cos(n * t)) for n in range(nmax + 1)])
    return I
# self-check of Bessel: I0 asymptotic vs np.i0 at x=60..300 and trapezoid
xs = np.array([60., 100., 300.])
P('bessel selfcheck ive0 asym vs np.i0:', np.max(np.abs(ive_asym(0, xs) - np.i0(xs) * np.exp(-xs)) / (np.i0(xs) * np.exp(-xs))))

def eps_nystrom(b, s, N):
    x, w = np.polynomial.legendre.leggauss(N)
    v = (x + 1) / 2; wv = w / 2
    r = v * v; wr = 2 * v * wv
    I1 = ive_asym(1, np.array([b]))[0] if b >= 60 else iven_ratio(b, 1)[1]
    pre = b / (2 * I1)            # (1/Z) * e^{-b}  (scaled)
    rr = np.sqrt(np.outer(r, r)); qq = np.sqrt(np.outer(1 - r, 1 - r))
    ker = pre * ive0(b * rr) * ive0(b * qq) * np.exp(b * (rr + qq - 1))
    ker *= np.exp(-b * s * s * (r[:, None] + r[None, :]))
    S = np.sqrt(wr)[:, None] * ker * np.sqrt(wr)[None, :]
    lam = np.linalg.eigvalsh(S)[-1]
    return -math.log(lam), (r, wr, pre)

def eps_legendre(b, s, J, NQ):
    I = iven_ratio(b, 2 * J + 2)
    l = np.clip(I[1:2 * J + 2:2] / I[1], 0, None)  # l_j = I_{2j+1}/I_1, j=0..J
    x, w = np.polynomial.legendre.leggauss(NQ)
    Pt = np.polynomial.legendre.legvander(x, J) * np.sqrt(2 * np.arange(J + 1) + 1)
    wt = w / 2 * np.exp(-b * s * s * (1 - x))
    G = Pt.T @ (wt[:, None] * Pt)
    M = np.sqrt(l)[:, None] * G * np.sqrt(l)[None, :]
    return -math.log(np.linalg.eigvalsh(M)[-1])

def A_(s): return 1 + 2 * s * s + 2 * s * math.sqrt(1 + s * s)
def Dfun(b): return 1 - 1 / (2 * b) - math.sqrt(2 * math.pi * b) * math.exp(-b) / 2
def deficit(s, b):
    tau = b ** (-1 / 3); d = tau; A = A_(s); D = Dfun(b)
    t1 = ((1 - tau) * (1 - 4 * tau) * (1 - 5 * d * d / 48)) ** -0.5
    t2 = math.sqrt(2 * math.pi * b) * math.exp(-b * (1 - 5 * tau) * (1 - math.cos(d)))
    t3 = math.sqrt(2 * math.pi * b) * math.exp(-b * A * tau / 2)
    lMin = math.log((t1 + t2 + t3) / D)
    lMout = math.log(b * math.sqrt(2 * math.pi * b) / (2 * D)) - (b * tau * tau / 64) * (1 - 1 / A ** 2) ** 2
    return max(lMin, math.log(A) + lMout)

avals = [0.05, 0.1, 0.3, 0.6, 1.0, math.pi / 2]
cclaim = [0.98, 0.95, 0.86, 0.76, 0.68, 0.65]
cnt = dict(P1=[0, 0], P1c=[0, 0], P2=[0, 0], P3=[0, 0, 0], P4=[0, 0])
for b in (64, 256, 1024):
    for a, cc in zip(avals, cclaim):
        s = math.sin(a); eps = 2 * math.asinh(s)
        N1 = 300 if b < 1000 else 500
        eN, _ = eps_nystrom(b, s, N1); eN2, _ = eps_nystrom(b, s, 2 * N1)
        J = int(4 * math.sqrt(b)) + 40
        eL = eps_legendre(b, s, J, 1500); eL2 = eps_legendre(b, s, J + 40, 2500)
        c1 = abs(eN - eN2) <= 1e-8 and abs(eL - eL2) <= 1e-8
        cnt['P1c'][0 if c1 else 1] += 1
        p1 = abs(eN2 - eL2) <= 1e-6 * max(1, eps); cnt['P1'][0 if p1 else 1] += 1
        p2 = eN2 >= -1e-10; cnt['P2'][0 if p2 else 1] += 1
        if b > 125:
            dfc = deficit(s, b); p3 = eN2 >= eps - dfc; cnt['P3'][0 if p3 else 1] += 1
        else:
            dfc = float('nan'); p3 = None; cnt['P3'][2] += 1
        cm = b * (eps - eN2); p4 = abs(cm - cc) <= 0.02 * cc + 0.005; cnt['P4'][0 if p4 else 1] += 1
        P(f'b={b} a={a:.4f} s={s:.4f} eps={eps:.8f} effN={eN2:.10f} effL={eL2:.10f} dN={eN-eN2:.1e} dL={eL-eL2:.1e} '
          f'P1c={c1} P1={p1} P2={p2} master_deficit={dfc:.3f} P3={p3} b(eps-eff)={cm:.4f} claim={cc} P4={p4}')
P('counts [met,failed(,not-qualifying)]:', cnt)

# P5: Barta ratio of psi at b=4096 for s>=0.1
b = 4096
res = []
for s in (0.1, 0.3, 0.6, 1.0):
    eN, (r, wr, pre) = eps_nystrom(b, s, 700)
    alpha = 2 * s * math.sqrt(1 + s * s)
    rr = np.sqrt(np.outer(r, r)); qq = np.sqrt(np.outer(1 - r, 1 - r))
    ker = pre * ive0(b * rr) * ive0(b * qq) * np.exp(b * (rr + qq - 1)) * np.exp(-b * s * s * (r[:, None] + r[None, :]))
    # B(r_i) = sum_j ker_ij wr_j psi_j / psi_i, evaluated in log-stable form
    B = (ker * wr[None, :] * np.exp(-b * alpha * (r[None, :] - r[:, None]) / 2)).sum(1)
    # restrict sup to r where quadrature resolves psi (r<=0.2): B on all nodes reported too
    supB = B.max(); eps = 2 * math.asinh(s)
    p5a = -math.log(supB) <= eN + 1e-9
    m = -math.log(supB) - eps
    p5 = -4.1e-4 - 1e-5 <= m <= -2e-4 + 1e-5
    P(f'P5 b=4096 s={s} eps_eff={eN:.8f} -log supB={-math.log(supB):.8f} (-log supB - eps)={m:.3e} P5a(supB>=||F||)={p5a} P5(in claimed range)={p5} argmax r={r[B.argmax()]:.4f}')
P('done')
