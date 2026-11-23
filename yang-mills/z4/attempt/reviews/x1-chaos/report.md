# x1-chaos (T188): would a referee of this kind catch a real error in the note?

## 1. Scoring table

Ten referee children were run, all ten that were planned: 8 planted copies and 2 controls. Each child was headless `claude -p --model sonnet` and received only its copy plus the brief's referee instruction for the half that holds the plant. Every child report is kept in `reports/<k>.final.md`; the raw streams are in `reports/<k>.jsonl`.

| copy | plant (kind) | half given | score | evidence (child's words, condensed) |
|---|---|---|---|---|
| 1 | (a) `1-cos θ ≥ θ²/2` in Lemma K, denominator (upper:215) | 1-4 | **MISSED** | "Lemma K and its radial form (lines 195-245) ... stand." The child flagged only the deficit-range number and a notation nit. |
| 2 | (b) `m_0 := 1-e^{-3η/4}` (½ dropped) (lower:661) | 5-8 | **CAUGHT** | DEFECT line 661: "a ≤ e^{-3η/4}=1-2m_0 holds only if m_0=½(...) ... Steps 4-7 do not close." |
| 3 | (c) hypothesis `μ ≥ e^{-η/4}` dropped from Prop. B (upper:788) | 1-4 | **CAUGHT** | DEFECT line 788: "proof needs μ ≥ e^{-η/4} ... line 807." |
| 4 | (d) Ω widened to `a_1 ∈ [a_-/2, π-a_-/2]` (lower:315-316) | 5-8 | **CAUGHT** | DEFECT line 315: "S4 only proved for a_1 ≥ a_- ... L-norm 1_Ω=1_ΩP false ... ansatz (iv) false." This matches every consequence listed in PLANTS.md. |
| 5 | (e) monotone reading `φ ≥ φ_L`, `Ψ(a_1) ≤ Ψ(π/2)` (lower:1039-1040) | 5-8 | **CAUGHT** | DEFECT lines 1039-1042: "holds only for a_1 ≤ π/2 ... use φ ≥ φ_R / the tent form." The child judged the error locally repairable, which is right, since the repair is the original text. It did not say that the unrepaired bookkeeping gives 2c*. |
| 6 | (f) `M = M(η,β)`, `M² = M_A² + log β` (lower:947) | 5-8 | **CAUGHT** | DEFECT line 947: "inconsistent with 'thresholds functions of η alone' ... tail prefactor ~β^{0.6} vs Q ~ β^{-0.2} ... breaks Δ_3, S4, L-sub." |
| 7 | (g) flux prefactor 4 → 2 in statement and proof (upper:829, 839) | 1-4 | **CAUGHT** | DEFECT line 829/839: "1-ςς=2 and both orderings ⇒ 4; contradicts Remark 842 and line 865." |
| 8 | (h) fibre master bound split at `2τ` (upper:504, 506) | 1-4 | **CAUGHT** | DEFECT lines 504-509: "only gives \|W'-w/A\| > (√2-1)√τ ... tail e^{-βA(√2-1)²τ/2}." |
| c1 | control, unmodified | 1-4 | no false alarm on the proofs | Raised three items. The deficit range is a real defect (row R1 below). The "0.15%" figure is a nit. The L4 circularity question was marked unverified by the child, and it is unfounded: the L4 proof, lower lines 179-226, cites no `tu:U-` label. |
| c2 | control, unmodified | 5-8 | no false alarm | Raised line 769, which is a real defect (row R2 below), plus two wording nits. |

**Catch rate: 7 of 8 caught, 0 partial, 1 missed (87.5%).** With n = 8 the 95% Wilson interval is about 53% to 98%. Each plant was run by one referee, once.

**False alarms on the controls:** no invented defect in any proof step. One nit ("0.15%" for 0.139%) and one concern the child itself marked as unverified, which turned out unfounded. Both controls instead found real defects of the unplanted note (rows R1 and R2).

**The kind of error missed:** a wrong justification for a true conclusion. In plant 1 a standard scalar inequality was reversed inside a proof, while the bound it supports, the lower bound on Z, stays true. Five upper-half referees (1, 3, 7, 8, c1) all wrote "Lemma K stands"; referee 1 was the only one holding the plant. These referees check what the lemmas conclude and recompute the numbers. They did not re-verify each textbook step quoted along the way.

**What this implies for the two clean referee reports on the real note.**
- **Gross local errors.** A referee of this kind, given half the note, catches most single local errors that break a stated claim or contradict nearby text (7 of 8 here). Two clean passes are fair evidence against a gross local error of the planted kinds.
- **The test is easier than real errors.** Every plant was freshly inserted, one per copy, and most created a visible inconsistency with untouched lines: plant 2 with line 667, plant 3 with 793, plant 4 with 342 and 786, plant 6 with 967, plant 7 with 843 and 865. Real gaps written consistently by the author have no such seams. So 7 of 8 overstates the catch rate for organic errors.
- **The class of error that gets missed is known:** false justifications whose conclusions are true or plausible.
- **The earlier clean reports missed real defects.** The same kind of referee, run on unplanted text, found real defects in the real note that the two clean reports did not repair. I confirmed three of them myself:
  - R1, the deficit range;
  - R2, line 769;
  - R3, the rate claimed in Prop. E13.
- **Weight to give them.** "Passed with bookkeeping repairs only" is consistent with residual minor defects. It is not evidence that the note is free of them.
- **Not independent.** All of this is within one model family: Opus here, Sonnet referees. It is not independent review.

## 2. Verdict table (rule 9): items checked in this run

Counts per program are given as "met, failed, measured only".

| item | verdict | evidence |
|---|---|---|
| Planted copies are faithful single-plant copies that compile | STANDS | `make_plants.py` (K1): 28 met, 0 failed, 0 measured only. 1-2 lines changed per copy; controls byte-identical; all copies 32 pages. |
| The planted statements are false (plants 1, 2, 7, 8) | STANDS | `verify_plants.py` (K2): 4 met, 0 failed, 0 measured only. Planted `1-cos≥t²/2` holds at 0 of 10,000 points. The flux ratio is 4.000 (2.000 with the planted 2). The true tail is 0.153, against the claimed e^{-4} = 0.018 (MC, seed 1, standard error 8e-4). |
| PLANTS.md was not changed after testing | STANDS | `sha256sum -c plants.sha256`: OK (4a35ba73...). |
| No referee saw PLANTS.md, notes or the original note | STANDS | `extract_reports.py` (K17): E-final 10/10 met, E-leak 10/10 met, tool calls measured only (6-8 per child). |
| R1. Real note, upper:101 and 564-565, "deficit 7.33 to 14.23 for 100≤β≤4096" | DEFECT (cosmetic) | Line 562 defines the deficit as maximised over s; with that definition the range is 8.833 (β=100) to 14.230. The value 7.3304 is the joint minimum at s=0.1 (`check_unplanted2.py` K6, `check_unplanted3.py` K9). Raised by referees 1, 7, 8 and c1. Referee 3 reproduced 7.33 using the joint reading. |
| R2. Real note, lower:769, "2.65+3.61/η < 4.53/η" | DEFECT (aside, not used) | Fails for η ∈ [0.3472, 0.4] (529 of 4000 grid points). The cited bound `sinh η ≤ 1.03η` is too weak: 1.0278η is needed (`check_line769.py` K12). Raised by referees 6 and c2. The implication itself is supported by the note's own numerics. |
| R3. Real note, Prop. E13 (lower:~591), rate `O((log β)^{3/2} β^{-1/2})` with C=1 | DEFECT (rate unproved; only Δ_i→0 is used) | The proof's own bound on Q in Lemma tails(b) decays like β^{-2/π²} = β^{-0.203}. Its ratio to the claimed rate grows without bound (K6, U2). Raised by referee 2. |
| R4. Real note, Lemma L-C (lower:73-74): "continuous and φ≤g a.e. ⇒ everywhere" needs open sets to have positive measure | NOT CHECKED (plausible; harmless for Haar) | Raised by referee 5 only. |
| R5. L4 circularity concern (c1, and the "not checked" lists of referees 7 and 8) | STANDS (no circularity by reference) | The L4 proof, lower:179-226, contains no `tu:U-` reference. I checked references only, not the content. |

Verdict counts: STANDS 5, DEFECT 3, NOT CHECKED 1.

## 3. Hypotheses each statement uses, and where they are stated

- **Catch rate.** One referee per plant; Sonnet children; the brief's instruction verbatim, with the half named as "Sections 1-4 (the file tun_upper.tex)" or "Sections 5-8 (the file tun_lower.tex)", in `prompts/<k>.txt`. Plants are as recorded in PLANTS.md. Scoring is by me against PLANTS.md: CAUGHT means the planted line or its direct consequence was named as a DEFECT.
- **R1.** The deficit is `log max(M_in, A M_out)` of Theorem tu:U-F-master with τ=δ=β^{-1/3}, maximised over s ∈ [0.1,1] as line 562 says. Grid: integer β, 901 values of s. β ≤ 125 lies outside τ < 1/5, which the note itself acknowledges.
- **R2.** The inequality is exactly as printed on line 769.
- **R3.** Lemma tails(b) gives `Q ≤ C(Λ)∫_L^∞ e^{-2t²/π²+Λt}t² dt`, and the assembly sets L = √(C log β) with C = 1 (lower:958). I used Λ = 2 and C(Λ) = 1, which are illustrative. The conclusion concerns the bound, not Q itself, so the rate is unproved rather than shown false.

## 4. Failed predicates

- **K5, `check_unplanted.py`: exit 1.** scipy is not installed. This was **my own defect**. It was rerun as `check_unplanted2.py` (numpy trapezoid) and kept in the register.
- **U1-note (K6): failed.** The cause was partly **my own expectation**: I assumed the s-maximised reading. U1b (K9) showed the 7.33 is the joint minimum. Line 562's own definition makes the note's number wrong, so this is also a **defect of the target**, though a cosmetic one.
- **U2-note (K6): failed. Defect of the target** (R3).
- **L769 (K12): failed. Defect of the target** (R2).
- **Plant 1 scored MISSED.** This is a failure of the review stack, the thing this brief tests, not of my programs.

## 5. What I did not check

- Repeatability: each copy went to one referee, once.
- Whether the referees would catch more than one plant per copy, or plants woven consistently through several lines.
- Referees given the whole note; each got only half.
- R4 (Lemma L-C), and the content of L4 beyond its citations.
- Lean was not used (the READY file exists). The Lean claims of the note were not checked.
- Plants 3, 4, 5 and 6 were checked by argument only (PLANTS.md), not numerically.

## 6. Delegated questions and outcomes, with task ids

Ten referee children, each admitted under T188 and released afterwards (logs in `reports/admit_*.log` and `reports/release_*.log`):

| copy | task | register check | outcome |
|---|---|---|---|
| 1 | T189 | K3 | MISSED |
| 2 | T190 | K4 | CAUGHT |
| 3 | T191 | K7 | CAUGHT |
| 4 | T192 | K8 | CAUGHT |
| 5 | T199 | K10 | CAUGHT |
| 6 | T200 | K11 | CAUGHT |
| 7 | T201 | K13 | CAUGHT |
| 8 | T202 | K14 | CAUGHT |
| c1 | T203 | K15 | no false alarm |
| c2 | T204 | K16 | no false alarm |

The question each child got was: "referee this half; STANDS or DEFECT per numbered statement". I reran the numeric claims I used from the children: R1 (K6, K9), R2 (K12) and R3 (K6).

**Deviations from common rule 7, made because the brief limits each child to its copy and the referee instruction:**
- No known-answer control question was given, so there was no control to grade first.
- No PCP rules were given, and the children have no `child/pcp` register.
- No grandchild instruction was given, and **no grandchild was run**.
- Children ran in `planted/<k>/`, not `child/`. The prompt was fed from `prompts/<k>.txt`, and output was captured as stream-json so it could be audited for leakage.
- Children ran two at a time with a 45 s stagger, appending to one register without file locking. Both verifies pass.

**Register:**
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` (preceded by "guards replayed: 0 problem(s)")

Control: control.txt = 0.272341.

## 7. Commands to rerun

Run from `/home/user/z4-workers/x1-chaos`. The programs refuse to overwrite their outputs (mode "x"), so move away `planted/`, the `*.json` results, `reports/` and `pcp/` first.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name make_plants --expect-exit 0 -- python3 make_plants.py
sha256sum PLANTS.md > plants.sha256      # only after writing PLANTS.md; check with: sha256sum -c plants.sha256
$P check --ws pcp --name verify_plants --expect-exit 0 -- python3 verify_plants.py
mkdir -p reports   # prompts/<k>.txt as in this directory
./run_referees.sh > reports/driver.out 2>&1
#   (per child: $R task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label x1-chaos-child-<k> --parent T188;
#    $P check --ws pcp --name child-run-<k> --cwd planted/<k> --timeout 900 -- bash -c "claude -p --model sonnet
#      --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' --output-format stream-json --verbose
#      < ../../prompts/<k>.txt > ../../reports/<k>.jsonl 2> ../../reports/<k>.err";
#    $R task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T<n>)
$P check --ws pcp --name check_unplanted --expect-exit 0 -- python3 check_unplanted.py      # fails: no scipy (kept)
$P check --ws pcp --name check_unplanted2 --expect-exit 0 -- python3 check_unplanted2.py
$P check --ws pcp --name check_unplanted3 --expect-exit 0 -- python3 check_unplanted3.py
$P check --ws pcp --name check_line769 --expect-exit 0 -- python3 check_line769.py
$P check --ws pcp --name extract_reports --expect-exit 0 -- python3 extract_reports.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
