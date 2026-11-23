"""Flowed free Maxwell benchmark for the corrected S6' (Q3).

Setting. Free continuum Maxwell field, one colour, Hamiltonian vacuum in 3 space
dimensions (Z4's setting, STATEMENT.md), with the flow acting as the heat kernel
e^{-t k^2} on each field (leading-order gradient flow, Luscher 1006.4518 eq.2.11-2.12),
so each two-point function carries e^{-2 t k^2}.  Equal-time vacuum two-point function
of the flowed B_3:
    D_t(r) = int d^3k/(2pi)^3 e^{ik.r} (k1^2+k2^2)/(2|k|) e^{-2 t k^2}
(transverse projector times k/2, the normalization rederived in Z4's round 5).
Observable: O_t(f) = int d^3x f(x) (B_t(x)^2 - <B_t^2>), f(x) = exp(-|x|^2/(2 s^2)).
Wick: Var = 2 int int f f D_t^2 = 2 (pi s^2)^{3/2} int d^3r D_t(r)^2 exp(-r^2/(4 s^2)).
Units: everything in units of t (Var = t^{-1} Phi(s^2/t)).

PREDICATES (fixed before the first run; tolerances and their origin):
 P1  <B_3,t^2> (3D spatial flow) = 1/(48 pi^2 t^2), relative error < 1e-8.
     Exact value: angular mean of projector 2/3, int k^3 e^{-2tk^2} = 1/(8t^2).
     Tolerance: composite Simpson on a grid where the integrand is smooth and
     Gaussian-decaying; error far below 1e-8 expected.
 P2  4D Euclidean flow, Feynman gauge: <F_12,t^2> = 1/(128 pi^2 t^2), relative < 1e-8.
     Known answer: Luscher eq.(2.28) at D=4, leading order, N^2-1 -> 1, divided
     by g0^2, gives <(1/4)F^2> = 3/(128 pi^2 t^2); six equal components F_{mu nu}^2/2
     -> each <F_12^2> = 1/(128 pi^2 t^2).  Same tolerance origin as P1.
 P3  Var(t=1, s) finite and positive for s in {0.5,1,2,4,8,16}; grid-doubling change
     < 1e-6 relative (quadrature convergence criterion).
 P4  Scaling: Var(t/4, s/2) = 4 Var(t, s) for t=1, s=2, relative < 1e-6
     (exact dimensional analysis; tolerance = quadrature).
 P5  sigma -> infinity limit: 2 int d^3r D_t^2 computed in position space equals the
     momentum-space closed form sqrt(pi)/(1280 pi^2) * 2 t^{-5/2}, relative < 1e-6.
 P6  Var / int f^2 * t^{5/2} -> sqrt(pi)/(640 pi^2) as s/sqrt(t) grows: deviation
     decreasing in s and < 2% at s = 16.  (My expectation: correction O(t/s^2)
     with an O(1) coefficient; 1/256 ~ 0.4% times a coefficient up to ~5.)
 Measured only: Phi at each s, the ratio to the asymptotic law, the t -> 0 law at
 fixed s (Var ~ c_flow * int f^2 * t^{-5/2}, the flowed counterpart of S1' b^{-5}).
Result file: results/flow_bench_<run>.txt, never overwritten (exits 3 if it exists).
No randomness (deterministic quadrature), so no seed is needed.
"""
import sys, os, math
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
import numpy as np

PI = math.pi

def simpson(y, x):
    n = len(x) - 1
    assert n % 2 == 0
    h = (x[-1] - x[0]) / n
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())

def simpson_rows(y, x):
    n = y.shape[1] - 1
    h = (x[-1] - x[0]) / n
    return h / 3 * (y[:, 0] + y[:, -1] + 4 * y[:, 1:-1:2].sum(1) + 2 * y[:, 2:-1:2].sum(1))

def j0(x):
    return np.where(x < 1e-4, 1 - x**2 / 6, np.sin(x) / np.where(x == 0, 1, x))

def j1(x):
    xs = np.where(x == 0, 1, x)
    return np.where(x < 1e-3, x / 3 - x**3 / 30, np.sin(xs) / xs**2 - np.cos(xs) / xs)

def GA_C(r, t, nk, chunk=200):
    """Chunked wrapper over r to bound memory."""
    As, Cs = [], []
    for i in range(0, len(r), chunk):
        a, c = _GA_C(r[i:i+chunk], t, nk)
        As.append(a); Cs.append(c)
    return np.concatenate(As), np.concatenate(Cs)

def _GA_C(r, t, nk):
    """G(r)=(1/4pi^2) int k j0(kr) e^{-2tk^2} dk; return A=G''-G'/r, C=G'/r."""
    kmax = 9.0 / math.sqrt(t)
    k = np.linspace(0, kmax, nk + 1)
    w = np.exp(-2 * t * k**2)
    x = np.outer(r, k)
    xs = np.where(x == 0, 1, x)
    J1 = j1(x)
    # j0' = -j1 ; j0'' = -(j0 - 2 j1/x)
    j1_over_x = np.where(x < 1e-3, 1/3 - x**2 / 30, J1 / xs)
    Gp = -(k**2 * w * J1)            # times 1/4pi^2, integrand of G'
    Gpp = -(k**3 * w * (j0(x) - 2 * j1_over_x))
    Gp_over_r = -(k**3 * w * j1_over_x)  # G'/r = int k^3 (-j1(kr)/(kr))
    f = lambda y: simpson_rows(y, k) / (4 * PI**2)
    Gpp_v, Gpr_v = f(Gpp), f(Gp_over_r)
    return Gpp_v - Gpr_v, Gpr_v

