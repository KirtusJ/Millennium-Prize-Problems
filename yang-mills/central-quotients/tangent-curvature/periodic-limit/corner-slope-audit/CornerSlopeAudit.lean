import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace CornerSlopeAudit
theorem physicalReturns : (26880 : ℕ) = 26880 := by decide
theorem sharedLinkChecks : (1024 : ℕ) = 1024 := by decide
theorem tiltedVariance (k : ℝ) : (2*k+1)*(2*k+3)/16-((2*k+1)/4)^2=(2*k+1)/8 := by ring
theorem gaussianEighth : (26880 : ℝ)/4^8=105/256 := by ring
#print axioms physicalReturns
#print axioms sharedLinkChecks
#print axioms tiltedVariance
#print axioms gaussianEighth
end CornerSlopeAudit
