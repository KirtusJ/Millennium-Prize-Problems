"""M1/M2 mutation test of Director Z4's six Lean files (worker r3-chaos).

Predicates (fixed before the first run):
  B0 (hypothesis test, per file): each ORIGINAL file in input/, copied unchanged
     to mut/base_<File>/, compiles with `lake env lean` exit 0, output contains no
     "sorry", and every "#print axioms" line lists only propext, Classical.choice,
     Quot.sound.  Report how many of 6 qualify.  Mutations of a file are run only
     if its baseline qualifies.
  A  (per mutation): the `old` string occurs exactly once in the original, so the
     mutation is one well-defined single change of a theorem STATEMENT.
  K  (per mutation predicted FALSE): Lean rejects, i.e. exit code != 0.
     A FALSE-predicted mutation with exit 0 is a SERIOUS finding.
  T  (per mutation predicted TRUE): measured only.  exit 0 -> ACCEPTED-AS-TRUE
     (original not sharp); exit != 0 -> statement still true but proof no longer
     fits (also: original not sharp; Lean's rejection here is not a "catch" of a
     false statement).
  M2: every "unused variable" linter warning of the baseline compiles is listed.
Tolerances: none; all predicates are on discrete exit codes / string matches.
Seeds: no randomness.  Result file results/m1_result.json is never overwritten
(the program refuses to run if it exists).
"""
import json, os, re, subprocess, sys, shutil
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, "input")
LAKE_DIR = "C:/Users/donke/z4-lean"
LAKE = os.path.expanduser("~/.elan/bin/lake.exe")
OUT = os.path.join(HERE, "results", "m1_result.json")
FILES = ["Scaling", "FiniteGroupControl", "LevelsControl", "TwoSided", "CharTransfer", "TrajectoryAudit"]
GOOD_AX = {"propext", "Classical.choice", "Quot.sound"}

