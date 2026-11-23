"""vortex_su2.py -- TEST (iii) of PROOF.md step S5 (CLAIMED): the SU(2) vortex free energy
F(L,beta) = -ln(Z_tw/Z) on a periodic L^4 torus is non-increasing in L (and tends to 0).

Model: SU(2) Wilson action S = sum_P beta_P * (1/2) Re tr U_P, weight exp(+S).
Twist: plaquettes in the (0,1) plane with x0 = x1 = 0 (all x2, x3): L^2 plaquettes ("stack").
Interpolation: stack coupling beta*(1-2s), s in [0,1]; d ln Z(s)/ds = -2 beta <Pst>_s,
Pst = sum_stack (1/2) tr U_P. Hence F = 2 beta * int_0^1 <Pst>_s ds.
Quadrature: 6-point Gauss-Legendre on [0,1]. Errors: binning (10 bins) per s-point, combined
in quadrature with the GL weights. Update: vectorized Metropolis, checkerboard by site parity
per direction (links (x,mu),(y,mu) with x,y same parity share no plaquette). Seed fixed: 20261123+tag.

PREDICATES (fixed before the first run):
 Q0 control: at beta = 0.4, L = 4, s = 0 the bulk plaquette <(1/2)tr U_P> agrees with the
    strong-coupling value I2(beta)/I1(beta) = 0.09950 (one-plaquette; 4D corrections are O(beta^5)
    ~ 1e-3) within 5 standard errors + 0.003. Tolerance: statistical (binning) + truncation estimate.
 Q1 (claimed step, per case): for beta in {1.8, 2.4}: F(3) <= F(2) + 3 sigma and F(4) <= F(3) + 3 sigma
    (sigma = combined error of the difference). 4 cases. "For all" reported as met/failed per case.
 Q2 (character positivity, step S2 PROVED): F(L,beta) >= -3 sigma for all 6 (L,beta).
 Measured only: the value of F, and F(4)/F(2).
Output: results_su2_<tag>.txt opened with mode "x" (never overwritten).
"""
import sys, numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[0], a[1], a[2], a[3]
    b0, b1, b2, b3 = b[0], b[1], b[2], b[3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 - a2*b3 + a3*b2,
                     a0*b2 + a2*b0 - a3*b1 + a1*b3,
                     a0*b3 + a3*b0 - a1*b2 + a2*b1])

def qconj(a):
    return np.stack([a[0], -a[1], -a[2], -a[3]])

def sh(a, mu, n):  # field at x + n*mu  (a has leading quaternion axis)
    return np.roll(a, -n, axis=1 + mu)

class Lat:
    def __init__(self, L, beta, s, rng):
        self.L, self.rng = L, rng
        self.U = np.zeros((4, 4) + (L,)*4); self.U[:, 0] = 1.0  # U[mu][q, x0..x3]
        self.B = np.full((4, 4) + (L,)*4, beta)                  # B[mu,nu][x] coupling of plaquette (x;mu,nu)
        self.B[0, 1, 0, 0] = beta*(1 - 2*s); self.B[1, 0, 0, 0] = beta*(1 - 2*s)
        x = np.indices((L,)*4).sum(0) % 2
        self.par = [x == 0, x == 1]
        self.eps = 0.5

    def plaq(self, mu, nu):  # tr/2 of U_mu(x) U_nu(x+mu) U_mu(x+nu)^+ U_nu(x)^+
        U = self.U
        p = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qconj(sh(U[mu], nu, 1)), qconj(U[nu])))
        return p[0]

    def staple(self, mu):
        U, A = self.U, 0.0
        for nu in range(4):
            if nu == mu: continue
            up = qmul(qmul(sh(U[nu], mu, 1), qconj(sh(U[mu], nu, 1))), qconj(U[nu]))
            A = A + self.B[mu, nu] * up
            dn_link = sh(U[nu], nu, -1)  # U_nu(x-nu)
            dn = qmul(qmul(qconj(sh(sh(U[nu], mu, 1), nu, -1)), qconj(sh(U[mu], nu, -1))), dn_link)
            A = A + sh(self.B[mu, nu][None], nu, -1)[0] * dn
        return A  # local action of link = sum_q U*A  (= (1/2) tr(U A))

    def sweep(self):
        acc = 0; tot = 0
        for mu in range(4):
            for p in self.par:
                A = self.staple(mu)
                n = int(p.sum())
                r = self.rng.normal(size=(3, n)) * self.eps
                nr = np.sqrt(1 + (r**2).sum(0))
                R = np.vstack([1/nr, r/nr]) if self.rng.random() < 0.5 else np.vstack([1/nr, -r/nr])
                old = self.U[mu][:, p]
                new = qmul(R, old)
                Ap = A[:, p]
                dS = (new[0]*Ap[0] - (new[1:]*Ap[1:]).sum(0)) - (old[0]*Ap[0] - (old[1:]*Ap[1:]).sum(0))
                ok = self.rng.random(n) < np.exp(np.minimum(dS, 0))
                new = new / np.sqrt((new**2).sum(0))
                old[:, ok] = new[:, ok]
                self.U[mu][:, p] = old
                acc += ok.sum(); tot += n
        a = acc/tot
        self.eps *= 1.05 if a > 0.5 else 0.95

    def stack(self):
        return self.plaq(0, 1)[0, 0].sum()

