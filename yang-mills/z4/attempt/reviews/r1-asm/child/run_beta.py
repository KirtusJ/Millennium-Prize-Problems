"""run_beta.py BETA  -- 1D double-well transfer operator, high precision (decimal) splitting.

PREDICATES FIXED BEFORE FIRST RUN (judged in analyze.py; tolerances and origin):
 Setup: kappa=1, h=1/sqrt(beta), N=round(2pi/h) to multiple of 4, h=2pi/N. No randomness (no seed needed).
 Float64 cannot resolve lambda_e-lambda_o ~ exp(-c* sqrt(beta)) (<1e-16 for beta>=64), so lambda_e, lambda_o and the
 even eigenvector are computed with python decimal at prec = ceil(c* sqrt(beta)/ln10)+60 digits (inverse iteration, shift from float64 eigh).
 Self-check predicate S1: inverse iteration residual max|A v - lam v| <= 10^-(prec-40)  (tolerance: working precision minus 40 guard digits).
 Self-check predicate S2: even vs odd matrices from the sigma fold: asymmetry max|A-A^T| <= 10^-(prec-40) is NOT required (T is only sigma-symmetric up to exp(-beta*...) truncation of the k=+-1 images); reported only.
 (a) A: r=-log m/sqrt(beta) satisfies |r-c*| < |r-2c*| for every beta in {64,256,1024,4096}; AND |r-c*| nonincreasing in beta;
     AND fit r = c + (a log beta + b)/sqrt(beta) on the three largest beta gives c within 3% of c*.
     (tolerance origin: m ~ poly(beta) exp(-c* sqrt(beta)) so corrections O(log beta/sqrt beta); 3% is my guess of fit quality, an expectation not a theorem.)
 (b) B: q=(-log g(pi/2)+log g(0))/sqrt(beta): |q-c*/2| < |q-c*| for every beta and same fit c within 3% of c*/2.
 (c) C: min over grid set S={eps>=2eta (eta=.25)} of (T phi)/(lambda_e phi) >= 1-1e-9 (1e-9 = float64 rounding slack in sums of 1e2 positive terms);
     same on kink window |x-pi/2|<=0.2, and at x=pi/2. Per rule 4 I count how many beta qualify (hypothesis: T phi>=lam phi is expected only where
     the subsolution inequality is meant to hold, i.e. S; the kink window is separately reported, not assumed).
 (d) D: |2q - r|/r <= 0.10 at the largest beta (both carry O(log beta/sqrt beta) corrections; 10% my guess).
 Result file results_beta<BETA>.json is opened with mode 'x'.
"""
import sys, json, math
from decimal import Decimal as D, getcontext
import numpy as np
from cstar import cstar

beta = int(sys.argv[1])
CS = cstar(800)
h0 = 1.0/math.sqrt(beta)
N = int(round(2*math.pi/h0/4))*4
h = 2*math.pi/N
prec = int(math.ceil(CS*math.sqrt(beta)/math.log(10)))+60
getcontext().prec = prec + 20

# ---- pi in Decimal (Machin)
def arctan_inv(n):
    x = D(1)/n; s = x; t = x; k = 1; n2 = n*n
    while abs(t) > D(10)**-(prec+25):
        t = -t/n2; k += 2; s += t/k
    return s
PI = 4*(4*arctan_inv(5)-arctan_inv(239))
def dsin(x):
    s = D(0); t = x; k = 1
    while abs(t) > D(10)**-(prec+25):
        s += t; t = -t*x*x/((k+1)*(k+2)); k += 2
    return s
H = 2*PI/N
Hb = D(beta)
# weights a_i = exp(-eps/2) = 1/(s+sqrt(1+s^2)), s=|sin x_i| = |sin(i H)|  (x_i=-pi+iH)
a = []
for i in range(N):
    s = abs(dsin(i*H)); a.append(1/(s+(1+s*s).sqrt()))
pref = H*(Hb/(2*PI)).sqrt()
Kd = {}
for n in range(0, N):
    v = D(0)
    for k in (-1, 0, 1):
        d = n*H+2*PI*k
        v += (-(Hb*d*d)/2).exp()
    Kd[n] = pref*v; Kd[-n] = Kd[n]
