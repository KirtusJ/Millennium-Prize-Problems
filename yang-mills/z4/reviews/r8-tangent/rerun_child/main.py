"""Free U(1) lattice gauge field on Z^4: plaquette variances/covariances, g=1.

Conventions: theta_mn(x) = A_m(x)+A_n(x+e_m)-A_m(x+e_n)-A_n(x).  With A(x)=int e^{ikx} A~(k):
theta~_mn = p_m A~_n - p_n A~_m,  p_m = e^{ik_m}-1   (theta~ = p ^ A~).
Covariance = g^2 * projector onto range(p^):  P = (p^)(p^)^dagger / |p|^2, i.e.
 P_(mn),(rs) = [p_m pb_r d_ns - p_m pb_s d_nr - p_n pb_r d_ms + p_n pb_s d_mr]/|p|^2,
 <theta_a(x) theta_b(y)> = g^2 int d^4k/(2pi)^4 e^{ik(x-y)} P_ab(k).
Reductions (f_m = |p_m|^2 = 2-2cos k_m, F = sum f):
 V   = <t12(0)^2>          = int (f1+f2)/F
 C1  = <t12(0)t12(e3)>     = int cos k3 (f1+f2)/F
 C2  = <t12(0)t12(e1)>     = int cos k1 (f1+f2)/F
 C3  = <t12(0)t13(0)>      = int p2 pb3/F = int f2 f3/(4F)
 C4  = <t12(0)t12(3e3)>    = int cos 3k3 (f1+f2)/F
Infinite volume: Schwinger 1/F = int_0^inf e^{-tF} dt; 1D factors a,b,c_n,d_n by periodic trapezoid
 (M=4096), t=e^u, u in [-30, ln 2e4] (6000 nodes; head < 1e-12), tail beyond T neglected (integrands
 decay >= t^-3 -> tail ~ 1e-9). Cross-check: midpoint grid n=48 (shifted, avoids k=0).
Finite torus L^4: exact sum over k = 2pi n/L, k=0 excluded, divided by L^4.
Independent check: real-space L=4 torus, build d1 (plaquettes x links), projector D D^+ via SVD
 (rank tol 1e-9), compare entries to the Fourier sum at L=4.
Expected (derived): V_inf = 2/d = 1/2 (equipartition); V_L = (1-1/L^4)/2 exactly
 (rank of exact 2-cochains on torus = 4N-(N-1)-4 = 3N-3, shared over 6N plaquettes).

PREDICATES (fixed before first run), exit 0 iff all pass:
 P1 |V_inf(Schwinger) - 0.5| < 1e-7
 P2 |V_L - (1-L^-4)/2| < 1e-12 for L=8,16
 P3 real-space L=4 projector entries agree with Fourier L=4 for V,C1,C2,C3 to 1e-10 (C4 wraps at L=4: 3e3 = -e3, also checked)
 P4 Schwinger vs midpoint n=48 agree to 2e-3 for all five quantities (midpoint O(h^2) coarse)
 P5 sum rule: sum over the 6 plaquettes' variances per site = d-1 = 3 (trivially 6*V) -> |6V_inf-3|<1e-6
 P6 (d) Monte Carlo (seed 12345, 2e6 samples) of Y = sum_{c=1..3} theta_c^2/2, theta_c~N(0,s^2), s^2=1/2:
    analytic mean 3s^2/2=0.75, var 6(s^2/2)^2 = 0.375; |MC-analytic| < 5 sigma_MC.
Writes results.txt (refuses to overwrite).
"""
import os, sys, itertools, numpy as np
OUT = "results.txt"
if os.path.exists(OUT):
    print("results.txt exists; refusing to overwrite"); sys.exit(2)
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
out, fails = [], []
def log(s): out.append(s); print(s)
def pred(name, ok, detail):
    log(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")
    if not ok: fails.append(name)

# --- infinite volume via Schwinger
M = 4096; k = 2*np.pi*np.arange(M)/M; f = 2-2*np.cos(k)
u = np.linspace(-30, np.log(2e4), 6000); t = np.exp(u)
E = np.exp(-np.outer(t, f))  # 6000 x 8192
a = E.mean(1); b = (E*f).mean(1)
c1 = (E*np.cos(k)).mean(1); c3 = (E*np.cos(3*k)).mean(1); d1 = (E*f*np.cos(k)).mean(1)
I = lambda g: trap(g*t, u)
inf = dict(V=I(2*b*a**3), C1=I(2*b*a**2*c1), C2=I(d1*a**3 + c1*b*a**2), C3=I(0.25*b**2*a**2), C4=I(2*b*a**2*c3))

def quantities(k1, k2, k3, k4):
    f1, f2, f3, f4 = [2-2*np.cos(x) for x in (k1, k2, k3, k4)]
    F = f1+f2+f3+f4
    with np.errstate(divide="ignore", invalid="ignore"):
        w = np.where(F > 0, 1/F, 0.0)
    return dict(V=(f1+f2)*w, C1=np.cos(k3)*(f1+f2)*w, C2=np.cos(k1)*(f1+f2)*w,
                C3=0.25*f2*f3*w, C4=np.cos(3*k3)*(f1+f2)*w)

def torus(L):
    kk = 2*np.pi*np.arange(L)/L
    K = np.meshgrid(kk, kk, kk, kk, indexing="ij")
    return {n: v.sum()/L**4 for n, v in quantities(*K).items()}

def midpoint(n):
    kk = 2*np.pi*(np.arange(n)+0.5)/n
    K = np.meshgrid(kk, kk, kk, kk, indexing="ij")
    return {n_: v.mean() for n_, v in quantities(*K).items()}

T8, T16, T4, MP = torus(8), torus(16), torus(4), midpoint(48)

# --- real-space check at L=4
L = 4; N = L**4
def idx(x): return np.ravel_multi_index(tuple(np.mod(x, L)), (L,)*4)
def link(x, m): return idx(x)*4+m
planes = [(m, n) for m in range(4) for n in range(m+1, 4)]
D = np.zeros((N*6, N*4))
e = np.eye(4, dtype=int)
for xi in range(N):
    x = np.array(np.unravel_index(xi, (L,)*4))
    for pi, (m, n) in enumerate(planes):
        r = xi*6+pi
        D[r, link(x, m)] += 1; D[r, link(x+e[m], n)] += 1
        D[r, link(x+e[n], m)] -= 1; D[r, link(x, n)] -= 1
U, S, _ = np.linalg.svd(D, full_matrices=False)
rank = int((S > 1e-9*S[0]).sum()); Ur = U[:, :rank]
def Pent(x, pa, y, pb):
    ra = idx(np.array(x))*6+planes.index(pa); rb = idx(np.array(y))*6+planes.index(pb)
    return Ur[ra] @ Ur[rb]
o = [0, 0, 0, 0]
RS = dict(V=Pent(o, (0, 1), o, (0, 1)), C1=Pent(o, (0, 1), [0, 0, 1, 0], (0, 1)),
          C2=Pent(o, (0, 1), [1, 0, 0, 0], (0, 1)), C3=Pent(o, (0, 1), o, (0, 2)),
          C4=Pent(o, (0, 1), [0, 0, 3, 0], (0, 1)))

names = dict(V="<t12(0)^2>", C1="<t12(0)t12(e3)>", C2="<t12(0)t12(e1)>", C3="<t12(0)t13(0)>", C4="<t12(0)t12(3e3)>")
log(f"{'quantity':20s} {'inf(Schwinger)':>16s} {'inf(midpt48)':>14s} {'L=16':>16s} {'L=8':>16s} {'L=4 Fourier':>14s} {'L=4 realspace':>14s}")
for q in names:
    log(f"{names[q]:20s} {inf[q]:16.10f} {MP[q]:14.8f} {T16[q]:16.12f} {T8[q]:16.12f} {T4[q]:14.10f} {RS[q]:14.10f}")
log(f"real-space L=4 rank of d1 = {rank} (expected 3N-3 = {3*N-3})")
pred("P1", abs(inf["V"]-0.5) < 1e-7, f"V_inf={inf['V']:.12f}")
for LL, TT in ((8, T8), (16, T16)):
    ex = 0.5*(1-LL**-4.0)
    pred(f"P2(L={LL})", abs(TT["V"]-ex) < 1e-12, f"V={TT['V']:.15f} exact={ex:.15f}")
pred("P3", all(abs(RS[q]-T4[q]) < 1e-10 for q in names) and rank == 3*N-3,
     "max diff %.2e" % max(abs(RS[q]-T4[q]) for q in names))
pred("P4", all(abs(inf[q]-MP[q]) < 2e-3 for q in names), "max diff %.2e" % max(abs(inf[q]-MP[q]) for q in names))
pred("P5", abs(6*inf["V"]-3) < 1e-6, f"6V={6*inf['V']:.10f}")
s2 = 0.5
rng = np.random.default_rng(12345)
th = rng.normal(0, np.sqrt(s2), size=(2_000_000, 3)); Y = (th**2).sum(1)/2
mY, vY = Y.mean(), Y.var(ddof=1)
seM = np.sqrt(0.375/len(Y)); seV = np.sqrt((np.mean((Y-mY)**4)-vY**2)/len(Y))
log(f"(d) Y: analytic mean=0.75 var=0.375 (Y=(s^2/2)chi2_3); MC mean={mY:.6f}+-{seM:.1e} var={vY:.6f}+-{seV:.1e}")
pred("P6", abs(mY-0.75) < 5*seM and abs(vY-0.375) < 5*seV, "")
log("ALL PASS" if not fails else f"FAILED: {fails}")
open(OUT, "w").write("\n".join(out)+"\n")
sys.exit(0 if not fails else 1)
