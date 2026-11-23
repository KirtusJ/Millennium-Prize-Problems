## The proof (t = 0, then t > 0)

Notation:
- φ(v) = g(v)e^(−2s\|v\|²), with g(v) = \|v_⊥\|²/(2\|v\|) and v_⊥ = (v₁, v₂).
- a(k) = φ(k̂vec(k)). This is the brief's a at t = 0.
- C = (2/l⁶) Σ_q \|f̂_b(q)\|² G(q), with G(q) = Σ_k a(k) a(q−k) (B1 step 1, upheld).

1. **Lattice → continuum, termwise.** Take \|k\|_∞ ≤ K ≤ π/b and ε = K²b²/24 < 1.
   - From sin y ≥ y − y³/6: k̂_i ≥ \|k_i\|(1−ε).
   - Also k̂ ≤ \|k\|.
   - Hence a(k) ≥ (1−ε)² φ(k). Elsewhere a ≥ 0.
2. **Pair bound (second order in q).** Put u = p + q/2, w = q/2 − p.
   - The Gaussians combine exactly: e^(−2s(\|u\|²+\|w\|²)) = e^(−4s\|p\|²) e^(−s\|q\|²).
   - \|u\|\|w\| ≤ \|p\|² + \|q\|²/4.
   - \|u_⊥\|²\|w_⊥\|² ≥ (\|p_⊥\|² − \|q_⊥\|²/4)² ≥ \|p_⊥\|⁴ − \|p_⊥\|²\|q\|²/2 [Lean `perp_prod`, `sq_sub_ge`].
   - Hence 4g(u)g(w) ≥ \|p_⊥\|⁴/\|p\|² − (3/4)\|q\|² [Lean `pair_core`] ≥ p₁² + p₂² − p₃² − (3/4)\|q\|² [Lean `sq_div_ge`].
   - When the numerator is negative, the bound holds trivially.
   - An earlier version used (\|p\| + \|q\|/2)² for \|u\|\|w\|. It gave a first-order error of about 4.5·η and was vacuous, so I discarded it.
3. **Region.** For \|q\|_∞ ≤ Q ≤ K, keep the shifted cube \|p\|_∞ ≤ K′ = K − Q/2. Every kept term then has \|k\|_∞, \|q−k\|_∞ ≤ K. The lower bound is a product of 1-D sums S₀ = Σe^(−4sp²) and S₁ = Σp²e^(−4sp²) on grids of spacing Δ = 2π/l with arbitrary shift:
   G(q) ≥ (1−ε)⁴ e^(−s\|q\|²)/4 · [2L₁L₀² − U₁U₀² − (3/4)\|q\|² U₀³].
4. **1-D sums, uniform in shift.**
   - Full-line sums use Poisson summation, which is exact for Gaussians: \|ΔS₀/√(π/α) − 1\| ≤ δ₀ = 2Σ_{m≥1} e^(−m²l²/(4α)), with α = 4s. Likewise for S₁, with δ₁ = 2Σ\|1 − m²l²/(2α)\| e^(−m²l²/(4α)).
   - Truncation tails are bounded by the integral from K′ − Δ. This needs K′ − Δ ≥ 1/√α, so that the summand is decreasing there.
   - This is the Riemann-sum lemma used. Its hypothesis is a Schwartz function for Poisson, plus monotone tails.
5. **Linearize in \|q\|².** Write A = (1−ε)⁴(2L₁L₀² − U₁U₀²)/4 and B′ = (1−ε)⁴(3/16)U₀³ + sA.
   - Using e^(−x) ≥ 1 − x [Lean `gauss_lin`, needs B ≥ 0]: G(q) ≥ A − B′\|q\|² for \|q\|_∞ ≤ Q.
   - For \|q\|_∞ > Q, the requirement Q² ≥ A/B′ makes the right side ≤ 0 ≤ G.
   - Hence the bound holds for every BZ representative q.
6. **Sum against \|f̂_b\|².** Parseval gives Σ_q\|f̂_b\|² = l³P_b. So
   **C_{b,s}(0) ≥ L := (2/l³)[A P_b − B′ Ψ′_b].**
   - Asymptotically (l/√s → ∞, b/√s → 0): (2/l³)A s^(5/2) → (5/8)·√π/(640π²) = 1.754·10⁻⁴. The factor 5/8 is the angular loss of the x − y step.
   - With κ = 2.5, θ = 0.5 and b = √s/2 the numbers are 0.48·(true) and B′-term ≈ 3.4·(true)·s. So L ≈ 0.48·2.806·10⁻⁴ s^(−5/2)(P_b − 7.0 sΨ′_b).
7. **t > 0.**
   - The atoms W_{kk′} ≥ 0 at E = k̂ + k̂′ (B1 step 1). Jensen [Lean `jensen_exp`] gives C(t) ≥ C(0) e^(−t M₁/M₀).
   - B3 gives M₁ ≤ (4/l³)Φ√(A₀A₂) =: Ū₁, and M₀ = C(0) ≥ L. Hence C(t) ≥ L·exp(−t Ū₁/L).
   - Since Ū₁ ≍ Φ s^(−3), we get Ū₁/L ≍ (Φ/P_b) s^(−1/2). So c(τ) = c₀ e^(−c₂τ), with τ = t/√s.
8. **V3.** M₁/M₀ ≤ Ū₁/L and M₂/M₀ ≤ (4/l³)Φ(√(A₀A₄) + A₂)/L.
   - The numerators scale as s^(−3) and s^(−7/2) by the explicit U_q bounds.
   - So both ratios are ≤ const·s^(−1/2) and ≤ const·s^(−1), provided sΨ′_b/P_b stays below a fixed θ < A/(B′s) (≈ 0.14 here).

Missing step, named:
- The comparison of P_b and Ψ′_b with ∫f² and ‖∇f‖₂² is not done. For P_b, the aliasing lemma applied to f² at q = 0 gives P_b ≥ ∫f² − S₄(b/2π)⁴‖Δ²(f²)‖₁ (PROOF_FREE_BOUNDS 2b, cited, not rechecked).
- For Ψ′_b, I only have the crude bound (π²/4) l³ sup\|∇f\|². So the "‖∇f‖₂" form of V1 is **not proved**.
- The uniform-in-c form of the U_q bounds used in steps 7 and 8 is written in one line, not checked numerically.

