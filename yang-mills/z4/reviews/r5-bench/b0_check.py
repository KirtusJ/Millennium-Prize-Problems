"""B0 hypothesis test: direct position-space computation of <B_3(x) e^{-tH} B_3(y)> on an N=4 lattice
versus the mode formula of STATEMENT.md.

Setup: N = 4, ell = 1, b = 1/N, g = 1 (g drops out of D_t; checked analytically in notes.md).
Variables A_i(x), 3 N^3 = 192 links. theta_12(x) = A_1(x) + A_2(x+e1) - A_1(x+e2) - A_2(x) (and 13, 23).
K = sum_{x,i<j} theta_ij theta_ij^T (192x192). H = (g^2/2b) E.E + (1/(2 g^2 b)) A^T K A.
Physical modes = eigenvectors of K with eigenvalue > 1e-9 (kernel = gauge gradients (N^3-1) + 3 constant
zero modes; on the Gauss-law subspace with zero modes removed only range(K) is dynamical).
Each physical mode: mass m = b/g^2, stiffness lambda/(g^2 b) -> omega = sqrt(lambda)/b,
ground-state <q e^{-tH} q> = g^2/(2 b omega) e^{-t omega}.
Direct: D(x,y) = c_x^T G_t c_y / (g^2 b^4), c_x = coefficient vector of theta_12(x).
Formula: D_t(r) = ell^-3 sum_{k!=0} e^{i k.r b} ((k^1^2+k^2^2)/k^2)(k^/2) e^{-t k^}.

PREDICATES (fixed before first run):
 Q1: dim ker K = (N^3 - 1) + 3 = 66, so number of physical modes = 2 (N^3 - 1) = 126.
 Q2: the physical frequencies, sorted, equal the multiset {k^(k), twice each, k != 0} to 1e-9 relative.
 Q3: max_{x,y} |D_direct - D_formula| <= 1e-9 * max|D_formula| at t = 0 and at t = 0.3.
     Tolerance origin: double precision eigendecomposition of a 192x192 matrix with entries O(1), condition
     ~ lambda_max/lambda_min ~ 12/0.6; errors expected ~1e-13; 1e-9 is a generous margin, not a fit.
 Q4: D_direct depends only on x - y (translation invariance), same tolerance.
Exit code 0 iff all predicates hold, 1 otherwise.
"""
import itertools, os, sys
import numpy as np

N = 4; b = 1.0 / N; ell = 1.0; g = 1.0
L = 3 * N**3
def idx(i, x):
    return i * N**3 + ((x[0] % N) * N + (x[1] % N)) * N + (x[2] % N)
def e(i):
    v = [0, 0, 0]; v[i] = 1; return np.array(v)
def theta(i, j, x):
    c = np.zeros(L); x = np.array(x)
    c[idx(i, x)] += 1; c[idx(j, x + e(i))] += 1; c[idx(i, x + e(j))] -= 1; c[idx(j, x)] -= 1
    return c
sites = list(itertools.product(range(N), repeat=3))
K = np.zeros((L, L))
for x in sites:
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        c = theta(i, j, x); K += np.outer(c, c)
lam, V = np.linalg.eigh(K)
phys = lam > 1e-9
nker = int((~phys).sum())
omega = np.sqrt(lam[phys]) / b
Vp = V[:, phys]

m = np.fft.fftfreq(N) * N
kh1d = (2 / b) * np.sin(np.pi * m / N)
KH = np.array(np.meshgrid(kh1d, kh1d, kh1d, indexing='ij'))
khat = np.sqrt((KH**2).sum(0))
kh_list = np.sort(np.concatenate([khat.ravel()[1:], khat.ravel()[1:]]))
res = []
ok = True
q1 = (nker == N**3 - 1 + 3) and (phys.sum() == 2 * (N**3 - 1))
res.append(f"Q1 ker dim = {nker} (expect {N**3+2}), phys = {phys.sum()} : {'MET' if q1 else 'FAILED'}")
ok &= q1
dev = np.max(np.abs(np.sort(omega) - kh_list) / kh_list.max())
q2 = dev < 1e-9
res.append(f"Q2 frequency multiset max rel dev = {dev:.2e} : {'MET' if q2 else 'FAILED'}"); ok &= q2

C12 = np.array([theta(0, 1, x) for x in sites])  # rows: theta_12(x)
for t in [0.0, 0.3]:
    G = (Vp * (g**2 / (2 * b * omega) * np.exp(-t * omega))) @ Vp.T
    Ddir = C12 @ G @ C12.T / (g**2 * b**4)
    with np.errstate(invalid='ignore', divide='ignore'):
        d = np.where(khat > 0, (KH[0]**2 + KH[1]**2) / khat**2 * khat / 2 * np.exp(-t * khat), 0.0) / ell**3
    Dr = np.real(np.fft.ifftn(d)) * N**3  # D(r) on integer separations r
    Dform = np.array([[Dr[tuple((np.array(x) - np.array(y)) % N)] for y in sites] for x in sites])
    err = np.max(np.abs(Ddir - Dform)); scale = np.max(np.abs(Dform))
    q3 = err <= 1e-9 * scale
    res.append(f"Q3 t={t}: max|direct-formula| = {err:.3e}, max|D| = {scale:.6e}, D(0) direct={Ddir[0,0]:.10f} formula={Dform[0,0]:.10f} : {'MET' if q3 else 'FAILED'}")
    ok &= q3
    # translation invariance
    ti = 0.0
    for x in sites:
        for y in sites[:8]:
            s = tuple((np.array(x) + np.array([1, 2, 3])) % N); u = tuple((np.array(y) + np.array([1, 2, 3])) % N)
            ti = max(ti, abs(Ddir[sites.index(x), sites.index(y)] - Ddir[sites.index(s), sites.index(u)]))
    q4 = ti <= 1e-9 * scale
    res.append(f"Q4 t={t}: translation-invariance dev = {ti:.2e} : {'MET' if q4 else 'FAILED'}"); ok &= q4

out = "\n".join(res)
print(out)
fn = "results_b0_1.txt"
k = 1
while os.path.exists(fn):
    k += 1; fn = f"results_b0_{k}.txt"
open(fn, "w").write(out + "\n")
print("written", fn)
sys.exit(0 if ok else 1)
