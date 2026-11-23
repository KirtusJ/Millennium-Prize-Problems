import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace Collective
theorem exponent (s p : ℝ) : (s+p/2)^2+(p/2-s)^2=2*s^2+p^2/2 := by ring
theorem gram (s p d : ℝ) : (s+p+d)*(s+p-d)-(p-s)^2=4*s*p-d^2 := by ring
theorem filledBall (k a : ℝ) : 2*k^2*a^6/6=(5*a/3)*(k^2*a^5/5) := by ring
#print axioms exponent
#print axioms gram
#print axioms filledBall
end Collective
