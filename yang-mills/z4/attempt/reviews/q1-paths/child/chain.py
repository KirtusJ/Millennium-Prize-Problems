"""T153 chain-of-balls test.  Usage: python3 chain.py TAG KAPPA beta1 beta2 ...   (results_TAG.json written with mode 'x')
Arithmetic: python Decimal, 50 digits, for sector eigenpairs (inverse iteration from float64 start, shift = float eigenvalue),
so that g, f (hence h=f/g) keep relative accuracy in the tail near x=pi/2 (g~exp(-2.3 sqrt(beta))). numpy float only for the start vector
and for rho_CB (positive-term Nystrom sums, relatively accurate).
PREDICATES (fixed before first run):
 P1 T symmetric and sigma-commuting (float, beta=16): max abs defect < 1e-14 * max T.   [tol = a few double eps]
 P2 g>0 on A; int_A f g > 0 after sign fix; sum g^2 dx (full circle) = 1 within 1e-40.   [Decimal precision]
 P3 Delta_identity == Delta_E(h) relative difference < 1e-25 (exact discrete identity; tol >> solver residual ~1e-35, << 50 digits).
 P4 L <= M per beta.      P5 M <= R per beta.      P6 Delta>0 and decreasing in beta.
 P7 (statement) h odd under x->-x: max|h(x)+h(-x)| < 1e-20 relative to max|h|.  (expectation taken from the task text)
 P8 (statement) Delta/lam_e < 1e-16 for beta>=36 ("below machine precision"): per-case count reported.
 P9 rho_CB refined(half-grid) vs coarse: measured only.
"""
import sys, json, math
from decimal import Decimal as D, getcontext
import numpy as np
getcontext().prec = 50
tag, kappa = sys.argv[1], float(sys.argv[2]); betas = [int(b) for b in sys.argv[3:]]

def pi_dec():
    getcontext().prec += 5
    def arctan_inv(n):
        x = D(1)/n; t = x; s = x; k = 1; n2 = n*n
        while abs(t) > D(10)**(-getcontext().prec):
            t = -t/n2; k += 2; s += t/k
        return s
    p = 4*(4*arctan_inv(5) - arctan_inv(239)); getcontext().prec -= 5; return +p
PI = pi_dec()
def sin_dec(x):
    s = t = x; k = 1; x2 = x*x
    while abs(t) > D(10)**(-getcontext().prec-2):
        t = -t*x2/((k+1)*(k+2)); k += 2; s += t
    return s

def lu(A):
    n = len(A); A = [r[:] for r in A]; piv = list(range(n))
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        A[k], A[p] = A[p], A[k]; piv[k], piv[p] = piv[p], piv[k]
        Ak = A[k]; d = Ak[k]
        for i in range(k+1, n):
            Ai = A[i]; m = Ai[k]/d; Ai[k] = m
            Ai[k+1:] = [a - m*b for a, b in zip(Ai[k+1:], Ak[k+1:])]
    return A, piv
def lusolve(F, b):
    A, piv = F; n = len(A); y = [b[p] for p in piv]
    for i in range(n):
        y[i] -= sum(a*c for a, c in zip(A[i][:i], y[:i]))
    for i in range(n-1, -1, -1):
        y[i] = (y[i] - sum(a*c for a, c in zip(A[i][i+1:], y[i+1:])))/A[i][i]
    return y
def matvec(A, v): return [sum(a*c for a, c in zip(r, v)) for r in A]
def dot(a, b): return sum(x*y for x, y in zip(a, b))

def top_pair(A):
    Af = np.array([[float(x) for x in r] for r in A]); w, V = np.linalg.eigh(Af)
    mu = D(float(w[-1])); v = [D(float(x)) for x in V[:, -1]]
    F = lu([[A[i][j] - (mu if i == j else 0) for j in range(len(A))] for i in range(len(A))])
    for _ in range(4):
        v = lusolve(F, v); nr = dot(v, v).sqrt(); v = [x/nr for x in v]
    lam = dot(v, matvec(A, v))/dot(v, v)
    res = max(abs(a - lam*b) for a, b in zip(matvec(A, v), v))
    return lam, v, float(res), float(w[-1])

