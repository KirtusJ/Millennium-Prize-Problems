import Mathlib.Tactic.LinearCombination
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

open Finset
namespace YangMills.OddClover

/-- A common Fourier covector kills the complementary-face pairing even
when the two vector potentials differ. -/
theorem commonCovector {R : Type*} [CommRing R]
    (p q r s a b c d u v w z : R) :
    (p*b-q*a)*(r*z-s*w) - (p*c-r*a)*(q*z-s*v) +
    (p*d-s*a)*(q*w-r*v) + (r*d-s*c)*(p*v-q*u) -
    (q*d-s*b)*(p*w-r*u) + (q*c-r*b)*(p*z-s*u) = 0 := by ring

/-- Four oriented faces supply one centered difference in a fixed axis
after multiplication by its symmetric averaging factor. -/
theorem centeredSymbol {R : Type*} [CommRing R] (x y : R) (h : x*y=1) :
    (1+y)*(x-1) = x-y := by linear_combination h

/-- Only diagonal variances remain in the upper bound after reflection
has made the mean cross products nonpositive. -/
theorem tileBound {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (K : ι → ι → ℝ) (D : ℝ) (diag : ∀ i ∈ s, K i i ≤ D)
    (off : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → K i j ≤ 0) :
    (∑ i ∈ s, ∑ j ∈ s, K i j) ≤ (s.card:ℝ)*D := by
  calc
    _ ≤ ∑ i ∈ s, ∑ j ∈ s, (if j=i then D else 0) := by
      apply sum_le_sum
      intro i hi
      apply sum_le_sum
      intro j hj
      by_cases eq : j=i
      · subst j
        simpa using diag i hi
      · simpa [eq] using off i hi j hj (Ne.symm eq)
    _ = _ := by simp

/-- The midpoint between copies of a tile of width 2h is a site plane. -/
theorem tileReflection (a h i j : ℤ) :
    2*(a+(i+j+1)*h)-(a+2*i*h) = a+2*(j+1)*h ∧
    2*(a+(i+j+1)*h)-(a+2*(i+1)*h) = a+2*j*h := by
  constructor <;> ring

/-- Covariance cancellation leaves the boundary terms in the free box. -/
theorem removeVolume {ι : Type*} (u : Finset ι) (C overlap : ι → ℝ)
    (volume : ℝ) (cancel : ∑ z ∈ u, C z = 0) :
    ∑ z ∈ u, overlap z*C z = ∑ z ∈ u, (overlap z-volume)*C z := by
  simp only [sub_mul, sum_sub_distrib, ← mul_sum, cancel, mul_zero, sub_zero]

/-- At h = beta^(1/40) the surface term per unit volume and the
accumulated pointwise error have the same power. -/
theorem susceptibilityBudget (h : ℝ) (hh : 0 < h) :
    h^3/h^4 + h^4/h^5 = 2/h := by
  field_simp
  ring

/-- A local density rescaling by 1/beta rescales the variance by its square. -/
theorem rawScale (t : ℝ) (ht : 0 < t) : (1/t)/(t^40)^2 = 1/t^81 := by
  field_simp
  ring

/-- A centered cube test with squared norm 1/27 converts a
correlation into a conditional variance bound. -/
theorem cubeTest (v t : ℝ) (cs : t^2 ≤ v*(1/27)) : 27*t^2 ≤ v := by
  linarith

end YangMills.OddClover
#print axioms YangMills.OddClover.commonCovector
#print axioms YangMills.OddClover.centeredSymbol
#print axioms YangMills.OddClover.tileBound
#print axioms YangMills.OddClover.tileReflection
#print axioms YangMills.OddClover.removeVolume
#print axioms YangMills.OddClover.susceptibilityBudget
#print axioms YangMills.OddClover.rawScale
#print axioms YangMills.OddClover.cubeTest
