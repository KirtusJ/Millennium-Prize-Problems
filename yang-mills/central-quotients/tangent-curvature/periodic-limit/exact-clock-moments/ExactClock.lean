import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace ExactClock
theorem equalCount : (3 : ℕ) = 3 := by decide
theorem unmatchedThird : (120 : ℕ) = 120 := by decide
theorem quadratic (a b c : ℝ) : 8*(25*a+5*b+c)+10*(4*a+2*b+c)=3*c+15*(16*a+4*b+c) := by ring
theorem variation : (3+10+15 : ℕ) = 28 := by decide
#print axioms equalCount
#print axioms unmatchedThird
#print axioms quadratic
#print axioms variation
end ExactClock
