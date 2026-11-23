"""tail2d_recheck.py -- challenger a5-chalB, independent recheck of the child's 2D S3a test.

2D SU(2), infinite volume, free b.c.: plaquette class angles i.i.d. with density
prop. to sin^2(a) e^{beta cos a} on [0, pi].  O = beta(1 - cos a).  Substituting
u = O: cos a = 1 - u/beta, sin^2 a da = sqrt(1-c^2) dc, so the density of O is
  prop. to sqrt(u(2 - u/beta)/beta) e^{-u}  on [0, 2 beta]  (exact).
P(O > t) by composite Simpson in s = sqrt(u) (removes the sqrt endpoint singularity),
200001 nodes.

PREDICATES (fixed before the first run):
 T1 control: mean of O equals beta(1 - I2(beta)/I1(beta)); Bessel I_n by its integral
    (1/pi) int_0^pi e^{beta cos x} cos(n x) dx, Simpson 200001 nodes; |diff| <= 1e-6
    (quadrature of analytic periodic integrands: error far below 1e-6).
 T2 for all beta in {2,4,8,16,32,64,128,256} and t in 0..min(40, 2beta) step 0.25:
    P(O>t) <= C e^{-t/8} with C = 1 (per-case count reported).  My expectation: the
    density of O is dominated by the Gamma(3/2) density times (2)^{1/2}, tails e^{-t}.
 T3 child's number: |P_8(O>4) - 0.03988840| <= 1e-6 (child grandchild Gauss-Legendre value).
 T4 convergence to the Gamma(3/2,1) tail: D(beta) = max_t<=20 |P_beta - Q| decreasing in beta.
"""
import numpy as np, math, sys, json

def simpson(y, x):
    h = (x[-1]-x[0])/(len(x)-1)
    return h/3*(y[0] + y[-1] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum())

def tail(beta, t, N=200001):
    smax = math.sqrt(2*beta)
    def mass(s0):
        s = np.linspace(s0, smax, N); u = s*s
        f = np.sqrt(np.maximum(u*(2 - u/beta), 0)) * np.exp(-u) * 2*s  # du = 2 s ds
        return simpson(f, s)
    return mass(math.sqrt(t))/mass(0.0) if t < 2*beta else 0.0

def meanO(beta, N=200001):
    s = np.linspace(0, math.sqrt(2*beta), N); u = s*s
    f = np.sqrt(np.maximum(u*(2-u/beta), 0))*np.exp(-u)*2*s
    return simpson(f*u, s)/simpson(f, s)

def bessel_ratio(beta, N=200001):
    x = np.linspace(0, math.pi, N); w = np.exp(beta*(np.cos(x)-1))
    return simpson(w*np.cos(2*x), x)/simpson(w*np.cos(x), x)

def Q(t):
    return math.erfc(math.sqrt(t)) + 2*math.sqrt(t/math.pi)*math.exp(-t)

def main(out):
    betas = [2, 4, 8, 16, 32, 64, 128, 256]
    res = {"cases": []}; t1 = True; n_ok = 0; n_all = 0; worst = 0.0; D = []
    for b in betas:
        m = meanO(b); ex = b*(1 - bessel_ratio(b)); t1 &= abs(m - ex) <= 1e-6
        ts = np.arange(0, min(40, 2*b) + 1e-9, 0.25); dmax = 0.0
        for t in ts:
            p = tail(b, t); n_all += 1; val = p*math.exp(t/8); worst = max(worst, val)
            n_ok += val <= 1.0 + 1e-12
            if t <= 20: dmax = max(dmax, abs(p - Q(t)))
        D.append(dmax)
        res["cases"].append(dict(beta=b, meanO=m, meanO_exact=ex, P_t4=tail(b, 4.0),
                                 P_t10=tail(b, 10.0), D=dmax))
    p84 = tail(8, 4.0)
    preds = {"T1": t1, "T2": n_ok == n_all, "T3": abs(p84 - 0.03988840) <= 1e-6,
             "T4": all(D[i+1] < D[i] for i in range(len(D)-1))}
    res.update(T2_count=f"{n_ok}/{n_all} cases qualify", Cemp=worst, P8_4=p84, D=D,
               predicates={k: bool(v) for k, v in preds.items()})
    with open(out, "x") as f: json.dump(res, f, indent=1)
    for c in res["cases"]:
        print(c)
    print("T2", res["T2_count"], "Cemp(sup P e^{t/8})", worst, "P_8(O>4)", p84, "D", D)
    print({k: ("MET" if v else "FAILED") for k, v in preds.items()})
    return 0 if all(preds.values()) else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
