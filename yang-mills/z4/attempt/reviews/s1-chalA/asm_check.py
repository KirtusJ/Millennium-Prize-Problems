"""asm_check.py -- numerical sanity checks for the NEW inequalities of TUNNEL_LOWER_FULL.md (worker r1-asm, T158).
Seed 12345 (numpy default_rng). Result file asm_check_results.json opened with mode "x".

PREDICATES (fixed before the first run; tolerance origin stated):
 P1 (Lemma L4, single-link core).  For U uniform on the geodesic ball B_r of S^3 (radius r about 1) and g ~ k (density prop. to
    sin^2 th e^{beta cos th}), P(Ug in B_r) >= LB1 := (v(r-t)/v(r)) * P(th <= t), v(r) = (2r - sin 2r)/(2pi).
    Checked by Monte Carlo (n = 200000) at beta in {256, 4096, 65536}, r = beta^{-1/3}, t = beta^{-5/12}:
    met if MC >= LB1 - 3*SE (3 SE: Monte Carlo noise).  "for all": 3 cases, all qualify (r > t needs beta^{1/12} > 1).
 P2 (Lemma L4, limit).  LBee(beta) = exp(-2 beta r^4) * LB1(beta)^2 and LBeo = LBee - 2 v(r)^2 k(pi-2r) k_sup (k from Z = 2 I1/beta,
    I1 lower bound (I7) of LEMMA_F) satisfy: LBeo nondecreasing on beta in {1e4,...,1e16} (decades) and 1 - LBeo(1e16) < 0.05.
    Tolerance 0.05: my own guess of the rate (1 - LB ~ beta^{-1/12}); a failure would be my expectation, not a defect.
    Also reported: first decade beta with LBeo >= exp(-eta/4) for eta = 0.25, 0.1 (measured only).
 P3 (tube balls inside supp phi).  For valley points U1 = (cos a, sin a e3), a in [a_-, pi - a_-], U2 = 1, and z within geodesic
    distance rho/sqrt(beta) in each link: beta alpha(S) q / 2 <= 1.5 rho^2 and a2(z) <= rho/sqrt(beta).
    Hypothesis of the bound: rho^2/beta <= 0.06; per rule 4 count qualifying cases. Tolerance 1e-12 (float rounding).
    Sampled 20000 points per beta in {64, 1024, 16384}, rho = 0.5, a_- = 0.2554.
 P4 (tent constant).  For eta in {0.25, 0.1, 0.02}: 2*Psi(pi/2) computed with Psi' = sqrt(2(eps+eta)) on [0, pi/2] equals
    c*(eta) = int_0^pi sqrt(2(eps+eta)) to 1e-9 (quadrature), and c*(eta) <= c* + pi sqrt(2 eta) (L3).  The monotone (non-tent)
    reading, Psi(pi - a_-) * 2, is reported (measured only) to show the factor-2 alternative.
 P5 (parameter chain).  For eta in {0.4, 0.2, 0.1, 0.05, 0.02, 0.01}: a_- = arcsin(sinh eta) <= pi/4 (HARNACK), r0 = sqrt(eta sin a_- /4)
    with r0 + 0.1 <= pi/2 (E13), l = r0/3 < r0/2, and the final bound B(eta) = c* + pi sqrt(2 eta) + 70 (a_- + r0) decreasing in eta
    with B(0.01) - c* < B(0.4) - c*.  M^2 required by S4-alg (c1 <= G_min (e^{3eta/4}-1) e^{-C}/4 with C = eps(sqrt2) + eta + 1)
    is reported (measured only) together with log(1/eta) and 1/sin a_-.
 P6 (E13 coverage, expected FAIL as a target-parameter defect).  E13's numerical eta' = 0.5 satisfies eta' <= a_-(eta = 0.25).
"""
import json, math, sys
import numpy as np

rng = np.random.default_rng(12345)
out = {}
CS = 4.6054132

def v(r):
    return (2*r - math.sin(2*r))/(2*math.pi)

