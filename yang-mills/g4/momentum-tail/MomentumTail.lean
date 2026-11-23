import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

noncomputable section
open MeasureTheory
namespace Millennium.G4.MomentumTail

open scoped BigOperators

theorem fejer_polynomial_transfer {I : Type*} [Fintype I]
    (a f g : I → ℝ) (e c : ℝ) (he : 0 ≤ e)
    (h : ∀ i, |f i - g i| ≤ e) (hnorm : (∑ i, |a i|) ≤ c) :
    |(∑ i, a i * f i) - (∑ i, a i * g i)| ≤ c * e := by
  rw [← Finset.sum_sub_distrib]
  simp only [← mul_sub]
  calc
    |∑ i, a i * (f i - g i)| ≤ ∑ i, |a i * (f i - g i)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i, |a i| * e := by
      apply Finset.sum_le_sum
      intro i _
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_left (h i) (abs_nonneg (a i))
    _ = (∑ i, |a i|) * e := by rw [Finset.sum_mul]
    _ ≤ c * e := mul_le_mul_of_nonneg_right hnorm he

-- NATIVE CHILD 1
/-- Outside the chosen central window the fourth-power Fejér test has a floor. -/
theorem fejer_floor (y : ℝ) (hy : y ≤ 1/4) : (3/4 : ℝ)^4 ≤ (1-y)^4 := by
  exact pow_le_pow_left₀ (by norm_num) (by linarith) 4

/-- The truncated eighth moment of a normalized Pareto-six tail costs A^-6. -/
theorem pareto_eight (A : ℝ) (hA : 1 ≤ A) :
    (1+4*(A^2-1))/A^8 ≤ 4/A^6 := by
  have hne : A ≠ 0 := by linarith
  calc
    (1+4*(A^2-1))/A^8 ≤ 4*A^2/A^8 :=
      div_le_div_of_nonneg_right (by linarith) (by positivity)
    _ = 4/A^6 := by
      field_simp [hne]
      ring

-- NATIVE CHILD 2
/-- Integrate a deterministic test floor against an arbitrary finite measure. -/
theorem measure_tail (μ : Measure ℝ) [IsFiniteMeasure μ] (S : Set ℝ)
    (hs : MeasurableSet S) (k : ℝ → ℝ) (hi : Integrable k μ)
    (hk : ∀ x, S.indicator (fun _ => (3/4 : ℝ)^4) x ≤ k x) :
    μ.real S*(3/4 : ℝ)^4 ≤ ∫ x, k x ∂μ := by
  have hind : Integrable (S.indicator (fun _ => (3/4 : ℝ)^4)) μ :=
    (integrable_const _).indicator hs
  have z := integral_mono hind hi hk
  rwa [integral_indicator hs, setIntegral_const, smul_eq_mul] at z

#print axioms fejer_polynomial_transfer
#print axioms fejer_floor
#print axioms pareto_eight
#print axioms measure_tail

end Millennium.G4.MomentumTail
