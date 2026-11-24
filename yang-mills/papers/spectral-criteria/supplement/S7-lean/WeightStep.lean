/-
Scalar step of the refinement step under a linear bound on the low-energy weight of the fine detail.
Lean 4.19.0, Mathlib v4.19.0. The operator inequalities that lead to the hypothesis `h` (the spectral
integral, the comparison of `(I - A²)⁻¹` with `H⁻¹`, and the refinement theorem) are not in this file;
the refinement theorem itself is in `Hilbert.lean`.
-/
import Mathlib

namespace WeightStep

/-- `d log (1/d) ≤ 1/e` for `d > 0`. -/
theorem mul_neg_log_le (d : ℝ) (hd : 0 < d) : d * (-Real.log d) ≤ 1 / Real.exp 1 := by
  have he : 0 < Real.exp 1 := Real.exp_pos 1
  have hpos : 0 < 1 / (d * Real.exp 1) := by positivity
  have h1 := Real.log_le_sub_one_of_pos hpos
  have h2 : Real.log (1 / (d * Real.exp 1)) = -Real.log d - 1 := by
    rw [one_div, Real.log_inv, Real.log_mul hd.ne' he.ne', Real.log_exp]; ring
  rw [h2] at h1
  have h3 : -Real.log d ≤ 1 / (d * Real.exp 1) := by linarith
  calc d * (-Real.log d) ≤ d * (1 / (d * Real.exp 1)) := mul_le_mul_of_nonneg_left h3 hd.le
    _ = 1 / Real.exp 1 := by field_simp

/-- From the implicit inequality for the deficit `d` to the explicit one. `m` is the number of steps,
`K` the constant of the weight bound, `δ = b - κ`. -/
theorem explicit (d δ K m : ℝ) (hd0 : 0 < d) (hm : 1 ≤ m) (hK : 0 ≤ K)
    (h : δ ≤ d * (1 + (3 + K * Real.log (m / d)) / m)) :
    (δ - K / (Real.exp 1 * m)) / (1 + (3 + K * Real.log m) / m) ≤ d := by
  have hm0 : 0 < m := by linarith
  have he : 0 < Real.exp 1 := Real.exp_pos 1
  have hlogm : 0 ≤ Real.log m := Real.log_nonneg hm
  have hD : 0 < 1 + (3 + K * Real.log m) / m := by positivity
  rw [div_le_iff₀ hD]
  have hsplit : Real.log (m / d) = Real.log m - Real.log d := Real.log_div hm0.ne' hd0.ne'
  have hx := mul_neg_log_le d hd0
  have e : d * (1 + (3 + K * Real.log (m / d)) / m)
      = d * (1 + (3 + K * Real.log m) / m) + K / m * (d * (-Real.log d)) := by
    rw [hsplit]; field_simp; ring
  have hKm : 0 ≤ K / m := div_nonneg hK hm0.le
  have h4 : K / m * (d * (-Real.log d)) ≤ K / m * (1 / Real.exp 1) :=
    mul_le_mul_of_nonneg_left hx hKm
  have h5 : K / m * (1 / Real.exp 1) = K / (Real.exp 1 * m) := by
    rw [div_mul_div_comm, mul_one, mul_comm m]
  linarith

end WeightStep

#print axioms WeightStep.mul_neg_log_le
#print axioms WeightStep.explicit