def run(beta):
    sb = D(beta).sqrt(); sbf = math.sqrt(beta)
    N0 = math.ceil(math.pi*sbf)
    N = N0
    while True:
        m = math.ceil(math.pi*sbf/(N*kappa))
        for mm in range(m, m+4):
            if (N*mm) % 4 == 0: m = mm; break
        else: N += 1; continue
        break
    Nx = 2*N*m; dx = 2*PI/Nx; h2 = Nx//2; q = Nx//4
    sinv = [abs(sin_dec(-PI + j*dx)) for j in range(Nx)]
    e = [1/(s + (s*s+1).sqrt()) for s in sinv]            # exp(-eps/2)
    c0 = (D(beta)/(2*PI)).sqrt()
    Kd = []
    for d in range(Nx):
        dl = (((d + h2) % Nx) - h2)*dx
        Kd.append(sum(c0*(-D(beta)*(dl + 2*PI*k)**2/2).exp() for k in (-1, 0, 1)))
    A = range(q, q+h2)
    TAA = [[dx*e[a]*Kd[(a-b) % Nx]*e[b] for b in A] for a in A]
    Rm = [[dx*e[a]*Kd[(a-b-h2) % Nx]*e[b] for b in A] for a in A]
    n = h2
    Tp = [[TAA[i][j]+Rm[i][j] for j in range(n)] for i in range(n)]
    Tm = [[TAA[i][j]-Rm[i][j] for j in range(n)] for i in range(n)]
    le, g, rg, lef = top_pair(Tp); lo, f, rf, lof = top_pair(Tm)
    sg = dot(g, g); g = [x/(2*dx*sg).sqrt() for x in g]; sf = dot(f, f); f = [x/(2*dx*sf).sqrt() for x in f]
    if sum(g) < 0: g = [-x for x in g]
    if dot(f, g) < 0: f = [-x for x in f]
    fg = dot(f, g)
    Rg = matvec(Rm, g)
    Delta_id = 2*dot(f, Rg)/fg
    # full circle arrays
    gF = [None]*Nx; fF = [None]*Nx
    for j in range(Nx):
        if q <= j < q+h2: gF[j] = g[j-q]; fF[j] = f[j-q]
        else:
            jp = (j+h2) % Nx; gF[j] = g[jp-q]; fF[j] = -f[jp-q]
    hF = [fF[j]/gF[j] for j in range(Nx)]
    # E(h)
    Ssum = D(0)
    for x in range(Nx):
        ex = e[x]*gF[x]; hx = hF[x]
        Ssum += ex*sum(Kd[(x-y) % Nx]*e[y]*gF[y]*(hx-hF[y])**2 for y in range(Nx))
    Delta_E = Ssum*dx*dx/2
    # direct difference (diagnostic)
    Delta_dir = le - lo
    norm_full = dx*sum(x*x for x in gF)
    # reflection test
    odd = max(abs(hF[j] + hF[(Nx-j) % Nx]) for j in range(Nx)); even = max(abs(hF[j] - hF[(Nx-j) % Nx]) for j in range(Nx))
    hmax = max(abs(x) for x in hF)
    # balls (cell-overlap weights)
    rho_b = (1/(2*sb))/dx; U = int(rho_b + D("1.5"))
    w = {}
    for u in range(-U, U+1):
        ov = min(D(u)+D(1)/2, rho_b) - max(D(u)-D(1)/2, -rho_b)
        if ov > 0: w[u] = ov/(2*rho_b)
    wsum = sum(w.values())
    jc = lambda i: (h2 + i*m) % Nx
    mi = [sum(wu*hF[(jc(i)+u) % Nx] for u, wu in w.items()) for i in range(N+1)]
    Mv = D(0)
    for i in range(N):
        Mv += sum(wu*wv*(hF[(jc(i)+u) % Nx]-hF[(jc(i+1)+v) % Nx])**2 for u, wu in w.items() for v, wv in w.items())
    Mv *= N
    L = (mi[0]-mi[N])**2
    # rho_CB on refined grid (float, Nystrom)
    dxf = float(dx); rf_ = 1/(2*sbf); lef_ = float(le)
    gA = np.array([float(x) for x in g]); xA = -math.pi + dxf*np.arange(q, q+h2)
    npts = 2*Nx; xs = -math.pi + dxf/2*np.arange(npts)
    def Kf(dlt):
        return sum(math.sqrt(beta/(2*math.pi))*np.exp(-beta*(dlt+2*math.pi*k)**2/2) for k in (-1, 0, 1))
    ef = lambda x: 1/(np.abs(np.sin(x)) + np.sqrt(np.sin(x)**2+1))
    Tf = lambda x, y: ef(x)[:, None]*Kf(x[:, None]-y[None, :])*ef(y)[None, :]
    gs = (Tf(xs, xA) + Tf(xs, xA+math.pi))@gA*dxf/lef_
    Tfull = Tf(xs, xs)
    ratio_den = Tfull*gs[:, None]*gs[None, :]
    def rho_cb(step):
        idx = np.arange(0, npts, step); num = np.zeros((npts, npts))
        for i in range(N):
            ci = i*math.pi/N; cj = (i+1)*math.pi/N
            def ball(c):
                d = np.abs(((xs - c + math.pi) % (2*math.pi)) - math.pi)
                return np.where(d <= rf_*(1+1e-9))[0]
            ix = ball(ci); iy = ball(cj)
            ix = np.intersect1d(ix, idx); iy = np.intersect1d(iy, idx)
            num[np.ix_(ix, iy)] += 1/(2*rf_)**2
        mask = num > 0
        return float((num[mask]/ratio_den[mask]).max())
    rho_ref = rho_cb(1); rho_coarse = rho_cb(2)
    Rv = 2*N*D(rho_ref)*Delta_id
    # g(pi/2) tail and float check of T
    out = dict(beta=beta, N=N, m=m, Nx=Nx, dx=float(dx), L=float(L), M=float(Mv), R=float(Rv), Delta_id=str(Delta_id), Delta_E=str(Delta_E),
        Delta_dir=str(Delta_dir), reldiff_id_E=float(abs(Delta_id-Delta_E)/Delta_id), lam_e=float(le), lam_o=float(lo), Delta_over_lam=float(Delta_id/le),
        M_over_L=float(Mv/L), R_over_M=float(Rv/Mv), logRL_over_logbeta=float(math.log(float(Rv/L))/math.log(beta)),
        rho_refined=rho_ref, rho_coarse=rho_coarse, m0=float(mi[0]), mN=float(mi[N]), mN_plus_m0=float(mi[N]+mi[0]),
        resid_g=rg, resid_f=rf, g_min=float(min(g)), g_at_halfpi=float(g[-1]), h_odd_defect=float(odd/hmax), h_even_defect=float(even/hmax),
        wsum=float(wsum), norm_full=str(norm_full), fg_pos=bool(fg > 0), g_pos=bool(min(g) > 0), eig_double_diff=lef-lof)
    return out

res = []
for b in betas:
    r = run(b); res.append(r); print(json.dumps(r), flush=True)
with open("results_%s.json" % tag, "x") as fh: json.dump(res, fh, indent=1)
