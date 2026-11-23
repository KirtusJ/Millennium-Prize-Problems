**Proved (conditional): liminf_{β→∞} (−log m_eo)/√β ≥ c* = 4.6054132, provided Lemma F holds: ε_eff(a) ≥ 2 asinh(sin a) − o(1) uniformly in a ∈ [0,π]. Lemma F is reduced exactly to a one-dimensional Legendre problem and checked numerically (deficit 0.65/β to 0.98/β at β = 64, 256, 1024), but it is NOT proved. Unconditionally, nothing sharper than A4's e^{−C√β} ≤ m_eo ≤ e^{−c√β} (unspecified c < C) is proved here. The other half, limsup ≤ c*, is MISSING: its route is outlined below, and the step that loses the constant in A4's argument is identified.**

Worker m1-agmon (task T129). "PROVED" means proved in writing by me in this file. No one else has reviewed it, and I share a model family with the director, so my agreement is not independent review. Nothing was fetched from the network, so no paper is cited. Classical Agmon / Helffer–Sjöstrand theory is the inspiration only and is not relied on.

## 0. Setting and notation

- **Space.** X = SU(2)², with probability Haar measure. Points are x = (U₁, U₂), and a_i is the class angle of U_i. In quaternion coordinates U = (x₀, x₁, x₂, x₃), x₀ = cos a.
- **Kernel.** k(g) = e^{β cos θ(g)}/Z, where θ(g) is the class angle of g. (K_i f)(x) = ∫ k(g) f(…U_i g…) dg, and K = K₁K₂. K_i acts on Peter–Weyl degree n as I_{n+1}(β)/I₁(β) > 0, so K_i ≥ 0 and K_i has a square root.
- **Potential and transfer.** V = 2β|u₁×u₂|². T = e^{−V/2} K e^{−V/2}.
- **Ground state.** g is the top eigenvector of T on gauge-invariant functions. It is positive, it is in sector ee, and λ = λ_ee.
- **Single-link valley energy.** ε(a) = 2 asinh(sin a) = arccosh(1 + 2 sin²a), and c* = ∫₀^π √(2ε) = 4.6054132.
- **Which flip.** By the exchange symmetry U₁ ↔ U₂, λ_eo = λ_oe. I write the odd flip as U₁ → −U₁, which acts as a₁ → π − a₁.

## 1. Fibre operator: exact reduction (Lemma R). PROVED

Fix U₁ with class angle a, and put s = sin a. Up to conjugation, which commutes with K₂, the potential is V_a(U₂) = 2βs²(x₁² + x₂²). Define F_a = e^{−V_a/2} K₂ e^{−V_a/2} on L²(SU(2)) and ε_eff(a) := −log‖F_a‖.

**(i) The fibre well is a circle, not two points.** V_a vanishes on the whole circle {x₁ = x₂ = 0} = {U₂ commuting with U₁}. The brief's picture of a top eigenfunction "concentrated at the two points U₂ = ±1" is wrong. The eigenfunction is spread uniformly along that circle and is Gaussian across it (DEFECT of the brief's heuristic; it does not affect the exponent).

**(ii) Reduction to one variable.** The proof has three steps.
- F_a commutes with U ↦ e^{iφσ₃} U e^{iψσ₃}. These maps rotate the (x₀, x₃) and (x₁, x₂) planes, and K₂ commutes with left and right translations.
- The kernel of F_a is strictly positive, so the top eigenvalue is simple and its eigenvector is positive. It is therefore invariant under the symmetry, and so it is a function of t = x₀² + x₃² − x₁² − x₂² ∈ [−1, 1].
- Under Haar measure t is uniform, because the volume form in Hopf coordinates is ∝ d(cos 2χ). The bi-invariant functions of degree 2j are √(2j+1) P_j(t), since D^j₀₀ = P_j(cos 2χ). Finally, V_a = βs²(1 − t).

Hence ε_eff(a) = −log λ_max(M), where M_jk = √l_j ⟨P̃_j, e^{−βs²(1−t)} P̃_k⟩_{dt/2} √l_k and l_j = I_{2j+1}(β)/I₁(β).

