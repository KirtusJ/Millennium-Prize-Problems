# r14-micro report: fidelity of SPATIAL_FLOW.md (SF) and MATCHED_MEASUREMENT.md (MM) to reports/

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean READY exists; Lean was not used (nothing to formalise).
I checked the summaries against the reports only, not the mathematics in the reports. Director, workers, child, grandchild and I share a model family, so this is not independent review.

## 1. Verdict table

### 1a. Findings (everything not FAITHFUL)

| # | Location (file, section, quoted words) | What the report says (file, quoted words) | Verdict | Suggested wording |
|---|---|---|---|---|
| 1 | SF, intro: "The measurement concerns SU(2) at two and three lattice spacings" | r11-match §4: "a third spacing (e.g. 2.4 with N=9 would need a 9^4, not done)". results_2 = the same 12⁴, β=2.5 run extended to 260 cfgs | **WRONG** | "concerns SU(2) at two lattice spacings" |
| 2 | MM, header: "Two lattice spacings (three in the extension)" | same as #1. The extension adds configurations, not a spacing | **WRONG** | "Two lattice spacings; the fine ensemble was later extended from 160 to 260 configurations" |
| 3 | SF §4: "The bound for t > 0 is correct and nearly empty (10⁻³ to 10⁻¹³ of the value)" | r13-volchal A5: "1e−3 to 2e−2 at t=0.02; 1e−13 to 4e−8 at t=0.1" | **WRONG** (range; arith Q20 FAILED) | "(between 10⁻¹³ and 2·10⁻² of the value)" |
| 4 | SF §7: "One child and one grandchild saved fetched papers and extracted text" | r11-lit §6: child stored `child/fhk.pdf`, `lucini.pdf`, `f.txt`, `l.txt`; r11-match §5: "it saved PDFs/text in child/src". No report says a grandchild did this | **WRONG** (attribution) | "Two children (of r11-lit and r11-match) saved …; r11-match deleted them, r11-lit left them for the tree's owner" |
| 5 | SF §7: "The session's process was restarted once during the extended measurement (see the measurement file)" | MM does not mention a restart; no report mentions one (grep "restart": only this line) | **WRONG** (internal inconsistency between the two files) | Add the restart to MM, or delete "(see the measurement file)" |
| 6 | SF §7: "A worker reported a second child process it had not started; it was another worker's child seen in the process list." | r11-flowbounds §5: "a second process named `child-run1` was started **in my directory** … by a shell I did not open. Its prompt grants WebFetch/WebSearch, it redirects to child_check.log" | **OVERSTATED** (the explanation is the director's and is not supported by the report; the report says the process ran in the worker's own directory) | "r11-flowbounds reported a second `child-run1` process in its directory, which it had not started (WebFetch/WebSearch granted, output to child_check.log). It left no register event, and the results used predate it. The director's explanation (another worker's child) is not checked here." |
| 7 | SF §1.3: "while the magnetic part reproduces 3/(48π²) to 0.25 per cent" | r12-wild table: τ²m = 0.006591, 0.006342, 0.006317, 0.006249 at τ = 1, 4, 8, 16. Verdict row: "−0.25%" at τ = 8 only | **OVERSTATED** (arith Q19: +4.08, +0.15, −0.25, −1.32 %) | "reproduces 3/(48π²) to 0.25 per cent at τ = 8 (+4 % at τ = 1, −1.3 % at τ = 16)" |
| 8 | SF §4: "Consequence for B3: M₁/M₀ ≤ const/√s and M₂/M₀ ≤ const/s are proved under s·Ψ′_b/P_b ≤ θ < 1/7, not otherwise." | r12-vol V3: "Not evaluated numerically"; also "the uniform-in-c form of the U_q bounds used in steps 7 and 8 is written in one line, not checked numerically". r13-volchal: "Step 7–8 scaling … NOT CHECKED beyond data"; U_q uniform-in-c "Not checked" | **OVERSTATED** (also drops the second non-vacuity condition ℓ/√s ≳ 9) | "… are claimed by the builder under θ < 1/7 and ℓ/√s ≳ 9. The challenger did not check steps 7–8 or the uniform-in-c U_q bounds." |
| 9 | SF §3 B2: "The constant is 10⁷ to 10⁹ above the measured error" | r11-flowbounds: 10⁷ to 10⁹ (its f, ℓ = 1). r12-chal A5: "The bound exceeds the true error by 7e4 to 1e15" | **OVERSTATED** (the range is the builder's alone) | "10⁷ to 10⁹ in the builder's cases, 7·10⁴ to 10¹⁵ in the challenger's" |
| 10 | SF §1.2: "(locators as read by the worker and its child, not reread by the director.)" | r11-lit §6: the child's question was "Q4 only" (FHK, LTW numbers). Sakai–Sasaki, Charalambous–Gross, Cao–Chatterjee, CCHS and Lüscher–Weisz were read by the worker alone | **OVERSTATED** (attribution) | "(locators as read by the worker; none of the §1.2 locators was read by its child; not reread by the director)" |
| 11 | SF §1.2: "carried out on three-dimensional space-time by Cao and Chatterjee (… Thm 1.6, 1.16) and by Chandra, Chevyrev, Hairer and Shen" | r11-lit: Thm 1.6 holds "if S_YM(X_n(t)) is tight"; CCHS is "local existence"; not checked "Whether CCHS define a 3D measure". Verdict: "STANDS (as a programme …)" | **OVERSTATED** (mild) | "pursued on three-dimensional space-time (Cao–Chatterjee, conditional on a tightness assumption; CCHS, local existence of the flow on a state space)" |
| 12 | MM, Predicates: "positivity of R at 0, ℓ/6, ℓ/3 met at both spacings" | r11-match: fine R(ℓ/3) = 4.8e-4 ± 1.2e-3 "(0.4 sigma)"; R(l/3) "NOT RESOLVED" | **OVERSTATED** (mild; the predicate counted as met, but positivity at fine ℓ/3 is not resolved) | "… met at both spacings (fine R(ℓ/3) only at 0.4 standard errors, i.e. not resolved)" |
| 13 | MM, scale paragraph: "a mismatch of +3.25(94) per cent, kept as a systematic" | r11-match verdict row: "LTW hep-lat/0307017 Table 1 (0.17680(76) at 2.5115) suggests the mismatch may be ~0" | **OMITTED** | add "a second source (LTW) suggests the mismatch may be close to zero" |
| 14 | MM, Result: "R(ℓ/6) ratio 0.498(54), Q0 ratio 0.972(11), R(ℓ/3) still unresolved" | r11-match supplementary: "R(0) 0.880(25)" (4.8 σ in results_2); "Q0=9.07(10)e-2 (moved +1.3 sigma …: possible incomplete thermalisation after 100 sweeps, or underestimated errors)" | **OMITTED** | add "R(0) ratio moved to 0.880(25); fine Q0 moved +1.3 σ, which the worker reads as possible incomplete thermalisation or underestimated errors" |
| 15 | MM, Reading 4: "3.01(19)√σ (cosh form)" | r11-match: "3.01(19) cosh form, 2.76(22) log form vs 3.74(12): 3.3 sigma low (cosh)" | **OMITTED** (minor) | add "(log form 2.76(22))" |
| 16 | SF §3 B1–B3 (not mentioned) | r11-flowbounds verdict: "PROOF_FREE_BOUNDS 3b–3d (sup\|f̂_b\| route) … DEFECT (of the route, for this purpose) … yields s^(−4), not s^(−5/2)" | **OMITTED** | add "the builder found that the route 3b–3d of PROOF_FREE_BOUNDS gives only s⁻⁴ and replaced it by a Schur/Parseval step" |
| 17 | SF §3 B1/B3 (not mentioned) | r11-flowbounds §4: "The lower bound v₂ ~ s^(−5/2) is measured, not proved, so the 1/√s and 1/s scalings in B3 are proved only up to that step"; D₄, ‖Δ²f²‖₁, sup f, ∫f, ∫f² "measured on a 64³ … grid, not proved" | **OMITTED** | add "B3's s-scaling rests on v₂ ~ s^(−5/2), which is measured only; the constants use grid-measured norms of f" |
| 18 | SF §3 "Challenge … 21 items stand" | r12-chal "What I did not check": S4 bounds, the aliasing lemma proof, the spectral identification text, interval arithmetic. "Lean: nothing was run" | **OMITTED** | add "the aliasing lemma and the spectral identification were used but checked by neither builder nor challenger" |
| 19 | SF §1.3 (r12-wild defect) | r12-wild: "the conclusion is drawn in the free theory only … I did not check whether some subtraction scheme rescues it"; "The transverse electric remainder also diverges"; "Positivity argument for electric observables under spatial flow: NOT CHECKED" | **OMITTED** | add "free theory only; whether a subtraction of the contact term rescues S6″ was not checked" |
| 20 | SF §4 bullets | r13-volchal: "A6 'constants depend on l only through Poisson errors' DEFECT (minor, imprecise)". Verdicts: "STANDS 9, DEFECT 3" | **OMITTED** (one of the three defects) | add "the builder's 'l enters only through Poisson errors' is imprecise (l also enters through Δ = 2π/l and H3, which needs l/√s ≥ 4.6)" |
| 21 | SF §4: "For a bump of width 0.15 … (L/C between 0.19 and 0.35)" | r12-vol: bump width 0.15, L/C 0.26 at s = 0.001. r13-volchal gives 0.35, 0.34, 0.23, 0.19–0.22 for "own f (bump …)" and does not state its bump's width | **OVERSTATED** (mild; this attributes width 0.15 to the challenger's f, which its report does not state) | "For the builder's bump of width 0.15 and the challenger's own bump …" |
| 22 | SF §1.1: "including a check of the projector on 4⁴ by building the coboundary as a matrix" | r11-flowchal not-checked: "The 4^4 check covers only orientation 12" | **OMITTED** (minor qualification) | "… on 4⁴ (orientation 12 only)" |

