"""Task (b): structural check of the transfer-operator eigenvalue on an actual N=2 lattice, beta=2.
Lattice: sites i=1,2 on a spatial circle, spatial links U_i (time t), V_i (time t+1), temporal links
T_i. Plaquette i: P_i = U_i T_{i+1} V_i^{-1} T_i^{-1} (T_3 = T_1). Weight w(P) = exp((beta/2) tr P).
Transfer action on a class function f of the t+1 holonomy:
   (K f)(U;T) = int dV_1 dV_2  w(P_1) w(P_2) f(V_1 V_2)
The V-integrals are done DIRECTLY over the link variables (no change of variables, no character
formula), with T random (generic gauge) AND T = 1, using SU(2) = unit quaternions in Hopf coords
   V = (cos e cos x1, cos e sin x1, sin e cos x2, sin e sin x2),  dV = sin e cos e de dx1 dx2 /(2 pi^2)
Gauss-Legendre (n_e points) in e on [0,pi/2], trapezoid (n_x points, periodic => spectral) in x1, x2.
The double V-integral factorizes exactly because tr(V1 V2) = 2 sum_mu s_mu V1_mu V2_mu
(s=(1,-1,-1,-1)) is bilinear; chi_1(X) = tr(X)^2 - 1 is handled with second moments.
Reference: (w_j/w_0)^2 with w_j = (1/d_j) int w chi_j dU via mpmath class-angle quadrature (dps 30).
Fixed seed random.seed(12345) for U and T.
PREDICATES (exit 1 if any fails):
 B1 Kchi_0 independent of U,T (gauge/config invariance): rel spread < 1e-11.
 B2 eigenfunction: R_1/2(U,T) = [K chi_1/2 (U)/chi_1/2(U1U2)] / K chi_0 equal across 3 configs (rel < 1e-10)
 B3 |R_1/2 - (w_1/2/w_0)^2| / (w_1/2/w_0)^2 < 1e-11 for every config.
 B4 same for j=1: |R_1 - (w_1/w_0)^2| rel < 1e-11.
 B5 quadrature convergence: results at (n_e,n_x)=(24,32) vs (32,40) agree to < 1e-12 rel.
Output: transfer_results.txt (new suffixed name if exists).
"""
import os, sys, math, random
from mpmath import mp, quad, sin as msin, cos as mcos, exp as mexp, pi as mpi

BETA = 2.0
S = (1.0, -1.0, -1.0, -1.0)

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qinv(a): return (a[0], -a[1], -a[2], -a[3])
def rand_su2(rng):
    v = [rng.gauss(0, 1) for _ in range(4)]; n = math.sqrt(sum(x*x for x in v))
    return tuple(x/n for x in v)

def gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n+1):
        x = math.cos(math.pi*(i-0.25)/(n+0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n+1):
                p0, p1 = p1, ((2*k-1)*x*p1 - (k-1)*p0)/k
            dp = n*(x*p1 - p0)/(x*x - 1)
            dx = p1/dp; x -= dx
            if abs(dx) < 1e-16: break
        xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs, ws

def haar_rule(ne, nx):
    xs, ws = gauss_legendre(ne)
    pts = []
    for x, w in zip(xs, ws):
        e = (x+1)*math.pi/4; we = w*math.pi/4
        ce, se = math.cos(e), math.sin(e)
        for i in range(nx):
            x1 = 2*math.pi*i/nx
            for j in range(nx):
                x2 = 2*math.pi*j/nx
                wt = we*se*ce*(2*math.pi/nx)**2/(2*math.pi**2)
                pts.append(((ce*math.cos(x1), ce*math.sin(x1), se*math.cos(x2), se*math.sin(x2)), wt))
    return pts

def moments(L, R, rule):
    """int dV w(L V^{-1} R): returns m0, m1[mu], m2[mu][nu]"""
    m0 = 0.0; m1 = [0.0]*4; m2 = [[0.0]*4 for _ in range(4)]
    for V, wt in rule:
        P = qmul(qmul(L, qinv(V)), R)
        g = wt*math.exp(BETA*P[0])       # (beta/2) tr P = beta * P0
        m0 += g
        for m in range(4):
            gm = g*V[m]; m1[m] += gm
            for n in range(4): m2[m][n] += gm*V[n]
    return m0, m1, m2

def K_apply(U, T, rule):
    U1, U2 = U; T1, T2 = T
    A = moments(qmul(U1, T2), qinv(T1), rule)   # P1 = U1 T2 V1^-1 T1^-1
    B = moments(qmul(U2, T1), qinv(T2), rule)   # P2 = U2 T1 V2^-1 T2^-1
    K0 = A[0]*B[0]
    Khalf = 2*sum(S[m]*A[1][m]*B[1][m] for m in range(4))                 # chi_1/2 = 2 X0
    X0sq = sum(S[m]*S[n]*A[2][m][n]*B[2][m][n] for m in range(4) for n in range(4))
    K1 = 4*X0sq - K0                                                      # chi_1 = 4 X0^2 - 1
    H = qmul(U1, U2)
    return K0, Khalf/(2*H[0]), K1/(4*H[0]**2 - 1)

mp.dps = 30
dens = lambda t: (2/mpi)*msin(t)**2*mexp(BETA*mcos(t))
w0 = quad(dens, [0, mpi])
wh = quad(lambda t: dens(t)*2*mcos(t), [0, mpi])/2
w1 = quad(lambda t: dens(t)*(4*mcos(t)**2 - 1), [0, mpi])/3
refh = float((wh/w0)**2); ref1 = float((w1/w0)**2)

rng = random.Random(12345)
I = (1.0, 0.0, 0.0, 0.0)
configs = []
for c in range(3):
    U = (rand_su2(rng), rand_su2(rng))
    T = (I, I) if c == 0 else (rand_su2(rng), rand_su2(rng))
    configs.append((U, T))

out = ["beta=%g  reference (w_1/2/w_0)^2=%.16g  (w_1/w_0)^2=%.16g" % (BETA, refh, ref1)]
fails = []
res = {}
for (ne, nx) in ((24, 32), (32, 40)):
    rule = haar_rule(ne, nx)
    rows = []
    for c, (U, T) in enumerate(configs):
        K0, Ah, A1 = K_apply(U, T, rule)
        Rh, R1 = Ah/K0, A1/K0
        rows.append((K0, Rh, R1))
        out.append("rule(%d,%d) cfg%d T=%s: Kchi0=%.16g R_1/2=%.16g resid=%.2e  R_1=%.16g resid=%.2e" % (
            ne, nx, c, "1" if c == 0 else "rand", K0, Rh, (Rh-refh)/refh, R1, (R1-ref1)/ref1))
    res[(ne, nx)] = rows
rows = res[(32, 40)]
K0s = [r[0] for r in rows]; Rhs = [r[1] for r in rows]; R1s = [r[2] for r in rows]
if (max(K0s)-min(K0s))/K0s[0] >= 1e-11: fails.append("B1")
if (max(Rhs)-min(Rhs))/Rhs[0] >= 1e-10: fails.append("B2")
if max(abs(r-refh)/refh for r in Rhs) >= 1e-11: fails.append("B3")
if max(abs(r-ref1)/ref1 for r in R1s) >= 1e-11: fails.append("B4")
conv = max(abs(a[k]-b[k])/abs(b[k]) for a, b in zip(res[(24, 32)], rows) for k in range(3))
out.append("rule convergence max rel diff = %.2e" % conv)
if conv >= 1e-12: fails.append("B5")
out.append("FAILS: " + (", ".join(fails) if fails else "none"))
txt = "\n".join(out); print(txt)
name = "transfer_results.txt"; k = 1
while os.path.exists(name):
    name = "transfer_results_%d.txt" % k; k += 1
open(name, "w").write(txt + "\n")
sys.exit(1 if fails else 0)
