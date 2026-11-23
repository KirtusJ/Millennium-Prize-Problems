# a8-micro: micro-review of A1_LEDGER.md, GROUNDING.md and README.md against reports/

Worker a8-micro, Director Z4, 23 Nov 2026. Principal: Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1), written first.
Lean was ready (`/home/user/z4-lean/READY` exists) but I did not use it, so this report makes no Lean claim.
Scope: I checked only how faithfully the three summaries report the files in `reports/` (14 files from 14 workers, plus PROOF_B_v2.md), and the director's own arithmetic. I did not review the mathematics. Line numbers are the file's own.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Overall: does any sentence read as a proved result about 4D Yang–Mills? | STANDS (none does) | Both README l.5 and the ledger's opening say there is no gate and no 4D result. Every "Proved" in the files concerns a lattice/elementary statement or a control. The overstatements below concern how strong individual steps are, not a 4D claim. |
| (C) cross-check arithmetic (ledger l.75) | STANDS except one rounding | q = 0.26979, 0.32254, 0.38509; ξ = 0.72461, **1.00519**, 1.40357; ξ(1−q) = 0.52911, 0.68097, 0.86307; LSQ exponent 0.740 (pairwise 0.77, 0.71). The ledger's "1.00" should read 1.01. |
| Worker count "Fifteen workers" | DEFECT | The list adds up to 3+1+1+5+1+1+1+1 = 14, and reports/ holds 14 worker reports. |
| Chain table row A, "three routes" | DEFECT | §(A) of the ledger and README l.16 both have four routes. |
| Chain table row B | DEFECT | The row describes v1 (three claimed steps, "under challenge now"). §(B) describes v2 (two claimed steps, "unchallenged"). |
| Curvature range "−1.1 and −2.2" | DEFECT | The builder's range is [−2.3, −1.2] (a3-Acurv S6). |
| Several items in the (C) "Proved" list | DEFECT (overstated) | a3-C tags these PROVED (examples), PROVED numerically, and NOT CHECKED. |
| "exactly −1/324" | DEFECT (overstated) | a7-wild §5: "−1/324 and 92/225 are guesses from floats". |
| The remaining numbers in the files (see §2) | STANDS | They match the reports to the digits quoted. |

Counts for the arithmetic predicates: **met 4, failed 1, measured only 2** (Q, P, E and G met; X failed; P with rounded inputs and the pairwise exponents measured only).
Counts for the fidelity findings in §2: WRONG 6, OVERSTATED 10, UNSUPPORTED 3, OMITTED 9, FAITHFUL 20 (spot-checked rows listed).

## 2. Findings: location, what the report says, verdict, suggested wording

### WRONG
| # | location (file, quoted words) | report (file, quoted words) | verdict | suggested wording |
|---|---|---|---|---|
| W1 | A1_LEDGER l.86 "Fifteen workers for the attempt so far" | the listed groups sum to 14; reports/ has a1-att, a1-rig, a1-idx, a2-chalR, a2-leanR, a3-{Acurv,Afs,Avort,B,C}, a4-chalcurv, a5-chalB, a6-Bfull, a7-wild = 14 | WRONG | "Fourteen workers" (or name the fifteenth) |
| W2 | A1_LEDGER l.13 (row A) "Broken on all three routes tried" | the ledger's own §(A) l.46 has a fourth route (a7-wild); README l.16 says "all four routes" | WRONG (internally inconsistent) | "Broken on all four routes tried" |
| W3 | A1_LEDGER l.14 (row B) "A chain with three claimed steps and none missing; under challenge now" | PROOF_B_v2.md l.234 "Remaining CLAIMED: L3 and L4. MISSING: none"; ledger l.62 "unchallenged in this version" | WRONG (stale: describes v1) | "Version 2: two claimed steps (L3, L4), none missing; not yet challenged" |
| W4 | A1_LEDGER l.28 "between −1.1 and −2.2 at every β from 4 to 48" | a3-Acurv S6: "κ_H ∈ [−2.3, −1.2] on every sample"; a4-chalcurv: "between −1.1 and −2.0" (table −2.04) | WRONG (lower end) | "between −1.1 and −2.3 at β = 4, 6, 12, 24, 48" |
| W5 | A1_LEDGER l.75 "ξ ... 0.72, 1.00, 1.40 lattice steps" | recomputed 1/(3.74·0.2660) = 1.0052 | WRONG (rounding; it does not change the conclusion) | "0.72, 1.01, 1.40" |
| W6 | GROUNDING l.22 "Ultraviolet stability in four dimensions (Bałaban, 1985–89)" | a1-rig l.78 "Balaban, UV stability 3D, CMP 102 (1985) ... 3D"; the 4D papers are 1987–89 (l.76–77) | WRONG (dates) | "(Bałaban, 1987–89; abstract level)" |

