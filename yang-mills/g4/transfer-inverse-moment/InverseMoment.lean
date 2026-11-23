import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

open MeasureTheory Set
open scoped BigOperators

namespace Millennium.G4.InverseMoment

/-- The exterior kernel and both vacuum boundary amplitudes are nonnegative.
The interior Gram kernel itself may have either sign. -/
theorem positive_exterior {I : Type*} [Fintype I] (w gram : I → I → ℝ) (H : ℝ)
    (hw : ∀ i j, 0 ≤ w i j) (hg : ∀ i j, gram i j ≤ H) :
    (∑ i, ∑ j, w i j * gram i j) ≤ H * ∑ i, ∑ j, w i j := by
  simp only [Finset.mul_sum]
  exact Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => by
    simpa [mul_comm] using mul_le_mul_of_nonneg_left (hg i j) (hw i j)

/-- Cancel the same exterior factor using the lower bound on the denominator. -/
theorem volume_cancellation (numer den ext H k : ℝ) (hd : 0 < den) (hk : 0 < k)
    (hH : 0 ≤ H) (num_bound : numer ≤ H * ext) (den_bound : k * ext ≤ den) :
    numer/den ≤ H/k := by
  apply (div_le_div_iff₀ hd hk).mpr
  nlinarith [mul_le_mul_of_nonneg_right num_bound hk.le,
    mul_le_mul_of_nonneg_left den_bound hH]

-- NATIVE CHILD 1
/-- A positive transfer spectrum on the measured space converts an inverse
first moment into a bound on the weight at small transfer eigenvalues. -/
theorem inverse_tail {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (x : X → ℝ) (A : Set X) (hA : MeasurableSet A) (s : ℝ) (hs : 0 < s)
    (nonneg : ∀ z, 0 ≤ x z) (positive : ∀ z ∈ A, 0 < x z)
    (cutoff : ∀ z ∈ A, x z ≤ s) (hi : Integrable (fun z => (x z)⁻¹) μ) :
    μ.real A ≤ s * ∫ z, (x z)⁻¹ ∂μ := by
  have point (z) (hz : z ∈ A) : 1/s ≤ (x z)⁻¹ := by
    simpa [one_div] using one_div_le_one_div_of_le (positive z hz) (cutoff z hz)
  have loc := setIntegral_ge_of_const_le hA (measure_ne_top μ A) point hi.integrableOn
  have glob := setIntegral_le_integral (s := A) hi
    (Filter.Eventually.of_forall fun z => inv_nonneg.mpr (nonneg z))
  calc
    μ.real A = s * (1/s * μ.real A) := by field_simp
    _ ≤ s * ∫ z, (x z)⁻¹ ∂μ := mul_le_mul_of_nonneg_left (loc.trans glob) hs.le

/-- Centering and projection can add at most one approximation error in norm. -/
theorem approximate_tail (v p eps h : ℝ) (hv : 0 ≤ v) (hh : 0 ≤ h)
    (tri : v ≤ eps+p) (approx : eps ≤ h/4) (poly : p ≤ h/4) :
    v^2 ≤ h^2/4 := by
  have bound : v ≤ h/2 := by linarith only [tri, approx, poly]
  nlinarith [pow_le_pow_left₀ hv bound 2]

-- NATIVE CHILD 2
lemma retained_mass (loss low high inside rho : ℝ)
    (hl : rho ≤ loss) (hs : loss ≤ low + inside + high)
    (hlo : low ≤ rho / 4) (hhi : high ≤ rho / 4) :
    rho / 2 ≤ inside := by
  linarith

/-- Residual after substituting the lower bound for the tilted axial mean in
the linear ODE for its derivative. -/
theorem radial_residual (k : ℝ) (hk : 0 < k) :
    (k/(k+4))*(3/k^2-3/(k+4)^2)-9/(2*k*(k+4)^2)+3/(k+4)^3 =
    (45*k+60)/(2*k*(k+4)^3) := by
  have hd : k+4 ≠ 0 := by linarith
  field_simp [ne_of_gt hk,hd]
  <;> ring

theorem beta_one_constants : 4 * (8:ℚ)^8 * 4^4 = 2^34 ∧
    (2:ℚ)^34/2^43 < 3/800 ∧ (1/20+1/32 : ℚ)^2 < 3/400 := by norm_num

#print axioms positive_exterior
#print axioms volume_cancellation
#print axioms inverse_tail
#print axioms approximate_tail
#print axioms retained_mass
#print axioms radial_residual
#print axioms beta_one_constants

end Millennium.G4.InverseMoment
