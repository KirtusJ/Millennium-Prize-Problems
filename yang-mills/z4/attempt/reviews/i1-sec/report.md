# report — i1-sec (task T99): section "A lower bound at fixed volume, and why it does not reach Hypothesis (A)"

Control: `control.txt` = 0.272341 (−ln tanh 1), written first. Lean: not used; no Lean claim.

Deliverables:
- `paper/sec_smallbox.tex` (label `sec:smallbox`; pp. 47–49 of the compiled 56-page paper);
- `paper/refs_add.tex` (vB00, Lu83, LM84);
- `paper/main_patch.md`.
- The compiled PDF is `paper_with_smallbox.pdf` (main patch items 1–2 applied in a scratch copy; `paper/main.tex` itself is untouched).

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| Section written with the 6 required parts (setting, reported statement + status + ≤25-line sketch, center remark, table, why not (A), false start) | STANDS | Sketch is 4 enumerated steps, ~22 rendered lines. Valley arms are named in Step 2. Displayed claim headed "Reported" (the preamble has no Statement environment). |
| Every number traceable to an input file:line | STANDS (after fix) | `tracecheck.py` K3: 74 cited pairs, 23 numbers with a same-line citation, 0 failures. Child P10 on the corrected text (my rerun K5): 55/55 references exist. |
| My first draft's numerics3.md (and some A4_M1/A4_M0) line citations | DEFECT (mine, fixed) | I had printed numerics2+numerics3 with one `cat -n`, so the numerics3 numbers were offset by 144; the A4_* lines were estimated. The child found l.227/242/272 do not exist. All traces were redone from grep. |
| My draft "It was proved by a session of a second model lineage" | DEFECT (mine, fixed) | The inputs say "written proof", not read by a person (child item 2). Now: "Its proof was written by … and has not been read by a person." |
| My draft "small-volume expansion of Lüscher [Lu83] with the same leading coefficients" | DEFECT (mine, fixed) | Lu83 was read only as an abstract, which gives no numbers (grounding l.29). Now: g^{2/3}/L form from Lu83; the coefficient check is against van Baal eq. (9) (grounding l.9). |
| Brief: center-sector remark "reported, same provenance" | DEFECT of the brief | crossreview.md covers M0 and M1 only (l.1, items 1–30); A4_center.md is not in it. The section says the center result "was not part of the step-by-step check". |
| A3_NOTES l.103 false-start formula 1−K+V ≥ β^{−1/3}(c(\|sin a₁\|+\|sin a₂\|) − C) "is false" | DEFECT of the input record | Read literally with free c, C, it follows from A4_M1 eq. (2) (c∫\|u_i\|\|g\|² ≤ ⟨g,(I−K+V)g⟩ + ch‖g‖², checked as STANDS in crossreview item 12). It is also trivially true for C ≥ 2c. The record omits the scaling that made the suggested form false. The section states the false start in words and does not print the formula, and a source comment says why. |
| Repository path `yang-mills/observable-normalization/one-site-vacuum/` | NOT CHECKED | It comes from my brief, not from the inputs (child item 12); no network. Commits c5c1ea9, 4966c89, dd2927a are from A3_NOTES l.109. \cite{Repo} names a different folder, and the text says so. |
| Table values (2-dir lattice ×β^{1/3}, e₀, e₁, gap, 4^{−1/3} conversions, 3-dir lattice) | STANDS | `numcheck.py` K1 (met 16, failed 0, measured 6). Child P1–P9 met. Grandchild: 1.89778065, 2.26964572. |
| Heuristic L³ rescaling H = (βL³)^{−1/3}h₃ | STANDS (as algebra) | numcheck P7 checks 20 seeded cases. The section labels the derivation heuristic and says it holds for L = 1 only. |
| refs_add.tex | STANDS | Fields are from grounding l.28–30; end pages are not recorded there and not given. The read-in-full / abstract-only marks appear in the text and in the entries. |
| Compile of the whole paper with the section | STANDS | K6 `compile.sh`: 3 passes exit 0, 0 undefined references, 0 overfull > 5 pt, no LaTeX warnings. The only overfull box (2.17 pt, line 20 of an earlier section) is also present in the unpatched paper. |
| main_patch.md items 3, 5, 6 | STANDS (compiled, not recorded) | Applied in a scratch copy: 3 passes exit 0, no undefined references. |

Verdict counts (13 rows): STANDS 7, DEFECT 5 (3 of my own draft, all fixed; 1 of the brief; 1 of the input record A3_NOTES), NOT CHECKED 1.

Predicate counts over my programs: **met 18, failed 0, measured only 6.**
- numcheck: met 16, measured 6.
- tracecheck: 1 predicate pair (T1, T2), met.
- compile1: met.
- Child program rerun by me: old text met 9, failed 1 (P10, a real defect of my draft); new text met 10, failed 0, measured 1.

## 2. Hypotheses each statement uses, and where stated

- **Reported one-site limit.**
  - One spatial site, k = 2 or 3.
  - K normalised (K1 = 1), Wilson increment ∝ e^{β ReTr U/2} against probability Haar measure.
  - T = e^{−V/2}Ke^{−V/2}, center-even gauge-invariant sector, β → ∞ at fixed j.
  - Source: A4_M1.md l.5–12, l.18; A4_M0.md l.9, l.11. Stated in §Setting.
