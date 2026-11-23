"""twopoint_check.py -- check the derived Euclidean two-point function against
direct numerical evaluation of the mode-expansion momentum integral.

Derived (notes.md):  G(x,t) = <B_3(x) e^{-tH} B_3(0)> = (t^2 + x3^2 - x1^2 - x2^2) / (pi^2 (r^2+t^2)^3)
Mode integral:       G(x,t) = Int d^3k/((2pi)^3 2k) (k^2 - k3^2) exp(i k.x - k t)
 - x along e3 (dist z):  G = 1/(8 pi^2) Int_0^inf dk k^3 e^{-kt} Int_{-1}^{1} dc (1-c^2) cos(k z c)
 - x along e1 (dist a):  G = 1/(8 pi^2) Int_0^inf dk k^3 e^{-kt} Int_{-1}^{1} dc (1-c^2) J0(k a sqrt(1-c^2))
   (azimuthal integral done via Int_0^{2pi} e^{i s cos phi} dphi = 2 pi J0(s)).

PREDICATE P_2pt (fixed before first run): at the 6 test points below, the relative
difference |G_num - G_formula| / |G_formula| < 1e-8 at every point.
Tolerance source: mpmath quad at dps=25 on smooth, exponentially damped integrands
typically gives >=15 correct digits; 1e-8 leaves a large margin for the 2D nesting,
yet is far below any normalization error (factors of 2, pi), which would be O(1).
Exit code 0 iff P_2pt passes, else 1. No randomness.
"""
import sys
import mpmath as mp

mp.mp.dps = 25

def G_formula(x1, x2, x3, t):
    r2 = x1*x1 + x2*x2 + x3*x3
    return (t*t + x3*x3 - x1*x1 - x2*x2) / (mp.pi**2 * (r2 + t*t)**3)

def G_axis3(z, t):
    inner = lambda k: mp.quad(lambda c: (1 - c*c) * mp.cos(k*z*c), [-1, 0, 1])
    return mp.quad(lambda k: k**3 * mp.exp(-k*t) * inner(k), [0, 2, 8, 30, mp.inf]) / (8*mp.pi**2)

def G_axis1(a, t):
    inner = lambda k: mp.quad(lambda c: (1 - c*c) * mp.besselj(0, k*a*mp.sqrt(1 - c*c)), [-1, 0, 1])
    return mp.quad(lambda k: k**3 * mp.exp(-k*t) * inner(k), [0, 2, 8, 30, mp.inf]) / (8*mp.pi**2)

tests = [("e3", 0.0, 1.0), ("e3", 0.7, 1.0), ("e3", 2.0, 0.5),
         ("e1", 0.7, 1.0), ("e1", 2.0, 1.5), ("e1", 0.4, 0.8)]
ok = True
for ax, d, t in tests:
    d = mp.mpf(d); t = mp.mpf(t)
    if ax == "e3":
        num = G_axis3(d, t); fo = G_formula(0, 0, d, t)
    else:
        num = G_axis1(d, t); fo = G_formula(d, 0, 0, t)
    rel = abs(num - fo) / abs(fo)
    ok &= rel < 1e-8
    print(f"{ax} d={float(d):.2f} t={float(t):.2f}  G_num={mp.nstr(num,15)}  G_formula={mp.nstr(fo,15)}  rel={mp.nstr(rel,3)}")
print("P_2pt:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
