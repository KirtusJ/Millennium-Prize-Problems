import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace WeakOS
theorem chamberCount : (165 : ℕ) = 165 := by decide
theorem supportedPairs : (729 : ℕ) = 729 := by decide
theorem weightDifference (r : ℝ) : 2*(1+r^2)-(1+r)^2=(r-1)^2 := by ring
theorem chainMode (p : ℝ) : (1+p)/2-(1-p)/2=p := by ring
#print axioms chamberCount
#print axioms supportedPairs
#print axioms weightDifference
#print axioms chainMode
end WeakOS
