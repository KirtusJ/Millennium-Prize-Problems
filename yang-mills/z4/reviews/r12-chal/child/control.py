"""Predicate: sum_{m in Z} exp(-pi m^2) printed to 6 decimals equals 1.086435 (known pi^(1/4)/Gamma(3/4)=1.0864348112).
Tolerance: terms beyond |m|=10 are < e^-314, so truncation is exact in float64. Exit 0 iff match."""
import math,sys
s=sum(math.exp(-math.pi*m*m) for m in range(-10,11))
k=math.pi**0.25/math.gamma(0.75)
with open("control.txt","x") as f: f.write("%.6f\n"%s)
print(s,k)
sys.exit(0 if "%.6f"%s=="1.086435" and abs(s-k)<1e-14 else 1)
