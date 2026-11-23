"""verify_plants.py -- numerical confirmation that planted statements are false (x1-chaos, T188).

Predicates (fixed before the first run; each one is a claim that the PLANTED text is wrong):
  V1  (plant 1) 1-cos t >= t^2/2 fails for every t in a grid of (0,pi]  (count cases where planted claim holds: expect 0).
  V2  (plant 2) with m_0 := 1-e^{-3eta/4}: e^{-3eta/4} = 1-2m_0 fails for all eta on grid (expect 0 holds),
      and bar_a(1-x)+bar_a x + m_0 = 1 exactly (no margin) for all x, i.e. the Step-4 bound 1-m_0 is not reached.
  V7  (plant 7) on a random finite symmetric positive kernel with unit g and sign vector s:
      lambda - <sg,Tsg> = 4<g1_A, T g1_Ac> (ratio 4/4 = 1 within 1e-12); the planted factor 2 gives ratio 2.
  V8  (plant 8) for |w/A| = sqrt(tau) (worst case) and |W'|^2 > 2 tau, the Gaussian tail
      P(|W'-w/A| > (sqrt2-1)sqrt tau) = exp(-beta A (sqrt2-1)^2 tau/2) exceeds the claimed exp(-beta A tau/2);
      and a Monte Carlo (seed 1, 2e5 samples, beta A tau = 8) of P(|W'|^2>2tau) exceeds exp(-beta A tau/2) = e^{-4}.
      Tolerance: MC standard error ~ sqrt(p/n); require excess > 5 standard errors.
Seeds fixed (numpy default_rng(1)). Output verify_plants.json opened with mode "x".
"""
import json, math
import numpy as np

res = {}
t = np.linspace(1e-3, math.pi, 10000)
res["V1_cases"] = int(t.size)
res["V1_planted_holds"] = int(np.sum(1 - np.cos(t) >= t**2 / 2))
res["V1_met"] = res["V1_planted_holds"] == 0

eta = np.linspace(1e-4, 0.4, 4000)
m0 = 1 - np.exp(-3 * eta / 4)
res["V2_cases"] = int(eta.size)
res["V2_planted_holds"] = int(np.sum(np.abs(np.exp(-3 * eta / 4) - (1 - 2 * m0)) < 1e-15))
abar = np.exp(-3 * eta / 4)
res["V2_max_abs(bar_a+m0-1)"] = float(np.max(np.abs(abar + m0 - 1)))
res["V2_met"] = res["V2_planted_holds"] == 0 and res["V2_max_abs(bar_a+m0-1)"] < 1e-14

rng = np.random.default_rng(1)
n = 200
Tm = rng.random((n, n)); Tm = (Tm + Tm.T) / 2
w, v = np.linalg.eigh(Tm); g = np.abs(v[:, -1]); lam = w[-1]
s = np.where(np.arange(n) < n // 2, 1.0, -1.0)
lhs = lam - (s * g) @ Tm @ (s * g)
gA = g * (s > 0); gB = g * (s < 0)
res["V7_ratio_lhs_over_4cross"] = float(lhs / (4 * gA @ Tm @ gB))
res["V7_ratio_lhs_over_2cross"] = float(lhs / (2 * gA @ Tm @ gB))
res["V7_met"] = abs(res["V7_ratio_lhs_over_4cross"] - 1) < 1e-12

bAt = 8.0  # beta*A*tau
claimed = math.exp(-bAt / 2)
honest = math.exp(-bAt * (math.sqrt(2) - 1) ** 2 / 2)
N = 200000
sd = 1 / math.sqrt(bAt)  # in units of sqrt(tau): W' = w/A + N(0, 1/(beta A)), tau=1
Wp = np.array([1.0, 0.0]) + sd * rng.standard_normal((N, 2))
p_mc = float(np.mean(np.sum(Wp**2, axis=1) > 2.0))
se = math.sqrt(p_mc * (1 - p_mc) / N)
res.update({"V8_claimed": claimed, "V8_honest_bound": honest, "V8_mc_P(|W'|^2>2tau)": p_mc, "V8_mc_se": se,
            "V8_met": honest > claimed and (p_mc - claimed) > 5 * se})
met = sum(bool(res[k]) for k in ("V1_met", "V2_met", "V7_met", "V8_met"))
res["counts"] = {"met": met, "failed": 4 - met, "measured_only": 0}
with open("verify_plants.json", "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
