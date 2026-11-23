"""
Predicates (fixed before running):
P1: control (int_0^pi sin^2) formatted to 6 decimals == 1.570796
P2: two independent methods agree within 1e-7
P3: |value - 4.6054132| < 5e-7
c* = int_0^pi sqrt(2*eps(a)) da, eps(a)=2*asinh(sin a); integrand = 2*sqrt(asinh(sin a)).
Symmetry a<->pi-a => c* = 2*int_0^{pi/2}.
Method A: a=u^2 on [0,pi/2], single GL rule n=200,400 (smooth in u).
Method B: a=(pi/2)t^4, t in [0,1], composite GL, 10 panels x (20,40) nodes.
Method C (no symmetry, full range, a=u^2 / a=pi-v^2 halves) cross-check.
"""
import numpy as np
f = lambda a: 2*np.sqrt(np.arcsinh(np.sin(a)))
def gl(g, lo, hi, n):
    x, w = np.polynomial.legendre.leggauss(n)
    return (hi-lo)/2*np.sum(w*g((hi-lo)/2*x+(hi+lo)/2))
# control
ctrl = "%.6f" % gl(lambda x: np.sin(x)**2, 0, np.pi, 50)
with open('control.txt','x') as fh: fh.write(ctrl+"\n")
P1 = ctrl == "1.570796"
h = np.pi/2
A = lambda n: 2*gl(lambda u: f(u*u)*2*u, 0, np.sqrt(h), n)
def B(m):
    g = lambda t: f(h*t**4)*h*4*t**3
    e = np.linspace(0,1,11)
    return 2*sum(gl(g,e[i],e[i+1],m) for i in range(10))
def C(n):  # full range, no symmetry
    s = np.sqrt(h)
    left = gl(lambda u: f(u*u)*2*u, 0, s, n)
    right = gl(lambda v: f(np.pi-v*v)*2*v, 0, s, n)
    return left+right
A200,A400,B20,B40,C200 = A(200),A(400),B(20),B(40),C(200)
val = (A400+B40)/2
P2 = abs(A400-B40) < 1e-7
P3 = abs(val-4.6054132) < 5e-7
d = 1e-8
out = [f"control={ctrl}",
 f"A n=200: {A200:.12f}", f"A n=400: {A400:.12f}",
 f"B 10x20: {B20:.12f}", f"B 10x40: {B40:.12f}", f"C full-range n=200: {C200:.12f}",
 f"|A400-B40|={abs(A400-B40):.2e}  |A200-A400|={abs(A200-A400):.2e}  |B20-B40|={abs(B20-B40):.2e}",
 f"value={val:.9f}  diff from claimed 4.6054132 = {val-4.6054132:.3e}",
 f"boundary: f({d})={f(d):.6e} vs 2*sqrt(d)={2*np.sqrt(d):.6e}; f(pi-d)={f(np.pi-d):.6e}",
 f"symmetry: f(0.3)={f(0.3):.12f} f(pi-0.3)={f(np.pi-0.3):.12f}",
 f"P1={'PASS' if P1 else 'FAIL'} P2={'PASS' if P2 else 'FAIL'} P3={'PASS' if P3 else 'FAIL'}"]
txt="\n".join(out)+"\n"; print(txt)
with open('result.txt','x') as fh: fh.write(txt)
