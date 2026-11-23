import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.FineMixing

theorem decay_product (r y : ℝ) (hr : 0 ≤ r) :
    Real.exp (-y) * (1-Real.exp (-(r*y))) ≤ r*(1-Real.exp (-y)) := by
  have h1 : 1 - Real.exp (-(r*y)) ≤ r*y := by
    linarith [Real.add_one_le_exp (-(r*y))]
  have h2 : y*Real.exp (-y) ≤ 1-Real.exp (-y) := by
    have h := mul_le_mul_of_nonneg_right (Real.add_one_le_exp y) (Real.exp_pos (-y)).le
    rw [← Real.exp_add, add_neg_cancel, Real.exp_zero] at h
    linarith
  calc
    _ ≤ Real.exp (-y)*(r*y) := mul_le_mul_of_nonneg_left h1 (Real.exp_pos _).le
    _ = r*(y*Real.exp (-y)) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left h2 hr

theorem inherited_deficit (b d r g v : ℝ) (hg : 0 < g)
    (h : b ≤ d+v/g) (hv : v ≤ r*d) : b*g ≤ d*(g+r) := by
  have hh := mul_le_mul_of_nonneg_right h hg.le
  rw [add_mul, div_mul_cancel₀ _ hg.ne'] at hh
  nlinarith only [hh,hv]

-- NATIVE CHILD 1
theorem full_colour_comparison (sumJ fine alpha : ℝ) (h : alpha*fine ≤ 2*sumJ) :
    (alpha/48)*fine ≤ sumJ/24 := by linarith

theorem gaussian_full_floor (v off sumJ : ℝ) (hv : v ≤ 16*off)
    (hj : off ≤ 7*sumJ) : v/2688 ≤ sumJ/24 := by linarith

-- NATIVE CHILD 2
theorem sphere_moment (k m : ℝ) (hm : m ≤ 1) :
    2*k^2+6*k+(k-3)^2*m ≤ 3*k^2+9 := by
  nlinarith only [mul_le_mul_of_nonneg_left hm (sq_nonneg (k-3))]

theorem local_to_global_score (v c : ℝ) (h : 4*c ≤ 256*v) : c/64 ≤ v := by linarith

#print axioms decay_product
#print axioms inherited_deficit
#print axioms full_colour_comparison
#print axioms gaussian_full_floor
#print axioms sphere_moment
#print axioms local_to_global_score
end Millennium.G4.FineMixing