**(iii) Numerical values** (eps_eff.py; the child's code is independent and agrees to 10 digits). ε_eff − ε = −c(a)/β, with:

| a | 0.05 | 0.1 | 0.3 | 0.6 | 1.0 | π/2 |
|---|---|---|---|---|---|---|
| c(a) | 0.98 | 0.95 | 0.86 | 0.76 | 0.68 | 0.65 |

These values are the same at β = 64, 256 and 1024 to within 2%. So ε_eff → ε, from below, at rate O(1/β). This is MEASURED, not proved.

## 2. Lemma F (needed, MISSING)

**Statement.** For every η > 0 there is β₀ such that for β ≥ β₀ and all a ∈ [0, π], ε_eff(a) ≥ ε(a) − η.

**Status.** Supported by §1(iii) at 8 angles and 3 values of β (deficit ≤ 1.04/β), but NOT proved.

**Suggested route (CLAIMED feasible, not done).** Use a Schur/Barta test on the reduced positive kernel in t, with ψ(t) = exp(−βα(1−t)/2) and α the flat-space harmonic ground-state exponent: ‖F_a‖ ≤ sup_t (F_a ψ)(t)/ψ(t). This reduces Lemma F to a uniform pointwise inequality. The errors to control are curvature, non-Gaussianity of k, and the far region where V is large.

## 3. Lemma K: exponential moments of the Wilson kernel. PROVED

The proof writes g = exp(X) with X ∈ su(2) ≅ ℝ³ and θ = |X| ≤ π, so that dg ∝ (sin θ/θ)² d³X.

**Statement.** Let β > 1, p ∈ ℝ³, H ≥ 0 and 0 < η ≤ 1, and put β' = β(1 − 5η²/48) − √β H. If β' > 0, then

 ∫ k(g) cosh(√β p·X) e^{√β H θ²/2} dg ≤ [ (β/β')^{3/2} e^{|p|²β/(2β')} + (β/2π)^{3/2} · 2π² · e^{−β(1−cos η) + √β(|p|π + Hπ²/2)} ] / (1 − 1/β).

**Proof.**
- *Inner region, θ ≤ η.* Here 1 − cos θ ≥ (θ²/2)(1 − 5η²/48). This is Lean-checked as `one_sub_cos_ge`, from Mathlib's `Real.cos_bound`. Also sin θ/θ ≤ 1. Extend the integral to ℝ³ and use ∫ e^{−β'|X|²/2} cosh(√β p·X) d³X = (2π/β')^{3/2} e^{β|p|²/(2β')}.
- *Outer region, η < θ ≤ π.* Here cos θ − 1 ≤ cos η − 1, and the total mass of (sin θ/θ)² d³X is 2π².
- *Denominator.* sin θ/θ ≥ 1 − θ²/6, and (1 − θ²/6)² ≥ 1 − θ²/3. On θ > √3 the integrand e^{−βθ²/2}(1 − θ²/3) is negative, so ∫_{θ≤√3} ≥ ∫_{ℝ³} = (2π/β)^{3/2}(1 − 1/β). ∎

**Consequence.** Take η = β^{−1/8}. For |p| ≤ P and H bounded, the right side is e^{|p|²/2 + O_{P,H}(β^{−1/4})}. The error is additive, not multiplicative in p².

**Checked numerically** (kernel_lemma.py run2): the bound holds in 50/50 cases on the grid β ∈ {16, …, 4096}, p ∈ {0.25, …, 3}, H ∈ {0, 1}. At β = 4096 the exact ratio log R/(p²/2) is 1.0000 to 1.0002 (H = 0).

**DEFECT in the brief's "needed bound".** The brief asks for ∫ k e^{√β p d(g)} dg ≤ e^{p²/2(1 + O(p/√β))} with the radial distance d(g) = θ. This is false at small p: the left side is E e^{p|Z|} with Z a 3-D standard Gaussian, which is about 1 + 1.6p. Measured: log R_rad/(p²/2) = 13.2 at p = 0.25 for every β. The correct object is a C² weight. Its increment is ⟨∇Φ, X⟩ + O(H|X|²), and cosh symmetrises the linear part.

## 4. Agmon inequality with a weight in the slow link only. PROVED (given Lemma F, for the use in §5)

Let Φ be a function of a₁ alone such that Φ∘a is C² on SU(2) (for example, constant near a₁ = 0 and a₁ = π). Put h = e^{√βΦ} g.

**Key identity.** Write B = K₂^{1/2} e^{−V/2}. Then T = B* K₁ B. Since Φ commutes with B,
 λ h = B* (e^{√βΦ} K₁ e^{−√βΦ}) B h.