### OVERSTATED
| # | location | report | verdict | suggested wording |
|---|---|---|---|---|
| O1 | A1_LEDGER l.46 "one amplitude is exactly −1/324" | a7-wild §5 "That the exact values are rational. −1/324 and 92/225 are guesses from floats." (NOT CHECKED) | OVERSTATED | "one amplitude is −0.003086419753 (numerically −1/324)" |
| O2 | A1_LEDGER l.70, under "Proved": "(C) fails exactly when the weight at the bottom of the spectrum is exponentially small" | a3-C Step 10 "PROVED (examples)" | OVERSTATED | "Shown by examples: (C) fails when …" |
| O3 | A1_LEDGER l.71, under "Proved": "The only lower-bound tools available ... are blind to the group" | a3-C Step 11 "NOT CHECKED beyond group-blind RP + Jensen"; "Griffiths/Ginibre ... recollection only" | OVERSTATED | "Not checked: the worker found only group-blind tools (RP log-convexity, Jensen); no correlation-inequality source was read" |
| O4 | A1_LEDGER l.68 "(C′) is false for every lattice-local observable even in the free field" | a3-C Step 4 "PROVED (numerically on the discriminator)", "ξ(1 − C₂(1)/C₂(0)) = 0.963ξ" | OVERSTATED (scope) | "(C′) fails in the free field for the lattice-local observables tested (numerically)" |
| O5 | A1_LEDGER l.75 "In the free field with the slice flow (C′) is a theorem (B3 …)" | a3-C §2 "B3 of SPATIAL_FLOW.md, valid only under s·Ψ′_b/P_b < 1/7 and ℓ/√s ≳ 9 (per its challenge)" | OVERSTATED (drops a qualification) | add "under s·Ψ′_b/P_b < 1/7 and ℓ/√s ≳ 9" |
| O6 | A1_LEDGER l.29 "typical-configuration curvature is positive in open boxes of side up to about √β" | a4-chalcurv: measured only for open L = 4 ("Open boxes larger than L = 4" not checked); "L ≳ √β" is the challenger's argument ("an extrapolation ... not a measurement") | OVERSTATED | "positive in the open 4⁴ box at β ≥ 12; the challenger argues that this persists up to side about √β" |
| O7 | A1_LEDGER l.28 "The mechanism was measured: ... k ≈ 2.5 ... independent of β" | a4-chalcurv A4: ensemble G, "no toron fluctuation in G; 1–2 seeds; one box size per group" | OVERSTATED (drops a qualification) | add "(one-loop ensemble without toron fluctuations, 1–2 seeds)" |
| O8 | A1_LEDGER l.42 "where the true value is flat (1/(2β)) and the drift is thermal" | a3-Afs S4 "constant for U(1)" CLAIMED; P_D FAILED; thermal drift "by the rotor model", "post hoc", residual "1.5 to 2.6σ" | OVERSTATED | "where z is expected to be flat (1/(2β)); a post-hoc rotor model attributes the drift to temperature" |
| O9 | A1_LEDGER l.62 "each of a routine kind"; README l.16 "two routine steps short of a proof" | a6-Bfull: L3 "NOT CHECKED (CLAIMED, outline) ... constants ... not written"; L4 "NOT CHECKED (CLAIMED, bookkeeping) ... stated, not written out". "Routine" is the director's word. | OVERSTATED | "two claimed steps, written only in outline, not checked" |
| O10 | GROUNDING l.12 "Existence by compactness alone is excluded in a footnote." | a1-rig l.50 "Weak existence by compactness is excluded unless other techniques establish properties of the limit" | OVERSTATED (drops "unless") | "Existence by compactness alone is excluded unless other techniques establish the properties of the limit (fn. 2, p. 12)" |

