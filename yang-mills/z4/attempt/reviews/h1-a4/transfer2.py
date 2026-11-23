"""transfer2.py -- h1-a4, item (d): exact one-site SU(2) transfer, k=2, gauge-invariant,
center-even sector (both n_i odd).  T = e^{-V/2} K e^{-V/2}, K eigenvalue (I_{n1}/I_1)(I_{n2}/I_1),
V = 2 beta sin^2 th1 sin^2 th2 sin^2 gamma.  Basis Phi_{n1 n2 L} = R_{n1 L}(th1) R_{n2 L}(th2) sqrt(2L+1) P_L(cos gamma),
R_{nL} ∝ sin^L th C^{(L+1)}_{n-1-L}(cos th), n <= N.  e^{-V/2} applied by Gauss-Chebyshev-II (th, M points)
x Gauss-Legendre (cos gamma, M points) quadrature: this is the Galerkin matrix of e^{-V/2} (to quadrature
accuracy); truncation error controlled by N -> N+16 and M -> M+32.  Eigenvalues by Lanczos with full
reorthogonalisation, fixed start vector (seed 11).
Usage: python3 transfer2.py beta N M out.json [v0]   (v0: V set to 0, control)

PREDICATES (fixed before the first run):
 C1 (v0 run only) top 3 distinct Ritz values equal the 3 largest distinct products a[n1]a[n2],
    n_i odd, to 1e-10 absolute (Lanczos in double precision).
 C2 radial basis orthonormal under the quadrature: max|Gram-I| < 1e-10 for every L.
 C3 Lanczos residual ||T v - lambda v|| < 1e-9 for the 4 largest Ritz pairs.
 (D1..D4 are evaluated by analyse2.py across runs.)
"""
import sys, json, time, numpy as np
from besselnp import In_over_I1
t0 = time.time()
beta = float(sys.argv[1]); N = int(sys.argv[2]); M = int(sys.argv[3]); outp = sys.argv[4]
v0 = len(sys.argv) > 5 and sys.argv[5] == "v0"
out = open(outp, "x")
h = beta**(-1/3)
k = np.arange(1, M+1); th = k*np.pi/(M+1); x = np.cos(th); s = np.sin(th)
W = 2*s**2/(M+1)                       # prob. Haar weight (2/pi) sin^2 th d th
xg, wg = np.polynomial.legendre.leggauss(M); wg = wg/2
Ls = list(range(N))
def gegen(alpha, mmax, x):
    C = np.zeros((mmax+1, len(x))); C[0] = 1
    if mmax >= 1: C[1] = 2*alpha*x
    for m in range(2, mmax+1):
        C[m] = (2*x*(m+alpha-1)*C[m-1] - (m+2*alpha-2)*C[m-2])/m
    return C
R = {}; ns = {}; gram_err = 0.0
for L in Ls:
    nl = [n for n in range(L+1, N+1) if n % 2 == 1]
    if not nl: continue
    ns[L] = nl
    C = gegen(L+1, nl[-1]-1-L, x)
    cols = np.array([s**L*C[n-1-L] for n in nl]).T          # M x len
    nrm = np.sqrt((W[:, None]*cols**2).sum(0)); cols = cols/nrm
    G = cols.T@(W[:, None]*cols); gram_err = max(gram_err, np.abs(G-np.eye(len(nl))).max())
    R[L] = cols
Lk = sorted(R)
P = np.array([np.sqrt(2*L+1)*np.polynomial.legendre.legval(xg, [0]*L+[1]) for L in Lk])   # nL x M
sizes = [len(ns[L])**2 for L in Lk]; offs = np.cumsum([0]+sizes); D = offs[-1]
a = In_over_I1(N+1, beta)
Kd = np.concatenate([np.outer(a[ns[L]], a[ns[L]]).ravel() for L in Lk])
sg2 = 1-xg**2
V = 2*beta*np.einsum('a,b,g->abg', s**2, s**2, sg2)
E = np.ones_like(V) if v0 else np.exp(-V/2)
E2 = E.reshape(M*M, M)
RW = {L: W[:, None]*R[L] for L in Lk}
def synth(c):
    A = np.empty((len(Lk), M*M))
    for i, L in enumerate(Lk):
        cl = c[offs[i]:offs[i+1]].reshape(len(ns[L]), len(ns[L]))
        A[i] = (R[L]@cl@R[L].T).ravel()
    return A.T@P                                   # (M*M) x M
def anal(Gr):
    B = (Gr*wg[None, :])@P.T                        # (M*M) x nL
    c = np.empty(D)
    for i, L in enumerate(Lk):
        Bl = B[:, i].reshape(M, M)
        c[offs[i]:offs[i+1]] = (RW[L].T@Bl@RW[L]).ravel()
    return c
def Tapply(c):
    g = anal(synth(c)*E2)
    g = g*Kd
    return anal(synth(g)*E2)
# Lanczos, full reorthogonalisation
rng = np.random.default_rng(11)
q = rng.standard_normal(D); q /= np.linalg.norm(q)
Q = [q]; al = []; be = []
maxit = int(sys.argv[6]) if len(sys.argv) > 6 else 160
for it in range(maxit):
    w = Tapply(Q[-1]); al.append(Q[-1]@w)
    w -= al[-1]*Q[-1]
    if it > 0: w -= be[-1]*Q[-2]
    Qm = np.array(Q)
    for _ in range(2): w -= Qm.T@(Qm@w)
    b = np.linalg.norm(w); be.append(b)
    if b < 1e-14: break
    Q.append(w/b)
mm = len(al)
Tm = np.diag(al)+np.diag(be[:mm-1], 1)+np.diag(be[:mm-1], -1)
ev, U = np.linalg.eigh(Tm); idx = np.argsort(ev)[::-1]; ev = ev[idx]; U = U[:, idx]
Qm = np.array(Q[:mm])
lam = []; resid = []
for j in range(6):
    v = Qm.T@U[:, j]; v /= np.linalg.norm(v)
    r = np.linalg.norm(Tapply(v)-ev[j]*v); lam.append(float(ev[j])); resid.append(float(r))
res = {"beta": beta, "N": N, "M": M, "v0": v0, "dim": int(D), "lanczos_steps": mm, "h": h,
       "lambda": lam, "resid": resid, "gram_err": float(gram_err),
       "one_minus_lam_over_h": [(1-l)/h for l in lam], "minus_log_lam_over_h": [-np.log(l)/h for l in lam],
       "gap_log_ratio": [float(np.log(lam[0]/lam[j])) for j in range(1, 6)], "seconds": time.time()-t0}
fails = []
res["C2"] = bool(gram_err < 1e-10); fails += [] if res["C2"] else ["C2"]
res["C3"] = bool(max(resid[:4]) < 1e-9); fails += [] if res["C3"] else ["C3"]
if v0:
    prods = sorted({round(a[n1]*a[n2], 13) for L in Lk for n1 in ns[L] for n2 in ns[L]}, reverse=True)[:3]
    dist = []
    for l in lam:
        if not dist or abs(l-dist[-1]) > 1e-8: dist.append(l)
    res["C1_exact"] = prods; res["C1_ritz"] = dist[:3]
    res["C1"] = bool(np.allclose(dist[:3], prods, atol=1e-10, rtol=0)); fails += [] if res["C1"] else ["C1"]
res["fails"] = fails
json.dump(res, out, indent=1); out.close()
print(json.dumps({k2: res[k2] for k2 in ("beta", "N", "M", "dim", "lambda", "resid", "gap_log_ratio", "seconds", "fails")}))
sys.exit(1 if fails else 0)
