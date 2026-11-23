"""check_gaps.py -- u1-gapB (T174). Numerical checks of the new inequalities for gaps A, B, C.

Definitions (as in note/tun_lower.tex, Lemma tu:L-S4 and Section tu:L-sec-assembly):
  e(S)=2 asinh S, k(S)=sqrt(1+S^2)/S, gamma=1-1/k, s_lo=sinh(eta)=sin a_-, r0^2=eta sinh(eta)/4,
  s_hi=sqrt(1+r0^2), l=r0/3, theta0=1/2, Theta(a)=theta0(sqrt(a^2+l^2)-l), t=Theta'(a2)^2/2.
  m0=(1-e^{-3eta/4})/2, m1=(1-e^{-1/16})/2, m=min(m0,m1).
  MA2(eta)=2 sqrt(2+r0^2)+max(coth(eta) log(1/m1), 0.75 eta coth(eta)+log(1/m0))   [new condition (M_A)]
  Mc2(eta)=(sqrt2/sinh eta)(e(sqrt2)+1)+log4-log(e^{eta/2}-1)+C, C=e(sqrt2)+eta+1/8+1  [note's c1 condition at equality]
  P(S)=exp(e(S)-M^2/k(S)),  F(x,y;a,b)=a(1-x)(1-y)+P x^gamma+b y.

PREDICATES (fixed before first run):
 P1 (N1) for all eta in grid, S in [s_lo,s_hi], x,y in [0,1], a in {0,e^{-3eta/4}}, b in {0,e^{-1/16}}:
        F <= 1-m (M^2=MA2). (F is affine increasing in a and in b, so the end values suffice.)
 P2 (N2) same with b in {0,1}, y in [0,m/2]: F <= 1-m/2.
 P3 MA2 >= sup_S max(k(e+log(1/m1)), k e+(k-1)(3eta/4)+log(1/(k m0)))   (the two branch conditions) on the S grid.
 P4 MA2(eta) <= Mc2(eta) for all eta in grid (note's c1 choice implies (M_A)).
 P5 Physical limit check (Delta_i=0, lambda=1), M^2=MA2: over a1 in [a_-,pi/2], a2 in [0,r0), x in (0,1)
        (V determined by x), y in [0,1] if a2>=l, y=0 if a2<l:
        1-[ (1/A1)(1-x)(1-y)+(A2/A1)x+(A3/A1)y ] >= m  with A1,A2,A3 from the note (Delta=0).
 P6 Gap C: |Mc2(0.4)-18.0|<0.06 (writer's number reproduces) and |Mc2(0.4)-14.8|>1 (FULL's number does not).
 P7 Gap B constants: S sqrt(1+S^2) <= 1.5 for S^2<=1+rhoB^2/beta, beta>=4, rhoB=1/2;
        and e^{-1.5 rhoB^2}-e^{-MA2} >= e^{-1.5 rhoB^2}/2 for every eta in grid (needs MA2>=1.5rhoB^2+log2).
 M1 (measured only) min slack of P1, P5 per eta; physical slack also with M^2=Mc2; and the smallest M^2
        (bisection) for which the P5 limit inequality holds on the grid with slack>=0, times eta.
Tolerance: 1e-12 absolute on predicates P1-P5 (double rounding of exp/log of O(10) numbers is ~1e-14).
Seeds: none needed (deterministic grids).
Output: results_check_gaps.json opened with mode "x".
"""
import json, math, sys
import numpy as np

TOL = 1e-12
e = lambda S: 2*np.arcsinh(S)
kf = lambda S: np.sqrt(1+S*S)/S
ETAS = [0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 1e-4]

def pars(eta):
    r02 = eta*math.sinh(eta)/4
    m0 = (1-math.exp(-0.75*eta))/2; m1 = (1-math.exp(-1/16))/2
    coth = 1/math.tanh(eta)
    MA2 = 2*math.sqrt(2+r02) + max(coth*math.log(1/m1), 0.75*eta*coth+math.log(1/m0))
    e2 = 2*math.asinh(math.sqrt(2)); C = e2+eta+1/8+1
    Mc2 = (math.sqrt(2)/math.sinh(eta))*(e2+1)+math.log(4)-math.log(math.exp(eta/2)-1)+C
    return dict(r02=r02, r0=math.sqrt(r02), m0=m0, m1=m1, m=min(m0, m1), MA2=MA2, Mc2=Mc2,
                slo=math.sinh(eta), shi=math.sqrt(1+r02), am=math.asin(math.sinh(eta)))

def Fgrid(eta, M2, ymax, bvals):
    p = pars(eta)
    S = np.geomspace(p['slo'], p['shi'], 300)[:, None, None]
    x = np.concatenate([np.linspace(0, 1, 401), 1-np.geomspace(1e-9, 1e-2, 50), np.geomspace(1e-12, 1e-2, 50)])[None, :, None]
    y = np.linspace(0, ymax, 101)[None, None, :]
    k = kf(S); g = 1-1/k; P = np.exp(e(S)-M2/k)
    worst = -np.inf
    for a in (0.0, math.exp(-0.75*eta)):
        for b in bvals:
            F = a*(1-x)*(1-y)+P*x**g+b*y
            worst = max(worst, float(F.max()))
    return worst

