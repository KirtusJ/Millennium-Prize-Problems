# report — a8-chalB2 (challenger of PROOF_B_v2.md, Theorem B′)

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean was available (READY exists) but I did not use it, so this report contains no Lean result.
I share a model family with the author and the director, so my agreement is not independent review.

## 1. Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | Lemma 1 (site-plane RP) | STANDS | I re-derived it. E₀ is fixed pointwise by ϑ, so ⟨FθF⟩ = ∫dU_{E₀}\|∫dU_{E₊}F e^{βW₊}\|² ≥ 0 also holds for F that depends on links in the plane. The exact 2D tests (row 5) are consistent with this. |
| 2 | Lemma 1′ (limit states: invariance, RP, DLR) | STANDS | Re-derived on paper: weak continuity for local continuous F, and the Wilson kernel preserves continuous local functions. |
| 3 | Transfer matrix, S1 | STANDS | ‖τF‖ ≤ ‖F‖ via the 2^j iteration. ⟨ψ,Tⁿψ⟩ = Cov because θO_{p₀} = O_{p₀}. The bound \|⟨ψ,Tⁿψ⟩\| ≤ ‖T\|_{Ω⊥}‖ⁿ‖ψ‖² holds for **every** n, so the restriction to "even n" is not needed (it is harmless). |
| 4 | Lemma 2 (chessboard, L = 2^k) | STANDS | Checked the indices: a = −2^i+1, θ_a∘ϑ_t = ϑ_{2a−1−t} in each direction, and S ⊂ H₊ holds through i = k−1. The images are |Λ|/4 distinct plaquettes, each hit 4 times, which gives the exponent ½·¼ = 1/8. Exact 2D U(1)/SU(2) torus test, L = 2, 4: P(O>t) ≤ Z_all^{1/N} holds in 100/100 cases. |
| 5 | Lemma 3 + Corollary (e^{60.2−t/8}) | STANDS | I re-derived ẑ ≤ (π/2)^{5/2}b^{−3/2}, the 3L⁴+L³ free links, α_p ≤ 4s and energy ≤ 48\|Λ\|. The (9/2)log β terms cancel. Recomputed D* = 60.1922. Only β ≥ 1 is used, and L → ∞ is taken before β → ∞. |
| 6 | Gauge repair / compact shell data | STANDS (paper level) | Triangle inequality for the bi-invariant class angle, plus the simply connected shell 2-skeleton. I checked that K_N exists; I did not compute its value. |
| 7 | Lemma H | STANDS | Proof re-derived. Smallest eigenvalue of Q on boxes of side 3, 4, 5, 6: 0.838, 0.300, 0.147, 0.0848, all > 0. |
| 8 | Lemma D (C^R ↑ P) | STANDS | C_pp on [−N,N]⁴ for N = 1, 2, 3, 4, 6: 0.29167, 0.49267, 0.49916, 0.49978, 0.49996. Nondecreasing and → ½. C(p₀,p₁) → 0.06884 ≈ G(1). |
| 9 | Lemma D's test report M1 (in the file) | DEFECT (labels only) | The file's values 0.2917, 0.4927, 0.4992 "for N = 2, 4, 6" are my values for N = 1, 2, 3 of the file's own box [−N,N]⁴. The file's "C⁶(p₀,p₁) = 0.0681" is my N = 3 value, 0.06811. The N labels are off by a factor of 2. The mathematics is unaffected. |
| 10 | Lemma R (h is a random constant, independent of ξ) | STANDS (given DLR in the limit) | The backward martingale needs E\|F\|² < ∞, which comes from S3a and L4(iii). Independence survives the L² limit. dh = 0, d*h = 0 and stationarity give Δh = 0, so the spectral measure sits at k = 0 and h is constant. Constancy carries real weight: with a background where f_{p_n} = −f_{p₀}, the ratio goes negative (−0.126 at n = 1). |
| 11 | Wick inequality Cov/Var ≥ (G(n)/G(0))² | STANDS | Recomputed: Cov = (3/2)G² + G·E\|f\|² + ¼Var\|f\|². Each term's ratio is ≥ c(n) because 0 < G(n) ≤ G(0). Checked in 80/80 cases (constant and random-constant backgrounds). |
| 12 | Lemma G | STANDS | My quadrature gives G(0) = 0.5000000 and G(n) > 0 for n = 1..16. G(1) = 0.0688747. Fitted exponent on n = 8..16: p = 4.094. The child and grandchild agree to within 5e-8 and 4e-10. The file's bound G ≥ c n^{−5} holds, but it is weak: the true decay is n^{−4}, so c(n) ~ n^{−8}. The n^{−10} in the file is valid but not sharp. |
| 13 | Interface: what the PROVED parts use from L3/L4 | DEFECT (repairable) | The assembly (end of §4) applies L4 to a sequence (β_k, μ_k) in which μ_k ∈ 𝓛_{β_k} **changes** with k. L4 as written says only "along some β_k → ∞", for an unnamed state. It must be stated for an arbitrary sequence μ_k ∈ 𝓛_{β_k}; its tightness source, S3a, is uniform in μ and supports that. Two symbols are also never defined: P_R (the plaquettes of the box) and Φ^b_out (in the DLR-in-the-limit step). |
| 14 | DLR in the limit (given L3, L4) | NOT CHECKED to referee depth | The outline is consistent, including the colour-averaging step. I did not write out the π-λ / product-test-function details. |
| 15 | §5 assembly, Theorem B′ | STANDS given rows 13–14 and L3/L4 | Order: k → ∞, then β → ∞ (inf over μ via subsequences), then n → ∞. m_μ is defined for every μ ∈ 𝓛_β with no uniqueness or ergodicity needed. The bound is through one vector, but that suffices for ‖T\|_{Ω⊥}‖ ≥ (c(n)−ε)^{1/n}, which is exactly m_μ as defined. |
| 16 | S2 Lean check (`s2_gap_le`) | NOT CHECKED | Not rerun. I checked the algebra by hand. |

