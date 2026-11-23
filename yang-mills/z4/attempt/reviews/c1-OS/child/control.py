"""control: G_1(0), Z^4, mass 1. Predicate: methods A (Schwinger/Bessel) and B (k4 analytic + 3D grid) agree to 1e-8 abs
(both are exponentially convergent quadratures); write 6 decimals to control.txt (mode x)."""
import sys; sys.path.insert(0,'.')
from lib import *
a=GA((0,0,0,0),1.0); b=GB((0,0,0,0),1.0,N=64)
print(a,b)
assert abs(a-b)<1e-8, "methods disagree"
open('control.txt','x').write("%.6f\n"%a)
