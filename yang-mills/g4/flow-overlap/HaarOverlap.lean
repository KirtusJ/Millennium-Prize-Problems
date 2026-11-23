import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open MeasureTheory Set Real

namespace Millennium.G4.HaarOverlap

/-- The force cannot decay faster than its Hessian bound allows along a complete flow. -/
theorem dissipation_floor (energy slope : ℝ → ℝ)
    (hd : ∀ x, HasDerivAt energy (slope x) x)
    (lower : ∀ x, -32 * energy x ≤ slope x) (u : ℝ) (hu : 0 ≤ u) :
    energy 0 ≤ exp (32*u) * energy u := by
  have deriv (x : ℝ) : HasDerivAt (fun t : ℝ => exp (32*t)*energy t)
      (exp (32*x)*(32*energy x+slope x)) x := by
    convert (((Real.hasDerivAt_exp (32*x)).comp x
      ((hasDerivAt_id x).const_mul 32)).mul (hd x)) using 1 <;> dsimp <;> ring
  have mono := monotone_of_hasDerivAt_nonneg deriv (fun x =>
    mul_nonneg (exp_pos _).le (by linarith [lower x]))
  simpa using mono hu

/-- Residual of the subsolution k/(4+k) in the tilted S³ mean equation. -/
theorem tilt_residual (k : ℝ) (hk : 0 < k) :
    1-(k/(4+k))^2-3*(k/(4+k))/k-4/(4+k)^2 = 5*k/(4+k)^2 := by
  have den : 4+k ≠ 0 := by linarith
  field_simp [den,ne_of_gt hk]
  <;> ring

/-- An exact score overlap with bounded variance certifies mean-square prediction error. -/
theorem score_prediction (h covariance score error : ℝ) (hh : 0 ≤ h) (hv : 0 < score)
    (overlap : h/2 ≤ covariance) (schwarz : covariance^2 ≤ error*score) :
    h^2/(4*score) ≤ error := by
  apply (div_le_iff₀ (by positivity : 0 < 4*score)).mpr
  nlinarith [pow_le_pow_left₀ (show 0 ≤ h/2 by linarith) overlap 2]

-- NATIVE CHILD 1
lemma weighted_leakage (outside loss width : ℝ) (hwidth : 0 < width)
    (h : width^2 * outside ≤ loss) : outside ≤ loss / width^2 := by
  have hsq : 0 < width^2 := pow_pos hwidth 2
  apply (le_div_iff₀ hsq).2
  simpa only [mul_comm outside (width^2)] using h

/-- Transfer-weighted concentration works even when the original measure has an atom at zero. -/
theorem weighted_tail_integral {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (x : X → ℝ) (hx : ∀ z, 0 ≤ x z) (out : Set X) (ho : MeasurableSet out)
    (w : ℝ) (hw : 0 < w) (hout : ∀ z ∈ out, w ≤ |x z-1|)
    (hi : Integrable x μ) (hl : Integrable (fun z => x z*(x z-1)^2) μ) :
    ∫ z in out, x z ∂μ ≤ (∫ z, x z*(x z-1)^2 ∂μ)/w^2 := by
  apply weighted_leakage _ _ _ hw
  have localBound := setIntegral_mono_on ((hi.const_mul (w^2)).integrableOn)
    hl.integrableOn ho (fun z hz => show w^2 * x z ≤ x z * (x z-1)^2 by
      have h : w^2 ≤ (x z-1)^2 := by simpa using pow_le_pow_left₀ hw.le (hout z hz) 2
      simpa [mul_comm] using mul_le_mul_of_nonneg_left h (hx z))
  rw [integral_const_mul] at localBound
  exact localBound.trans (setIntegral_le_integral hl
    (Filter.Eventually.of_forall fun z => mul_nonneg (hx z) (sq_nonneg _)))

-- NATIVE CHILD 2
/-- Three scaled moments control the transfer-weighted squared deviation. -/
theorem three_moments (c₁ c₂ c₃ W d : ℝ) (h₁ : c₁ ≤ W+d)
    (h₂ : W-d ≤ c₂) (h₃ : c₃ ≤ W+d) :
    c₃-2*c₂+c₁ ≤ 4*d := by linarith

/-- First moment, inside mass and first moment outside a relative band. -/
theorem band_mass_error (mass inside first outside target w d : ℝ)
    (hm : inside ≤ mass) (hw : 0 ≤ w) (hd : |first-target| ≤ d)
    (ho : 0 ≤ outside) (band : |first-outside-inside| ≤ w*inside) :
    |inside-target| ≤ d + outside + w*mass := by
  rw [abs_le] at hd band ⊢
  have h := mul_le_mul_of_nonneg_left hm hw
  constructor <;> linarith [hd.1,hd.2,band.1,band.2]

/-- A projected witness cannot carry overlap exceeding its norm times the probe norm. -/
theorem projected_weight (s overlap m weight : ℝ) (hs : 0 ≤ s) (hm : 0 < m)
    (lower : s ≤ overlap) (schwarz : overlap^2 ≤ weight*m) :
    s^2/m ≤ weight := by
  apply (div_le_iff₀ hm).mpr
  exact (pow_le_pow_left₀ hs lower 2).trans schwarz

#print axioms dissipation_floor
#print axioms tilt_residual
#print axioms score_prediction
#print axioms weighted_leakage
#print axioms weighted_tail_integral
#print axioms three_moments
#print axioms band_mass_error
#print axioms projected_weight

end Millennium.G4.HaarOverlap
