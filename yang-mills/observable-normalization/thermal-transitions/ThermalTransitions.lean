import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

namespace YangMills.ThermalTransitions

/-- A forward or backward geometric contribution has the same multiplier. -/
theorem geometricStep (v z : ℝ) :
    v*z - 2*v + v/z = (z+1/z-2)*v := by ring

theorem positiveMultiplier (z : ℝ) (hz : 0 < z) :
    0 ≤ z+1/z-2 := by
  have h : z+1/z-2 = (z-1)^2/z := by field_simp [ne_of_gt hz]; ring
  rw [h]
  positivity

theorem determinantPair (a b x y : ℝ) :
    (a+b)*(a*x^2+b*y^2)-(a*x+b*y)^2 = a*b*(x-y)^2 := by ring

theorem shiftedPair (a b x y : ℝ) :
    (a*x+b*y)*(a*x^3+b*y^3)-(a*x^2+b*y^2)^2 = a*b*x*y*(x-y)^2 := by ring

theorem stationaryAndMoving (a b x : ℝ) :
    (a+b)*(b*x^2)-(b*x)^2 = a*b*x^2 ∧
    (b*x)*(b*x^3)-(b*x^2)^2 = 0 := by constructor <;> ring

end YangMills.ThermalTransitions
#print axioms YangMills.ThermalTransitions.geometricStep
#print axioms YangMills.ThermalTransitions.positiveMultiplier
#print axioms YangMills.ThermalTransitions.determinantPair
#print axioms YangMills.ThermalTransitions.shiftedPair
#print axioms YangMills.ThermalTransitions.stationaryAndMoving
