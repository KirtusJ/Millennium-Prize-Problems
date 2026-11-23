"""compare.py -- numerical comparison of coupling ranges (L4, L5). Deterministic, no seed needed.

Sources of the formulas (located by me, pages of the PDFs):
  SZZ  = arXiv:2204.12737, (1.2)-(1.3) p.4: weight exp(N*b*Re sum_p Tr Q_p), SU(N): |b| < 1/(16(d-1)).
  AC   = arXiv:2202.10375, Thm 1.1 p.5: weight exp(-b*sum_p Re(chi(1)-chi(s_p))), d=4,
         b >= (114 + 4 log|G|)/Delta_G, rate (b/2)*Delta_G per lattice unit.  (log taken natural: INFERRED.)
  B4   = OVERALL_DISPOSITION.md: SU(2) Wilson, tanh(beta) <= 1/20; Hamiltonian kappa*lambda <= 1/384.
B4's normalization of the Wilson weight is NOT stated in my inputs, so two conventions are computed:
  conv A: weight exp(beta * Re Tr U_p), Tr unnormalized (Chatterjee's (2.1) convention) -> coefficient of Re Tr is beta.
  conv B: weight exp((beta/2) * Re Tr U_p) (physics beta = 4/g^2 for SU(2)) -> coefficient beta/2.
SZZ's coefficient of Re Tr for SU(2) is 2*b, so SZZ covers coefficient < 2/(16*3) = 1/24.

Predicates (fixed before first run; tolerance 1e-12 = double rounding, for exact identities):
  C1 -ln(tanh 1) rounds to the value in control.txt.
  C2 atanh(1/20) lies in (0.05, 0.0501).
  C3 SZZ bound for SU(N), d=4 equals 1/48 within 1e-12.
  C4 (my expectation) B4's maximal beta lies INSIDE SZZ's range under conv B.
  C5 (my expectation) B4's maximal beta lies OUTSIDE SZZ's range under conv A.
  C6 (my expectation) AC threshold for G=Z2 with the sign character (Delta=2, |G|=2) exceeds 50.
Measured only: the two coverage ratios, AC thresholds for Z2, Z3 (chi faithful 1-dim), the AC rate at threshold.
Result file results/compare.json is never overwritten (exit 3). Exit 0 if all predicates evaluated.
"""
import json, math, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    out = os.path.join(BASE, "results", "compare.json")
    if os.path.exists(out):
        print("exists; refusing to overwrite"); return 3
    r = {}; pred = {}
    ctrl = open(os.path.join(BASE, "control.txt")).read().strip()
    pred["C1"] = f"{-math.log(math.tanh(1)):.6f}" == ctrl
    bmax = math.atanh(1 / 20); r["B4_beta_max"] = bmax
    pred["C2"] = 0.05 < bmax < 0.0501
    szz4 = 1 / (16 * (4 - 1)); r["SZZ_b_max_d4"] = szz4
    pred["C3"] = abs(szz4 - 1 / 48) < 1e-12
    cover = 2 * szz4  # max coefficient of Re Tr for SU(2) under SZZ
    r["SZZ_coeff_ReTr_max_SU2_d4"] = cover
    r["convA_coeff"] = bmax; r["convB_coeff"] = bmax / 2
    r["ratio_convA"] = bmax / cover; r["ratio_convB"] = (bmax / 2) / cover
    pred["C4"] = bmax / 2 < cover
    pred["C5"] = bmax >= cover
    # AC thresholds
    z2 = (114 + 4 * math.log(2)) / 2.0
    z3_delta = 1 - math.cos(2 * math.pi / 3)  # Re(chi(1)-chi(w)) for faithful 1-dim character of Z3
    z3 = (114 + 4 * math.log(3)) / z3_delta
    r["AC_beta_min_Z2"] = z2; r["AC_beta_min_Z3"] = z3
    r["AC_rate_at_threshold_Z2"] = z2 / 2 * 2.0
    r["AC_rate_at_threshold_general"] = "(114+4 log|G|)/2 >= 57 per lattice unit"
    pred["C6"] = z2 > 50
    for k, v in r.items(): print(k, v)
    for k, v in pred.items(): print(k, "MET" if v else "FAILED")
    met = sum(pred.values()); failed = len(pred) - met
    print(f"met {met}, failed {failed}, measured only 6")
    json.dump({"values": r, "predicates": pred}, open(out, "w"), indent=1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
