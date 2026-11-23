import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
open MeasureTheory Filter
namespace YangMills.HamiltonianVariance

theorem linkReplacement {K κ frozen original : ℝ} (hκ : 0 < κ)
    (trial : κ*K + original ≤ frozen) : K ≤ (frozen-original)/κ := by
  exact (le_div_iff₀ hκ).mpr (by linarith only [trial])

/-- Square of the upper bound on interval probability at the chosen half-width. -/
theorem intervalChoice {z : ℝ} (hz : 0 < z) :
    2*Real.pi^2*z*(1/(8*Real.pi^2*z)) = (1/2 : ℝ)^2 := by
  field_simp [Real.pi_ne_zero, hz.ne']
  ring

theorem varianceFloor {v u p : ℝ} (prob : p ≤ 1/2) (sq : u^2*(1-p) ≤ v) :
    u^2/2 ≤ v := by
  linarith only [mul_le_mul_of_nonneg_left prob (sq_nonneg u), sq]

theorem trialKinetic (m : ℝ) (hm : 0 ≤ m) :
    3*m^2/(4*(4*m+1)) ≤ 3*m/16 := by
  apply (div_le_iff₀ (by linarith : 0 < 4*(4*m+1))).mpr
  linarith only [hm]

theorem fourLinks {r : ℝ} (hr : 0 ≤ r) :
    1-r^4 ≤ 4*(1-r) := by
  have id : 4*(1-r)-(1-r^4) = (1-r)^2*(r^2+2*r+3) := by ring
  have hp : 0 ≤ r^2+2*r+3 := by linarith [sq_nonneg r]
  linarith only [id,mul_nonneg (sq_nonneg (1-r)) hp]

theorem optimizedTrial {g m x : ℝ} (pos : 0 < m) (hx : 0 ≤ x) (root : g=x^2)
    (lo : 6*x ≤ m) (hi : m ≤ 6*x+1) :
    3*m/16+6*g/m ≤ 17*x/8+3/16 := by
  have h : 6*g/m ≤ x := (div_le_iff₀ pos).mpr
    (by linarith only [root, mul_le_mul_of_nonneg_left lo hx])
  linarith only [hi,h]

theorem covarianceToEnergy {M u κ : ℝ} (hκ : 0 ≤ κ) (second mean : ℝ)
    (identity : M = 4*κ*(1-second)) (loss : u=1-mean)
    (square : 0 ≤ 1-2*mean+second) : M ≤ 8*κ*u := by
  rw [identity,loss]
  linarith only [mul_nonneg hκ square]

/-- Lift the escape probability to the second moment of the trace law. -/
theorem escapeToVariance (μ : Measure ℝ) [IsFiniteMeasure μ] (m u : ℝ) (hu : 0 ≤ u)
    (h : 1/2 ≤ μ.real {x | u ≤ |x-m|})
    (hi : Integrable (fun x : ℝ => (x-m)^2) μ) :
    u^2/2 ≤ ∫ x, (x-m)^2 ∂μ := by
  let s : Set ℝ := {x | u ≤ |x-m|}
  have hs : MeasurableSet s := measurableSet_le measurable_const
    ((continuous_id.sub continuous_const).abs.measurable)
  have H := setIntegral_ge_of_const_le (μ := μ) (c := u^2) hs (measure_ne_top μ s)
    (f := fun x : ℝ => (x-m)^2) (fun x hx => by
      have hx' : u ≤ |x-m| := hx
      simpa only [← sq, sq_abs] using mul_self_le_mul_self hu hx') hi.integrableOn
  have upper := setIntegral_le_integral (s := s) hi
    (Eventually.of_forall fun x => sq_nonneg (x-m))
  have ht : (1/2 : ℝ) ≤ μ.real s := h
  linarith only [mul_le_mul_of_nonneg_left ht (sq_nonneg u), H, upper]

/-- Jensen's exponential tangent for an arbitrary normalized spectral law. -/
theorem normalizedSpectralWitness (μ : Measure ℝ) [IsProbabilityMeasure μ]
    {t M : ℝ} (ht : 0 ≤ t) (hi : Integrable (fun x : ℝ => x) μ)
    (he : Integrable (fun x : ℝ => Real.exp (-t*x)) μ)
    (hm : (∫ x, x ∂μ) ≤ M) :
    Real.exp (-t*M) ≤ ∫ x, Real.exp (-t*x) ∂μ := by
  let b := Real.exp (-t*M)
  have hb : 0 ≤ b := (Real.exp_pos _).le
  have tangent (x : ℝ) : b*(1+t*M-t*x) ≤ Real.exp (-t*x) := by
    have h := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (t*M-t*x)) hb
    change Real.exp (-t*M)*(1+t*M-t*x) ≤ Real.exp (-t*x)
    calc
      _ ≤ Real.exp (-t*M)*Real.exp (t*M-t*x) := by dsimp [b] at h; linarith only [h]
      _ = _ := by rw [← Real.exp_add]; congr 1; ring
  have hir : Integrable (fun x : ℝ => 1+t*M-t*x) μ :=
    (integrable_const _).sub (hi.const_mul t)
  have h := integral_mono (hir.const_mul b) he tangent
  rw [integral_const_mul, integral_sub (integrable_const _) (hi.const_mul t),
      integral_const_mul, integral_const, measureReal_univ_eq_one, one_smul] at h
  have h' : (1:ℝ) ≤ 1+t*M-t*(∫ x, x ∂μ) := by
    linarith only [mul_le_mul_of_nonneg_left hm ht]
  exact (by simpa only [mul_one] using mul_le_mul_of_nonneg_left h' hb : b ≤ _).trans h

end YangMills.HamiltonianVariance
#print axioms YangMills.HamiltonianVariance.linkReplacement
#print axioms YangMills.HamiltonianVariance.intervalChoice
#print axioms YangMills.HamiltonianVariance.varianceFloor
#print axioms YangMills.HamiltonianVariance.trialKinetic
#print axioms YangMills.HamiltonianVariance.fourLinks
#print axioms YangMills.HamiltonianVariance.optimizedTrial
#print axioms YangMills.HamiltonianVariance.covarianceToEnergy
#print axioms YangMills.HamiltonianVariance.escapeToVariance
#print axioms YangMills.HamiltonianVariance.normalizedSpectralWitness
