# p5-fid (T29): fidelity micro-review of paper/ against src/

Control: `control.txt` = 0.272341 (−ln tanh 1). I share a model family with the director and the writers, so my agreement is not independent review. Lean: not used; no Lean result is claimed.

## 1. Verdict table

Verdicts: **FAITHFUL**, **OVERSTATED**, **WRONG**, **OMITTED**, **INCONSISTENT**. "Unsupported by src" means the sentence may be true, but nothing in src/ backs it.

| # | Location (file:line, quoted words) | What the source says | Verdict | Suggested wording |
|---|---|---|---|---|
| 1 | sec_provenance.tex:15 "The paper itself has had the corresponding review (Section~\ref{sec:paperreview})." | sec_paperreview.tex:1 is the placeholder "(to be filled after the review of the assembled paper)" (fidcheck Q10 FAILED: a defect of the target) | **WRONG** | Delete the sentence until the review exists, or write "is under review; Section x.y will record its findings." |
| 2 | sec_provenance.tex:15 "found six wrong and ten overstated sentences, which were corrected" | A1_LEDGER.md:92 "6 wrong, 10 overstated, 3 unsupported and 9 omitted statements … they are corrected above" | **OMITTED** | "…found 6 wrong, 10 overstated, 3 unsupported and 9 omitted statements, which were corrected…" |
| 3 | main.tex:39 "three other working groups … obtained the bound $m_\mu(\beta)\le C\beta^{-1/8}$ … energies of order $\beta^{-1/8}$" | THEOREM_B.md:66 (C4) "m(β) ≤ C·β^(−1/32)·(log(2+β))^(1/16)"; "B4 concurs with the qualitative result and adds low-energy vectors at nonzero momentum" (no order given) | **WRONG** vs src. A later result may exist, but no file in src/ gives the exponent −1/8. | Quote the rate the cited commits contain, with its source. If −1/8 is newer, cite the exact file. |
| 4 | main.tex:39 "One of those groups also reports that the random constant background of Lemma R vanishes, which turns the inequality … into an equality" | Not in any src/ file | **OVERSTATED** (unsupported by src) | Keep only with a locator in RepoThread, or delete. |
| 5 | main.tex:39 "its author has not read their proofs" | THEOREM_B.md:66 "The director has not read C4's proof." | **OVERSTATED** (misattributed: the source makes the statement about the director, not the author) | "Neither the author nor the director session has read their proofs." |
| 6 | main.tex:30 "It holds, with the same proof, for the gauge group $\U(1)$"; main.tex:36 "Both hold for $\U(1)$ as well" | THEOREM_B.md "Compact U(1) … everything goes through" (a discriminator argument, not a written proof); main.tex:52 says "Nothing is proved about gauge groups other than $\SU(2)$" | **INCONSISTENT** (the paper contradicts itself) and **OVERSTATED** | "The argument is expected to go through for U(1) (Section …); we have not written it." |
| 7 | sec_provenance.tex:18–19 Codex checks "as it stood at commit 34f97d2 … one of them derived the asymptotics … and recomputed the constant in the tail bound" | No src/ file mentions Codex, a second lineage, or commit 34f97d2 | **OVERSTATED** (unsupported by src). The phrase "recomputed the constant in the tail bound" also takes the second-lineage scope beyond Lemma R, the Wick inequality and the free correlation (brief item 4). | Give the exact RepoThread comment. Either drop "and recomputed the constant in the tail bound", or add the tail constant to the stated scope with its locator. |
| 8 | main.tex:41 "Lemma~\ref{pf:lem-R} and the asymptotics of $G$ were checked … by sessions of a second model lineage" | Same as row 7 | **OVERSTATED** (unsupported by src) | Same as row 7. Also name the Wick inequality, so that the disclosure matches sec_provenance. |
| 9 | sec_provenance.tex:10 "Theorem~\ref{thm:reduction}: one challenge. The proof stood. Eight statements around it were wrong and were corrected" | a2-chalR: "STANDS 16 / DEFECT 8 / NOT CHECKED 1". The 8 defects include "wording", "omissions", "imprecise" and "not admitted plainly". The challenge was of Theorem R with c = 1/2. The paper's Theorem R′ for every c ∈ (0,1) follows chalR item 15's suggestion and was not itself challenged. | **OVERSTATED** (two points: "wrong" for defects of wording and omission; and the challenged version is not the printed one) | "Eight defects (in remarks, wording and the table) were found and corrected. The printed form with general c follows the challenger's remark and was not re-challenged." |
| 10 | sec_provenance.tex:11 "The second found a mislabelled test and a quantifier missing from one statement." | a8-chalB2: "STANDS 12, DEFECT 2, NOT CHECKED 2". Row 13 also lists two undefined symbols. The DLR-in-the-limit step and the S2 Lean check were not checked. | **OMITTED** | Add: "…and two undefined symbols; it did not check the DLR-in-the-limit details or rerun the Lean file." |
| 11 | sec_provenance.tex:11 "The third … found no failing line." | a9-chalL34: 11 stand, "1 DEFECT (non-fatal, η not explicit)". Lemma D and Lemma G were not re-audited, and the Lean file L34.lean was "not rerun". | **OMITTED** | "…found no failing line, one declared non-fatal defect (a constant not explicit); it did not re-audit Lemmas D and G or rerun L34.lean." |
| 12 | sec_provenance.tex:13 "Theorem~\ref{thm:conditional}: one challenge. The statement stood. One step of the proof used positivity…" | c2-chalS: "12 STANDS, 3 DEFECT, 2 NOT CHECKED". The other two defects are of wording (the free-field test is of an analogue) and of status lines. The unchecked items are the discriminators and joint satisfiability. | **OMITTED** (the step-8 claim itself is faithful) | "…three defects (the positivity step, repaired; two of wording and status, corrected); the 2D Ising discriminator was not checked." |
| 13 | sec_provenance.tex:10–11 "a circular gauge fixing, which was repaired, and could not check a classification of Gibbs states, which the second version avoids" | a5-chalB: 17/1/1, defect A3(ii′), NOT CHECKED S3c(i); THEOREM_B "Challenges" 1 | **FAITHFUL** | — |
| 14 | sec_provenance.tex:28 Lean row "Finite-sum inequalities in the proof of Theorem~\ref{thm:reduction} (… mean energy, sharp constant $e$) — A1R.L1–L7…" | a2-leanR: L1 is stated with C(1/2) ≤ D·C(1), L5 is "mean energy ≤ 2 log D", L6/L6_sharp' concern the spectral subspace [1,2]. All are for c = 1/2. The printed Theorem R′ is for general c, and the [1,2] constant e does not appear in the printed proof. | **OVERSTATED** | "…for the case c = 1/2 of Theorem R′ (the printed proof for general c is not formalized); L6 concerns a remark not printed here." |
| 15 | sec_provenance.tex:29 "\repo{s2\_gap\_le}, \repo{s2\_power}" | src mentions only `s2_gap_le` (PROOF_B_v2.md:66: "not rerun here"; THEOREM_B: "recompiled by the director") | **OVERSTATED** (s2_power unsupported by src) | Add the locator for s2_power, or drop it. |
| 16 | sec_provenance.tex:24, 41 commits c44e0c8 and 92623fa | Not in src | NOT CHECKED (unsupported by src) | — |
| 17 | sec_provenance.tex:30 "$1-\cos x\ge 2x^2/\pi^2$ on $[-\pi,\pi]$" | L3_L4.md:16 (`one_sub_cos_ge`). fidcheck Q6: 200001/200001 grid points satisfy it. | **FAITHFUL** | — |
| 18 | main.tex:9 abstract "five lattice hypotheses, of which two are proved"; main.tex:36 | A2_LEDGER table H0–H4, with H0 and H2 proved. Child count 5/5 and 2/2, confirmed by my reading of sec_reduction (the status table). | **FAITHFUL** | — |
| 19 | main.tex:9 "five attempted routes … each of which fails" | A1_LEDGER: four routes broken. A2_LEDGER:103: exclusion "tested before any work was put into it and fails in principle". There are 5 subsections in sec:routes. | **FAITHFUL** (the count matches). The 5th "route" was tested in principle, not attempted as a chain. | Optionally "four attempted routes and one argument by exclusion". |
| 20 | main.tex:36 "six properties, each proved or cited" | A1_LEDGER:48 "Six properties are shared, with proof or citation". Child: P1–P6 at sec_negative:426–440. | **FAITHFUL** | — |
| 21 | main.tex:51 "ten standard facts of measure theory without proof or citation" | THEOREM_B lists 10. The child and grandchild count 10 at sec_proof:543–552. sec_proof:554 also uses Weyl's formula, Plancherel and Isserlis without citation. | **OMITTED** (minor) | "…ten standard facts of measure theory, and Weyl's integration formula, Plancherel's theorem and Isserlis' theorem, without proof or citation." |
| 22 | main.tex:23–28 Theorem 1.1 vs sec_proof.tex:9–17 | The inequality, 𝓛_β, O_p, "every n ≥ 1", G(0)=1/2, G>0 and G = π⁻²n⁻⁴+O(n⁻⁶) all agree, and m_μ := −log‖T_μ\|Ω⊥‖ (sec_proof:115) agrees. However, main.tex puts "Consequently sup m_μ → 0" **outside** the theorem environment, while sec_proof:13 recalls it as part of the statement. | **INCONSISTENT** (minor) | Move "Consequently …" inside `\begin{theorem}` in main.tex. |
| 23 | main.tex:28 "$G(0)=\tfrac12$, $G(n)>0$, $G(n)=\pi^{-2}n^{-4}+O(n^{-6})$" | fidcheck Q1–Q4: G(0)=0.5000000000, G(1)=0.0688747458 (a8: 0.0688747), 16/16 positive, π²n⁴G = 1.0202 at n=16 (a5: 1.020), with (π²n⁴G−1)·n² ≈ 5.2–5.9 for n=8..16, consistent with O(n⁻²) relative. Note that sec_proof:486 says the exponentially small terms are not converted into a multiple of n⁻⁶. | **FAITHFUL** | — |
| 24 | sec_reduction.tex:41 / table "(A): gap at every coupling" vs its statement "$m(\beta)>0$ for all $\beta\ge\beta_1$" | A2_LEDGER H1: "m(β) > 0 for all large β" | **INCONSISTENT** (the name does not match the statement); main.tex:30 repeats "at every coupling" | "(A): gap at all large β" (or state it for all β > 0). |
| 25 | sec_reduction.tex:395 "H0 … proved" | A2_LEDGER "Proved (re-derived in this program; literature at abstract level)". sec_reduction:402 cites OS78 (not read) for site RP, while sec_proof Lemma pf:lem-rp re-proves it. | **FAITHFUL**, but the justification at sec_reduction:402 should point to Lemma~\ref{pf:lem-rp}/\ref{pf:lem-limit}, not to OS78 | — |
| 26 | sec_negative.tex:134 "the director's ledger gives −1.1 to −2.3" | A1_LEDGER:28 "between −1.1 and −2.3" | Number **FAITHFUL**. It uses the operational role "director" for an internal document the reader cannot see (brief item 4). | "an earlier summary gives…" |
| 27 | sec_negative.tex:86 "\cite{SZZ23} gives (A) for β<1/12"; :480 "β_c≈1.64"; :485 "0.090±0.003"; :311 "0.562" | A1_LEDGER:27 "β below 1/12"; A2_LEDGER:103 "β = 1.64", "0.090 ± 0.003"; A1_LEDGER:42 "z = 0.56" | **FAITHFUL** (spot checks only) | — |

