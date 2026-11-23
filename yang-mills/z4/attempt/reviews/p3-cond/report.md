# p3-cond report (task T21): sec_reduction.tex

Worker p3-cond for Director Z4. Principal: Kirtus Justus. Control: `control.txt` = 0.272341.
I share a model family with the director, the source authors and my child, so this is not independent review.

**Did any step fail to follow?** In the final text, no. I found no step of Theorem R′ or Theorem S that fails to follow from what the text assumes. Two points rest on material I did not read, and the text says so where they occur:
- (i) Step 9 uses the reconstruction theorem as read in KQR, together with the description of the reconstructed space (Ω = [1], e^{−sH}[f] = [f_s]). That description is recalled from OS73 §4 and was not read.
- (ii) E0′ is proved with my own Schwartz norms. I did not compare them with the norms of KQR eq. (9.18).

My first draft overstated in three places, which the child found:
- It said "both theorems are proved in full".
- It cited Lu77 and OS78 as if they had been read.
- It asserted ‖T‖ ≤ 1 without proof.

The first two are now corrected in the text. The third is now attributed to the cited construction of OS78, which is marked as not read and not repeated.

Deliverable: `/home/user/z4-workers/p3-cond/sec_reduction.tex`. The compile test `main_test.tex` gives 12 pages in total. The section runs over pages 1–11 and the bibliography is on page 12. pdflatex was run twice with no errors and no undefined references.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | Theorem R′ (thm:reduction), any c ∈ (0,1): R1–R5 and proof | STANDS | Full proof is in the text. Numerical check N6 ((R2) tail and mean bounds) holds on 3000/3000 random atomic measures. |
| 2 | Remark D ≥ e^{1−c} (√e at c = ½) | STANDS | Two-line proof (μ_β is a probability measure on E ≥ 1). N5 holds 3000/3000, with minimum ratio/e^{1−c} = 1 − 2·10⁻¹⁶. |
| 3 | Observation red:twomass ((C) is not locality alone) | STANDS | Proof is in the text. It uses the free-field dispersion relation, which the text calls standard and does not prove. The child rechecked the inequality. |
| 4 | Theorem S (thm:conditional) statement vs THEOREM_S §3 | STANDS | Child Q1 found the hypotheses H0–H4 and conclusions 1–4 equal to the source. |
| 5 | Step 1 compactness (nearest-point extension + Lemma red:AA) | STANDS | This is my own proof. It differs from the source's piecewise-linear interpolation, and the statement is unchanged. |
| 6 | Step 2 Taylor lemma, E0′ with s = D+6 | STANDS | M = Dk+1, P = 4k+2 (the source has 4k+1). N7 checks the arithmetic 241/241. The child rechecked the constants. |
| 7 | E0′ norms equal to KQR's | NOT CHECKED | I did not read KQR. The text marks this. |
| 8 | Lemma red:dense (closure of ⟨W₄, R_θ⟩ = O(4)) | STANDS | Five-step proof in the text. My N1–N3 hold. The child's q2b was rerun by me (K4) with identical output. |
| 9 | Step 6 reflection positivity (proved on 𝒯 ⊃ ⁰𝒮₊) | STANDS | Proof in the text. |
| 10 | Step 7 gap lemma in the repaired form \|B(s)\| ≤ e^{−s}F_f(0)^{½}F_g(0)^{½} | STANDS | It uses only that T is self-adjoint. The text explains why the monotone form needs T ≥ 0 (Lu77, not used). |
| 11 | Source step 8 in the monotone form | DEFECT (of the source, repaired) | Found by CHALLENGE_S (t_pos2: 3 of 6 cases fail). I did not rerun it. |
| 12 | Cluster E4 | STANDS | The proof reduces to compact support by OS Cauchy–Schwarz, then uses a rotation and Lemma red:gap. This fills CHALLENGE_S's "fillable gap" about unordered supports. |
| 13 | Step 9: identification of e^{−sH} in the reconstruction | NOT CHECKED | Recalled from OS73 §4 and not read. The text says so. |
| 14 | Free-field table: transcription of THEOREM_S §6 and CHALLENGE_S A4 | STANDS | The child compared every number. The numbers themselves were not recomputed by me. |
| 15 | Status table: H0 proved, H2 proved | NOT CHECKED | Written as the brief instructs. I did not check THEOREM_B. The sources mark OS78 as CLAIMED and say Theorem B′ has one model family. Those qualifiers are provenance and are not in this section. |
| 16 | My first draft: "proved in full", Lu77/OS78 as read | DEFECT (mine, fixed) | Found by child Q1 and corrected in the text. |
| 17 | Compile and style checks | STANDS | check_section K7: 7 met, 0 failed. Section 11 pp. |

Verdict counts: **12 STANDS, 2 DEFECT, 3 NOT CHECKED.**

## 2. Hypotheses each statement uses, and where they are stated

- **Theorem R′:** the abstract data are 0 < T_β ≤ 1, ψ_β ⊥ Ω_β, ψ_β ≠ 0 (§red:R, list), together with (A) hyp:A, (B) hyp:B and (C) hyp:C. (B) is used only in R5. For the Wilson transfer matrix the condition 0 < T needs Lu77; the text says so and does not use it.
- **Observation red:twomass:** the free-field one-particle dispersion relation (standard, not proved).
- **Theorem S:** μ_β ∈ 𝓛_β, site-scalar bounded real gauge-invariant fields, a = m, N_β, Z_i (§red:S-setting), H0 hyp:H0, H1 = hyp:A, H2 = hyp:B, H3 hyp:H3, H4 hyp:H4, and the reconstruction theorem red:OS (cited from OS75 via KQR).
- **Steps used by each part of the proof:**

  | Step | Uses |
  |---|---|
  | 1 | H2, H3(b), H3(c) |
  | 2 | H3(b) |
  | 3 | H0, H2, H3(c) |
  | 4 | H0, H4, H3(c), Lemma red:dense |
  | 6 | H0, boundedness of the fields |
  | 7 | T self-adjoint (from H0), H1 with a = m, Steps 2 and 6 |
  | 8 | H3(a), H3(c) |
  | 9 | Theorem red:OS and the recalled OS73 description |

  The paragraph "Where each hypothesis enters" in the text lists the same.

