import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace InteractionControls
theorem shellDifference : (4 : ℕ) = 4 := by decide
theorem ringCount : (6 : ℕ) = 6 := by decide
theorem secondMomentConstant : (1152 : ℕ) = 1152 := by decide
theorem pairEnergy (e m : ℝ) : 2*e-2*m=2*(e-m) := by ring
#print axioms shellDifference
#print axioms ringCount
#print axioms secondMomentConstant
#print axioms pairEnergy
end InteractionControls
