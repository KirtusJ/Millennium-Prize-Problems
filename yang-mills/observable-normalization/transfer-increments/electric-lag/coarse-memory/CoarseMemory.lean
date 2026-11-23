import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace YangMills.CoarseMemory

/-- Fiber variance of a two-point fine law at a fixed coarse value. -/
theorem fiberVariance (w x y : ℝ) :
    w*x^2+(1-w)*y^2-(w*x+(1-w)*y)^2=w*(1-w)*(x-y)^2 := by ring

theorem variancePositive (w x y : ℝ) (hw : 0 < w) (hw' : w < 1)
    (hxy : x ≠ y) : 0 < w*(1-w)*(x-y)^2 := by
  exact mul_pos (mul_pos hw (sub_pos.mpr hw')) (sq_pos_of_ne_zero (sub_ne_zero.mpr hxy))

/-- Covariances kill the common constant in the electric endpoint law. -/
theorem covarianceProduct (a b x y t : ℝ) :
    (a+t*x)*(b+t*y)-a*b-t*(a*y+b*x)=t^2*x*y := by ring

theorem traceResponse (a b : ℝ) :
    (a/4)^2+3*(b/4)^2=(a^2+3*b^2)/16 := by ring

/-- For binary endpoints the four deviations from the independent law
have equal magnitudes and sum to zero. -/
theorem binaryResidual (x y m v : ℝ) :
    (1+m*x+m*y+(m^2+v)*x*y)/4-((1+m*x)/2)*((1+m*y)/2)=v*x*y/4 := by ring

end YangMills.CoarseMemory
#print axioms YangMills.CoarseMemory.fiberVariance
#print axioms YangMills.CoarseMemory.variancePositive
#print axioms YangMills.CoarseMemory.covarianceProduct
#print axioms YangMills.CoarseMemory.traceResponse
#print axioms YangMills.CoarseMemory.binaryResidual
