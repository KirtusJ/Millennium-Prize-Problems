"""l1-obs independent check of (b),(c),(d),(a-pointwise) for observable-weights.

Conventions (my own derivation): one colour real field z on links of periodic box,
Z_ij(x)=z_j(x+e_i)-z_j(x)-z_i(x+e_j)+z_i(x); C = plaquette-link incidence matrix;
Gaussian Euclidean action per time step sum|z(t+1)-z(t)|^2/2 + sum_plaq |Z|^2/2
(Wilson beta(1-ReP) with links exp(s z), 1-ReP ~ |ImP|^2/2, s^2 beta = 1).
Frequencies w=arccosh(1+m/2), m eigenvalue of C^T C.

PREDICATES (fixed before first run):
P1[box] first visible energy (2*min w over modes with a>1e-12, a = (C v)_P^2/(2 sinh w), P = (1,2) plaquette at origin)
        equals closed form 2 arccosh(1+2 sin^2(pi/max(N1,N2))) within 1e-9   [tol: eigh error ~1e-13 on <=270 dims; 1e-9 grouping tol]
P2[box] first visible energy equals auditor value within 5e-9 [auditor gives 8 decimals: half unit]
P3[box] threshold weight (3/2)(sum a over modes with w=w_min)^2 equals auditor within 5e-9 [same]
P4[box] one-colour variance sum a equals checks.md value within 5e-9 [8 decimals]
P5[t]  (2,2,2), t=0,1,2: direct time-lattice Gaussian covariance of Z(0),Z(t) (periodic time T=60, pseudo-inverse of
        precision on all links) equals Fourier k(t) within rel 1e-8 [tol: finite-T error exp(-T w_min)~1e-46, pinv conditioning ~1e-12]
P6[t]  Monte Carlo (seed 20261123, 400000 draws, 3 colours) Cov(|Z0|^2/2,|Zt|^2/2) within 5 standard errors of 3k(t)^2/2
        [tol: CLT, 5 sigma]; and the alternative 3k^2 (doubled) is NOT within 5 s.e. (measured; discriminates factor)
P7[N]  N=4,8: matrix threshold energy and mass equal closed form (E=2w, mass=(3/2)(2m/(N^3 sinh w))^2) within rel 1e-9
P8     N*E-4pi and N^8*mass-24pi^2 for N=4,8,16,32 (closed form): successive ratio of differences for (16,32) in [3.8,4.2]
        i.e. O(N^-2) [tol: Taylor next-order term changes ratio by O(N^-2) ~ 1%]
P9     pointwise: constant-field plaquette beta(1-ReP)/(2h|X1xX2|^2) -> 1, |ratio-1| decreasing roughly linearly in h
        (ratio of errors between successive h=1e-1..1e-3 (factor 10) in [5,20])  [tol: expected O(h^2)/O(h) correction]
"""
import numpy as np, itertools, math, sys
from math import pi

def incidence(shape):
    n = int(np.prod(shape)); sites = np.arange(n).reshape(shape)
    def L(site_idx, d): return 3*site_idx + d
    rows = []
    for (i, j) in [(0,1),(0,2),(1,2)]:
        for x in itertools.product(*[range(N) for N in shape]):
            r = np.zeros(3*n)
            xi = list(x); xi[i] = (x[i]+1) % shape[i]
            xj = list(x); xj[j] = (x[j]+1) % shape[j]
            s0 = sites[x]; si = sites[tuple(xi)]; sj = sites[tuple(xj)]
            r[L(si,j)] += 1; r[L(s0,j)] -= 1; r[L(sj,i)] -= 1; r[L(s0,i)] += 1
            rows.append(r)
    return np.array(rows)   # first n rows: (0,1)-plaquettes; row 0 = origin

def modes(shape):
    C = incidence(shape); M = C.T @ C
    ev, V = np.linalg.eigh(M)
    keep = ev > 1e-9
    m = ev[keep]; w = np.arccosh(1 + m/2)
    a = (C[0] @ V[:, keep])**2 / (2*np.sinh(w))
    return w, a, ev

def threshold(w, a, tol=1e-9):
    act = a > 1e-12
    wmin = w[act].min()
    shell = np.abs(w - wmin) < tol
    return 2*wmin, 1.5*a[shell].sum()**2

def kfour(shape, t):
    p = np.array(np.meshgrid(*[2*pi*np.arange(N)/N for N in shape], indexing='ij'))
    q = (2*np.sin(p/2))**2; m = q.sum(0); mask = m > 1e-12
    w = np.arccosh(1 + m[mask]/2)
    return np.sum((q[0]+q[1])[mask]*np.exp(-t*w)/(2*np.sinh(w)))/np.prod(shape)

res = {"met":0, "failed":0, "measured":0}
def pred(name, ok, msg):
    res["met" if ok else "failed"] += 1
    print(f"{name}: {'MET' if ok else 'FAILED'} {msg}")
def meas(name, msg):
    res["measured"] += 1; print(f"{name}: MEASURED {msg}")

