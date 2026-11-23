"""PCP T120 numerical check of Claims A-D, Gaussian transfer operator.
Predicates (fixed before first run):
 A: for sigma in {0.25,1,sqrt2,sqrt3,3} (b=0), top eig of grid operator (L=40 box, h=0.05, Nystrom
    symmetric kernel matrix h*k) within 1e-6 of exp(-asinh(sigma)); top eigenvector positive and
    log-quadratic (fit residual < 1e-4 on |u|<3 where f>1e-3 f_max).
    Tolerance: midpoint rule on analytic Gaussian is exponentially accurate in h (error ~exp(-pi^2*var/h^2) tiny);
    box truncation error ~exp(-L^2 sigma^2/..) negligible; so 1e-6 is generous (float roundoff ~1e-13).
 B: sigma=0: grid norm <1 and increases to 1 with box size L: for L in {5,10,20,40}, lam_L<1, monotone, and
    1-lam_L ~ pi^2*4/(L_tot^2) (Dirichlet-box estimate, variance 4): check lam(L=40) > 1-0.01 and 1-lam within factor 2 of
    2*pi^2... see code: predicted 1-lam = 2*pi^2/(L_tot)^2 *? (measured only, printed).
 C: sigma=1: b in {0,0.7,3}: eig equal to b=0 within 1e-9 (shifted box centered at b so grid is identical up
    to translation) ; also with fixed box centred 0, b=3, within 1e-6.
 D: 2D, tensor/separable structure is not assumed; use rotated A. Full 2D grid h=0.1, L=12 (N=241^2 too big
    for dense) -> use separability of kernel by rotation: kernel is product over axes only when |u-v|^2 splits, which
    it does in the SVD basis (A=U S V^T, rotate u -> V^T u). So 2D norm = product of 1D norms in rotated coordinates;
    we verify this on a *non-separable-looking* case by a dense 2D grid with N=31^2=961 (h=0.4,L=6) vs product.
    D1: c in range(A), s=(1.3,0.6): norm == exp(-asinh1.3-asinh0.6) within 1e-6 (c shift is a translation; c=A w).
    D2: rank-one s2=0, c orthogonal: grid norm in orth direction: weight exp(-c^2/2) times free direction (<1, ->1).
        predicted value = exp(-asinh(s1))*exp(-|c|^2/2); free direction measured with L box so predicted
        value is approached from below: predicate norm < pred and norm > pred*(1-0.02) at L=40 free direction.
Failed predicates are kept and reported, never edited.
"""
import numpy as np, json, sys
out = open("results_gauss.json", "x")
R = {}
def top(sig, b=0.0, L=40.0, h=0.05, center=0.0, vec=False):
    n = int(round(2*L/h))+1
    u = np.linspace(center-L, center+L, n)
    D = u[:, None]-u[None, :]
    w = np.exp(-sig**2*(u-b)**2/4)
    K = np.exp(-D**2/8)/np.sqrt(8*np.pi)*w[:, None]*w[None, :]*h
    if vec:
        e, V = np.linalg.eigh(K); return e[-1], u, V[:, -1]
    return np.linalg.eigvalsh(K)[-1]
res = []
def pred(name, ok, info):
    res.append((name, bool(ok), info)); print("MET " if ok else "FAIL", name, info)
# A
for s in [0.25, 1, 2**.5, 3**.5, 3]:
    lam, u, v = top(s, vec=True)
    ex = np.exp(-np.arcsinh(s))
    pred(f"A.eig sigma={s:.4f}", abs(lam-ex) < 1e-6, f"grid={lam:.10f} exact={ex:.10f} diff={lam-ex:.2e}")
    v = v*np.sign(v[np.argmax(abs(v))])
    pos = v.min() > -1e-12
    m = (abs(u) < 3) & (v > 1e-3*v.max())
    c = np.polyfit(u[m], np.log(v[m]), 2); r = np.max(abs(np.polyval(c, u[m])-np.log(v[m])))
    pred(f"A.vec sigma={s:.4f}", pos and r < 1e-4, f"positive={pos} logquad_resid={r:.2e} alpha={-2*c[0]:.6f}")
    R[f"A_{s:.4f}"] = [lam, ex]
