import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace YangMills.PlaneOverlap

theorem horizontalLoss (x y t f : ℝ) :
    (x^2+t^2)*(y^2+t^2)-(f*t^2+x*y)^2 =
    (1-f^2)*t^2*(y^2+t^2)+t^2*(f*y-x)^2 := by ring

theorem continuumLoss (u z : ℝ) :
    1+2*u*z+z^2-(1+u*z)^2=(1-u^2)*z^2 := by ring

theorem productSquare (u v : ℝ) :
    (v-u)^2-u^2=v*(v-2*u) := by ring

/-- Quartic coefficient in [log(1+uz)^2 - 2 log(1+uz) log(l)/2]/2,
where l is the shifted momentum norm. -/
theorem quartic (u : ℝ) :
    ((u^4/4+2*u^4/3)-
    (u*(4*u^3/3-u)+(-u^2/2)*(1/2-u^2)+(u^3/3)*u))/2
    =5*u^2*(1-u^2)/8 := by ring

end YangMills.PlaneOverlap
#print axioms YangMills.PlaneOverlap.horizontalLoss
#print axioms YangMills.PlaneOverlap.continuumLoss
#print axioms YangMills.PlaneOverlap.productSquare
#print axioms YangMills.PlaneOverlap.quartic