## Overclaim scan (item 3)

No hits for: verified, resolve, novel, breakthrough, remarkable, clearly, obviously, well known, it is easy to see, we believe, Millennium, prize, Clay. The one exception is the bibliography entry `Repo` (refs.tex:116, repository name "Millennium-Prize-Problems"), which the brief excepts.

Hits that claim too much:
- sec_provenance:15, "has had the corresponding review" (row 1).
- main.tex:41, the second-lineage "checked" (rows 7–8).

Hits that are fine:
- review: main.tex:5, :41, :54 and sec_provenance:6, all used to deny review.
- verifies: sec_provenance:41, qualified ("say nothing about whether a result is right").
- establish: sec_reduction:356 (a quotation of JW) and sec_negative:673 ("no search establishing absence").
- solve: sec_proof:437 (algebraic).
- first: about 18 hits, all ordinal or "first unproved step".

## The disclosure (item 4)

- No sentence presents agreement among same-family sessions as review. main.tex:41 and sec_provenance:6 both say "not independent review".
- **The second-lineage scope is over-stated in one place.** sec_provenance:18 adds "recomputed the constant in the tail bound", which goes beyond Lemma R, the Wick inequality and the free correlation (row 7).
- main.tex:41 names only Lemma R and the asymptotics of G and omits the Wick inequality. That is an inconsistency with the provenance section, not an overclaim.
- **Operational aliases.** No Z4, A4, B4, C4, D4 or G4 appears in the text; they occur only in the bibliography keys RepoB4 and RepoC4. The role word "director" is used at main.tex:41 and sec_provenance:6, :21. The paper defines it at those points, so it is acceptable. At sec_negative:134 it appears as "the director's ledger", a pointer to an internal document (row 26).

