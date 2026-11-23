import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.ExteriorEnergy

theorem minorSum (a b c : ℝ) :
    2*(a^2*b^2+a^2*c^2+b^2*c^2) ≥ 2*a^2*(b^2+c^2) := by
  nlinarith only [sq_nonneg (b*c)]

theorem secondDirection (r a b c : ℝ) (ha : 0 ≤ a) (hc : 0 ≤ c) (hcb : c ≤ b)
    (h : r^2=a^2+b^2+c^2) (hr : 1 ≤ r-a) :
    r ≤ 2*b^2 := by
  have hx : 0 ≤ r+a := by linarith
  nlinarith only [h,mul_nonneg (show 0 ≤ r-a-1 by linarith) hx,
    mul_nonneg (sub_nonneg.mpr hcb) (show 0 ≤ b+c by linarith),ha]

theorem fiberSquare (r t : ℝ) :
    (2*r*t)^2/2=2*r^2*t^2 := by ring

theorem planeAverage (l wx wy z v w : ℝ) :
    ((wx*w-wy*v)^2+(wy*z-l*w)^2+(l*v-wx*z)^2+
     (wx*w-wy*v)^2+(wy*z+l*w)^2+(l*v+wx*z)^2)/2 =
    (wx*w-wy*v)^2+z^2*(wx^2+wy^2)+l^2*(v^2+w^2) := by ring

theorem gaussianEnergy (r c : ℝ) (hr : 0 < r) :
    2*r + 2*(r+c)^2/r = 4*r + 4*c + 2*c^2/r := by
  field_simp
  ring

end YangMills.ExteriorEnergy
#print axioms YangMills.ExteriorEnergy.minorSum
#print axioms YangMills.ExteriorEnergy.secondDirection
#print axioms YangMills.ExteriorEnergy.fiberSquare
#print axioms YangMills.ExteriorEnergy.planeAverage
#print axioms YangMills.ExteriorEnergy.gaussianEnergy
