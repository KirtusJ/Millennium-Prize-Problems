# report.md: p6-rev (reviser), task T35

Control: control.txt = 0.272341 (−ln tanh 1). Lean: /home/user/z4-lean/READY exists, but Lean was not used and no Lean result is claimed. I share a model family with the director, the writers and both reviewers, so my agreement is not independent review.

Deliverables:
- paper/: revised in place. It compiles three times with no errors, no undefined references and no overfull boxes, and comes to **45 pages** (43 before). Theorem 1.1 is on PDF p. 1.
- CHANGES.md: per item, the file, the lines and what was done.
- The original sources are kept in orig/paper_before/.

## 1. Verdict table

Each verdict is about the revised text. STANDS means the item is dealt with in the text, checked by my program or by my reading. DEFECT means not done, or a problem remains. NOT CHECKED means not checked by me.

### Referee, section 6

| Item | Verdict | One line of evidence |
|---|---|---|
| R1 U(1) claims (D1) | STANDS | P6: "holds, with the same proof" and "Both hold for U(1)" absent. main.tex:52 and :70 now say the same thing (expected to adapt, not written, known stronger [Guth80, FS82]). |
| R2 §8.7 / false review claim (D2) | STANDS | P6: "has had the corresponding review" and the placeholder are absent. sec_paperreview.tex is 7 lines and ends "It has not been re-reviewed." |
| R3 title and abstract (D3) | STANDS | P11: 4 sentences. The structure result, (G(n)/G(0))², H0–H4 and the AI/no-review status are all present. Sentence 1 is weakened to subsequential limits in finite-dimensional distributions along β_k→∞, as Prop pf:prop-L4 and Lemma pf:lem-R give. |
| R4 Section 7 vs Section 4 (D6) | STANDS | sec_negative.tex:655-665 cites Prop pf:prop-L4(d) and Lemma pf:lem-R and says the colours may be correlated. The χ² computation is for the free part only and is called an illustration. |
| R5 vortex F_4 vs F_2 (D7) | STANDS | P2 met: −0.20±0.47 (β=1.8) and −0.25±1.04 (β=2.4) are recomputed from the table. Both have the predicted sign and are unresolved. "the wrong sign" is absent. The Z_2 convention is given as "not stated in the source". |
| R6 H0 (D8) | STANDS, with one added hypothesis | H0 is restricted to bounded continuous local F in closed half-spaces, all four directions. Lemma pf:lem-limit(2) is extended to every direction and plane, and its proof gives this. Theorem S Step 6 needs continuity of the O_i, which I added to the definition (sec_reduction.tex:130). See §3. |
| R7 Lemma 5.12 (D9) | STANDS | (U1)–(U4); "standing assumption of the paper" absent (P6). (U1) is now a stated hypothesis of the lemma only. |
| R8 Obs 5.3 (D10) | STANDS | P3 met: 32+24=56 (also recounted by the grandchild). S6 is stated with β_0. β=4, 6 are marked as not bearing on it, β≥12 as bearing on it. Per-row counts given, or "not recorded". |
| R9 Obs 5.11 family (D11) | STANDS | P4 met: closed-form moments vs quadrature agree to 6.6e-10, continuity holds, the jump at β=1 holds. |
| R10 Prop 4.14(e) (D12) | STANDS | sec_proof.tex:341: "the σ-field of the limit curvatures outside the box only"; "Ψ:=𝖫F_sh is this fixed linear image of the shell curvature". |
| R11 other groups' results (D13) | STANDS | main.tex:54-55: one paragraph "Related results, not used here", with comment numbers from THREAD_LOCATORS.md, "reported, not proved here", and "Neither the author nor the sessions that wrote this paper have read those proofs". |
| R12 direction sentence, tables (D4) | STANDS | P6: "We prove that it does." absent. P7: Consequently is inside the theorem. Table intro:status follows the theorem, and the notation table is at the end of §2. |
| R13 OS73/OS75 theorem numbers | DEFECT (not done) | The primary sources are not reachable (network limited to the Clay PDF). The text still says "as read in [KQR21]" and "recalled, not read". |
| R14 exclude L=2 (D14) | STANDS | k≥2 or L≥4 at main.tex:16, 67, 85; sec_reduction.tex:7, 11; sec_proof.tex:46, 75, 79, 138. |
| R15 cuts (D15) | STANDS (cuts made); length not reduced | The Ising table and observation are reduced to 2 sentences. The free-field test is 1 paragraph plus a 3-row table. The R′ remark is cut. §5 chatter is removed. Nothing is cut from §4. Pages went from 43 to 45, because the additions required by D3/D4/D10/D11/D13 outweigh the cuts. |