### UNSUPPORTED by the reports
| # | location | report | verdict | suggested wording |
|---|---|---|---|---|
| U1 | GROUNDING l.34 "its author remarks that the needed inequalities are easier in the abelian case" | not found in any file in reports/ (searched "easier", "abelian case") | UNSUPPORTED | delete, or give a locator |
| U2 | A1_LEDGER l.46 "the director reran that program, bytes identical (after first failing ...)" | not in a7-wild; this is the director's own statement | UNSUPPORTED here (cannot be checked from reports/) | point to the register event |
| U3 | A1_LEDGER l.75, the R values, a√σ, "3.74", the B4 audit | the sources (`../fixed-size/MATCHED_MEASUREMENT.md`, `../../transfer-operator/findings-audit/`) are not in reports/ | NOT CHECKED (only the arithmetic was checked) | — |

### OMITTED material
| # | report (file, quoted words) | missing from | verdict | suggested wording |
|---|---|---|---|---|
| M1 | a7-wild §5 "The test refutes positivity of the plaquette-character dual only, not of every dual; a resummation over intertwiners could change the signs"; "The direct d=4 one-site enumeration" not checked (d = 4 holds by embedding) | A1_LEDGER l.46–47, and the list in l.48 | OMITTED | add "(plaquette-character dual only; another positive representation is not excluded)" |
| M2 | a2-chalR "STANDS 16 / DEFECT 8 / NOT CHECKED 1", including #11 "(C) is a statement about locality and nothing else": DEFECT (hierarchy counterexample) and #22 (2D table row); a3-B "A1 §6 discriminator row '2D: (B) true': DEFECT (of the target A1)" | A1_LEDGER row R l.12 ("Proved, challenged") | OMITTED | "Proved; the challenge left R1–R6 standing and found 8 defects in remarks and the discriminator table (incl. the 2D row, found also by a3-B)" |
| M3 | a2-leanR "L8 (measure version): NOT CHECKED" | A1_LEDGER l.12 "inequalities in Lean" | OMITTED (minor) | "the elementary inequalities in Lean; the measure version is not formalized" |
| M4 | a3-Afs P_D FAILED ("z_U1(L) for L = 4, 6 within a factor 2 of 1/(2β)": 0.553, 0.684) | A1_LEDGER l.42 | OMITTED | mention the failed predicate |
| M5 | a3-Avort: SU(2) tested only for "β above 2.4" not checked, boxes ≤ 4⁴; "At β = 2.4, F(4) − F(3) = +1.26 ± 1.05, the wrong direction at 1.2σ"; Tomboulis–Yaffe "which I did NOT read" | A1_LEDGER l.33–34 | OMITTED | "undecided for SU(2) at β ≤ 2.4 on 2⁴ to 4⁴ (at β = 2.4 the difference has the wrong sign at 1.2σ)"; "Tomboulis–Yaffe itself not read" |
| M6 | a3-Acurv "S8 ... CLAIMED: literature from memory, not read"; S9 "not reread" | A1_LEDGER l.30 | OMITTED | add a line saying the later steps S8 and S9 are claimed from memory |
| M7 | a5-chalB A3(i) tightness "STANDS (as argument)"; chessboard theorem "cited from memory (FILS, Biskup), not read"; A3(iv) "abstract level" | A1_LEDGER l.54 ("Seventeen items stand ...") | OMITTED | "seventeen stand (two only as argument, one at abstract level)" |
| M8 | a6-Bfull "Direct-DLR positivity route ... DEFECT of that route"; "Theorem B′ ... weaker than (B) ... (dyadic L, periodic states only)" | A1_LEDGER l.56–62 (the second point is partly there) | OMITTED (minor) | mention the failed alternative route |
| M9 | a1-att "Faizal–Shabir arXiv:2606.19362: DEFECT at the level of strategy (abstract only)", hole (iii); a1-rig: OS78, Lüscher and Bałaban are "ABSTRACT ONLY" | GROUNDING l.35 ("no review found"); GROUNDING l.5 names only Guth, Fröhlich–Spencer, Göpfert–Mack and Borgs as abstract-only, and table rows l.19, l.22 carry no marker | OMITTED | "one claimed full construction, no review found; from its abstract its strategy rests on a strong-coupling expansion, which holds for U(1) (hole iii)"; mark OS78, Lüscher and Bałaban "abstract level" |

