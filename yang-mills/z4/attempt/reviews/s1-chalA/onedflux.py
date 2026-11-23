"""onedflux.py BETA -- independent recomputation (worker r1-asm, T158) of m = log(lambda_e/lambda_o) on the 1D grid model
used by the child T160 (kappa=1: N = 4*round(2pi sqrt(beta)/4), h = 2pi/N, x_i = -pi + i h,
eps = 2 asinh|sin x|, K_xy = h sqrt(beta/2pi) sum_{k=-1,0,1} exp(-beta (x-y+2pi k)^2/2), T = e^{-eps/2} K e^{-eps/2},
sigma: x -> x + pi).

METHOD (different from the child's eigen-difference by inverse iteration):
 * even/odd folded matrices on A = {x_i : i in [N/4, 3N/4)} ( = [-pi/2, pi/2) ), T_pm(x,y) = T(x,y) +- T(x, sigma y);
 * top eigenvectors g_A, f_A by repeated matrix squaring (2^12 = 4096 powers) in Python Decimal, then Rayleigh quotient;
 * Delta from the flux identity (I0) of TUNNEL_LOWER.md: Delta <f_A, g_A> = 2 <f_A, R g_A>, R(x,y) = T(x, sigma y) on A x A.
   (Exact identity: with T_+ g = l_e g, T_- f = l_o f, (l_e - l_o)<f,g> = <f,(T_+ - T_-)g> = 2<f,R g>.)
PREDICATES (fixed before the first run):
 Q1: Decimal precision prec = ceil(c* sqrt(beta)/ln 10) + 60 digits; eigen-residual max|T_+ g - l_e g| / max|g| <= 10^-(prec-40)
     and same for f (tolerance: working precision less 40 guard digits; power 4096 with ratio of second to first eigenvalue
     <= 0.95 gives 0.95^4096 ~ 1e-91, enough at beta <= 256; if Q1 fails the run is reported as not converged).
 Q2: r := -log m / sqrt(beta) agrees with the child's r (child/results_beta<BETA>_v2.json) to |diff| <= 1e-6
     (tolerance: same model, both high precision; 1e-6 is far above rounding, far below any modelling change).
 Q3: Delta_flux agrees with (l_e - l_o) from the two Rayleigh quotients to relative 1e-20 (both exact at this precision).
No randomness. Result file onedflux_beta<BETA>.json opened with mode "x".
"""
import sys, json, math
from decimal import Decimal as D, getcontext

beta = int(sys.argv[1])
CS = 4.6054132
N = int(round(2*math.pi*math.sqrt(beta)/4))*4
prec = int(math.ceil(CS*math.sqrt(beta)/math.log(10))) + 60
getcontext().prec = prec + 20
EPS = D(10) ** -(prec + 25)

def dpi():
    def at(n):
        x = D(1)/n; s = x; t = x; k = 1
        while abs(t) > EPS:
            t = -t/(n*n); k += 2; s += t/k
        return s
    return 4*(4*at(5) - at(239))
PI = dpi()
def dsin(x):
    s = D(0); t = x; k = 1
    while abs(t) > EPS:
        s += t; t = -t*x*x/((k+1)*(k+2)); k += 2
    return s
H = 2*PI/N
B = D(beta)
w = []
for i in range(N):
    s = abs(dsin(-PI + i*H))
    w.append(1/(s + (1 + s*s).sqrt()))          # e^{-eps/2} = e^{-asinh s}
pref = H*(B/(2*PI)).sqrt()
def kern(n):  # n = index difference mod N in [0, N)
    v = D(0)
    for k in (-1, 0, 1):
        d = n*H + 2*PI*k
        v += (-(B*d*d)/2).exp()
    return pref*v
kd = [kern(n) if n <= N//2 else None for n in range(N)]
for n in range(N//2 + 1, N):
    kd[n] = kern(n)
def T(i, j):
    return w[i]*kd[(i - j) % N]*w[j]
Aidx = list(range(N//4, 3*N//4)); M = len(Aidx)
Tp = [[T(i, j) + T(i, (j + N//2) % N) for j in Aidx] for i in Aidx]
Tm = [[T(i, j) - T(i, (j + N//2) % N) for j in Aidx] for i in Aidx]
R = [[T(i, (j + N//2) % N) for j in Aidx] for i in Aidx]

def matmul(X, Y):
    Yt = list(zip(*Y))
    return [[sum(a*b for a, b in zip(row, col)) for col in Yt] for row in X]
def topvec(Mx):
    P = Mx
    for _ in range(12):
        P = matmul(P, P)
        s = max(abs(v) for row in P for v in row)
        P = [[v/s for v in row] for row in P]
    v = [sum(row) for row in P]          # P applied to the all-ones vector
    s = max(abs(x) for x in v); v = [x/s for x in v]
    Mv = [sum(a*b for a, b in zip(row, v)) for row in Mx]
    lam = sum(a*b for a, b in zip(v, Mv))/sum(a*a for a in v)
    res = max(abs(a - lam*b) for a, b in zip(Mv, v))/max(abs(x) for x in v)
    return v, lam, res
g, le, rg = topvec(Tp)
f, lo, rf = topvec(Tm)
Rg = [sum(a*b for a, b in zip(row, g)) for row in R]
delta = 2*sum(a*b for a, b in zip(f, Rg))/sum(a*b for a, b in zip(f, g))
m = (le/lo).ln()
r = float(-(m.ln()))/math.sqrt(beta)
tol_res = D(10) ** -(prec - 40)
Q1 = bool(rg <= tol_res and rf <= tol_res)
Q3 = bool(abs(delta - (le - lo)) <= abs(delta)*D(10)**-20)
child = None; Q2 = None
try:
    with open("child/results_beta%d_v2.json" % beta) as fh:
        cj = json.load(fh)
    for key in ("r", "rr", "r_val"):
        if key in cj:
            child = float(cj[key]); break
    if child is None:
        child = float(-(D(cj["m"]).ln()))/math.sqrt(beta) if "m" in cj else None
    if child is not None:
        Q2 = bool(abs(child - r) <= 1e-6)
except FileNotFoundError:
    pass
out = dict(beta=beta, N=N, prec=prec, lambda_e='%.30e' % le, lambda_o='%.30e' % lo, delta_flux='%.20e' % delta,
           delta_rayleigh='%.20e' % (le - lo), m='%.20e' % m, r=r, child_r=child,
           res_g='%.3e' % rg, res_f='%.3e' % rf, Q1=Q1, Q2=Q2, Q3=Q3)
with open("onedflux_beta%d.json" % beta, "x") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
sys.exit(0 if (Q1 and Q3 and Q2 is not False) else 3)
