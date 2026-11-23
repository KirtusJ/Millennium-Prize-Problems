"""fid_check.py -- numeric constants of tun_lower.tex. Predicates FIXED BEFORE THE FIRST RUN.
Notation: eps(a)=2 asinh(sin a); e(S)=2 asinh S; alpha(S)=2S sqrt(1+S^2); h(S)=1+sqrt(1+S^2)/S.
P1  c* = int_0^pi sqrt(2 eps) da equals 4.6054132 to 5e-8 (7 printed decimals; Gauss-Legendre 400 nodes, a=u^2).
P2  a_- = arcsin(sinh eta): eps(sin a_-)=2 eta to 1e-12 for eta in {0.4,0.2,0.1,0.05,0.01};
    a_- <= pi/4 for all eta<=0.4, and arcsin(sinh 0.65)<=pi/4<arcsin(sinh 0.66) (tex says "eta<=0.65").
P3  Coefficients: 8.35*3+9.09<=35 ; 8.35*2+9.09<=35 ; 8.35<=35 (junction/corner bound 35(a_-+r0)).
P4  r0=sqrt(eta sin a_-/4): r0^2/sin a_- = eta/4 to 1e-12; ell=r0/3 < r0/2; r0 < pi/2.
P5  c1 condition: M^2 := -log(Gmin (e^{eta/2}-1) e^{-C}/4), Gmin=exp(-(sqrt2/sin a_-)(e(sqrt2)+1)),
    C=e(sqrt2)+eta+theta0^2/2+1. tex remark says M^2>=18.0 at eta=0.4; FULL says 14.8,23.4,40.4,73.9,174,339
    at eta=0.4,0.2,0.1,0.05,0.02?,0.01 (the list has 6 values for 5+ etas; eta list unknown -> reported only).
    Predicate: M^2 >= 1.5*rho_B^2+log 2 = 1.0681 for every eta in (0,0.4] sampled; and report M^2.
P6  L_beta (tex L4) at beta=1e4,1e6,1e9,1e12,1e16 equals 0.014,0.096,0.31,0.53,0.75 within 0.0006 / 0.0006 /0.006/0.006/0.006
    (rounding of the printed digits).  k-step law: density of theta ~ sin^2(theta) e^{beta cos theta}.
P7  h-closed form: |log J(closed form of tex Lemma gauss) - log J(direct Gaussian completion)| < 1e-9 on 200 random
    points (random u1,u2 unit-ish, random Psi',Theta' tilts, beta=1e3,b=sqrt(beta) w).  Also G1: ||l l^T-(S^2 I-u1u1^T-u2u2^T-2ww^T)||<1e-12,
    G2: l p=-kappa w to 1e-12, flat identity (h-2)(1+2S^2h)=h and 1+2S^2h=exp(e(S)) to 1e-12.
P8  (vol) v(r)>=11 r^3/(24 pi) for r in (0,1/2] (grid 2000);  (I1 up) I1(z)<=(pi/2)e^z/sqrt(2 pi z) for z in {1,10,100,1e3,1e4} .
P9  S4-alg slack in the limit Delta_i->0, lambda=1: slack=1-[(1-x)(1-y)/A1 + x A2/A1 + y A3/A1] >=0 on a grid of the support
    a1 in [a_-,pi/2], a2 in {0..r0 grid} (y=0) and a2=r0 (y in [0,1)), t=beta*alpha*q/2 in [0,M^2) (x=exp(t-M^2)),
    with M^2 at equality in c1 condition; eta in {0.4,0.2,0.1,0.05,0.01}.  Claimed (tex) slack: 0.107,0.107,0.095,0.049,0.0100.
    Predicate: min slack >= 0 for all five eta.  Claimed numbers compared and reported only (grid unspecified in the tex).
Tolerances: P1 7-decimal rounding; P2/P4/P7 double precision; P6 rounding of printed digits; others exact inequalities.
Result file opened with mode 'x'. Fixed seed 12345."""
import sys, numpy as np
from math import *
rng = np.random.default_rng(12345)
out = []
def rec(name, ok, msg):
    out.append("%s %s : %s" % (name, "MET" if ok else "FAILED", msg))
