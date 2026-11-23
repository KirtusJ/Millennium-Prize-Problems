import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace WindingPairs
theorem diagonalFloor (l u w : ℝ) (hl : l ≤ u) (hw : 0 ≤ w) : l ≤ (1-w)*l+w*u := by nlinarith [mul_nonneg hw (sub_nonneg.mpr hl)]
theorem energyWeight (m w e : ℝ) (h : (1-w)*e ≤ m) : e-m ≤ e*w := by nlinarith only [h]
theorem transferWeight (r w q : ℝ) (h : r ≤ w+(1-w)*q) : r-q ≤ (1-q)*w := by nlinarith only [h]
theorem commonMix (g a b c d : ℝ) : (g-a)*(b-g)-(g-c)*(d-g)=(a+b-c-d)*g+c*d-a*b := by ring
#print axioms diagonalFloor
#print axioms energyWeight
#print axioms transferWeight
#print axioms commonMix
end WindingPairs
