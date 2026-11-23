"""Migdal-Kadanoff recursion, d dims, scale b=2, in character space (own code).

Plaquette weight f(U)=1+sum_j c_j d_j chi_j(U), normalised int f dU = 1.
One MK step (two orderings, both reported because conventions differ):
  A (stack then convolve): f -> f^lam pointwise (lam=b^(d-2), bond moving),
        then b^2 convolutions: c_j -> c_j^(b^2).
  B (convolve then power; the form quoted in Ito-Seiler 0803.3019 eq.2.2):
        c_j -> c_j^(b^2) first, then pointwise power lam.
Groups: U(1) Wilson f ~ exp(beta cos th); SU(2) Wilson f ~ exp((beta/2) chi_{1/2}).
Numerics: class-function grids (U(1): N=4096 uniform angle grid + FFT;
SU(2): psi in (0,pi), Haar (2/pi)sin^2 psi, Gauss-free midpoint grid, characters j<=J).

PREDICATES (fixed before first run):
 P0 (code sanity) step-0 c_1 of U(1) Wilson from the grid equals I1/I0 (own Bessel
    series) within 1e-9 (spectral accuracy of FFT on analytic periodic fn, double precision).
    Also d=2 control: after one step c_1' = c_1^(b^2) exactly within 1e-9 (no stacking, lam=1).
 P1 (grid) c_1 after 3 steps at N=2048 vs N=4096 for U(1) beta=2,10 differ by < 1e-6 relative.
 P2 (d=4, b=2) FOR ALL cases (group in {U1,SU2}, order in {A,B}, beta0 in
    {0.5,1,2,4,8}): c_1(n) < 1e-8 for some n <= NMAX=400 ("flows to strong coupling").
    Qualifying cases are counted per case and reported; no all-or-nothing claim is made.
 P3 (controls on the code, U(1), order A) d=3: all beta0 flow to strong (c_1<1e-8, n<=NMAX);
    d=5: beta0=8 does NOT flow (c_1 > 0.9 at n=NMAX or monotone increasing), i.e. a weak
    coupling phase shows up. If P3 fails the code is suspect, not the physics.
 P4 (log running, U(1) d=4 order A) for case beta0=8: report beta_eff(n)=I1/I0 inverse of c_1;
    no pass/fail, just report n at which c_1<0.01.
Tolerances: 1e-9 from double-precision spectral accuracy; 1e-8 strong-coupling threshold:
c_j drop super-exponentially (c->c^4) once small so 1e-8 is far past any crossover;
NMAX=400 chosen by the 6-minute budget.
Result files: opened mode 'x' (never overwritten). Seeds: none needed (deterministic); np.random.seed(0) set anyway.
"""
import sys, math, json
import numpy as np
np.random.seed(0)
B = 2

def bessel_I(n, x):
    s, k = 0.0, 0
    while True:
        t = (x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n))
        s += t; k += 1
        if k > 5 and t < 1e-18*s: return s

# ---------- U(1) ----------
def u1_coef(fv):           # fv on grid th_k=2 pi k/N, integral-normalised
    N = len(fv); c = np.fft.rfft(fv).real/N     # c_n = <f cos n th> ... f=1+2 sum c_n cos
    return c/c[0]                                # c_n (n>=0), c[0]=1
