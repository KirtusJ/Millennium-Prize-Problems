import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith

namespace Millennium.G4.RareCoarse
open scoped BigOperators

theorem sum_weighted_rows {F E : Type*} [Fintype F] [Fintype E]
    (y R : F → ℝ) (s : F → E → ℝ) (w m : E → ℝ)
    (hw : ∀ e, 0 ≤ w e)
    (hr : ∀ f, y f ^ 2 ≤ ∑ e, R f * s f e * w e)
    (hc : ∀ e, ∑ f, R f * s f e ≤ 3 * m e) :
    ∑ f, y f ^ 2 ≤ 3 * ∑ e, m e * w e := by
  calc
    _ ≤ ∑ f, ∑ e, R f * s f e * w e := Finset.sum_le_sum fun f _ => hr f
    _ = ∑ e, (∑ f, R f * s f e) * w e := by
      rw [Finset.sum_comm]
      simp only [Finset.sum_mul]
    _ ≤ ∑ e, (3 * m e) * w e :=
      Finset.sum_le_sum fun e _ => mul_le_mul_of_nonneg_right (hc e) (hw e)
    _ = _ := by simp only [mul_assoc, Finset.mul_sum]

theorem gaussian_floor (v w j : ℝ) (hv : v ≤ 3*w) (hj : w ≤ 168*j) :
    v ≤ 504*j := by linarith

-- NATIVE CHILD 1
theorem gated_deficit (b d k g r : ℝ) (hg : 0 < g)
    (h : b ≤ d + r*d/g + k) :
    (b-k)*g ≤ d*(g+r) := by
  have h' := mul_le_mul_of_nonneg_right h hg.le
  rw [add_mul, add_mul, div_mul_cancel₀ _ hg.ne'] at h'
  nlinarith only [h']

theorem rare_suppression (x u z k : ℝ) (hz : 0 ≤ z)
    (hu : x ≤ u) (h : u*z ≤ k) : x*z ≤ k :=
  (mul_le_mul_of_nonneg_right hu hz).trans h

-- NATIVE CHILD 2
theorem weighted_step (b d prev loss k m s : ℝ)
    (hm : 0 ≤ m) (hc : prev-loss ≤ b) (hd : b-k ≤ s*d) :
    m*prev - m*(loss+k) ≤ (m*s)*d := by
  have hh : prev-(loss+k) ≤ s*d := by linarith
  have h' := mul_le_mul_of_nonneg_left hh hm
  nlinarith only [h']

#print axioms sum_weighted_rows
#print axioms gaussian_floor
#print axioms gated_deficit
#print axioms rare_suppression
#print axioms weighted_step
end Millennium.G4.RareCoarse
