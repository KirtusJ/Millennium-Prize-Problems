import Mathlib
/-- Per-mode longitudinal electric weight under spatial flow: p = |D_s|^2 (spatial), q = |D_4|^2,
covariance 1/A with A = p + q. The weight p/A (from D_i a_4) plus q*(p/p)/A (from D_4 (P_L a)_i)
is exactly 1 and carries no flow factor. -/
theorem long_weight_one (p q : ℝ) (hp : 0 < p) (hq : 0 ≤ q) :
    p * (1 / (p + q)) + q * (p / p) * (1 / (p + q)) = 1 := by
  have hA : (p + q) ≠ 0 := by linarith
  have hp' : p ≠ 0 := ne_of_gt hp
  field_simp
/-- In physical units the lattice density 1 becomes 1/b^4; t^2/b^4 is unbounded as b → 0. -/
theorem unbounded (t : ℝ) (ht : 0 < t) (C : ℝ) : ∃ b : ℝ, 0 < b ∧ C < t^2 / b^4 := by
  obtain ⟨n, hn⟩ := exists_nat_gt (C / t^2)
  refine ⟨(1 / ((n:ℝ) + 1)) ^ ((1:ℝ)/4), by positivity, ?_⟩
  have h4 : ((1 / ((n:ℝ) + 1)) ^ ((1:ℝ)/4)) ^ 4 = 1 / ((n:ℝ) + 1) := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]; norm_num
  rw [h4, div_div_eq_mul_div, div_one]
  have ht2 : 0 < t^2 := by positivity
  rw [div_lt_iff₀ ht2] at hn
  nlinarith
#print axioms long_weight_one
#print axioms unbounded