Verdict counts: **STANDS 12, DEFECT 2, NOT CHECKED 2.**

## 2. Hypotheses each statement uses, and where they are stated

- Lemma 1: L even, G = SU(2) (needed for ½Tr U⁻¹ = ½Tr U), Haar invariant under inversion (§1).
- Lemma 1′: torus embedded around the origin, weak limits along L = 2^k (§0, §1).
- Transfer matrix: translation invariance and RP of μ ∈ 𝓛_β (§1).
- Lemma 2: L = 2^k (dyadic doubling), RP planes at every a (Lemma 1 plus translation invariance), f ≥ 0 a function of the closed block (§2).
- Lemma 3: β ≥ 1 (s = β^{−1/2} ≤ 1), d = 4, SU(2) Haar class density; L → ∞ at fixed β to drop the O(log β / L) terms (§2). I measured these terms: at β = 10⁴ the finite-L bound is D_L = 85.5, 72.9, 66.5 for L = 2, 4, 8.
- Lemma H: box contractible, shell connected, T_int meets the shell once per tree (§3).
- DLR in the limit: L3 (uniform for \|ψ\| ≤ M) and L4 (i)–(iii) (§3).
- Lemma D: Gaussian conditional covariance from the DLR-in-the-limit result (§3, §4).
- Lemma R: DLR in the limit; E\|F\|² < ∞ (S3a + L4(iii)); translation invariance of the law of F (L4(ii)); 3 independent colours (K_∞ in L3) (§4).
- Lemma G: Fourier formula for P (Lemma D) (§4).
- Inequality: Lemma R (constant h), G(n) ≥ 0, L4(iii) convergence in moments (§4).

## 3. Failed predicates

- **D1b (lemmaGD run 3)**: the file's M1 values were expected at the stated N = 2, 4, 6. They match N = 1, 2, 3 instead. The defect is the **target's** (mislabelled test report), not the mathematics. My expectation was also too literal.
- **Runs K3 and K4** (lemmaGD, lemmaGD-run2) exited 1. K3 failed because scipy is not installed. K4 failed on a KeyError: plaquette p₁ is outside the N = 1 box. Both were **my own program's** defects, not the target's, and no predicate was evaluated as failed in either run. In K4 the G section had already completed and its results file was kept: lemmaGD_results.txt.

Predicate counts (met, failed, measured only):
- chess2d: 100, 0, 100 (r ratios). 76 of the 100 cases are non-trivial (t < 2β); in the other 24, P = Z_all = 0.
- lemmaGD run 3: 14, 1, 12.
- child-g rerun: 4, 0, 0.
- **Total: 118, 1, 112.**

## 4. What I did not check

- L3 and L4 themselves (excluded by the brief).
- The DLR-in-the-limit details.
- The value of K_N.
- §6 discriminators.
- The S2 Lean proof.
- A d = 4 numerical chessboard test, and SU(2) Monte Carlo in d = 4. The only exact tests were in d = 2, where every plaquette lies in reflection planes and the image count is N (not N/4).
- Literature locators: I fetched nothing.

## 5. Delegated questions and outcomes

- **Child (child-run1, sonnet), question A4:** compute G(n) for n = 0..16, its sign, and the decay exponent.
  - Control (∫1 d⁴k/(2π)⁴ = 1): answered 1.0, **correct**, graded before I read anything else.
  - Returned: G(0) = 0.5, G(1) = 0.06887475, all G(n) > 0, p = 4.09 on n = 8..16, with n⁴G → 1/π².
  - I **reran** its g.py in a copy, `rerun_child/` (check K6). The output is identical, and it agrees with my independent lemmaGD values to within 4.8e-8, which is my print rounding.
  - The child's register verifies PASS.
  - Its rerun instructions start with `rm -f` of the result files. That conflicts with the spirit of the never-overwrite rule; the values are unaffected.
- **Grandchild (spawned by the child), question:** recompute G(0) and G(1) by a direct 4D grid, with control ∫4sin²(k/2)dk/2π = 2.
  - Control passed.
  - Returned G(0) = 0.5 and G(1) = 0.0688747462 (Richardson extrapolation). The child reran it.
  - I did not rerun the grandchild myself, but its value agrees with mine and the child's to within 1e-9.

## 6. Commands to rerun (from /home/user/z4-workers/a8-chalB2)

Results files are opened with mode "x", so give a new output name (or a fresh copy) on each rerun.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
$P check --ws pcp --name chess2d --expect-exit 0 -- python3 chess2d.py chess2d_results_NEW.txt
$P check --ws pcp --name lemmaGD-run3 --expect-exit 0 -- python3 lemmaGD.py lemmaGD_results_NEW.txt   # exits 1 (D1b)
mkdir rerun_child2 && cp child/g.py rerun_child2/ && $P check --ws pcp --name child-g-rerun --cwd rerun_child2 --expect-exit 0 -- python3 g.py
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last line of `$P verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`:
`A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
