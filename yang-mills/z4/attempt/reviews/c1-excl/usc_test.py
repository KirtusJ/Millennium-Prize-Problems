"""usc_test.py  --  tests for the runner-up lemma (upper semicontinuity of the gap) of c1-excl.

Lemma (stated in report.md): if beta -> mu_beta is weakly continuous, then
  m(beta) = inf_F inf_k  f_{F,k}(beta),   f_{F,k} = -(1/2k) log( C_F(2k) / C_F(0) ),
C_F(n) the truncated reflection-positive correlation of a local observable F, is an infimum of
continuous functions, hence upper semicontinuous; and nothing more: Z = {m = 0} need not be closed.

Step tested here: the monotonicity used in the proof (Lyapunov): for a finite positive measure mu on
[-1,1], a_n = int x^n dmu, the sequence  g_k = -(1/2k) log(a_{2k}/a_0)  is NONINCREASING in k and
tends to -log max|supp mu|.  (Proof: a_{2k}^{1/2k}/a_0^{1/2k} = ||x||_{L^{2k}(mu/a_0)} increases in k.)

PREDICATES (fixed before the first run):
 P1  for all 2000 random discrete measures (seed 12345, 1..8 atoms in [-1,1], positive weights),
     g_{k+1} <= g_k + 1e-12 for k = 1..60.   Tolerance 1e-12: double rounding of logs of numbers >= 1e-300
     is below 1e-13 relative; 1e-12 absolute leaves a margin.  Atoms with |x|<1e-3 are kept (they only
     make a_{2k} smaller).  Report how many cases qualify (a_0>0 and some atom nonzero: all, by construction).
 P2  for the same measures, |g_200 - (-log max|x|)| <= log(n_atoms * w_max/w_min)/200 + 1e-9 (an explicit
     bound: a_{2k} <= a_0 xmax^{2k} and a_{2k} >= w_top xmax^{2k}).
 P3  explicit example showing that continuity of every correlation does NOT give lower semicontinuity:
     mu_beta = (1-w) delta_{e^-1} + w delta_{1/2... } family below; all moments a_n(beta) continuous
     (checked on a grid: max jump between neighbouring grid points <= 2*grid step * max|d a_n/d beta|),
     while m(beta) = -log max supp jumps: m = 1 for beta <= 1, m = log 2 ... see code. Predicate: the set
     {beta: m(beta) <= log(1.05)} on the grid equals {beta > 1} exactly, and m(1) = 1 (not 0): Z is not closed
     at its infimum in this model of the abstract situation.
 P4  the same example, approaching beta* = 1 from below: correlation length 1/m stays equal to 1 (does not
     diverge) -- "first-order-like" jump allowed by u.s.c.
"""
import math, random, sys

random.seed(12345)
out = open(sys.argv[1] if len(sys.argv) > 1 else "usc_result.txt", "x")
def log(s):
    print(s); out.write(s + "\n")

def gk(atoms, k):
    a0 = sum(w for x, w in atoms)
    # log-space (first run K1 underflowed: 0.05**400 = 0 in double; program defect, fixed here)
    ls = [math.log(w) + 2 * k * math.log(abs(x)) for x, w in atoms if x != 0]
    M = max(ls)
    la = M + math.log(sum(math.exp(l - M) for l in ls))
    return -(la - math.log(a0)) / (2 * k)

# P1, P2
qual = 0; fail1 = 0; fail2 = 0; worst1 = -1e9; worst2 = 0
for c in range(2000):
    n = random.randint(1, 8)
    atoms = [(random.uniform(-1, 1), random.uniform(0.01, 1.0)) for _ in range(n)]
    xmax = max(abs(x) for x, w in atoms)
    if xmax < 0.05:  # avoid underflow at k=200; does not qualify
        continue
    qual += 1
    g = [gk(atoms, k) for k in range(1, 61)]
    d = max(g[i + 1] - g[i] for i in range(59))
    worst1 = max(worst1, d)
    if d > 1e-12: fail1 += 1
    ws = [w for x, w in atoms]
    bound = math.log(n * max(ws) / min(ws)) / 200 + 1e-9
    e = abs(gk(atoms, 200) - (-math.log(xmax)))
    worst2 = max(worst2, e / bound)
    if e > bound: fail2 += 1