def branches(eta):
    p = pars(eta)
    S = np.geomspace(p['slo'], p['shi'], 20000); k = kf(S)
    b1 = k*(e(S)+math.log(1/p['m1'])); b2 = k*e(S)+(k-1)*0.75*eta+np.log(1/(k*p['m0']))
    return float(max(b1.max(), b2.max()))

def phys_slack(eta, M2, n=120):
    p = pars(eta); am = p['am']; r0 = p['r0']; l = r0/3; th0 = 0.5
    a1 = np.linspace(am, math.pi/2, n)[:, None, None, None]
    a2 = np.concatenate([np.linspace(0, r0*(1-1e-9), n)])[None, :, None, None]
    x = np.concatenate([np.linspace(1e-9, 1-1e-9, 200), 1-np.geomspace(1e-9, 1e-2, 30)])[None, None, :, None]
    y = np.linspace(0, 1, 41)[None, None, None, :]
    S = np.sqrt(np.sin(a1)**2+np.sin(a2)**2); k = kf(S)
    V = 2*(M2+np.log(x))/k                       # x=c1/G=exp(-M2+kV/2)
    Thp = th0*a2/np.sqrt(a2**2+l**2); t = Thp**2/2
    Psi2 = 2*(e(np.sin(a1))+eta)                  # chi=1 on [a_-,pi/2]
    lA1 = -e(S)+Psi2/2+t; lA2 = -V/2+Psi2/2+t; lA3 = -e(S)+Psi2/2
    yy = np.where(a2 >= l, y, 0*y)
    R = np.exp(-lA1)*(1-x)*(1-yy)+np.exp(lA2-lA1)*x+np.exp(lA3-lA1)*yy
    return float((1-R).min())

def main():
    out = dict(predicates={}, measured={})
    fails = []
    def rec(name, ok, info):
        out['predicates'][name] = dict(ok=bool(ok), info=info)
        if not ok: fails.append(name)
    p1 = {}; p2 = {}; p3 = {}; p4 = {}; p5 = {}; m5 = {}
    for eta in ETAS:
        p = pars(eta)
        w1 = Fgrid(eta, p['MA2'], 1.0, (0.0, math.exp(-1/16)))
        p1[eta] = dict(maxF=w1, bound=1-p['m'], slack=(1-p['m'])-w1)
        w2 = Fgrid(eta, p['MA2'], p['m']/2, (0.0, 1.0))
        p2[eta] = dict(maxF=w2, bound=1-p['m']/2, slack=(1-p['m']/2)-w2)
        br = branches(eta); p3[eta] = dict(sup_branches=br, MA2=p['MA2'])
        p4[eta] = dict(MA2=p['MA2'], Mc2=p['Mc2'], eta_MA2=eta*p['MA2'], eta_Mc2=eta*p['Mc2'])
        if eta >= 0.001:
            s = phys_slack(eta, p['MA2']); p5[eta] = dict(slack=s, m=p['m'])
            sc = phys_slack(eta, p['Mc2'])
            lo, hi = 0.5, p['MA2']*1.5
            for _ in range(40):
                mid = (lo+hi)/2
                if phys_slack(eta, mid, n=60) >= 0: hi = mid
                else: lo = mid
            m5[eta] = dict(slack_at_MA2=s, slack_at_Mc2=sc, minimal_M2_grid=hi, eta_times_minimal_M2=eta*hi, m=p['m'])
        print(eta, p1[eta]['slack'], p2[eta]['slack'], br <= p['MA2'], p4[eta], m5.get(eta), flush=True)
    rec('P1', all(v['slack'] >= -TOL for v in p1.values()), p1)
    rec('P2', all(v['slack'] >= -TOL for v in p2.values()), p2)
    rec('P3', all(v['sup_branches'] <= v['MA2']+TOL for v in p3.values()), p3)
    rec('P4', all(v['MA2'] <= v['Mc2'] for v in p4.values()), p4)
    rec('P5', all(v['slack'] >= v['m']-TOL for v in p5.values()), p5)
    Mc = pars(0.4)['Mc2']
    rec('P6', abs(Mc-18.0) < 0.06 and abs(Mc-14.8) > 1, dict(Mc2_04=Mc))
    beta = np.linspace(4, 1e6, 100000); S = np.sqrt(1+0.25/beta)
    ok7a = float((S*np.sqrt(1+S*S)).max())
    ok7b = min(math.exp(-0.375)-math.exp(-pars(eta)['MA2'])-math.exp(-0.375)/2 for eta in ETAS)
    rec('P7', ok7a <= 1.5 and ok7b >= 0, dict(max_Ssqrt=ok7a, min_margin_G=ok7b))
    out['measured']['M1'] = m5
    out['failed'] = fails
    with open('results_check_gaps.json', 'x') as f:
        json.dump(out, f, indent=1, default=str)
    print('FAILED:', fails)
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