def u1_rebuild(c, N):
    full = np.zeros(N//2+1); full[:len(c)] = c[:N//2+1]
    spec = np.zeros(N//2+1, complex); spec[:] = full
    f = np.fft.irfft(spec*N, n=N)               # f_k = sum_n c_n e^{i n th}
    return f/np.mean(f)
def u1_wilson(beta, N):
    th = 2*np.pi*np.arange(N)/N
    lf = beta*(np.cos(th)-1); f = np.exp(lf); return f/np.mean(f)
def u1_step(fv, d, order):
    N = len(fv); lam = B**(d-2); nconv = B**2
    if order == 'A':
        g = fv**lam; g /= g.mean()
        c = u1_coef(g)**nconv
        return u1_rebuild(c, N)
    else:
        c = u1_coef(fv)**nconv
        g = u1_rebuild(c, N)
        g = np.maximum(g, 1e-300)**lam; return g/g.mean()
def run_u1(beta, d, order, N=4096, nmax=400, thr=1e-8):
    f = u1_wilson(beta, N); traj = []
    for n in range(nmax+1):
        c1 = u1_coef(f)[1]; traj.append(c1)
        if c1 < thr: return n, traj, True
        f = u1_step(f, d, order)
    return nmax, traj, False

# ---------- SU(2) ----------
class SU2:
    def __init__(self, Ng=3000, J2max=800):   # J2max = 2 j max
        self.psi = (np.arange(Ng)+0.5)*np.pi/Ng
        self.w = (2/np.pi)*np.sin(self.psi)**2*(np.pi/Ng)
        self.m = np.arange(1, J2max+2)        # m=2j+1 = 2..; skip m=1 (trivial)
        self.chi = np.sin(np.outer(self.m, self.psi))/np.sin(self.psi)   # chi_j, d_j=m
    def coef(self, f):
        f = f/np.sum(f*self.w); return (self.chi[1:] @ (f*self.w))/self.m[1:]   # c_j for m=2..
    def rebuild(self, c):
        f = 1 + (c*self.m[1:]) @ self.chi[1:]
        return f/np.sum(f*self.w)
    def wilson(self, beta):
        f = np.exp((beta/2)*(2*np.cos(self.psi)-2)); return f/np.sum(f*self.w)
    def step(self, f, d, order):
        lam = B**(d-2); nconv = B**2
        if order == 'A':
            g = f**lam; return self.rebuild(self.coef(g)**nconv)
        g = self.rebuild(self.coef(f)**nconv); g = np.maximum(g, 1e-300)**lam
        return g/np.sum(g*self.w)
def run_su2(beta, d, order, nmax=400, thr=1e-8, S=None):
    f = S.wilson(beta); traj = []
    for n in range(nmax+1):
        c = S.coef(f)[0]; traj.append(c)       # c_{1/2}
        if c < thr: return n, traj, True
        f = S.step(f, d, order)
    return nmax, traj, False

def main(out):
    R = {}; log = []
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s); log.append(s)
    # P0
    ok0 = True
    for beta in (0.5, 2.0, 10.0):
        c1 = u1_coef(u1_wilson(beta, 4096))[1]; ref = bessel_I(1, beta)/bessel_I(0, beta)
        P('P0 c1 grid', c1, 'Bessel', ref, 'diff', abs(c1-ref)); ok0 &= abs(c1-ref) < 1e-9
    f2 = u1_step(u1_wilson(2.0, 4096), 2, 'A'); c1 = u1_coef(u1_wilson(2.0, 4096))[1]
    d2 = abs(u1_coef(f2)[1]-c1**4); P('P0 d=2 control diff', d2); ok0 &= d2 < 1e-9
    P('P0', 'PASS' if ok0 else 'FAIL')
    # P1
    ok1 = True
    for beta in (2.0, 10.0):
        v = []
        for N in (2048, 4096):
            f = u1_wilson(beta, N)
            for _ in range(3): f = u1_step(f, 4, 'A')
            v.append(u1_coef(f)[1])
        rel = abs(v[0]-v[1])/v[1]; P('P1 beta', beta, v, 'rel', rel); ok1 &= rel < 1e-6
    P('P1', 'PASS' if ok1 else 'FAIL')
    # P2
    betas = (0.5, 1, 2, 4, 8); S = SU2(); q = 0; tot = 0; rows = []
    for grp in ('U1', 'SU2'):
        for order in ('A', 'B'):
            for b0 in betas:
                if grp == 'U1': n, tr, fl = run_u1(b0, 4, order)
                else: n, tr, fl = run_su2(b0, 4, order, S=S)
                tot += 1; q += fl
                P('P2', grp, order, 'beta0', b0, 'flows_strong', fl, 'n', n, 'c1[0,1,5,20,n]',
                  [float('%.4g' % tr[i]) for i in (0, min(1, n), min(5, n), min(20, n), n)])
                rows.append(dict(grp=grp, order=order, beta0=b0, strong=bool(fl), n=n, c_last=tr[-1]))
    P('P2 qualifying cases', q, 'of', tot, '->', 'PASS' if q == tot else 'FAIL (see per-case)')
    # P3
    ok3 = True
    for b0 in betas:
        n, tr, fl = run_u1(b0, 3, 'A'); P('P3 d=3 beta0', b0, 'strong', fl, 'n', n); ok3 &= fl
    n, tr, fl = run_u1(8, 5, 'A', nmax=400); weak = (not fl) and tr[-1] > 0.9
    P('P3 d=5 beta0=8 strong', fl, 'c1_last', tr[-1], 'weak-phase', weak); ok3 &= weak
    P('P3', 'PASS' if ok3 else 'FAIL')
    # P4
    n, tr, fl = run_u1(8, 4, 'A'); idx = next((i for i, v in enumerate(tr) if v < 0.01), None)
    P('P4 U1 d=4 A beta0=8: first n with c1<0.01 =', idx, '; c1 at n=0,10,20,40,80:',
      [float('%.4g' % tr[i]) for i in (0, 10, 20, 40, 80) if i < len(tr)])
    with open(out, 'x') as fh: json.dump(dict(rows=rows, log=log), fh, indent=1)

if __name__ == '__main__':
    main(sys.argv[1])
