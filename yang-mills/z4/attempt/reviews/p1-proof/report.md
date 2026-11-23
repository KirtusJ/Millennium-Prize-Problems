# report — p1-proof (task T17): proof section for Theorem B′, `sec_proof.tex`

Control: `control.txt` = 0.272341 (−ln tanh 1). I share a model family with the authors, the challengers and the director, so my agreement is not independent review.

**Possible defects (top of report, as the brief requires): none found.** I found no step in PROOF_B_v2.md, L3_L4.md or G4_LEMMA_R.md that does not follow, so `sec_proof.tex` contains no `% POSSIBLE GAP` marker. My child's read-through flagged three places where my own first draft said more than it proved (C_G called explicit, "exactly 6 plaquettes" with no argument, and the limit tail bound argued too tersely). None of the three is a defect of the source files. I repaired all three in the final file (§5).

The deliverable is `sec_proof.tex`, which is `\input` by `main_test.tex`. pdflatex was run twice: 0 errors, 0 undefined references, 0 undefined citations, 0 overfull boxes. main_test.pdf has 16 pages. The section fills pages 1–16, minus the dummy theorem at the top of page 1 and the references at the bottom of page 16, so it is **about 15.5 pages**.

## 1. Verdict table (items of the section)

| item | verdict | evidence (one line) |
|---|---|---|
| Site-plane RP and limit states (Lemmas pf:lem-rp, pf:lem-limit) | STANDS | Re-derived: E₀/E₊/E₋ partition, W₊ with ½ on π, Haar inversion; DLR goes from continuous local to bounded measurable by equality of two measures. |
| Transfer matrix, spectral bound for **every** n ≥ 1 (pf:lem-transfer, pf:prop-spectral) | STANDS | The a_{2^i} iteration gives ‖τF‖ ≤ ‖F‖; Cov = ⟨v,Tⁿv⟩ ≤ ‖T\|Ω⊥‖ⁿ Var for every n. The "even n" restriction is removed (challenge 2). |
| Chessboard estimate, L = 2^k (pf:lem-chess) | STANDS | Index map θ_a∘ϑ_t = ϑ_{t′} checked for both parities. H₊ condition 2^i ≤ L/2; Z({0})^{|Λ|} ≤ Z(all). |
| Free energy, tail e^{60.2−t/8} (pf:lem-free, pf:cor-tail) | STANDS | checks.py P3: D* = 60.192240; P4: ẑ bound and Haar(B_s) ≥ c_H s³ hold. The leftover (6/L) log β term is written out and vanishes as L → ∞. |
| Zero set, shell simple connectivity, nondegeneracy (pf:lem-flat, pf:lem-shell, pf:cor-zero) | STANDS | Axial-tree induction, gluing order, and every shell plaquette lying in a face (now proved in the text). K_N is said to be finite and not computed. |
| L3 uniform Laplace limit (pf:thm-L3) | STANDS | Near and far constants re-derived (λ/16 and 7). The child re-derived them independently. η(δ), and hence c, is declared not explicit. |
| L4 as one proposition with explicit quantifiers, for an arbitrary sequence μ_k ∈ 𝓛_{β_k} (pf:prop-L4 (a)–(e)) | STANDS | Repair from challenge 2 included. The base-point change is done by equality in law, so L3_L4's "Colour" paragraph is not needed. Paths for P_R run inside T_s ∪ T_int. |
| Cube word identity for Bianchi (eq. pf:eq-cube) | STANDS | Written out in full: six words, 30 letters, reduced by hand. checks.py P1/P2 (search + incidence signs) and the child's check1 P3 (printed strings vs the plaquette definition) both reduce it to the empty word. |
| Increasing Dirichlet covariances (pf:lem-D) | STANDS | Variational formula; d*h^R = 0 on all of Λ′_R via the T_int gauge remark. Box labels corrected: 7/24, 0.49267, 0.49916 for N = 1, 2, 3 (side 2N). |
| Decomposition F = ξ + constant f (pf:lem-R) | STANDS | Lévy downward theorem plus characteristic functions. Constancy by the G4 L² argument, with one sentence of attribution. checks.py P5 checks the Hodge Laplacian = 8 − Σ shifts identity exactly on (ℤ/4)⁴. |
| Free correlation G (pf:lem-G), G = 1/(π²n⁴) + O(n⁻⁶) | STANDS | Elementary bounds on \|k\| ≤ 1 give the explicit three-term error bound. Numerics: G(0) = 0.5, G(1) = 0.0688747, π²n⁴G(8) = 1.092 (mine and the child's agree). |
| Wick inequality (pf:lem-wick) | STANDS | checks.py P8: Monte Carlo agrees with the covariance and variance formulas within 5 SE, using a correlated-colour background. |
| Assembly; sharp decay c(n) = 4/(π⁴n⁸)(1+O(n⁻²)) | STANDS | Argument by contradiction along a sequence (β_k, μ_k); Var_∞ ≥ 3/8. |
| Compile check | STANDS | pdflatex twice; no errors and no undefined refs or cites. |

Counts: **STANDS 14, DEFECT 0, NOT CHECKED 0** (items). Predicates: **met 11, failed 0, measured only 16** (my checks.py, K1). Child's check1 (K2 output; my rerun K3 is byte-identical): met 25, failed 0, measured only 0.

## 2. Hypotheses each statement uses, and where they are stated

- **Lemma pf:lem-rp** uses: L even; SU(2) (½Tr U⁻¹ = ½Tr U); Haar invariance under inversion. Stated in §pf:sec-rp.
- **pf:lem-limit** uses: weak limits along L = 2^k; the torus embedded around the origin (§pf:sec-setting).
- **Transfer matrix and pf:prop-spectral** use: translation invariance and RP of μ ∈ 𝓛_β; the DLR property for Var > 0.
- **pf:lem-chess** uses: L = 2^k; f ≥ 0 a function of the closed block 0; RP at every a.
- **pf:lem-free and pf:cor-tail** use: β ≥ 1; d = 4; the Weyl class density; L → ∞ before β → ∞.
- **pf:lem-flat and pf:lem-shell** use: any group; boxes ∏[a_i, b_i]; N ≥ 1.
- **pf:thm-L3** uses: box R; the T_s ∪ T_int gauge; λ_N > 0; the zero set; \|ψ\| ≤ M with β ≥ β₀(M); (E1)–(E3).
- **pf:prop-L4** uses: β_k ≥ 1, β_k → ∞, μ_k ∈ 𝓛_{β_k} arbitrary; the uniform tail; L3; the standard facts.
- **pf:lem-D and pf:lem-R** use: the conclusions of pf:prop-L4.
- **pf:lem-wick** uses: constant f, the same for p₀ and p_n; 0 < G(n) ≤ G(0).

The restrictions L = 2^k, limits of periodic states only, and "m → 0 includes m = 0" are stated in the first paragraph of the section.

## 3. Failed predicates

None, in either my program or the child's.

- The child's verdict table had three rows marked STRONGER-UNPROVED. These were findings against my own draft, not against the sources:
  - Row 3: "C_G explicit" was not delivered. Lemma G(4) now states the explicit three-term bound and says the exponential terms are not converted to a multiple of n⁻⁶.
  - Row 8: "exactly 6 plaquettes" had no argument. A one-clause proof is added.
  - Row 12: the limit tail bound was argued too tersely. It is now written via O_p → ½\|F_p\|² in law plus the portmanteau theorem. The child's reading that {O_p > t} ⊂ {½\|F\|² > t} points the wrong way is correct, but the proof does not rely on that inclusion.
- Child row 7: Lemma flat silently assumed a symmetric box. It is now stated for ∏[a_i, b_i].

Tolerance sources:
- P3 (±0.005): the two decimals printed in PROOF_B_v2.
- P6 (1e−3): my own loose quadrature estimate.
- P8 (5 SE): from 20 batches.
- The child's tolerances are listed in child/report.md §2.

## 4. What I did not check

- The Lean files (L34.lean, S2.lean). I did not use Lean. /home/user/z4-lean/READY exists, but this report claims no Lean result.
- None of the "standard facts" was source-checked.
- The values λ_N, C^{R_N} and K_N were not recomputed. λ_N and C^{R_N} are quoted "for orientation only"; K_N is never computed by anyone.
- Monte Carlo of the Wilson measure: not run.
- Theorem 1.1's own text: only a dummy was used.
- C4's alternative route.
- G4's asymptotic claim was re-proved here, not taken from G4.
- The section is written by the same model family as its sources. A referee outside that family has not read it.

## 5. Delegated questions and outcomes

- **Child**: task **T25**, admitted under T17, released after use. It ran as check K2 in my register (sonnet, exit 0, 239 s).
  - Question: read sec_proof.tex against PROOF_B_v2.md and L3_L4.md and list every statement that got STRONGER.
  - Control: "constant in front of \|ψ\|² in L3_L4" — answered **7, correct**. I graded it before reading anything else.
  - Result: 20 rows — STANDS 5, STRONGER-PROVED 9, STRONGER-UNPROVED 3, NOT CHECKED 3. The intended strengthenings are all STRONGER-PROVED: every n, the n⁻⁸ decay, L4 for every sequence, TV form of L3, strict monotonicity of G, and E\|f\|⁴ < ∞. The three UNPROVED rows are repaired (§3).
  - The child worked on a snapshot taken before my last wording fixes.
  - I reread its check1.py and reran it in rerun_child/ (K3): output byte-identical.
- **Grandchild**: task **T26**, admitted under T25 and released, per the child and the task graph events 50–51.
  - Question: compare only the statement of pf:thm-L3 with L3_L4 §2(d).
  - Control: plaquettes per link — **6, correct** (L3_L4.md line 71).
  - Result: the theorem is stronger than §2(d) alone, because it adds the whole-chart lower bound, TV/uniform-in-W convergence and the explicit K_∞ mean. All of these appear in L3_L4 §2(b)–(c), which the child confirmed. I read grandchild/findings.md and agree.

## 6. Commands to rerun (from /home/user/z4-workers/p1-proof)

Result files are opened with mode "x", so give new names or remove the old files first.
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name checks-run1 --expect-exit 0 --timeout 300 -- python3 checks.py checks_result1.txt
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label p1-proof-child --parent T17          # gave T25
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
mkdir -p rerun_child && cp child/check1.py child/L3_L4.md rerun_child/
$P check --ws pcp --name child-check1-rerun --cwd rerun_child --expect-exit 0 --timeout 600 -- python3 -I check1.py
$R task-release $G --by principal --id T25
pdflatex -interaction=nonstopmode main_test.tex; pdflatex -interaction=nonstopmode main_test.tex
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Register: K1 checks-run1, K2 child-run1, K3 child-check1-rerun.
- Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Last line of the Rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