def theta_cdf_grid(beta, n=200001):
    # density on [0, pi] prop. to sin^2 th exp(beta (cos th - 1)); grid restricted to where mass is
    tmax = min(math.pi, 40.0/math.sqrt(beta))
    th = np.linspace(0, tmax, n)
    d = np.sin(th)**2*np.exp(beta*(np.cos(th) - 1))
    c = np.concatenate([[0], np.cumsum((d[1:] + d[:-1])/2*np.diff(th))])
    return th, c/c[-1]

def p_theta_le(beta, t):
    th, c = theta_cdf_grid(beta)
    return float(np.interp(t, th, c))

def sample_theta(beta, n):
    th, c = theta_cdf_grid(beta)
    return np.interp(rng.random(n), c, th)

def sample_ball(r, n):
    a = np.linspace(0, r, 100001); d = np.sin(a)**2
    c = np.concatenate([[0], np.cumsum((d[1:] + d[:-1])/2*np.diff(a))]); c /= c[-1]
    return np.interp(rng.random(n), c, a)

def unit(n):
    x = rng.normal(size=(n, 3)); return x/np.linalg.norm(x, axis=1)[:, None]

def quat(angle, axis):
    return np.concatenate([np.cos(angle)[:, None], np.sin(angle)[:, None]*axis], axis=1)

def qmul(p, q):
    a0, a = p[:, 0], p[:, 1:]; b0, b = q[:, 0], q[:, 1:]
    return np.concatenate([(a0*b0 - np.sum(a*b, 1))[:, None], a0[:, None]*b + b0[:, None]*a + np.cross(a, b)], axis=1)

def cls(q):
    return np.arccos(np.clip(q[:, 0], -1, 1))

res = {"met": 0, "failed": 0, "measured": 0}
def judge(name, ok, info):
    out[name] = dict(ok=bool(ok), **info)
    res["met" if ok else "failed"] += 1
    print(name, "MET" if ok else "FAILED", info)

# P1
for beta in (256, 4096, 65536):
    r = beta**(-1/3); t = beta**(-5/12); n = 200000
    LB1 = v(r - t)/v(r)*p_theta_le(beta, t)
    U = quat(sample_ball(r, n), unit(n)); g = quat(sample_theta(beta, n), unit(n))
    stay = cls(qmul(U, g)) <= r
    p = stay.mean(); se = math.sqrt(p*(1 - p)/n)
    judge("P1_beta%d" % beta, p >= LB1 - 3*se, dict(r=r, t=t, LB1=LB1, MC=p, SE=se))

# P2
def logI1_lower(b):
    return b + math.log((1 - 1/(2*b))/math.sqrt(2*math.pi*b) - 0.5*math.exp(-b) if b < 700 else (1 - 1/(2*b))/math.sqrt(2*math.pi*b))
def LB(beta):
    r = beta**(-1/3); t = beta**(-5/12)
    lb1 = v(r - t)/v(r)*p_theta_le(beta, t)
    lbee = math.exp(-2*beta*r**4)*lb1**2
    logZ = math.log(2) + logI1_lower(beta) - math.log(beta)
    logcross = math.log(2) + 2*math.log(v(r)) + (beta*math.cos(math.pi - 2*r) - logZ) + (beta - logZ)
    return lbee, lbee - math.exp(logcross), logcross
rows = []
for e in range(4, 17):
    b = 10.0**e; lbee, lbeo, lc = LB(b); rows.append((b, lbee, lbeo, lc))
mono = all(rows[i+1][2] >= rows[i][2] for i in range(len(rows) - 1))
judge("P2_monotone_and_limit", mono and 1 - rows[-1][2] < 0.05,
      dict(table=[dict(beta=b, LBee=x, LBeo=y, log_cross=c) for b, x, y, c in rows]))
for eta in (0.25, 0.1):
    first = next((b for b, x, y, c in rows if y >= math.exp(-eta/4)), None)
    out["P2_first_beta_eta%.2f" % eta] = first; res["measured"] += 1
    print("P2 first decade beta with LBeo >= e^{-eta/4}, eta=%.2f:" % eta, first)

