import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.LowSpin

open scoped InnerProductSpace

theorem bessel_ratio_step (r x : ℝ) (hx : 0 ≤ x)
    (h : 3*r ≤ 2*x*(1-r)) : r ≤ 2*x/(2*x+3) := by
  apply (le_div_iff₀ (by linarith : 0 < 2*x+3)).2
  linarith only [h]

-- NATIVE CHILD 1
theorem adjoint_conditional_square (p : ℝ) :
    (4*p^2-1)^2 = 1+(4*p^2-1)+(16*p^4-12*p^2+1) := by
  ring

-- NATIVE CHILD 2
theorem common_exterior_pairing {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (x y : H) (θ nx ny : ℝ) (hx : ‖x‖ ≤ θ*nx) (hy : ‖y‖ ≤ θ*ny) :
    ‖⟪x,y⟫_ℂ‖ ≤ θ^2*(nx*ny) := by
  calc
    ‖⟪x,y⟫_ℂ‖ ≤ ‖x‖ * ‖y‖ := norm_inner_le_norm x y
    _ ≤ (θ*nx)*(θ*ny) := mul_le_mul hx hy (norm_nonneg y) ((norm_nonneg x).trans hx)
    _ = θ^2*(nx*ny) := by ring

theorem variance_transmission (r d u t : ℝ)
    (hr : 0 < r) (hd : 0 ≤ d) (hu : r ≤ u) (ht : t ≤ r-d) :
    t/r ≤ 1-d/u := by
  have hpos : 0 < u := lt_of_lt_of_le hr hu
  have hfrac : d/u ≤ d/r := div_le_div_of_nonneg_left hd hr hu
  have hbound : t/r ≤ (r-d)/r := (div_le_div_iff_of_pos_right hr).2 ht
  rw [sub_div, div_self (ne_of_gt hr)] at hbound
  linarith

#print axioms bessel_ratio_step
#print axioms adjoint_conditional_square
#print axioms common_exterior_pairing
#print axioms variance_transmission

end Millennium.G4.LowSpin
