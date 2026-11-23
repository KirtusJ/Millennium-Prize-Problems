import Mathlib.Analysis.SpecialFunctions.Trigonometric.InverseDeriv
import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

open Real Set MeasureTheory
open scoped Topology

namespace YangMills.StarReconstruction

/-- The product of two Abel kernels, extended by zero off the interval. -/
noncomputable def kernel (a t b : ℝ) : ℝ :=
  (Real.sqrt (t-a)*Real.sqrt (b-t))⁻¹

theorem kernelPrimitive {a b : ℝ} (hab : a < b) {x : ℝ} (hx : x ∈ Ioo a b) :
    HasDerivAt (fun t => Real.arcsin ((2*t-a-b)/(b-a))) (kernel a x b) x := by
  have hd : 0 < b-a := sub_pos.mpr hab
  set q := (2*x-a-b)/(b-a)
  have ql : -1 < q := (lt_div_iff₀ hd).mpr (by linarith [hx.1])
  have qr : q < 1 := (div_lt_iff₀ hd).mpr (by linarith [hx.2])
  have hn : 0 < 1-q^2 := by nlinarith [mul_pos (sub_pos.mpr qr) (by linarith : 0 < 1+q)]
  have e : 1-q^2=4*(x-a)*(b-x)/(b-a)^2 := by dsimp [q]; field_simp; ring
  have xa := sub_pos.mpr hx.1
  have bx := sub_pos.mpr hx.2
  have hfour : Real.sqrt 4 = 2 := by nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 4), Real.sqrt_nonneg (4:ℝ)]
  have hrad : Real.sqrt (1-q^2)*(b-a)=2*Real.sqrt (x-a)*Real.sqrt (b-x) := by
    rw [e, Real.sqrt_div (by positivity), Real.sqrt_sq hd.le,
        Real.sqrt_mul (by positivity), Real.sqrt_mul (by norm_num)]
    rw [hfour]
    field_simp
  have der := (Real.hasDerivAt_arcsin (ne_of_gt ql) (ne_of_lt qr)).comp x
    (((((hasDerivAt_id x).const_mul 2).sub_const a).sub_const b).div_const (b-a))
  convert der using 1
  dsimp [kernel]
  field_simp [ne_of_gt hd, ne_of_gt (Real.sqrt_pos.2 hn),
    ne_of_gt (Real.sqrt_pos.2 (sub_pos.mpr hx.1)), ne_of_gt (Real.sqrt_pos.2 (sub_pos.mpr hx.2))]
  linarith

theorem betaIntegral {a b : ℝ} (hab : a < b) : (∫ t, kernel a t b) = Real.pi := by
  let f := fun t => Real.arcsin ((2*t-a-b)/(b-a))
  have hc : Continuous f := by dsimp [f]; fun_prop
  have hpos : ∀ t ∈ Ioo a b, 0 ≤ kernel a t b := by intro t _; unfold kernel; positivity
  have hi := intervalIntegral.integrableOn_deriv_of_nonneg hc.continuousOn
    (fun x hx => kernelPrimitive hab hx) hpos
  have hint : IntervalIntegrable (fun t => kernel a t b) volume a b :=
    (intervalIntegrable_iff_integrableOn_Ioc_of_le hab.le).2 hi
  have hv := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le hab.le hc.continuousOn
    (fun x hx => kernelPrimitive hab hx) hint
  have hl : (2*a-a-b)/(b-a) = -1 := (div_eq_iff (ne_of_gt (sub_pos.mpr hab))).2 (by ring)
  have hr : (2*b-a-b)/(b-a) = 1 := (div_eq_iff (ne_of_gt (sub_pos.mpr hab))).2 (by ring)
  have hs : ∀ t, t ∉ Ioc a b → kernel a t b = 0 := by
    intro t h
    by_cases ha : a < t
    · have hbt : b ≤ t := le_of_not_ge (fun htb => h ⟨ha,htb⟩)
      simp [kernel, Real.sqrt_eq_zero_of_nonpos (sub_nonpos.mpr hbt)]
    · simp [kernel, Real.sqrt_eq_zero_of_nonpos (sub_nonpos.mpr (le_of_not_gt ha))]
  rw [← setIntegral_eq_integral_of_forall_compl_eq_zero hs,
    ← intervalIntegral.integral_of_le hab.le, hv]
  dsimp [f]
  rw [hl, hr, Real.arcsin_one, Real.arcsin_neg_one]
  ring

theorem kernelIntegrable {a b : ℝ} (hab : a < b) :
    Integrable (fun t => kernel a t b) := by
  by_contra hf
  have h := betaIntegral hab
  rw [integral_undef hf] at h
  exact Real.pi_pos.ne h

theorem integrablePair {a b : ℝ} {g : ℝ → ℝ} (hm : Measurable g)
    (hg : IntegrableOn g (Ioo a b)) :
    Integrable (fun p : ℝ × ℝ => g p.1 * kernel p.1 p.2 b)
      ((volume.restrict (Ioo a b)).prod volume) := by
  have hm₂ : Measurable (fun p : ℝ × ℝ => g p.1 * kernel p.1 p.2 b) := by
    unfold kernel
    fun_prop
  apply (integrable_prod_iff hm₂.aestronglyMeasurable).2
  constructor
  · filter_upwards [ae_restrict_mem (μ := volume) measurableSet_Ioo] with s hs
    exact (kernelIntegrable hs.2).const_mul (g s)
  · apply (hg.norm.mul_const Real.pi).congr
    filter_upwards [ae_restrict_mem (μ := volume) measurableSet_Ioo] with s hs
    change ‖g s‖ * Real.pi = ∫ t, ‖g s * kernel s t b‖
    have hnn (t : ℝ) : 0 ≤ kernel s t b := by unfold kernel; positivity
    simp_rw [norm_mul, Real.norm_of_nonneg (hnn _)]
    rw [integral_const_mul, betaIntegral hs.2]