### Referee verdict-table defects 20–32

| Item | Verdict | One line of evidence |
|---|---|---|
| 20 | STANDS | as R6 |
| 21 | STANDS | as R1 |
| 22 | STANDS | as R4 |
| 23 | STANDS | as R7 |
| 24 | STANDS | as R2 |
| 25 | STANDS | as R8 |
| 26 | STANDS | as R5 |
| 27 | STANDS | as R9 |
| 28 (D17) | STANDS | sec_negative.tex:367-374 specifies direction 0 of length 2, six plaquettes and spins in {0,½,1}. The text says this reading of the source is ours. |
| 29 (D17) | STANDS | "No inequality of any kind is known" is absent (P6). It is replaced by "was found in the sources read … no systematic literature search". Obs 6.1 is restated as a checkable implication. Obs 6.2 opens with its status line. |
| 30 | STANDS | Ising calibration cut to two sentences. |
| 31 | STANDS | The direction sentence, Consequently inside the theorem, and the JW quote (p. 6) plus "This is not the mass gap …" are in place. The table of contents moved after the Introduction, so Theorem 1.1 is now on PDF p. 1 (checked with pdftotext). |
| 32 | STANDS | as R3 |

### Fidelity review rows that are not FAITHFUL

| Row | Verdict | One line of evidence |
|---|---|---|
| 1 | STANDS | as R2 |
| 2 | STANDS | sec_provenance.tex:15: "$6$ wrong, $10$ overstated, $3$ unsupported and $9$ omitted" |
| 3 | STANDS | The rate is quoted from comment 7102141403. "three groups" and "Ward identity" are removed. |
| 4 | STANDS | comment 7102652403; "reported, not proved here" |
| 5 | STANDS | "Neither the author nor the sessions that wrote this paper have read those proofs." |
| 6 | STANDS | as R1 |
| 7 | STANDS | sec_provenance.tex:17-19 gives the scope with comment numbers. The tail constant is kept, because comment 7102590992 supports it. |
| 8 | STANDS | main.tex:57-58 names the Wick inequality and gives the scope per comment. |
| 9 | STANDS | "Eight defects (in remarks, wording and the table) … not re-challenged" |
| 10 | STANDS | "two undefined symbols; it did not check the details of the DLR equations in the limit or rerun the Lean file" |
| 11 | STANDS | "one declared non-fatal defect … did not re-audit Lemmas … or rerun … L34.lean" |
| 12 | STANDS | "It found three defects … The discriminators and the joint satisfiability … were not checked" |
| 14 | STANDS | The Lean row covers c=½ and says L6 concerns a remark not printed. "sharp constant e" is removed. |
| 15 | STANDS | s2_power is absent (P6). |
| 16 | NOT CHECKED | Commits c44e0c8 and 92623fa cannot be checked against src/. They are left as printed. |
| 21 | STANDS | main.tex:69 matches sec_proof.tex:554: ten facts plus Weyl, Plancherel and Isserlis. |
| 22 | STANDS | P7 |
| 24 | STANDS | "(A): a gap at all large couplings" everywhere. P6 confirms "gap at every coupling" is absent. |
| 25, 26 (FAITHFUL with notes) | STANDS | The status points to the lemmas. "an earlier summary" replaces "the director's ledger". |

**Verdict counts** (47 rows: 15 + 13 + 19):
- STANDS 45. This includes R6 with an added hypothesis and R15, where the cuts were made but the length grew; the child grades R15 PARTLY.
- DEFECT 1: R13.
- NOT CHECKED 1: fidelity row 16.

**Predicate counts** (revcheck.py, final run 3, K5): **met 9, failed 0, measured only 3**.

Across all runs: run 1 (K1) crashed from my own parser defect after 2 predicates were met; runs 2 (K2) and 3 (K5) each gave 9 met, 0 failed, 3 measured only.

## 2. Hypotheses each statement uses, and where they are stated

