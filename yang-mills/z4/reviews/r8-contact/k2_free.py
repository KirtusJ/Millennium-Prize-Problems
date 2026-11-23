"""K2 known-answer comparison: A4's contact coefficient against the free lattice theory.

Conversion (derived in notes.md, step 2):
  SU(2), x_p = TrU_p/2 = cos(|theta_p|/2) = 1 - |theta_p|^2/8 + O(theta^4), theta_p^a = g b^2 B^a, beta = 4/g^2.
  beta(1-x_p) = sum_a theta_a^2/(2 g^2) + O(g^2), so A4's O_b = (1/2) b^3 sum_x f(bx) sum_a (B_3^a)^2
  = (1/2) sum_a O_bench_a, three independent free colour copies at leading order.
  Per colour Var(O_bench) b^5 -> c * int f^2 with c = 2 sum_{r in Z^3} G(r)^2, G the dimensionless
  equal-time two-point function of b^2 B_3 (= theta_12/g) at b = 1, infinite volume.
  Hence A4's free total coefficient T = (3/4) c.
  4D isotropic Wilson lattice: Ghat4(q) = int dk0/2pi (q1^2+q2^2)/(khat0^2+qhat^2) = (qh1^2+qh2^2)/(qh sqrt(qh^2+4)).
  Hamiltonian lattice (bench): GhatH(q) = (qh1^2+qh2^2)/(2 qh).
  Free removable part by A4's mask (exact Gaussian conditioning, derived in notes.md):
  per masked x-link, colour, unit weight w (g = 1): E Var(Q_e | ext) = 4 s2 E(thb_p - thb_p')^2 + 8 s2^2,
  s2 = 1/6 (conditional variance: 6 action faces), E(thb_p-thb_p')^2 = 2 G4(0) - 2 G4(e2) - 4 s2.
  Mask average: x- and y-links each included with probability 1/6. Removable coefficient
  R = (3 colours)(1/4 prefactor^2)(2 orientations)(1/6) * K = K/4, K = 4 s2 (1 - 2G4(e2) - 4 s2) + 8 s2^2.
  A4's lower coefficient: 1/18; its radial part 8 s2^2 /4 = 2/36 /4 ... (check P5).

Predicates (fixed before the first run):
 P1 control: G4(0) = 1/2 (exact: sum over the 6 orientations of (khat_mu^2+khat_nu^2)/khat^2 = 3).
    Tolerance 1e-3: midpoint quadrature error at n=96, integrand ~ |q| near 0 (estimate, checked by n=64 vs 96).
 P2 convergence: c4, cH, G4(e2) change by < 1e-3 relative between n=64 and n=96 grids.
 P3 regularization change: c4 < cH (pointwise Ghat4/GhatH = 2/sqrt(qh^2+4) < 1). Report ratio.
 P4 A4 lower coefficient below free total: 1/18 < T = 0.75 c4.
 P5 A4 coefficient equals free radial term: (3/4)(2)(1/6)(8 s2^2)/ (2*... ) i.e. R_radial = 2 s2^2 = 1/18 to 1e-12.
 P6 A4 lower coefficient below free removable: 1/18 <= R = K/4.
 P7 removable below total: R < T.
 Measured only: c4, cH, ratio c4/cH, R/T, (1/18)/R, (1/18)/T.
Results appended to a new file results/k2_<timestamp>.txt (never overwritten). No randomness.
"""
import numpy as np, time, os, sys

def grid(n):
    q = -np.pi + (np.arange(n) + 0.5) * 2 * np.pi / n
    Q1, Q2, Q3 = np.meshgrid(q, q, q, indexing="ij")
    h1, h2, h3 = (2*np.sin(Q1/2))**2, (2*np.sin(Q2/2))**2, (2*np.sin(Q3/2))**2
    return Q2, h1, h2, h3

def compute(n):
    Q2, h1, h2, h3 = grid(n)
    hh = h1 + h2 + h3
    qh = np.sqrt(hh)
    G4 = (h1 + h2) / (qh * np.sqrt(hh + 4))
    GH = (h1 + h2) / (2 * qh)
    return dict(G4_0=G4.mean(), G4_e2=(np.cos(Q2)*G4).mean(), c4=2*(G4**2).mean(),
                cH=2*(GH**2).mean(), GH_0=GH.mean())

# check of the k0 integral formula
k0 = -np.pi + (np.arange(200000)+0.5)*2*np.pi/200000
a = 0.7
num = (1/(4*np.sin(k0/2)**2 + a*a)).mean()
k0err = abs(num - 1/(a*np.sqrt(a*a+4)))

r64, r96 = compute(64), compute(96)
s2 = 1/6
G0, Ge2, c4, cH = r96["G4_0"], r96["G4_e2"], r96["c4"], r96["cH"]
K = 4*s2*(2*G0 - 2*Ge2 - 4*s2) + 8*s2**2
R = K/4
Rrad = 8*s2**2/4
T = 0.75*c4
TH = 0.75*cH
P = {}
P["P1"] = abs(G0 - 0.5) < 1e-3
P["P2"] = all(abs(r96[k]-r64[k]) < 1e-3*abs(r96[k]) for k in ("c4", "cH", "G4_e2"))
P["P3"] = c4 < cH
P["P4"] = 1/18 < T
P["P5"] = abs(Rrad - 1/18) < 1e-12
P["P6"] = 1/18 <= R
P["P7"] = R < T
lines = [f"k0 formula check err {k0err:.2e}",
         f"n=64 {r64}", f"n=96 {r96}",
         f"c4 {c4:.6f} cH {cH:.6f} c4/cH {c4/cH:.4f}",
         f"G4(e2) {Ge2:.6f}  E(thb_p-thb_p')^2 {2*G0-2*Ge2-4*s2:.6f}",
         f"A4 total free coeff T=0.75 c4 = {T:.6f}; Hamiltonian analogue 0.75 cH = {TH:.6f}",
         f"free removable R = {R:.6f} (radial {Rrad:.6f} + transverse {R-Rrad:.6f})",
         f"A4 1/18 = {1/18:.6f};  (1/18)/R = {(1/18)/R:.4f}; (1/18)/T = {(1/18)/T:.4f}; R/T = {R/T:.4f}",
         "predicates " + " ".join(f"{k}={'met' if v else 'FAILED'}" for k, v in P.items())]
os.makedirs("results", exist_ok=True)
fn = f"results/k2_{time.strftime('%Y%m%d_%H%M%S')}.txt"
assert not os.path.exists(fn)
open(fn, "w").write("\n".join(lines) + "\n")
print("\n".join(lines)); print("wrote", fn)
sys.exit(0 if all(P.values()) else 1)
