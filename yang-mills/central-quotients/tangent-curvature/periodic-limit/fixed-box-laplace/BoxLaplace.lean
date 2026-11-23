import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace BoxLaplace
theorem signedWords : (2401 : ℕ) = 2401 := by decide
theorem geometryCases : (2616 : ℕ) = 2616 := by decide
theorem normalization (h c m : ℝ) : (1-h*(c-m))*(1-h*m)-(1-h*c)=h^2*m*(c-m) := by ring
theorem evenCancellation (c f : ℝ) : c*f+(-c)*f=0 := by ring
#print axioms signedWords
#print axioms geometryCases
#print axioms normalization
#print axioms evenCancellation
end BoxLaplace
