import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.Plaquette

/-- The second trace is that of P Q^{-1}, with the common edge forward in both loops. -/
theorem joinedTrace (a b x y z u v w : ℝ) :
    (2*(a*b + x*u + y*v + z*w))/2 - (2*a)*(2*b)/4 =
      x*u + y*v + z*w := by ring

/-- With the same edge convention, the defect instead uses the trace of P Q. -/
theorem mismatch (a b x y z u v w : ℝ)
    (hp : a^2+x^2+y^2+z^2=1) (hq : b^2+u^2+v^2+w^2=1) :
    (x+u)^2+(y+v)^2+(z+w)^2 =
      2-2*(a*b-x*u-y*v-z*w)-(a-b)^2 := by
  linarith only [hp,hq]

/-- For equal diagonal gradient moments A and cross moment B. -/
theorem edgeDecomposition (c d A B : ℝ) :
    A*c^2+2*B*c*d+A*d^2 = A*(c-d)^2+c*d*(2*A+2*B) := by ring

/-- A uniform estimate for signed coefficients on a pair of neighboring plaquettes. -/
theorem edgeUpper (c d A B : ℝ) (hm : 0 ≤ A-B) (hp : 0 ≤ A+B) :
    A*c^2+2*B*c*d+A*d^2 ≤ 2*A*(c^2+d^2) := by
  have h := mul_nonneg hm (sq_nonneg (c+d))
  have g := mul_nonneg hp (sq_nonneg (c-d))
  linarith only [h,g]

/-- A measured upper energy form and positive variance bound work for the same smearing. -/
theorem commonSmearing {energy variance R numerator denominator : ℝ}
    (hvar : 0 < variance) (hden : denominator ≤ variance)
    (hnum : energy ≤ numerator) (hcmp : numerator ≤ R*denominator) (hR : 0 ≤ R) :
    energy / variance ≤ R := by
  exact (div_le_iff₀ hvar).mpr (hnum.trans (hcmp.trans (mul_le_mul_of_nonneg_left hden hR)))

end YangMills.Plaquette
#print axioms YangMills.Plaquette.joinedTrace
#print axioms YangMills.Plaquette.mismatch
#print axioms YangMills.Plaquette.edgeDecomposition
#print axioms YangMills.Plaquette.edgeUpper
#print axioms YangMills.Plaquette.commonSmearing