### 1b. Statements checked and found FAITHFUL (one line each)

| Location | Report evidence | Verdict |
|---|---|---|
| SF §1.1: −0.009864957816795690839…, +0.057333237804766231595…, 45-digit | r11-flowchal T1, T2 | FAITHFUL |
| SF §1.1: negative from 3.50, stays negative to 50, grid 0.05, 1001 points | r11-flowchal T4 (τ* = 3.4968; 1001 of 1001; arith Q13) | FAITHFUL |
| SF §1.1: moment-sequence reason, 8/3, 4/3, 1/(48π²t²), powers 8 and 5 | r11-flowchal T4, T5b, T5c, T6; arith Q18 | FAITHFUL |
| SF §1.2: Sakai–Sasaki PRD 107 034510, Sec. II.B eqs. (3)–(4), Sec. V eq. (13); Lüscher–Weisz Sec. 7, 8.2; no finiteness source | r11-lit items 1, 2, 6, 10 | FAITHFUL |
| SF §1.3: weight 1, 1/b⁴, 1.011/1.0016/1.0006/1.0002 at τ = 1, 4, 8, 16, L = 48, STATEMENT defect 4 | r12-wild table and verdict | FAITHFUL |
| SF §3: B1 hypotheses, V ~ Φ s^(−5/2), B2 form, B3, √π/(640π²) (arith Q11) | r11-flowbounds §2; r12-chal A8 | FAITHFUL |
| SF §3: odd/even N, sides 0.7, 1, 2; 21 stand, 1 text defect; s^(−7/2); 1/√3; ≈60 asymptotic, V/C 118–620 | r12-chal table | FAITHFUL |
| SF §4: L formula, A ≍ s^(−5/2), B′ ≍ s^(−3/2), B′/(As) → 7, 5/8 asymptote (arith Q17 1.7538e-4), 18/18 and 18/18, 1/7, ℓ/√s ≳ 9, K < π/b or N odd, e^(−8π²), Ū₁/L 210–320 vs 34–68, undefined symbols, "B ≥ 0" → "A ≥ 0" | r12-vol, r13-volchal | FAITHFUL |
| SF §6: Lean declaration counts 6, 10 (+2), 6, 2 and contents; "not in Lean" list | r11-flowbounds §2, r12-lean, r12-vol, r12-wild | FAITHFUL (the "+1 auxiliary" of R11Flow is not in the report: NOT CHECKED) |
| SF §7: 9 of 9 controls correct; r12-vol brief control 0.00028061 wrong, child correct (arith Q11); mpmath absent | all nine reports; r12-vol failed predicates; r11-flowchal | FAITHFUL |
| MM: a√σ 0.3690(30), 0.1905(8), FHK Table 3 compilation; sides 2.214, 2.286; +3.25(94) % (arith Q1, Q2) | r11-match, r11-lit item 7 | FAITHFUL |
| MM: √(6s) = 0.29ℓ (arith Q4: 0.2887), s/a² = 0.5, 2.0 | r11-lit Q1 (R_d = √(6τ)) | FAITHFUL |
| MM: control table (0.875486(760), 0.876282 (arith Q10, −1.05 σ), plaquettes, 4.4e-16, 1.1e-5, 5.9e-7, +5.9/+7.5/+5.6, failed +29.6 / 14.4 / 10.0, "five" errors (arith Q15: 4.7)) | r11-match C1–C6 | FAITHFUL |
| MM: jackknife defect, nineteenfold, production unaffected | r11-match §3 | FAITHFUL |
| MM: 2990 and 160 cfgs; table values and ratios 0.913(33), 0.494(67), 0.956(12); 8 blocks, "a quarter" | results_1.txt (0.9128±0.0328, 0.4942±0.0668, 0.9564±0.0121) | FAITHFUL |
| MM: 88, 31, 11 standard errors; R(6 steps) = −2.0(1.1)e-3 within 2 σ | results_1.txt (88.3, 31.2, 10.9); arith Q9 | FAITHFUL |
| MM Reading 2: 4.4 % (3.6 σ), 9 % (2.7 σ), a²/(8s) 0.25 vs 0.0625, c ≈ 0.2, (ℓ ratio)³ = 0.91 (arith Q7: 0.9085), Q0 moved the wrong way | results_1; r11-match §1 | FAITHFUL |
| MM Reading 3: factor two, 7.6 σ; one step in time | results_1 | FAITHFUL |
| MM Reading 4: 3.01(19) (arith Q12: 3.0096), 3.74(12) Teper Table 1, 3.78(7) LTW Table 14 | r11-match, r11-lit item 9 | FAITHFUL |
| MM counts 25, 1, 8 | r11-match §1 | FAITHFUL |
| SF ↔ MM consistency: S6‴ "does not show agreement between spacings at short separation" vs MM Reading 3 | — | consistent |

