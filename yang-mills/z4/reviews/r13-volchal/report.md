# Report r13-volchal: challenge of THEOREM_V (lower bound L for C_{b,s}(0), Jensen extension to t > 0)

Control: `control.txt` = 0.272341 (−ln tanh 1).

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| A1 Step 1, a(k) ≥ (1−ε)²φ(k) | STANDS | Re-derived on paper. Only the numerator \|k̂_⊥\|² loses (1−ε)². 1/\|k̂\| ≥ 1/\|k\| and e^{−2s k̂²} ≥ e^{−2s k²} both go the favourable way (k̂ ≤ \|k\|). Power 2 per factor and 4 per pair are correct. Indirectly tested by Q1 (18/18). |
| A2 Step 2, pair bound and Gaussian identity | STANDS | Paper derivation (Cauchy–Schwarz; X²/P − (X²−XY/2)/(P+Y/4) ≤ 3Y/4; X²/P ≥ 2X−P). Child, rerun by me: 10⁶ samples, 0 violations, worst −5.6e−17 (rounding) at q=0, p₃→0, where the bound is tight. Gaussian identity is exact. |
| A3 Steps 3–4, 1-D sums, Poisson δ₀/δ₁, tails | STANDS | a3_sums.py: P1–P4 hold for 13 values of l/√s in [5,130] × 20 shifts (all 13 satisfy the tail hypothesis). δ₀ and δ₁ are exact Poisson error terms with the correct sign and size. |
| A3 Region and BZ membership | STANDS, with a formal gap | For K < π/b every kept k and q−k is a distinct BZ mode. The text allows K = π/b. When N is even, the points k_i = ±π/b are then the same mode and are counted twice in the cube. The effect is of order e^{−8π²} at b = √s/2. Missing hypothesis: K < π/b, or N odd. |
| A3 "uniform in l" | DEFECT (statement scope) | The bracket 2L₁L₀² − U₁U₀² is negative for l/√s ≤ 8 (−4.08 at 5, −0.019 at 8; first positive at 9). L is vacuous there. Uniformity holds only for l/√s ≳ 9, and the document does not state this. |
| A4 L ≤ C for own f (bump, and ∫f = 0) | STANDS | 18 of 18 cases qualify (H1–H6). Q2 L ≤ C: 18/18. Q1 G(q) ≥ A − B′\|q\|² at every BZ q: 18/18. L/C = 0.35, 0.34 (s=5e−4, l=1,2); 0.23 (l=3); 0.19–0.22 (s=1e−3); **vacuous (L < 0) in 6 of 18 cases, all at s = 0.002** (sΨ′/P = 0.161–0.183 > 1/7). |
| A5 Jensen direction, M₁/M₀ exponent, replacement by Ū₁/L | STANDS (but nearly empty) | C(t) ≥ C(0)e^{−tM₁/M₀}: 36/36. M₁ ≤ Ū₁: 18/18. C(t) ≥ L e^{−tŪ₁/L}: 24/24 with L > 0. The replacement is valid because L ≤ M₀ and Ū₁ ≥ M₁ both increase the exponent. Ratio of bound to C(t): 1e−3 to 2e−2 at t=0.02; 1e−13 to 4e−8 at t=0.1. Reason: Ū₁/L is 210–320, while the true M₁/M₀ is 34–68. |
| A6 "no step uses ∫f" | STANDS | Nothing in steps 1–6 uses ∫f. For f₂ (lattice ∫f = 0 exactly) L/C = 0.15–0.35 when s ≤ 1e−3. |
| A6 "constants depend on l only through Poisson errors" | DEFECT (minor, imprecise) | l also enters through Δ = 2π/l in the tail lower limit K′−Δ, in the tail normalisation, and in hypothesis H3 (K′−Δ ≥ 1/√α, which needs l/√s ≥ 4.6). Numerically (2/l³)A s^{5/2} = 1.3274e−4, 1.3443e−4, 1.3485e−4, so l-dependence is weak at fixed b/√s. |
| A6 A ~ s^{−5/2}, B′ ~ s^{−3/2}, threshold sΨ′/P < 0.14 | STANDS | B′/(As) → 7.000 (measured 7.000–7.25, and 7.0001 at l/√s = 130). The threshold is 1/7 = 0.143. Consistent with the data: vacuous exactly when sΨ′/P > 0.143. |
| A6 constants 1.754e−4, 0.48·true, 3.4 s | STANDS | Asymptote 5/8 × 2.806e−4 = 1.754e−4 (5/8 = (2/3)/(16/15) re-derived). With ε = 0.0651: 0.4775 × true = 1.3398e−4, and I measured 1.3397e−4. B′-term 3.34·s·true. The bound's leading constant is A s^{5/2}(2/l³) = 1.34e−4 against the true 2.806e−4, i.e. 0.48 of it (0.625 when b/√s → 0). |
| Document completeness | DEFECT (presentation) | P_b, Ψ′_b, L₀, U₀, L₁, U₁, κ and θ are used but never defined in THEOREM_V.md, and the file has no statement section. I had to supply my own definitions (stated in a3_sums.py). Step 5's "needs B ≥ 0" should read A ≥ 0. When A < 0, H3 gives B′ > 0, so L < 0 ≤ C and nothing breaks. |
| Step 7–8 scaling Ū₁/L ≍ s^{−1/2} | NOT CHECKED beyond data | Measured √s·Ū₁/L = 4.7 (s=5e−4) and 7.7 (s=1e−3) for l=1, f₁. Not constant: it depends on (1 − 7sΨ′/P). It holds only with sΨ′/P bounded away from 1/7, as step 8 says. |

