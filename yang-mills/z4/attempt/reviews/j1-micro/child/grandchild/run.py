"""T112. Predicate (fixed before first run): claim 2.6828 is REPRODUCED iff
|d_400 - 2.6828| <= 0.5e-4 AND |d_400 - d_200| < 1e-8 (converged), where
d = int_0^pi da/sqrt(2*eps(a)), eps = 2*asinh(sin a), via a = pi*sin^2(t/2),
da=(pi/2) sin t dt, t in [0,pi], fixed-node Gauss-Legendre (own implementation).
Control: int_0^pi sin = 2. Rerun: python3 run.py  (files opened with mode 'x').
"""
import numpy as np, json

def gl(n):
    x = np.cos(np.pi*(np.arange(1, n+1)-0.25)/(n+0.5))
    for _ in range(100):
        p0 = np.ones(n); p1 = x.copy()
        for k in range(2, n+1):
            p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
        dp = n*(x*p1-p0)/(x*x-1)
        dx = p1/dp; x = x-dx
        if np.max(abs(dx)) < 1e-16: break
    p0 = np.ones(n); p1 = x.copy()
    for k in range(2, n+1):
        p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
    dp = n*(x*p1-p0)/(x*x-1)
    return x, 2/((1-x*x)*dp*dp)

def integ(f, A, B, n):
    x, w = gl(n)
    return (B-A)/2*np.sum(w*f((B-A)/2*x+(A+B)/2))

with open('control.txt', 'x') as f:
    f.write("%.6f\n" % integ(np.sin, 0, np.pi, 40))

def integrand_t(t):
    a = np.pi*np.sin(t/2)**2
    b = np.pi*np.cos(t/2)**2          # pi - a, accurate near a=pi
    s = np.where(t < np.pi/2, np.sin(a), np.sin(b))
    return 1/np.sqrt(4*np.arcsinh(s)) * (np.pi/2)*np.sin(t)

res = {n: integ(integrand_t, 0, np.pi, n) for n in (100, 200, 400)}
# arccosh-form comparison at moderate points
a = np.linspace(0.3, 2.8, 7)
e1 = 2*np.arcsinh(np.sin(a)); e2 = np.arccosh(1+2*np.sin(a)**2)
cmp_ = float(np.max(abs(e1-e2)))
d = res[400]
ok = abs(d-2.6828) <= 0.5e-4 and abs(res[400]-res[200]) < 1e-8
out = {"d": {str(k): float("%.12f" % v) for k, v in res.items()},
       "d_10digits": "%.10f" % d, "diff_400_200": res[400]-res[200],
       "arccosh_vs_asinh_max_diff_moderate": cmp_,
       "claimed": 2.6828, "reproduced": bool(ok)}
with open('result.json', 'x') as f: json.dump(out, f, indent=1)
with open('notes.md', 'x') as f:
    f.write("# T112\nSubstitution a=pi sin^2(t/2). d(100,200,400)=%s\nd=%.10f reproduced=%s\narccosh vs 2asinh max diff at a in [0.3,2.8]: %.2e\nRerun: cd /home/user/z4-workers/j1-micro/child/grandchild && rm -f control.txt result.json notes.md && python3 run.py\n" % (res, d, ok, cmp_))
print(open('control.txt').read(), json.dumps(out, indent=1))