- **Theorem 1.1** (main.tex:20-25; sec_proof.tex:10-17):
  - SU(2), d=4, Wilson action;
  - periodic boxes of side 2^k with k≥2, and μ∈𝓛_β;
  - plaquette p_0 spatial at time 0;
  - limits taken box → β → n;
  - the ten standard facts plus Weyl, Plancherel and Isserlis (sec_proof.tex:541-554).
  - Unchanged in content. The only change is that k≥2 now excludes L=2, which changes no limit point.
- **Lemma pf:lem-limit(2)** (sec_proof.tex:94): now for every direction j and every site plane {x_j=c}. It rests on Lemma pf:lem-rp (every j, every reflection plane, L≥4) and on weak continuity for continuous local θF·F.
- **Theorem R′** (sec_reduction.tex:65-74):
  - abstract data with 0<T_β≤1;
  - (A), (B), and (C) with constants c∈(0,1) and K_C.
- **Theorem S** (sec_reduction.tex:191):
  - H0 in its restricted form (sec_reduction.tex:148-150);
  - H1 = (A), H2 = (B), H3 with integer exponent q, H4;
  - site-scalar observables that are now **bounded and continuous** (sec_reduction.tex:130);
  - the reconstruction theorem as read in KQR21, and the recalled description of the reconstructed space (Step 9).
- **Lemma neg:lem-usc**: its own hypotheses (U1)–(U4) (sec_negative.tex:402-407).
- **S6** (sec_negative.tex:91-94): β ≥ β_0, every box, every U with all Re Tr Q_p ≥ 0.
- **Obs neg:obs-usc**: the explicit family ν_β (sec_negative.tex:424-442).

## 3. Failed predicates, and points the director should know

- **revcheck run 1 (K1, exit 1).**
  - Cause: an IndexError in my P3 parser, which matched a caption line containing "periodic". This was **my program's defect**, not the target's.
  - P1 and P2 were met before the crash; the output is kept as revcheck_result1.txt.
  - Fixed in the parser only, with the predicates unchanged; run 2 (K2) met all 9.
- **Not a predicate, but a change of meaning (D8).** Restricting H0 to continuous local F made Theorem S need continuity of the fields O_i: Step 6 applies RP to F_β, an infinite sup-norm-convergent sum. I added "continuous" to the definition of site-scalar observables and redefined 𝒜_+ as a sup-norm closure.
  - Net effect: Theorem S has a weaker hypothesis H0 and a stronger hypothesis on the O_i.
  - The example field, the plaquette sum, is continuous.
  - This revision has not been challenged. sec_provenance.tex:13 says so.
- **D15 did not shorten the paper (43 → 45 pages).** The cuts are as instructed. The new abstract, the two tables, the explicit S6, the spectral family, the related-results paragraph and the reviews summary outweigh them.

## 4. What I did not check

- The mathematics of Section 4 beyond the edited lines. I relied on the referee, and P10 shows that only the 25 edited lines differ.
- Whether the H0 restriction leaves any other use of H0 in Theorem S uncovered. By reading, Steps 3, 4 and 6 and Lemma red:gap are covered: translations and W_4 come from Lemma pf:lem-limit(1), and RP in {t=0} acts on 𝒜_+.
- OS73/OS75 (R13).
- Commits cited in §8.
- RepoThread itself: I used only THREAD_LOCATORS.md.
- The SU(2) and Z_2 Monte Carlo data: only the arithmetic of F_4−F_2 was rechecked.
- The Z_2 convention: I searched src/ only.
- The reading of "2×1×1" (direction 0 of length 2) and of the spins {0,½,1}. It is inferred from 729 = 3^6 and from the printed spins, and the text says so.
- Lean: not used.

## 5. Delegated questions and outcomes

**Child.** Task T42 was admitted under T35 (child_admit.log, event 82), run as check K3 `child-run1` (exit 0, 139 s), and released (child_release.log, event 86).
- Model: sonnet.
- Input: REFEREE.md, FIDELITY.md, CHANGES.md and the revised sources, copied to child/input/. My notes were not given.
- Question: is each of the 15 referee items, and each non-FAITHFUL fidelity row, addressed in the revised text (not merely claimed in CHANGES.md), and do the CHANGES.md citations match?
- Control: the number of required changes in the referee's section 6. Known answer 15; the child answered **15, correct**. I graded this before reading anything else.
- Returned (child/report.md):
  - 33 items: ADDRESSED 30, PARTLY 1 (R15: the free-field section and the Ising part were shrunk, not removed, which is what D15 asked), NOT ADDRESSED 0, DECLARED NOT DONE 2 (R13, fidelity 16).
  - Its predicates: run 1 met 86, failed 7; run 2 met 93, failed 0. Of the 7 failures, 4 were its own windows or expectations, and **3 were defects of CHANGES.md**: wrong main.tex line numbers for item 14 (:79) and fidelity rows 24 and 25 (:41).
