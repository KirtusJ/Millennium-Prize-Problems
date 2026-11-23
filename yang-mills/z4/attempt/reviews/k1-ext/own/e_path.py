"""Own check (k1-ext): transverse zero-point energy E(x) of the SU(2) Wilson plaquette map
at flat configurations on periodic boxes N1 x N2 x N3, computed in REAL SPACE from the
singular values of the plaquette derivative, compared with the Fourier formulas of
two-site-exterior/README.md (2^3) and full-neutral.md section 1 (general box).

Normalization (README): link coordinates z with generators i sigma_a/2 (quaternion angle z/2);
F = (P - 1) as 4 real quaternion components per plaquette; E(x) = sum_j arsinh sigma_j(D_x),
all 9n singular values (n = N1 N2 N3 sites, 3n links).  full-neutral uses quaternion angles,
sigma_fn = 2 sigma_README and E = 1/2 sum omega(sigma_fn^2), omega(x) = 2 arsinh(sqrt(x)/2);
these coincide term by term (checked as predicate P2b).
Flat representative: cycle holonomy exp(i phi_j sigma3), constant link exp(i phi_j sigma3/N_j);
adjoint angle per link theta_j = 2 phi_j/N_j; central iff every phi_j in pi Z.
Fourier formula: for each momentum p_j = 2 pi k_j/N_j and charge q in {-1,0,1}, two transverse
singular values sqrt(sum_j sin^2((p_j + q theta_j)/2)) and one zero.

PREDICATES (fixed before the first run):
 P1  real-space singular values = Fourier formula, max abs error <= 1e-11 at every sampled
     flat point on every box. Tolerance: float64 SVD of a <=324x432 matrix with O(1) entries,
     roundoff ~ 1e-14..1e-13; README reported 2.2e-15 on 2^3; 1e-11 is a 100x margin.
 P2  2^3 centre: E = 44.39835697395 (README E_*) within 1e-9 (printed digits of README).
 P2b full-neutral form 1/2 sum omega(4 sigma^2) equals sum arsinh sigma within 1e-12 at all points.
 P3  rank at central points = 6n-6, at regular points (some phi_j not in pi Z) = 6n-2,
     including enhanced-stabiliser points phi = (c,0,0) with c generic (SV threshold 1e-9).
 P4  for all sampled non-central flat points: E(x) - E_*,N > 0 (strict, margin > 1e-9).
     Per-case hypothesis test: count of sampled points that are non-central (dist to central
     set > 1e-6 in phi) reported first.
 P5  2^3 path phi=(c,0,0), c in [0, pi]: E strictly increasing in c on [0, pi/2] and strictly
     decreasing on [pi/2, pi] (README pairing: E decreasing in t=|cos(phi_1)|/2... here
     cycle angle phi, C=2phi), max at c = pi/2 (holonomy i sigma3).  Step tolerance 1e-12.
 P6  site-gauge invariance: random site gauge changes sorted singular values by <= 1e-11.
 P7  affine remainder uniformity: r = F(x exp z) - F(x) - D_x z; over 60 random base points x
     (30 flat, 30 random Haar) and |z| = rho in {0.2, 0.1, 0.05}: max |r|/rho^2 at the three
     rho agree within a factor 1.5 and are <= 10 (smooth F on compact X; the constant C in
     README's |F|^2 >= (1-eps)|b+Dz|^2 - C rho^4/eps is 2*(this)^2 at most).
 M1  measured only: E - E_* along phi = (c,c,c) and (c,0,0) for small c (slope near centre).
Seeds fixed: numpy default_rng(4116).
Output: results file opened with mode "x" (never overwritten).
"""
import sys, itertools
import numpy as np

I2 = np.eye(2, dtype=complex)
PA = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)

def box(N):
    sites = list(itertools.product(*[range(k) for k in N]))
    idx = {s: a for a, s in enumerate(sites)}
    nxt = np.zeros((len(sites), 3), int)
    for s, a in idx.items():
        for i in range(3):
            t = list(s); t[i] = (t[i] + 1) % N[i]; nxt[a, i] = idx[tuple(t)]
    return len(sites), nxt

def adj(m): return m.conj().swapaxes(-1, -2)

