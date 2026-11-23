import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

namespace YangMills.ThermalCount

theorem deficitIdentity {s t : ℝ} (h : 1+s ≠ 0) :
    1-(1+t)/(1+s)^2 = (2*s+s^2-t)/(1+s)^2 := by
  field_simp
  ring

theorem deficitFactors {s t : ℝ} (hs : 0 ≤ s) (ht : 0 ≤ t) (hm : t ≤ s^2) :
    2*s/(1+s)^2 ≤ (2*s+s^2-t)/(1+s)^2 ∧
    (2*s+s^2-t)/(1+s)^2 ≤ 2*s := by
  have hd : 0 < (1+s)^2 := by positivity
  constructor
  · exact div_le_div_of_nonneg_right (by linarith) hd.le
  · apply (div_le_iff₀ hd).2
    nlinarith [sq_nonneg s, pow_nonneg hs 3]

theorem rankLoss {a b e : ℝ} (hb : 0 < b) (he : 6*b-a^2 ≤ e) :
    6-e/b ≤ a^2/b := by
  apply (le_div_iff₀ hb).2
  rw [sub_mul, div_mul_cancel₀ _ hb.ne']
  linarith

end YangMills.ThermalCount
#print axioms YangMills.ThermalCount.deficitIdentity
#print axioms YangMills.ThermalCount.deficitFactors
#print axioms YangMills.ThermalCount.rankLoss
