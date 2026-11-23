"""Informational (outside requested j<=4): max (theta_j-I)/M for j=5,8,12,20,30 over 1500 log c in [0.05,50]. Constant 1 needs <=1; constant 2 needs <=2.
Exit 1 only if constant-2 ratio>2 (would be a T2 defect)."""
import math,sys
E=math.e;out={};bad=0
for j in (5,8,12,20,30):
  w=(-9,0)
  for i in range(1501):
    c=10**(-1.3+(math.log10(50)+1.3)*i/1500)
    M=int(math.sqrt(800/c))+50
    t=2*sum(m**(2*j)*math.exp(-c*m*m) for m in range(1,M+1))
    I=math.gamma(j+.5)*c**(-j-.5); Mx=(j/(E*c))**j
    g=(t-I)/Mx
    if g>w[0]: w=(g,c)
  out[j]=w; bad|= w[0]>2
print(out); sys.exit(bad)
