# report.md — d1-run (task T38), Director Z4, 23 Nov 2026

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean: /home/user/z4-lean/READY exists; Lean was **not used**, and no Lean result is claimed. Main deliverable: `RUNNING.md`.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Definition g2(R,β) = SF coupling, 1/g2 = Γ′(η)/k, gauge invariant, defined for SU(2) and U(1), g2 = g0² + O(g0⁴) | STANDS | RUNNING §1, §3 step 6; identical to LNWW's coupling (c1 = their m1 to 8 digits) |
| Thm 1: g2 = g0² + c1 g0⁴ + O_R(g0⁶) at fixed R, with c1 = −(1/k) d/dη[½ log det(H+DD†) − log det D†D] | STANDS, conditional on Hyp U + Lemma N at that R | proof RUNNING §3. Laplace with parameters CITED (Hörmander 7.7.5, from memory). Slice/Jacobian and determinant identity PROVED |
| Hyp U (unique minimum mod symmetry), SU(2), R ≥ 4, η = π/4 | STANDS (CITED) | LNWW hep-lat/9207009 §5.2 Thm 1, eqs (5.8),(5.9); SU(2) premises eq (5.11): 0 < η < π, L/a ≥ 4. Appendix B proof not read |
| Hyp U for U(1); and for SU(2) at R = 2, 3 | NOT CHECKED (local strict minimality COMPUTED only) | P3 min eig > 0 |
| Symmetry group must include the boundary torus at x0 = T | STANDS | without it H has an extra p = 0 zero mode. With it, H+DD† > 0 at every R (P3, 24/24 rows) |
| Lemma N (nondegeneracy) per listed R | STANDS (COMPUTED, floating point) | min eig(H(p)+D(p)D(p)†) = 0.120 (R=4) … 0.00906 (R=16), ≫ 1e-12 error bound |
| Thm 2: 0 < c1(R;U(1)) ≤ 1/(2cos(π/(2R²))) for all R; c1 ≡ 0 for non-compact U(1) | STANDS (PROVED) | RUNNING §4. Numerically every row satisfies the bound (A6b, 9/9) |
| Table c1(R;SU(2)), R = 2..16 | STANDS (COMPUTED) | equals LNWW Table 1 (p. 46) at R = 6, 8, 10, 12, 16 to all 8 printed digits. Child's dense route at R = 4: 0.312997 vs 0.313012 |
| c1(R;SU(2)) − c1(R/2;SU(2)) > 0 for R ∈ {4,6,8,10,12,16} | STANDS (COMPUTED) | 0.0866, 0.0724, 0.0707, 0.0708, 0.0706, 0.0698; 2b0 ln 2 = 0.0644 |
| U(1) differences | STANDS (COMPUTED) | 0.0043 … 0.0089, decreasing to 0.0044 at R = 16; c1 → 1/4 |
| log growth / monotonicity of c1(R;SU(2)) for all R | NOT CHECKED (MISSING as proof) | CITED only: LNWW eqs (7.37)–(7.39), numerical to L = 32. My fit gives A/(2b0) = 1.004 |
| Finite group: no expansion | STANDS (PROVED, elementary) | RUNNING §3 |
| Torus spoiled by torons | STANDS (PROVED, elementary: zero-action non-equivalent constant fields) | name and refs CITED secondhand via LNWW §5.1 p. 30 |
| SU(2), d = 3: c1 grows like R | STANDS (COMPUTED) | c1/R = 0.167 → 0.144 for R = 4..24 |
| SU(2), d = 5 | NOT CHECKED | — |
| Uniformity in R / Balaban | NOT CHECKED | the statement about Balaban is from memory with no locator: CLAIMED only |
| Bearing on the gap | none (DEFECT of any reading that says otherwise) | β → ∞ is taken first; C′(R) is uncontrolled |

**Counts.**
- Verdict rows: 13 STANDS, 0 DEFECT, 5 NOT CHECKED (including MISSING/CLAIMED items). The "none" row is a statement of scope.
- Predicates: **met 101, failed 18, measured only 4.**
  - 97 are analyze.py's predicates A1–A7, which also cover c1sf P1–P5, P7 (A5) and P8 (A6) on every row.
  - The other 4 are child/grandchild checks that I reread or reran: control, S(V), k, and the c1(4) agreement.
  - The 18 failures are c1sf's P6 at its original tolerance.
  - The 4 measured-only items are the fit coefficients, the d = 3 ratios at R < 8, the child's mineig, and the U(1) limit 1/4.

## 2. Hypotheses each statement uses, and where they are stated

- **Thm 1** (RUNNING §3) uses:
  - Hyp U (§2; SU(2): LNWW Thm 1);
  - Lemma F (freeness, §2, proved);
  - Lemma N (§2, computed per R);
  - Lemma 0 (critical point, §2);
  - smoothness in η on a compact J around π/4;
  - Laplace with parameters (Hörmander Thm 7.7.5, cited from memory).
- **Thm 2** (RUNNING §4) uses:
  - Lemma N for U(1) at that R (for A > 0);
  - the η-independence of D (abelian Ad);
  - H_η = cosθ H_t + H_s (Wilson action).
  - It does **not** need Hyp U: it is a statement about the formula c1. It holds as the coefficient of g2 only where Thm 1 holds.
- **Table** (RUNNING §5) uses: floating-point determinants (slogdet/LU), eigvalsh, and central differences in η with Richardson extrapolation.

