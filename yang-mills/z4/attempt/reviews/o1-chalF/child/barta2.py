"""T142 follow-up: log-form refinement check (fixes P4 defect of barta.py: underflow).
Predicates fixed before first run:
 Q1 log B: coarse (P=256,n=24) vs fine (P=512,n=32) differ < 1e-9 absolute (= relative on B) for ALL 108 cases
    (tolerance: same 1e-9 as P4 but on log B, which cannot underflow).
 Q2 exp(logB_fine) agrees with res1.csv B within 1e-9 relative wherever B>1e-250 (count reported).
 Q3 grandchild B(0; beta=64,s=0.3)=0.5576952560 agrees with ours within 1e-9 relative.
"""
import numpy as np, sys, csv
from barta import ive, RHOS, BETAS, SS
def logB(beta, s, rho, P=256, n=24):
    al = 2*s*np.sqrt(1+s*s); c = s*s+al/2; A = 1+2*c
    R = np.sqrt(max(1-rho*rho, 0.0)); pk = np.arcsin(min(rho/A, 1.0))
    br = np.unique(np.concatenate([np.linspace(0, np.pi/2, P+1), [pk]]))
    xg, wg = np.polynomial.legendre.leggauss(n)
    a, b = br[:-1], br[1:]
    phi = (0.5*(b-a)[:,None]*xg[None,:] + 0.5*(a+b)[:,None]).ravel()
    wt = (0.5*(b-a)[:,None]*wg[None,:]).ravel()
    rp = np.sin(phi); Rp = np.cos(phi)
    f = ive(0, beta*R*Rp)*ive(0, beta*rho*rp)
    e = beta*(R*Rp + rho*rp - c*rp**2 + (al/2-s*s)*rho**2 - 1.0)
    i1 = ive(1, np.array([beta]))[0]
    lg = np.log(wt*f*rp*Rp) + e
    m = lg.max()
    return np.log(beta/i1) + m + np.log(np.exp(lg-m).sum())
def main():
    old = {(int(r['beta']), float(r['s']), float(r['rho'])): float(r['B']) for r in csv.DictReader(open('res1.csv'))}
    fails = []; ok1 = 0; ok2 = 0; n2 = 0; rows = []
    for beta in BETAS:
        for s in SS:
            for rho in RHOS:
                l = logB(beta, s, rho); l2 = logB(beta, s, rho, 512, 32)
                ok1 += abs(l-l2) < 1e-9
                ob = old[(beta, s, rho)]
                if ob > 1e-250:
                    n2 += 1; ok2 += abs(np.exp(l2)-ob)/ob < 1e-9
                rows.append((beta, s, rho, l2, abs(l-l2)))
    print("Q1", ok1, "/108"); print("Q2", ok2, "/", n2)
    if ok1 != 108: fails.append("Q1")
    if ok2 != n2: fails.append("Q2")
    g = float(np.exp(logB(64, .3, 0.0, 512, 32))); gc = 0.5576952560
    print("Q3 mine", repr(g), "grandchild", gc, "rel", abs(g-gc)/g)
    if abs(g-gc)/g >= 1e-9: fails.append("Q3")
    with open("res_log.csv", "x") as f:
        f.write("beta,s,rho,logB,abs_change_on_refinement\n")
        for r in rows: f.write("%d,%g,%g,%.12f,%.3e\n" % r)
    print("FAILED:", fails); return 1 if fails else 0
if __name__ == "__main__": sys.exit(main())
