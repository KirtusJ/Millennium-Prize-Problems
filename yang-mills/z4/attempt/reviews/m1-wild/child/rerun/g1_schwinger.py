"""
G(1) = (2pi)^-4 Int_{[-pi,pi]^4} (a1+a2)/(a0+a1+a2+a3) cos(k0) d^4k,  a=(2 sin(k/2))^2
via Schwinger 1/D = Int_0^inf exp(-tD) dt.  With x=2t, i_v(x)=exp(-x) I_v(x):
  G = (1/2) Int_0^inf dx  4 i1(x) (i0(x)-i1(x)) i0(x)^2.

Predicates (written BEFORE running; failure = result not trusted):
 P1 control.txt already holds 1.000000 (cos integral).
 P2 own i0,i1 match integral definition (1/pi)Int_0^pi e^{x(cos th -1)} cos(v th) dth
    to <1e-12 at x in {0.5,5,19.9,20.1,60} (series/asymptotic switch both sides).
 P3 switch point 15 vs 30 changes G by <1e-10.
 P4 quadrature with panels doubled / GL order changed changes G by <1e-10.
 P5 tail (x>X) analytic leading term 1/(2 pi^2 x^3)*(1/2) integrated, compared with
    numerically integrated tail: agree to relative 1e-2 at X=1e3 (sanity of tail form).
 P6 sanity: replacing cos(k0) factor C by B (i.e. cos->1) gives (a1+a2)/D integral = 1/2
    exactly (by symmetry, <(a1+a2)/D> = 2*(1/4)).
Tolerance: from P3/P4 spreads and tail truncation of asymptotic series; no target value used.
"""
import numpy as np
from math import factorial, pi

def i_series(v, x):
    x = np.asarray(x, float); h = x/2
    s = np.zeros_like(x); term = h**v/factorial(v)
    k = 0
    while True:
        s += term
        k += 1
        term = term*h*h/(k*(k+v))
        if np.all(term < 1e-18*s) : break
    return np.exp(-x)*s

def i_asym(v, x, nterms=30):
    x = np.asarray(x, float)
    s = np.zeros_like(x); a = 1.0; best = None
    mu = 4*v*v
    for k in range(nterms):
        t = a/x**k*(-1)**k
        s += t
        a = a*(mu-(2*k+1)**2)/((k+1)*8)
        if k > 3 and abs(a)/x.min()**(k+1) < 1e-17 : break
    return s/np.sqrt(2*pi*x)

def iv(v, x, sw=20.0):
    x = np.asarray(x, float)
    out = np.empty_like(x)
    m = x <= sw
    if m.any(): out[m] = i_series(v, x[m])
    if (~m).any(): out[~m] = i_asym(v, x[~m])
    return out

def F(x, sw=20.0, cosfac=True):
    i0 = iv(0, x, sw); i1 = iv(1, x, sw)
    return (4*i1 if cosfac else 4*i0)*(i0-i1)*i0**2

def gl(f, a, b, npan, order):
    xs, ws = np.polynomial.legendre.leggauss(order)
    edges = np.linspace(a, b, npan+1); tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        xx = 0.5*(hi-lo)*xs+0.5*(hi+lo)
        tot += 0.5*(hi-lo)*np.sum(ws*f(xx))
    return tot

def G(X=60.0, npan=60, order=24, sw=20.0, cosfac=True):
    f = lambda x: F(x, sw, cosfac)
    body = gl(f, 0.0, X, npan, order)
    # tail x>X: u=1/x, dx = du/u^2
    g = lambda u: f(1.0/u)/u**2
    tail = gl(g, 1e-12, 1.0/X, 8, order)   # integrand ~u, smooth
    return 0.5*(body+tail), 0.5*body, 0.5*tail

if __name__ == "__main__":
    # P1
    assert open('control.txt').read().strip() == '1.000000'
    # P2
    res = {}
    th = np.linspace(0, pi, 1)  # placeholder
    xs, ws = np.polynomial.legendre.leggauss(200)
    def i_int(v, x):
        t = 0.5*pi*(xs+1)
        return 0.5*pi/pi*np.sum(ws*np.exp(x*(np.cos(t)-1))*np.cos(v*t))
    p2 = 0
    for x in [0.5, 5, 19.9, 20.1, 60]:
        for v in (0, 1):
            p2 = max(p2, abs(float(iv(v, np.array([x]))[0]) - i_int(v, x)))
    res['P2 max err'] = p2
    base = G()
    res['G'] = base[0]; res['body'] = base[1]; res['tail'] = base[2]
    res['P3'] = abs(G(sw=15.0)[0]-G(sw=30.0)[0])
    var = [G(npan=120, order=24)[0], G(npan=60, order=40)[0], G(X=120.0, npan=120)[0], G(X=30.0, npan=30)[0]]
    res['P4 spread'] = max(abs(v-base[0]) for v in var)
    # P5: tail of asymptotic form vs numeric at X=1e3
    X = 1e3
    num = 0.5*gl(lambda u: F(1/u)/u**2, 1e-12, 1/X, 8, 24)
    ana = 0.5/(2*pi**2)/(2*X**2)
    res['P5 rel'] = abs(num/ana-1)
    res['P6 cos->1 value'] = G(cosfac=False)[0]
    for k, v in res.items(): print(k, repr(v))
    ok = res['P2 max err'] < 1e-12 and res['P3'] < 1e-10 and res['P4 spread'] < 1e-10 \
         and res['P5 rel'] < 1e-2 and abs(res['P6 cos->1 value']-0.5) < 1e-9
    print('PREDICATES PASS' if ok else 'PREDICATES FAIL')
    with open('result.txt', 'x') as f:
        f.write("G1 = %.10f\nerr_est = %.2e\npredicates = %s\n" % (res['G'], max(res['P3'], res['P4 spread'], 1e-12), 'PASS' if ok else 'FAIL'))
        for k, v in res.items(): f.write("%s = %r\n" % (k, v))
