import PositiveTime
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

open Filter MeasureTheory Set
open scoped Topology ENNReal

namespace Millennium.YangMills.D4

/-- Spectral weight of the positive-time difference (I - exp(-sH))v. -/
noncomputable def differenceWeight (s E : ℝ) : ℝ≥0∞ :=
  ENNReal.ofReal ((1 - Real.exp (-E*s))^2)

noncomputable def differenceMeasure (μ : Measure ℝ) (s : ℝ) : Measure ℝ :=
  μ.withDensity (differenceWeight s)

private theorem measurableWeight (s : ℝ) : Measurable (differenceWeight s) := by
  unfold differenceWeight
  fun_prop

private theorem realWeight (s E : ℝ) :
    (differenceWeight s E).toReal = (1 - Real.exp (-E*s))^2 :=
  ENNReal.toReal_ofReal (sq_nonneg _)

/-- At every fixed positive difference time, all nonzero energies retain
positive weight. The underlying measure may have an arbitrary zero-energy atom. -/
theorem differenceNullSets (μ : Measure ℝ) {s : ℝ} (hs : 0 < s) (A : Set ℝ) :
    differenceMeasure μ s A = 0 ↔ μ (A \ {0}) = 0 := by
  unfold differenceMeasure
  rw [withDensity_apply_eq_zero' (measurableWeight s).aemeasurable]
  have zero (E : ℝ) : differenceWeight s E = 0 ↔ E = 0 := by
    rw [differenceWeight, ENNReal.ofReal_eq_zero]
    constructor
    · intro h
      have he : 1 - Real.exp (-E*s) = 0 := by nlinarith [sq_nonneg (1 - Real.exp (-E*s))]
      have hx : Real.exp (-E*s) = Real.exp 0 := by rw [Real.exp_zero]; linarith
      have hp := Real.exp_injective hx
      exact neg_eq_zero.mp ((mul_eq_zero.mp hp).resolve_right hs.ne')
    · rintro rfl
      simp
  have eq : {E | differenceWeight s E ≠ 0} ∩ A = A \ {0} := by
    ext E
    simp only [mem_inter_iff, mem_setOf_eq, mem_diff, mem_singleton_iff, ne_eq, zero]
    exact and_comm
  rw [eq]

private theorem pointDifference (s t E : ℝ) :
    (differenceWeight s E).toReal * Real.exp (-E*t) =
    Real.exp (-E*t) - 2 * Real.exp (-E*(t+s)) + Real.exp (-E*(t+2*s)) := by
  rw [realWeight, mul_add, Real.exp_add, mul_add, Real.exp_add, show -E*(2*s) = -E*s + -E*s by ring,
    Real.exp_add]
  ring

/-- The forward second difference is a positive-measure Laplace correlation.
All integrability follows from the three observed clock readings. -/
theorem differenceCorrelation (μ : Measure ℝ) (s t : ℝ)
    (i₀ : Integrable (fun E : ℝ => Real.exp (-E*t)) μ)
    (i₁ : Integrable (fun E : ℝ => Real.exp (-E*(t+s))) μ)
    (i₂ : Integrable (fun E : ℝ => Real.exp (-E*(t+2*s))) μ) :
    Integrable (fun E : ℝ => Real.exp (-E*t)) (differenceMeasure μ s) ∧
    laplace (differenceMeasure μ s) t =
      laplace μ t - 2*laplace μ (t+s) + laplace μ (t+2*s) := by
  have finite : ∀ᵐ E ∂μ, differenceWeight s E < ⊤ :=
    ae_of_all _ fun _ => ENNReal.ofReal_lt_top
  have scaled := i₁.const_mul (2:ℝ)
  constructor
  · unfold differenceMeasure
    rw [integrable_withDensity_iff_integrable_smul₀' (measurableWeight s).aemeasurable finite]
    simpa only [smul_eq_mul, pointDifference, Pi.add_apply, Pi.sub_apply] using
      (i₀.sub scaled).add i₂
  · unfold laplace differenceMeasure
    rw [integral_withDensity_eq_integral_toReal_smul (measurableWeight s) finite]
    simp only [smul_eq_mul, pointDifference]
    have split := integral_add (i₀.sub scaled) i₂
    simp only [Pi.sub_apply] at split
    rw [split, integral_sub i₀ scaled, integral_const_mul]

/-- A cofinal scalar bound on the measured differences excludes exactly the
strict positive interval below m. Zero-energy states have arbitrary multiplicity. -/
theorem positiveGapAboveKernel (μ : Measure ℝ) {s m M : ℝ} (hs : 0 < s)
    (T : ℕ → ℝ) (late : Tendsto T atTop atTop) (clock : ∀ k, 0 ≤ T k)
    (i₀ : ∀ k, Integrable (fun E : ℝ => Real.exp (-E*T k)) μ)
    (i₁ : ∀ k, Integrable (fun E : ℝ => Real.exp (-E*(T k+s))) μ)
    (i₂ : ∀ k, Integrable (fun E : ℝ => Real.exp (-E*(T k+2*s))) μ)
    (bound : ∀ᶠ k in atTop,
      laplace μ (T k) - 2*laplace μ (T k+s) + laplace μ (T k+2*s) ≤ M*Real.exp (-m*T k)) :
    μ (Ioo 0 m) = 0 := by
  have facts (k : ℕ) := differenceCorrelation μ s (T k) (i₀ k) (i₁ k) (i₂ k)
  have null := energySupportOfEnvelope (differenceMeasure μ s) T late clock (fun k => (facts k).1)
    (bound.mono fun k hk => (facts k).2.le.trans hk)
  apply measure_mono_null _ ((differenceNullSets μ hs (Iio m)).mp null)
  intro E hE
  exact ⟨hE.2, ne_of_gt hE.1⟩

/-- A shrinking filter can make a gap-one point mass pass a rate-three
late bound. Take the difference time s = exp(-T) at sampled time T. -/
theorem shrinkingFilter (T : ℝ) :
    (1-Real.exp (-(Real.exp (-T))))^2 * Real.exp (-T) ≤ Real.exp (-3*T) := by
  let s := Real.exp (-T)
  have hs : 0 ≤ s := (Real.exp_pos _).le
  have lo : 0 ≤ 1 - Real.exp (-s) := sub_nonneg.mpr (Real.exp_le_one_iff.mpr (neg_nonpos.mpr hs))
  have hi : 1 - Real.exp (-s) ≤ s := by linarith only [Real.add_one_le_exp (-s)]
  have hsq := mul_self_le_mul_self lo hi
  have eq : Real.exp (-3*T) = Real.exp (-T) * Real.exp (-T) * Real.exp (-T) := by
    rw [← Real.exp_add, ← Real.exp_add]
    congr 1
    ring
  rw [eq, pow_two]
  exact mul_le_mul_of_nonneg_right hsq hs

-- BEGIN PCP OS generated time-difference control
noncomputable def differenceShape (q : ℝ) : ℝ := 1 - 2*q + 1*q^2

/-- The native coefficients preserve positivity and annul only q=1. -/
theorem differenceShapeControl (q : ℝ) :
    differenceShape q = (1-q)^2 ∧ (differenceShape q = 0 ↔ q = 1) := by
  have h : differenceShape q = (1-q)^2 := by unfold differenceShape; ring
  constructor
  · exact h
  · rw [h, sq_eq_zero_iff, sub_eq_zero, eq_comm]

#print axioms differenceNullSets
#print axioms differenceCorrelation
#print axioms positiveGapAboveKernel
#print axioms shrinkingFilter
#print axioms differenceShapeControl

end Millennium.YangMills.D4
