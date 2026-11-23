"""Control: c(0) by 3D midpoint quadrature (quad.py). Predicate C0: |c(0)-0.5| < 1e-4 and
mesh agreement N=96 vs N=144 < 1e-4 (tolerance: expected error from |q| cusp at q=0, O(N^-4) for midpoint,
checked empirically by two meshes). Writes control.txt (mode x)."""
from quad import cvals
a=cvals(96,1)[0]; b=cvals(144,1)[0]
print(a,b)
with open("control.txt","x") as f: f.write("%.6f\n"%b)
ok = abs(b-0.5)<1e-4 and abs(a-b)<1e-4
print("C0 met" if ok else "C0 FAILED")
