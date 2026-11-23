import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace HorizontalCurvature
theorem varyingFaces : (256 : ℕ) = 256 := by decide
theorem speedSquared : (1024 : ℕ) = 1024 := by decide
theorem actionExpansion (u z : ℝ) : 2*(u-z)^2=2*u^2-4*u*z+2*z^2 := by ring
theorem tensorNumerator (b v u : ℝ) : 4*v-8*b*v*u=4*v*(1-2*b*u) := by ring
#print axioms varyingFaces
#print axioms speedSquared
#print axioms actionExpansion
#print axioms tensorNumerator
end HorizontalCurvature
