import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace YangMills.GradientEndpoints

/-- One coordinate of the second-order imaginary quaternion term. -/
theorem productArea (a b c d : ℝ) :
    a*(d-b)-b*(c-a) + (a+c-a)*(-d)-(b+d-b)*(-c) = a*d-b*c := by ring

theorem originShift (a b c d u v : ℝ) :
    (a+u)*(d+v)-(b+v)*(c+u) = a*d-b*c+u*(d-b)-v*(c-a) := by ring

theorem squareCurl (a b : ℝ) :
    2*a*b+2*a*b-(-2*a*b)-(-2*a*b)=8*a*b := by ring

theorem linkAndFace (a b : ℝ) :
    ((2*a*b)^2+(-2*a*b)^2)/2 + (8*a*b)^2/4=20*a^2*b^2 := by ring

theorem gaussianCancellation (x y : ℝ) :
    -(x+y)/2-(-x-y)/2=0 := by ring

end YangMills.GradientEndpoints
#print axioms YangMills.GradientEndpoints.productArea
#print axioms YangMills.GradientEndpoints.originShift
#print axioms YangMills.GradientEndpoints.squareCurl
#print axioms YangMills.GradientEndpoints.linkAndFace
#print axioms YangMills.GradientEndpoints.gaussianCancellation
