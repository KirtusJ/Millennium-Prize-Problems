import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.Tactic.Linarith

open Real Set MeasureTheory
open scoped ENNReal

namespace YangMills.PositiveTimeSumRule

noncomputable def detector (u : ℝ) := exp (-u) * (1-exp (-u))^2
noncomputable def massConstant : ℝ := 3*log 3-4*log 2
noncomputable abbrev cell : Measure ℝ := volume.restrict (Ioc 0 1)
noncomputable abbrev times : Measure ℝ := volume.restrict (Ioi 0)
noncomputable abbrev square := cell.prod cell

theorem cellSupport : ∀ᵐ x ∂cell, x ∈ Ioc (0:ℝ) 1 :=
  ae_restrict_mem measurableSet_Ioc

theorem positiveTime : ∀ᵐ t ∂times, 0 < t := ae_restrict_mem measurableSet_Ioi

theorem squarePositive : ∀ᵐ z ∂square, 0 < 1+z.1+z.2 := by
  apply (Measure.ae_prod_iff_ae_ae (measurableSet_lt measurable_const (by fun_prop : Measurable (fun z : ℝ × ℝ => 1+z.1+z.2)))).2
  filter_upwards [cellSupport] with x hx
  filter_upwards [cellSupport] with y hy
  change 0 < 1+x+y
  linarith [hx.1,hy.1]

theorem cellIntegral {f : ℝ → ℝ} (hi : IntervalIntegrable f volume 0 1)
    (hn : ∀ x ∈ Ioc 0 1, 0 ≤ f x) :
    ∫⁻ x, ENNReal.ofReal (f x) ∂cell = ENNReal.ofReal (∫ x in (0:ℝ)..1, f x) := by
  rw [intervalIntegral.integral_of_le zero_le_one, ofReal_integral_eq_lintegral_ofReal hi.1]
  exact cellSupport.mono hn