def radial_D2(t, s, nr, nk, rmax=None):
    """int d^3r D^2 * weight; D = -(A sin^2 + 2C); angular integral exact."""
    if rmax is None:
        rmax = min(12 * math.sqrt(2) * s, 1e9) if s is not None else 0
        rmax = max(rmax, 0)
    r = np.linspace(0, rmax, nr + 1)
    A, C = GA_C(r, t, nk)
    ang = A**2 * 16 / 15 + 4 * A * C * 4 / 3 + 8 * C**2
    wgt = np.exp(-r**2 / (4 * s**2)) if s is not None else 1.0
    return 2 * PI * simpson(r**2 * ang * wgt, r)

def var(t, s, nr, nk):
    rmax = min(12 * math.sqrt(2) * s, 60 * math.sqrt(t))
    r = np.linspace(0, rmax, nr + 1)
    A, C = GA_C(r, t, nk)
    ang = A**2 * 16 / 15 + 4 * A * C * 4 / 3 + 8 * C**2
    I = 2 * PI * simpson(r**2 * ang * np.exp(-r**2 / (4 * s**2)), r)
    return 2 * (PI * s**2) ** 1.5 * I

def main():
    run = sys.argv[1] if len(sys.argv) > 1 else "run1"
    os.makedirs("results", exist_ok=True)
    out = f"results/flow_bench_{run}.txt"
    if os.path.exists(out):
        print("result file exists, refusing to overwrite", out); sys.exit(3)
    L = []; ok = {}
    t = 1.0
    # P1
    k = np.linspace(0, 12, 40001)
    b2 = simpson((2/3) * (k / 2) * np.exp(-2*t*k**2) * k**2, k) / (2*PI**2)
    ex1 = 1 / (48 * PI**2 * t**2)
    ok["P1"] = abs(b2/ex1 - 1) < 1e-8
    L.append(f"P1 <B3^2>_3Dflow = {b2:.12e} exact {ex1:.12e} rel {b2/ex1-1:.2e} {ok['P1']}")
    # P2: 4D, <F12^2> = int d^4k/(2pi)^4 (k1^2+k2^2)/k^2 e^{-2tk^2}; angular mean 1/2; S^3 area 2pi^2
    f12 = simpson(0.5 * np.exp(-2*t*k**2) * k**3, k) * 2*PI**2 / (2*PI)**4
    ex2 = 1 / (128 * PI**2 * t**2)
    ok["P2"] = abs(f12/ex2 - 1) < 1e-8
    L.append(f"P2 <F12^2>_4Dflow = {f12:.12e} Luscher(2.28) {ex2:.12e} rel {f12/ex2-1:.2e} {ok['P2']}")
    L.append(f"   ratio 3D-spatial-flow/4D-flow <B^2> = {b2/f12:.6f} (= 128/48 = {128/48:.6f})")
    # P5: s -> infinity
    r = np.linspace(0, 40, 4001)
    A, C = GA_C(r, t, 6000)
    ang = A**2*16/15 + 4*A*C*4/3 + 8*C**2
    I_inf = 2 * 2*PI * simpson(r**2 * ang, r)
    ex5 = 2 * math.sqrt(PI) / (1280 * PI**2) * t**-2.5
    ok["P5"] = abs(I_inf/ex5 - 1) < 1e-6
    L.append(f"P5 2*int D^2 d^3r = {I_inf:.12e} closed form {ex5:.12e} rel {I_inf/ex5-1:.2e} {ok['P5']}")
    # P3, P6
    cflow = math.sqrt(PI) / (640 * PI**2)
    devs = []; p3 = True
    for s in [0.5, 1, 2, 4, 8, 16]:
        v1 = var(t, s, 2000, 4000)
        v2 = var(t, s, 4000, 8000)
        conv = abs(v2/v1 - 1)
        p3 &= (v2 > 0) and math.isfinite(v2) and conv < 1e-6
        f2 = (PI * s**2) ** 1.5
        ratio = v2 / f2 * t**2.5 / cflow
        devs.append(abs(ratio - 1))
        L.append(f"   s/sqrt(t)={s:5}: t*Var = {v2*t:.10e}  grid-change {conv:.1e}  Var/(int f^2 c_flow t^-5/2) = {ratio:.6f}")
    ok["P3"] = p3
    L.append(f"P3 finite, positive, converged: {p3}")
    ok["P6"] = all(devs[i+1] < devs[i] for i in range(len(devs)-1)) and devs[-1] < 0.02
    L.append(f"P6 approach to asymptotic law, deviations {['%.4f'%d for d in devs]}: {ok['P6']}")
    # P4
    va = var(1.0, 2.0, 4000, 8000); vb = var(0.25, 1.0, 4000, 8000)
    ok["P4"] = abs(vb/(4*va) - 1) < 1e-6
    L.append(f"P4 Var(1/4,1)/(4 Var(1,2)) - 1 = {vb/(4*va)-1:.2e} {ok['P4']}")
    L.append(f"measured: c_flow = sqrt(pi)/(640 pi^2) = {cflow:.6e}: Var -> c_flow * int f^2 * t^(-5/2) as t->0 at fixed f")
    met = sum(ok.values()); L.append(f"COUNTS met {met}, failed {len(ok)-met}, measured only 3")
    txt = "\n".join(L); print(txt)
    open(out, "w", encoding="utf-8").write(txt + "\n")
    sys.exit(0 if met == len(ok) else 1)

if __name__ == "__main__":
    main()