/-- Composition inside a double integral, with the product integrability
hypothesis visible to the caller. -/
theorem abelTwice {a b : ℝ} (g : ℝ → ℝ)
    (hi : Integrable (fun p : ℝ × ℝ => g p.1 * kernel p.1 p.2 b)
      ((volume.restrict (Ioo a b)).prod volume)) :
    (∫ t, ∫ s in Ioo a b, g s * kernel s t b) = (∫ s in Ioo a b, g s)*Real.pi := by
  rw [← integral_integral_swap (f := fun s t => g s * kernel s t b) hi]
  rw [← integral_mul_const]
  apply integral_congr_ae
  filter_upwards [ae_restrict_mem (μ := volume) measurableSet_Ioo] with s hs
  rw [integral_const_mul, betaIntegral hs.2]

theorem reconstructDerivative {v : ℝ} (hv : 0 < v) (c : ℝ) (g : ℝ → ℝ)
    (hm : Measurable g) (hg : IntegrableOn g (Ioo 0 v)) :
    (∫ t, c*kernel 0 t v + ∫ s in Ioo 0 v, g s*kernel s t v) =
      Real.pi*(c+∫ s in Ioo 0 v, g s) := by
  have h := integrablePair hm hg
  rw [integral_add ((kernelIntegrable hv).const_mul c) h.integral_prod_right, integral_const_mul, betaIntegral hv, abelTwice g h]
  ring

/-- Substituting the Abel inverse into the differentiated forward equation
returns the actual derivative data, including the endpoint term. -/
theorem inverseForward {v : ℝ} (hv : 0 < v) (F g : ℝ → ℝ) (hg : Continuous g)
    (hf : ∀ x ∈ Set.uIcc 0 v, HasDerivAt F (g x) x) :
    (∫ t, F 0*kernel 0 t v + ∫ s in Ioo 0 v, g s*kernel s t v) = Real.pi*F v := by
  have hint := hg.intervalIntegrable (μ := volume) 0 v
  have ih := (intervalIntegrable_iff_integrableOn_Ioc_of_le hv.le).1 hint
  have val := intervalIntegral.integral_eq_sub_of_hasDerivAt hf hint
  rw [intervalIntegral.integral_of_le hv.le, integral_Ioc_eq_integral_Ioo] at val
  rw [reconstructDerivative hv _ _ hg.measurable (ih.mono_set Ioo_subset_Ioc_self), val]
  ring

/-- Exact excess squared error for any two sign readings with a prescribed
weighted mean. The probability of the sign may depend on the known magnitude. -/
theorem signLoss (p u d t : ℝ) :
    let m := p*u+(1-p)*d
    p*(u-t)^2+(1-p)*(d-t)^2=(m-t)^2+p*(1-p)*(u-d)^2 := by dsimp; ring

theorem integratedMinimum {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    (p u d t : Ω → ℝ) (hp : ∀ᵐ x ∂μ, 0 ≤ p x ∧ p x ≤ 1)
    (i₁ : Integrable (fun x => (p x*u x+(1-p x)*d x-t x)^2) μ)
    (i₂ : Integrable (fun x => p x*(u x-t x)^2+(1-p x)*(d x-t x)^2) μ) :
    (∫ x, (p x*u x+(1-p x)*d x-t x)^2 ∂μ) ≤
      ∫ x, p x*(u x-t x)^2+(1-p x)*(d x-t x)^2 ∂μ := by
  apply integral_mono_ae i₁ i₂
  filter_upwards [hp] with x hx
  rw [signLoss]
  exact le_add_of_nonneg_right (mul_nonneg (mul_nonneg hx.1 (sub_nonneg.mpr hx.2)) (sq_nonneg _))

theorem rawReciprocal (β S : ℝ) (h : 6*β-S ≠ 0) :
    β^2/(6*β-S)-β/6-S/36=S^2/(36*(6*β-S)) := by field_simp; ring

theorem inverseCoefficients (c₁ c₂ : ℝ) (h₁ : c₁ = -3/4)
    (h₂ : c₂+3*c₁/2 = -9/8) : c₂=0 := by linarith

theorem irreducibleVariance : (3/2:ℝ)/48^2=1/1536 := by norm_num

end YangMills.StarReconstruction
#print axioms YangMills.StarReconstruction.kernelPrimitive
#print axioms YangMills.StarReconstruction.betaIntegral
#print axioms YangMills.StarReconstruction.kernelIntegrable
#print axioms YangMills.StarReconstruction.integrablePair
#print axioms YangMills.StarReconstruction.abelTwice
#print axioms YangMills.StarReconstruction.reconstructDerivative
#print axioms YangMills.StarReconstruction.inverseForward
#print axioms YangMills.StarReconstruction.signLoss
#print axioms YangMills.StarReconstruction.integratedMinimum
#print axioms YangMills.StarReconstruction.rawReciprocal
#print axioms YangMills.StarReconstruction.inverseCoefficients
#print axioms YangMills.StarReconstruction.irreducibleVariance
