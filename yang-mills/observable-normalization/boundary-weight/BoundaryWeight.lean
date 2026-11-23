import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

namespace YangMills.BoundaryWeight
open scoped BigOperators

/-- Compare a deep face with every face of the same orientation in a smaller cube. -/
theorem translatedAverage {ι : Type*} (s : Finset ι) (row : ι → ℝ)
    (a b : ℝ) (hs : 0 < (s.card : ℝ))
    (order : ∀ i ∈ s, a ≤ row i)
    (total : ∑ i ∈ s, row i ≤ s.card * b) : a ≤ b := by
  have h := Finset.sum_le_sum order
  simp only [Finset.sum_const, nsmul_eq_mul] at h
  exact le_of_mul_le_mul_left (h.trans total) hs

/-- A lower Rayleigh bound forces a positive fraction into the boundary layer. -/
theorem boundaryFraction (d e w : ℝ) (he : e < 1)
    (budget : 4+d ≤ 5*w+(4+e)*(1-w)) :
    (d-e)/(1-e) ≤ w := by
  apply (div_le_iff₀ (by linarith : 0 < 1-e)).2
  linarith only [budget]

theorem cubeAverage (r : ℝ) (hr : 0 < r) :
    6*(3*r^2*(r+1)-r^3)/(3*r^2*(r+1)) = 4+2/(r+1) := by
  have hp : r+1 ≠ 0 := by linarith
  field_simp [ne_of_gt hr, hp]
  <;> ring

end YangMills.BoundaryWeight
#print axioms YangMills.BoundaryWeight.translatedAverage
#print axioms YangMills.BoundaryWeight.boundaryFraction
#print axioms YangMills.BoundaryWeight.cubeAverage
