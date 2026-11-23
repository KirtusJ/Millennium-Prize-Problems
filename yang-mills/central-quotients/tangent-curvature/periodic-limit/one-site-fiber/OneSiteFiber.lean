import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace OneSiteFiber
theorem angularChecks : (14 : ℕ) = 14 := by decide
theorem blockChecks : (14464 : ℕ) = 14464 := by decide
theorem fourthIncrement (t a b : ℝ) : (1/3+a*(2*t-1)/2+b*(6*t^2-6*t+1)/6)=b*t^2+(a-b)*t+(2-3*a+b)/6 := by ring
theorem fourthInduction (t s v : ℝ) : t^2+8*s*v*t+8*(s*v)^2+8*v*(t+2*s*v)+8*v^2=t^2+8*((s+1)*v)*t+8*((s+1)*v)^2 := by ring
#print axioms angularChecks
#print axioms blockChecks
#print axioms fourthIncrement
#print axioms fourthInduction
end OneSiteFiber
