"""Predicates (fixed before run): on 6001 log-spaced c in [1e-3,50], j=1..4, find max of theta_j/(Gamma(j+.5)c^(-j-.5)+(j/(ec))^j) (constant 1).
Expectation (mine): constant 1 holds numerically (ratio<1) because the sum-vs-integral gap for a two-sided sum is <= 2*(gap), and gap<M typically.
Also probe worst-case ratio of (theta-integral)/M (needs <=2 for constant 2, <=1 for constant 1). Informational; exit 0 always unless constant-2 gap ratio>1+1e-9 (a T2 defect)."""
import math,sys
E=math.e
def th(j,c):
    M=int(math.sqrt(800/c))+50
    return 2*sum(m**(2*j)*math.exp(-c*m*m) for m in range(1,M+1))
worst={}
n=6000
for j in range(1,5):
  for i in range(n+1):
    c=10**(-3+(math.log10(50)+3)*i/n)
    I=math.gamma(j+.5)*c**(-j-.5); Mx=(j/(E*c))**j
    g=(th(j,c)-I)/Mx
    if g>worst.get(j,(-9,0))[0]: worst[j]=(g,c)
print(worst)
sys.exit(1 if any(v[0]>1+1e-9 for v in worst.values()) else 0)
