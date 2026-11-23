"""ball_check.py -- independent recheck of the child's test (i) plus the new scalar/matrix facts
used in THEOREM_B_GENERAL.md. Metric <X,Y>_rho = -(1/N) Tr(drho X drho Y); s(U) = 1-(1/N)Re Tr rho(U).

PREDICATES (fixed before the first run):
 B1 (SU(3) ball constant): V(s)/s^4 from a deterministic Weyl-formula grid quadrature at s=1e-4
    equals c_formula = omega_8 (2s)^4/(s^4 Vol_rho(SU3)) = 9 sqrt(3)/(8 pi), Vol_rho(SU3)=sqrt3(2pi)^5/(2*3^4)
    (Macdonald volume for -Tr, rescaled), within rel 2e-2 (O(s) curvature correction + grid error).
 B1' (SU(2) same formula): V(s)/s^{3/2} at s=1e-6 from the exact Weyl density (2/pi)sin^2 equals
    omega_3 2^{3/2}/(2 pi^2) = 4 sqrt2/(3 pi) within rel 1e-3.
 B2 (U(1), rho_k = e^{it}+e^{ikt}, N=2, faithful): V(s)/sqrt(s) at s=1e-4 equals 2/(pi sqrt(1+k^2))
    within rel 1e-2 for k in {1,2,5,10,50} (grid spacing 2pi/4e7; O(s) correction).
 B3 (constants are not functions of (dim G, N) alone): for rho_50, V(1)/[lim V(s)/sqrt s] > 20.
 B4 (global upper bound s(exp X) <= |X|^2/2 for ALL X): 0 violations beyond 1e-12 over 20000 random
    X in su(3) (scales up to |X|=10) and 20000 in u(1)_k, k=1..50.
 B5 (lower bound s(exp X) >= (2/pi^2)|X|^2 when ||drho X||_op <= pi): 0 violations beyond 1e-12.
 B6 (Haar Jacobian bound): for X in su(3) with |X|_rho <= pi/(2 sqrt3): ||ad X||_op <= 2 sqrt(N)|X|_rho
    and prod over ad-eigenpairs (sin(l/2)/(l/2))^2 >= (2/pi)^8; 0 violations in 20000 samples.
 B7 (chordal Lipschitz): |chi(AVB)-chi(AB)| <= chi(V), chi=sqrt(s), for 20000 random SU(3) triples (tol 1e-12).
 Seeds: default_rng(7001..). Output ball_check_results.txt mode 'x'. Exit 0 iff all met.
"""
import numpy as np, sys, math

out = open('ball_check_results.txt', 'x')
def w(s): print(s); out.write(s + '\n'); out.flush()
ok_all = True
def rep(name, ok, msg):
    global ok_all; ok_all &= bool(ok); w(f"{name}: {'MET' if ok else 'FAILED'} {msg}")

# B1: Weyl formula for SU(3): Haar density on (t1,t2), t3=-t1-t2: |Delta|^2/(6 (2pi)^2)
s = 1e-4
a = math.acos(1 - 3 * s)
n = 4001
t = np.linspace(-a, a, n); h = t[1] - t[0]
T1, T2 = np.meshgrid(t, t); T3 = -T1 - T2
f = (3 - np.cos(T1) - np.cos(T2) - np.cos(T3)) / 3
e = np.exp(1j * np.array([T1, T2, T3]))
D = (np.abs(e[0] - e[1]) * np.abs(e[0] - e[2]) * np.abs(e[1] - e[2])) ** 2
V = (D * (f <= s)).sum() * h * h / (6 * (2 * np.pi) ** 2)
vol = math.sqrt(3) * (2 * math.pi) ** 5 / (2 * 3 ** 4)
om8 = math.pi ** 4 / 24
cf = om8 * 2 ** 4 / vol
rep('B1', abs(V / s ** 4 / cf - 1) <= 2e-2, f"V/s^4={V/s**4:.5f} c_formula={cf:.6f} 9sqrt3/(8pi)={9*math.sqrt(3)/(8*math.pi):.6f}")

s2 = 1e-6; al = math.acos(1 - s2)
V2 = (2 / math.pi) * (al / 2 - math.sin(2 * al) / 4)
c2 = (4 * math.pi / 3) * 2 ** 1.5 / (2 * math.pi ** 2)
rep("B1'", abs(V2 / s2 ** 1.5 / c2 - 1) <= 1e-3, f"V/s^1.5={V2/s2**1.5:.6f} formula={c2:.6f}")

