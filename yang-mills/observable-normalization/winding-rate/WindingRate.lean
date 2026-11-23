import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace YangMills.WindingRate

theorem renewal (p s : ℝ) :
    (1-s*p+5*p^2)*(1+s*p)+(s^2-6)*p^2 =
      1-p^2+5*s*p^3 := by ring

theorem denominator (p m c : ℝ) :
    1-2*(3+m*(c-1))*p+5*p^2 =
    (1-p)*(1-5*p)-2*m*p*(c-1) := by ring

theorem strictGain (p m : ℝ) (hp : 0 < p) (hq : 5*p < 1) (hm : m ≤ 3) :
    m*(1-5*p) < 5*(1-p) := by
  have h := mul_le_mul_of_nonneg_right hm (by linarith : 0 ≤ 1-5*p)
  linarith

theorem blockAllowance : (9/10:ℝ)*(101/100)^8 < 1 := by norm_num
theorem unweightedAllowance : (308981:ℝ)*(41/200)^8 < 1 := by norm_num
end YangMills.WindingRate
#print axioms YangMills.WindingRate.renewal
#print axioms YangMills.WindingRate.denominator
#print axioms YangMills.WindingRate.strictGain
#print axioms YangMills.WindingRate.blockAllowance
#print axioms YangMills.WindingRate.unweightedAllowance
