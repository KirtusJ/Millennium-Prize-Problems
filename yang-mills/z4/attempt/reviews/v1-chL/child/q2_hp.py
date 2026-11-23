"""Q2b high precision (Decimal, 60 digits): predicate fixed before run: max rel err of (h-2)(1+2S^2h)-h over S in {1e-6..1e6 logspace 25 pts} < 1e-40."""
from decimal import Decimal as D, getcontext
getcontext().prec=60
worst=D(0)
for i in range(25):
    S=D(10)**(D(-6)+D(12)*i/24)
    h=1+(1+S*S).sqrt()/S
    worst=max(worst,abs((h-2)*(1+2*S*S*h)-h)/h)
r=f"worst rel err {worst:.3e} pass {worst<D('1e-40')}"
print(r)
open('q2_hp_result.txt','x').write(r+'\n')