## Mechanics (item 5)

Delegated to the child. I reran the compile myself in a scratch copy (check K4, `build_own/`).
- **Overfull boxes wider than 10pt: 3.**
  - 34.41pt, sec_reduction.tex:113–114 (the dispersion relation in the proof of the two-mass observation).
  - 57.50pt, sec_reduction.tex:288–289 (Lemma red:dense (v)).
  - 104.70pt, sec_provenance.tex:24–25 (the Lean paragraph and table).
  - One further box of 3.78pt (sec_proof:135–136) is below the threshold.
- Undefined references or citations: none.
- Duplicate labels: none.
- Bibliography: 31 `\bibitem`, 31 cited keys. None is uncited and none is missing.
- The `\ref` targets I checked resolve to the intended statements: hyp:A/B/C/H0/H3/H4, thm:reduction, thm:conditional, pf:lem-R, pf:sec-standard, sec:paperreview. sec:paperreview resolves, but to an empty placeholder.

## Counts

**Verdict rows:**
- FAITHFUL 9 (rows 13, 17, 18, 19, 20, 23, 25, 26 number, 27)
- OVERSTATED 7 (rows 4, 5, 7, 8, 9, 14, 15)
- WRONG 2 (rows 1, 3)
- OMITTED 5 (rows 2, 10, 11, 12, 21)
- INCONSISTENT 3 (rows 6, 22, 24)
- NOT CHECKED 1 (row 16)

