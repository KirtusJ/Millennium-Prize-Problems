import Mathlib

theorem KB_bound (g : ℝ) (hg : 0 < g) :
    min 4 (8 * (min g (17 * Real.sqrt g / 8 + 3 / 16)) / g)
      * (1 + min g (17 * Real.sqrt g / 8 + 3 / 16)) ≤ 43 := by
  set s := Real.sqrt g with hs
  have hs0 : 0 ≤ s := Real.sqrt_nonneg g
  have hss : s * s = g := Real.mul_self_sqrt hg.le
  set B := min g (17 * s / 8 + 3 / 16) with hB
  have hB0 : 0 ≤ B := le_min hg.le (by positivity)
  have hBc : B ≤ 17 * s / 8 + 3 / 16 := min_le_right _ _
  rcases le_total g 16 with h | h
  · have hs4 : s ≤ 4 := by nlinarith
    calc min 4 (8 * B / g) * (1 + B) ≤ 4 * (1 + B) :=
          mul_le_mul_of_nonneg_right (min_le_left _ _) (by linarith)
      _ ≤ 43 := by nlinarith
  · have hs4 : 4 ≤ s := by nlinarith
    calc min 4 (8 * B / g) * (1 + B) ≤ (8 * B / g) * (1 + B) :=
          mul_le_mul_of_nonneg_right (min_le_right _ _) (by linarith)
      _ ≤ 43 := by
        rw [div_mul_eq_mul_div, div_le_iff₀ hg]
        nlinarith [mul_le_mul hBc hBc hB0 (by positivity)]

#print axioms KB_bound
