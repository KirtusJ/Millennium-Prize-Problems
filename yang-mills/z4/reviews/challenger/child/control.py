"""Control: integral over SU(2) (normalized Haar) of chi_{1/2}(U)^2 = 1.
Class-angle reduction: density (2/pi) sin^2(theta) on [0,pi], tr U = 2 cos theta.
Quadrature: mpmath.quad (tanh-sinh), mp.dps = 50.
PREDICATE C1: |I - 1| < 1e-12  -> exit 0, else exit 1.
Writes control.txt only if it does not already exist (else control_<n>.txt).
"""
import os, sys
from mpmath import mp, quad, sin, cos, pi
mp.dps = 50
I = quad(lambda t: (2/pi)*sin(t)**2*(2*cos(t))**2, [0, pi])
name = "control.txt"; k = 1
while os.path.exists(name):
    name = "control_%d.txt" % k; k += 1
with open(name, "w") as f:
    f.write(mp.nstr(I, 40) + "\n")
err = abs(I - 1)
print("control integral =", mp.nstr(I, 40), " |I-1| =", mp.nstr(err, 5), " file:", name)
sys.exit(0 if err < 1e-12 else 1)
