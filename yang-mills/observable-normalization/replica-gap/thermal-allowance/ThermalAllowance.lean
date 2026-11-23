import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace YangMills.ThermalAllowance

theorem twoBins (a b c d : ℝ) :
    (a^2+b^2)^2 + 2*(a*c+b*d)^2 + (c^2+d^2)^2 =
    (a^2+b^2+c^2+d^2)^2 - 2*(a*d-b*c)^2 := by ring

theorem endpointMixture (z c : ℝ) (h0 : 0 ≤ c) (h1 : c ≤ 1) :
    (z-c)^2 ≤ (1-c)*z^2+c*(1-z)^2 := by
  nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]

theorem atomCap (q u : ℝ) (hq : 0 ≤ q) (hhalf : q ≤ 1/2)
    (hu : 0 ≤ u) (hu1 : u ≤ 1) : q*u*(1-q*u) ≤ q*(1-q) := by
  have h := mul_le_mul_of_nonneg_left hu1 hq
  have hpos : 0 ≤ 1-q-q*u := by linarith
  nlinarith [mul_nonneg (show 0 ≤ q-q*u by linarith) hpos]

theorem purityCap (p q : ℝ) (bound : p ≤ (1-q)^2+q^2) :
    q*(1-q) ≤ (1-p)/2 := by nlinarith

theorem bestLag (a b r : ℝ) (ordered : b ≤ a) (hr : 0 ≤ r) :
    b-r*a ≤ (1-r)*b := by nlinarith [mul_nonneg hr (sub_nonneg.mpr ordered)]

end YangMills.ThermalAllowance
#print axioms YangMills.ThermalAllowance.twoBins
#print axioms YangMills.ThermalAllowance.endpointMixture
#print axioms YangMills.ThermalAllowance.atomCap
#print axioms YangMills.ThermalAllowance.purityCap
#print axioms YangMills.ThermalAllowance.bestLag