- Use: I fixed the three citations and recomputed all main.tex line numbers after the table-of-contents move (CHANGES.md, final section).
- My rerun: I reread check_items2.py, which greps child/input/paper against line windows, and reran it as check K4 `rerun-child-check-items2` with output results_parentrerun.txt. Result: 93 met, 0 failed, identical to its run 2.
  - Its input is the copy taken before the final table-of-contents move. That move changed only main.tex line positions, and my revcheck run 3 covers the final text.
- Limits the child itself states: it ran no compile, no comment-number check and no mathematical check.

**Grandchild.** Task T43 (parent T42) was admitted (event 83) and released (event 84) by the child.
- Control: 7·8+6·4. Known answer 80; it answered **80, correct**.
- Question: recount the sample counts of neg:tab-curv against the claimed 56.
- Result: 32 + 24 = 56. The 20 for program 2 rests on the caption total alone.
- Reruns: the child reran it (check recount-56), and my own revcheck P3 independently gives 32/24/56.

## 6. Register verification

My register pcp/ has checks K1 to K5:
- K1: revcheck-run1, exit 1, my defect.
- K2: revcheck-run2, exit 0.
- K3: child-run1, exit 0.
- K4: rerun-child-check-items2, exit 0.
- K5: revcheck-run3, exit 0.

Verification results:
- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` The line before it gives the register SHA-256 as e9288cd012fec24f….
- `$P verify --ws child/pcp`, last line: `result: PASS (…)`
- The child quotes the same two last lines for its own register.

## 7. Exact commands to rerun (from /home/user/z4-workers/p6-rev)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control, = control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$P init pcp --principal principal --principal-name "Kirtus Justus"
# fetch (only allowed URL), kept outside this directory:
S=/tmp/claude-0/-home-user-z4-workers-p6-rev/af154311-c1e7-4135-ab5a-eec80ddf5192/scratchpad/clay
mkdir -p $S && curl -sS -o $S/yangmills.pdf https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf && pdftotext -layout $S/yangmills.pdf $S/ym.txt
# edits: tools/rep.py FILE tools/e_*.py (exact-replacement scripts, abort on mismatch); original sources in orig/paper_before/
$P check --ws pcp --name revcheck-run3 --expect-exit 0 --timeout 280 -- python3 revcheck.py revcheck_result3.txt paper orig/paper_before $S/ym.txt build_check3
#   (result file and build dir must be new names on each run: mode "x" / fresh copy)
cd paper && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex; cd ..
grep -n '^!\|undefined\|Overfull' paper/main.log
for w in verified reviewed establishes clearly obviously novel remarkable Director Z4 A4 B4 C4 G4; do grep -n -i -w "$w" paper/*.tex; done
$R task-admit $G --by principal --label p6-rev-child --parent T35          # printed T42
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T42
$P check --ws pcp --name rerun-child-check-items2 --cwd child --expect-exit 0 --timeout 200 -- python3 check_items2.py results_parentrerun.txt
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

## 8. Word grep (verified, reviewed, establishes, clearly, obviously, novel, remarkable, Director, Z4, A4, B4, C4, G4)

Nine hits remain, each kept for a stated reason:
- **reviewed** at main.tex:5, main.tex:8, main.tex:73 and sec_paperreview.tex:7. All four deny review ("not reviewed by a mathematician", "has not been independently reviewed", "has not been re-reviewed").
- **director** at main.tex:58, sec_provenance.tex:6 and sec_provenance.tex:21. This is the operational role, defined at those points. The fidelity review called it acceptable, and the "director's ledger" pointer is gone.
- **z4** at refs.tex:116 and sec_provenance.tex:24. This is the literal folder name `yang-mills/z4/attempt` in the repository path, a locator the reader needs.

There are no whole-word hits for A4, B4, C4 or G4. The bibliography keys RepoB4 and RepoC4 appear only in the source, not in the typeset text.
