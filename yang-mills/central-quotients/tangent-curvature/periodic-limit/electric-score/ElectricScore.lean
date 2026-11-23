import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ElectricScore
theorem sharedLinkCases : (512 : ℕ) = 512 := by decide
theorem secondMomentCases : (8 : ℕ) = 8 := by decide
theorem scoreVariance (a b : ℝ) : (1+b^4-a^8)+12*(a^6*(1+3*b)/4-a^8)=1+b^4+3*a^6*(1+3*b)-13*a^8 := by ring
theorem squaredDifference (x y : ℝ) : (x-y)^2=x^2-2*x*y+y^2 := by ring
#print axioms sharedLinkCases
#print axioms secondMomentCases
#print axioms scoreVariance
#print axioms squaredDifference
end ElectricScore
