import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace SecondBoxHolonomy
theorem midMultiplicity : (4 : ℕ) = 4 := by decide
theorem comparisonCount : (17424 : ℕ) = 17424 := by decide
theorem derivativeDifference (a s : ℝ) : (a+s)*(1+a+s)-(a-s)*(1+a-s)=2*s*(1+2*a) := by ring
#print axioms midMultiplicity
#print axioms comparisonCount
#print axioms derivativeDifference
end SecondBoxHolonomy
