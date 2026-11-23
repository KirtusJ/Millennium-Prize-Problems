# Two-sided bound on C_b(t) in the free lattice Maxwell benchmark (r9-proof, builder)

Status: a written proof. Steps marked [Lean] are formalized in `R9Bounds.lean` (compiles with exit 0; only the standard axioms). All other steps are **proved in text only**. The numerical checks are in `bounds.py`, with results in `results_bounds_run1.json`.

## 0. Setting and hypotheses

- Periodic lattice with N³ sites, spacing b = ℓ/N, sites x ∈ {0..N−1}³ at physical positions bx. Momenta k ∈ (2π/ℓ)ℤ³, taken modulo 2π/b. BZ means the representatives with |k_i b| ≤ π.
- k̂_i = (2/b) sin(k_i b/2) and k̂ = |k̂|. P₃₃(k) = (k̂₁² + k̂₂²)/k̂² and w(k) = P₃₃(k) k̂/2 for k ≠ 0.
- **H1** (from STATEMENT.md; normalization confirmed by the earlier review, not rederived here): D_t(r) = ℓ⁻³ Σ_{k≠0} e^{ik·r} w(k) e^{−t k̂}.
- **H2** (Wick, from STATEMENT.md): C_b(t) = 2b⁶ Σ_{x,y} f(bx) f(by) D_t(b(x−y))².
- **H3**: f: T³_ℓ → ℝ is real, C⁴ and periodic, with ∫f ≠ 0. Notation: f̃(p) = ∫_T f(y) e^{−ip·y} dy for p ∈ (2π/ℓ)ℤ³, ‖f‖₁ = ∫|f| and D₄ = ‖Δ²f‖_{L¹(T)}.
- **H4**: N ≥ 3.
- fhat_b(q) = b³ Σ_x f(bx) e^{−iq·bx}. This function is (2π/b)-periodic in q.
- Constant: S₄ = Σ_{m∈ℤ³∖0} |m|⁻⁴. `bounds.py` bounds it rigorously by summing exactly over |m|_∞ ≤ 60 and bounding the tail by an integral: 16.3597 ≤ S₄ ≤ 16.5791.

## 1. Momentum representation (route step 1)

**Claim.** C_b(t) = (2/ℓ⁶) Σ_{k,k'≠0, BZ} |fhat_b(k+k')|² w(k) w(k') e^{−t(k̂+k̂')}.

*Proof.* Square H1:
D_t(r)² = ℓ⁻⁶ Σ_{k,k'} e^{i(k+k')·r} w(k) w(k') e^{−t(k̂+k̂')}.

Put this into H2 and exchange the finite sums. For real f and q = k + k':
b⁶ Σ_{x,y} f(bx) f(by) e^{iq·b(x−y)} = conj(fhat_b(q)) · fhat_b(q) = |fhat_b(q)|². ∎

Every term is ≥ 0, since w ≥ 0 and P₃₃ ∈ [0,1].

*Hypothesis test (before use).*
- N = 8, t ∈ {0.05, 0.1, 0.2}: position-space and momentum-space values agree to relative error ≤ 5.5·10⁻¹⁵. The tolerance was 10⁻¹⁰ (P0 in `bounds.py`, run K2).
- The sub-agent checked the same thing independently, with a brute-force k,k' double sum: ≤ 3.7·10⁻¹⁵. I reran its program (run K3) and got an identical result file.

**Spectral reading (text only).** O_b(f)Ω is centered, so it has no vacuum component. It is quadratic in the fields, so it lies in the two-photon sector. That sector is finite-dimensional because the lattice is finite. Its spectral measure μ_b is therefore finitely atomic and satisfies ∫e^{−tE} dμ_b = C_b(t).

Step 1 gives a second finite atomic measure: weights W_{kk'} = (2/ℓ⁶)|fhat_b(k+k')|² w(k) w(k') ≥ 0 at energies E_{kk'} = k̂ + k̂' ≥ 0. It has the same Laplace transform for all t > 0. Distinct exponentials are linearly independent, so the two measures coincide. Hence S5e (finite sums, index set = pairs (k,k')) applies directly to the spectral measure of e^{−τH} O_b(f) Ω.

## 2. Aliasing lemma

**Claim.** For q ∈ (2π/ℓ)ℤ³: fhat_b(q) = Σ_{m∈ℤ³} f̃(q + 2πm/b), and the sum converges absolutely.

*Proof.*
1. Expand f(y) = ℓ⁻³ Σ_p f̃(p) e^{ip·y}. This converges absolutely because |f̃(p)| ≤ D₄/|p|⁴ (below) and Σ|p|⁻⁴ converges in 3D.
2. Then b³ Σ_x e^{i(p−q)·bx} = b³N³ = ℓ³ if p ≡ q mod 2π/b, and 0 otherwise. ∎