## 3. Failed predicates

- **c1sf.py P6** ("Γ1′ at h = 1e-3 vs 5e-4 agree to 1e-7"): FAILED in 18 of 24 rows. The largest difference is 1.6e-6, i.e. 4e-8 in c1.
  - Cause: **my own expectation.** I set the tolerance before knowing |Γ1‴|.
  - analyze.py A2 re-tested it at 1e-5 and states that this relaxation was post hoc. All values in the table are Richardson-extrapolated, and they agree with LNWW to 1e-8.
- **Child (T40)**: its sf1loop.py used k = +|4 dS0/dη|. The grandchild (T41) caught this.
  - It was the child's own defect, not a defect of the target. The child kept the wrong-sign file and wrote a separate corrected one.
  - The grandchild's predicate "k == +37.638582" failed on sign for the same reason. My brief to the child defined k = 4 dS0/dη, which is negative.
- None of my predicates failed as a defect of the target.

## 4. What I did not check

- Hyp U for U(1), and for SU(2) at R = 2, 3.
- LNWW appendix B (the proof of Thm 1).
- Hörmander 7.7.5 was not reopened.
- No interval arithmetic: the table is floating point with error bounds argued, not certified.
- A proof of log growth or monotonicity of c1(R;SU(2)) for all R.
- SU(2) in d = 5.
- c1 at R = 6 by an independent route (the child ran out of budget).
- The η-dependence of the U(1) quartic terms beyond what enters through cos θ in H. In my formulation these are part of r = O(g0⁶), so this is only a check of the claim that they do not enter c1, which follows from the proof.
- Narayanan–Wolff hep-lat/9502021: the PDF was unreadable, so nothing from it is cited.
- Balaban: not read.
- The child's code was rerun by me only at R = 4.

## 5. Delegated questions and outcomes

- **Child T40** (admitted under T38, released; label d1-run-child).
  - Question: an independent evaluation of c1(R=4,6;SU(2)) by dense full-lattice matrices, with a finite-difference Hessian and no Fourier decomposition.
  - Control: S0 = 768(1−cos(π/32)) = 3.698130. I computed it before launch. **Graded first: correct.**
  - Result: c1(4) = +0.312997 (after its sign fix; Richardson error estimate about 1.2e-5). Mine is 0.313012, a difference of 1.5e-5: consistent. R = 6 was not run.
  - I reread its code (it is independent: different coordinates and a finite-difference H) and reran it under my register as K3 `child-rerun-R4`. It reproduced c1_rich = −0.3129974 in the raw convention, which is +0.312997 after the sign fix.
  - Its min eig(H+DD†) = 0.1457 differs from mine (0.1206). The likely reason is a different normalisation of the boundary column of D. Such a normalisation changes log det by an η-independent constant only, so c1 is unaffected; CLAIMED, not traced.
- **Grandchild T41** (parent T40, released; started by the child).
  - Question: recompute k(π/4) at R = 4 from the plaquette action by finite difference.
  - Control 3.698130: correct.
  - Result: k = −37.6385818856, against my analytic −37.63858188655: agreement to 1e-10. It found the child's sign defect.

## 6. Rerun commands (exact)

```
cd /home/user/z4-workers/d1-run
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# result files are opened with mode "x": use new names (e.g. results2/) on rerun; analyze.py reads results/*.txt
$P check --ws pcp --name u1-d4  --expect-exit 0 -- python3 c1sf.py U1  4 2 3 4 5 6 8 10 12 16 results/u1_d4.txt
$P check --ws pcp --name su2-d4 --expect-exit 0 -- python3 c1sf.py SU2 4 2 3 4 5 6 8 10 12 16 results/su2_d4.txt
$P check --ws pcp --name su2-d3 --expect-exit 0 -- python3 c1sf.py SU2 3 4 6 8 12 16 24 results/su2_d3.txt
$P check --ws pcp --name analyze --expect-exit 0 -- python3 analyze.py results/analysis.txt
$P check --ws pcp --name child-rerun-R4 --expect-exit 0 --cwd child -- python3 sf1loop.py 4 rerun_by_parent_R4.json
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Running times: su2-d4 174 s, u1-d4 32 s, su2-d3 29 s; 1 thread each.

Register: checks K1–K6, all exit 0 as expected.
- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 7. Sources (read)

- **LNWW, hep-lat/9207009, read in full text.** M. Lüscher, R. Narayanan, P. Weisz, U. Wolff, "The Schrödinger functional — a renormalizable probe for non-abelian gauge theories", Nucl. Phys. B384 (1992) 168.
  - URL: https://arxiv.org/pdf/hep-lat/9207009. The PDF text was extracted to the scratchpad, outside this directory.
  - Used: §5.1 p. 30 (torons, refs [59],[60]); §5.2 Thm 1, eqs (5.8),(5.9); §5.3 eqs (5.10),(5.11); eqs (3.20),(6.22) (Γ1 form, via the fetch agent's report; (3.20) read verbatim by it); Table 1 p. 46; eqs (7.37)–(7.41).
- **Narayanan–Wolff, hep-lat/9502021: abstract only.** Nothing is cited from it.

**Same model family:** my agreement with the director, the child and the grandchild is not independent review. The independent evidence is LNWW's 1992 table, which my code reproduces to 8 digits.
