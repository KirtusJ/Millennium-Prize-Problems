import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.OrbitStep

theorem constantAction (c d a b t : ℝ) :
    1-(c*d+t*a*b) = (1-c*d)-t*a*b := by ring
theorem diagonal (c s t : ℝ) (h : c^2+s^2=1) :
    1-(c*c+t*s*s)=(1-t)*s^2 := by nlinarith

theorem normalHessian (a b : ℝ) :
    (a^2+b^2)/2-a*b=(a-b)^2/2 := by ring
theorem contrast (u v : ℝ) :
    -(u^2+v^2)/2-((-u^2)+(-v^2))/2=0 := by ring

theorem rotorQuartic (x y z : ℝ) :
    (x^2+y^2)/12-z^2/6=(x^2+y^2-2*z^2)/12 := by ring

end YangMills.OrbitStep
#print axioms YangMills.OrbitStep.constantAction
#print axioms YangMills.OrbitStep.diagonal
#print axioms YangMills.OrbitStep.normalHessian
#print axioms YangMills.OrbitStep.contrast
#print axioms YangMills.OrbitStep.rotorQuartic
