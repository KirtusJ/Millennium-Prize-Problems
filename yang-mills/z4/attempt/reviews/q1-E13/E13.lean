import Mathlib

/-- flat fixed-point identity in the form used in E13.md: with r = sqrt(1+S^2), h = 1 + r/S,
    (h - 2) (1 + 2 S^2 h) = h. -/
theorem flat_identity (S : ℝ) (hS : 0 < S) :
    let r := Real.sqrt (1 + S ^ 2)
    let h := 1 + r / S
    (h - 2) * (1 + 2 * S ^ 2 * h) = h := by
  intro r h
  have hr : r ^ 2 = 1 + S ^ 2 := Real.sq_sqrt (by positivity)
  simp only [h]
  field_simp
  linear_combination (2 * S ^ 3) * hr

/-- kernel density lower bound: sqrt(1-t) ≥ 1 - t/2 - t^2/2 on [0,1]. -/
theorem sqrt_lower (t : ℝ) (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    1 - t / 2 - t ^ 2 / 2 ≤ Real.sqrt (1 - t) := by
  have hs := Real.sqrt_nonneg (1 - t)
  have hsq : Real.sqrt (1 - t) ^ 2 = 1 - t := Real.sq_sqrt (by linarith)
  -- (1-t)(2+t)/2 = 1 - t/2 - t^2/2 and sqrt(1-t) ≤ 1
  have hle : Real.sqrt (1 - t) ≤ 1 := by nlinarith
  nlinarith [mul_nonneg hs (by linarith : (0:ℝ) ≤ 1 - Real.sqrt (1 - t)), mul_nonneg h0 hs]

/-- 1 - sqrt(1-t) ≤ t on [0,1]  (used: |1 - g0| ≤ |xi|^2). -/
theorem one_sub_sqrt_le (t : ℝ) (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    1 - Real.sqrt (1 - t) ≤ t := by
  have hsq : Real.sqrt (1 - t) ^ 2 = 1 - t := Real.sq_sqrt (by linarith)
  have hs := Real.sqrt_nonneg (1 - t)
  have hle : Real.sqrt (1 - t) ≤ 1 := by nlinarith
  nlinarith

/-- cross-term bound (corrected): for h, s > 0, 2 h s / (1 + 2 h s^2) ≤ 1 / s. -/
theorem cross_bound (h s : ℝ) (hh : 0 < h) (hs : 0 < s) :
    2 * h * s / (1 + 2 * h * s ^ 2) ≤ 1 / s := by
  rw [div_le_div_iff₀ (by positivity) hs]
  nlinarith

#print axioms flat_identity
#print axioms sqrt_lower
#print axioms one_sub_sqrt_le
#print axioms cross_bound
