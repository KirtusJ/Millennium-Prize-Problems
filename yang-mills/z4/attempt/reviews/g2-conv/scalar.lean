import Mathlib

/-! Scalar steps used in SCALING_LIMIT.md (g2-conv, T77). -/

/-- F1: product splitting, upper direction: 1 - ab ≤ (1-a) + (1-b) on [0,1]². -/
theorem one_sub_mul_le (a b : ℝ) (ha0 : 0 ≤ a) (ha1 : a ≤ 1) (hb0 : 0 ≤ b) (hb1 : b ≤ 1) :
    1 - a * b ≤ (1 - a) + (1 - b) := by nlinarith

/-- F2: monotonicity of (a+w)/(n+w) in w when a ≤ n (used to replace W by V). -/
theorem ratio_mono (a n v w : ℝ) (hn : 0 < n) (han : a ≤ n) (hv : 0 ≤ v) (hvw : v ≤ w) :
    (a + v) / (n + v) ≤ (a + w) / (n + w) := by
  rw [div_le_div_iff₀ (by linarith) (by linarith)]
  nlinarith

/-- F3: (a+v)/(n+v) ≥ t/(1+t) with t = (a+v)/n, for 0 ≤ a. -/
theorem ratio_ge (a n v : ℝ) (hn : 0 < n) (ha : 0 ≤ a) (hv : 0 ≤ v) :
    ((a + v) / n) / (1 + (a + v) / n) ≤ (a + v) / (n + v) := by
  have h1 : ((a + v) / n) / (1 + (a + v) / n) = (a + v) / (n + (a + v)) := by
    field_simp
  rw [h1]
  apply div_le_div_of_nonneg_left (by linarith) (by linarith) (by linarith)

/-- F4: the fibre minimisation of S7: 4k - 8ku + 4k²u² ≥ 4k - 4. -/
theorem fibre_min (k u : ℝ) : 4 * k - 4 ≤ 4 * k - 8 * k * u + 4 * k ^ 2 * u ^ 2 := by
  nlinarith [sq_nonneg (k * u - 1)]

/-- F5: -log(1-μ) ≤ μ/(1-μ) for 0 ≤ μ < 1. -/
theorem neglog_le (μ : ℝ) (h0 : 0 ≤ μ) (h1 : μ < 1) : -Real.log (1 - μ) ≤ μ / (1 - μ) := by
  have hpos : 0 < 1 - μ := by linarith
  have h := Real.log_le_sub_one_of_pos (inv_pos.mpr hpos)
  rw [Real.log_inv] at h
  have : (1 - μ)⁻¹ - 1 = μ / (1 - μ) := by field_simp
  linarith

/-- F6: μ ≤ -log(1-μ) for μ < 1. -/
theorem le_neglog (μ : ℝ) (h1 : μ < 1) : μ ≤ -Real.log (1 - μ) := by
  have hpos : 0 < 1 - μ := by linarith
  have h := Real.log_le_sub_one_of_pos hpos
  linarith

#print axioms one_sub_mul_le
#print axioms ratio_mono
#print axioms ratio_ge
#print axioms fibre_min
#print axioms neglog_le
#print axioms le_neglog