- **Fibre bound.** B*B = e^{−V/2} K₂ e^{−V/2} is the direct integral over U₁ of F_{U₁}, and ‖F_{U₁}‖ = e^{−ε_eff(a₁)}. Hence for any function m(U₁) ≥ 0, ∫ m |Bh|² = ‖B m^{1/2} h‖² ≤ ∫ m e^{−ε_eff(a₁)} |h|².
- **Schur step.** The conjugated K₁ has a positive kernel. Using |f(x)f(y)| ≤ (f(x)² + f(y)²)/2 and symmetrising gives
 ⟨f, e^{√βΦ} K₁ e^{−√βΦ} f⟩ ≤ ∫ w(U₁) |f|², where w(U₁) = ∫ k(γ) cosh(√β(Φ(U₁γ) − Φ(U₁))) dγ.
- **Result.** Combining the two:
 λ ‖h‖² ≤ ∫ e^{log w(a₁) − ε_eff(a₁)} |h|². (A)
 By Lemma K, with |∇(Φ∘a)| = |Φ'(a)| and H = ‖Hess(Φ∘a)‖_∞, we have log w ≤ Φ'(a)²/2 + o(1).

This answers the brief's question of which operator inequality is true. "T ≤ e^{−ε_eff/2} K₁ e^{−ε_eff/2}" is not what is used. The Schur step turns the conjugated K₁ into the multiplication operator w(U₁), which commutes with B, so the "K₁ moves a₁ between half-steps" problem disappears.

**Choice of weight.** Fix δ, η, τ ∈ (0, 1).
- On [0, π/2] let f(a) = ∫₀^a √(2(ε − η)₊). Extend f symmetrically, f(π − a) = f(a), and smooth the concave kink at π/2 on a window of width τ, keeping |f̃'| ≤ |f'|.
- To make Φ∘a C² at the edge of I, replace √(2(ε − η)₊) by √(2ρ_η(ε)). Here √ρ_η is smooth, ρ_η ≤ (ε − η)₊, and ρ_η ≥ ε − 2η for ε ≥ 3η. This changes c*_η by O(√η) only, and that change vanishes as η → 0.
- Put Φ = (1 − δ) f̃. Then Φ = 0 on the inner set I = {ε(a₁) < η}, which is a neighbourhood of a₁ ∈ {0, π}, and Φ∘a is C² with H depending only on (η, τ).
- Assume Lemma F with η/4. On I^c, (A) gives the exponent q ≤ (1 − δ)²(ε − η) − ε + η/4 + o(1) ≤ −3η/4 + o(1). On I, q ≤ η/4 + o(1).
- λ_ee ≥ 1 − O(β^{−1/3}). This is PROVED by a short trial-function argument: a bump of radius β^{−1/3} at (1, 1), where V ≤ 2β·r⁴ and 1 − ⟨φ, Kφ⟩ = O(1/(βr²)). It is also CITED from context/A4_center_bounds.md, Setup ("1 − λ₀ = O(h)"), read locally; its proof was not checked by me. So λ ≥ e^{−η/4} for β large.
- Then ∫_{I^c} (λ − e^q)|h|² ≤ ∫_I (e^q − λ)|h|², which gives ‖e^{√βΦ} g‖² ≤ C(η) ‖g‖². (B)

## 5. From (B) to the splitting. PROVED (given (B))

**Sign trial.** Let s = sign(π/2 − a₁). It is odd under the flip, gauge invariant, and s² = 1. With A = {a₁ < π/2}, the exact identity for symmetric positive kernels gives
 λ_ee − λ_eo ≤ λ_ee − ⟨sg, T sg⟩ = ½ ∫∫ (s(x) − s(y))² g(x) T(x,y) g(y) = 2 ⟨g1_A, T g1_{A^c}⟩.

**Weight across the barrier.** f is L-Lipschitz with L = √(2ε(π/2)) = 1.8776, and the class angle is 1-Lipschitz. So for x ∈ A and y ∈ A^c,
 Φ(x) + Φ(y) ≥ (1 − δ)(c*_η − 2Lτ − L d₁(x, y)), where c*_η = ∫₀^π √(2(ε − η)₊) → c* as η → 0.