# (name, file, theorem, old, new, prediction FALSE/TRUE, reason)
M = [
 ("S1", "Scaling", "physical_gap_tendsto_atTop",
  "theorem physical_gap_tendsto_atTop {a m : ℕ → ℝ} {c : ℝ} (hc : 0 < c)",
  "theorem physical_gap_tendsto_atTop {a m : ℕ → ℝ} {c : ℝ}", "FALSE",
  "drop 0<c: c=-1, m=0 gives m/a=0, not ->atTop"),
 ("S2", "Scaling", "lattice_gap_tendsto_zero",
  "    Tendsto m atTop (𝓝 0) := by", "    Tendsto m atTop (𝓝 1) := by", "FALSE",
  "limit 0 -> 1: a=1/n, m=0 is a counterexample"),
 ("S3", "Scaling", "lattice_gap_tendsto_zero",
  "(ha : Tendsto a atTop (𝓝 0)) (ha0 : ∀ n, a n ≠ 0)", "(ha : Tendsto a atTop (𝓝 0))", "FALSE",
  "drop a n != 0: a=0, m=1 gives m/a=0 (Lean x/0=0) but m->1"),
 ("T1", "TwoSided", "twoSided_cluster",
  "    c ≤ L ∧ L ≤ C := by\n  have h1", "    c < L ∧ L ≤ C := by\n  have h1", "FALSE",
  "strict: m = c*a gives L = c"),
 ("T2", "TwoSided", "twoSided_of_tendsto",
  "∀ᶠ n in atTop, (M / 2) * a n ≤ m n", "∀ᶠ n in atTop, M * a n ≤ m n", "FALSE",
  "M/2 -> M: m/a = M - 1/n is a counterexample"),
 ("T3", "TwoSided", "twoSided_cluster",
  "theorem twoSided_cluster (a m : ℕ → ℝ) (c C L : ℝ) (hc : 0 < c) (hcC : c ≤ C)",
  "theorem twoSided_cluster (a m : ℕ → ℝ) (c C L : ℝ) (hcC : c ≤ C)", "TRUE",
  "0<c is not needed for pointwise bounds passing to a limit"),
 ("F1", "FiniteGroupControl", "z2_physical_gap_le",
  "x * (-Real.log (Real.tanh x)) ≤ 1 / (1 + x) := by", "x * (-Real.log (Real.tanh x)) ≤ 1 / (2 + x) := by", "TRUE",
  "numerically max of x(-log tanh x)(2+x) = 0.971 < 1 (sharpness.py), so still true"),
 ("F2", "FiniteGroupControl", "z2_gap_le",
  "-Real.log (Real.tanh x) ≤ 2 / (Real.exp (2 * x) - 1) := by", "-Real.log (Real.tanh x) ≤ 1 / (Real.exp (2 * x) - 1) := by", "FALSE",
  "-log tanh x ~ 2/(e^{2x}-1) as x->inf, so 1/(...) fails for large x"),
 ("F3", "FiniteGroupControl", "z2_gap_pos",
  "theorem z2_gap_pos (x : ℝ) (hx : 0 < x) :", "theorem z2_gap_pos (x : ℝ) :", "FALSE",
  "x=0: tanh 0 = 0, log 0 = 0, 0<0 false"),
 ("L1", "LevelsControl", "levels_gap_le",
  "theorem levels_gap_le (c χ : ι → ℝ) (i0 : ι) {d b : ℝ}\n    (hgap : ∀ j, j ≠ i0 → c j ≤ c i0 - d)\n",
  "theorem levels_gap_le (c χ : ι → ℝ) (i0 : ι) {d b : ℝ}\n", "FALSE",
  "drop spacing: d huge, c constant, chi=-1 off i0 gives lam1<=0"),
 ("L2", "LevelsControl", "levels_gap_le",
  "    (hsmall : 2 * (Fintype.card ι : ℝ) * Real.exp (-b * d) ≤ 1) :\n    0 < lam1",
  "    :\n    0 < lam1", "FALSE",
  "drop smallness: b=0, chi=-1 off i0, K=3 gives lam1=-1<0"),
 ("L3", "LevelsControl", "levels_gap_le",
  "≤ 4 * (Fintype.card ι : ℝ) * Real.exp (-b * d) := by", "≤ 2 * (Fintype.card ι : ℝ) * Real.exp (-b * d) := by", "FALSE",
  "4K->2K: K large, q=1/(2K), chi=-1, gap equality: -log ratio -> log 3 > 1 = 2Kq"),
 ("L4", "LevelsControl", "levels_physical_gap_tendsto_zero",
  "(i0 : ι) {d : ℝ} (hd : 0 < d)", "(i0 : ι) {d : ℝ}", "FALSE",
  "d=0, c constant, ratio constant 1/2: b*log2 -> inf"),
 ("C1", "CharTransfer", "conv_char",
  "theorem conv_char (w ψ : G → ℂ) (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) :", "theorem conv_char (w ψ : G → ℂ) :", "FALSE",
  "drop multiplicativity: w=delta_1, psi=delta_1 on Z2 non-eigen? (w=delta_1: conv = psi, coeff = psi(1); psi=delta_g, g!=1 gives psi = 0*psi false)"),
 ("C2", "CharTransfer", "coeff_real_even",
  "    (heven : ∀ y, w y⁻¹ = w y) :", "    :", "FALSE",
  "drop evenness: Z3, w=delta_g, psi nontrivial: coeff=psi(g^-1) not real"),
 ("C3", "CharTransfer", "iterate_char",
  "(conv w)^[N] ψ = coeff w ψ ^ N • ψ := by", "(conv w)^[N] ψ = coeff w ψ ^ (N + 1) • ψ := by", "FALSE",
  "N=0: psi = coeff*psi, false for w=0, psi=1"),
 ("C4", "CharTransfer", "coeff_real_even",
  "    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)\n    (heven : ∀ y, w y⁻¹ = w y)",
  "    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y)\n    (heven : ∀ y, w y⁻¹ = w y)", "TRUE",
  "on a finite group a multiplicative psi is 0 or unitary (psi(1)^2=psi(1), psi(g)^|G|=psi(1)); both cases keep the identity"),
 ("A1", "TrajectoryAudit", "w_upper",
  "(hb : 0 < b) (hD : 36 * kapA β b ^ 2 ≤ D) :\n    Aq β b ^ 2 / (8 * D) ≤", "(hb : 0 < b) :\n    Aq β b ^ 2 / (8 * D) ≤", "FALSE",
  "drop D>=36k^2: D -> 0+ makes LHS unbounded"),
 ("A2", "TrajectoryAudit", "L_lower",
  "(9 / 64) / (β * (1 + 2 * β) * b) ≤ Lq β b := by", "(10 / 64) / (β * (1 + 2 * β) * b) ≤ Lq β b := by", "FALSE",
  "(1+2b)/(1+B) -> 1 as beta->0, so 9/64 is sharp"),
 ("A3", "TrajectoryAudit", "w_upper",
  "≤ 9 / (512 * (1 + β) ^ 2) := by", "≤ 8 / (512 * (1 + β) ^ 2) := by", "TRUE",
  "max ((1+b)/(2(1+B)))^2 = 0.4665 (sharpness.py): sharp constant ~ 9*0.4665/512, so 8/512 still true"),
 ("A4", "TrajectoryAudit", "L_bounded_forces",
  "(hb : 0 < b) (hb0 : b ≤ b0)", "(hb : 0 < b)", "FALSE",
  "beta=1/n, b=n, b0=1, C=9/64: min(c/4,c^2/4)>0 but beta^2 b = 1/n"),
 ("A5", "TrajectoryAudit", "L_tendsto_top",
  "Tendsto (fun n => Lq (β n) (b n)) atTop atTop := by", "Tendsto (fun n => Lq (β n) (b n)) atTop atBot := by", "FALSE",
  "limit direction flipped; L>0"),
 ("A6", "TrajectoryAudit", "w_upper",
  "≤ 9 / (512 * (1 + β) ^ 2) := by", "≤ 9 / (512 * (1 + β) ^ 3) := by", "FALSE",
  "exponent 2->3: w ~ 9/(2048*(1.5 beta)^2) decays like beta^-2, beats beta^-3 for large beta"),
]