def F(links, nxt):
    out = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        p = links[:, i] @ links[nxt[:, i], j] @ adj(links[nxt[:, j], i]) @ adj(links[:, j])
        out.append(np.stack((p[:, 0, 0].real - 1, p[:, 0, 0].imag, p[:, 0, 1].real, p[:, 0, 1].imag), -1))
    return np.concatenate(out).ravel()

def expz(z):  # generator i sigma/2, z in R^3 -> SU(2)
    th = np.linalg.norm(z) / 2
    if th == 0: return I2.copy()
    n = z / np.linalg.norm(z)
    return np.cos(th) * I2 + 1j * np.sin(th) * np.einsum('c,cij->ij', n, PA)

def D(links, nxt):
    n = links.shape[0]; cols = []; h = 0.5
    for s in range(n):
        for ax in range(3):
            for a in range(3):
                vals = []
                for sg in (-1, 1):
                    m = links.copy()
                    m[s, ax] = links[s, ax] @ (np.cos(h) * I2 + 1j * sg * np.sin(h) * PA[a])  # left-translated
                    vals.append(F(m, nxt))
                cols.append((vals[1] - vals[0]) / (2 * np.sin(h)) / 2)  # per quaternion angle, then per z (=2 angle)
    return np.stack(cols, 1)

def flat_links(N, phi):
    n, _ = box(N)
    L = np.zeros((n, 3, 2, 2), complex)
    for j in range(3):
        a = phi[j] / N[j]
        L[:, j] = np.diag([np.exp(1j * a), np.exp(-1j * a)])
    return L

def fourier(N, phi):
    th = 2 * np.array(phi) / np.array(N)
    vals = []
    for k in itertools.product(*[range(m) for m in N]):
        p = 2 * np.pi * np.array(k) / np.array(N)
        for q in (-1, 0, 1):
            v = np.sqrt(np.sum(np.sin((p + q * th) / 2) ** 2))
            vals += [v, v, 0.0]
    return np.sort(np.array(vals))

def E_of(sv): return float(np.sum(np.arcsinh(sv)))
def omega(x): return 2 * np.arcsinh(np.sqrt(x) / 2)

