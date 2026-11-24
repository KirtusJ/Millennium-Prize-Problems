import Mathlib

/-!
# b2-haar: algebra at the zeros and a generic first-zero lemma

Nothing here mentions Bessel functions.  The ODE relations are hypotheses
(real numbers standing for the values R(k), p(k), w(k) at one point k).
-/

open Set Filter Topology

namespace B2Haar

/-- (a) Proof A, algebra at a zero of p - q: if p = R/k then
    p' := -(2R+3/k) p + 3R/k^2 equals -2 R (R/k), hence is < 0 when R, k > 0. -/
theorem a_at_zero (k R p : ℝ) (hk : 0 < k) (hR : 0 < R) (hpq : p = R / k) :
    -(2 * R + 3 / k) * p + 3 * R / k ^ 2 = -2 * R * (R / k) ∧
    -(2 * R + 3 / k) * p + 3 * R / k ^ 2 < 0 := by
  have h1 : -(2 * R + 3 / k) * p + 3 * R / k ^ 2 = -2 * R * (R / k) := by
    subst hpq; field_simp; ring
  refine ⟨h1, ?_⟩
  rw [h1]
  have : 0 < R / k := div_pos hR hk
  nlinarith

/-- (b) algebra at a zero of p': the general second-derivative expression
    p'' = -(2R' - 3/k^2) p - (2R+3/k) p' + 3R'/k^2 - 6R/k^3, with R' = p and p' = 0,
    equals -2p^2 + 6(p - R/k)/k^2, which is < 0 when p > 0 and p < R/k. -/
theorem b_at_zero (k R p : ℝ) (hk : 0 < k) (hp : 0 < p) (hpq : p < R / k) :
    -(2 * p - 3 / k ^ 2) * p - (2 * R + 3 / k) * 0 + 3 * p / k ^ 2 - 6 * R / k ^ 3
      = -2 * p ^ 2 + 6 * (p - R / k) / k ^ 2 ∧
    -2 * p ^ 2 + 6 * (p - R / k) / k ^ 2 < 0 := by
  refine ⟨by field_simp; ring, ?_⟩
  have h1 : 6 * (p - R / k) / k ^ 2 < 0 := div_neg_of_neg_of_pos (by linarith) (by positivity)
  nlinarith [sq_nonneg p, mul_pos hp hp]

/-- (c) at a zero of w' = 3R - (2R+1/k) w one has w < 3/2. -/
theorem c_w_lt (k R w : ℝ) (hk : 0 < k) (hR : 0 < R)
    (hz : 3 * R - (2 * R + 1 / k) * w = 0) : w < 3 / 2 := by
  have hpos : 0 < 2 * R + 1 / k := by positivity
  have hw : w = 3 * R / (2 * R + 1 / k) := by
    rw [eq_div_iff hpos.ne']; linarith
  rw [hw, div_lt_iff₀ hpos]
  have : 0 < 1 / k := by positivity
  nlinarith

/-- (c) the two auditor formulas agree identically when w = k^2 p:
    p(3-2w) + w/k^2 = (4-2w) w / k^2; and both are > 0 when p > 0, w < 2. -/
theorem c_formulas_equal (k p w : ℝ) (hk : 0 < k) (hw : w = k ^ 2 * p) :
    p * (3 - 2 * w) + w / k ^ 2 = (4 - 2 * w) * w / k ^ 2 := by
  subst hw; field_simp; ring

theorem c_second_pos (k p w : ℝ) (hk : 0 < k) (hp : 0 < p) (hw : w = k ^ 2 * p)
    (hw2 : w < 2) : 0 < p * (3 - 2 * w) + w / k ^ 2 := by
  rw [c_formulas_equal k p w hk hw]
  have : 0 < w := by rw [hw]; positivity
  apply div_pos _ (by positivity)
  nlinarith

/-- (c) general identity: with R' = p and the expression w' = 3R - (2R+1/k) w,
    differentiating symbolically gives 3p - (2p - 1/k^2) w - (2R+1/k) w';
    at w' = 0 this is p(3-2w) + w/k^2. (Pure algebra.) -/
theorem c_second_at_zero (k R p w : ℝ) :
    3 * p - (2 * p - 1 / k ^ 2) * w - (2 * R + 1 / k) * 0 = p * (3 - 2 * w) + w / k ^ 2 := by
  ring

/-- Proof B: s = (sqrt(4+k^2) - 2)/k solves 1 - s^2 - 4 s/k = 0. -/
theorem s_root (k : ℝ) (hk : 0 < k) :
    let s := (Real.sqrt (4 + k ^ 2) - 2) / k
    1 - s ^ 2 - 4 * s / k = 0 := by
  intro s
  have hsq : Real.sqrt (4 + k ^ 2) ^ 2 = 4 + k ^ 2 := Real.sq_sqrt (by positivity)
  simp only [s]
  field_simp
  ring_nf
  nlinarith [hsq]

/-- Proof B, last step: if R > s > 0 and 1 - s^2 - 4s/k = 0 then
    R' - R/k = 1 - 4R/k - R^2 < 0. -/
theorem riccati_gives (k R s : ℝ) (hk : 0 < k) (hs : 0 < s) (hRs : s < R)
    (hroot : 1 - s ^ 2 - 4 * s / k = 0) : 1 - 3 * R / k - R ^ 2 < R / k := by
  have h4 : 4 * s / k < 4 * R / k := by
    apply div_lt_div_of_pos_right _ hk; linarith
  have hsR : s ^ 2 < R ^ 2 := by nlinarith
  have e : 3 * R / k + R / k = 4 * R / k := by ring
  linarith

/-- Proof B, at a crossing R = s: R' = 1 - 3s/k - s^2 = s/k. -/
theorem B_crossing (k s : ℝ) (hroot : 1 - s ^ 2 - 4 * s / k = 0) :
    1 - 3 * s / k - s ^ 2 = s / k := by
  have : 1 - s ^ 2 = 4 * s / k := by linarith
  have e : 1 - 3 * s / k - s ^ 2 = (1 - s ^ 2) - 3 * s / k := by ring
  rw [e, this]; ring

/-- Proof B: (s/k) * 2/sqrt(4+k^2) < s/k for s, k > 0. -/
theorem B_sprime_lt (k s : ℝ) (hk : 0 < k) (hs : 0 < s) :
    s / k * (2 / Real.sqrt (4 + k ^ 2)) < s / k := by
  have hq : 0 < s / k := div_pos hs hk
  have h2 : (2:ℝ) < Real.sqrt (4 + k ^ 2) := by
    rw [show (2:ℝ) = Real.sqrt 4 by
      rw [show (4:ℝ) = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]]
    exact Real.sqrt_lt_sqrt (by norm_num) (by nlinarith)
  have h3 : 2 / Real.sqrt (4 + k ^ 2) < 1 := by
    rw [div_lt_one (by linarith)]; exact h2
  calc s / k * (2 / Real.sqrt (4 + k ^ 2)) < s / k * 1 := by
        exact mul_lt_mul_of_pos_left h3 hq
    _ = s / k := mul_one _

/-- (d) reduction, abstract: if p is antitone on (0,∞), w x = x^2 p x is monotone on (0,∞),
    L > 0, β ≥ 1, 0 < k ≤ L β, then p L ≤ β^2 p k. -/
theorem d_reduction (p : ℝ → ℝ) (L β k : ℝ) (hL : 0 < L) (hβ : 1 ≤ β) (hk : 0 < k)
    (hkL : k ≤ L * β)
    (hp : ∀ a b, 0 < a → a ≤ b → p b ≤ p a)
    (hw : ∀ a b, 0 < a → a ≤ b → a ^ 2 * p a ≤ b ^ 2 * p b) :
    p L ≤ β ^ 2 * p k := by
  have h1 : p (L * β) ≤ p k := hp k (L * β) hk hkL
  have hLb : L ≤ L * β := by nlinarith
  have h2 : L ^ 2 * p L ≤ (L * β) ^ 2 * p (L * β) := hw L (L * β) hL hLb
  have h3 : (L * β) ^ 2 * p (L * β) = L ^ 2 * (β ^ 2 * p (L * β)) := by ring
  rw [h3] at h2
  have h4 : p L ≤ β ^ 2 * p (L * β) := le_of_mul_le_mul_left h2 (by positivity)
  have h5 : β ^ 2 * p (L * β) ≤ β ^ 2 * p k := mul_le_mul_of_nonneg_left h1 (by positivity)
  linarith

/-- Generic first-zero lemma.  f differentiable on (0,K), f < 0 on (0,ε) for some ε > 0,
    and at every zero x ∈ (0,K) of f, deriv f x < 0.  Then f < 0 on (0,K). -/
theorem first_zero {f : ℝ → ℝ} {K ε : ℝ} (hε : 0 < ε)
    (hdiff : DifferentiableOn ℝ f (Ioo 0 K))
    (hneg : ∀ x ∈ Ioo 0 ε, f x < 0)
    (hzero : ∀ x ∈ Ioo 0 K, f x = 0 → deriv f x < 0) :
    ∀ x ∈ Ioo 0 K, f x < 0 := by
  intro x0 hx0
  by_contra hcon
  push_neg at hcon
  set δ := min ε x0 / 2 with hδ
  have hx0pos : 0 < x0 := hx0.1
  have hδpos : 0 < δ := by positivity
  have hδx : δ < x0 := by
    have : min ε x0 ≤ x0 := min_le_right _ _
    linarith
  have hδε : δ < ε := by
    have : min ε x0 ≤ ε := min_le_left _ _
    linarith
  have hfδ : f δ < 0 := hneg δ ⟨hδpos, hδε⟩
  have hsub : Icc δ x0 ⊆ Ioo 0 K := fun y hy => ⟨by linarith [hy.1], lt_of_le_of_lt hy.2 hx0.2⟩
  have hcont : ContinuousOn f (Icc δ x0) := (hdiff.continuousOn).mono hsub
  set S := Icc δ x0 ∩ f ⁻¹' (Ici 0) with hS
  have hSc : IsClosed S := hcont.preimage_isClosed_of_isClosed isClosed_Icc isClosed_Ici
  have hSne : S.Nonempty := ⟨x0, ⟨le_of_lt hδx, le_refl _⟩, hcon⟩
  have hSbdd : BddBelow S := ⟨δ, fun y hy => hy.1.1⟩
  set z := sInf S with hz
  have hzS : z ∈ S := hSc.csInf_mem hSne hSbdd
  have hzI : z ∈ Ioo 0 K := hsub hzS.1
  have hfz0 : 0 ≤ f z := hzS.2
  have hδz : δ < z := by
    rcases lt_or_eq_of_le hzS.1.1 with h | h
    · exact h
    · exfalso; have := hzS.2; simp only [mem_preimage, mem_Ici] at this; rw [← h] at this; linarith
  -- f < 0 on [δ, z)
  have hbelow : ∀ y ∈ Ico δ z, f y < 0 := by
    intro y hy
    by_contra hy'
    push_neg at hy'
    have hyS : y ∈ S := ⟨⟨hy.1, le_trans (le_of_lt hy.2) hzS.1.2⟩, hy'⟩
    have := csInf_le hSbdd hyS
    linarith [hy.2]
  have hDz : DifferentiableAt ℝ f z := hdiff.differentiableAt (isOpen_Ioo.mem_nhds hzI)
  -- f z = 0
  have hfz : f z = 0 := by
    by_contra hne
    have hpos : 0 < f z := lt_of_le_of_ne hfz0 (Ne.symm hne)
    have hev : ∀ᶠ y in 𝓝 z, 0 < f y := hDz.continuousAt.eventually (lt_mem_nhds hpos)
    have hev' : ∀ᶠ y in 𝓝[<] z, 0 < f y := nhdsWithin_le_nhds hev
    have hev2 : ∀ᶠ y in 𝓝[<] z, 0 < f y ∧ y ∈ Ioo δ z :=
      hev'.and (Ioo_mem_nhdsLT hδz)
    obtain ⟨y, hy1, hy2⟩ := hev2.exists
    linarith [hbelow y ⟨le_of_lt hy2.1, hy2.2⟩]
  have hd : deriv f z < 0 := hzero z hzI hfz
  have hHas : HasDerivWithinAt f (deriv f z) (Iio z) z := hDz.hasDerivAt.hasDerivWithinAt
  have hsl : ∀ᶠ y in 𝓝[<] z, slope f z y < 0 :=
    hHas.limsup_slope_le' (by simp) hd
  obtain ⟨y, hy1, hy2⟩ := (hsl.and (Ioo_mem_nhdsLT hδz)).exists
  rw [slope_def_field, hfz, sub_zero] at hy1
  have hfy : f y < 0 := hbelow y ⟨le_of_lt hy2.1, hy2.2⟩
  have hyz : y - z < 0 := by linarith [hy2.2]
  have : 0 < f y / (y - z) := div_pos_of_neg_of_neg hfy hyz
  linarith

end B2Haar

#print axioms B2Haar.a_at_zero
#print axioms B2Haar.b_at_zero
#print axioms B2Haar.c_w_lt
#print axioms B2Haar.c_formulas_equal
#print axioms B2Haar.c_second_pos
#print axioms B2Haar.c_second_at_zero
#print axioms B2Haar.s_root
#print axioms B2Haar.riccati_gives
#print axioms B2Haar.B_crossing
#print axioms B2Haar.B_sprime_lt
#print axioms B2Haar.d_reduction
#print axioms B2Haar.first_zero
