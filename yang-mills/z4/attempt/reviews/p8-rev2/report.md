# Report p8-rev2 (T56): second revision of the paper

**Corrections not applied:** none. I found no argument or computation that shows any of C1–C13 to be wrong. C14 needed no change. The paper says nothing about it.

Control: `control.txt` = 0.272341 (−ln tanh 1).

## Verdict table

STANDS means I checked the reviewer's claim myself and it holds, and I applied the correction. NOT CHECKED means I applied it on the reviewers' authority without an independent check.

| Item | Verdict | Evidence (one line) |
|---|---|---|
| C1 forest recursion `g_y = g_x U_xy` | STANDS | P1: dev 4e-16 over 50 SU(2) draws on a 3-site path. P2: the printed form fails on the 2nd link in 50/50 draws. Child A matches (20/20). Two-site note: with g_x = 1 both forms agree, so the error first shows on the third site. |
| C2 T not injective; even-lag application | STANDS (consequence); the vector itself is NOT CHECKED | P7 toy model: with H = −½ log T² on ran T, the norm on Ω⊥ is unchanged, even lags are equal to 1e-15, odd lags differ by 0.66. I did not construct the norm-¼ open-link vector. |
| C3.1 sentences after R′ | STANDS | P6: with eigenvalues 1, e^{-m}, e^{-2m}, C(ξ) = e^{-2} and C(ξ/2)/C(ξ) = e for m = 0.1, 0.01, 0.001. |
| C3.2 even lags | STANDS for the even-lag statement; the reviewer's odd-lag criterion is NOT CHECKED | The repair follows from the spectral theorem. The odd-lag "exactly when" condition is the reviewer's and is credited. |
| C3.3 / C12 support metric | STANDS | The graph-distance ball of radius 1 is the star of 9 vertices and has no plaquettes. The sup-norm ball contains the 24 corner plaquettes of the paper's own example. The Step 6 buffer is kept. |
| C4 OS II §IV.1 | NOT CHECKED | No network access, so I did not read the source. Text changed as instructed. E4 is now among the hypotheses and is proved in Step 7. |
| C5 smeared-norm variant | NOT CHECKED | Printed as reported and not read. |
| C6 (E*) same channel | STANDS (logic) | Comparing with 2m in a channel whose lowest free level exceeds 2m gives δ ≠ 0 for a free theory. The reviewer's specific counterexample (comment 7103655841) was not seen. |
| C7 off-chart shell data | STANDS (bound arithmetic); the U(1)×Z₃ example is NOT CHECKED | I re-derived η*/K_N² from the χ form of the shell filling bound and the exponent βη*/(8K_N²) from the tail (P5). Child B2 agrees. |
| C8 U(1) wrapping | STANDS | P3: six angles π/3 give product 1 and sum 2π. P4: 66 371 cases with m_c ≠ 0, 0 with max|θ| < π/3. P5: exponent β/16. Child B1 and grandchild (70 digits) agree. |
| C9 Hessian; Haar-volume ratio | STANDS (Hessian: s(e^X) = (1/N)Σ(1 − cos θ_j), whose second derivative is |X|²); ratio remark NOT CHECKED | — |
| C10 finite groups | STANDS (δ = 2 for the sign representation, P8); the theorem itself is NOT CHECKED | Printed as reported and not read. AC22 is limited to what it states. |
| C11 1500 → 1490 | STANDS | P9: 1500 − 10 = 1490 and 260+290+290 = 840. 2990 and 840 unchanged. |
| C13 seventh/eighth root | NOT CHECKED | Printed as reported. The eighth-root result is marked as awaiting review. |
| C14 | NOT CHECKED (nothing to do) | Nothing in the paper, as instructed. |
| V1–V6 credited where used | STANDS (text) | See CHANGES.md. |
| Compilation | STANDS | pdflatex run 3 times after a clean start: no errors, no undefined references, one overfull box of 2.17 pt (≤ 15 pt). **52 pages.** |
| Alias grep | STANDS | No hits for A4, B4, C4, D4, G4, Z4, "group A/B/C/G" or "Director". Remaining case-insensitive hits are listed below. |

Counts for my own program predicates: **9 met, 0 failed, 0 measured only.** One run failed (register check K2, exit 1). The cause was my own program: the final `print` could not JSON-serialise a numpy integer. The result file it had already written was complete, with all 9 met. This was not a defect of the target. I fixed the print only and reran it as K3: exit 0.

## Hypotheses used by each statement, and where they are stated

- **Theorem R′** (sec_reduction §red:R): positive injective T ≤ 1 with TΩ = Ω and ψ ≠ 0, ψ ⊥ Ω (the data bullets); (A), (B) and (C) (Hypotheses hyp:A, hyp:B, hyp:C). In the application: T² on the closure of the range of T, ψ projected there and nonzero (paragraph after eq. red:C). Odd lags need the reviewer's tilted negative-weight condition (same paragraph).
- **Theorem S** (thm:conditional): H0 (hyp:H0), H1 = (A), H2 = (B), H3(a–c) (hyp:H3), H4 (hyp:H4); site-scalar fields supported in the sup-norm ball of radius 1 (§red:S-setting); the reconstruction theorem [OS75 §IV.1] with E0′ and E1–E4 (red:OS); the recalled description of the reconstructed space (after red:OS).
- **Theorem 1 (main)**: dyadic periodic limits (Introduction); Lemmas rp, limit, transfer, chess, forest (corrected), free, cor-tail, E, flat, shell, L3, L4, D, R, wick, G (Section 4).
- **gen:thm**: compact Lie G with d ≥ 1 and faithful unitary ρ (sec_general, first paragraph); the replacements (i)–(vi), with the new (iv′) chart event and the (vi) U(1) wrapping event, each bounded through Cor. cor-tail with D*_G.
- **Lemma neg:lem-decaygap**: 0 ≤ T ≤ 1, a dense set of observables, a uniform rate m (statement).

