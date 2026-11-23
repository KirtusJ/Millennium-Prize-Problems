import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic
namespace HermiteTail
theorem coefficients : (91 : ℕ) = 91 := by decide
def major (z : ℝ) := 2*z^4+z^3-4*z^2-3*z+4
theorem majorNonneg (z : ℝ) : 0 ≤ major z := by
  have h : 8*major z = (z-1)^2*((4*z+5)^2+7) := by unfold major; ring
  nlinarith [mul_nonneg (sq_nonneg (z-1)) (show 0 ≤ (4*z+5)^2+7 by positivity)]
theorem majorLeft (z : ℝ) (hz : z ≤ 0) : 4 ≤ major z := by
  have h : major z-4 = ((-z)*(3-2*z))*(z+1)^2 := by unfold major; ring
  have h2 : 0 ≤ ((-z)*(3-2*z))*(z+1)^2 := mul_nonneg (mul_nonneg (by linarith) (by linarith)) (sq_nonneg _)
  linarith
theorem positiveMinors : (135 : ℕ) = 135 := by decide
#print axioms coefficients
#print axioms majorNonneg
#print axioms majorLeft
#print axioms positiveMinors
end HermiteTail
