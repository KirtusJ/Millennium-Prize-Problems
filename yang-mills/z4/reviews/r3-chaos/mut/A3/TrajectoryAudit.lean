import Mathlib

/-!
Z4 trajectory bounds for A4's interval (A2).
Conventions: kappa_A = 2/(beta*b), g = beta^2/2,
B = min g (17*sqrt g/8 + 3/16), A = 9 kappa_A/(8(1+B)), L = A/16,
w = A^2/(8 D) for any D with D >= 36 kappa_A^2 (covers A4's D and D_*).
-/

noncomputable section
open Filter Topology

def gB (β : ℝ) : ℝ := β ^ 2 / 2
def BB (β : ℝ) : ℝ := min (gB β) (17 * Real.sqrt (gB β) / 8 + 3 / 16)
def kapA (β b : ℝ) : ℝ := 2 / (β * b)
def Aq (β b : ℝ) : ℝ := 9 * kapA β b / (8 * (1 + BB β))
def Lq (β b : ℝ) : ℝ := Aq β b / 16

lemma BB_nonneg (β : ℝ) : 0 ≤ BB β := by
  unfold BB gB
  apply le_min (by positivity)
  have := Real.sqrt_nonneg (β ^ 2 / 2)
  linarith

/-- upper bound 1 + B ≤ 1 + 2β (sharp as β → 0). -/
lemma one_add_BB_le (β : ℝ) (hβ : 0 < β) : 1 + BB β ≤ 1 + 2 * β := by
  unfold BB
  rcases le_or_lt β 4 with h | h
  · have : gB β ≤ 2 * β := by unfold gB; nlinarith
    have := min_le_left (gB β) (17 * Real.sqrt (gB β) / 8 + 3 / 16)
    linarith
  · have hs : Real.sqrt (gB β) ≤ 3 * β / 4 := by
      have h1 : gB β ≤ (3 * β / 4) ^ 2 := by unfold gB; nlinarith
      calc Real.sqrt (gB β) ≤ Real.sqrt ((3 * β / 4) ^ 2) := Real.sqrt_le_sqrt h1
        _ = 3 * β / 4 := Real.sqrt_sq (by linarith)
    have := min_le_right (gB β) (17 * Real.sqrt (gB β) / 8 + 3 / 16)
    linarith

/-- lower bound 1 + B ≥ (1 + β)/2. -/
lemma one_add_BB_ge (β : ℝ) (hβ : 0 < β) : (1 + β) / 2 ≤ 1 + BB β := by
  unfold BB
  have hs : β / 2 ≤ Real.sqrt (gB β) := by
    have h1 : (β / 2) ^ 2 ≤ gB β := by unfold gB; nlinarith
    calc β / 2 = Real.sqrt ((β / 2) ^ 2) := (Real.sqrt_sq (by linarith)).symm
      _ ≤ Real.sqrt (gB β) := Real.sqrt_le_sqrt h1
  have h2 : (1 + β) / 2 ≤ 1 + gB β := by unfold gB; nlinarith [sq_nonneg (β - 1)]
  have h3 : (1 + β) / 2 ≤ 1 + (17 * Real.sqrt (gB β) / 8 + 3 / 16) := by nlinarith
  rcases min_choice (gB β) (17 * Real.sqrt (gB β) / 8 + 3 / 16) with h | h <;> rw [h] <;> linarith

lemma Lq_eq (β b : ℝ) (hβ : 0 < β) (hb : 0 < b) :
    Lq β b = 9 / (64 * (β * b) * (1 + BB β)) := by
  have := BB_nonneg β
  unfold Lq Aq kapA
  field_simp
  ring

/-- A2(i): L ≥ (9/64) / (β(1+2β) b). -/
theorem L_lower (β b : ℝ) (hβ : 0 < β) (hb : 0 < b) :
    (9 / 64) / (β * (1 + 2 * β) * b) ≤ Lq β b := by
  rw [Lq_eq β b hβ hb]
  have h1 := one_add_BB_le β hβ
  have h0 := BB_nonneg β
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  have hbb : 0 < β * b := mul_pos hβ hb
  nlinarith [mul_le_mul_of_nonneg_left h1 hbb.le]

/-- A2(ii): w ≤ 9 / (512 (1+β)^2) for any D ≥ 36 κ_A^2 (A4's D and D_* both qualify). -/
theorem w_upper (β b D : ℝ) (hβ : 0 < β) (hb : 0 < b) (hD : 36 * kapA β b ^ 2 ≤ D) :
    Aq β b ^ 2 / (8 * D) ≤ 8 / (512 * (1 + β) ^ 2) := by
  have h1 := one_add_BB_ge β hβ
  have h0 := BB_nonneg β
  have hk : 0 < kapA β b := by unfold kapA; positivity
  have hDp : 0 < D := by nlinarith
  have hA : Aq β b ^ 2 = 81 * kapA β b ^ 2 / (64 * (1 + BB β) ^ 2) := by
    unfold Aq; field_simp; ring
  rw [hA, div_div, div_le_div_iff₀ (by positivity) (by positivity)]
  have hsq : (1 + β) ^ 2 ≤ 4 * (1 + BB β) ^ 2 := by nlinarith
  have hk2 : 0 < kapA β b ^ 2 := by positivity
  nlinarith [mul_le_mul_of_nonneg_left hsq hk2.le, mul_le_mul_of_nonneg_left hD (by positivity : (0:ℝ) ≤ (1 + BB β) ^ 2)]

/-- A2(iii): along b_n>0, β_n>0 with β_n(1+2β_n)b_n → 0, L_n → +∞. -/
theorem L_tendsto_top (β b : ℕ → ℝ) (hβ : ∀ n, 0 < β n) (hb : ∀ n, 0 < b n)
    (hx : Tendsto (fun n => β n * (1 + 2 * β n) * b n) atTop (𝓝 0)) :
    Tendsto (fun n => Lq (β n) (b n)) atTop atTop := by
  rw [tendsto_atTop]
  intro M
  set ε : ℝ := (9 / 64) / (|M| + 1) with hε
  have hεp : 0 < ε := by positivity
  filter_upwards [(tendsto_order.1 hx).2 ε hεp] with n hn
  have hxp : 0 < β n * (1 + 2 * β n) * b n := by
    have := hβ n; have := hb n; positivity
  have h1 := L_lower (β n) (b n) (hβ n) (hb n)
  have h2 : (9 / 64) / ε ≤ (9 / 64) / (β n * (1 + 2 * β n) * b n) :=
    div_le_div_of_nonneg_left (by norm_num) hxp hn.le
  have h3 : (9 / 64) / ε = |M| + 1 := by
    rw [hε]; field_simp; ring
  have := le_abs_self M
  linarith

/-- A2(iv): if moreover β_n → ∞, the guaranteed weight w_n → 0 (for any D_n ≥ 36 κ_A^2). -/
theorem w_tendsto_zero (β b D : ℕ → ℝ) (hβ : ∀ n, 0 < β n) (hb : ∀ n, 0 < b n)
    (hD : ∀ n, 36 * kapA (β n) (b n) ^ 2 ≤ D n)
    (hβinf : Tendsto β atTop atTop) :
    Tendsto (fun n => Aq (β n) (b n) ^ 2 / (8 * D n)) atTop (𝓝 0) := by
  have hDp : ∀ n, 0 < D n := fun n => by
    have : 0 < kapA (β n) (b n) := by unfold kapA; have := hβ n; have := hb n; positivity
    nlinarith [hD n]
  have hup : Tendsto (fun n => (9:ℝ) / (512 * (1 + β n) ^ 2)) atTop (𝓝 0) := by
    have h1 : Tendsto (fun n => 1 + β n) atTop atTop := tendsto_atTop_add_const_left _ 1 hβinf
    have h2 : Tendsto (fun n => 512 * (1 + β n) ^ 2) atTop atTop :=
      (Tendsto.const_mul_atTop (by norm_num) ((tendsto_pow_atTop (by norm_num)).comp h1))
    exact tendsto_const_nhds.div_atTop h2
  apply squeeze_zero (fun n => by have := hDp n; positivity) _ hup
  intro n
  exact w_upper (β n) (b n) (D n) (hβ n) (hb n) (hD n)

/-- A2(v) complementary, corrected shape: if b ≤ b0 and L ≤ C then
β² b ≥ min (c/4) (c²/(4 b0)) with c = 9/(64 C). -/
theorem L_bounded_forces (β b b0 C : ℝ) (hβ : 0 < β) (hb : 0 < b) (hb0 : b ≤ b0)
    (hC : 0 < C) (hL : Lq β b ≤ C) :
    min ((9 / (64 * C)) / 4) ((9 / (64 * C)) ^ 2 / (4 * b0)) ≤ β ^ 2 * b := by
  set c : ℝ := 9 / (64 * C) with hc
  have hcp : 0 < c := by positivity
  have hb0p : 0 < b0 := lt_of_lt_of_le hb hb0
  rw [Lq_eq β b hβ hb] at hL
  have h0 := BB_nonneg β
  have h1 := one_add_BB_le β hβ
  have hbb : 0 < β * b := mul_pos hβ hb
  -- from L ≤ C : c ≤ β b (1+B) ≤ β b + 2 β^2 b
  have hkey : c ≤ β * b + 2 * (β ^ 2 * b) := by
    have hpos : 0 < 64 * (β * b) * (1 + BB β) := by positivity
    rw [div_le_iff₀ hpos] at hL
    have : c ≤ β * b * (1 + BB β) := by
      rw [hc, div_le_iff₀ (by positivity)]; nlinarith
    nlinarith [mul_le_mul_of_nonneg_left h1 hbb.le]
  by_cases hy : c / 4 ≤ β ^ 2 * b
  · exact le_trans (min_le_left _ _) hy
  · push_neg at hy
    have hx : c / 2 ≤ β * b := by linarith
    have hsq : (β * b) ^ 2 ≤ (β ^ 2 * b) * b0 := by
      have : (β * b) ^ 2 = (β ^ 2 * b) * b := by ring
      rw [this]; exact mul_le_mul_of_nonneg_left hb0 (by positivity)
    have : c ^ 2 / 4 ≤ (β ^ 2 * b) * b0 := by nlinarith
    apply le_trans (min_le_right _ _)
    rw [div_le_iff₀ (by positivity)]; nlinarith

/-- Counterexample showing the unconditioned complementary statement (no bound on b) is false:
β = 1/n, b = n gives L bounded (≤ 9/64) while β² b = 1/n → 0. -/
theorem complementary_needs_b_bound (n : ℝ) (hn : 0 < n) :
    Lq (1 / n) n ≤ 9 / 64 ∧ (1 / n) ^ 2 * n = 1 / n := by
  constructor
  · rw [Lq_eq _ _ (by positivity) hn]
    have h0 := BB_nonneg (1 / n)
    have : (1 / n) * n = 1 := by field_simp
    rw [this, div_le_div_iff₀ (by positivity) (by norm_num)]
    nlinarith
  · field_simp; ring

end

#print axioms L_lower
#print axioms w_upper
#print axioms L_tendsto_top
#print axioms w_tendsto_zero
#print axioms L_bounded_forces
#print axioms complementary_needs_b_bound
