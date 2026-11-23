"""r12-wild: electric vs magnetic density of the free U(1) lattice gauge field under SPATIAL flow vs FULL 4D flow.

Definitions (lattice units, periodic L^4, k=0 removed): D_mu=e^{ik_mu}-1, q_mu^2=4sin^2(k_mu/2), A=sum q^2, p^2=spatial part.
Feynman covariance delta/A. theta_{mu nu}=D_mu a_nu - D_nu a_mu.
Spatial flow: a_i -> (P_T e^{-tau p^2} + P_L) a_i, a_4 unflowed (flowchal's reading: gradient of spatial-plaquette action).
Full flow: a -> (P_T4 e^{-tau A} + P_L4) a (4D).
e = (1/L^4) sum_k sum_i <|theta_i4|^2>,  m = (1/L^4) sum_k sum_{i<j} <|theta_ij|^2>.
Exact per-mode expressions (derived; checked by explicit covariance matrix on random modes, predicate P0):
  spatial: m=2p^2/A e^{-2tau p^2}, e=2q4^2/A e^{-2tau p^2}+1 (p!=0), e=3 (p=0,k4!=0); full: m=2p^2/A f^2, e=3f^2-m, f=e^{-tau A}.
  Closed forms are checked against explicit covariance matrices on random modes (P_formula, tol 1e-12, roundoff).
Physical reading: t = tau b^2 fixed, b->0 means tau->inf; t^2<density>_phys = tau^2 * (lattice density).

PREDICATES (fixed before first run):
 P0  per-mode matrix computation of longitudinal electric part equals 1 to 1e-12 for 200 random modes with p!=0 (seed 12).
     Tolerance: float64 roundoff.
 P1  spatial flow: tau^2*m(tau) at tau=8 and tau=16 (L=48) within 10% of continuum 1/(16 pi^2)=0.0063326.
     Tolerance: O(1/tau) lattice corrections (~1/8) and finite volume; 10% is my own estimate.
 P2  spatial flow: e(tau) >= 0.99 for every tau in {1,2,4,8,16} (L=48). Source: longitudinal part =1 per mode with p!=0,
     fraction of p=0 modes is 1/L^3, transverse part >=0.
 P3  spatial flow: tau^2*e(tau) / (tau^2*m(tau)) grows: ratio(16)/ratio(4) >= 10 (expected ~16 if m~1/tau^2, e~const).
 P4  full 4D flow control: tau^2*(e+m) at tau=8,16 within 10% of continuum 3/(32 pi^2)=0.0094989 (= 4*t^2<1/4 F^2> = 4*3/(128pi^2)).
     Same tolerance source as P1.
 M1  measured only: e(tau) - (1 - 1/L^3) (transverse electric remainder) at each tau.
"""
import sys, json, numpy as np
L = int(sys.argv[1]); tag = sys.argv[2]
rng = np.random.default_rng(12)
res = {"L": L, "pred": {}, "data": {}}

def mats(n, tau, mode):
    k = 2*np.pi*np.array(n)/L
    D = np.exp(1j*k)-1
    A = np.sum(np.abs(D)**2); p2 = np.sum(np.abs(D[:3])**2)
    C = np.eye(4)/A  # covariance of a
    F = np.eye(4, dtype=complex)
    if mode == "spatial":
        Ds = D[:3]
        PL = np.outer(Ds, Ds.conj())/p2
        F[:3,:3] = PL + (np.eye(3)-PL)*np.exp(-tau*p2)
    else:
        PL = np.outer(D, D.conj())/A
        F = PL + (np.eye(4)-PL)*np.exp(-tau*A)
    Cf = F @ C @ F.conj().T
    return D, Cf, PL, p2

def theta2(D, Cf, mu, nu):
    v = np.zeros(4, dtype=complex); v[nu] += D[mu]; v[mu] -= D[nu]
    return np.real(v @ Cf @ v.conj())  # <|v.a|^2>

# P0: longitudinal electric part per mode
bad = 0; qual = 0
for _ in range(200):
    n = rng.integers(0, L, 4)
    if np.all(n[:3] == 0): continue
    qual += 1
    k = 2*np.pi*n/L; D = np.exp(1j*k)-1; A = np.sum(np.abs(D)**2); p2 = np.sum(np.abs(D[:3])**2)
    Ds = D[:3]; PL = np.outer(Ds, Ds.conj())/p2
    # a_4 and longitudinal a_i are unflowed; build longitudinal electric vector components
    tot = 0.0
    for i in range(3):
        # theta_i4^L = D_i a_4 - D_4 (PL a)_i ; linear functional on a
        w = np.zeros(4, dtype=complex); w[3] = D[i]; w[:3] -= D[3]*PL[i, :]
        tot += np.real(w @ (np.eye(4)/A) @ w.conj())
    if abs(tot-1) > 1e-12: bad += 1
res["pred"]["P0"] = {"qualifying": qual, "met": qual-bad, "failed": bad}