M = N//2
def sector(sg):
    A = [[None]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            A[i][j] = a[i]*a[j]*(Kd[i-j]+sg*Kd[i-j-M if i-j-M > -N else i-j+M] if False else 0)
    return A
def Tent(i, j): return a[i]*a[j]*Kd[i-j]
def sector(sg):
    return [[Tent(i, j)+sg*Tent(i, j+M) for j in range(M)] for i in range(M)]
Ae, Ao = sector(1), sector(-1)
asym = max(abs(Ae[i][j]-Ae[j][i]) for i in range(0, M, 7) for j in range(M))

def solve_top(A):
    Af = np.array([[float(x) for x in r] for r in A])
    Af = (Af+Af.T)/2
    w, V = np.linalg.eigh(Af)
    mu = w[-1]; v0 = V[:, -1]
    mu = D(float(mu))
    n = len(A)
    # LU with partial pivoting of A - mu I
    L = [[x for x in r] for r in A]
    for i in range(n): L[i][i] -= mu
    piv = list(range(n))
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(L[r][c]))
        if p != c: L[c], L[p] = L[p], L[c]; piv[c], piv[p] = piv[p], piv[c]
        pc = L[c][c]; rc = L[c]
        for r in range(c+1, n):
            f = L[r][c]/pc
            if f != 0:
                L[r][c] = f; rr = L[r]
                for k in range(c+1, n): rr[k] -= f*rc[k]
            else: L[r][c] = D(0)
    def solve(b):
        b = [b[piv[i]] for i in range(n)]
        for i in range(n):
            s = b[i]; Li = L[i]
            for k in range(i): s -= Li[k]*b[k]
            b[i] = s
        for i in range(n-1, -1, -1):
            s = b[i]; Li = L[i]
            for k in range(i+1, n): s -= Li[k]*b[k]
            b[i] = s/Li[i]
        return b
    # NOTE: pivoting permutes rows only; solve on permuted b is correct for P A = L U.
    v = [D(float(x)) for x in v0]
    for it in range(60):
        v = solve(v)
        nv = max(abs(x) for x in v)
        v = [x/nv for x in v]
        Av = [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
        lam = sum(v[i]*Av[i] for i in range(n))/sum(x*x for x in v)
        res = max(abs(Av[i]-lam*v[i]) for i in range(n))
        if res < D(10)**-(prec-40): break
    return lam, v, res, it
le, ve, rese, ite = solve_top(Ae)
lo, vo, reso, ito = solve_top(Ao)
delta = (le-lo)/lo
m = (1+delta).ln()
r = float(-m.ln()/D(math.sqrt(beta)))
# eigenvector: g(0)=u[0] (x=-pi == pi well), g(pi/2): index 3N/4 mod M = M/2 ... N/4
i_q = (3*N//4) % M
assert abs(-math.pi+ (3*N//4)*h - math.pi/2) < 1e-9
sc = ve[0]
q = float(-(ve[i_q]/sc).ln()/D(math.sqrt(beta)))

# ---- (c) tent subsolution, float64
x = -math.pi+np.arange(N)*h
eps = 2*np.arcsinh(np.abs(np.sin(x)))
af = np.exp(-eps/2)
dd = x[:, None]-x[None, :]
K = h*math.sqrt(beta/(2*math.pi))*sum(np.exp(-beta*(dd+2*math.pi*k)**2/2) for k in (-1, 0, 1))
T = af[:, None]*K*af[None, :]
eta = 0.25
gx, gw = np.polynomial.legendre.leggauss(120)
def Psi(dist, e):
    s = dist/2*(gx+1); w = gw*dist/2
    return np.sum(w*np.sqrt(2*(2*np.arcsinh(np.abs(np.sin(s)))+e)))
ax = np.abs(x); dist = np.minimum(ax, math.pi-ax)
Ps = np.array([Psi(d, eta) for d in dist])
phi = np.exp(-math.sqrt(beta)*(Ps-Ps.min()))
ratio = (T@phi)/(float(le)*phi)
S = eps >= 2*eta
W = np.abs(x-math.pi/2) <= 0.2
kink = int(np.argmin(np.abs(x-math.pi/2)))
out = dict(beta=beta, N=N, h=h, prec=prec, cstar=CS, le='%.40e'%le, lo='%.40e'%lo, delta='%.30e'%delta,
           m='%.30e'%m, r=r, q=q, res_e='%.3e'%rese, res_o='%.3e'%reso, it_e=ite, it_o=ito, asym_even='%.3e'%asym,
           psi_tent_halfpi_eta0=Psi(math.pi/2, 0.0), cstar_half=CS/2,
           c_minS=float(ratio[S].min()), c_nS=int(S.sum()), c_argminS_x=float(x[S][np.argmin(ratio[S])]),
           c_minW=float(ratio[W].min()), c_nW=int(W.sum()), c_kink=float(ratio[kink]), c_kink_x=float(x[kink]),
           c_ratio_W=[float(v) for v in ratio[W]])
with open("results_beta%d_v2.json" % beta, "x") as f: json.dump(out, f, indent=1)
print({k: v for k, v in out.items() if k != "c_ratio_W"})