eps = lambda a: 2*np.arcsinh(np.sin(a)); e = lambda S: 2*np.arcsinh(S)
# P1
x, w = np.polynomial.legendre.leggauss(400); u = (x+1)/2*sqrt(pi); wu = w/2*sqrt(pi)
cs = float(np.sum(wu*2*u*np.sqrt(2*eps(u*u))))
rec("P1", abs(cs-4.6054132) < 5e-8, "c*=%.9f" % cs)
# P2/P4
ok = True; msg = []
for eta in [0.4, 0.2, 0.1, 0.05, 0.01]:
    am = asin(sinh(eta)); r0 = sqrt(eta*sin(am)/4)
    ok &= abs(float(eps(am))-2*eta) < 1e-12 and am <= pi/4
    msg.append("eta=%g a-=%.6f r0=%.6f r0^2/sin=%.3e(eta/4=%.3e)" % (eta, am, r0, r0*r0/sin(am), eta/4))
    ok &= abs(r0*r0/sin(am)-eta/4) < 1e-12 and r0/3 < r0/2 and r0 < pi/2
rec("P2/P4", ok, "; ".join(msg))
rec("P2b", asin(sinh(.65)) <= pi/4 < asin(sinh(.66)), "arcsin(sinh .65)=%.5f arcsin(sinh .66)=%.5f pi/4=%.5f" % (asin(sinh(.65)), asin(sinh(.66)), pi/4))
rec("P3", 8.35*3+9.09 <= 35 and 8.35*2+9.09 <= 35, "corner %.2f junction a-coef %.2f r0 coef 8.35" % (8.35*3+9.09, 8.35*2+9.09))
# P5
def M2(eta):
    am = asin(sinh(eta)); lGm = -(sqrt(2)/sin(am))*(float(e(sqrt(2)))+1); C = float(e(sqrt(2)))+eta+.125+1
    return -(lGm+log(expm1(eta/2))-C-log(4))   # log domain: Gmin underflows for small eta (run1 defect, mine)
etas = [0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
rec("P5", all(M2(t) >= 1.5*.25+log(2) for t in etas), "M^2 = " + ", ".join("%g:%.2f" % (t, M2(t)) for t in etas) + " ; 3.4/eta+O(1) check eta*M^2 = " + ", ".join("%.2f" % (t*M2(t)) for t in etas))
# P6
def Lbeta(beta):
    r = beta**(-1/3); t = beta**(-5/12); T = t*sqrt(beta)
    vol = lambda r: (2*r-sin(2*r))/(2*pi)
    uu = np.linspace(0, 60, 600001)[1:]; th = uu/sqrt(beta)
    dens = np.sin(th)**2*np.exp(-2*beta*np.sin(th/2)**2)
    tot = np.trapezoid(dens, uu); m = uu <= T
    P = np.trapezoid(dens[m], uu[m])/tot
    # refine upper cell
    return exp(-2*beta*r**4)*((vol(r-t)/vol(r))*P)**2, P
claim = {1e4: .014, 1e6: .096, 1e9: .31, 1e12: .53, 1e16: .75}; tol = {1e4: 6e-4, 1e6: 6e-4, 1e9: 6e-3, 1e12: 6e-3, 1e16: 6e-3}
ok = True; msg = []
for b in claim:
    L, P = Lbeta(b); ok &= abs(L-claim[b]) < tol[b]; msg.append("beta=%g L=%.4f (claim %.3f) P_k=%.4f" % (b, L, claim[b], P))
rec("P6", ok, "; ".join(msg))
# P7
def rot(ax, ang):
    ax = ax/np.linalg.norm(ax); K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]]); return np.eye(3)+sin(ang)*K+(1-cos(ang))*K@K
