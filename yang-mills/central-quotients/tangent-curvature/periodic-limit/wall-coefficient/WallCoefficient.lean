import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace WallCoefficient
theorem chartLaplacian : (8 : ℕ) = 8 := by decide
theorem jacobian (h k : ℝ) : (1-h)^2-(1-h)*h+k^2=1-3*h+2*h^2+k^2 := by ring
theorem signedTotal (q : ℝ) : (-20-12-12+1+24+9)*q= -10*q := by ring
#print axioms chartLaplacian
#print axioms jacobian
#print axioms signedTotal
end WallCoefficient