### FAITHFUL (spot-checked)
- Curvature: "0 of 24 samples above 1/2"; "+3, +9.6, +23"; SU(3) "2.3 against 2.5; one seed"; "1 − 2β"; "β below 1/12"; "2.5 times the threshold" (c₀ = 0.38–0.40).
- Dual: "4 of 729"; "−0.002892 ± 0.000237"; "2×1×1"; the six properties P1–P6; "search snippets, not read".
- Finite-size: z = 0.56, 2.1, 8.0 (0.562, 2.12, 8.02) and 0.34, 0.55, 0.68.
- (B): "888 of 888"; "24 of 24"; "e⁵¹"; "17 separations"; "Seventeen items stand, one defect, one not checked"; the repair of the gauge fixing; "c₀·n^(−10)"; "every even separation"; "no step is missing".
- (C): the reduction to (C′), the Euclidean-time smearing, "Missing: (C′) for the slice-flowed ... density".
- Grounding: SZZ "|β| < 1/(16(d−1))", "Ricci N/2", "8(d−1)N|β|"; Chatterjee Thm 2.4 / Def 2.3; Adhikari–Cao Thm 1.1 rate (β/2)Δ_G; Chatterjee 2018 p.8; Ito–Seiler r < 1; the 2025–26 arXiv numbers and "one retraction"; the B4 two-sector obstruction (a1-idx (c)1).

## 3. Hypotheses each statement uses, and where they are stated

- (C) cross-check: C(1)/C(0) is identified with "R at one step over R(0)", and ξ = 1/(m₀₊₊a) with m₀₊₊/√σ = 3.74 (ledger l.75; the sources are outside reports/). My program takes these inputs as given.
- The fidelity verdicts assume that the reports in reports/ are the ones the director summarized (GROUNDING l.5, ledger links point to `reviews/…`). I matched them by worker name.

## 4. Failed predicates

- **X** (xcheck_C.py, register K2, exit 1): "|ξ − quoted| ≤ 0.005 for all 3 cases". Result: 2 of 3 qualify. Case 2 gives ξ = 1.00519 against the quoted 1.00. This is a **defect of the target** (a rounding error in the ledger). The tolerance is half a unit in the last quoted decimal. With the rounded inputs the products are 0.526, 0.677, 0.861, so the ledger's 0.53, 0.68, 0.86 come from the unrounded values, which agree.
- K2 was registered with expect-exit 0 and exited 1. That mismatch is kept in the register.

## 5. What I did not check

- The mathematics of every report (outside the brief).
- The sources outside reports/: A1_REDUCTION.md, MATCHED_MEASUREMENT.md, SPATIAL_FLOW.md, the B4 audit, OVERALL_DISPOSITION.md, the `reviews/` links (whether they resolve).
- The director's statements about its own reruns (Lean recompile, a7 rerun).
- That the a1-idx "three places" where a summary reads stronger or weaker are exactly three. I saw the section; I did not count it line by line.
- Every sentence of GROUNDING §3 against the full a1-att text. I checked by grep, so subtler paraphrase drift there may be missed.
- The README file table (A1_REDUCTION.md is not in this directory).

## 6. Delegated questions and outcomes

- **Child** (sonnet, headless, register event child-run1, exit 0 in 37 s). Question: the (C) arithmetic alone (q, ξ, P, exponents).
  - Control: 1/(3.74·0.3690) to three decimals, known answer 0.725. **The child answered 0.725: correct.** I graded this before reading anything else.
  - Returned: q = 0.270, 0.323, 0.385; ξ = 0.725, 1.005, 1.404; P = 0.529, 0.681, 0.863; exponents 0.77, 0.71, 0.74; LSQ 0.74. It reported 0 failed predicates. Its predicates were weaker than mine and did not test the quoted 1.00.
  - My handling: I reread calc.py and reran it in child_rerun/ (register child-calc-rerun, K3). The output is byte-identical to child/result.txt and agrees with my xcheck_C.py to every printed digit.
- **Grandchild** (started by the child in child/grandchild/). Question: an independent recomputation of the three q and the three ξ values.
  - Control: 1.012/3.751, known answer 0.270. **It answered 0.270: correct.**
  - Its q and ξ agree with the child's and with mine (child/grandchild/result.txt). The child says it reran this. I did not rerun the grandchild myself; its numbers are covered by mine.

## 7. PCP OS

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 8. Rerun (from /home/user/z4-workers/a8-micro; result files are opened with mode "x", so give each rerun a new name)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name xcheck-C --expect-exit 0 -- python3 xcheck_C.py result_xcheck_C_2.txt     # exits 1 (predicate X fails)
mkdir child_rerun2 && cp child/calc.py child_rerun2/ && $P check --ws pcp --name child-calc-rerun2 --cwd child_rerun2 --expect-exit 0 -- python3 calc.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Director, worker, child and grandchild are one model family. This is not independent review.
