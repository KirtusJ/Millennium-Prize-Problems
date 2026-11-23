import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.Isotropic

theorem signed_winding (a d : ℝ) : (a-d)^2 - (a+d)^2 = -4*a*d := by ring

theorem total_variance_bounds (x m j lo hi : ℝ)
    (h : x = m+j) (hl : lo ≤ j) (hu : j ≤ hi) : m+lo ≤ x ∧ x ≤ m+hi := by
  constructor <;> linarith

-- NATIVE CHILD 1
theorem star_second_moment (a b : ℝ) : (a+b)^2 ≤ 2*(a^2+b^2) := by
  nlinarith only [sq_nonneg (a-b)]

theorem shell_weights (r : ℝ) (hr : 1 ≤ r) : 2*(2*r+1)^2 ≤ 18*r^2 := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hr) (by linarith : 0 ≤ 10*r+2)]

theorem directed_influence (c : ℝ) (hc : 6/25 ≤ c) : 1 < 6*c := by linarith

-- NATIVE CHILD 2
theorem transfer_defect (x j h : ℝ) (hx : 0 < x) (hh : h ≤ x-j) :
    h/x ≤ 1-j/x := by
  rw [le_sub_iff_add_le, ← add_div, div_le_iff₀ hx]
  linarith

#print axioms signed_winding
#print axioms total_variance_bounds
#print axioms star_second_moment
#print axioms shell_weights
#print axioms directed_influence
#print axioms transfer_defect
end Millennium.G4.Isotropic
