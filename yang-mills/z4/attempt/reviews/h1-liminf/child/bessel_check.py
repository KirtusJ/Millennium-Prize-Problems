"""T90 numeric check of predicates (A)-(D). Fixed: no randomness (deterministic grid).
Notation r_nu=I_{nu+1}/I_nu, kappa_n=I_{n+1}/I_1 = prod_{j=1}^n r_j (kappa_0=1).
Predicates (fixed before first run), grid nu,n=0..400, x,beta in G:
 (A) r_nu(x) - x/(nu+1+sqrt((nu+1)^2+x^2)) >= -TOL
 (B) x/(nu+1/2+sqrt((nu+1/2)^2+x^2)) - r_nu(x) >= -TOL
 (C) n(n+2)/(2(beta+n+1/2)) <= -ln kappa_n <= n(n+3)/(2beta), each side within TOL
 (D) m in {.05,.1,.2,.3}, beta in G, beta>=100, M=floor(m sqrt beta), 0<=n1,n2<=M:
     1-k1*k2 - (beta/(beta+M+1/2))/(1+m^2+3m/sqrt(beta))*(n1(n1+2)+n2(n2+2))/(2beta) >= -TOL
TOL = 1e-25 (Decimal prec 70; r from backward continued-fraction recurrence, started at two
different depths; case valid only if the two agree to 1e-40 relative => truncation error << TOL).
Equality cases (n=0 in C; n1=n2=0 in D) are exact zeros; slack 0 counts as met.
Validation: I0(1),I1(1),I0(10),I1(10) from power series vs known literature values.
Output: results.json (mode x), failures listed. Nothing is overwritten."""
import sys, json, math
from decimal import Decimal as D, getcontext
getcontext().prec = 70
G = [D(s) for s in "0.5 1 2 5 10 20 50 100 200 500 1000 2000 5000 10000".split()]
NMAX = 400

def ratios(x, extra):
    N = NMAX + 2 + int(x) + extra
    r = D(0)
    out = {}
    for nu in range(N, -1, -1):          # r_nu = 1/(2(nu+1)/x + r_{nu+1})
        r = 1 / (D(2*(nu+1))/x + r)
        if nu <= NMAX + 1: out[nu] = r
    return out

def series_I(n, x):
    x = D(x); s = D(0); t = (x/2)**n / math.factorial(n); k = 0
    while True:
        s += t; k += 1; t = t*(x/2)**2/(k*(k+n))
        if t < D(10)**-60: break
    return s

def validate():
    known = {(0,1):"1.2660658777520082",(1,1):"0.5651591039924851",(0,10):"2815.716628466254",(1,10):"2670.988303701255"}
    res = {}
    for (n,x),v in known.items():
        got = series_I(n,x); err = abs(got-D(v))/D(v)
        res[f"I{n}({x})"]=(str(got)[:20], v, float(err)); assert err < D("1e-14"), (n,x,got)
    # CF vs series ratio
    for x in (D(1), D(10)):
        rr = ratios(x, 200)[1]; ser = series_I(2,x)/series_I(1,x)
        assert abs(rr-ser)/ser < D("1e-40")
    return res

def main():
    TOL = D("1e-25")
    val = validate()
    out = {"validation": val, "counts": {}, "min_slack": {}, "failures": {"A":[],"B":[],"C":[],"D":[]}, "invalid": []}
    cnt = {k:0 for k in "ABCD"}; ok = {k:0 for k in "ABCD"}
    mins = {k:(None,None) for k in "ABCD"}   # (slack/(relative scale), where)
    nz = {k:(None,None) for k in "ABCD"}  # smallest strictly positive RELATIVE slack
    def rec(k, slack, rel, where):
        cnt[k]+=1
        if slack >= -TOL: ok[k]+=1
        else: out["failures"][k].append([where, float(slack)])
        # smallest slack: use relative slack (slack / rhs scale) to compare meaningfully, also keep abs
        if mins[k][0] is None or slack < mins[k][0][0]: mins[k]=((slack,rel),where)
        if slack > 0 and (nz[k][0] is None or rel < nz[k][0][1]): nz[k]=((slack,rel),where)
    for x in G:
        ra = ratios(x, 300); rb = ratios(x, 600)
        bad = [nu for nu in range(NMAX+1) if abs(ra[nu]-rb[nu]) > D("1e-40")*ra[nu]]
        if bad: out["invalid"].append([float(x), bad[:3], len(bad)]); continue
        r = ra
        # kappa_n via cumulative product r_1..r_n
        kap = [D(1)]
        for n in range(1, NMAX+1): kap.append(kap[-1]*r[n])
        xf = x
        for nu in range(NMAX+1):
            lo = x/((nu+1)+((D(nu+1))**2+x*x).sqrt())
            hi = x/((D(nu)+D("0.5"))+((D(nu)+D("0.5"))**2+x*x).sqrt())
            rec("A", r[nu]-lo, (r[nu]-lo)/r[nu], ("nu",nu,"x",float(x)))
            rec("B", hi-r[nu], (hi-r[nu])/r[nu], ("nu",nu,"x",float(x)))
        for n in range(NMAX+1):
            nl = -kap[n].ln()
            lo = D(n*(n+2))/(2*(x+n+D("0.5"))); hi = D(n*(n+3))/(2*x)
            rec("C", min(nl-lo, hi-nl), min(nl-lo,hi-nl)/(hi if hi>0 else D(1)), ("n",n,"beta",float(x)))
        if x >= 100:
            for m in map(D, ("0.05","0.1","0.2","0.3")):
                M = int((m*x.sqrt()).to_integral_value(rounding="ROUND_FLOOR"))
                pre = (x/(x+M+D("0.5")))/(1+m*m+3*m/x.sqrt())
                for n1 in range(M+1):
                    for n2 in range(M+1):
                        rhs = pre*(n1*(n1+2)+n2*(n2+2))/(2*x)
                        lhs = 1-kap[n1]*kap[n2]
                        rec("D", lhs-rhs, (lhs-rhs)/lhs if lhs>0 else D(0), ("m",float(m),"beta",float(x),"M",M,"n1",n1,"n2",n2))
    for k in "ABCD":
        out["counts"][k] = {"cases":cnt[k], "pass":ok[k], "fail":cnt[k]-ok[k]}
        (s,rel),w = mins[k]
        (s2,r2),w2 = nz[k]
        out["min_pos_rel_slack"] = out.get("min_pos_rel_slack",{}); out["min_pos_rel_slack"][k]={"abs":float(s2),"rel":float(r2),"where":w2}
        out["min_slack"][k] = {"abs":float(s), "rel":float(rel), "where":w, "abs_str":str(s)[:30]}
    with open(sys.argv[1],"x") as f: json.dump(out,f,indent=1)
    print(json.dumps({k:out[k] for k in ("counts","min_slack","min_pos_rel_slack","invalid")},indent=1,default=str))
    print({k:len(v) for k,v in out["failures"].items()})
    sys.exit(0 if not any(out["failures"].values()) and not out["invalid"] else 1)
main()