- T(x, y) ≤ K(x, y) because V ≥ 0.
- Schur gives sup_x ∫ K(x, y) e^{√β L d₁} dy = E_k e^{√β L θ}. This is bounded uniformly in β: by the radial version of Lemma K it is ≤ E e^{L|Z|}(1 + o(1)). Measured value: 1.51 at L = 0.25.

**Conclusion.** λ_ee − λ_eo ≤ C(η, τ) e^{−√β(1−δ)(c*_η − 2Lτ)}, and m_eo ≤ (λ_ee − λ_eo)/λ_eo. Letting δ, τ, η → 0 gives liminf (−log m_eo)/√β ≥ c*, conditional on Lemma F. ∎

## 6. Why the slow-link weight is not lossy: the 2-D valley. PROVED (harmonic level)

- **The valley.** {V = 0} is the set of commuting pairs. Modulo conjugation it is the 2-D torus (a, b) of a common maximal torus, so the brief's "for a₂ not near a centre" is part of the valley.
- **Transverse energy.** Linearise at (e^{iaσ₃}, e^{ibσ₃}), with δ_i the perpendicular parts of u_i. Then u₁×u₂ ≈ e₃×(sin a δ₂ − sin b δ₁). The gauge direction is (sin a, sin b)w. The physical mode y = (sin a δ₂ − sin b δ₁)/S, with S² = sin²a + sin²b, has unit-variance step and potential 2βS²|y|². Its transverse energy is therefore ε_v(a, b) = 2 asinh(S) ≥ ε(a) (Lean: `valley_energy_ge`).
- **Agmon distance.** Every path from the well (0, 0) to (π, 0) or (π, π) has Agmon length ≥ ∫ √(2ε(a)) |da| ≥ c*. Equality requires sin b ≡ 0, so the minimiser is the brief's path. Paths through other valley points or through (π, π) cost strictly more, which is consistent with the measured m_oo/m_eo → 2.

This harmonic-level statement is CLAIMED as the explanation. The rigorous half (U) of §4–5 does not need it, because Lemma F already covers all of link 2.

## 7. Half (L): limsup ≤ c*. MISSING

- **What A4 proves.** A4 bounds (λ₀^N − λ_χ^N) below by inf_{D_R²} T^N, using a path argument (CITED, context/A4_center_bounds.md, "Lower bound by an explicit route", read locally). It bounds V pointwise along the route and pays an O(1) confinement and potential cost per step over N ~ L/s steps, so it gets only e^{−C√β} with C unspecified.
- **Where the constant is lost.** It is lost in that pointwise per-step bound. The sharp per-step cost is ε(a) + v²/2, the transverse ground energy plus the longitudinal Gaussian cost. Summed with v = √(2ε) it gives √β ∫ √(2ε) da = √β c*.
- **Sharp route (CLAIMED, not done).**
  1. Restrict paths to a transverse tube of fixed rescaled radius κ.
  2. Insert the positive ground state φ_{s(a_t)} of the κ-killed transverse problem, with energy → ε(a) as κ → ∞.
  3. Bound ⟨φ_{s'}, Q_s φ_s⟩ ≥ e^{−ε(a)}(1 − O(|Δs|)), with Δs = O(β^{−1/2}) per step, which is O(1) in total.
  4. Pay v²/2 per longitudinal step, and O(1)·N·o(1) for curvature and for the non-Gaussian kernel.
  5. Near the ends ε ~ 2a, and the dwell time √β ∫ da/(2√a) is finite.

  Combined with A4's |u| versus u comparison, this would give limsup ≤ c*. None of these steps is written as a proof here.

## Step tags (summary)

| step | tag |
|---|---|
| Lemma R (fibre reduction to Legendre in t) | PROVED |
| Lemma F (ε_eff ≥ ε − o(1) uniformly) | MISSING (numerically supported) |
| Lemma K (kernel moment bound) | PROVED; scalar core Lean-checked |
| Agmon inequality (A) and estimate (B) | PROVED given Lemma F |
| λ_ee → 1 | PROVED (sketch) / CITED (A4 Setup) |
| Sign-trial splitting bound | PROVED |
| Upper bound on the splitting, liminf ≥ c* | PROVED given Lemma F |
| 2-D valley: transverse energy and Agmon minimiser | PROVED at harmonic level, scalar core in Lean; relevance CLAIMED |
| Lower bound on the splitting, limsup ≤ c* | MISSING (route CLAIMED); unconditional e^{−C√β} CITED (A4) |