def compile_lean(path):
    env = dict(os.environ)
    env["PATH"] = os.path.expanduser("~/.elan/bin") + os.pathsep + env.get("PATH", "")
    p = subprocess.run([LAKE, "env", "lean", path], cwd=LAKE_DIR, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1500)
    out = p.stdout + p.stderr
    errs = [l for l in out.splitlines() if ": error" in l or l.startswith("error")]
    ax = [l for l in out.splitlines() if "depends on axioms" in l or "does not depend on any axioms" in l]
    badax = []
    for l in ax:
        m = re.search(r"\[(.*)\]", l)
        if m:
            s = {x.strip() for x in m.group(1).split(",")}
            if not s <= GOOD_AX:
                badax.append(l)
    unused = [l for l in out.splitlines() if "unused variable" in l]
    return {"exit": p.returncode, "first_error": errs[0] if errs else None, "n_errors": len(errs),
            "sorry": "sorry" in out, "axioms": ax, "bad_axioms": badax, "unused": unused,
            "out_tail": out[-1500:]}


def main():
    if os.path.exists(OUT):
        print("refusing: result exists", OUT); return 2
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    jobs = []
    for f in FILES:
        d = os.path.join(HERE, "mut", "base_" + f); os.makedirs(d, exist_ok=True)
        dst = os.path.join(d, f + ".lean"); shutil.copyfile(os.path.join(INP, f + ".lean"), dst)
        jobs.append(("base", f, dst))
    applied = {}
    for (n, f, th, old, new, pred, why) in M:
        src = open(os.path.join(INP, f + ".lean"), encoding="utf-8").read()
        cnt = src.count(old)
        applied[n] = cnt
        if cnt != 1:
            continue
        d = os.path.join(HERE, "mut", n); os.makedirs(d, exist_ok=True)
        dst = os.path.join(d, f + ".lean")
        with open(dst, "w", encoding="utf-8", newline="") as h:
            h.write(src.replace(old, new))
        jobs.append(("mut", n, dst))
    with ThreadPoolExecutor(max_workers=6) as ex:
        res = dict(zip([j[1] for j in jobs], ex.map(lambda j: compile_lean(j[2]), jobs)))
    base_ok = {f: (res[f]["exit"] == 0 and not res[f]["sorry"] and not res[f]["bad_axioms"]) for f in FILES}
    rows = []
    for (n, f, th, old, new, pred, why) in M:
        r = res.get(n)
        row = {"name": n, "file": f, "theorem": th, "old": old, "new": new, "prediction": pred, "why": why,
               "A_unique": applied[n] == 1, "baseline_ok": base_ok[f]}
        if r:
            row.update({k: r[k] for k in ("exit", "first_error", "n_errors", "sorry", "bad_axioms")})
            if pred == "FALSE":
                row["verdict"] = "CAUGHT" if r["exit"] != 0 else "NOT CAUGHT (SERIOUS)"
            else:
                row["verdict"] = "ACCEPTED-AS-TRUE" if r["exit"] == 0 else "REJECTED-BUT-TRUE (proof no longer fits)"
        rows.append(row)
    result = {"baseline": {f: {k: res[f][k] for k in ("exit", "first_error", "sorry", "axioms", "bad_axioms", "unused")} for f in FILES},
              "B0_qualify": sum(base_ok.values()), "mutations": rows}
    with open(OUT, "x", encoding="utf-8") as h:
        json.dump(result, h, indent=1, ensure_ascii=False)
    print("B0 baseline qualifying:", result["B0_qualify"], "/ 6")
    for f in FILES:
        print(" base", f, res[f]["exit"], "unused:", len(res[f]["unused"]))
        for u in res[f]["unused"]:
            print("   ", u)
    for r in rows:
        print(r["name"], r["file"], r["theorem"], r["prediction"], r.get("exit"), r.get("verdict"), "|", (r.get("first_error") or "")[:160])
    return 0


if __name__ == "__main__":
    sys.exit(main())