Verdict counts over the findings table: WRONG 5, OVERSTATED 8, OMITTED 9. As STANDS / DEFECT / NOT CHECKED: the summaries' arithmetic STANDS except one range (#3). The summaries carry DEFECTS in 13 sentences (#1–#12, #21) and omit 9 report items. Items NOT CHECKED are listed in §4.

## 2. Hypotheses each statement uses and where they are stated
- My review assumes that the nine reports and results_1/2.txt in `reports/` are the director's sources, as the brief states.
- Statements in the summaries that cite no worker report (S6‴ text, "S5 (a)–(g)", "variance ∝ b⁻⁵, S1′", "removes 'convergence with a rate: not proved'", director's reruns, "tenth round", `R12Slice.long_weight_one`, R11Flow "+1 auxiliary") rest on files I do not have. I mark them NOT CHECKED.
- Tolerances in arith.py: half a unit of the last quoted digit (the rounding convention of the quoted number), unless its docstring says otherwise.

## 3. Failed predicates (arith.py run1, `result_arith_run1.txt`: 24 met, 5 failed, 3 measured only)
- Q5_R0, Q6_R0, Q6_Rl6, Q8: **my own expectation**. I recomputed from the rounded table values (e.g. 3.42/3.751, 0.042), which gives 0.9128(336), 2.60 σ, 7.54 σ and 89.3 σ. results_1.txt, computed from the unrounded values, prints 0.9128 ± 0.0328, 2.7, 7.6 and 88.3, and the summary quotes exactly those. These are not defects of the target.
- Q20: **defect of the target** (SF §4 range; finding #3).

## 4. What I did not check
- The mathematics and numerics of the reports themselves (outside the brief).
- Files the summaries cite but that are not in `reports/`: FLOW_PROOF.md, FLOW_STRUCTURE.md, STATEMENT.md, THEOREMS_B.md, THEOREM_V.md, the Lean files, the director's register, and the director's reruns and recompilation claims.
- Whether r13-volchal's bump has width 0.15 (#21).
- The literature itself (no network).

## 5. Delegated questions and outcomes
- **Child** (sonnet, `child/`, register check K1 `child-run1`, exit 0, 86 s).
  - Question: arithmetic only, items A1–A15 (numbers and formulas from the summaries).
  - Control: 12·0.1905/(6·0.3690) − 1 in per cent. It answered **3.25: CORRECT**, graded before I read anything else.
  - Returned: a MATCH/MISMATCH table. Its mismatches (R(0) 0.9118, 89.3 σ, 2.6 σ, 7.54/6.98 σ, Q0 4.34 %) all come from the rounded inputs I gave it in PROMPT.txt (e.g. 3.42 instead of 3.424). They agree with my own Q5/Q6/Q8 failures and are not defects of the summaries. It also gave A15 "20 cfgs per block" (160/8); results_1 shows block = 19 with 8 blocks, so the child's figure is naive, not a contradiction.
  - Its predicates were fixed in the docstring, with mode "x". I reran `recompute.py` in `rerun_child/` (K3): report.md and results.json are identical. Child register: `result: PASS`.
- **Grandchild** (the child's Agent sub-agent, `child/grandchild/`).
  - Question: an independent recomputation of the cosh effective mass (A13).
  - Control: r = 2, closed form acosh((1+√3)/2) = 0.8314429. Correct by algebra (2c² − 1 = 2c).
  - Returned: m·a = 1.1110144, m/√σ = 3.0109 with R(2) = 3.65e-3. With R(2) = 3.652e-3 I get 3.0096 (Q12). Both round to 3.01.
  - I reran `solve.py` in `rerun_gc/` (K4): identical output.

## 6. Commands to rerun (from /home/user/z4-workers/r14-micro)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"        # fresh copy only
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name arith-run2 --expect-exit 0 -- python3 arith.py result_arith_run2.txt   # mode "x": new name
mkdir rerun_child2 && cp child/recompute.py rerun_child2/
$P check --ws pcp --name child-rerun2 --cwd rerun_child2 --expect-exit 0 -- python3 recompute.py
mkdir rerun_gc2 && cp child/grandchild/solve.py rerun_gc2/
$P check --ws pcp --name grandchild-rerun2 --cwd rerun_gc2 --expect-exit 0 -- python3 solve.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Register: K1 child-run1, K2 arith-run1, K3 child-rerun, K4 grandchild-rerun (all exit 0).
- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Counts (met, failed, measured only): arith.py 24, 5, 3 (4 of the 5 failures are my own expectation, 1 is a target defect). Child: 27 rows MATCH, 12 MISMATCH (all from the rounded inputs in my prompt), 6 rows report a value with no claim.
