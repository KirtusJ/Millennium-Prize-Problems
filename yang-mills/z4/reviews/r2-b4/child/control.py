"""Control: SU(2) Haar integral of chi_1(U)^4 by midpoint quadrature over theta in [0,pi]
with Haar weight (2/pi) sin^2 theta, chi_n(theta) = sin((n+1)theta)/sin(theta).
Predicate (fixed before running): |I - 2| <= 1e-12.  Exit 0 iff it holds.
"""
import math, os, sys

def chi(n, t):
    return math.sin((n + 1) * t) / math.sin(t)

K = 2000
h = math.pi / K
I = sum((2 / math.pi) * math.sin(t) ** 2 * chi(1, t) ** 4 * h
        for t in ((k + 0.5) * h for k in range(K)))
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "control.txt"), "w") as f:
    f.write("%.12f\n" % I)
print("Haar integral of chi_1^4 = %.15f" % I)
sys.exit(0 if abs(I - 2) <= 1e-12 else 1)