Row 6 is also overstated; it is counted once.

**Predicates of fidcheck.py (final run 2, K3): met 13, failed 1, measured only 17.**
- The failure is Q10, a defect of the target.
- Run 1 (K2) had 4 failures, Q1, Q2 and Q4 among them: my own defect (an arccosh underflow gave 1/sinh 0). Its Q3 "MET" was spurious for the same reason. The file is kept as fidcheck_result1.txt.

**For-all predicates:**
- Q3: 16/16 cases qualify.
- Q6: 200001/200001 cases qualify.

**Tolerances:**
- Q1: 1e-6. The quadrature difference between 120 and 180 nodes is ≤ 1e-15.
- Q2: 1e-6, from a8's print rounding of 5e-8 plus margin.
- Q4: 0.05, my own margin.
- Q5: 1e-4, the printed 4th decimal.
- Q6: 1e-15, float rounding.
- 10pt overfull threshold: from the brief.

## 2. Hypotheses each statement uses, and where stated

- **Theorem 1.1** (main.tex:23):
  - SU(2), Wilson action;
  - periodic boxes of side 2^k, weak limit points 𝓛_β;
  - site-plane reflection positivity (sec_proof Lemma pf:lem-rp);
  - the ten standard facts (sec_proof:539–552), plus Weyl, Plancherel and Isserlis (:554).
