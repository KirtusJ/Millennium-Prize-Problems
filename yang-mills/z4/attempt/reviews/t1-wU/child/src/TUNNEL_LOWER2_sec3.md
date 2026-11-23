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
