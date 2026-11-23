import Mathlib

/-- (F1) 1 - ab >= ((1-a)+(1-b))/2 for a,b in [0,1]; used for 1 - K1 K2 >= ((1-K1)+(1-K2))/2. -/
theorem one_sub_mul_ge (a b : ℝ) (ha0 : 0 ≤ a) (ha1 : a ≤ 1) (hb0 : 0 ≤ b) (hb1 : b ≤ 1) :
    ((1 - a) + (1 - b)) / 2 ≤ 1 - a * b := by
  nlinarith [mul_nonneg ha0 (sub_nonneg.mpr hb1), mul_nonneg hb0 (sub_nonneg.mpr ha1)]

/-- (F2) Casimir sum: sum_{nu=1}^{n} (nu + 1/2) = n(n+2)/2. -/
theorem casimir_sum (n : ℕ) :
    (∑ k ∈ Finset.range n, ((k:ℝ) + 1 + 1/2)) = (n:ℝ) * (n + 2) / 2 := by
  induction n with
  | zero => simp
  | succ m ih => rw [Finset.sum_range_succ, ih]; push_cast; ring

/-- (F3) log(1+y) >= y/(1+y) for y >= 0. -/
theorem log_one_add_ge (y : ℝ) (hy : 0 ≤ y) : y / (1 + y) ≤ Real.log (1 + y) := by
  have h1 : 0 < 1 + y := by linarith
  have h := Real.one_sub_inv_le_log_of_pos h1
  have : 1 - (1 + y)⁻¹ = y / (1 + y) := by field_simp
  linarith

/-- (F4) Jacobi bound minimisation: 4 s^2 u^2 - 8 s u + 4 s >= 4 s - 4. -/
theorem jacobi_min (s u : ℝ) : 4 * s - 4 ≤ 4 * s^2 * u^2 - 8 * s * u + 4 * s := by
  nlinarith [sq_nonneg (2 * s * u - 2)]

/-- (F5) the regime split: for a0 <= n, 0 <= v <= w, a0 + v >= c n, 0 < n: (a0+w)/(n+w) >= min(1/2, c/2). -/
theorem quotient_split (a0 v w n c : ℝ) (hn : 0 < n) (ha : 0 ≤ a0) (hv : 0 ≤ v) (hvw : v ≤ w)
    (hc : c * n ≤ a0 + v) : min (1/2) (c/2) ≤ (a0 + w) / (n + w) := by
  have hnw : 0 < n + w := by linarith
  rw [le_div_iff₀ hnw]
  rcases le_total w n with h | h
  · have : c / 2 * (n + w) ≤ a0 + w := by
      rcases le_total 0 c with hc0 | hc0
      · nlinarith
      · nlinarith
    calc min (1/2) (c/2) * (n + w) ≤ c / 2 * (n + w) := by
          apply mul_le_mul_of_nonneg_right (min_le_right _ _) hnw.le
      _ ≤ a0 + w := this
  · calc min (1/2) (c/2) * (n + w) ≤ 1 / 2 * (n + w) := by
          apply mul_le_mul_of_nonneg_right (min_le_left _ _) hnw.le
      _ ≤ a0 + w := by linarith

#print axioms one_sub_mul_ge
#print axioms casimir_sum
#print axioms log_one_add_ge
#print axioms jacobi_min
#print axioms quotient_split
