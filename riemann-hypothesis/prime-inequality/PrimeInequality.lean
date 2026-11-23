import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Riemann.PrimeInequality

/-- Normalize the explicit source bracket by the mass of the distinguished cells. -/
theorem normalizeBracket {n t r m b k : ℝ} (a X : ℝ)
    (hn : 0 < n) (ht : 0 < t) (hr : 0 < r) (hm : 0 < m)
    (hb : 0 < b) (hk : 0 < k) :
    (t*a*(1+m^2/k) + m*(2*n*m*b*X + r*k*b*X/(n*(n/X)))) /
      (t*m*b*(r/n)/2) =
    2*(n/r)*(a/b)*(1/m+m/k) + 4*(n/t)*(n/r)*X*m +
      2*(n/t)*X^2*(k/n^2) := by
  field_simp
  ring

/-- Bounds for the inverse densities and the envelope scale give the four printed costs. -/
theorem fourCosts {X d v a x p q m z : ℝ}
    (hX : 1 ≤ X) (hd : 0 ≤ d) (ha : 0 ≤ a)
    (hx : 0 ≤ x) (hp : 0 ≤ p) (hq : 0 ≤ q) (hm : 0 ≤ m) (hz : 0 ≤ z)
    (hD : d ≤ X) (hV : v ≤ 2*X) (hA : a ≤ 2*x) :
    2*d*a*(p+q) + 4*v*d*X*m + 2*v*X^2*z ≤
      8*X^3*(x*p+x*q+m+z) := by
  have pos : 0 ≤ X := by linarith
  have cube : X ≤ X^3 := by nlinarith [mul_nonneg (by linarith : 0 ≤ X-1) (by nlinarith : 0 ≤ X^2+X)]
  have first : 2*d*a ≤ 8*X^3*x := by
    calc
      2*d*a ≤ 2*X*(2*x) := by gcongr
      _ ≤ 8*X^3*x := by nlinarith [mul_le_mul_of_nonneg_right cube hx, mul_nonneg pos hx]
  have mid : 4*v*d*X ≤ 8*X^3 := by
    calc
      4*v*d*X ≤ 4*(2*X)*X*X := by gcongr
      _ = _ := by ring
  have last : 2*v*X^2 ≤ 8*X^3 := by
    calc
      2*v*X^2 ≤ 2*(2*X)*X^2 := by gcongr
      _ ≤ _ := by nlinarith [pow_nonneg pos 3]
  nlinarith only [mul_le_mul_of_nonneg_right first (add_nonneg hp hq),
    mul_le_mul_of_nonneg_right mid hm, mul_le_mul_of_nonneg_right last hz]

/-- Taking the normalized mean preserves a bound valid for each translated table. -/
theorem translateMean {ι : Type*} (s : Finset ι) (hs : s.Nonempty)
    (g : ι → ℝ) (E : ℝ) (h : ∀ i ∈ s, g i ≤ E) :
    (∑ i ∈ s, g i) / (s.card : ℝ) ≤ E := by
  have pos : 0 < (s.card : ℝ) := by exact_mod_cast hs.card_pos
  apply (div_le_iff₀ pos).mpr
  simpa [mul_comm] using Finset.sum_le_sum h

end Riemann.PrimeInequality

#print axioms Riemann.PrimeInequality.normalizeBracket
#print axioms Riemann.PrimeInequality.fourCosts
#print axioms Riemann.PrimeInequality.translateMean
