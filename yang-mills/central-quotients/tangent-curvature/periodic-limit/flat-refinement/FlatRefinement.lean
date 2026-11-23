import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace FlatRefinement
theorem hardShells : ([6,12,8] : List ℕ) = [6,12,8] := by decide
theorem radialTrace : (288 - 3*24 : ℕ) = 216 := by decide
theorem symbolCoefficient (s : ℝ) : -(12+(-216+384*s)/2)=24*(4-8*s) := by ring
#print axioms hardShells
#print axioms radialTrace
#print axioms symbolCoefficient
end FlatRefinement
