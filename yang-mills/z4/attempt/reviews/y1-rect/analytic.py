"""analytic.py -- y1-rect (T194). Deterministic checks (no randomness; numpy only).

Predicates fixed before the first run (tolerances and their sources):
 A1  Bessel ratio R(k)=I2(k)/I1(k) by continued fraction agrees with the power series
     for k in [0.01, 10] to 1e-12 relative (float64 rounding; series terms all positive).
 A2  R'(k) formula used in target (R' = 1 - 3R/k - R^2) agrees with a central finite
     difference (step 1e-5) to 1e-7 absolute for k in [0.05, 60]
     (FD truncation ~ h^2 R''' ~ 1e-10, cancellation ~ 1e-16/1e-5 = 1e-11; 1e-7 is loose).
 A3  m(k) = min(R'(k), R(k)/k) > 0 on the grid, and R'(k) <= R(k)/k on the grid
     (radial variance <= tangential variance; expectation, may fail).
 A4  c1 := inf_k (1+k)^2 m(k) over grid k in [0, 2000] is >= 2^-22 (target's tilted
     Haar lemma constant). Measured value reported.
 A5  c2 := inf_k max(1, k/6)^2 m(k) (beta>=1, k=beta|H|<=6 beta) is >= 2^-22/49
     (target's J lower bound). Measured value reported; c2*(1+R) is the improved J floor.
 A6  Combinatorics on the 4^4 torus (also 6^4): with selected x-links {y+z even} on one
     time slice, every xy face of that slice contains exactly one selected link.
 A7  Site reflection theta: y -> 2*y0 - y (mod L), L even, y0 = 0. For a selected
     x-link at (x,y0,z,t): the reflected oriented path of staple a_+ (x -> x+e_y ->
     x+e_y+e_x -> x+e_x) is exactly the staple a_- with the same endpoints and same
     traversal direction; the rectangle a_+ . a_-^{-1} does not contain the common link;
     every plaquette of the lattice has all its links in the closed + half
     {0<=y<=L/2} or all in the closed - half {L/2<=y<=L} (mod L) i.e. no plaquette
     contains links from both open halves; links lying in the fixed planes are
     mapped to themselves with the same orientation.
 A8  Weak coupling: G(0)-G(e1) = 1/8 within 1e-6 on L=48 (exact sum rule up to
     finite-volume zero-mode term 1/(4 L^4)); report r = 8[G0-G(1,1)]+4[G0-G(2,0)]
     so that 1-W12 ~ r*3/(4 beta), 1-W11 ~ 3/(4 beta). r(L=48) vs r(L=64) differ < 1e-4.
"""
import numpy as np, sys, math, itertools

def R_cf(k, depth=None):
    # I_{n}/I_{n-1} = 1/(2n/k + I_{n+1}/I_n); backward from deep n
    if k == 0: return 0.0
    if depth is None: depth = int(60 + 2*k)
    t = 0.0
    for n in range(depth, 1, -1):
        t = 1.0/(2*n/k + t)
    return t  # I2/I1

def I_series(n, x, terms=400):
    s = 0.0; term = (x/2)**n / math.factorial(n)
    for m in range(terms):
        s += term
        term *= (x/2)**2/((m+1)*(m+1+n))
        if term < 1e-30*s: break
    return s

def Rp(k):
    R = R_cf(k); return 1 - 3*R/k - R*R

def m_of(k):
    if k < 1e-6: return 0.25
    R = R_cf(k); return min(1 - 3*R/k - R*R, R/k)

out = open(sys.argv[1], "x")
def log(s):
    print(s); out.write(s + "\n"); out.flush()
fails = []
# A1
ks = np.linspace(0.01, 10, 200)
err = max(abs(R_cf(k) - I_series(2,k)/I_series(1,k))/(I_series(2,k)/I_series(1,k)) for k in ks)
log(f"A1 max rel err CF vs series = {err:.3e}");
if not err < 1e-12: fails.append("A1")
# A2
ks = np.linspace(0.05, 60, 400); h = 1e-5
err = max(abs(Rp(k) - (R_cf(k+h)-R_cf(k-h))/(2*h)) for k in ks)
log(f"A2 max abs err R' formula vs FD = {err:.3e}")
if not err < 1e-7: fails.append("A2")
# A3, A4, A5
grid = np.concatenate([np.linspace(0, 10, 10001), np.linspace(10, 2000, 20000)])
mv = np.array([m_of(k) for k in grid])
rad_le_tan = all((Rp(k) <= R_cf(k)/k + 1e-15) for k in grid if k > 1e-6)
log(f"A3 min m = {mv.min():.6e} (>0: {mv.min()>0}); R'<=R/k on grid: {rad_le_tan}")
if not mv.min() > 0: fails.append("A3a")
if not rad_le_tan: fails.append("A3b")
c1v = (1+grid)**2*mv; i1 = c1v.argmin()
log(f"A4 c1 = inf (1+k)^2 m(k) = {c1v[i1]:.6f} at k={grid[i1]:.4f}; 2^-22 = {2**-22:.3e}; (1+k)^2 m at k=2000: {c1v[-1]:.5f} (asymptote 3/2)")
if not c1v[i1] >= 2**-22: fails.append("A4")
c2v = np.maximum(1, grid/6)**2*mv; i2 = c2v.argmin()
log(f"A5 c2 = inf max(1,k/6)^2 m(k) = {c2v[i2]:.6f} at k={grid[i2]:.4f}; tail k=2000: {c2v[-1]:.6f} (asymptote 1/24={1/24:.6f}); target constant 2^-22/49 = {2**-22/49:.3e}; ratio {c2v[i2]/(2**-22/49):.3e}")
if not c2v[i2] >= 2**-22/49: fails.append("A5")
for b in [0.5, 1, 2, 2.3, 3.4]:
    log(f"   u(beta={b}) = I2/I1 = {R_cf(b):.8f}, u^2 = {R_cf(b)**2:.8f}")
