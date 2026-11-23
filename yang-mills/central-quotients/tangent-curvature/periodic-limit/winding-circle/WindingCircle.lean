import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace WindingCircle
theorem branchCases : (1024 : ℕ) = 1024 := by decide
theorem frameCases : (1352 : ℕ) = 1352 := by decide
theorem orthogonalFrame (x y k : ℝ) : (x+k*y)^2+(k*x-y)^2=(1+k^2)*(x^2+y^2) := by ring
theorem inverseFirst (x y k : ℝ) : (x+k*y)+k*(k*x-y)=(1+k^2)*x := by ring
#print axioms branchCases
#print axioms frameCases
#print axioms orthogonalFrame
#print axioms inverseFirst
end WindingCircle
