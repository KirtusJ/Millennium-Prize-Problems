"""Extract SU(2) Wilson-action data from Teper hep-th/9812187 and derive (a)-(e).

Input: ref/text/pNN.txt (pypdf extraction; NN = PDF page index, printed page = NN-1).
Output: results/run<N>.json (new file each run, never overwritten).

PREDICATES (fixed before first run; exit 0 iff all P1-P5 hold, else exit 1):
  P1  Table 10 (PDF p12) parses to exactly 8 rows with 2.2 <= beta <= 2.6,
      every a*sqrt(sigma) having an error in brackets.
  P2  Table 1 (PDF p4) SU(2) column gives 0++ = 3.74 +- 0.12 and 2++ = 5.62 +- 0.26.
  P3  Eq.(2) on PDF p3 is the O(a^2) form m/sqrt(sigma)(a) = m/sqrt(sigma)(0) + c a^2 sigma
      (text contains "ca2σ"), and Appendix A (PDF p11) mentions an extra O(a4) check.
  P4  L*sqrt(sigma) = 8*a*sqrt(sigma) of an 8^4 lattice:
      beta=2.3 (tabulated, single row) lies in [2.90, 3.00];
      beta=2.5 (paper's single preferred value 0.186(3), PDF p11) lies in [1.45, 1.55].
  P5  There exists a pair of tabulated betas (one representative value per beta;
      2.4 -> 0.2673(15), 2.5 -> 0.186(3) as stated on PDF p11) whose ratio of
      a*sqrt(sigma) satisfies |r - 2| < 0.05.
MEASURED ONLY (no pass/fail): all ratios between adjacent-by-0.2 beta pairs, errors.
"""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = lambda n: open(os.path.join(HERE, "ref", "text", f"p{n:02d}.txt"), encoding="utf-8").read()

def parse_table10():
    rows = []
    for line in T(12).splitlines():
        m = re.match(r"^(\d\.\d+)\s+(\d+)\s+(\d\.\d+)\((\d+)\)", line)
        if not m:
            continue
        b, lat, v, e = m.groups()
        dec = len(v.split(".")[1])
        rows.append({"beta": float(b), "lattice_raw": lat, "a_sqrt_sigma": float(v),
                     "err": int(e) * 10 ** (-dec), "pdf_page": 12, "printed_page": 11})
        if float(b) >= 2.85:
            break
    return rows

def main():
    res = {"predicates": {}, "measured": {}}
    rows = parse_table10()
    sel = [r for r in rows if 2.2 <= r["beta"] <= 2.6]
    res["table10_2.2_to_2.6"] = sel
    res["predicates"]["P1"] = len(sel) == 8 and all(r["err"] > 0 for r in sel)

    t1 = T(4)
    p2a = re.search(r"0\+\+ 3\.74±0\.12", t1) is not None
    p2b = re.search(r"2\+\+ 5\.62±0\.26", t1) is not None
    res["predicates"]["P2"] = p2a and p2b
    res["table1_su2"] = {"0++": [3.74, 0.12], "2++": [5.62, 0.26], "pdf_page": 4, "printed_page": 3}

    res["predicates"]["P3"] = ("ca2σ" in T(3)) and ("O(a4)" in T(11))

    # representative values per beta
    rep = {}
    for r in sel:
        rep.setdefault(r["beta"], []).append((r["a_sqrt_sigma"], r["err"]))
    rep = {b: v[0] for b, v in rep.items() if len(v) == 1}
    rep[2.4] = (0.2673, 0.0015)   # PDF p11
    rep[2.5] = (0.186, 0.003)     # PDF p11
    res["representative"] = {str(b): v for b, v in sorted(rep.items())}

    L = {str(b): (8 * rep[b][0], 8 * rep[b][1]) for b in (2.3, 2.5)}
    # alternative per-lattice values at 2.5 (measured only)
    L25_alts = {r["lattice_raw"]: (8 * r["a_sqrt_sigma"], 8 * r["err"]) for r in sel if r["beta"] == 2.5}
    res["L_sqrt_sigma_8^4"] = L
    res["measured"]["L_sqrt_sigma_8^4_beta2.5_per_row"] = L25_alts
    res["predicates"]["P4"] = 2.90 <= L["2.3"][0] <= 3.00 and 1.45 <= L["2.5"][0] <= 1.55

    ratios = {}
    bs = sorted(rep)
    for i, b1 in enumerate(bs):
        for b2 in bs[i + 1:]:
            (x, dx), (y, dy) = rep[b1], rep[b2]
            r = x / y
            ratios[f"{b1}/{b2}"] = (r, r * math.hypot(dx / x, dy / y))
    res["measured"]["ratios"] = ratios
    near2 = {k: v for k, v in ratios.items() if abs(v[0] - 2) < 0.05}
    res["near2"] = near2
    res["predicates"]["P5"] = len(near2) > 0

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    n = 1
    while os.path.exists(os.path.join(HERE, "results", f"run{n}.json")):
        n += 1
    out = os.path.join(HERE, "results", f"run{n}.json")
    with open(out, "x", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res, indent=1))
    print("wrote", out)
    ok = all(res["predicates"].values())
    print("PREDICATES:", res["predicates"], "ALL_PASS" if ok else "SOME_FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
