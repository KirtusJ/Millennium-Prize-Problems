import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.AiryWall

theorem jacobianPolynomial (x a b c d : ℝ) :
    (x^2-a^2-c^2)*(x^2-b^2-d^2)-(a*b+c*d)^2 =
    x^4-x^2*(a^2+b^2+c^2+d^2)+(a*d-b*c)^2 := by ring

theorem wallShift (R x s : ℝ) (hx : 0 ≤ x) (h : x ≤ R)
    (he : R^2 ≤ x^2+s) : (R-x)*R ≤ s := by
  nlinarith only [he,mul_nonneg hx (sub_nonneg.mpr h)]

theorem potentialSplit (x u v : ℝ) :
    2*(x^2*u^2+x^2*v^2+u^2*v^2)=
    2*x^2*(u^2+v^2)+2*(u*v)^2 := by ring

theorem fourSquares (x a b c d : ℝ) :
    2*x^2*(a^2+b^2+c^2+d^2)=
    ((2*x*a)^2+(2*x*b)^2+(2*x*c)^2+(2*x*d)^2)/2 := by ring

theorem airyRescaling (x z f : ℝ) :
    -(4*f*(2*x+z))/2+4*x*f = -2*z*f := by ring

theorem gaussianVariance (v : ℝ) :
    (4*3*v^2+12*v^2)-(4*v)^2=8*v^2 := by ring
end YangMills.AiryWall
#print axioms YangMills.AiryWall.jacobianPolynomial
#print axioms YangMills.AiryWall.wallShift
#print axioms YangMills.AiryWall.potentialSplit
#print axioms YangMills.AiryWall.fourSquares
#print axioms YangMills.AiryWall.airyRescaling
#print axioms YangMills.AiryWall.gaussianVariance
