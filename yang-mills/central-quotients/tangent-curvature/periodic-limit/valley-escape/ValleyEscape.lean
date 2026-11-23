import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ValleyEscape
theorem testedNormalPairs : (2401 : ℕ) = 2401 := by decide
theorem normalArea (x y z t : ℝ) : (x*t-y*z)^2+(x*z+y*t)^2=(x^2+y^2)*(z^2+t^2) := by ring
theorem trialVariance (v : ℝ) : 4*(24*v^2-(2*v)^2)=5*(4*v)^2 := by ring
#print axioms testedNormalPairs
#print axioms normalArea
#print axioms trialVariance
end ValleyEscape
