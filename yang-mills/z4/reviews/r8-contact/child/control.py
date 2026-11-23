"""Control: G4(0) = 1/2 exactly, and the analytic k4 integral.

Claim: G4(0) = int d^4k/(2pi)^4 (kh1^2+kh2^2)/(kh1^2+..+kh4^2).
The BZ^4 and the measure are invariant under permutations of the 4 axes, so
I_mu = int kh_mu^2/kh^2 is the same for every mu, and sum_mu I_mu = int 1 = 1.
Hence I_mu = 1/4 and G4(0) = I_1 + I_2 = 1/2 exactly.

Analytic k4 integral (A = 3D khat^2 > 0):
  int dk4/(2pi) 1/(A + 2 - 2 cos k4) = 1/sqrt((A+2)^2 - 4) = 1/sqrt(A(A+4)).
So Ghat4(q) = (kh1^2+kh2^2)/sqrt(A(A+4)).

PREDICATES (fixed before first run):
 P1 4D midpoint grid n=32 (permutation-symmetric grid, so the symmetry argument
    holds exactly on the grid): |G4(0) - 0.5| < 1e-12 (origin: float64 rounding of
    ~1e6-term sum).
 P2 3D reduced form with analytic k4, midpoint grid n=256: |G4(0)-0.5| < 1e-3
    (origin: midpoint quadrature error of a bounded integrand with a direction-
    dependent value at q=0; expected O(n^-3) ~ 1e-6, tolerance generous).
 P3 analytic k4 formula vs 4096-point periodic trapezoid for A in
    {1e-2,0.1,1,5,12}: relative error < 1e-10 (origin: trapezoid on a periodic
    analytic function converges exponentially; for A=1e-2 the pole distance is
    ~0.1 so 4096 points gives error ~exp(-400)).
No randomness. Writes control_result_<timestamp>.txt (never overwrites).
"""
import numpy as np, os, time, sys

ok = True
def pred(name, cond, msg):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ": " + msg)
    ok &= bool(cond)

def mid(n):
    return -np.pi + (np.arange(n) + 0.5) * 2 * np.pi / n

# P1
n = 32
kh2 = 4 * np.sin(mid(n) / 2) ** 2
a, b, c, d = np.meshgrid(kh2, kh2, kh2, kh2, indexing="ij", sparse=True)
g0_4d = ((a + b) / (a + b + c + d)).mean()
pred("P1", abs(g0_4d - 0.5) < 1e-12, f"4D grid n=32 G4(0)={g0_4d:.15f}")

# P2
n = 256
kh2 = 4 * np.sin(mid(n) / 2) ** 2
s = 0.0
for i in range(n):
    A = kh2[i] + kh2[:, None] + kh2[None, :]
    N = kh2[i] + kh2[:, None]
    s += (N / np.sqrt(A * (A + 4))).sum()
g0_3d = s / n**3
pred("P2", abs(g0_3d - 0.5) < 1e-3, f"3D reduced n=256 G4(0)={g0_3d:.10f}")

# P3
k = np.arange(4096) * 2 * np.pi / 4096
errs = []
for A in [1e-2, 0.1, 1.0, 5.0, 12.0]:
    num = (1.0 / (A + 4 * np.sin(k / 2) ** 2)).mean()
    ana = 1 / np.sqrt(A * (A + 4))
    errs.append(abs(num / ana - 1))
pred("P3", max(errs) < 1e-10, f"max rel err k4 formula = {max(errs):.2e}")

fn = f"control_result_{time.strftime('%Y%m%d_%H%M%S')}.txt"
assert not os.path.exists(fn)
with open(fn, "x") as f:
    f.write(f"G4(0) 4D n=32: {g0_4d:.15f}\nG4(0) 3D n=256: {g0_3d:.12f}\nk4 max rel err: {max(errs):.3e}\nall_pass: {ok}\n")
print("wrote", fn)
sys.exit(0 if ok else 1)