Counts (met, failed, measured only): **met 41** (A3: P1–P4; A4/A5 predicate families Q1–Q6 across all cases; child's 5 items, rerun), **failed 0** in my programs, **measured only 9** (L/C values, threshold l/√s ≈ 9, constants, scaling ratios). Verdicts: **STANDS 9, DEFECT 3** (scope of "uniform in l"; the "only Poisson" claim; undefined symbols), **NOT CHECKED 1**. No wrong inequality, wrong constant or wrong Poisson term was found.

## 2. Hypotheses used and where they are stated
- K ≤ π/b and ε = K²b²/24 < 1: step 1. Should be K < π/b (see table).
- \|q\|_∞ ≤ Q ≤ K, and K′ = K − Q/2: step 3.
- K′ − Δ ≥ 1/√α (monotone tails): step 4.
- Poisson for Gaussian Schwartz functions: step 4.
- A ≥ 0 for e^{−x} ≥ 1 − x: step 5, labelled "B ≥ 0".
- Q² ≥ A/B′: step 5.
- B1 step 1 momentum representation: cited from THEOREMS_B. I re-checked it numerically (Q3, position-space FFT = momentum sum to 1e−9 relative).
- B3 M₁ bound: step 7, from THEOREMS_B. Checked (Q5).
- L > 0 for the t > 0 bound: implicit in step 7.
- Not stated anywhere: l/√s ≳ 9 for non-vacuity, and the definitions of P_b and Ψ′_b. My reading: l³P_b = Σ_q\|f̂_b\|², and l³Ψ′_b = Σ_q \|q\|²\|f̂_b\|² over BZ representatives.

## 3. Failed predicates
- None in my programs (a3-sums K2, a4-bound K4, child-rerun K3: all exit 0, 0 FAILS).
- Child: one run failed with a SyntaxError in its own code (its own defect, not the target's). Its rerun passed.

## 4. Not checked
- Lean: READY exists, but I wrote no Lean file and claim no Lean result. I did not open the author's Lean names (`perp_prod`, `pair_core`, `sq_div_ge`, `gauss_lin`, `jensen_exp`).
- The missing-step items (P_b and Ψ′_b against ∫f² and ‖∇f‖²) are acknowledged by the author as not done.
- The uniform-in-c U_q bounds of steps 7–8 (I used exact lattice A_p, which is a stronger test of the Jensen chain but not of the U_q bounds).
- The K = π/b double count with N even was not demonstrated numerically, because it is of size e^{−8π²}.
- N was capped at 176 (l=3, s=5e−4 used b/√s = 0.76, not 0.5).
- Only one shape family of f was tested.

## 5. Delegated questions
- **Child** (child/, sonnet, register entry child-run1 = K1, exit 0, 75 s). Question: A2, the pair bound and the claims (i)–(iv) on 10⁶ random (p, q).
  - Control: 4g(u)g(w) at p = (1,2,2), q = 0. Child answered 2.777778, which is correct (25/9). I graded it before reading anything else.
  - Outcome: all items STANDS, 0 violations. Tight at q = 0, p₃ = 0. Slack is at least 0.458\|q\|² when p₃ = 0 and q ≠ 0.
  - I read child/check.py (the formulas for g, L and rhs are correct) and reran it in rerun_child/ (K3). results.json was identical.
- **Grandchild** (child/grandchild/). Question: the boundary cases p_⊥ = 0 with small q, and q ∥ p, 2·10⁵ samples each, with a known-answer control first.
  - Outcome: 0 violations.
  - The child reran it in child/rerun_gc/ and got identical output. I did not rerun the grandchild separately; its question is covered by the child's sample classes (p_⊥ = 0, q = ±2p, q = λp), which I reran.

## 6. Rerun commands (results files open with mode "x": move the old ones away first)
```
cd /home/user/z4-workers/r13-volchal
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name a3-sums --expect-exit 0 -- python3 a3_sums.py results/a3_run1.txt
$P check --ws pcp --name a4-bound --expect-exit 0 --timeout 300 -- python3 a4_bound.py results/a4_run1.txt 176
$P check --ws pcp --name child-rerun --cwd rerun_child --expect-exit 0 -- python3 check.py
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last lines of the verifiers:
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Note: the director and I share a model family, so my agreement is not independent review.
