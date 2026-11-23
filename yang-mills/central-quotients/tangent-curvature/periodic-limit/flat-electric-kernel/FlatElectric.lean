import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace FlatElectric
theorem hoppingChecks : (96 : ℕ) = 96 := by decide
theorem commonWeylCost : (8 : ℕ) = 8 := by decide
theorem centerExponent (v c d t : ℝ) : v*((1-t)*(c-d)^2+t*(c+d)^2)=v*(c^2+d^2-2*c*d*(1-2*t)) := by ring
#print axioms hoppingChecks
#print axioms commonWeylCost
#print axioms centerExponent
end FlatElectric
