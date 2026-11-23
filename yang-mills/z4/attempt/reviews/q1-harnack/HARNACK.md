**Proved here (in writing, unreviewed): the Harnack chain (H4) of TUNNEL_LOWER2.md, in pointwise form and with an absolute constant. For every x with a₁(x), a₂(x) ≤ π/2 and V(x) ≤ 2M², g(x) ≥ λ·m_B·k_min²/k_sup² · e^{−M²−K/2} · exp(−n₀ℓ(K_M) − n₁₂ℓ(K₀) − n₃ℓ(K_K)) (Theorem H4 below), where m_B is the g²-mass of the corner piece B = {a₁, a₂ ≤ a₋, V ≤ K}. With d = 3.65, ρ = 0.265, K = 1 this gives, on the junction R_well of TUNNEL_LOWER2 §2 and on the corner part of S, −log g ≤ 35(a₋ + r₀)√β + 0.5·ℓ(K_M)√M β^{1/4} + O(log β) − log(4m_B). The only inputs are Tg = λg with λ ≤ 1, g > 0 continuous, the σ₁, σ₂ symmetries, and m_B. m_B ≥ 1/4 − o(1) is Lemma M4, which is PROVED given (B); (B) is PROVED given Lemma F and λ_ee ≥ e^{−η/4}. That last bound is only a sketch in the sources (λ ≥ 1 − O(β^{−1/3})), and I did not recheck it. A lower bound on |f| is not needed: Lemma P' uses only Σ_S f², which M4 already gives. This closes H4. It does not close (E1), (E3) or continuum P', so the target limsup ≤ c* is still NOT proved.**

Worker q1-harnack (task T150). I share a model family with the director and with the authors of the input files, so my agreement is not independent review. No network source was used.

## 0. What I use, restated and rechecked