**Decay.** For p ≠ 0: |p|⁴ f̃(p) = ∫ (Δ²f) e^{−ip·y}. This is integration by parts on the torus, with no boundary terms. So |f̃(p)| ≤ D₄/|p|⁴.

**Consequences.**
- (2a) Upper bound. Take q in the BZ. For m ≠ 0, |q_i + 2πm_i/b| ≥ π|m_i|/b, so |q + 2πm/b| ≥ π|m|/b. Hence
  F_b := max_q |fhat_b(q)| ≤ ‖f‖₁ + S₄ (b/π)⁴ D₄.
  A cruder bound with no condition on b also holds: F_b ≤ b³ Σ|f| ≤ ℓ³ sup|f|.
- (2b) Lower bound. Take q = 0. The aliases sit at |p| = 2π|m|/b, so
  |fhat_b(0)| ≥ |∫f| − S₄ (b/2π)⁴ D₄.

## 3. Upper bound (route step 2)

- (3a) [Lean: `jordan_khat`, using Mathlib's `Real.mul_le_sin` and `Real.sin_le`]. For b > 0 and |k_i b| ≤ π: (2/π)|k_i| ≤ |k̂_i| ≤ |k_i|. Hence (2/π)|k| ≤ k̂ ≤ |k|.
- (3b) [Lean: `factor_upper`]. 0 ≤ |fhat_b|² ≤ F_b² and u(k) := w(k) e^{−t k̂} ≥ 0. Together with step 1 this gives
  C_b(t) ≤ (2/ℓ⁶) F_b² S_b(t)², where S_b(t) = Σ_{k≠0, BZ} u(k).
  Checked numerically as P6.
- (3c) By 3a, w(k) ≤ k̂/2 ≤ |k|/2 and e^{−t k̂} ≤ e^{−(2t/π)|k|}. Write k = (2π/ℓ)n with n ≠ 0. Then
  S_b(t) ≤ (π/ℓ) Σ_{n∈ℤ³∖0} |n| e^{−a|n|}, with a = 4t/ℓ.
- (3d) **Lattice-sum lemma.** Σ_{n≠0} |n| e^{−a|n|} ≤ G(a) := 4π e^{√3a/2} (6/a⁴ + √3/a³).
  *Proof.* Let Q_n = n + [−½,½]³, which has unit volume. For y ∈ Q_n, |y − n| ≤ √3/2, so |n| ≤ |y| + √3/2 and e^{−a|n|} ≤ e^{√3a/2} e^{−a|y|}. Sum over n ≠ 0, and enlarge the region to ℝ³:
  ≤ e^{√3a/2} ∫_{ℝ³} (|y| + √3/2) e^{−a|y|} dy = e^{√3a/2} · 4π(6/a⁴ + √3/a³). ∎
  Checked as P4. On these cases the bound exceeds the lattice sum by a factor 7.7 to 22.
- **Result.** C_b(τ) ≤ V(τ) := (2/ℓ⁶) F² (π/ℓ)² G(4τ/ℓ)², with F = ‖f‖₁ + S₄ (b₀/π)⁴ D₄ for b ≤ b₀. The alternative F = ℓ³ sup|f| needs no b₀.

## 4. Lower bound (route step 3)

- (4a) [Lean: `keep_terms`, `keep_terms_card`]. Keep the four pairs (k, −k) with k ∈ {±(2π/ℓ)e₁, ±(2π/ℓ)e₂}. They are distinct and nonzero mod 2π/b because N ≥ 3 (H4).
  - For k = (2π/ℓ)e_1: k̂ = κ_N := (2N/ℓ) sin(π/N), P₃₃ = 1 and w = κ_N/2. The same holds for e₂.
  - Modes along e₃ must not be used: there P₃₃ = 0.
  Therefore C_b(t) ≥ (2/ℓ⁶) |fhat_b(0)|² κ_N² e^{−2tκ_N}.
- (4b) sin x / x is decreasing on (0, π]. So κ_N increases in N and lies in [κ₃, 2π/ℓ], with κ₃ = 3√3/ℓ.
  The function κ ↦ 2 log κ − 2tκ is concave, so on an interval κ² e^{−2tκ} is smallest at an endpoint:
  κ_N² e^{−2tκ_N} ≥ m(t) := min(κ₃² e^{−2tκ₃}, (2π/ℓ)² e^{−4πt/ℓ}).
- (4c) Choose b₀ = min(ℓ/3, 2π (|∫f| / (2 S₄ D₄))^{1/4}). By 2b, |fhat_b(0)| ≥ |∫f|/2 for b ≤ b₀.
- **Result.** v(τ) := (2/ℓ⁶) (∫f)²/4 · m(2τ) ≤ C_b(2τ) for all b ≤ b₀.

## 5. Theorem and corollary

**Theorem.** Assume H1–H4 and b ≤ b₀ (the b₀ of 4c, also used in F). Then for every τ > 0:
0 < v(τ) ≤ C_b(2τ) and C_b(τ) ≤ V(τ) < ∞,
with v, V, b₀ as defined in sections 3 and 4. None of them depends on b.

The theorem as posed is **true**. Nothing in it needed correcting.

Differences from the suggested route:
- The fhat bound comes from the aliasing lemma with D₄, not from "b³Σ|f| ≤ 2∫|f|".
- N ≥ 3 is needed.
- Modes along e₃ must be excluded.

**Corollary** [Lean: `window_from_two_sided`, combining keep_terms with S5e, copied verbatim from HeatRegularized.lean]. Apply S5e with the atoms of step 1. Then the regularized spectral measure of e^{−τH} O_b(f) Ω has mass ≥ v/2 in [0, E₀], with E₀ = (1/τ) log(2V/v), uniformly in b ≤ b₀.

The identification of the step-1 atoms with the spectral measure is text only (section 1). MeasureHeat M3 is not needed: at fixed b the measure is finite.

## 6. Concrete case: ℓ = 1, f(y) = Σ_m exp(−|y−m|²/(2R²)), R = 0.1

The normalization (peak 1) is my choice. STATEMENT.md does not fix it. The ratios below do not depend on it.

Constants:
- A = ∫f = f̃(0) = (2π)^{3/2} R³ = 0.0157496.
- Every alias f̃(2πm/b) = A e^{−2π²R²|m|²/b²} is positive. So fhat_b(0) ≥ A for every N, which gives F0 = A with no smallness condition.
- f > 0, so F_b ≤ b³Σf = fhat_b(0) = A θ_N³ ≤ A(1 + ε₈) for N ≥ 8, with ε₈ = 1.96·10⁻⁵. So b₀ = 1/8.
- v(τ) = 2A² m(2τ) and V(τ) = 2A²(1+ε₈)² π² G(4τ)².

| τ | v (proved) | C_b(2τ), N = 16 … 64 | C_b(τ), N = 16 … 64 | V (proved) | C/v | V/C | E₀ |
|---|---|---|---|---|---|---|---|
| 0.05 | 4.738·10⁻³ | 7.856 … 5.085 | 180.8 … 265.8 … 195.5 | 1.720·10⁷ | 1073–1658 | 6.5·10⁴–9.5·10⁴ | 454.1 |
| 0.1 | 1.587·10⁻³ | 0.1364 … 0.1166 | 7.856 … 5.085 | 1.057·10⁵ | 73–86 | 1.3·10⁴–2.1·10⁴ | 187.1 |

- The bracket holds in all 10 cases (P5).
- The bounds are loose. The lower bound loses a factor 73 to 1660, because it keeps only the four lowest modes. The upper bound loses a factor 10⁴ to 10⁵, because it replaces |fhat_b| by its sup and does not use the decay of f̃ on the scale 1/R.
- As a result the window E₀ (187 and 454) is 15 to 36 times the lowest atom, which is about 4π ≈ 12.57. That is valid, but far from sharp.

## 7. What is NOT proved

- Convergence of C_b(t) to C(t), and its rate (S2′). Only b-uniform bounds are proved.
- Uniformity in τ: v(τ) decays like e^{−8πτ/ℓ}, and V(τ) grows like τ⁻⁸ as τ → 0.
- Infinite volume: v ∝ ℓ⁻⁸ (∫f)² → 0 as ℓ → ∞. The lower bound uses the lowest box mode.
- H1, the normalization of D_t, is taken from STATEMENT.md and its review. It is not rederived here.
- The spectral identification (section 1), the aliasing lemma (2), the lattice-sum lemma (3d) and the monotonicity/concavity facts (4b): proved in text only.
- S₄ ≤ 16.58 comes from a program with an explicit integral tail bound. It is not formalized.
- Nothing here concerns interacting Yang–Mills.

---

## Review note (Director Z4, 23 November 2026)

Attacked by a challenger (`../reviews/r10-chal/`): every constant rederived and confirmed, with a non-symmetric f, odd and even N and box sides 0.5, 0.7, 1, 2. Two corrections to the text above, which is otherwise left as written:

1. Section 0: "BZ means the representatives with |k_i b| ≤ π" must read −π < k_i b ≤ π, each mode once. Read literally, the edge mode is counted twice for even N.
2. Hypothesis to add: the vacuum energy is subtracted, HΩ = 0. H1 already assumes it.

Literature: the continuum limit of abelian lattice gauge theory is treated by Gross and by Driver (Comm. Math. Phys. 110, 1987); see `../LITERATURE.md`. This proof is an elementary Gaussian computation used as a known-answer test and claims nothing beyond that.

Note, 23 November 2026 (second session): for the slice-flowed observable the route of steps 3b to 3d (the supremum of the sampled Fourier coefficient) gives s⁻⁴ where the truth is s^(−5/2); it is replaced there by a Schur and Parseval step, and "convergence with a rate" is proved for s > 0. See [`SPATIAL_FLOW.md`](SPATIAL_FLOW.md), section 3.
