import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.FineTail

theorem scalar_time_split (h d x y : ℝ)
    (hh : 0 ≤ h) (hx : 0 ≤ x) (hy : 0 ≤ y)
    (_hh1 : h ≤ 1) (hxd : x ≤ d) (hy1 : y ≤ 1) :
    x ^ 2 + h * y ^ 2 ≤ d ^ 2 + h := by
  have hx2 : x ^ 2 ≤ d ^ 2 := by
    simpa only [pow_two] using mul_self_le_mul_self hx hxd
  have hy2 : y ^ 2 ≤ 1 := by
    simpa only [pow_two, mul_one] using mul_self_le_mul_self hy hy1
  have hhy : h * y ^ 2 ≤ h := by
    simpa only [mul_one] using mul_le_mul_of_nonneg_left hy2 hh
  exact add_le_add hx2 hhy

-- NATIVE CHILD 1
theorem retained_and_tail (u e x y : ℝ) :
    (u*x + e*y)^2 ≤ (u^2 + e^2)*(x^2 + y^2) := by
  nlinarith only [sq_nonneg (u*y-e*x)]

-- NATIVE CHILD 2
theorem angle_bound (h t s : ℝ) (hh : h ≤ 1) (ht : t ≤ s) :
    t + h*(1-t) ≤ h+(1-h)*s := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hh) (sub_nonneg.mpr ht)]

#print axioms scalar_time_split
#print axioms retained_and_tail
#print axioms angle_bound

end Millennium.G4.FineTail