def binerr(x, nb=10):
    x = np.asarray(x); m = len(x)//nb
    b = x[:m*nb].reshape(nb, m).mean(1)
    return x.mean(), b.std(ddof=1)/np.sqrt(nb)

def run_F(L, beta, ntherm, nmeas, seed, out):
    gx, gw = np.polynomial.legendre.leggauss(6); s_pts = (gx + 1)/2; w = gw/2
    F, var = 0.0, 0.0
    for k, s in enumerate(s_pts):
        lat = Lat(L, beta, s, np.random.default_rng(seed + 100*k))
        for _ in range(ntherm): lat.sweep()
        obs = []
        for _ in range(nmeas):
            lat.sweep(); obs.append(lat.stack())
        m, e = binerr(obs)
        F += 2*beta*w[k]*m; var += (2*beta*w[k]*e)**2
        out.write(f"  L={L} beta={beta} s={s:.4f} <Pst>={m:.5f} +- {e:.5f}\n"); out.flush()
    return F, np.sqrt(var)

if __name__ == "__main__":
    tag = sys.argv[1]; ntherm = int(sys.argv[2]); nmeas = int(sys.argv[3])
    betas = [float(b) for b in sys.argv[4].split(",")]
    out = open(f"results_su2_{tag}.txt", "x")
    out.write(f"args: {sys.argv[1:]}\n")
    # Q0 control
    lat = Lat(4, 0.4, 0.0, np.random.default_rng(20261123))
    for _ in range(ntherm): lat.sweep()
    pl = []
    for _ in range(nmeas):
        lat.sweep(); pl.append(np.mean([lat.plaq(m, n).mean() for m in range(4) for n in range(m+1, 4)]))
    m, e = binerr(pl); ref = 0.0995
    q0 = abs(m - ref) <= 5*e + 0.003
    out.write(f"Q0 control plaquette beta=0.4: {m:.5f} +- {e:.5f} ref {ref} -> {'MET' if q0 else 'FAILED'}\n"); out.flush()
    res = {}
    for beta in betas:
        for L in (2, 3, 4):
            res[(L, beta)] = run_F(L, beta, ntherm, nmeas, 20261123 + 1000*L + int(100*beta), out)
            out.write(f"F(L={L},beta={beta}) = {res[(L,beta)][0]:.4f} +- {res[(L,beta)][1]:.4f}\n"); out.flush()
    met = failed = 0
    for beta in betas:
        for (a, b) in ((2, 3), (3, 4)):
            (Fa, ea), (Fb, eb) = res[(a, beta)], res[(b, beta)]
            ok = Fb <= Fa + 3*np.hypot(ea, eb); met += ok; failed += (not ok)
            out.write(f"Q1 beta={beta} F({b})<=F({a})+3sig: {'MET' if ok else 'FAILED'}\n")
    q2 = [res[k][0] >= -3*res[k][1] for k in res]
    out.write(f"Q1 met {met} failed {failed}; Q2 met {sum(q2)} failed {len(q2)-sum(q2)}; Q0 {'MET' if q0 else 'FAILED'}\n")
    out.close()
    sys.exit(0 if (q0 and failed == 0 and all(q2)) else 1)