aud = {(2,2,2):(3.52549435,0.046875),(3,3,3):(3.13359847,0.01410935),(3,2,5):(3.13359847,0.00285714)}
var_cm = {(2,2,2):0.45306962,(3,3,3):0.49085147,(3,2,5):0.46651745}
print("hypothesis per case: boxes tested 3 (+ (4,3,2) measured); all have N>=2 in every direction")
for shape in [(2,2,2),(3,3,3),(3,2,5),(4,3,2)]:
    w, a, ev = modes(shape)
    E, mass = threshold(w, a)
    closed = 2*np.arccosh(1+2*np.sin(pi/max(shape[0],shape[1]))**2)
    print(shape, f"E1={E:.10f} weight={mass:.10f} var={a.sum():.10f} closed={closed:.10f} "
          f"min w all={w.min():.6f} min active w={E/2:.6f} zero modes={np.sum(ev<=1e-9)} k(0)Fourier={kfour(shape,0):.10f}")
    pred(f"P1{shape}", abs(E-closed) < 1e-9, f"diff={E-closed:.2e}")
    if shape in aud:
        pred(f"P2{shape}", abs(E-aud[shape][0]) < 5e-9, f"diff={E-aud[shape][0]:.2e}")
        pred(f"P3{shape}", abs(mass-aud[shape][1]) < 5e-9, f"diff={mass-aud[shape][1]:.2e}")
        pred(f"P4{shape}", abs(a.sum()-var_cm[shape]) < 5e-9, f"diff={a.sum()-var_cm[shape]:.2e}")

# (c) direct time-lattice Gaussian on 2^3
shape = (2,2,2); C = incidence(shape); M = C.T @ C; nl = M.shape[0]; T = 60
Dt = np.roll(np.eye(T), 1, axis=1) - np.eye(T)
Q = np.kron(Dt.T @ Dt, np.eye(nl)) + np.kron(np.eye(T), M)
Cov = np.linalg.pinv(Q, rcond=1e-10, hermitian=True)
c0 = C[0]
rng = np.random.default_rng(20261123)
for t in (0,1,2):
    blk = Cov[0:nl, t*nl:(t+1)*nl]
    cz = c0 @ blk @ c0
    kt = kfour(shape, t)
    pred(f"P5[t={t}]", abs(cz/kt-1) < 1e-8, f"direct={cz:.12f} fourier={kt:.12f}")
    v = kfour(shape, 0)
    S = 400000
    g = rng.standard_normal((S, 3, 2))
    L = np.linalg.cholesky(np.array([[v, kt],[kt, v]]) + 1e-15*np.eye(2))
    Zs = g @ L.T
    y0 = 0.5*(Zs[:,:,0]**2).sum(1); yt = 0.5*(Zs[:,:,1]**2).sum(1)
    prod = (y0-y0.mean())*(yt-yt.mean()); cov = prod.mean(); se = prod.std()/math.sqrt(S)
    pred(f"P6[t={t}]", abs(cov-1.5*kt**2) < 5*se, f"MC={cov:.6f}+-{se:.6f} 3k^2/2={1.5*kt**2:.6f} 3k^2={3*kt**2:.6f} doubled within 5se: {abs(cov-3*kt**2)<5*se}")
    print(f"   C_Y limit t={t}: {1.5*kt**2:.10f}")

# (d)
def closed_atom(N):
    m = 4*np.sin(pi/N)**2; w = np.arccosh(1+m/2)
    return 2*w, 1.5*(2*m/(N**3*np.sinh(w)))**2
for N in (4, 8):
    w, a, _ = modes((N,N,N)); E, mass = threshold(w, a); Ec, mc = closed_atom(N)
    pred(f"P7[N={N}]", abs(E/Ec-1) < 1e-9 and abs(mass/mc-1) < 1e-9, f"matrix E={E:.12f} mass={mass:.6e}; closed E={Ec:.12f} mass={mc:.6e}")
dE, dm = [], []
for N in (4, 8, 16, 32):
    E, mass = closed_atom(N)
    dE.append(N*E-4*pi); dm.append(N**8*mass-24*pi**2)
    print(f"N={N}: N*E={N*E:.10f} (4pi={4*pi:.10f}, diff {dE[-1]:.4e}); N^8 mu={N**8*mass:.8f} (24pi^2={24*pi**2:.8f}, diff {dm[-1]:.4e})")
rE = dE[2]/dE[3]; rm = dm[2]/dm[3]
pred("P8", 3.8 <= rE <= 4.2 and 3.8 <= rm <= 4.2, f"ratio dE(16)/dE(32)={rE:.4f}, dmu ratio={rm:.4f}; ratios(8/16)={dE[1]/dE[2]:.4f},{dm[1]/dm[2]:.4f}")

# (a) pointwise constant-field plaquette
def qmul(p, q):
    a1, b1 = p[0], p[1:]; a2, b2 = q[0], q[1:]
    return np.concatenate([[a1*a2 - b1@b2], a1*b2 + a2*b1 + np.cross(b1, b2)])
def qexp(v):
    r = np.linalg.norm(v); return np.concatenate([[math.cos(r)], (math.sin(r)/r if r>0 else 1.0)*v])
def qinv(q): return q*np.array([1,-1,-1,-1])
X1 = np.array([.7,-.2,.4]); X2 = np.array([-.3,.9,.5])
errs = []
for h in (1e-1, 1e-2, 1e-3):
    beta = h**-3
    U1, U2 = qexp(h*X1), qexp(h*X2)
    P = qmul(qmul(U1, U2), qmul(qinv(U1), qinv(U2)))
    Y = beta*(1-P[0]); ref = 2*h*np.cross(X1, X2)@np.cross(X1, X2)
    errs.append(abs(Y/ref-1)); print(f"h={h}: beta(1-ReP)={Y:.6e} 2h|X1xX2|^2={ref:.6e} ratio-1={Y/ref-1:.3e}")
r1, r2 = errs[0]/errs[1], errs[1]/errs[2]
pred("P9", 5 <= r1 <= 20 and 5 <= r2 <= 20, f"error ratios {r1:.2f} {r2:.2f} (10 => O(h), 100 => O(h^2))")
print(f"COUNTS met={res['met']} failed={res['failed']} measured={res['measured']}")
sys.exit(0 if res['failed']==0 else 1)
