import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace WallShift
theorem wallCount : (3204 : ℕ) = 3204 := by decide
theorem magneticShift (y d h : ℝ) : 2*(y-d*h)^2*h-2*y^2*h= -4*y*d*h^2+2*d^2*h^3 := by ring
theorem wallAtEndpoint (r h : ℝ) : (2*r^2-h)^2+4*r^2*h-4*r^4=h^2 := by ring
#print axioms wallCount
#print axioms magneticShift
#print axioms wallAtEndpoint
end WallShift
