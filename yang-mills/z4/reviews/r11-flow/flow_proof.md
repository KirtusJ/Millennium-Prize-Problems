# The spatially flowed, sharp-time B₃² in the free lattice Maxwell benchmark (r11-flow, builder)

Status: a written proof. Steps marked [Lean] are in `FlowWindow.lean` (this directory; exit 0, axioms propext, Classical.choice, Quot.sound only, log `lean_try2.log`) or in the r9 file `input/R9Bounds.lean`. Everything else is **proved in text only**. Numerical checks: `flow_bench.py` → `results_flow_run1.json`, `flow_box.py` → `results_box_run1.json`.

## 0. Setting and hypotheses

Same setting as `input/PROOF_FREE_BOUNDS.md` (the r9 proof), with its review corrections:
- BZ means −π < k_i b ≤ π, with each mode counted once.
- HΩ = 0.
- N ≥ 3.

Notation used below:
- k̂, P₃₃, w(k) = P₃₃ k̂/2.
- H1: the unflowed D₀ normalization, taken from STATEMENT.md and its review. It is not rederived here.
- H3: f real, C⁴, periodic, with ∫f ≠ 0.
- fhat_b(q) = b³Σ_x f(bx)e^{−iq·bx}.
- P_b := b³Σ_x f(bx)².
- s > 0 is the flow time; t and τ are Euclidean times.

## 1. The flow convention (derived)

Take the quadratic magnetic action in lattice units, S_M = ½Σ_p θ_p², with θ = C A, where C is the lattice curl from links to plaquettes. Its gradient flow in **lattice** flow time σ is dA/dσ = −∂S_M/∂A = −CᵀC A. Put σ = s/b², so that s has physical units (length²).

In Fourier space:
- Let D_i = e^{ik_ib} − 1. Then |D_i|² = b²k̂_i².
- The plaquette field is θ_ij(k) = D_iA_j − D_jA_i.
- CᵀC = curl†curl = |D|²·1 − D D†. This is b²k̂² times the projector onto the vectors orthogonal to D, i.e. the transverse ones.

Consequences:
- Longitudinal (pure-gauge) components do not move.
- Transverse components are multiplied by e^{−σ b²k̂²} = **e^{−s k̂²}**.
- θ depends only on the transverse part, so B^s₃(k) = e^{−sk̂²}B₃(k).
- The equal-time two-point function carries **e^{−2sk̂²}**:
  D^s(r) = ℓ⁻³Σ_{k≠0} e^{ik·r} u(k), with u(k) := w(k)e^{−2sk̂²}.

This convention is the linearization of Lüscher's ∂_tB_μ = D_νG_νμ, restricted to spatial directions. Its kernel is e^{−|x|²/4s}, with rms radius √(6s) in three dimensions. The √(8s) quoted in the task is the four-dimensional radius; the spatial flow's radius is √(6s).

The claim was checked directly on N = 4: build C, exponentiate CᵀC, take θ₁₂, and compare with the Fourier multiplier. Max error 5.7·10⁻¹⁵ (P0b).

**Continuum value.** ⟨B²⟩ = ∫d³k/(2π)³ · (2/3 angular average of P₃₃) · (|k|/2) · e^{−2sk²} = (1/(6π²)) ∫₀^∞ k³e^{−2sk²} dk = **1/(48π²s²)**.
- This is the convention above: e^{−sk²} on the field, e^{−2sk²} on the two-point function. It reproduces LITERATURE.md's value.
- If the field were multiplied by e^{−2sk²} instead (flow dA/ds = −2∂S/∂A), the value would be 1/(192π²s²).

## 2. Momentum representation

