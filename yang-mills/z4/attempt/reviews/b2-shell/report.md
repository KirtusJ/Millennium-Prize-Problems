Overall verdict: all six auditor claims STAND (6 STANDS, 0 DEFECT, 0 NOT CHECKED). Claims 4 and 5 stand under stated hypotheses that the auditor does not spell out (see below). The only defect found is a wording mismatch in the auditor's preamble, which does not change any result.

Worker b2-shell, task T215. Control: control.txt = 0.272341 (-ln tanh 1). Lean was ready (/home/user/z4-lean/READY exists) but I did not use it. No Lean claim is made.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| 1 Shell weights w_r = 8r²+2/3, w_m = 4m²−2m+1/3 | STANDS | Exact brute force, m=1..12, all 78 (m,r) cases equal. The antipode count is (2m)³−(2m−1)³ = 12m²−6m+1, because only c=m has distance m. Total Σw_r = (8m³−1)/3 (12/12). The child reproduced this independently and I reran its program: 156/156. |
| 2 A_m bounds, unfolding, constant 8, sharpness | STANDS | Unfolding is exact (144/144 coefficients). A_m ≤ 8(1+s)/(1−s)³+2/(3(1−s)) ≤ 16/(1−s)³ and A_m ≤ (16m³−2)/3 ≤ 8m³ hold exactly on 69 rational s values × m=1..12 (828 to 840 cases). The ratio A_m(1−m^{-1/2})/(2m^{3/2}) rises monotonically: 3.93 (m=4), 7.48 (m=64), 7.996 (m=4^10), always below 8. A random positive-measure chain test (seed 20261124, m=1..6) gives 6/6. The indexing s^{r−1}+s^{2m−r−1} matches spatial.md. |
| 3 I/(48e) ≤ W ≤ 2I | STANDS | Exact check, with e bracketed by rationals, on 840 (m,s) cases including s=0 and s=1. Observed min W/I = 0.2502 and max = 2.0000, so the constant 1/(48e) ≈ 0.0077 is valid but very loose. The step floor(z) ≥ z/2 and the step s^{r−1} ≥ 1/e for r ≤ floor(z) both hold (840/840). Proof: (1/t−1)·ln(1−t) ≥ −1. |
| 4 Plane identity and kernel bounds; scope examples | STANDS (conditional) | Σ_{r=1}^{N−1}(s^{r−1}+s^{N−r−1}) = 2(1−s^{N−1})/(1−s) holds exactly (2208/2208). The bounds (1−1/e)·min(L,1/(1−s)) ≤ f ≤ min(L,1/(1−s)) hold for N=2..64 (2208/2208). Example 1_{x_j=0}: PSD (eigenvalues N²·δ_{p⊥=0} ≥ 0), χ=N², D_j(0)=N², ρ=0. Example 1_{x=0}+N^{-2}: PSD (eigenvalues 1+N·δ_{p,0}), χ=N+1, D_j(0)=2, D_j(r)=1 for r≥1, ρ=δ_1/2. Checked at N=4,6,8. |
| 5 Hybrid contact estimate, 2D weights 4r and 2m−1/2 | STANDS (conditional) | Exact 2D brute force: 78/78 cases, shell totals 8r and 4m−1. Unfolded coefficients are 4l (l<m), 4m−1 (l=m) and 4(2m−l) ≤ 4l (l>m), so A2 ≤ min(4m²−1, 4/(1−s)²) ≤ 4·min(m²,(1−s)^{-2}). Exact check: 828/828. |
| 6 Nonnecessity example | STANDS | χ(N) = S_s·S_q²/N with S_a = [(1+a)/(1−a)]·(1−a^N)/(1+a^N). Brute-force 3D sums match this for N=16 and 32, and the 3D kernel is PSD. χ: 4.329314 (N=16), 4.328259 (32), …, 4.327908 (512), with limit 2coth(1/2) = 4.3279068275. **2tanh(1/2)coth²(1/2) is the same number** (tanh·coth = 1), so both closed forms are right. W/N² → L = (1/3)∫₀^{1/2} u²·cosh(u−1/2)/cosh(1/2) du = 0.0124718. The error is ≈ 0.037/N, so W grows quadratically. |

Counts over all predicates (both of my programs plus the child rerun): **24 met, 1 failed, 0 measured only**. The failed one is listed below.

## Hypotheses each statement uses, and where they are stated

- **H0 (geometry):** periodic cube of even side N=2m, with d(c)=min(c,2m−c). From the brief.
- **H1 (axial domination):** |C(x)| ≤ c_j(d(x_j)) for every j. Stated in spatial.md §1 (Cauchy–Schwarz on the transverse-translation matrix). Claims 1, 2 and 5 use it in the tie-averaged form: C(x) ≤ the average of c_j(r) over the maximising axes. This follows from H1 alone.
- **H2 (representation):** c_j(r) = ∫(s^{r−1}+s^{N−r−1})dν_j for 1≤r≤N−1, with ν_j ≥ 0 and mass ≤ K. Stated in spatial.md §"Local transfer spectral weight". Claims 2, 3 and 5 use it.
  - **Indexing attack:** the auditor's preamble writes s^r+s^{N−r}. That is not spatial.md's form. Claims 2 and 3 do use the spatial.md form, so they are consistent. The s^r form is the slice-face case with measure s·dν, so every upper bound only gets weaker in that case. This is a wording defect of the preamble, not of the claims.
