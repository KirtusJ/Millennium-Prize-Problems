**The target limsup (−log m_eo)/√β ≤ c* is NOT proved. Proved in writing here (unreviewed): (i) the cut-off algebra that turns three local one-step estimates into a subsolution Tφ ≥ λ_ee φ on a tube along the valley, with a valley-direction cut-off that works because of the tilt gain (Lemma S4-alg, scalar core in Lean); (ii) ‖T_ΩΩ‖ < λ_ee on that tube (from Lemma F); (iii) the Agmon estimate (B) applies verbatim to the odd ground state f, and with links exchanged, so f² and g² put mass ≥ 1 − (1−λ)/(1−e^{−K}) − o(1) on the four corner wells intersected with {V ≤ K} (Lemma M4); (iv) one of the three local estimates (E2) follows from Lemma K. Still MISSING (written as sketches only, tagged CLAIMED): the local Gaussian estimates (E1) and (E3) with errors o(1) uniform on the tube, the Harnack chain (H4) giving g ≥ e^{−C(η+a₋+r₀)√β} on the corner/tube junction, and the continuum (flow) form of Lemma P'. Given those three, limsup ≤ c* follows by §5. Numerics (my own run and the child's, independent): −log[(Tφ)/φ] − (ε(S) − Ψ'²/2) = O(β^{−1/2}) with √β·|diff| ≤ 2.1 on 12 tube points at β = 256, 1024, 4096 (36/36 within 3/√β); the cut-off subsolution with η = 0.25 has Tφ/φ ≥ 1 at the tube points tested (see §6).**

Worker p1-lower2 (task T146). I share a model family with the director and the authors of the input files; this is not independent review. No network source used. Inputs read: TUNNEL_LOWER.md (Lemmas C, P', 1D proof), TUNNEL_THEOREM.md (§1 model, §3 Lemma K, §4 inequality (A), estimate (B), §6 valley linearisation), LEMMA_F.md (Lemma F, flat fixed point (I5), kernel e^{β⟨U,U'⟩}/Z (I1), Z = 2I₁/β (I2)).

## 0. Notation

