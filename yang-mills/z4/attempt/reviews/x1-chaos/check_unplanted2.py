"""check_unplanted2.py (v2: v1 failed, scipy absent; quad replaced by trapezoid on [L,L+60], 6e5 intervals, truncation e^{-2(60)^2/pi^2} negligible) -- recompute two referee claims about the UNPLANTED text (x1-chaos, T188).

Predicates (fixed before the first run):
  U1  (referee 1 claim) The note (tun_upper.tex lines 101, 564-565) says: for 100 <= beta <= 4096, with tau=delta=beta^{-1/3},
      the deficit max_{s in [0.1,1]} log max(M_in, A M_out) ranges over [7.33, 14.23]. Predicate U1-note: the computed
      min over the beta range is within 0.01 of 7.33 and the max within 0.01 of 14.23 (tolerance: two-decimal rounding
      in the note). Beta grid: integers 100..4096; s grid: 901 points on [0.1,1].
  U2  (referee 2 claim) The note (tun_lower.tex Prop. E13) says sup Delta_i = O((log b)^{3/2} b^{-1/2}) with L=sqrt(C log b),
      C=1 (assembly). Lemma tails(b) bounds Q by C(Lambda) int_L^inf e^{-2t^2/pi^2+Lambda t} t^2 dt. Predicate U2-note:
      this bound times b^{1/2}/(log b)^{3/2} stays bounded on b in [1e2, 1e40] (it decreases at the end).
      Measured with Lambda = L of the weight scale (Lambda=2.0, a fixed illustrative constant) and C(Lambda)=1.
Output check_unplanted2.json opened with mode "x". No randomness.
"""
import json, math
import numpy as np


def deficit(beta, s):
    tau = delta = beta ** (-1 / 3)
    D = 1 - 1 / (2 * beta) - math.sqrt(2 * math.pi * beta) * math.exp(-beta) / 2
    A = 1 + 2 * s * s + 2 * s * math.sqrt(1 + s * s)
    Min = (((1 - tau) * (1 - 4 * tau) * (1 - 5 * delta**2 / 48)) ** -0.5
           + math.sqrt(2 * math.pi * beta) * math.exp(-beta * (1 - 5 * tau) * (1 - math.cos(delta)))
           + math.sqrt(2 * math.pi * beta) * math.exp(-beta * A * tau / 2)) / D
    Mout = beta * math.sqrt(2 * math.pi * beta) / (2 * D) * math.exp(-beta * tau**2 / 64 * (1 - A**-2) ** 2)
    return math.log(max(Min, A * Mout))

res = {}
ss = np.linspace(0.1, 1, 901)
vals = []
for b in range(100, 4097):
    vals.append(max(deficit(b, s) for s in ss))
vals = np.array(vals)
res["U1_min"] = float(vals.min()); res["U1_min_at_beta"] = int(100 + vals.argmin())
res["U1_max"] = float(vals.max()); res["U1_max_at_beta"] = int(100 + vals.argmax())
res["U1_at_beta100_s1"] = deficit(100, 1.0)
res["U1_at_beta100_worst"] = float(vals[0])
res["U1_note_met"] = abs(res["U1_min"] - 7.33) <= 0.01 and abs(res["U1_max"] - 14.23) <= 0.01

Lam = 2.0
ratios = []
for lb in np.linspace(math.log(1e2), math.log(1e40), 40):
    L = math.sqrt(lb)
    tt = np.linspace(L, L + 60.0, 600001); q = float(np.trapezoid(np.exp(-2 * tt * tt / math.pi**2 + Lam * tt) * tt * tt, tt))
    ratios.append(q * math.exp(lb / 2) / lb**1.5)
res["U2_ratio_first_last"] = [ratios[0], ratios[-1]]
res["U2_ratio_increasing_at_end"] = bool(ratios[-1] > ratios[-2])
res["U2_note_met"] = not res["U2_ratio_increasing_at_end"]
res["U2_Q_exponent_C1"] = -2 / math.pi**2
res["counts"] = {"met": int(res["U1_note_met"]) + int(res["U2_note_met"]),
                 "failed": 2 - int(res["U1_note_met"]) - int(res["U2_note_met"]), "measured_only": 0}
with open("check_unplanted2.json", "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