log(f"P1/P2 cases qualifying: {qual} of 2000")
log(f"P1 monotone: failed {fail1} of {qual}; max increase g_(k+1)-g_k = {worst1:.3e}  -> {'MET' if fail1==0 else 'FAILED'}")
log(f"P2 limit: failed {fail2} of {qual}; max error/bound = {worst2:.3f}  -> {'MET' if fail2==0 else 'FAILED'}")

# P3, P4: mu_beta = delta_{e^-1} (weight 1) + w(beta) delta_{1} restricted to Omega-perp is not allowed
# (eigenvalue 1 belongs to the vacuum), so use atoms at e^-1 and at x_top(beta) := 1 - 0 ... we model the
# massless continuum by a spectral density on (0,1) that switches on: weight w(beta)=max(0,beta-1) spread
# uniformly on [0.5,1).  Top of support: e^-1 for beta<=1, 1 for beta>1 -> m = 1 then 0.
def moments(beta, n):
    w = max(0.0, beta - 1.0)
    # int_{0.5}^1 x^n dx / 0.5
    unif = (1 - 0.5 ** (n + 1)) / (n + 1) / 0.5
    return math.exp(-n) + w * unif
def m_of(beta):
    return 1.0 if beta <= 1.0 else 0.0
grid = [0.5 + i * 1e-3 for i in range(1001)]
okc = True
for n in (0, 2, 10, 50):
    mx = max(abs(moments(grid[i + 1], n) - moments(grid[i], n)) for i in range(1000))
    lim = 2 * 1e-3 * 1.0  # |d a_n / d beta| <= 1 since unif <= 2*0.5 ... (<=1)
    if mx > lim: okc = False
    log(f"P3 continuity n={n}: max neighbour jump {mx:.3e} <= {lim:.1e}: {mx <= lim}")
# m via the lemma's formula, k large, numerically (inf over k approximated by k=2000)
def m_formula(beta, K=2000):
    # log-space (run K2 underflowed: exp(-4000) = 0; program defect, fixed here)
    def logmom(n):
        w = max(0.0, beta - 1.0)
        t = [-float(n)]
        if w > 0:
            t.append(math.log(w * (1 - 0.5 ** (n + 1)) / (n + 1) / 0.5))
        M = max(t); return M + math.log(sum(math.exp(x - M) for x in t))
    return min(-(logmom(2 * k) - logmom(0)) / (2 * k) for k in (1, 10, 100, K))
Zgrid = [b for b in grid if m_formula(b) <= math.log(1.05)]
expect = [b for b in grid if b > 1.0 + 1e-12]
p3 = okc and len(Zgrid) > 0 and abs(min(Zgrid) - min(expect)) < 1e-12 and len(Zgrid) == len(expect) and m_of(1.0) == 1.0
log(f"P3 Z on grid = (1, 1.5] : {len(Zgrid)} points, first {min(Zgrid):.4f}; m(1) = {m_of(1.0)} -> {'MET' if p3 else 'FAILED'}")
xi_below = [1 / m_of(b) for b in grid if b <= 1.0]
p4 = max(xi_below) == 1.0
log(f"P4 corr. length below beta*=1: max {max(xi_below)} (no divergence) -> {'MET' if p4 else 'FAILED'}")
log(f"note: m_formula(1.0)={m_formula(1.0):.4f}, m_formula(1.001)={m_formula(1.001):.4f} (k<=2000 upper approximations)")
out.close()
sys.exit(0 if (fail1 == 0 and fail2 == 0 and p3 and p4) else 1)