- x = (U₁, U₂) ∈ SU(2)², u_i vector parts, a_i class angles, |u_i| = sin a_i.
- k(U,U') = e^{β⟨U,U'⟩}/Z; one step of K = K₁K₂ moves both links: x' = (U₁g₁, U₂g₂), g_i i.i.d. with density k. So T(x,x') = e^{−V(x)/2} k(U₁,U₁')k(U₂,U₂') e^{−V(x')/2}.
- V = 2β|u₁×u₂|². S² := |u₁|² + |u₂|² = sin²a₁ + sin²a₂. q := |u₁×u₂|²/S² (gauge invariant). So V = 2βS²q exactly.
- ε(s) = 2 asinh s, α(S) = 2S√(1+S²), A(S) = 1 + 2S² + 2S√(1+S²), log A = ε(S) (LEMMA_F I5).
- λ = λ_ee ≤ 1 (‖T‖ ≤ ‖K‖ ≤ 1).

## 1. Linear algebra at a valley point (PROVED)

At x₀ = (cos a + sin a e₃, cos b + sin b e₃), write g_i = exp(X_i), X_i ∈ ℝ³, and split X_i = X_i∥ e₃ + X_i⊥.
- Quaternion product: (c + s e₃)(1 + X) has vector part u + cX + s e₃×X + O(|X|²) (+ the e₃·X term in the scalar part). So δa_i = X_i∥ (the class angle moves only along e₃), and the perpendicular displacement of u_i is δ_i = cos a_i X_i⊥ + sin a_i e₃×X_i⊥ = R(a_i)X_i⊥, a rotation of X_i⊥ by a_i.
- u₁×u₂ = e₃×(sin a δ₂ − sin b δ₁) + O(|X|²). So, in the 6 tangent coordinates (X₁, X₂), the Hessian of V/(2β) at x₀ is the rank-2 form |sin a R(b)X₂⊥ − sin b R(a)X₁⊥|². (Signs: δ₂ multiplies sin a.)
- Decomposition of ℝ⁶: valley (X₁∥, X₂∥), dimension 2; physical transverse y = (sin a δ₂ − sin b δ₁)/S, dimension 2; gauge z = (sin b δ₂ + sin a δ₁)/S, dimension 2 (simultaneous conjugation by e^{w}, w ⊥ e₃, gives δ_i = sin a_i (w×e₃)); stabiliser = rotations about e₃, dimension 1; 3 − 1 = 2. Total 2 + 2 + 2 = 6.
- The map (X₁⊥, X₂⊥) ↦ y is a co-isometry (rows orthonormal because R(·) are rotations and (sin²a + sin²b)/S² = 1). So if X_i ~ N(0, I₃/β) then (X₁∥, X₂∥, y-step) are independent with variances 1/β, 1/β and I₂/β.
- Hence the linearised one-step problem is: two free Gaussian directions (a₁, a₂), one flat transverse oscillator in y ∈ ℝ² with T_y = e^{−βS²|y|²} N(y, I/β) e^{−βS²|y'|²}, and two gauge directions on which everything is constant. The flat transverse problem has the exact fixed point e^{−βα(S)|y|²/2} with eigenvalue 1/A(S) = e^{−ε(S)} (LEMMA_F I5, Lean `fixed_point`). Gauge-invariantly, |y|² = q to leading order.

## 2. The subsolution (step 1)

**Ansatz.** Fix η ∈ (0, η₀), a₋ with ε(sin a₋) = 2η, r₀ with r₀²/sin a₋ ≤ η/4, θ₀ > 0, ℓ ∈ (0, r₀/2), M > 0. Put
- Ψ(a) smooth nondecreasing, Ψ = 0 for a ≤ a₋/2, Ψ' = √(2(ε(sin a) + η)) on [a₋, π − a₋/2], flat after (as in the 1D Lemma S);
- Θ(a) = θ₀(√(a² + ℓ²) − ℓ) (smooth even, so Θ∘a₂ is C² on SU(2) with Hessian ≤ C θ₀/ℓ);
- G = exp(−β α(S) q/2), E = exp(−√β Θ(a₂)), c₁ = e^{−M²}, c₂ = e^{−√βΘ(r₀)};
- φ_L = μ e^{−√βΨ(a₁)} (G − c₁)₊ (E − c₂)₊, φ_R = φ_L∘σ (σ: U₁ → −U₁, a₁ → π − a₁), φ = max(φ_L, φ_R).
- Ω = {φ > 0} ∩ {a₁ ∈ [a₋, π − a₋]}. On the support, |a₂| < r₀ and q < 2M²/(βα(S)) (transverse radius O(M/√β)).

φ is gauge invariant (a₁, a₂, q are). Because ‖(G−c₁)₊‖_∞, ‖(E−c₂)₊‖_∞ ≤ 1, φ ≤ μ off Ω.

**Three local one-step estimates.** For x on the support of φ_L with a₁ ∈ [a₋, π − a₋/2], with o(1) uniform in x as β → ∞ (η, a₋, r₀, θ₀, ℓ, M fixed):
- (E1) lower: T(e^{−√βΨ} G E)(x) ≥ e^{−√βΨ}GE(x) · A₁, A₁ = exp(−ε(S) + (Ψ'² + |∇Θ|²)/2 − o(1)).
- (E2) upper: T(e^{−√βΨ} E)(x) ≤ e^{−√βΨ}E(x) · A₂, A₂ = exp(−V(x)/2 + (Ψ'² + |∇Θ|²)/2 + o(1)).
- (E3) upper: T(e^{−√βΨ} G)(x) ≤ e^{−√βΨ}G(x) · A₃, A₃ = exp(−ε(S) + Ψ'²/2 + o(1)).

Status:
- (E2) PROVED given Lemma K (TUNNEL_THEOREM §3): drop e^{−V(x')/2} ≤ 1; the kernel is a product, apply Lemma K on each link to the C² functions Ψ∘a₁ and Θ∘a₂ (bounded Hessian H ≤ C(η, a₋) and Cθ₀/ℓ). The symmetry X → −X of k turns e^{p·X} into cosh(p·X), so no factor 2. Error O_H(β^{−1/4}).
- (E1) CLAIMED (sketch, error budget complete but constants not written). Restrict the integral to |X_i| ≤ L/√β with L = β^{1/10} (positivity: a lower bound). On that set: Ψ(a₁') = Ψ(a₁) + Ψ'X₁∥ + O(L²/β·(|Ψ''| + |Ψ'| cot a₋)); same for Θ; βq' and V(x')/2 = β|u₁'×u₂'|² equal their linearisations at the nearest valley point up to O((M+L)³/√β); α(S') − α(S) = O(L/√β) multiplies βq' = O((M+L)²); the density of X is Gaussian up to e^{O(L⁴/β)} (as in Lemma K, 1 − cos θ = θ²/2 + O(θ⁴)) and Z from LEMMA_F (I2), (I7). The Gaussian integral is then exactly e^{(Ψ'² + |∇Θ|²)/2} · e^{−ε(S)} (§1 and I5); the truncation loses a factor 1 − O(e^{−(L−C(M))²/4}). Cross terms between the Θ-tilt and y vanish at a₂ ≥ M/√β (∇a₂ ∥ valley) and are O(θ₀M/(ℓ√β)) below. Total error O(β^{−1/2+3/10}) = o(1).
- (E3) CLAIMED, same as (E1) for the inner part, with the inner Gaussian integral extended to ℝ² (an upper bound) and the outer part |X| > L/√β bounded by e^{−√βΨ(x)} e^{−L²/4} (Ψ Lipschitz). This is an additive error; it is relative o(1) because G(x) ≥ c₁ = e^{−M²} on the support, with M fixed.

**Lemma S4-alg (PROVED; scalar core Lean `cutoff_identity`, `cutoff_pos`).** Write G = c₁ + g̃, E = c₂ + ẽ with g̃, ẽ > 0 on the support. Since (G−c₁)₊(E−c₂)₊ ≥ (G−c₁)₊(E−c₂) ≥ GE − c₁E − c₂G·[pointwise where used] and T is positive,
 Tφ_L/(μe^{−√βΨ}) ≥ A₁GE − A₂c₁E − A₃c₂G,
and exactly (ring identity)
 A₁GE − A₂c₁E − A₃c₂G − λg̃ẽ = g̃ẽ(A₁ − λ) + c₁ẽ(A₁ − A₂) + c₂g̃(A₁ − A₃) + c₁c₂(A₁ − A₂ − A₃).
[Precisely: T((G−c₁)₊(E−c₂)₊ e^{−√βΨ}) ≥ T((G−c₁)₊ (E − c₂) e^{−√βΨ}) ≥ T(GE e^{−√βΨ}) − c₁T(E e^{−√βΨ}) − c₂T((G−c₁)₊e^{−√βΨ}), and (G−c₁)₊ ≤ G.]
Sign of each term on the support, with D := ε(S) − ε(sin a₁) ≤ 2(S − sin a₁) ≤ r₀²/sin a₋ ≤ η/4 (Lean `sqrt_increment` for S − s ≤ (S² − s²)/(2s); ε is 2-Lipschitz):
- A₁ − λ ≥ e^{η − D − o(1)} − 1 ≥ e^{3η/4 − o(1)} − 1 > 0.
- A₁ − A₃ = e^{−ε(S)+Ψ'²/2}(e^{|∇Θ|²/2 − o(1)} − e^{o(1)}): positive where |∇Θ| ≥ θ₀/2 (i.e. |a₂| ≥ ℓ, which contains the a₂-edge {E ≤ 2c₂} for β large), negative but o(1)·e^{η} elsewhere; there ẽ ≥ E/2 ≥ e^{−√βΘ(ℓ)}/2 ≫ c₂, so the term c₂g̃(A₁ − A₃) is absorbed by g̃ẽ(A₁ − λ).
- A₁ − A₂ = e^{(Ψ'²+|∇Θ|²)/2}(e^{−ε(S)−o(1)} − e^{−V(x)/2+o(1)}): positive where V(x)/2 ≥ ε(S) + 1; where V(x)/2 < ε(S) + 1 one has G ≥ G_min := e^{−α(ε(S)+1)/(2S²)} (because βαq/2 = (α/(2S²))·V/2), so g̃ ≥ G_min − c₁ ≥ G_min/2 for M large, and c₁ẽ|A₁ − A₂| ≤ c₁ẽ e^{2+...} is absorbed by g̃ẽ(A₁ − λ) once c₁ ≤ G_min(e^{3η/4}−1)e^{−C}/4.
- c₁c₂(A₁ − A₂ − A₃): at the a₂-edge with g̃ ≫ c₁ it is absorbed by c₂g̃(A₁ − A₃) (which is ≥ c₂g̃·cθ₀²); at the transverse edge (V large, A₂ ≈ 0) by c₁ẽ(A₁ − A₂) ≥ c₁ẽA₁/2 when ẽ ≫ c₂, and in the corner by c₁c₂(A₁ − A₃) > 0 when |∇Θ| ≥ θ₀/2.
Hence Tφ_L ≥ λφ_L on the support of φ_L for β ≥ β₀, given (E1)–(E3). With φ = max(φ_L, φ_R): Tφ ≥ Tφ_L ≥ λφ_L = λφ where φ_L ≥ φ_R (and symmetrically). This is the 1D "reflected branch" step. Tag: the algebra is PROVED; its inputs (E1), (E3) are CLAIMED.

**‖T_ΩΩ‖ < λ (PROVED given Lemma F).** T = B*K₁B with B = K₂^{1/2}e^{−V/2}; 1_ΩT1_Ω = (B1_Ω)*K₁(B1_Ω), so ‖T_ΩΩ‖ ≤ ‖1_Ω B*B 1_Ω‖ ≤ sup_{a₁∈[a₋,π−a₋]} ‖F_{a₁}‖ ≤ e^{−ε(sin a₋) + η/2} = e^{−3η/2} by Lemma F (LEMMA_F.md, η/2-form). λ ≥ 1 − O(β^{−1/3}) (TUNNEL_THEOREM §4, trial bump) gives ‖T_ΩΩ‖ < λ.

**Lemma C then gives g ≥ φ on Ω**, provided φ ≤ g on Ω^c, i.e. g ≥ μ on R_well := supp φ ∩ {a₁ < a₋ or a₁ > π − a₋} (φ = 0 elsewhere off Ω). That is step 2.

## 3. Mass and Harnack in the wells (step 2)

**(B) applies to f (PROVED, by rereading TUNNEL_THEOREM §4).** The proof of (A) uses only: Tu = λ_u u; the factorisation T = B*K₁B; the fibre bound ‖F_{U₁}‖ ≤ e^{−ε_eff(a₁)}; and the Schur step ⟨F, e^{√βΦ}K₁e^{−√βΦ}F⟩ = ∫∫ k cosh(√β(Φ(x)−Φ(y))) F(x)F(y) ≤ ∫ w F², valid for any real F (|F(x)F(y)| ≤ (F(x)² + F(y)²)/2). No positivity of u is used. (B) then needs only λ_u ≥ e^{−η/4}. For u = f this holds: the odd trial b − b∘σ with b a gauge-invariant bump of radius β^{−1/3} at (1,1) (made even in U₂ → −U₂) has disjoint supports from its image and ⟨b, Tσb⟩ ≤ e^{−cβ}, so λ_eo ≥ 1 − O(β^{−1/3}) (sketch, same as for λ_ee). So ‖e^{√βΦ(a₁)} f‖ ≤ C(η).
- Exchange: K₁, K₂ commute (different links), so T = B'*K₂B' with B' = K₁^{1/2}e^{−V/2}; the same proof gives ‖e^{√βΦ(a₂)}u‖ ≤ C(η) for u ∈ {f, g}.

**Lemma M4 (PROVED given (B)).** Let C_η = {ε(sin a₁) < 2η, ε(sin a₂) < 2η} (the four corners (a₁,a₂) ∈ {0,π}²). For u ∈ {f, g}, ‖u‖ = 1, and K > 0:
 ∫_{C_η ∩ {V ≤ K}} u² ≥ 1 − (1 − λ_u)/(1 − e^{−K}) − 2C(η)e^{−2√β φ_min(η)}.
Proof: λ_u = ⟨e^{−V/2}u, K e^{−V/2}u⟩ ≤ ∫e^{−V}u² ≤ 1 − (1 − e^{−K})∫_{V>K}u²; and (B) in each link bounds ∫_{ε(sin a_i) ≥ 2η} u². ∎ Each corner carries 1/4 of it by the symmetries (g: σ₁, σ₂ even; f: σ₁ odd, σ₂ even; f² is σ₁-even).

**Lemma H4 (Harnack chain; CLAIMED, sketch).** Let D_K = (C_{η'} ∩ {V ≤ K}) ∪ R_well. Claim: for x ∈ D_K, g(x) ≥ μ := exp(−C(K, M)(η + a₋ + r₀)√β − C β^{1/4} − C log β).
- (H-a) per-step bound PROVED: for d(z,z') ≤ r/√β on both links, T(z,z') ≥ e^{−(V(z)+V(z'))/2} (c β^{3/2} e^{−r²})² (k = e^{β⟨U,U'⟩}/Z, e^{β⟨U,U'⟩} = e^{β}e^{−β|U−U'|²/2}, Z = 2I₁(β)/β ≤ C e^β β^{−3/2}).
- (H-b) sup g ≤ C β³ PROVED (g = λ^{−1}Tg, sup T(x,·) ≤ (sup k)², Cauchy–Schwarz).
- (H-c) geometry CLAIMED: every point of D_K is joined to every point of B := C_η ∩ {V ≤ K} by a chain of ≤ n = C(η + a₋ + r₀)√β + Cβ^{1/4} steps of length ≤ 1/√β staying in {V ≤ K'} (first decrease the transverse displacement, which takes O(β^{1/4}) steps where S ≥ β^{−1/4}, and none needed inside |u_i| ≤ β^{−1/4} where V ≤ 2; then move along the valley).
- Then g(x) = λ^{−n}(T^n g)(x) ≥ (c')^n β^{−O(1)} ∫_B g ≥ (c')^n β^{−O(1)} ∫_B g²/sup g, with ∫_B g² ≥ 1/4 − o(1) by M4.
Since a₋ ~ η, r₀ ~ η and η → 0 at the end, −log μ = o(√β) in the double limit β → ∞ then η → 0, exactly as in the 1D Lemma H.

## 4. What Lemma P' needs, and gets

Lemma P' (TUNNEL_LOWER §1) needs: a σ-invariant S, paths in S from x to σx of length ≤ n = O(√β), a lower bound on Q(e) = T(z,z')g(z)g(z') along the paths, and a lower bound on Σ_S f².
- S = (C_η ∩ {V ≤ K}) ∪ (tube along a₂ ≈ 0) ∪ (its U₂ → −U₂ image). Σ_S f² ≥ 1 − o(1) − (1−λ_eo)/(1−e^{−K}) by M4. PROVED given (B).
- g along the paths: ≥ μ on the corner parts (H4, CLAIMED), ≥ φ ≥ μ(1−c₁)(1−c₂)e^{−√βΨ(a₁)} on the tube core (Lemma C + §2, given (E1),(E3),(H4)).
- Continuum form: in SU(2)² single paths have measure zero; P' must be used with flows (each x sends a unit of flow spread over balls of radius ~1/√β). The discrete proof (Cauchy–Schwarz along γ_x) carries over to flows with ρ_S = sup over (z,z') of flow density / Q(z,z'). MISSING as a written proof (CLAIMED routine). This is the same gap TUNNEL_LOWER calls "1D continuum (κ → 0 with tubes): CLAIMED".

## 5. Conditional conclusion

Given (E1), (E3), (H4) and continuum P':
 Δ ≥ (Σ_S f²)/ρ_S ≥ ½ · β^{−O(1)} · μ² e^{−√β · 2Ψ(π/2)}, 2Ψ(π/2) ≤ ∫₀^π √(2(ε+η)) ≤ c* + π√(2η) (Lean L3 in TUNNEL_LOWER).
So −log m_eo ≤ −log Δ ≤ √β(c* + π√(2η) + 2C(η + a₋ + r₀)) + O(β^{1/4}) + O(log β), and limsup (−log m_eo)/√β ≤ c* + π√(2η) + C'η for every η; let η → 0. **Conditional, not proved.**

## 6. Numerical evidence (tube_ratio.py, results_main.txt; child T147 independent)

Core ratio, φ₀ = e^{−√βΨ₀(a₁)}G with Ψ₀' = √(2ε(sin a₁)) (η = 0, no cut-off), prediction pred = ε(S) − Ψ₀'²/2 = ε(S) − ε(sin a₁). n = 4·10⁵ antithetic pairs per β. diff = −log R − pred:

| a₁ | √β·diff at β=256 | 1024 | 4096 |
|---|---|---|---|
| 0.5 (4 pts) | +1.30 … +2.04 | +1.34 … +1.90 | +1.58 … +2.06 |
| π/2 (4 pts) | −0.48 … −0.22 | −0.42 … −0.32 | +0.18 … +0.89 (SE·√β ≈ 0.6–0.9) |
| 2.5 (4 pts) | −1.52 … −1.35 | −1.70 … −1.39 | −1.19 … −0.92 |

- √β·diff is bounded (≤ 2.1 in absolute value), so diff = O(β^{−1/2}): the per-step error that (E1) claims is o(1) is seen to be ~2/√β. Its sign follows the S³ Laplacian of Ψ∘a₁ (Ψ'' + 2Ψ' cot a₁ > 0 at a₁ = 0.5, < 0 at 2.5), which is the Hessian term of (E1)/Lemma K; the magnitude is about 2/3 of −ΔΨ/2 (measured only, not explained).
- The worst |diff| is at a₁ = 0.5 (the end nearest the well, where cot a₁ is largest). This is why the tube stops at a₋ and the wells need H4.
- Cut-off subsolution (η = 0.25, θ₀ = 0.5, ℓ = 0.08, r₀ = 0.15, M = 2): Tφ₁/φ₁ ≥ 1 (with 4 SE margin) at 52 of 53 support points for β ∈ {1024, 4096}. The one failure is β = 1024, a₁ = 0.5, a₂ = 0, y = 0: R₁ = 0.967 (SE 0.004). At β = 4096 the same point gives 1.120. At β = 256 (measured only) R₁ < 1 at 6 of 19 points, all with a₂ ≲ 0.07 and y ≤ 1. The smallest ratios sit at a₂ ≈ 0, where E has no tilt and pays the Hessian of Θ, and at a₁ = 0.5. Points at the transverse and a₂ edges have large ratios (1.4–190), as the cut-off algebra predicts.
- Child T147 (independent code, 4·10⁵ samples/point, different seeds): on all 36 core points its −log R agrees with mine within 2.62 combined SE (0 of 36 beyond 3 SE). Its worst |diff| per β is 0.129, 0.072, 0.041, against my 0.127, 0.059, 0.032.
- v1 failure kept: with ℓ = 0.02, θ₀ = 1 (results_smoke.txt) Tφ/φ < 1 at a₂ ≈ 0 (15/51): the Hessian of Θ at U₂ = 1 (Θ∘a₂ is a radial function of a 3-vector there) costs ≈ 3θ₀/(2ℓ√β) ≈ 1.2–2.3 nats per step at these β. This is a quantitative warning for (E1): its o(1) is O(θ₀/(ℓ√β)) and only small when √β ≫ θ₀/ℓ. It is not a defect of the asymptotic argument.

## 7. Step tags

| step | tag |
|---|---|
| §1 tangent decomposition 2 + 2 + 2, co-isometry, flat fixed point at S | PROVED |
| (E2) upper tilt bound | PROVED given Lemma K |
| (E1) lower local Gaussian estimate, uniform o(1) on the tube | CLAIMED (sketch) |
| (E3) upper local Gaussian estimate | CLAIMED (sketch) |
| Lemma S4-alg (cut-offs (G−c₁)₊(E−c₂)₊ and the tilt gain in a₂) | PROVED given (E1)–(E3); identity in Lean |
| ‖T_ΩΩ‖ < λ_ee | PROVED given Lemma F |
| (B) for the odd ground state f, and with links exchanged | PROVED (reading of TUNNEL_THEOREM §4) |
| λ_eo ≥ 1 − O(β^{−1/3}) | PROVED (sketch) |
| Lemma M4 (mass on corners ∩ {V ≤ K}) | PROVED given (B) |
| (H-a), (H-b) | PROVED |
| (H-c) chain geometry, hence H4 | CLAIMED |
| continuum Lemma P' (flows) | MISSING (CLAIMED routine) |
| target limsup ≤ c* | MISSING; conditional on (E1), (E3), H4, continuum P' |
