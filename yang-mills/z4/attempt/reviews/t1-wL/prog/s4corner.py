"""s4corner.py -- writer t1-wL. Checks of constants used in tun_lower.tex (main terms only, beta -> infinity limit).

Predicates (fixed before the first run):
 P1 (S4-alg main-term inequality, the case analysis of the assembly file): for each eta in
    {0.4,0.2,0.1,0.05,0.01}, with a_-=arcsin(sinh eta), r0=sqrt(eta sin a_-/4), l=r0/3, theta0=1/2,
    and M^2 taken AT EQUALITY in the c1 condition c1 = G_min (e^{eta/2}-1) e^{-C}/4,
    G_min = exp(-(sqrt2/sin a_-)(e(sqrt2)+1)), C = e(sqrt2)+eta+theta0^2/2+1,
    the lower bound  A1 G E - A2 c1 E - A3 c2 G >= lambda (G-c1)(E-c2)  holds (Delta_i = 0, lambda = 1)
    at every grid point of the support with a1 in [a_-, pi/2]. Equivalent form, with x=c1/G, y=c2/E in [0,1):
       1 >= (1/A1)(1-x)(1-y) + (A2/A1) x + (A3/A1) y.
    Grid: a1 (40 pts), a2 in [0,r0] (40 pts; y in [0,1) free when a2=r0, y=0 otherwise), t=beta alpha q/2 in [0,M^2) (200 pts),
    y (200 pts). The assembly file's claim implies P1 holds. Tolerance 0 (exact main terms; o(1) dropped).
    Measured: min slack and where.
 P2 (FULL sec 4): "M^2 >= 2 rho_B^2" implies e^{-1.5 rho_B^2} - e^{-M^2} >= e^{-1.5 rho_B^2}/2, at rho_B = 1/2.
    Tested at M^2 = 2 rho_B^2 exactly (the minimal admissible value). Expectation of the writer: FAILS.
 P3 (HARNACK constants): min over d,rho<=1/2 of l(K0)/d is 8.35 +- 0.01, and l(K_K)/d at d=3.65, rho=0.265, K=1 is 9.09 +- 0.01,
    where l(K') = K' + R^2 + log(pi/2) + 2 log(24 pi/(11 rho^3)), R = d + 2 rho, K0 = 2(2rho+rho^2)^2,
    K_K = 2(sqrt(K/2)+2rho+rho^2)^2. Tolerance 0.01 = rounding of the quoted values. Also 8.35*2+9.09 <= 35 and 8.35 <= 35.
"""
import math, sys, json
out = sys.argv[1]
fh = open(out, "x")
def e(S): return 2*math.asinh(S)
res = {}
# P1
allok = True; worst = None
for eta in [0.4, 0.2, 0.1, 0.05, 0.01]:
    am = math.asin(math.sinh(eta)); r0 = math.sqrt(eta*math.sin(am)/4); l = r0/3; th0 = 0.5
    Gmin = math.exp(-(math.sqrt(2)/math.sin(am))*(e(math.sqrt(2))+1)); C = e(math.sqrt(2))+eta+th0**2/2+1
    M2 = -math.log(Gmin*(math.exp(eta/2)-1)*math.exp(-C)/4)
    mins = (1e9, None)
    for i in range(40):
        a1 = am + (math.pi/2-am)*i/39
        for j in range(40):
            a2 = r0*j/39
            S = math.sqrt(math.sin(a1)**2+math.sin(a2)**2)
            Thp = th0*a2/math.sqrt(a2*a2+l*l)
            lnA1 = -e(S) + 2*math.asinh(math.sin(a1)) + eta + Thp**2/2   # Psi'^2/2 = eps(sin a1)+eta
            ys = [k/200 for k in range(200)] if j == 39 else [0.0]
            for kk in range(200):
                t = M2*kk/200
                x = math.exp(t-M2)
                V2 = t*S/math.sqrt(1+S*S)
                lnp = -V2 + e(S)            # log(A2/A1)
                lnr = -Thp**2/2             # log(A3/A1)
                for y in ys:
                    rhs = math.exp(-lnA1)*(1-x)*(1-y) + math.exp(lnp)*x + math.exp(lnr)*y
                    sl = 1 - rhs
                    if sl < mins[0]: mins = (sl, dict(a1=a1, a2=a2, t=t, M2=M2, x=x, y=y, p=math.exp(lnp), r=math.exp(lnr)))
    ok = mins[0] >= 0
    allok &= ok
    res[f"P1_eta{eta}"] = dict(met=ok, M2=M2, min_slack=mins[0], at=mins[1])
res["P1"] = allok
# P2
rB = 0.5; M2 = 2*rB**2
lhs = math.exp(-1.5*rB**2) - math.exp(-M2); rhs = math.exp(-1.5*rB**2)/2
res["P2"] = dict(met=lhs >= rhs, lhs=lhs, rhs=rhs, needed_M2=1.5*rB**2+math.log(2))
# P3
def ell(Kp, d, rho): return Kp + (d+2*rho)**2 + math.log(math.pi/2) + 2*math.log(24*math.pi/(11*rho**3))
best = min((ell(2*(2*r+r*r)**2, d, r)/d, d, r) for d in [1+0.005*i for i in range(800)] for r in [0.05+0.001*k for k in range(451)])
lk = ell(2*(math.sqrt(0.5)+2*0.265+0.265**2)**2, 3.65, 0.265)/3.65
res["P3"] = dict(met=abs(best[0]-8.35) <= 0.01 and abs(lk-9.09) <= 0.01 and 2*8.35+9.09 <= 35, min_l0_over_d=best, lK_over_d=lk)
json.dump(res, fh, indent=1); fh.close()
print(json.dumps({k: (v if isinstance(v, bool) else v.get("met")) for k, v in res.items()}))
