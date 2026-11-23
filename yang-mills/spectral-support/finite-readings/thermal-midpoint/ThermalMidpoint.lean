import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.ThermalMidpoint

theorem cancelStatic (r s : ℝ) : 2*(r+1)*s-s-(2*r+1)*s=0 := by ring

theorem threeReadings (r y : ℝ) :
    2*(r+1)*y-(2*y^2-1)-(2*r+1)=2*(y-1)*(r-y) := by ring

theorem peak (r y : ℝ) : 4*(y-1)*(r-y) ≤ (r-1)^2 := by
  nlinarith only [sq_nonneg (2*y-r-1)]

theorem above (r y : ℝ) (hy : 1 ≤ y) (hr : r ≤ y) :
    (y-1)*(r-y) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.mpr hy) (sub_nonpos.mpr hr)

theorem midpointEquality (r : ℝ) :
    4*((1+r)/2-1)*(r-(1+r)/2)=(r-1)^2 := by ring

theorem offsetExample : 2*(5/4+1 : ℝ)*(17/16)-(2*(17/16 : ℝ)^2-1)-(2*(5/4 : ℝ)+1)>0 := by
  norm_num

end YangMills.ThermalMidpoint
#print axioms YangMills.ThermalMidpoint.threeReadings
#print axioms YangMills.ThermalMidpoint.cancelStatic
#print axioms YangMills.ThermalMidpoint.peak
#print axioms YangMills.ThermalMidpoint.above
#print axioms YangMills.ThermalMidpoint.midpointEquality
#print axioms YangMills.ThermalMidpoint.offsetExample