theorem expCell {u : ℝ} (hu : 0 < u) :
    ∫⁻ x, ENNReal.ofReal (exp (-u*x)) ∂cell = ENNReal.ofReal ((1-exp (-u))/u) := by
  rw [cellIntegral ((by fun_prop : Continuous (fun x : ℝ => exp (-u*x))).intervalIntegrable 0 1)
    (fun x _ => (exp_pos _).le)]
  congr 1
  rw [intervalIntegral.integral_comp_mul_left exp (neg_ne_zero.mpr hu.ne'), integral_exp]
  simp
  ring

theorem logCell {c : ℝ} (hc : 0 < c) :
    (∫ s in (0:ℝ)..1, (c+s)⁻¹) = log (c+1)-log c := by
  rw [intervalIntegral.integral_comp_add_left (fun y : ℝ => y⁻¹)]
  simpa [Real.log_div (by linarith : c+1 ≠ 0) hc.ne'] using
    integral_inv_of_pos (a := c) (b := c+1) hc (by linarith)

theorem squareConstant :
    ∫⁻ z, ENNReal.ofReal ((1+z.1+z.2)⁻¹) ∂square = ENNReal.ofReal massConstant := by
  rw [lintegral_prod _ (by fun_prop)]
  have inner {s : ℝ} (hs : s ∈ Ioc 0 1) :
      ∫⁻ r, ENNReal.ofReal ((1+s+r)⁻¹) ∂cell =
        ENNReal.ofReal (log (2+s)-log (1+s)) := by
    have hc : 0 < 1+s := by linarith [hs.1]
    have hi : ContinuousOn (fun r : ℝ => (1+s+r)⁻¹) (uIcc 0 1) := by
      apply ContinuousOn.inv₀ (by fun_prop)
      intro r hr
      rw [uIcc_of_le zero_le_one] at hr
      linarith [hr.1]
    rw [cellIntegral hi.intervalIntegrable (fun r hr => inv_nonneg.mpr (by linarith [hr.1])),
      logCell hc]
    congr 2
    ring_nf
  calc
    _ = ∫⁻ s, ENNReal.ofReal (log (2+s)-log (1+s)) ∂cell :=
      lintegral_congr_ae (cellSupport.mono fun s hs => inner hs)
    _ = ENNReal.ofReal massConstant := by
      have cont (a : ℝ) (ha : 0 < a) : ContinuousOn (fun s : ℝ => log (a+s)) (uIcc 0 1) := by
        apply ContinuousOn.log (by fun_prop)
        intro s hs
        rw [uIcc_of_le zero_le_one] at hs
        linarith [hs.1]
      have i1 := (cont 1 zero_lt_one).intervalIntegrable (μ := volume)
      have i2 := (cont 2 (by norm_num)).intervalIntegrable (μ := volume)
      rw [cellIntegral (i2.sub i1) (fun x hx => sub_nonneg.mpr
        (Real.log_le_log (by linarith [hx.1]) (by linarith))),
        intervalIntegral.integral_sub i2 i1,
        intervalIntegral.integral_comp_add_left log, intervalIntegral.integral_comp_add_left log,
        integral_log, integral_log]
      congr 1
      norm_num [massConstant]
      ring

noncomputable def mixture (u : ℝ) (z : ℝ × ℝ) : ℝ≥0∞ :=
  ENNReal.ofReal (exp (-(1+z.1+z.2)*u))

theorem squareKernel {u : ℝ} (hu : 0 < u) :
    ∫⁻ z, mixture u z ∂square = ENNReal.ofReal (detector u/u^2) := by
  have factor (s r : ℝ) : mixture u (s,r) =
      (ENNReal.ofReal (exp (-u)) * ENNReal.ofReal (exp (-u*s))) *
        ENNReal.ofReal (exp (-u*r)) := by
    unfold mixture
    change ENNReal.ofReal (exp (-(1+s+r)*u)) = _
    rw [show -(1+s+r)*u = (-u+-u*s)+ -u*r by ring, exp_add, exp_add,
      ENNReal.ofReal_mul (by positivity), ENNReal.ofReal_mul (exp_pos _).le]
  rw [lintegral_prod _ (by unfold mixture; fun_prop)]
  simp_rw [factor, lintegral_const_mul _ (by fun_prop : Measurable (fun r : ℝ =>
    ENNReal.ofReal (exp (-u*r)))), expCell hu]
  set v := (1-exp (-u))/u
  have hv : 0 ≤ v := div_nonneg (sub_nonneg.mpr (exp_le_one_iff.mpr (by linarith))) hu.le
  simp_rw [mul_right_comm (ENNReal.ofReal (exp (-u))) _ (ENNReal.ofReal v)]
  rw [lintegral_const_mul _ (by fun_prop), expCell hu]
  change (_ * ENNReal.ofReal v) * ENNReal.ofReal v = _
  rw [← ENNReal.ofReal_mul (exp_pos _).le, ← ENNReal.ofReal_mul (mul_nonneg (exp_pos _).le hv)]
  congr 1
  unfold detector v
  ring

theorem timeIntegral {c E : ℝ} (hc : 0 < c) (hE : 0 < E) :
    ∫⁻ t, ENNReal.ofReal (exp (-c*(t*E))) ∂times = ENNReal.ofReal (1/(c*E)) := by
  simp_rw [show ∀ t : ℝ, -c*(t*E) = -(c*E)*t by intro t; ring]
  have hn : -(c*E) < 0 := neg_neg_of_pos (mul_pos hc hE)
  rw [← ofReal_integral_eq_lintegral_ofReal (integrableOn_exp_mul_Ioi hn 0)
    (Filter.Eventually.of_forall fun t => (exp_pos _).le), integral_exp_mul_Ioi hn]
  simp

theorem singleEnergy {E : ℝ} (hE : 0 < E) :
    ∫⁻ t, ENNReal.ofReal (detector (t*E)/t^2) ∂times =
      ENNReal.ofReal (E*massConstant) := by
  have hkernel : ∀ᵐ t ∂times, ENNReal.ofReal (detector (t*E)/t^2) =
      ENNReal.ofReal (E^2) * ∫⁻ z, mixture (t*E) z ∂square := by
    filter_upwards [positiveTime] with t ht
    rw [squareKernel (mul_pos ht hE), ← ENNReal.ofReal_mul (sq_nonneg E)]
    congr 1
    field_simp
    ring
  have hswap : (∫⁻ t, ∫⁻ z, mixture (t*E) z ∂square ∂times) =
      ∫⁻ z, ∫⁻ t, mixture (t*E) z ∂times ∂square :=
    lintegral_lintegral_swap (by unfold Function.uncurry mixture; fun_prop)
  have hin : ∀ᵐ z ∂square, (∫⁻ t, mixture (t*E) z ∂times) =
      ENNReal.ofReal E⁻¹ * ENNReal.ofReal ((1+z.1+z.2)⁻¹) := by
    filter_upwards [squarePositive] with z hz
    unfold mixture
    rw [timeIntegral hz hE, ← ENNReal.ofReal_mul (inv_nonneg.mpr hE.le)]
    congr 1
    simp [one_div, mul_inv_rev]
  rw [lintegral_congr_ae hkernel, lintegral_const_mul' _ _ ENNReal.ofReal_ne_top, hswap,
    lintegral_congr_ae hin, lintegral_const_mul' _ _ ENNReal.ofReal_ne_top, squareConstant,
    ← mul_assoc, ← ENNReal.ofReal_mul (sq_nonneg E), ← ENNReal.ofReal_mul (by positivity)]
  congr 1
  field_simp
  ring

/-- Integration over positive physical times returns the full first moment.
The spectral law is allowed infinite first moment and need not have finite total mass. -/
theorem positiveTimeSum (ν : Measure ℝ) [SFinite ν] (supp : ∀ᵐ E ∂ν, 0 ≤ E) :
    (∫⁻ t, (∫⁻ E, ENNReal.ofReal (detector (t*E)) ∂ν) *
        ENNReal.ofReal ((t^2)⁻¹) ∂times) =
      ENNReal.ofReal massConstant * ∫⁻ E, ENNReal.ofReal E ∂ν := by
  have pull (t : ℝ) : (∫⁻ E, ENNReal.ofReal (detector (t*E)) ∂ν) *
      ENNReal.ofReal ((t^2)⁻¹) = ∫⁻ E, ENNReal.ofReal (detector (t*E)/t^2) ∂ν := by
    rw [← lintegral_mul_const' _ _ ENNReal.ofReal_ne_top]
    apply lintegral_congr
    intro E
    rw [div_eq_mul_inv, ENNReal.ofReal_mul (show 0 ≤ detector (t*E) by unfold detector; positivity)]
  simp_rw [pull]
  rw [lintegral_lintegral_swap (by unfold Function.uncurry detector; fun_prop)]
  rw [← lintegral_const_mul' _ _ ENNReal.ofReal_ne_top]
  apply lintegral_congr_ae
  filter_upwards [supp] with E hE
  rcases hE.eq_or_lt with h|h
  · subst E
    simp [detector]
  · rw [singleEnergy h, ENNReal.ofReal_mul h.le, mul_comm]

/-- The symbol on the first-moment line can cancel only when both phases equal one. -/
theorem phaseRigidity {x y v w : ℝ} (unitTwo : x^2+y^2=1)
    (unitThree : v^2+w^2=1) (re : 1+3*v=4*x) (im : 3*w=4*y) :
    x=1 ∧ y=0 ∧ v=1 ∧ w=0 := by
  have a : (1+3*v)^2+(3*w)^2 = 16 := by rw [re,im]; nlinarith only [unitTwo]
  have b : v=1 := by nlinarith only [a,unitThree]
  have c : w=0 := by rw [b] at unitThree; nlinarith only [unitThree,sq_nonneg w]
  exact ⟨by linarith, by linarith, b, c⟩

/-- Separating grid error, missing-time error and errors of the measured triples. -/
theorem gridLower {reported retained total outside mesh noise : ℝ}
    (sampleError : |reported-retained| ≤ mesh+noise)
    (subwindow : retained ≤ total) (tail : total-retained ≤ outside) :
    reported-(mesh+noise) ≤ total ∧
    total ≤ reported+mesh+noise+outside := by
  obtain ⟨lo,hi⟩ := abs_le.mp sampleError
  constructor
  · linarith only [hi,subwindow]
  · linarith only [lo,tail]

theorem massConstant_pos : 0 < massConstant := by
  have h := Real.log_pos (show 1 < (3:ℝ)^3/2^4 by norm_num)
  rw [Real.log_div (by norm_num) (by norm_num), Real.log_pow, Real.log_pow] at h
  simpa [massConstant] using h

end YangMills.PositiveTimeSumRule
#print axioms YangMills.PositiveTimeSumRule.squarePositive
#print axioms YangMills.PositiveTimeSumRule.cellIntegral
#print axioms YangMills.PositiveTimeSumRule.expCell
#print axioms YangMills.PositiveTimeSumRule.logCell
#print axioms YangMills.PositiveTimeSumRule.squareConstant
#print axioms YangMills.PositiveTimeSumRule.squareKernel
#print axioms YangMills.PositiveTimeSumRule.timeIntegral
#print axioms YangMills.PositiveTimeSumRule.singleEnergy
#print axioms YangMills.PositiveTimeSumRule.positiveTimeSum
#print axioms YangMills.PositiveTimeSumRule.phaseRigidity
#print axioms YangMills.PositiveTimeSumRule.gridLower
#print axioms YangMills.PositiveTimeSumRule.massConstant_pos