cr = lambda a: np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
worstJ = worstG1 = worstG2 = worstF = 0; beta = 1e3
for _ in range(200):
    a1, a2 = rng.uniform(.3, 1.4), rng.uniform(.05, .4)
    n1 = rng.normal(size=3); n1 /= np.linalg.norm(n1); n2 = rng.normal(size=3); n2 /= np.linalg.norm(n2)
    u1, u2 = sin(a1)*n1, sin(a2)*n2; x01, x02 = cos(a1), cos(a2)
    R1 = x01*np.eye(3)+cr(u1); R2 = x02*np.eye(3)+cr(u2)
    L = np.hstack([-cr(u2)@R1, cr(u1)@R2])   # l(xi)=R1xi1 x u2 + u1 x R2 xi2
    wv = np.cross(u1, u2); S2 = u1@u1+u2@u2; S = sqrt(S2); W = wv@wv
    worstG1 = max(worstG1, np.abs(L@L.T-(S2*np.eye(3)-np.outer(u1, u1)-np.outer(u2, u2)-2*np.outer(wv, wv))).max())
    hh = 1+sqrt(1+S2)/S
    th0, ell = .5, .05
    Pp, Tp = rng.uniform(0, 1.8), rng.uniform(0, .5)
    p = -np.concatenate([Pp*u1/np.linalg.norm(u1), Tp*u2/np.linalg.norm(u2)])
    kappa = Pp*x01/sin(a1)+Tp*x02/sin(a2)
    worstG2 = max(worstG2, np.abs(L@p+kappa*wv).max())
    worstF = max(worstF, abs((hh-2)*(1+2*S2*hh)-hh), abs(1+2*S2*hh-exp(e(S))))
    b = sqrt(beta)*wv; P_ = np.eye(6)+2*hh*L.T@L; c = p-2*hh*L.T@b
    direct = -.5*np.linalg.slogdet(P_)[1]+.5*c@np.linalg.solve(P_, c)-hh*b@b
    sv = np.linalg.svd(L, compute_uv=False)
    sw2 = S2-2*W; sw = sqrt(sw2); sj2 = sv**2
    # singular values of l: sw, and the two others (from l l^T eigenvalues); closed form uses all three sigma_j^2 and the w-component
    pw = -kappa*sqrt(W)/sw; bw = np.linalg.norm(b)
    closed = (Pp**2+Tp**2)/2-.5*np.sum(np.log(1+2*hh*sj2))-(hh*pw**2*sw2+2*hh*sw*pw*bw+hh*bw**2)/(1+2*hh*sw2)
    worstJ = max(worstJ, abs(closed-direct))
rec("P7", worstJ < 1e-9 and worstG1 < 1e-12 and worstG2 < 1e-12 and worstF < 1e-12, "logJ closed-vs-direct %.3e G1 %.3e G2 %.3e flat %.3e" % (worstJ, worstG1, worstG2, worstF))
# P8
rr = np.linspace(1e-4, .5, 2000); vv = (2*rr-np.sin(2*rr))/(2*pi)
ok8 = bool(np.all(vv >= 11*rr**3/(24*pi))); tt = np.linspace(0, pi, 400001)
ok8b = True; msg = []
for z in [1, 10, 100, 1e3, 1e4]:
    I1s = np.trapezoid(np.exp(z*(np.cos(tt)-1))*np.cos(tt), tt)/pi   # e^{-z} I1
    ratio = I1s/((pi/2)/sqrt(2*pi*z)); ok8b &= ratio <= 1; msg.append("z=%g ratio %.4f" % (z, ratio))
rec("P8", ok8 and ok8b, "vol min ratio %.3f; " % float(np.min(vv/(11*rr**3/(24*pi)))) + "; ".join(msg))
# P9
claimed = {0.4: .107, 0.2: .107, 0.1: .095, 0.05: .049, 0.01: .0100}; msg = []; ok9 = True
for eta in claimed:
    am = asin(sinh(eta)); r0 = sqrt(eta*sin(am)/4); ell = r0/3; th0 = .5; m2 = M2(eta)
    best = 9
    for a1 in np.linspace(am, pi/2, 60):
        Pp2 = 2*(float(eps(a1))+eta)
        for a2, ys in [(a, [0.]) for a in np.linspace(0, r0, 25)[:-1]]+[(r0, list(np.linspace(0, .99, 12)))]:
            Tp2 = (th0*a2/sqrt(a2*a2+ell*ell))**2
            S = sqrt(sin(a1)**2+sin(a2)**2)
            for t in np.linspace(0, m2*.999999, 400):
                xx = exp(t-m2); Vh = t*S/sqrt(1+S*S)
                A1 = exp(-float(e(S))+(Pp2+Tp2)/2); A2 = exp(-Vh+(Pp2+Tp2)/2); A3 = exp(-float(e(S))+Pp2/2)
                for y in ys:
                    best = min(best, 1-((1-xx)*(1-y)/A1+xx*A2/A1+y*A3/A1))
    ok9 &= best >= 0; msg.append("eta=%g min slack %.4f (claimed %.4f)" % (eta, best, claimed[eta]))
rec("P9", ok9, "; ".join(msg))
s = "\n".join(out); print(s)
with open("results_fid_rerun_parent.txt", "x") as fh: fh.write(s+"\n")
sys.exit(0 if all(" MET" in l for l in out) else 1)
