import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace YangMills.OpenSlab

theorem normalization (n z c r : ℝ) (hc : c*z=n) :
    (r*c)*z=r*n := by rw [mul_assoc,hc]

theorem tail (low high total next q : ℝ) (h : total=low+high)
    (bound : next ≤ low+q*high) :
    next-q*total ≤ (1-q)*low := by rw [h]; linarith

theorem calibratedRatio (c k cmin kmin : ℝ) (hc : cmin ≤ c)
    (hk : kmin ≤ k) (hp : 0 ≤ cmin) (hk0 : 0 ≤ k) :
    cmin*kmin ≤ c*k := by
  calc
    cmin*kmin ≤ cmin*k := mul_le_mul_of_nonneg_left hk hp
    _ ≤ c*k := mul_le_mul_of_nonneg_right hc hk0

theorem falseSignal : (4/5 : ℝ) > 3/4 := by norm_num
theorem correctedSignal : (4/5 : ℝ)*(5/8)=1/2 := by norm_num

end YangMills.OpenSlab
#print axioms YangMills.OpenSlab.normalization
#print axioms YangMills.OpenSlab.tail
#print axioms YangMills.OpenSlab.calibratedRatio
#print axioms YangMills.OpenSlab.falseSignal
#print axioms YangMills.OpenSlab.correctedSignal
