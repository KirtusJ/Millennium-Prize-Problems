# r9-proof report (builder): two-sided bound on C_b in the free lattice Maxwell benchmark

Control: `control.txt` = 0.272341 (−ln tanh 1).

The full proof is in `proof.md`, the Lean in `R9Bounds.lean`, the program in `bounds.py`, and the results in `results_bounds_run1.json`.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| THEOREM: v ≤ C_b(2τ) and C_b(τ) ≤ V for b ≤ b₀, with explicit constants | STANDS (proved in text; finite-sum steps in Lean) | proof.md §3–5: V = (2/ℓ⁶)F²(π/ℓ)²G(4τ/ℓ)², v = (2/ℓ⁶)(∫f)²/4 · m(2τ), b₀ = min(ℓ/3, 2π(\|∫f\|/(2S₄‖Δ²f‖₁))^{1/4}) |
| Route step 1: momentum representation with the (2/ℓ⁶) normalization | STANDS | Derived in proof.md §1. At N = 8 it agrees with the position-space formula to rel ≤ 5.5·10⁻¹⁵ (mine, K2) and ≤ 3.7·10⁻¹⁵ (sub-agent; my rerun K3 gave an identical file) |
| Route step 2: upper bound | STANDS, with a different fhat bound | The fhat bound uses aliasing with ‖Δ²f‖₁ (or ℓ³ sup\|f\|), not "b³Σ\|f\| ≤ 2∫\|f\|", which I did not prove. G(a) is checked in 15 cases (P4) |
| Route step 3: lower bound | STANDS, with two added conditions | It needs N ≥ 3 (so that k ≠ −k), and modes along e₃ must be excluded (P₃₃ = 0). The suggested k = (2π/ℓ)e₁ is fine |
| Route step 4: bracket for ℓ = 1, Gaussian R = 0.1, τ = 0.05 and 0.1, N = 16…64 | STANDS | 10 of 10 cases bracketed (P5). Loose: C/v is 73 to 1658 and V/C is 1.3·10⁴ to 9.5·10⁴. The window E₀ is 187 (τ = 0.1) and 454 (τ = 0.05), against a lowest atom of about 12.57 |
| Lean (a): Jordan bounds on k̂ | STANDS | `R9.jordan_khat`, using Mathlib `Real.mul_le_sin` and `Real.sin_le`. Exit 0, axioms propext / Classical.choice / Quot.sound, no sorry |
| Lean (b): term keeping and the factorized upper bound | STANDS | `R9.keep_terms`, `R9.keep_terms_card`, `R9.factor_upper`. Same compile |
| Lean (c): corollary via S5e | STANDS | `R9.window_from_two_sided`. S5 is copied verbatim from input/HeatRegularized.lean, lines 13–177 |
| Identification of the step-1 atoms with the spectral measure of O_bΩ | STANDS, text only | proof.md §1: two-photon sector, finite-dimensional, uniqueness of finite Laplace sums |
| Convergence C_b → C, uniformity in τ, infinite volume | NOT CHECKED | Not proved. v → 0 as ℓ → ∞ |

## 2. Hypotheses and where they are stated

- **H1:** the formula for D_t, normalization k̂/2. Taken from STATEMENT.md (confirmed by its review); not rederived here. Stated in proof.md §0.
- **H2:** Wick, C_b = 2b⁶ΣffD². From STATEMENT.md; proof.md §0.
- **H3:** f real, C⁴, periodic, ∫f ≠ 0. proof.md §0. Used in §2 and §4c.
- **H4:** N ≥ 3. proof.md §0. Used in §4a.
- **b ≤ b₀:** proof.md §4c. In the concrete case b₀ = 1/8 for V; v holds for all N ≥ 3.
- **Corollary:** also uses S5e's hypotheses (w ≥ 0, E ≥ 0, τ > 0, v > 0). These are discharged by §1 and §5.
- **Concrete case:** the normalization of f (peak 1) is my choice. All the quantities are homogeneous of degree 2 in f, so the ratios do not depend on it.

## 3. Failed predicates

- **K1 (`bounds`, first run): exit 1, expected 0.**
  - All 63 printed predicates were MET. The program then crashed while computing S₄, because scipy is not installed, before it wrote the result file.
  - This was a defect of my own program, not of the target.
  - I replaced scipy's quadrature with the closed-form tail integral and reran it as K2: exit 0. K1 stays in the register.
- No predicate about the target failed.

**Counts (met, failed, measured only):**
- My program K2: 63, 0, 31.
- Sub-agent program, rerun by me as K3: 18, 0, 0.
- Lean K4: 2, 0, 0.
- Program-level failures: 1 (K1).

## 4. What I did not check

- I did not rederive the normalization of D_t (H1).
- I did not prove convergence of C_b(t) to C(t), or its rate.
- The bounds are not uniform in τ: v ~ e^{−8πτ/ℓ}, and V ~ τ⁻⁸ as τ → 0.
- Infinite volume is not covered.
- The following are proved in text only, not in Lean: the aliasing lemma, the lattice-sum lemma G(a), the monotonicity of κ_N and the endpoint-minimum argument, and the spectral identification.
- S₄ ≤ 16.58 comes from a program, not from Lean.
- I did not try to sharpen the bounds. A much better V would use the decay of f̃ on the scale 1/R.
- MeasureHeat M3 is not used: at fixed b the measure is finite, so S5e suffices.

## 5. Delegated question and outcome

**Question given to the sub-agent** (in child/, with its own register child/pcp):
- Control: ζ(2) to 8 decimals. It answered 1.64493407, which is correct.
- P1: position-space vs momentum-space C_b at N = 8, t ∈ {0.05, 0.1, 0.2}, tolerance 1e-10.
- P2: C_b(t) for N ∈ {16, 24, 32, 48, 64}, t ∈ {0.05, 0.1, 0.2}.

**What came back:**
- P1 holds, with relative differences ≤ 3.7·10⁻¹⁵.
- The P2 table is positive and finite.
- Its verify ended in PASS.

**What I did with it:**
- I reread `child/corr_check.py` and reran it in my register (K3, tag parentrerun). Apart from comment lines, the result file is identical to the sub-agent's.
- Its C_b values also match my own independent FFT-convolution code in K2 to all printed digits (for example C_16(0.05) = 180.7619…).
- The sub-agent noted that C_b(0.05) is not monotone in N over 16 to 64. This is consistent with the S2 review ("O(b²) only once t/b is large"). It does not affect the theorem, whose bounds are uniform in b.

## 6. Commands to rerun

```
cd C:/Users/donke/z4-workers/r9-proof
export PYTHONUTF8=1
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name bounds3 --expect-exit 0 -- python bounds.py    # move/rename results_bounds_run1.json first: never overwritten (assert)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child_rerun2 --expect-exit 0 -- python child/corr_check.py rerun2
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r9-proof/R9Bounds.lean
cd C:/Users/donke/z4-workers/r9-proof && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

**Last line of `verify --ws pcp`:**
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

The child register verifies with the same PASS line.

Director, worker and sub-agent are one model family, so this is not independent review.