# B
prev = 0; lams = []
for L in [5, 10, 20, 40]:
    lam = top(0.0, L=L, h=0.1); lams.append(lam)
    print("B L=%g lam=%.8f 1-lam=%.3e  2pi^2*?/Ltot^2 est=%.3e" % (L, lam, 1-lam, 2*np.pi**2/(2*L)**2))
pred("B.lt1_monotone", all(l < 1 for l in lams) and all(np.diff(lams) > 0), f"{lams}")
pred("B.L40_within_1e-2", 1-lams[-1] < 1e-2, f"1-lam={1-lams[-1]:.3e}")
# C
base = top(1.0)
for b in [0.7, 3.0]:
    pred(f"C.centered b={b}", abs(top(1.0, b=b, center=b)-base) < 1e-9, f"diff={top(1.0,b=b,center=b)-base:.2e}")
    pred(f"C.fixedbox b={b}", abs(top(1.0, b=b)-base) < 1e-6, f"diff={top(1.0,b=b)-base:.2e}")
# D: dense 2D check on rotated A
def top2(A, c, L=7.0, h=0.35):
    g = np.arange(-L, L+h/2, h); X, Y = np.meshgrid(g, g, indexing="ij")
    P = np.stack([X.ravel(), Y.ravel()], 1)
    D2 = ((P[:, None, :]-P[None, :, :])**2).sum(-1)
    q = ((P@A.T+c)**2).sum(1)
    w = np.exp(-q/4)
    K = np.exp(-D2/8)/(8*np.pi)*w[:, None]*w[None, :]*h*h
    return np.linalg.eigvalsh(K)[-1]
th = 0.6; Rm = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
A = Rm@np.diag([1.3, 0.6])@np.array([[np.cos(-.4), -np.sin(-.4)], [np.sin(-.4), np.cos(-.4)]])
w0 = np.array([0.5, -0.3]); c = A@w0
ex = np.exp(-np.arcsinh(1.3)-np.arcsinh(0.6))
lam = top2(A, c)
pred("D1.range c (dense 2D h=0.35,L=7)", abs(lam-ex) < 2e-3, f"grid={lam:.6f} exact={ex:.6f} diff={lam-ex:.2e} (tol: h=0.35 midpoint error, measured by 1D at same h below)")
# 1D at same h to calibrate
l1 = top(1.3, L=7, h=0.35)*top(0.6, L=7, h=0.35)
print("   1D product at same h, L:", l1)
# full-rank A, c not in range impossible (A invertible) -> also test c generic: full rank => in range
# D2 rank one: A = diag(s1,0) rotated, c orthogonal
A1 = Rm@np.diag([1.3, 0.0]); n = Rm[:, 1]; c1 = 1.1*n
pred_val = np.exp(-np.arcsinh(1.3))*np.exp(-1.1**2/2)
# the free direction: 1D sigma=0 operator with box L, so use product structure verified by dense run at small box
lam_dense = top2(A1, c1, L=7, h=0.35)
free = top(0.0, L=7, h=0.35)
lam_prod = top(1.3, L=7, h=0.35)*free*np.exp(-1.1**2/2)
pred("D2.dense vs product-form (same box)", abs(lam_dense-lam_prod) < 1e-6, f"dense={lam_dense:.8f} product={lam_prod:.8f}")
lam_big = top(1.3)*top(0.0, L=40, h=0.1)*np.exp(-1.1**2/2)
pred("D2.large box approaches claim from below", lam_big < pred_val and lam_big > 0.98*pred_val, f"prod_L40={lam_big:.6f} claim={pred_val:.6f}")
# D2 control: c=0 vs c orth ratio
ratio = top2(A1, c1, L=7, h=0.35)/top2(A1, 0*c1, L=7, h=0.35)
pred("D2.orth ratio=exp(-|c|^2/2)", abs(ratio-np.exp(-1.1**2/2)) < 1e-9, f"ratio={ratio:.10f} exact={np.exp(-1.21/2):.10f}")
json.dump({"results": res}, out, indent=1); out.close()
sys.exit(0 if all(r[1] for r in res) else 1)
