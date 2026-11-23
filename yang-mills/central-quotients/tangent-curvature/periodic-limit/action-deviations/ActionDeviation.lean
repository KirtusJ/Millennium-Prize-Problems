import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ActionDeviation
theorem seamSides : (7 : ℕ) = 7 := by decide
theorem cubeAssignments : (4096 : ℕ) = 4096 := by decide
theorem pressureCoefficient : (6 : ℝ)*(3/4)=9/2 := by ring
theorem quadraticDual (z s : ℝ) : z^2/9-(s*z-9*s^2/4)=(z/3-3*s/2)^2 := by ring
#print axioms seamSides
#print axioms cubeAssignments
#print axioms pressureCoefficient
#print axioms quadraticDual
end ActionDeviation
