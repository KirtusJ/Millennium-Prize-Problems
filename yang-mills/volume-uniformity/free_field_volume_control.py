"""Director Z5 | Yang-Mills | volume-uniformity controls on the free lattice field.

Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada.
Program drafted with assistance from Claude (Anthropic), acting as Director Z5.

WHAT IS COMPUTED
Gaussian lattice field with action (1/2) sum (nabla phi)^2 + (1/2)(m0 a)^2 phi^2 on a
periodic box: N^3 spatial sites with spacing a = L/N, T time sites with the same
spacing. For spatial momentum k the two-point function in time is
  G_k(t) = (1/T) sum_{n=0}^{T-1} exp(2 pi i n t / T) / (4 sin^2(pi n / T) + K^2),
  K^2 = sum_i 4 sin^2(k_i / 2) + (m0 a)^2,
and the transfer-operator energy of the mode is omega with cosh(omega) = 1 + K^2/2,
that is omega = 2 asinh(K/2). Physical energy is omega / a.
Massless case (m0 = 0): the zero mode is not a state of the gap; the gap is the mode
k = (2 pi / N, 0, 0), K = 2 sin(pi / N). Massive case: the gap is k = 0, K = m0 a.
Conventions: N >= 2, T even, t in 0..T; m0 in physical units; zero momentum is
excluded in the massless case and included in the massive case.

PREDICATES (fixed before the first run)
 H  (hypothesis test, per case) the energy read from the pole is the decay rate of
    the summed propagator: G_k(t) * 2 sinh(omega) sinh(omega T / 2) / cosh(omega (t - T/2))
    equals 1 to 1e-25 for t = 0, 1, T/4, T/2 at 40 digits. Basis: 15 guard digits.
    Cases that fail H are listed and excluded below; the number that qualify is reported.
 P1 Massless: N omega(N) < 2 pi for every tested N, and 2 pi - N omega(N) shrinks by a
    factor in [3, 5] at each doubling of N. Basis: the leading correction is of order
    N^-2, giving 4; the window is +-25 per cent and the factors are reported.
    Consequence recorded: physical gap M(N, L) = N omega(N) / L < 2 pi / L for every
    regulator N, so inf over L of M is 0 at every N and in the limit N -> infinity.
 P2 Massive positive control, m0 = 1: M0(a) = (2/a) asinh(a/2) depends on a alone,
    M0(a) >= 2 asinh(1/2) for every tested a <= 1, and 1 - M0(a) shrinks by a factor
    in [3, 5] at each halving of a. Basis as in P1 (correction a^2/24).
    Meaning: a gap bounded below uniformly in L, with a positive continuum value.
Tested: N in {4, 8, 16, 32, 64}; T = 8 N for H; a in {1, 1/2, 1/4, 1/8, 1/16}.

OUTPUT free_field_volume_control_result.json, refused if it exists. No random numbers.
RERUN  python -I free_field_volume_control.py <mpmath site directory>
"""
import json, os, sys
sys.path.append(sys.argv[1])
import mpmath as mp

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "free_field_volume_control_result.json")
if os.path.exists(OUT):
    sys.exit("result file exists; refusing to overwrite")
s = lambda x, n=30: mp.nstr(x, n)
TOL = mp.mpf(10) ** -25

def G(K2, t, T):
    return mp.fsum(mp.cos(2 * mp.pi * n * t / T) / (4 * mp.sin(mp.pi * n / T) ** 2 + K2) for n in range(T)) / T

def h_case(label, K, T):
    w = 2 * mp.asinh(K / 2)
    worst = mp.mpf(0)
    for t in (0, 1, T // 4, T // 2):
        r = G(K * K, t, T) * 2 * mp.sinh(w) * mp.sinh(w * T / 2) / mp.cosh(w * (t - mp.mpf(T) / 2))
        worst = max(worst, abs(r - 1))
    return {"case": label, "T": T, "omega": s(w), "worst_dev": s(worst, 5), "met": bool(worst < TOL)}

res = {"program": "free_field_volume_control.py", "dps": 40, "H": []}
NS = [4, 8, 16, 32, 64]
AS = [mp.mpf(1) / 2 ** j for j in range(5)]
qualN, quala = [], []
for N in NS:
    h = h_case("massless N=%d" % N, 2 * mp.sin(mp.pi / N), 8 * N); res["H"].append(h)
    if h["met"]: qualN.append(N)
for a in AS:
    h = h_case("massive a=%s" % s(a, 6), a, 64); res["H"].append(h)
    if h["met"]: quala.append(a)
res["H_qualify"] = {"massless": qualN, "of_massless": NS, "massive": [s(a, 6) for a in quala], "of_massive": [s(a, 6) for a in AS]}

Nw = [N * 2 * mp.asinh(mp.sin(mp.pi / N)) for N in qualN]
d1 = [2 * mp.pi - x for x in Nw]
f1 = [d1[i] / d1[i + 1] for i in range(len(d1) - 1)]
p1 = len(qualN) >= 2 and all(x > 0 for x in d1) and all(3 <= f <= 5 for f in f1)
res["P1"] = {"N": qualN, "N_omega": [s(x) for x in Nw], "two_pi_minus": [s(x, 12) for x in d1], "factors": [s(f, 8) for f in f1],
             "M_times_L_sup_over_tested_N": s(max(Nw)) if Nw else None, "two_pi": s(2 * mp.pi)}

M0 = [2 / a * mp.asinh(a / 2) for a in quala]
d2 = [1 - x for x in M0]
f2 = [d2[i] / d2[i + 1] for i in range(len(d2) - 1)]
floor = 2 * mp.asinh(mp.mpf(1) / 2)
p2 = len(quala) >= 2 and all(x >= floor for x in M0) and all(3 <= f <= 5 for f in f2)
res["P2"] = {"a": [s(a, 6) for a in quala], "M0": [s(x) for x in M0], "floor_2asinh_half": s(floor), "factors": [s(f, 8) for f in f2]}

h_all = all(h["met"] for h in res["H"])
res["verdicts"] = {"H_all_cases": "MET" if h_all else "FAILED", "P1": "MET" if p1 else "FAILED", "P2": "MET" if p2 else "FAILED"}
with open(OUT, "x", encoding="utf-8", newline="\n") as f:
    json.dump(res, f, indent=1, sort_keys=True); f.write("\n")
print(res["verdicts"]); print("qualify", res["H_qualify"])
print("P1", res["P1"]["N_omega"][-1], res["P1"]["factors"]); print("P2", res["P2"]["M0"], res["P2"]["factors"])
sys.exit(0 if (h_all and p1 and p2) else 1)
