import Mathlib
open Real
example (x r : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hr : 0 ≤ r) : x * (1 - x ^ r) ≤ r * (1 - x) := by
  rcases hx0.eq_or_lt with h | h
  · subst h; simp; nlinarith
  · have h1 : x ^ r = exp (log x * r) := Real.rpow_def_of_pos h r
    have h2 := Real.add_one_le_exp (log x * r)
    have h3 : -log x ≤ 1/x - 1 := by
      have := Real.log_le_sub_one_of_pos (one_div_pos.mpr h)
      rw [one_div, Real.log_inv] at this; rwa [one_div]
    have h4 : -(x * log x) ≤ 1 - x := by
      have := mul_le_mul_of_nonneg_left h3 h.le
      rw [mul_sub, mul_one_div_cancel h.ne'] at this; linarith
    rw [h1]
    have h5 : x * (1 - exp (log x * r)) ≤ x * (-(log x * r)) := mul_le_mul_of_nonneg_left (by linarith) h.le
    nlinarith