- **Center remark.** All 2^k characters, β large, nontrivial χ (A4_center.md l.5–7).
- **Numbers.**
  - Rayleigh–Ritz for h_k (upper bounds; convergence by basis increase): numerics2 l.14–15, numerics3 l.20, l.89–98.
  - Lattice: Peter–Weyl and Nyström (numerics2 l.12); 3-dir converged only to β ≤ 4 (numerics3 l.18–21).
- **Heuristic.**
  - Constant modes only, small A, T replaced by e^{−H} (not proved for L > 1).
  - Bare vs renormalised coupling equal only at leading order.
  - Source: grounding l.43–53, l.77–81. Stated in §Why.
- **Literature regime.** z = mL ≲ 1 (van Baal pp. 11–12, read in full; Lüscher–Münster abstract): grounding l.17, l.57–58.

## 3. Failed predicates

None in my own programs. Kept and recorded:
- the child's P10 failure on my first draft (K4, exit 1, reproduced identically). This was a defect of my draft, not of the child's expectation.
- the child's v1 program: P10 passed wrongly because its parser skipped comments on table rows. That is the child's own defect, which it found and recorded.

## 4. What I did not check

- The proofs themselves. I checked only that the section describes them as the inputs do.
- Primary literature: no network. vB00, Lu83, LM84 rest on grounding.md.
- The repository path given in the brief.
- `tracecheck.py` T2 only tests numbers on a line that carries a citation, or on the line before a comment line. It covered 23 numbers; the rest of the numbers in the prose were covered by the child's item-by-item check (50 items).
- I did not rerun the grandchild's program; the child reports that it reran it.
- The optional abstract sentence was not compiled.
- No Lean.

## 5. Delegated questions and outcomes

- **Child T105** (admitted under T99, event 206; run as check K2 `child-run1`, exit 0 in 211 s; released, event 210).
  - Question: an independent fidelity check of the finished section and refs_add.tex against the inputs, with a verdict for every number and every attributed statement.
  - Control −ln tanh(1/2): expected 0.771937, answered 0.771937. Graded **PASS** before I read anything else.
  - Outcome: 50 items.
    - FAITHFUL 44 (including 1 marked "faithful to source, argument incomplete": the false start).
    - OVERSTATED 2: "proved by" in the intro; the Lu83 coefficient claim.
    - UNSUPPORTED 1: the repository path.
    - WRONG 1: the numerics3 trace lines.
    - Its report also lists the M1 trace lines as off by 2.
  - All were applied (see §1). For the path I kept the brief's text and gave its source.
  - Reread: I read check_sec_v2.py. Its predicates match its docstring. It contains one dead line in P6 that has no effect.
  - Rerun: K4 on the old text gives an identical result. K5 on the corrected text gives met 10, failed 0.
- **Grandchild T106** (admitted by the child under T105, released by it).
  - Question: from grounding.md and A3_NOTES.md alone, recompute 6.534885·4^{−1/3} against 4.116719735, and convert the two 3-direction gaps.
  - Control −ln tanh 3 = 0.004958: correct, per the child.
  - Outcome: 1.89778065 and 2.26964572. The difference from the published e₀ is within rounding. Not rerun by me.
- Both share my model family. Their agreement is not independent review.

## 6. Commands to rerun (from /home/user/z4-workers/i1-sec; result files use mode "x": move results/ away first)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
mkdir -p results
$P check --ws pcp --name numcheck1 --expect-exit 0 -- python3 numcheck.py results/numcheck1.json
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label i1-sec-child --parent T99          # printed T105
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T105
$P check --ws pcp --name tracecheck1 --expect-exit 0 -- python3 tracecheck.py results/tracecheck1.txt
# child rerun: childrerun/ = child/check_sec_v2.py + child/inputs + child/target (old text); childrerun2/ same with paper/sec_smallbox.tex, paper/refs_add.tex as target/
$P check --ws pcp --name child-rerun-v2-oldtarget --cwd childrerun --expect-exit 1 -- python3 -I check_sec_v2.py
$P check --ws pcp --name child-rerun-v2-newtarget --cwd childrerun2 --expect-exit 0 -- python3 -I check_sec_v2.py
$P check --ws pcp --name compile1 --expect-exit 0 --timeout 300 -- ./compile.sh /tmp/claude-0/-home-user-z4-workers-i1-sec/fa3bc265-caca-4de8-919d-101c30cb287f/scratchpad/build2
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Register checks:

| check | name | exit |
|---|---|---|
| K1 | numcheck1 | 0 |
| K2 | child-run1 | 0 |
| K3 | tracecheck1 | 0 |
| K4 | child-rerun-v2-oldtarget | 1, expected 1 |
| K5 | child-rerun-v2-newtarget | 0 |
| K6 | compile1 | 0 |

- `$P verify --ws pcp`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Recommendation in main_patch.md: abstract NONE. The result is by another lineage, holds at fixed volume in one sector, and the section shows it gives nothing for (A); an alternative sentence is supplied if the author disagrees.
