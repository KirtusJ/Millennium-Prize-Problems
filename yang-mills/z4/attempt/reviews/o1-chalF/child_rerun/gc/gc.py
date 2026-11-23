"""B(0), beta=64, s=0.3 via 2-D quadrature (no Bessel library).
Predicates (fixed before first run):
 P1: control int_0^1 x^2 dx equals 1/3 within 1e-6, written as 0.333333.
 P2: B(0) changes by < 1e-9 relative between the two finest (nu,nt) resolutions.
 P3: all exponents <= 0 (no overflow), results finite.
Method: I_n(b) = e^b/pi * int_0^pi exp(b(cos t -1)) cos^n t dt (midpoint in t);
B = b*A/D, A = int_0^1 u du (1/pi) int exp(b(sqrt(1-u^2)-1) + b(cos t-1)... ) ; scale e^b cancels exactly.
Here A uses I0(b sqrt(1-u^2)) = e^{b R}/pi int exp(bR(cos t-1)) dt, so
A*e^{-b} = int u exp(b(R-1) - b c u^2) [ (1/pi) int exp(bR(cos t-1)) dt ] du ; D*e^{-b} = (1/pi) int exp(b(cos t-1)) cos t dt.
"""
import numpy as np
# control
x, w = np.polynomial.legendre.leggauss(8); x = (x+1)/2; w = w/2
with open('control.txt', 'x') as f: f.write("%.6f\n" % np.sum(w*x**2))
beta, s = 64.0, 0.3
alpha = 2*s*np.sqrt(1+s*s); c = s*s+alpha/2
def B0(nu, nt):
    x, w = np.polynomial.legendre.leggauss(nu); u = (x+1)/2; w = w/2
    t = (np.arange(nt)+0.5)*np.pi/nt
    R = np.sqrt(1-u*u)
    E = beta*R[:,None]*(np.cos(t)[None,:]-1)
    assert E.max() <= 0
    inner = np.exp(E).sum(1)/nt
    A = np.sum(w*u*np.exp(beta*(R-1)-beta*c*u*u)*inner)
    D = np.sum(np.exp(beta*(np.cos(t)-1))*np.cos(t))/nt
    return beta*A/D
res = [(nu, nt, B0(nu, nt)) for nu, nt in [(100,400),(200,800),(400,1600),(800,3200)]]
lines = []
for i, (nu, nt, v) in enumerate(res):
    d = abs(v-res[i-1][2])/abs(v) if i else float('nan')
    lines.append("nu=%d nt=%d B0=%.14f rel_diff_prev=%.3e" % (nu, nt, v, d))
p2 = abs(res[-1][2]-res[-2][2])/abs(res[-1][2]) < 1e-9
lines.append("P1 control pass: %s" % (open('control.txt').read().strip()=="0.333333"))
lines.append("P2 convergence pass: %s" % p2)
lines.append("B(0)=%.10f" % res[-1][2])
with open('result.txt', 'x') as f: f.write("\n".join(lines)+"\n")
print("\n".join(lines))