# P3
am = 0.2554; rho = 0.5
for beta in (64, 1024, 16384):
    n = 20000; qual = rho**2/beta <= 0.06
    a = am + (math.pi - 2*am)*rng.random(n)
    U1 = qmul(quat(a, np.tile([0, 0, 1.0], (n, 1))), quat(rho/math.sqrt(beta)*rng.random(n), unit(n)))
    U2 = quat(rho/math.sqrt(beta)*rng.random(n), unit(n))
    u1, u2 = U1[:, 1:], U2[:, 1:]
    w = np.cross(u1, u2); S2 = np.sum(u1**2, 1) + np.sum(u2**2, 1); S = np.sqrt(S2)
    q = np.sum(w**2, 1)/S2; alpha = 2*S*np.sqrt(1 + S2)
    ratio = beta*alpha*q/2/rho**2; a2 = cls(U2)
    ok = qual and ratio.max() <= 1.5 + 1e-12 and a2.max() <= rho/math.sqrt(beta) + 1e-12
    judge("P3_beta%d" % beta, ok, dict(qualifies=qual, max_ratio=float(ratio.max()), max_a2_scaled=float(a2.max()*math.sqrt(beta)/rho)))

# P4
eps = lambda a: 2*np.arcsinh(np.abs(np.sin(a)))
def integ(fn, lo, hi, n=2000001):
    x = np.linspace(lo, hi, n); y = fn(x); return float(np.sum((y[1:] + y[:-1])/2)*(x[1] - x[0]))
cstar = integ(lambda a: np.sqrt(2*eps(a)), 0, math.pi)
out["cstar_quad"] = cstar
for eta in (0.25, 0.1, 0.02):
    half = integ(lambda a: np.sqrt(2*(eps(a) + eta)), 0, math.pi/2)
    full = integ(lambda a: np.sqrt(2*(eps(a) + eta)), 0, math.pi)
    amn = math.asin(math.sinh(eta))
    mono = integ(lambda a: np.sqrt(2*(eps(a) + eta)), amn, math.pi - amn)
    judge("P4_eta%.2f" % eta, abs(2*half - full) <= 1e-9 and full <= cstar + math.pi*math.sqrt(2*eta) + 1e-9,
          dict(two_Psi_half=2*half, cstar_eta=full, L3_bound=cstar + math.pi*math.sqrt(2*eta), monotone_reading_2Psi_end=2*mono))

# P5
Bs = []
for eta in (0.4, 0.2, 0.1, 0.05, 0.02, 0.01):
    amn = math.asin(math.sinh(eta)); s = math.sin(amn); r0 = math.sqrt(eta*s/4); l = r0/3
    Smin = s; epsS = lambda S: 2*math.asinh(S)
    logGmin = -(math.sqrt(1 + Smin**2)/Smin)*(epsS(math.sqrt(2)) + 1)   # worst case over S in [sin a_-, sqrt 2]: use max of each factor
    C = epsS(math.sqrt(2)) + eta + 1
    M2 = -(logGmin + math.log(math.exp(0.75*eta) - 1) - C - math.log(4))
    B = CS + math.pi*math.sqrt(2*eta) + 70*(amn + r0)
    Bs.append(B)
    ok = amn <= math.pi/4 and r0 + 0.1 <= math.pi/2 and l < r0/2
    judge("P5_eta%.2f" % eta, ok, dict(a_minus=amn, r0=r0, ell=l, M2_required=M2, log_inv_eta=math.log(1/eta),
                                       inv_sin_a=1/s, final_bound=B))
judge("P5_bound_decreasing", all(Bs[i+1] < Bs[i] for i in range(len(Bs) - 1)) and Bs[-1] - CS < Bs[0] - CS, dict(B=Bs))

# P6
amn = math.asin(math.sinh(0.25))
judge("P6_E13_covers_Omega", 0.5 <= amn, dict(eta_prime=0.5, a_minus=amn))

out["counts"] = res
with open("asm_check_results.json", "x") as fh:
    json.dump(out, fh, indent=1, default=float)
print(res)
sys.exit(0)