- X = SU(2)² with Haar probability measure. a_i is the class angle of U_i, which equals the geodesic distance from U_i to 1. u_i is the vector part, s_i = |u_i| = sin a_i, and V = 2β|u₁×u₂|².
- k(U,U') = e^{β cos θ}/Z, where θ is the geodesic distance and Z = 2I₁(β)/β (LEMMA_F I1, I2). The kernel factorises: T(z,z') = e^{−V(z)/2} k(U₁,U₁') k(U₂,U₂') e^{−V(z')/2}.
- ‖T‖ ≤ ‖K‖ ≤ 1, so λ := λ_ee ≤ 1. The kernel is continuous, so g = λ^{−1}Tg is continuous. The kernel is strictly positive, so g > 0, and g is the unique top eigenvector. Hence g∘σ₁ = g∘σ₂ = g, where σ_i: U_i → −U_i. V and K are invariant under both σ_i.
- **(sup) PROVED.** g(x) = λ^{−1}∫T(x,y)g(y)dy ≤ λ^{−1}‖T(x,·)‖₂ ≤ λ^{−1} sup T ≤ λ^{−1}k_sup², where k_sup = βe^β/(2I₁(β)) ≤ β√(2πβ)/(2D) (LEMMA_F I7). This is TUNNEL_LOWER2 (H-b), rechecked. P7 MET.
- **(I₁ up) PROVED.** I₁(z) ≤ (π/2)e^z/√(2πz).
  - The part of (1/π)∫₀^π e^{z cos t} cos t dt over [π/2, π] is ≤ 0.
  - On [0, π/2], cos t ≤ 1 and cos t ≤ 1 − 2t²/π². Lean: `one_sub_cos_ge_jordan`.
  - Extend the integral to [0, ∞) and evaluate the Gaussian.
  - P1 MET: the maximum ratio is 0.6366 ≈ 2/π, as z → ∞.
- **(k_min) PROVED.** If θ ≤ R/√β, then k ≥ √(2/π)β^{3/2}e^{−R²/2}. This uses cos θ ≥ 1 − θ²/2 (Lean `cos_ge_quad`) and (I₁ up). P3 MET.
- **(vol) PROVED.** The Haar probability volume of a geodesic ball of radius r in S³ is v(r) = (2/π)∫₀^r sin² = (2r − sin 2r)/(2π). For r ≤ 1/2 it satisfies v(r) ≥ 11r³/(24π). Lean: `x_sub_sin_ge` with x = 2r. P2 and P2b MET.
- **(infl) PROVED.** Suppose z is within geodesic distance ρ/√β of p in each link. The vector part is 1-Lipschitz in ℝ⁴, and the chord is at most the geodesic, so |δu_i| ≤ ρ/√β. Hence √(V(z)/2) ≤ √(V(p)/2) + ρ(s₁(p) + s₂(p)) + ρ²/√β. P6 MET, with a worst margin of −3.6·10⁻³.

## 1. The chain lemma (PROVED)

**Lemma Ch.** Let p₀ = x, p₁, …, p_n = y satisfy d(U_i(p_j), U_i(p_{j+1})) ≤ d/√β for i = 1, 2. Let B_j be the product of the geodesic balls of radius ρ/√β around p_j, with ρ ≤ √β/2. Put R = d + 2ρ. Then

 T^n(x,y) ≥ e^{−V(x)/2 − V(y)/2} k_min² Π_{j=1}^{n−1} exp(−ℓ(sup_{B_j} V)),
 ℓ(K') := K' + R² + log(π/2) + 2 log(24π/(11ρ³)).

Proof.
- Restrict the iterated integral to z_j ∈ B_j.
- Consecutive z's are within R/√β in each link, so each of the 2n kernel factors is ≥ k_min.
- Each interior z_j appears in two T factors and carries e^{−V(z_j)}. Bound V(z_j) by sup_{B_j} V.
- vol(B_j) = v(ρ/√β)². Finally k_min²v² = e^{−R²−log(π/2)−2log(24π/(11ρ³))}. ∎

P8 MET: a Monte-Carlo check of T² against the n = 2 bound at β = 64 and 256, 6/6 cases. The bound lies about 14.8 nats below the true value, so it is valid but lossy.

## 2. Geometry of the path (PROVED). This is TUNNEL_LOWER2 (H-c), corrected and made explicit

Fix x with a₁, a₂ ≤ π/2 and V(x) ≤ 2M², and fix y ∈ B = {a₁, a₂ ≤ a*, V ≤ K} with a* ≤ π/4. The path has four phases. Each phase is subdivided by arc length into the stated number of pieces, each piece of length ≤ d/√β.

- **Phase 0 (n₀ = ⌈(π/2)√M β^{1/4}/d⌉ steps).**
  - Let m = min(s₁, s₂). Rotate the axis of the link with the smaller s by conjugation. The rotation is about n₁×n₂, through the angle ψ ∈ [0, π/2] towards the line of the other axis (sign chosen).
  - The class angles are unchanged, and V(t) = 2βs₁²s₂² sin²((1−t)ψ) is nonincreasing, ending at 0.
  - The arc length is mψ ≤ (π/2)m sin ψ.
  - Also (m sin ψ)² ≤ m·max(s)·sin ψ = |u₁×u₂| ≤ M/√β. Lean: `phase0_len`.
  - Hence mψ ≤ (π/2)√M β^{−1/4}.
  - If m = 0 or the axes are undefined, then V = 0 already and the phase is trivial (stay put).
  - P4 MET on 2·10⁴ random pairs. The worst value of the length ratio is 0.997, so the bound is nearly sharp.
- **Phase 1 (⌈a₂(x)√β/d⌉ steps).** The pair is now commuting. Shrink U₂ to 1 along its one-parameter subgroup. The vector parts stay parallel, so V ≡ 0 (P5).
- **Phase 2 (⌈(a₁(x) + a*)√β/d⌉ steps).** With U₂ = 1, move U₁ along a geodesic to U₁(y). The length is ≤ a₁(x) + a₁(y), and V ≡ 0.
- **Phase 3 (n₃ = ⌈a*√β/d⌉ steps).** Grow U₂ from 1 to U₂(y) along its subgroup. V(t) = (sin(t a₂(y))/sin a₂(y))² V(y) ≤ V(y) ≤ K, because a₂(y) ≤ π/2. Lean: `phase3_mono`. P5 MET.

**The bounds on sup_{B_j} V come from (infl), with s_i ≤ 1 and β ≥ 1.**
- Phase 0: K_M = 2(M + 2ρ + ρ²)².
- Phases 1 and 2: K₀ = 2(2ρ + ρ²)².
- Phase 3: K_K = 2(√(K/2) + 2ρ + ρ²)².

The step counts depend only on x and on a*, not on y. Each phase can be padded by zero steps, so a single n works for all y ∈ B.

## 3. Theorem H4 (PROVED, given m_B)

For β ≥ max(1, 4ρ²), ρ ≤ 1/2 and x ∈ D_M := {a₁, a₂ ≤ π/2, V ≤ 2M²}:

 g(x) ≥ (λ m_B/k_sup²) · k_min² · e^{−M²−K/2} · exp(−n₀ℓ(K_M) − n₁₂ℓ(K₀) − n₃ℓ(K_K)),
 m_B = ∫_B g², n₁₂ = ⌈a₂(x)√β/d⌉ + ⌈(a₁(x) + a*)√β/d⌉.

Proof.
- g = λ^{−n}T^n g ≥ T^n g, because λ ≤ 1 and g > 0. So g(x) ≥ ∫_B T^n(x,y)g(y)dy.
- Apply Lemma Ch along the §2 chain. It holds uniformly in y ∈ B, since V(y) ≤ K and V(x) ≤ 2M².
- Finally ∫_B g ≥ ∫_B g²/sup g ≥ λm_B/k_sup². ∎

By σ₁, σ₂ the same bound holds at the other three corners.

**Corollary (junction and corners).**
- Take a* = a₋ = arcsin(sinh η). Then the corner piece of C_η = {ε(sin a_i) < 2η} is exactly {a_i < a₋}, and ε(sin a₋) = 2η, as in TUNNEL_LOWER2. Also a₋ ≤ π/4 for η ≤ 0.65.
- On supp φ_L: G > c₁ gives q < 2M²/(βα(S)), so V = 2βS²q < 2M²S/√(1+S²) < 2M². And E > c₂ gives a₂ < r₀.
- Hence R_well ⊂ D_M ∪ σ₁D_M, and C_η ∩ {V ≤ K} ⊂ D_{√(K/2)}.
- With d = 3.65 and ρ = 0.265, the program gives ℓ(K₀)/d = 8.35 (the minimum over d and ρ ≤ 1/2) and ℓ(K_K)/d = 9.09 at K = 1. So:
  - **junction:** −log g ≤ √β[8.35(2a₋ + r₀) + 9.09a₋] + R_β;
  - **corners:** −log g ≤ √β[8.35·3a₋ + 9.09a₋] + R_β;
  - in both cases at most 35(a₋ + r₀)√β + R_β;
  - R_β = (n₀ + 3)ℓ(K_M) + M² + K/2 + log(k_sup²/(λk_min²m_B)) = O(M^{5/2}β^{1/4}) + O(log β).
- Measured coefficient C_tot(η) = [ℓ₀(2a₋ + r₀) + ℓ_K a₋]/d, with r₀ = √(η sin a₋/4): 1.50, 3.00, 6.06, 12.6 at η = 0.05, 0.1, 0.2, 0.4. That is 0.33c*, 0.65c*, 1.3c*, 2.7c*, linear in η.
- M depends on η through c₁ = e^{−M²} ≲ G_min(e^{3η/4} − 1). So M² = O(log(1/η)), and M enters only the β^{1/4} term. Hence −log μ/√β → 35(a₋ + r₀) as β → ∞, and this → 0 as η → 0.

**Comparison with TUNNEL_LOWER2's claimed H4.**
- It claimed C(K, M) in front of √β. Here the coefficient is absolute, because the large-V part (phase 0) costs only O(β^{1/4}) steps.
- Its (H-a) constant e^{−r²} per link is weaker than the e^{−r²/2} here but valid.
- Its (H-c) sketch ("first decrease the transverse displacement, O(β^{1/4}) steps") is phase 0. The monotonicity of V and the length bound are now proved.

## 4. Numerical evidence on the 1D model (child T152, grandchild T154; my rerun agreed)

- −log(g(a)/g(0)) ≤ √βJ(a) + log β held in 12/12 cases, for β ∈ {256, 1024, 4096} and a ∈ {0.05, …, 0.4}. In fact √β(L − J) ∈ [−2.09, −0.05], so g is above the Agmon prediction.
- L ≤ 10a held in 12/12 cases. The largest L/a was about 0.7.
- This is consistent with H4, and H4 is lossy. The chain coefficient (about 8.35 per unit length) is far above the true cost: in 1D, J(a) ≈ (4/3)a^{3/2}.
- Caveat: L was evaluated at the grid point nearest a, while J was evaluated at a itself.
- The reduced SU(2)² eigenfunction was not computed.

## 5. Step tags

| step | tag |
|---|---|
| (sup), (I₁ up), (k_min), (vol), (infl) | PROVED; scalar cores in Lean (Harnack.lean) |
| Lemma Ch (n-step ball chain) | PROVED |
| Path geometry, phases 0–3, V monotone | PROVED (Lean: `phase0_len`, `phase3_mono`) |
| Theorem H4, given m_B | PROVED |
| Corollary: R_well and the corners of S, −log g ≤ 35(a₋+r₀)√β + O(M^{5/2}β^{1/4} + log β) | PROVED given M4 |
| m_B ≥ 1/4 − o(1) (Lemma M4) | PROVED given (B) (TUNNEL_LOWER2; first inequality rederived by me) |
| (B) | PROVED given Lemma F and λ ≥ e^{−η/4} (TUNNEL_THEOREM §4; read, not rechecked) |
| λ_ee ≥ 1 − O(β^{−1/3}) | CLAIMED (sketch in the sources; not rechecked) |
| lower bound on \|f\| | not needed (P' uses Σ_S f²) |
| (E1), (E3), continuum P', target limsup ≤ c* | MISSING (not my step) |
