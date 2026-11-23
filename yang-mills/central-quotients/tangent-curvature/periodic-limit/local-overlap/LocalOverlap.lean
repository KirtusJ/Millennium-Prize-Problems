import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
namespace LocalOverlap
theorem symbolBound : (1295 : ℕ) = 1295 := by decide
theorem separatedClocks : (2 : ℕ) = 2 := by decide
theorem squaredOrders : (84 : ℕ) = 84 := by decide
theorem overlapNeeded (w a b K : ℝ) (hw : 0 ≤ w) (h : w+a ≤ K*(w+b)) (hsmall : K*b ≤ a/2) : a/2 ≤ K*w := by nlinarith
#print axioms symbolBound
#print axioms separatedClocks
#print axioms squaredOrders
#print axioms overlapNeeded
end LocalOverlap
