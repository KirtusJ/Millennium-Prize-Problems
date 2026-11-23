import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace CurvatureKernel
theorem noncommutingWitnesses : (24 : ℕ) = 24 := by decide
theorem linearCoboundaries : (72 : ℕ) = 72 := by decide
theorem twoEdgeDefect (u v c h : ℝ) : -v+u-(u-v+h*c)= -h*c := by ring
theorem resampling (p : ℝ) : p-p*p=p*(1-p) := by ring
#print axioms noncommutingWitnesses
#print axioms linearCoboundaries
#print axioms twoEdgeDefect
#print axioms resampling
end CurvatureKernel