# vectorized BZ sums (closed forms verified against mats() on random modes below)
n1 = np.arange(L); k1 = 2*np.pi*n1/L; q2 = 4*np.sin(k1/2)**2
Q = np.meshgrid(q2, q2, q2, q2, indexing="ij")
p2 = Q[0]+Q[1]+Q[2]; A = p2+Q[3]
mask = A > 0
Asafe = np.where(mask, A, 1.0); psafe = np.where(p2 > 0, p2, 1.0)
def dens(tau, mode):
    # magnetic: theta_ij involves only transverse spatial part; sum_{i<j}|theta_ij|^2 = p^2 |a_T|^2 ; <|a_T|^2> = 2/A (2 spatial-transverse dirs)
    if mode == "spatial":
        fT = np.exp(-tau*p2); fL = 1.0; f4 = 1.0
        mag = np.where(p2 > 0, p2*2/Asafe*fT**2, 0.0)
        # electric: sum_i |D_i a4 - D4 a_i|^2 = sum_i|D4|^2|a_T,i|^2 (T part) + longitudinal (=1 per mode, p>0) ;
        # cross terms between T and (a4, a_L) vanish (orthogonal, covariance diagonal)
        el = np.where(p2 > 0, Q[3]*2/Asafe*fT**2 + 1.0, 0.0)
        # p=0, k4!=0: theta_i4 = -D4 a_i, a_i unflowed (no spatial gradient) -> sum_i q4^2/A = 3
        el = np.where((p2 == 0) & mask, 3.0, el)
    else:
        f = np.exp(-tau*Asafe)
        # full flow on transverse 4D part: gauge-invariant theta depend only on 4D-transverse part, 3 transverse dirs
        # sum_{mu<nu}|theta|^2 = A |a_T4|^2 = A*3/A f^2 = 3 f^2 ; split: magnetic share p^2/A *? -> compute: total = 3f^2;
        # electric share = sum_i |theta_i4|^2 ; by symmetry of transverse projector: electric = (2 q4^2 + p^2)/A *f^2 ... use check
        tot = np.where(mask, 3*f**2, 0.0)
        mag = np.where(mask, (p2*2 - p2*0)/Asafe*f**2, 0)
        el = tot - mag
    return float(el[mask].sum()/L**4), float(mag[mask].sum()/L**4)

# P_formula: verify closed forms against explicit matrices on random modes
fb = 0; fq = 0
for _ in range(100):
    n = rng.integers(0, L, 4)
    if np.all(n == 0): continue
    for mode in ("spatial", "full"):
        tau = float(rng.uniform(0.1, 3))
        D, Cf, PL, pp = mats(n, tau, mode) if not (mode == "spatial" and np.all(n[:3] == 0)) else (None,)*4
        if D is None: continue
        fq += 1
        e = sum(theta2(D, Cf, i, 3) for i in range(3)); m = sum(theta2(D, Cf, i, j) for i in range(3) for j in range(i+1, 3))
        qq = 4*np.sin(np.pi*np.array(n)/L)**2; P2 = qq[:3].sum(); AA = qq.sum()
        if mode == "spatial":
            fT = np.exp(-tau*P2); m_c = P2*2/AA*fT**2; e_c = qq[3]*2/AA*fT**2 + 1.0
        else:
            f = np.exp(-tau*AA); m_c = 2*P2/AA*f**2; e_c = 3*f**2 - m_c
        if abs(m-m_c) > 1e-12 or abs(e-e_c) > 1e-12: fb += 1
res["pred"]["P_formula"] = {"qualifying": fq, "met": fq-fb, "failed": fb}

taus = [1, 2, 4, 8, 16]
for mode in ("spatial", "full"):
    for t in taus:
        e, m = dens(t, mode)
        res["data"][f"{mode}_tau{t}"] = {"e": e, "m": m, "tau2e": t*t*e, "tau2m": t*t*m}
c_m = 1/(16*np.pi**2); c_tot = 3/(32*np.pi**2)
d = res["data"]
p1 = [abs(d[f"spatial_tau{t}"]["tau2m"]/c_m-1) <= 0.10 for t in (8, 16)]
res["pred"]["P1"] = {"met": sum(p1), "failed": 2-sum(p1), "rel": [d[f"spatial_tau{t}"]["tau2m"]/c_m-1 for t in (8, 16)]}
p2l = [d[f"spatial_tau{t}"]["e"] >= 0.99 for t in taus]
res["pred"]["P2"] = {"qualifying": 5, "met": sum(p2l), "failed": 5-sum(p2l)}
r = lambda t: d[f"spatial_tau{t}"]["e"]/d[f"spatial_tau{t}"]["m"]
res["pred"]["P3"] = {"ratio16_over_ratio4": r(16)/r(4), "met": int(r(16)/r(4) >= 10), "failed": int(r(16)/r(4) < 10)}
p4 = [abs(t*t*(d[f"full_tau{t}"]["e"]+d[f"full_tau{t}"]["m"])/c_tot-1) <= 0.10 for t in (8, 16)]
res["pred"]["P4"] = {"met": sum(p4), "failed": 2-sum(p4), "rel": [t*t*(d[f"full_tau{t}"]["e"]+d[f"full_tau{t}"]["m"])/c_tot-1 for t in (8, 16)]}
res["measured"] = {"M1": {t: d[f"spatial_tau{t}"]["e"]-(1-1/L**3) for t in taus}}
with open(f"result_{tag}.json", "x") as fh: json.dump(res, fh, indent=1)
print(json.dumps(res["pred"], indent=1)); print(json.dumps(res["data"], indent=1)); print(res["measured"])