- **Theorem R′** (sec_reduction thm:reduction): (A), (B) and (C) with c ∈ (0,1); 0 < T_β ≤ 1.
- **Theorem S** (thm:conditional): H0, H1 = (A), H2 = (B), H3, H4; and the reconstruction theorem as read in KQR21 (red:OS).
- **Fidelity claims:** the source for each is in the table.

## 3. Failed predicates

- **Q10 (run 2).** The paper claims a review that is a placeholder. Defect of the target.
- **Q1, Q2, Q4 (run 1).** My own program defect (arccosh underflow). Q3 in run 1 was spuriously met. Fixed in run 2 with the predicates unchanged.
- **Child.** Its overfull-box file attribution parser failed (its own defect; attributions confirmed by hand), and its status-row regex was loose (its own expectation).

## 4. What I did not check

- The negative-results sections line by line. I spot-checked the curvature table range, the bound 1/12, z(L), 1.64 and 0.090, and the counts; the rest of sec_negative (about 600 lines) is not checked.
- sec:CE content against c1-E and HYPOTHESIS_E.
- The intro sentence "At strong coupling … for every compact gauge group [OS78]" against the source.
- p4-refs bibliography fields.
- Anything outside src/: RepoThread, the Codex checks, and the commits 34f97d2, c44e0c8, 92623fa, 4e29b71 and 16175fe.
- Lean: not run.
- The mathematics of the proofs: I checked only fidelity and arithmetic.

## 5. Delegated questions and outcomes

- **Child T31** (admitted under T29; run as `child-run1`, K1, exit 0, 80 s; released).
  - **Question:** brief item 5 (mechanics) and the item-2 counts: five hypotheses with two proved, five routes, six properties, ten facts.
  - **Control:** the number of `\section` commands, which I counted first as 8. The child answered **8: correct**, graded before reading anything else.
  - **Returned:** 3 overfull boxes wider than 10pt; no undefined or duplicate labels; 31/31 bibliography entries; counts 5/2/5/6/10, all as claimed.
  - **Rerun:** I recompiled independently (K4, same four boxes, same widths) and rescanned bibliography and labels with my own script (31/31, no duplicates).
  - **Not rerun:** I did not rerun its analyze.py. I recounted Q7 (8 sections) in fidcheck and read the items it cites.
  - The child's register verifies PASS.
- **Grandchild T32** (admitted by the child under T31, released).
  - **Question:** independently recount the items of pf:sec-standard.
  - **Control:** the `\input` lines in main.tex = 6. Matched.
  - **Outcome:** 10 items at sec_proof:543–552. That agrees with my own reading.

## 6. Commands to rerun

```
cd /home/user/z4-workers/p5-fid
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$P init pcp --principal principal --principal-name "Kirtus Justus"
$R task-admit $G --by principal --label p5-fid-child --parent T29          # printed/recorded T31
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T31
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
$P check --ws pcp --name fidcheck-run2 --expect-exit 0 --timeout 280 -- python3 fidcheck.py fidcheck_result_NEW.txt paper src   # mode "x": new name each run
cp -r paper build_NEW && $P check --ws pcp --name pdflatex-x2 --cwd build_NEW --expect-exit 0 --timeout 280 -- bash -c "pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex >/dev/null"
grep -n 'Overfull\|multiply\|undefined' build_NEW/main.log
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Register: K1 child-run1 (exit 0), K2 fidcheck run 1 (exit 0, 4 predicates failed), K3 fidcheck-run2 (exit 0), K4 pdflatex-x2 (exit 0).

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- child `$P verify --ws child/pcp`: `result: PASS (…)`
