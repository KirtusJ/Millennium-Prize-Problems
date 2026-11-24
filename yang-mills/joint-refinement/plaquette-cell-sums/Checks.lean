import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.CellSums

theorem family_average {k : ℕ} (J : ℝ) (lower : Fin k → ℝ)
    (h : ∀ i, lower i ≤ J) : ∑ i, lower i ≤ k * J := by
  simpa using (Finset.sum_le_sum (s := Finset.univ) (fun i _ => h i))

theorem effective_count (S Q V D : ℝ)
    (hQ : 0 < Q) (hV : V ≤ D*S^2) : V/Q ≤ D*(S^2/Q) := by
  rw [← mul_div_assoc]
  exact div_le_div_of_nonneg_right hV hQ.le

-- NATIVE CHILD 1
theorem lifted_deficit (full cell coarse lift factor : ℝ) (he : 0 ≤ lift)
    (hv : factor*coarse ≤ cell) (hj : lift*cell ≤ full) :
    lift*(factor*coarse) ≤ full := (mul_le_mul_of_nonneg_left hv he).trans hj

theorem latent_sign_ratio (m p b : ℝ) (hm : 0 < m) :
    m*p/(m*p+m^2*b^2) = p/(p+m*b^2) := by
  have h : m*p+m^2*b^2=m*(p+m*b^2) := by ring
  rw [h]
  exact mul_div_mul_left _ _ hm.ne'

-- NATIVE CHILD 2
theorem collective_degree (a b : ℕ) (ha : a ≤ 3) (hb : b ≤ 2) :
    2*(a+b) ≤ 10 := by omega

#print axioms family_average
#print axioms effective_count
#print axioms lifted_deficit
#print axioms latent_sign_ratio
#print axioms collective_degree
end Millennium.G4.CellSums
