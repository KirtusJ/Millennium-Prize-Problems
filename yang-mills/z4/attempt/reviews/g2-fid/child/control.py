"""Control: I_1(1) to 9 decimals via exact series sum_k (1/2)^(2k+1)/(k!(k+1)!). Predicate: value rounds to 0.565159104 (known answer)."""
from fractions import Fraction as F
from math import factorial as f
s=sum(F(1,2**(2*k+1))/(f(k)*f(k+1)) for k in range(30))
v="%.9f"%float(s)
open("control.txt","x").write(v+"\n"); print(v)
