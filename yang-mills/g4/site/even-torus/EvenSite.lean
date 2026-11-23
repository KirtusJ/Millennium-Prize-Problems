import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

noncomputable section
open MeasureTheory
open scoped ComplexConjugate

namespace Millennium.G4.EvenSite

/-- Positive normal links are based on the layer before the directed step. -/
theorem normal_half_flip (m t : ℕ) (ht : t < 2*m) : (2*m-1-t < m ↔ m ≤ t) := by omega

/-- Interior tangent layers are exchanged, and the two fixed layers stay put. -/
def reflectedLayer (m t : ℕ) := if t = 0 then 0 else 2*m-t

theorem tangent_layers (m t : ℕ) (hm : 0 < m) (ht : t < 2*m) :
    (reflectedLayer m t = t ↔ t = 0 ∨ t = m) ∧
    (0 < t ∧ t < m ↔ m < reflectedLayer m t) := by
  unfold reflectedLayer
  split <;> omega

/-- The two endpoints of every positive normal edge lie in its closed half,
including the wrap from the last layer back to zero. -/
theorem normal_endpoints (m t : ℕ) (h : t < 2*m) :
    (t < m → t + 1 ≤ m) ∧
    (m ≤ t → (if t + 1 = 2*m then 0 else t+1) = 0 ∨
      (m ≤ (if t + 1 = 2*m then 0 else t+1) ∧ t+1 < 2*m)) := by
  constructor
  · omega
  · intro ht
    split <;> omega

-- NATIVE CHILD 1
variable {X Y : Type*} [MeasurableSpace X] [MeasurableSpace Y]

/-- The two half-actions are absorbed into f. The boundary-only action and
partition normalization are in w. This theorem calculates the original product
integral of the split variables without assuming conditional positivity. -/
def siteIntegrand (w : Y → ℝ) (f : Y → X → ℂ) (v : Y × (X × X)) : ℂ :=
  (w v.1 : ℂ) * (conj (f v.1 v.2.1) * f v.1 v.2.2)

theorem site_pair_formula (η : Measure Y) (μ : Measure X) [IsProbabilityMeasure η]
    [IsProbabilityMeasure μ] (w : Y → ℝ) (f : Y → X → ℂ)
    (hi : Integrable (siteIntegrand w f) (η.prod (μ.prod μ))) :
    (∫ v, siteIntegrand w f v ∂η.prod (μ.prod μ)) =
      ((∫ y, w y * Complex.normSq (∫ x, f y x ∂μ) ∂η : ℝ) : ℂ) := by
  rw [integral_prod _ hi, ← integral_complex_ofReal]
  apply integral_congr_ae
  apply Filter.Eventually.of_forall
  intro y
  unfold siteIntegrand
  simp only [integral_const_mul, integral_prod_mul (fun x => conj (f y x)) (f y),
    integral_conj, Complex.ofReal_mul, Complex.normSq_eq_conj_mul_self]

theorem site_reflection_positive (η : Measure Y) (μ : Measure X) [IsProbabilityMeasure η]
    [IsProbabilityMeasure μ] (w : Y → ℝ) (f : Y → X → ℂ) (hw : ∀ y, 0 ≤ w y)
    (hi : Integrable (siteIntegrand w f) (η.prod (μ.prod μ))) :
    (∫ v, siteIntegrand w f v ∂η.prod (μ.prod μ)).im = 0 ∧
      0 ≤ (∫ v, siteIntegrand w f v ∂η.prod (μ.prod μ)).re := by
  rw [site_pair_formula η μ w f hi]
  refine ⟨rfl, ?_⟩
  exact integral_nonneg (fun y => mul_nonneg (hw y) (Complex.normSq_nonneg _))

-- NATIVE CHILD 2
theorem face_softening (copies energy : ℝ) (hn : copies ≤ 4) (he : 0 ≤ energy) :
    copies*energy/8 ≤ energy/2 := by
  nlinarith only [mul_le_mul_of_nonneg_right hn he]

theorem dyadic_fraction (k L : ℕ) (hk : L < 2*k) : L^4 < 16*k^4 := by
  have h := Nat.pow_lt_pow_left hk (by decide : 4 ≠ 0)
  simpa [mul_pow] using h

/-- Gaussian square, linear shift and random-constant covariance weights at
lag zero are A, B and C. Their lag multipliers are r², r and 1. -/
theorem covariance_mixture (r A B C : ℝ) (hr : 0 ≤ r) (h1 : r ≤ 1)
    (hB : 0 ≤ B) (hC : 0 ≤ C) :
    r^2*(A+B+C) ≤ r^2*A+r*B+C := by
  have hsq : r^2 ≤ r := by nlinarith [mul_nonneg hr (sub_nonneg.mpr h1)]
  nlinarith only [mul_nonneg (sub_nonneg.mpr hsq) hB,
    mul_nonneg (sub_nonneg.mpr (hsq.trans h1)) hC]

#print axioms normal_half_flip
#print axioms tangent_layers
#print axioms normal_endpoints
#print axioms site_pair_formula
#print axioms site_reflection_positive
#print axioms face_softening
#print axioms dyadic_fraction
#print axioms covariance_mixture

end Millennium.G4.EvenSite
