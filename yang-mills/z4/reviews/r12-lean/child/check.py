"""Numerical check of F1..F6, 1e5 random points each, seed 20240607.
Predicates (fixed before first run):
 F1 hyp: y>=0.            claim: y - y^3/6 <= sin y.
 F2 hyp: y real (all).    claim: |sin y - y| <= |y|^3/6.
 F3 hyp: b>0,k real.      claim: |(2/b) sin(kb/2) - k| <= b^2|k|^3/24.
 F4a hyp: |y|<=pi/2.      claim: (2/pi)|y| <= |sin y| <= |y|.
 F4b hyp: b>0,|kb|<=pi.   claim: (2/pi)|k| <= |(2/b)sin(kb/2)| <= |k|.
 F5 hyp: c>0, M>=1 int.   claim: sum_{m<=M} exp(-c m^2) <= sqrt(pi/c)/2.
 F6 hyp: x>=0,j>=1,c>0.   claim: x^(2j) exp(-c x^2) <= (j/(ec))^j (compared in log domain).
Sampling: y mix of U[-30,30], log-uniform magnitude 1e-6..1 (random sign), and for F1 sign forced >=0 for qualifying
and negative y included to count non-qualifying. Cases violating hypotheses are counted, not tested.
Tolerance: eps=2^-52 (float64 unit roundoff ~1.1e-16 per op). Claim "lhs<=rhs" passes if lhs-rhs <= TOL*eps*(|lhs|+|rhs|+extra)
 where extra = magnitude of operands cancelled (|y| for F1/F2, |k| for F3), TOL=8 (a handful of ops each <=1ulp
 plus libm sin error <=1ulp). F5: TOL scaled by n terms summed (naive accumulation error <= n*eps*sum). F6: log domain,
 error in log of magnitude ~ eps*(|2j ln x|+c x^2+|j(ln j-1-ln c)|), TOL=8.
Relative slack = (rhs-lhs)/rhs-ish: (rhs-lhs)/max(|rhs|,|lhs|) (min over qualifying; negative within tol = rounding noise).
Result file opened mode 'x'.
"""
import numpy as np, math, sys
eps = 2.0**-52
TOL = 8
rng = np.random.default_rng(20240607)
N = 10**5
out = open(sys.argv[1], "x")
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s+"\n")

def mix(n, lo=-30, hi=30):
    u = rng.uniform(lo, hi, n)
    m = 10**rng.uniform(-6, 0, n) * rng.choice([-1, 1], n)
    return np.where(rng.random(n) < 0.5, u, m)

def report(name, hyp, lhs, rhs, extra):
    h = hyp
    d = (lhs - rhs)[h]
    tol = TOL*eps*(np.abs(lhs)+np.abs(rhs)+extra)[h]
    fail = d > tol
    rel = ((rhs-lhs)/np.maximum(np.maximum(np.abs(rhs), np.abs(lhs)), 1e-300))[h]
    slack_tol = ((rhs-lhs)[h]/tol)
    P(f"{name}: sampled={len(hyp)} qualifying={int(h.sum())} fails={int(fail.sum())} "
      f"min_rel_slack={rel.min():.3e} min_slack_in_tol_units={slack_tol.min():.3g} "
      f"(min rel slack among rhs>1e-8*extra: {rel[(np.abs(rhs[h])>1e-8*extra[h])].min():.3e})")
    if fail.any():
        i = np.where(fail)[0][:3]; P("  first fails idx", i, "d", d[i], "tol", tol[i])

# F1: include negatives (non-qualifying)
y = mix(N)
report("F1", y >= 0, y - y**3/6, np.sin(y), np.abs(y))
# F2
y = mix(N)
report("F2", np.ones(N, bool), np.abs(np.sin(y)-y), np.abs(y)**3/6, np.abs(y))
# F3
b = 10**rng.uniform(-3, 1.5, N); k = mix(N, -50, 50)
b = np.where(rng.random(N) < 0.1, -b, b)  # 10% non-qualifying b<0
report("F3", b > 0, np.abs((2/b)*np.sin(k*b/2)-k), b**2*np.abs(k)**3/24, np.abs(k))
# F4a
y = mix(N, -3, 3)
q = np.abs(y) <= np.pi/2
lo = 2/np.pi*np.abs(y); mid = np.abs(np.sin(y)); hi = np.abs(y)
report("F4a-lower", q, lo, mid, np.abs(y)); report("F4a-upper", q, mid, hi, np.abs(y))
# F4b
b = 10**rng.uniform(-3, 1, N); k = mix(N, -5, 5)
q = (np.abs(k*b) <= np.pi)
mid = np.abs((2/b)*np.sin(k*b/2)); ak = np.abs(k)
report("F4b-lower", q, 2/np.pi*ak, mid, ak); report("F4b-upper", q, mid, ak, ak)
# F5
c = 10**rng.uniform(-2, 1, N); M = np.floor(10**rng.uniform(0, 3.5, N)).astype(int)
M[rng.random(N) < 0.02] = 0   # non-qualifying
lhs = np.zeros(N); nn = np.zeros(N)
for i in range(N):
    if M[i] < 1: continue
    cut = min(M[i], int(math.sqrt(745/c[i]))+1)  # later terms underflow to 0 / below 1e-300
    m = np.arange(1, cut+1, dtype=float)
    lhs[i] = math.fsum(np.exp(-c[i]*m*m)); nn[i] = cut
rhs = np.sqrt(np.pi/c)/2
# fsum is exact-sum of rounded terms, so error ~ per-term exp error (few eps) -> relative; use extra = 0, TOL 8 fine, but state n-scaling:
report("F5", M >= 1, lhs, rhs, np.zeros(N))
# F6
j = rng.integers(1, 61, N); c = 10**rng.uniform(-2, 2, N)
t = 10**rng.uniform(-3, 1, N); t[:1000] = 1.0   # t = c x^2/j ; 1000 pts exactly at equality point
x2 = j*t/c; x = np.sqrt(x2)
x = np.where(rng.random(N) < 0.02, -x, x)  # non-qualifying
ll = 2*j*np.log(np.abs(x)) - c*x*x
lr = j*(np.log(j)-1-np.log(c))
ext = np.abs(2*j*np.log(np.abs(x)))+c*x*x+np.abs(lr)
d = ll-lr; h = x >= 0
tol = TOL*eps*ext
fail = (d > tol)[h]
P(f"F6: sampled={N} qualifying={int(h.sum())} fails={int(fail.sum())} min_rel_slack={(-np.expm1(d))[h].min():.3e} "
  f"min_slack_in_tol_units={((-d)/tol)[h].min():.3g} ; equality pts (t=1) max|d|={np.abs(d[:1000][h[:1000]]).max():.3e}")
out.close()