For the flowed observable:
Var_b := ⟨O_{b,s}(f)²⟩ = (2/ℓ⁶) Σ_{k,k'≠0} |fhat_b(k+k')|² u(k)u(k').

*Proof.*
1. B^s₃ is a linear function of the A's, and the vacuum is Gaussian. So Wick's theorem gives ⟨O²⟩ = 2b⁶Σ_{x,y} f f D^s(b(x−y))². O is centered, so there is no disconnected term.
2. Then repeat r9 §1 with e^{−tk̂} replaced by e^{−2sk̂²}. ∎

Checked against the position-space Wick sum at N = 8: relative error ≤ 1.8·10⁻¹⁵ (P0a).

**Spectral form (as r9 §1).** O_{b,s}Ω lies in the finite-dimensional two-photon space. Its spectral measure is ν_b = Σ W_{kk'} δ_{k̂+k̂'}, with W_{kk'} = (2/ℓ⁶)|fhat_b(k+k')|²u(k)u(k') ≥ 0. So:
- M_j := ⟨O(H−E₀)^jO⟩ = Σ W_{kk'}(k̂+k̂')^j.
- Var_b = M₀.

## 3. Lemmas

- **L1 (Cauchy–Schwarz).** For every q and nonnegative g, h on the BZ: Σ_k g(k)h(q−k) ≤ (Σg²)^{½}(Σh²)^{½}. The reason: k ↦ q − k is a bijection of the BZ.
- **L2 (Parseval).** Σ_{q∈BZ}|fhat_b(q)|² = b⁶N³Σ_x f(bx)² = ℓ³P_b.
- **L3 (P_b uniform).**
  - P_b ≤ ℓ³ sup f² for every b.
  - Sharper: apply the r9 aliasing lemma to f². This gives P_b ≤ ∫f² + S₄(b₀/2π)⁴‖Δ²(f²)‖₁ for b ≤ b₀.
  - For the Gaussian of §6 every alias is positive, and P_b ≤ (∫f²)·θ₁(16)³ for N ≥ 16, with θ₁(N) = Σ_m e^{−π²R²N²m²}.
- **L4 (one-dimensional sums).**
  - For a > 0: Σ_{n∈ℤ} e^{−an²} ≤ θ(a) := 1 + √(π/a). The function is decreasing on [0, ∞), so Σ_{n≥1} ≤ ∫₀^∞.
  - For m ≥ 1: Σ_{n∈ℤ} n^{2m}e^{−an²} ≤ T_m(a) := Γ(m+½)a^{−m−½} + 2(m/(ea))^m.
  - Reason for the second: x^{2m}e^{−ax²} is unimodal on [0, ∞) with maximum (m/(ea))^m [Lean: `gauss_factor_le`, from `pow_mul_exp_neg_le`: y^m e^{−y} ≤ m^m e^{−m}]. A unimodal g ≥ 0 satisfies Σ_{n≥1} g(n) ≤ ∫₀^∞ g + max g.
- **L5 (lattice sums).** For c > 0, m ≥ 1, and a = 16c/ℓ²:
  - Σ_{k∈BZ} k̂^{2m}e^{−ck̂²} ≤ 3^m(2π/ℓ)^{2m} T_m(a) θ(a)².
  - Σ_{k∈BZ} e^{−ck̂²} ≤ θ(a)³.

  *Proof.*
  1. k̂^{2m} = (Σ_i k̂_i²)^m ≤ 3^{m−1}Σ_i k̂_i^{2m}, by the power mean.
  2. e^{−ck̂²} = Π_i e^{−ck̂_i²}, so each term factorizes over coordinates.
  3. Per coordinate, with |k_ib| ≤ π: (2/π)|k_i| ≤ |k̂_i| ≤ |k_i| [Lean: R9 `jordan_khat`]. So k̂_i^{2m}e^{−ck̂_i²} ≤ k_i^{2m}e^{−(4c/π²)k_i²}.
  4. With k_i = 2πn/ℓ, the exponent is a n², a = 16c/ℓ².
  5. Enlarge the BZ to ℤ and apply L4. ∎

## 4. Theorems

Fix s > 0, f and ℓ. Define, with a_s := 64s/ℓ²:
- Ū_j := ¼·3^{j+1}(2π/ℓ)^{2j+2} T_{j+1}(a_s) θ(a_s)², for j = 0, 1, 2. This bounds U_j := Σ_k u(k)² k̂^{2j} ≤ ¼Σ k̂^{2j+2}e^{−4sk̂²}. The reason: u² ≤ (k̂²/4)e^{−4sk̂²}, since P₃₃ ≤ 1. Then use L5 with c = 4s.
- P̄ := sup_{b≤b₀} P_b, by L3.
- κ₃ = 3√3/ℓ, and m_s := min(κ₃²e^{−4sκ₃²}, (2π/ℓ)²e^{−4s(2π/ℓ)²}).
- b₀ as in r9 (4c). Then |fhat_b(0)| ≥ |∫f|/2 for b ≤ b₀; for f with nonnegative aliases, |fhat_b(0)| ≥ |∫f| for every b.

**Theorem 1 (variance).** For b ≤ b₀:
v₀ := (2/ℓ⁶)(∫f/2)² m_s ≤ Var_b ≤ V₀ := (2/ℓ³) P̄ Ū₀.

*Proof.*
- Upper bound: Var_b = (2/ℓ⁶)Σ_q|fhat_b(q)|²(u∗u)(q). By L1, (u∗u)(q) ≤ U₀. Then L2 and L3.
- Lower bound: every term is ≥ 0. Keep the four pairs (k, −k) with k = ±(2π/ℓ)e₁, ±(2π/ℓ)e₂. They are distinct mod 2π/b because N ≥ 3 [Lean: R9 `keep_terms`].
  - Each pair has q = 0, P₃₃ = 1 and u(k)u(−k) = (κ_N/2)²e^{−4sκ_N²}, with κ_N = (2N/ℓ)sin(π/N) ∈ [κ₃, 2π/ℓ].
  - x ↦ xe^{−4sx} is log-concave, so its minimum over [κ₃², (2π/ℓ)²] is at an endpoint. ∎

None of v₀, V₀, b₀ depends on b. V₀ ~ c∫f²·s^{−5/2} as s → 0 (with P̄ → ∫f²). This is the (√s)⁻⁵ of LITERATURE.md, up to the constant.

**Theorem 2 (energy moments).** For b ≤ b₀:
- M₁ ≤ M₁^up := (4/ℓ³) P̄ √(Ū₀Ū₁).
- M₂ ≤ M₂^up := (2/ℓ³) P̄ (2√(Ū₀Ū₂) + 2Ū₁).

*Proof.*
- M₁: by symmetry k ↔ k', M₁ = (4/ℓ⁶)Σ_q|fhat|²Σ_k (uk̂)(k) u(q−k). Apply L1, then L2 and L3.
- M₂: (k̂+k̂')² = k̂² + 2k̂k̂' + k̂'². So M₂ = (2/ℓ⁶)Σ_q|fhat|²[2Σ(uk̂²)(k)u(q−k) + 2Σ(uk̂)(k)(uk̂)(q−k)]. Apply L1 to each sum. ∎

**Corollary (window, no Euclidean-time regularization).** Let E* := 2M₁^up/v₀. The spectral measure of the sharp-time vector O_{b,s}(f)Ω has weight ≥ v₀/2 in [0, E*], for every b ≤ b₀ [Lean: `markov_window`, finite sums, with w ≥ 0, E ≥ 0, v > 0, M > 0].

So, at fixed s > 0, A4's original sharp-time conditions hold for the flowed observable, uniformly in the cutoff and in physical units:
- variance bounded below;
- variance bounded above;
- first and second moments bounded above;
- a fixed weight in a fixed window.

(M₁^up > 0 holds trivially.)

**Theorem 3 (⟨(B^s₃)²⟩).** ⟨(B^s₃)²⟩ = ℓ⁻³Σ_{k≠0}u(k). With a' = 32s/ℓ²:
- Upper: ⟨(B^s₃)²⟩ ≤ (1/(2ℓ³)) √(3(2π/ℓ)²T₁(a')θ(a')² · (θ(a')³ − 1)). By L1-type Cauchy–Schwarz, k̂ = k̂·1, and L5 with c = 2s. The k = 0 term of the θ³ bound equals 1 and is subtracted. As s → 0 the right side is ~ c/s².
- Lower: for M with 2M + 1 ≤ N:
  ⟨(B^s₃)²⟩ ≥ ℓ⁻³ Σ_{0<|n|_∞≤M} (4/π³)((k₁²+k₂²)/|k|) e^{−2s|k|²}, with k = 2πn/ℓ.
  The reasons: P₃₃ ≥ (4/π²)(k₁²+k₂²)/|k|², by Jordan per coordinate and k̂ ≤ |k|; k̂ ≥ (2/π)|k|; e^{−2sk̂²} ≥ e^{−2s|k|²}; and the other terms are ≥ 0.
  This is an explicit finite sum, independent of b for b ≤ ℓ/(2M+1).
  - **NOT PROVED in closed form:** that this lower bound is ≥ c/s² with an explicit c for all s. It holds for each s by evaluation, and numerically the ratio to the true value is constant (3.88 at M = 7 for the three s), which suggests the s⁻² form. A closed-form c would need M ~ ℓ/√s and a lattice-sum lower bound, which I did not write.

## 5. Concrete case (ℓ = 1, Gaussian f of width R = 0.1, peak 1, b ≤ b₀ = 1/16)

All aliases are positive, so |fhat_b(0)| ≥ ∫f and the factor ¼ in v₀ is dropped. Limits are Richardson extrapolations from N = 64 and 96, assuming an error ∝ b².

| s | v₀ | Var limit | V₀ | M₁ limit | M₁^up | M₂ limit | M₂^up | ⟨B²⟩ lower | ⟨B²⟩ limit | ⟨B²⟩ upper | E* |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.002 | 1.079e−2 | 6.5625 | 293.4 | 229.7 | 2.18e4 | 8759 | 1.86e6 | 136.0 | 527.05 | 8024 | 4.0e6 |
| 0.005 | 7.81e−3 | 0.48579 | 40.53 | 11.22 | 1904 | 278.0 | 1.03e5 | 21.63 | 83.834 | 1601 | 4.9e5 |
| 0.01 | 4.04e−3 | 0.055196 | 9.821 | 0.9711 | 326 | 17.90 | 1.24e4 | 5.277 | 20.453 | 503.3 | 1.6e5 |

How loose the bounds are:
- Var/v₀ is 608, 62 and 14. The lower bound keeps only four modes.
- V₀/Var is 45, 83 and 178. Most of this is the Jordan factor (π²/4)^{5/2} ≈ 9.5 in the Gaussian exponent, and the box-to-L1 replacement in L1.
- M₁^up/M₁ is 95 to 336, and M₂^up/M₂ is 212 to 694.
- So the proved window E* is 10⁵ to 10⁶ times larger than the actual mean-energy scale 2M₁/Var (70, 46 and 35). It is valid, but not useful as a number.

Other measured quantities:
- Var·(asymptotic (√π/(640π²))∫f²s^{−5/2})⁻¹ = 0.75, 0.55, 0.35. The LITERATURE.md asymptotic needs R ≫ √s; here √s/R = 0.45 to 1.

## 6. What is not proved

- The convergence of Var, M₁, M₂ and ⟨B²⟩ as b → 0. It is measured: the change from N = 64 to 96 is ≤ 0.9%.
- The rate of that convergence.
- A closed-form s⁻² lower constant for ⟨B²⟩.
- Uniformity in s. As s → 0, V₀ ~ s^{−5/2} and E* → ∞.
- Infinite volume: v₀ ∝ ℓ⁻⁸.
- H1 (normalization), which is taken from STATEMENT.md.
- The text-only lemmas L2 to L5. L4's unimodal-sum inequality is not formalized; only its pointwise maximum is.
- The finite-volume difference between the lattice limit and 1/(48π²s²). In the ℓ = 1 box the limit is the **box** sum. It is below the infinite-volume value by 0.11%, 0.71% and 3.1% at s = 0.002, 0.005 and 0.01. This is a power-law image effect of the massless kernel, roughly ∝ s²/ℓ⁴ (see report: failed predicates P5 and Q2).
- Nothing here concerns interacting Yang–Mills.