## 3. Failed predicates

- **numerics.py N4** (Kronecker approximation within 1e-3 using n ≤ 10⁴, θ = 1): it held for 4 of 5 φ. At φ = 0.5 the best distance is 3.6·10⁻³.
  - This is **my own expectation**: the tolerance was too tight. It is not a defect of the target, because the lemma needs the infinite set.
  - Two of my φ values (3.0 and 6.0) were integers and are hit trivially. That is a poor choice of mine.
  - The grandchild's G1 failed the same way, with the same number (3.597·10⁻³ at n = 9752).
- **check_section.py M1:** the "first" word counter is broken (a double-escaped regex), so it reports 0. The text contains "first" once ("The source first stated (C)"). That word is not a priority claim. This is my own bug in a measured-only line.
- **Child's own failures, as it classified them:**
  - q2 run 1: a bug in its search.
  - The K2 expectation: an expected exit code of its own.
  - Grandchild G1: its tolerance was too tight.

  None of these is a target defect.

Counts (met, failed, measured only):
- numerics.py (K1): 6, 1, 0.
- check_section.py (K2 first run): 7, 0, 1. Final K7: 7, 0, 1.
- Child q2b rerun by me (K4): 3, 0, 0.

"For all" predicates were tested per case:

| Predicate | Cases that hold |
|---|---|
| N2 | 6/6 |
| N4 | 4/5 |
| N5 | 3000/3000 |
| N6 | 3000/3000 |
| N7 | 241/241 |

Tolerances:
- 1e-12 for N2, N5 and N6 is float64 round-off headroom.
- 1e-3 for N4 is my own choice.
- Page range 8–12 comes from the brief.

## 4. What I did not check

- OS73, OS75, KQR21, OS78 and Lu77 were not read (no network).
- THEOREM_B (H0, H2 for SU(2)).
- The free-field numbers themselves: I did not recompute them, only the transcription (via the child).
- The bound G_m(n) ≤ C/|n|²: the text says "we do not prove it here".
- The local CLT for H4 of the free field.
- Lean: not used. /home/user/z4-lean/READY exists, and no Lean result is claimed.
- A1_REDUCTION's (C⁺)/R5 short-time statement is left out of the section.
- The source's "Relation to attempt 1" (H3 ⇒ (C⁺)) is left out because I could not close it in a few lines: it needs C(N) ≲ C(ξ).

## 5. Delegated questions and outcomes

- **Child T27** (`p3-cond-child`, parent T21): admitted ("ADMITTED T27"), run as check K3 (exit 0, 190 s), and released by me (event 56).
  - Control: dim so(4). It answered **6, which is correct**. I graded it before reading anything else.
  - Q1 was to read the section against THEOREM_S/CHALLENGE_S and list statements that got stronger. It found:
    - "proved in full" (Step 9 is cited and recalled);
    - Lu77 and OS78 presented as theorems although the sources hold them CLAIMED;
    - H2's qualifier dropped;
    - ‖T‖ ≤ 1 added;
    - c generalised (from the challenge record, so legitimate);
    - P = 4k+2 differs from the source.

    I corrected the first two in the text. ‖T‖ ≤ 1 is now attributed to the cited construction. The status entries for H0 and H2 stay as the brief instructs (item 15).
  - Q2 was the density lemma: every step follows, and its q2b holds (a), (b) 6/6 and (c). I reread q2b.py and reran it (K4), with identical output.
- **Grandchild T28** (`p3-cond-grandchild`, parent T27): the graph shows it admitted at seq 54 and released at seq 55.
  - Control: 2+2 = 4, which is correct.
  - Question: approximate R12(0.5) by R12(n·1.0) with n ≤ 10⁴, and the boundary case θ = π/2.
  - G1 failed (3.6e-3; tolerance too tight). G2 held: the group has 384 elements, the group is finite, and the rotation by 0.5 is not in it.
  - I reran gc.py (K5): its output is identical to out.txt. My N4 gives the same 3.60e-3 independently.

## 6. Rerun commands (from /home/user/z4-workers/p3-cond)

Output files open with mode "x", so move them first, or use a fresh copy directory as K6/K7 did.

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name numerics --expect-exit 0 -- python3 numerics.py                       # K1 (exit 1: N4)
$P check --ws pcp --name check_section --expect-exit 0 -- python3 check_section.py             # K2
$R task-admit $G --by principal --label p3-cond-child --parent T21                            # -> T27
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"   # K3
$P check --ws pcp --name rerun-child-q2b --cwd rerun_child --expect-exit 0 -- python3 -I q2b.py                                   # K4
$P check --ws pcp --name rerun-grandchild-gc --cwd rerun_child/grandchild --expect-exit 0 -- bash -c "python3 -I gc.py | diff - out.txt"   # K5
$P check --ws pcp --name check_section-final --cwd rerun_check --expect-exit 0 -- python3 check_section.py                        # K6
$P check --ws pcp --name check_section-final2 --cwd rerun_check2 --expect-exit 0 -- python3 check_section.py                      # K7 (final text)
$R task-release $G --by principal --id T27
pdflatex -interaction=nonstopmode main_test.tex; pdflatex -interaction=nonstopmode main_test.tex
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the verify commands:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Child register `child/pcp`: `result: PASS (...)`