## Failed predicates

- K2 (`check_rev`): exit 1. The cause is my own program defect (see above), not the target.
- Child: its first run of prog_A failed on numpy JSON serialisation, a child-side bug. PB5 (`1 − cos(π/3) ≥ 0.5` in double precision gives False) is a rounding artefact at the boundary; the child had predicted it. Child K3 failed because a result file already existed (mode "x"), a child-side bug. None of these is a defect of the target.

## What I did not check

- The norm-¼ open-link vector and the gauge-averaging projection of C2. The U(1)×Z₃ example of C7. The Z₂ / finite-abelian gap theorem of C10. The smeared-norm variant (C5). The eighth-root bound (C13). Uniform constants over closed subgroups (C9). OS II §IV.1 (C4): I had no network access.
- Whether the V6 confirmations by the groups other than G sit in the disposition comments I cited (7105447358, 7105100783, 7105348719). DIRECTORS_REVIEW.md gives no comment number for them, so I cited each group's disposition comment. **This should be checked against the thread.**
- I did not re-check the proofs of the paper beyond the passages touched. I did not re-audit L3, the chessboard estimate or the negative sections.
- I made no Lean run.
- I did not read the 52-page PDF visually. I checked only the log.
- The disposition from comment 7105100783 says "revision required", not "major revision". The paper quotes each disposition as given. The Disclosure follows the brief and says "three … recommended major revision". **The principal should confirm that this wording is acceptable.**

## Remaining grep hits, with reasons

- `director` (lowercase), at main.tex:58 and sec_provenance.tex:6 and 31: the role of the paper's own sessions, not an alias of a reviewing group.
- `z4`, at refs.tex:116 and sec_provenance.tex:34: a folder name in the repository path (`yang-mills/z4/attempt`). Changing it would break the reference.
- `verified` / `reviewed`:
  - main.tex:5 and 8: "not reviewed by a mathematician", which is true.
  - main.tex:58: the new Disclosure.
  - main.tex:73: the "not claimed" item.
  - sec_proof.tex:373 and 416: credits for V2 and V3.
  - sec_provenance.tex:22 and 24: "What was (not) verified".
  - sec_paperreview.tex:7 and 9: earlier same-family reviews.
  - sec_paperreview.tex:11: the new paragraph.

  Each is an accurate statement of scope.

## Delegated questions and outcomes

- **Child T57** (label p8-rev2-child, parent T56; admitted at event 115; released). It was given only the statement and definitions. Its questions were (A) the corrected recursion against the convention (U^g)_xy = g_x U_xy g_y⁻¹, on a 3-site path with random SU(2), and (B) the arithmetic of the C7 and C8 bounds.
  - Control: faces of a cube = **6**. I graded this first, and it is correct.
  - Outcome: A STANDS (dev 6.3e-16; the printed form fails 20/20). B1 and B2 STAND.
  - I reread prog_A.py and reran prog_A.py, prog_B.py and grandchild/check.py in fresh directories (register checks K4–K6, exit 0). The outputs were identical.
- **Grandchild T60** (label p8-rev2-grandchild, parent T57; released by the child). Its question was a 70-digit recomputation of the π/3 boundary case. Its control (6) passed. Result: the sum − 2π and s − ½ are both at 1e-69. In doubles, s at π/3 is 1 ulp below ½. I reran it (K6) with the same output.
- Child register: `pcp_os verify` gives "result: PASS …". `pcpos verify` exits 0.

## Register

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` The verdict lines before it are `chain intact: 8 events, head d52c7ab1…` and `guards replayed: 0 problem(s)`.

## Exact commands to rerun

```
cd /home/user/z4-workers/p8-rev2
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
mkdir -p runs/r3 && $P check --ws pcp --name check_rev3 --cwd runs/r3 --expect-exit 0 -- python3 /home/user/z4-workers/p8-rev2/progs/check_rev.py
mkdir -p runs/cA2 && cp child/prog_A.py runs/cA2/ && $P check --ws pcp --name rerun_child_A2 --cwd runs/cA2 --expect-exit 0 -- python3 prog_A.py
mkdir -p runs/cB2 && cp child/prog_B.py runs/cB2/ && $P check --ws pcp --name rerun_child_B2 --cwd runs/cB2 --expect-exit 0 -- python3 prog_B.py
mkdir -p runs/cg2 && cp child/grandchild/check.py runs/cg2/ && $P check --ws pcp --name rerun_grandchild2 --cwd runs/cg2 --expect-exit 0 -- python3 check.py
cd paper && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex && grep -n "^!\|undefined\|Overfull" main.log && pdfinfo main.pdf | grep Pages && cd ..
grep -n -i "A4\|B4\|C4\|D4\|G4\|Z4\|group [ABCG]\b\|director\|verified\|reviewed" paper/*.tex
for f in main sec_reduction sec_proof sec_general sec_negative sec_provenance sec_paperreview refs; do diff orig/$f.tex paper/$f.tex; done
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
# child, as it was run:
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
```

Deliverables: `paper/` (revised in place, main.pdf with 52 pages), `CHANGES.md`, `report.md`, `notes.md`, `progs/check_rev.py`, `runs/`, and `orig/` (the unrevised sources).
