"""T142 Barta ratio quadrature (numpy only: scipy is not installed here).

Fixed predicates (before first run):
 P1 Bessel: exp(1)*ive0(1)=1.2660658778 and ive1(1)*e=0.5651591040 within 1e-9
    (reference: tabulated I_0(1), I_1(1); tolerance = 1e-9 abs, trapezoid is spectral).
 P2 Bessel nodes: ive0/ive1 at x in {64,4096} with M nodes vs 2M nodes agree < 1e-13 rel.
 P3 s->0: B(0) at s=1e-9, beta=64 equals 1 within 1e-8 (identity int I0(b R')u du=I1(b)/b).
 P4 quadrature refinement (panels P->2P, GL nodes n->n+8): B changes < 1e-9 relative
    for ALL 108 cases (count qualifying cases is reported).
 P5 hypothesis 'B(rho)<=1 for all cases' is tested and counted, not asserted.
Method: rho'=sin(phi), R'=cos(phi), smooth in phi on [0,pi/2]; composite Gauss-Legendre with
breakpoints at uniform grid plus phi*=asin(min(rho/A,1)). Exponent combined in log form:
 log B = beta[(a/2-s^2)rho^2 + ...] using ive: I_n(x)=ive(n,x)e^x, total exponent
 beta*(R R' + rho rho' - c rho'^2 + (a/2-s^2) rho^2 - 1).
Outputs opened with mode 'x'.
"""
import numpy as np, sys

def ive(n, x, M=None):
    """exp(-x) I_n(x), x>=0 array, periodic midpoint rule on [0,pi]."""
    x = np.asarray(x, float)
    if M is None:
        M = int(8*np.sqrt(max(float(x.max()), 1.0))) + 48
    t = (np.arange(M)+0.5)*np.pi/M
    w = np.exp(np.multiply.outer(x, np.cos(t)-1.0))
    if n: w = w*np.cos(n*t)
    return w.mean(axis=-1)

def B(beta, s, rho, P=256, n=24, Mscale=None):
    al = 2*s*np.sqrt(1+s*s); c = s*s+al/2; A = 1+2*c
    R = np.sqrt(max(1-rho*rho, 0.0))
    pk = np.arcsin(min(rho/A, 1.0))
    br = np.unique(np.concatenate([np.linspace(0, np.pi/2, P+1), [pk]]))
    xg, wg = np.polynomial.legendre.leggauss(n)
    a, b = br[:-1], br[1:]
    phi = (0.5*(b-a)[:,None]*xg[None,:] + 0.5*(a+b)[:,None]).ravel()
    wt = (0.5*(b-a)[:,None]*wg[None,:]).ravel()
    rp = np.sin(phi); Rp = np.cos(phi)
    x1 = beta*R*Rp; x2 = beta*rho*rp
    M1 = None if Mscale is None else Mscale
    f = (ive(0, x1, M1)*ive(0, x2, M1))
    e = beta*(R*Rp + rho*rp - c*rp**2 + (al/2-s*s)*rho**2 - 1.0)
    # I1(beta)=ive1(beta)e^beta ; ive1 scalar
    i1 = ive(1, np.array([beta]), M1)[0]
    val = beta/i1*np.sum(wt*f*np.exp(e)*rp*Rp)   # rho' d rho' = sin cos dphi
    return val

RHOS = [0, .1, .3, .5, .7, .9, .99, .999, 1.0]
BETAS = [64, 256, 1024, 4096]; SS = [.1, .3, 1.0]
def main():
    fails = []
    e1 = np.exp(1.0)
    v0 = e1*ive(0, np.array([1.0]))[0]; v1 = e1*ive(1, np.array([1.0]))[0]
    p1 = abs(v0-1.2660658778) < 1e-9 and abs(v1-0.5651591040) < 1e-9
    print("P1", p1, v0, v1)
    if not p1: fails.append("P1")
    worst = 0
    for x in (64., 4096.):
        for n in (0, 1):
            m = int(8*np.sqrt(x))+48
            a = ive(n, np.array([x]), m)[0]; b = ive(n, np.array([x]), 2*m)[0]
            worst = max(worst, abs(a-b)/abs(b))
    p2 = worst < 1e-13; print("P2", p2, worst)
    if not p2: fails.append("P2")
    b0 = B(64, 1e-9, 0.0); p3 = abs(b0-1) < 1e-8; print("P3", p3, b0)
    if not p3: fails.append("P3")
    rows = []; ok = 0; maxrel = 0; le1 = 0
    for beta in BETAS:
        for s in SS:
            for rho in RHOS:
                v = B(beta, s, rho); v2 = B(beta, s, rho, P=512, n=32)
                rel = abs(v-v2)/abs(v2); maxrel = max(maxrel, rel)
                ok += rel < 1e-9; le1 += v2 <= 1
                rows.append((beta, s, rho, v2, rel, v))
    print("P4 qualifying", ok, "of", len(rows), "max rel", maxrel)
    if ok != len(rows): fails.append("P4")
    print("P5 B<=1 in", le1, "of", len(rows), "(not asserted)")
    with open("res1.csv", "x") as f:
        f.write("beta,s,rho,B\n")
        for r in rows: f.write("%d,%g,%g,%.12e\n" % r[:4])
    with open("res_conv.csv", "x") as f:
        f.write("beta,s,rho,B_fine,rel_change,B_coarse\n")
        for r in rows: f.write("%d,%g,%g,%.12e,%.3e,%.12e\n" % r)
    with open("summary.csv", "x") as f:
        f.write("beta,s,A,supB,rho_at_sup,neg_log_supB,neg_log_supB_minus_logA\n")
        for beta in BETAS:
            for s in SS:
                al = 2*s*np.sqrt(1+s*s); A = 1+al+2*s*s
                sub = [r for r in rows if r[0] == beta and r[1] == s]
                m = max(sub, key=lambda r: r[3])
                f.write("%d,%g,%.10f,%.12e,%g,%.10f,%.10f\n" % (beta, s, A, m[3], m[2], -np.log(m[3]), -np.log(m[3])-np.log(A)))
    print("FAILED:", fails)
    return 1 if fails else 0
if __name__ == "__main__":
    sys.exit(main())
