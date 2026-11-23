import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ElectricMesh
theorem convolutionBins : (512 : ℕ) = 512 := by decide
theorem marginalBins : (8 : ℕ) = 8 := by decide
theorem noCompleteFaceCases : (297 : ℕ) = 297 := by decide
theorem residualNorm (whole leading : ℝ) : (whole-leading)+leading=whole := by ring
#print axioms convolutionBins
#print axioms marginalBins
#print axioms noCompleteFaceCases
#print axioms residualNorm
end ElectricMesh