# B2, B3
th = (np.arange(40_000_000) + 0.5) * (2 * np.pi / 40_000_000)
res = {}
for k in (1, 2, 5, 10, 50):
    sk = 1 - 0.5 * (np.cos(th) + np.cos(k * th))
    Vs = np.mean(sk <= 1e-4); V1 = np.mean(sk <= 1.0)
    lim = 2 / (math.pi * math.sqrt(1 + k * k))
    res[k] = (Vs / 1e-2, lim, V1)
    rep(f'B2[k={k}]', abs(Vs / 1e-2 / lim - 1) <= 1e-2, f"V(1e-4)/1e-2={Vs/1e-2:.6f} formula={lim:.6f} V(1)={V1:.4f}")
    del sk
r50 = res[50][2] / res[50][1]
rep('B3', r50 > 20, f"rho_50: V(1)/lim V(s)s^-1/2 = {r50:.2f}")

rng = np.random.default_rng(7001)
def rand_su3(M, scale):
    Z = rng.standard_normal((M, 3, 3)) + 1j * rng.standard_normal((M, 3, 3))
    H = (Z + np.conj(np.swapaxes(Z, -1, -2))) / 2
    H = H - np.trace(H, axis1=1, axis2=2)[:, None, None] * np.eye(3) / 3
    nrm = np.sqrt(np.real(np.einsum('mij,mji->m', H, H)) / 3)
    H = H / nrm[:, None, None] * scale[:, None, None]
    return 1j * H   # X anti-Hermitian, |X|_rho = scale
M = 20000
sc = rng.uniform(0, 10, M)
X = rand_su3(M, sc)
lam = np.linalg.eigvalsh(-1j * X)                      # eigenvalues theta_j
sx = np.mean(1 - np.cos(lam), axis=1)                  # s(exp X)
q = 0.5 * np.mean(lam ** 2, axis=1)                    # |X|^2/2
v4 = np.sum(sx > q + 1e-12)
opn = np.max(np.abs(lam), axis=1)
m5 = opn <= np.pi
v5 = np.sum(sx[m5] < (2 / np.pi ** 2) * 2 * q[m5] - 1e-12)
# u(1)_k
ks = rng.integers(1, 51, M); xs = rng.uniform(-10, 10, M)
sk = 1 - 0.5 * (np.cos(xs) + np.cos(ks * xs)); qk = 0.25 * (1 + ks ** 2) * xs ** 2
v4b = np.sum(sk > qk + 1e-12)
m5b = np.maximum(np.abs(xs), np.abs(ks * xs)) <= np.pi
v5b = np.sum(sk[m5b] < (2 / np.pi ** 2) * 2 * qk[m5b] - 1e-12)
rep('B4', v4 + v4b == 0, f"violations su3={v4} u1k={v4b}")
rep('B5', v5 + v5b == 0, f"violations su3={v5} (of {m5.sum()}) u1k={v5b} (of {m5b.sum()})")

# B6: ad eigenvalues: i(theta_j-theta_k)
sc6 = rng.uniform(0, np.pi / (2 * math.sqrt(3)), M)
X6 = rand_su3(M, sc6)
l6 = np.linalg.eigvalsh(-1j * X6)
difs = [l6[:, j] - l6[:, k] for j, k in ((0, 1), (0, 2), (1, 2))]
adop = np.max(np.abs(difs), axis=0)
prod = np.ones(M)
for dd in difs:
    x = dd / 2
    prod *= np.where(np.abs(x) < 1e-15, 1.0, (np.sin(x) / np.where(x == 0, 1, x)) ** 2)
v6a = np.sum(adop > 2 * math.sqrt(3) * sc6 + 1e-12); v6b = np.sum(prod < (2 / np.pi) ** 8 - 1e-12)
rep('B6', v6a + v6b == 0, f"adop violations={v6a}, jacobian violations={v6b}, min prod={prod.min():.4f} vs (2/pi)^8={(2/np.pi)**8:.4f}")

# B7
def haar_su3(M):
    Z = (rng.standard_normal((M, 3, 3)) + 1j * rng.standard_normal((M, 3, 3))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2); Q = Q * (d / np.abs(d))[:, None, :]
    det = np.linalg.det(Q); return Q / (det ** (1 / 3))[:, None, None]
A, Vv, B = haar_su3(M), haar_su3(M), haar_su3(M)
chi = lambda U: np.sqrt(np.maximum(0, 1 - np.real(np.trace(U, axis1=1, axis2=2)) / 3))
lhs = np.abs(chi(A @ Vv @ B) - chi(A @ B)); v7 = np.sum(lhs > chi(Vv) + 1e-12)
rep('B7', v7 == 0, f"violations={v7}")
w('ALL PREDICATES MET' if ok_all else 'SOME PREDICATE FAILED')
out.close(); sys.exit(0 if ok_all else 1)