def main(outpath):
    rng = np.random.default_rng(4116)
    res = open(outpath, 'x')
    def w(*a):
        s = ' '.join(str(x) for x in a); print(s); res.write(s + '\n'); res.flush()
    fails = []; met = []
    def pred(name, ok, info):
        (met if ok else fails).append(name); w(f'{name}: {"MET" if ok else "FAILED"} {info}')
    boxes = [(2, 2, 2), (3, 2, 2), (3, 3, 2)]
    maxerr = 0.0; p2b = 0.0; rank_ok = True; p4_cases = 0; p4_noncentral = 0; p4_min = np.inf; gauge_err = 0.0
    for N in boxes:
        n, nxt = box(N)
        pts = [np.zeros(3), np.array([np.pi, 0, 0]), np.array([np.pi, np.pi, np.pi]), np.array([0, np.pi, 2 * np.pi])]
        pts += [np.array([c, 0, 0]) for c in (0.3, 1.1, 2.0)]                 # enhanced stabiliser type
        pts += [np.array([c, c, 0]) for c in (0.7,)]
        pts += [rng.uniform(0, 2 * np.pi, 3) for _ in range(4)]
        pts += [t * np.array([1.3, 0.8, 2.1]) for t in (0.01, 0.1, 0.5, 1.0)]  # path centre -> regular
        cen = fourier(N, np.zeros(3)); Ec = E_of(cen)
        w(f'box {N}: n={n}, E_*,N (Fourier) = {Ec:.11f}')
        for phi in pts:
            Dm = D(flat_links(N, phi), nxt)
            sv = np.sort(np.linalg.svd(Dm, compute_uv=False))
            fo = fourier(N, phi)
            err = np.max(np.abs(sv - fo)); maxerr = max(maxerr, err)
            E = E_of(sv)
            p2b = max(p2b, abs(0.5 * np.sum(omega(4 * sv ** 2)) - E))
            central = np.all(np.abs(np.sin(phi)) < 1e-6)
            rank = int(np.sum(sv > 1e-9)); exp_rank = 6 * n - 6 if central else 6 * n - 2
            if rank != exp_rank: rank_ok = False
            p4_cases += 1
            if not central:
                p4_noncentral += 1; p4_min = min(p4_min, E - Ec)
            w(f'  phi={np.round(phi,4)} central={central} rank={rank} (exp {exp_rank}) E={E:.10f} E-E*={E-Ec:.3e} sv_err={err:.2e}')
        # gauge invariance at one regular point
        L = flat_links(N, np.array([1.3, 0.8, 2.1]))
        g = np.array([expz(rng.normal(size=3) * 2) for _ in range(n)])
        Lg = g[:, None] @ L @ adj(g[nxt])
        s1 = np.sort(np.linalg.svd(D(L, nxt), compute_uv=False)); s2 = np.sort(np.linalg.svd(D(Lg, nxt), compute_uv=False))
        gauge_err = max(gauge_err, np.max(np.abs(s1 - s2)))
        if N == (2, 2, 2):
            pred('P2', abs(Ec - 44.39835697395) < 1e-9, f'E_* = {Ec:.12f}')
    pred('P1', maxerr <= 1e-11, f'max sv error {maxerr:.2e}')
    pred('P2b', p2b <= 1e-12, f'max |1/2 sum omega - sum arsinh| = {p2b:.2e}')
    pred('P3', rank_ok, 'ranks 6n-6 central / 6n-2 non-central at all sampled points')
    w(f'P4 hypothesis: {p4_noncentral} of {p4_cases} sampled points are non-central')
    pred('P4', p4_min > 1e-9, f'min E-E_* over non-central = {p4_min:.4e}')
    pred('P6', gauge_err <= 1e-11, f'gauge change in sorted sv {gauge_err:.2e}')
    # P5 path on 2^3 using Fourier (validated by P1) plus real-space at a few points
    cs = np.linspace(0, np.pi, 401)
    Es = np.array([E_of(fourier((2, 2, 2), [c, 0, 0])) for c in cs])
    half = 200
    inc = np.all(np.diff(Es[:half + 1]) > 1e-12); dec = np.all(np.diff(Es[half:]) < -1e-12)
    pred('P5', inc and dec, f'increasing on [0,pi/2]: {inc}, decreasing on [pi/2,pi]: {dec}, E(pi/2)-E*={Es[half]-Es[0]:.6f}')
    # M1 slope near centre
    for dirn in ([1, 0, 0], [1, 1, 1]):
        d = np.array(dirn, float) / np.linalg.norm(dirn)
        for c in (1e-3, 1e-2, 1e-1):
            dE = E_of(fourier((2, 2, 2), c * d)) - E_of(fourier((2, 2, 2), np.zeros(3)))
            w(f'M1 dir {dirn} |phi|={c}: E-E*={dE:.6e}, (E-E*)/|phi|={dE/c:.6f}')
    # P7 affine remainder
    n, nxt = box((2, 2, 2)); ratios = {}
    bases = [flat_links((2, 2, 2), rng.uniform(0, 2 * np.pi, 3)) for _ in range(30)]
    for _ in range(30):
        bases.append(np.array([[expz(rng.normal(size=3) * 3) for _ in range(3)] for _ in range(n)]))
    for rho in (0.2, 0.1, 0.05):
        mx = 0.0
        for L in bases:
            Dm = D(L, nxt); F0 = F(L, nxt)
            for _ in range(3):
                z = rng.normal(size=(n, 3, 3)); z *= rho / np.linalg.norm(z)
                Lz = np.array([[L[s, a] @ expz(z[s, a]) for a in range(3)] for s in range(n)])
                r = F(Lz, nxt) - F0 - Dm @ z.ravel()
                mx = max(mx, np.linalg.norm(r) / rho ** 2)
        ratios[rho] = mx; w(f'P7 rho={rho}: max |r|/rho^2 = {mx:.4f}')
    v = list(ratios.values())
    pred('P7', max(v) / min(v) <= 1.5 and max(v) <= 10, f'ratios {v}')
    w(f'COUNTS met={len(met)} failed={len(fails)} measured_only=1 (M1); failed: {fails}')
    res.close()
    return 0 if not fails else 2

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