- **H3:** C(0) ≤ K, used in "χ ≤ K + …" in claims 2 and 5. spatial.md only gives mass ≤ c_j(1) ≤ C(0). So K must be taken ≥ C(0). spatial.md does this implicitly; the auditor does not state it.
- **H4 (claim 4):** D_j(r) = ∫(s^{r−1}+s^{N−r−1})dρ_j for 1≤r≤N−1, with ρ_j ≥ 0. This is the transfer representation applied to the zero-transverse-momentum (plane-sum) mode. It is not written out in the target files; spatial.md states only the axial version.
  - **Normalisation attack:** P_j(r) equals D_j(r) only if each plane sum is normalised by N^{-1} (the square root of the area). If "plane average" means 1/N² per plane, then P_j = D_j/N² and the identity must carry N². The brief does not fix which one is meant.
  - **Straddling faces:** the representation covers r ≥ 1 only. Contact at r=0 stays separate as D_j(0), which is correct, because s^{−1} would appear there.
- **H5 (claim 5):** H1 restricted to the plane x_j=0, with axes k and l, and H2 for ν_k and ν_l.
- **H6 (claim 6):** s = e^{−1/N}, q = e^{−1}, and C = (3N)^{-1} Σ_i k_s(x_i)·Π_{l≠i} k_q(x_l). I reconstructed this form from the brief's wording. The target files contain no such example.

## Failed predicates

- **shell_audit.py "P6 W quadratic growth":** I required |W(512)/W(256) − 4| < 0.01 and measured 3.97701. This was **my own expectation** (I ignored the O(1/N) correction), not a defect of the target. The follow-up p6b.py shows W/N² → 0.0124718 with error·N → 0.037 (Q1 and Q2 met).
- **The child's own P2:** Σ_r w_r == ((2m)^d − (2m−1)^d)/d failed in 22 of 24 cases. This was the child's wrong expectation (that formula is the last-shell value). Its corrected P2′ met 24/24.

## Not checked

- Inequalities were checked on a finite rational grid of s (k/64 and 1−10^{-k}, k=2..6) and m ≤ 12. Sharpness was checked up to m = 4^10. For all s and m I rely on my written derivations (above), not on the program.
- Whether H4 (the plane-sum transfer representation for straddling faces) is actually derivable from the Wilson transfer construction. I accepted it by analogy with spatial.md.
- spatial.md's own constants 18 and 36. These were not asked. The 2(2r+1)² count does hold by inspection.
- No Lean was used.

## Delegated questions

- **Child T218 (b2-shell-child, parent T215, admitted and released).**
  - Question (i): brute-force the 3D and 2D tie-shared shell weights for m=1..12 against the stated formulas, with exact Fractions.
  - Control: Σk² for k=1..10 = 385. I graded it correct before reading anything else.
  - Returned: both claims STAND, 156 met and 0 failed.
  - I reread its code (correct enumeration and tie rule) and reran it in my register (check K4): 156 true, 0 false.
- **Grandchild T219 (b2-shell-grandchild, parent T218, admitted and released by the child; confirmed in the graph).**
  - Question: hand-list the 3D values for m=1 and m=2.
  - Control: 7·8 = 56, correct.
  - Returned w = 7/3 (m=1), 26/3 and 37/3 (m=2). These equal my brute-force values and the formulas.

## PCP OS

Register pcp holds: K1 child-run1 (exit 0), K2 shell-audit-run1 (exit 1, expected 0: the P6 tolerance failure above), K3 p6b-run1 (exit 0), K4 child-rerun (exit 0).

- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## For the auditor

- **Antipodal counting:** correct. Only one residue c=m has distance m, so the r=m shell has (2m)³−(2m−1)³ sites, and each axis gets a third by symmetry.
- **Reflected-power indexing:** your preamble's s^r+s^{N−r} is not spatial.md's s^{r−1}+s^{N−r−1}. Your computations, however, use the latter. Fix the preamble.
- **Reverse comparison:** correct, but the constant 1/(48e) is about 33 times weaker than the observed minimum W/I ≈ 1/4.
- **Plane-contact normalisation:**
  - State whether P_j uses a 1/N or a 1/N² normalisation per plane.
  - State the plane-sum transfer representation (H4) explicitly for straddling faces at r ≥ 1.
  - State C(0) ≤ K.
- **Claim 6:** 2coth(1/2) and 2tanh(1/2)coth²(1/2) are equal.

## Rerun commands (from /home/user/z4-workers/b2-shell)

Result files open with mode "x", so delete or rename results_shell.txt, results_p6b.txt and child_rerun.jsonl first, or run in a copy of the directory.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name shell-audit-run1 --expect-exit 0 -- python3 shell_audit.py
$P check --ws pcp --name p6b-run1 --expect-exit 0 -- python3 p6b.py
$P check --ws pcp --name child-rerun --expect-exit 0 -- python3 child/shell_check.py child_rerun.jsonl
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

shell-audit-run1 exits 1 by design: its P6 tolerance failure is kept.