# A6, A7
def combin(L):
    ok6 = True
    for x, y, z in itertools.product(range(L), repeat=3):
        # xy face at (x,y,z): x-links at (x,y,z) and (x,y+1,z)
        sel = [((y + z) % 2 == 0), (((y+1) % L + z) % 2 == 0)]
        if sum(sel) != 1: ok6 = False
    # A7: links as (site tuple (x,y,z,t), dir); y index 1
    E = np.eye(4, dtype=int)
    def th_site(s): s = list(s); s[1] = (-s[1]) % L; return tuple(s)
    def sh(s, d, sgn=1): return tuple((np.array(s) + sgn*E[d]) % L)
    def path_steps(start, dirs):  # list of oriented steps (from, to)
        steps = []; s = start
        for d, sg in dirs:
            t = sh(s, d, sg); steps.append((s, t)); s = t
        return steps
    ok7 = True
    for x, z, t in itertools.product(range(L), repeat=3):
        s0 = (x, 0, z, t)
        ap = path_steps(s0, [(1, +1), (0, +1), (1, -1)])
        am = path_steps(s0, [(1, -1), (0, +1), (1, +1)])
        refl = [(th_site(a), th_site(b)) for a, b in ap]
        if refl != am: ok7 = False
        common = (s0, sh(s0, 0))
        rect = ap + [(b, a) for a, b in reversed(am)]
        und = {frozenset(e) for e in rect}
        if frozenset(common) in und: ok7 = False
        if len(rect) != 6 or rect[0][0] != rect[-1][1]: ok7 = False
    def half(link):  # +1 if both endpoints y in [0,L/2], -1 if in [L/2,L] (0 or L/2 count both)
        ys = [s[1] for s in link]
        plus = all(0 <= y <= L//2 for y in ys) and not (set(ys) == {0, L-1})
        minus = all((y >= L//2 or y == 0) for y in ys)
        return plus, minus
    for s in itertools.product(range(L), repeat=4):
        for mu in range(4):
            for nu in range(mu+1, 4):
                a = s; b = sh(a, mu); c = sh(b, nu); d = sh(a, nu)
                links = [(a, b), (b, c), (d, c), (a, d)]
                hs = [half(l) for l in links]
                if not (all(h[0] for h in hs) or all(h[1] for h in hs)): ok7 = False
    # tangential links in plane y=0 fixed with orientation
    for s in itertools.product(range(L), repeat=4):
        if s[1] != 0: continue
        for mu in (0, 2, 3):
            if (th_site(s), th_site(sh(s, mu))) != (s, sh(s, mu)): ok7 = False
    return ok6, ok7
for L in (4, 6):
    ok6, ok7 = combin(L)
    log(f"A6 L={L} every xy face has exactly one selected x-link: {ok6}")
    log(f"A7 L={L} reflection maps a+ to a-, rectangle excludes common link, no plaquette straddles, plane links fixed: {ok7}")
    if not ok6: fails.append(f"A6 L={L}")
    if not ok7: fails.append(f"A7 L={L}")
# A8
def Gdiff(L):
    p = 2*np.pi*np.arange(L)/L
    s2 = 4*np.sin(p/2)**2
    P0, P1, P2, P3 = np.meshgrid(p, p, p, p, indexing="ij", sparse=True)
    den = s2[:, None, None, None] + s2[None, :, None, None] + s2[None, None, :, None] + s2[None, None, None, :]
    den[0, 0, 0, 0] = np.inf
    g1 = np.sum((1 - np.cos(P0))/den)/L**4
    g11 = np.sum((1 - np.cos(P0 + P1))/den)/L**4
    g2 = np.sum((1 - np.cos(2*P0))/den)/L**4
    return g1, g11, g2
rs = {}
for L in (48, 64):
    g1, g11, g2 = Gdiff(L)
    r = 8*g11 + 4*g2
    rs[L] = r
    log(f"A8 L={L}: G0-G(e)={g1:.8f} (1/8 - {0.125-g1:.2e}), G0-G(1,1)={g11:.8f}, G0-G(2,0)={g2:.8f}, r={r:.6f}")
    if not abs(g1 - 0.125) < 1e-6: fails.append(f"A8 sumrule L={L}")
if not abs(rs[48] - rs[64]) < 1e-4: fails.append("A8 conv")
r = rs[64]
for b in [2, 2.3, 3.4]:
    log(f"   weak coupling LO beta={b}: W11 ~ {1-0.75/b:.4f}, W12 ~ {1-r*0.75/b:.4f}")
log(f"FAILED PREDICATES: {fails if fails else 'none'}")
sys.exit(1 if fails else 0)
