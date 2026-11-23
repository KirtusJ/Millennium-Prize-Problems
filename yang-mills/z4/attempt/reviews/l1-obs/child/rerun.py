"""Rerun of grandchild result with parent code (q.py). Predicate: E == 2acosh(1+2sin^2(pi/max(N1,N2))) to 1e-8 for (5,2,3),(2,5,3),(3,2,5); and grandchild E,W agree to 1e-8."""
from q import *
for N,(E0,W0) in {(5,2,3):(2.23329063,0.00171185),(2,5,3):(2.23329063,0.00171185),(3,2,5):(3.13359847,0.00285714)}.items():
    G,s=modes(N);E,mu,v=first(G)
    Ecl=2*math.acosh(1+2*math.sin(math.pi/max(N[0],N[1]))**2)
    print(N,"E=%.8f mu=%.8f cf=%.8f"%(E,mu,Ecl),"cf_ok",abs(E-Ecl)<1e-8,"agree_gc",abs(E-E0)<1e-8 and abs(mu-W0)<1e-8)
