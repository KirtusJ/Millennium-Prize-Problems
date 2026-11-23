"""Step 1: claimed z(L) = -L^2 ln a, beta=2.3, L=1..8, U(1) a=I1/I0, SU(2) a=I2/I1.
I_n(x) by trapezoid quadrature of (1/pi) int_0^pi exp(x cos t) cos(n t) dt (periodic integrand -> spectral accuracy).
Predicates (fixed before running):
 T1: 0<a<1 for both groups (else ln a not negative).
 T2: z(L) strictly increasing in L for L=1..8, both groups (tolerance: none, exact arithmetic on floats).
 T3: z(L)/L^2 constant (= -ln a) to 1e-12 (tests the 'z ~ L^2' reading; tolerance = float roundoff).
Note 'unbounded' cannot be shown by 8 points; only the closed form -L^2 ln a with a<1 implies it (analytic, not tested).
Output file written with mode 'x'.
"""
import numpy as np
t=np.linspace(0,np.pi,400001)
def I(n,x): return np.trapezoid(np.exp(x*np.cos(t))*np.cos(n*t),t)/np.pi
b=2.3
a={'U(1)':I(1,b)/I(0,b),'SU(2)':I(2,b)/I(1,b)}
out=[]
res={}
for g,av in a.items():
    out.append(f"{g}: a={av:.10f}  sigma=-ln a={-np.log(av):.10f}")
    z=[-L*L*np.log(av) for L in range(1,9)]
    for L,zz in enumerate(z,1): out.append(f"  L={L} m_L={-L*np.log(av):.8f} z={zz:.8f}")
    res[g]=(0<av<1, all(np.diff(z)>0), max(abs(np.array(z)/np.arange(1,9)**2+np.log(av)))<1e-12)
    out.append(f"  predicates T1,T2,T3 = {res[g]}")
s="\n".join(out); print(s)
with open("table.txt","x") as f: f.write(s+"\n")
