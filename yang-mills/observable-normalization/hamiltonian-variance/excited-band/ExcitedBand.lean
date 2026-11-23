import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
open MeasureTheory Filter
namespace YangMills.ExcitedBand

/-- s = E(1-x²), with y = sqrt s and k = sqrt K. -/
theorem scoreFloor {s y K k : ℝ} (hy : 0 ≤ y)
    (ys : y^2=s) (ks : k^2=K) (ysmall : y ≤ 1)
    (score : 3 ≤ 4*s + 4*k*y) :
    9 ≤ 32*s*(1+K) := by
  have h : 3 ≤ 4*y*(1+k) := by
    nlinarith only [score, ys, mul_le_mul_of_nonneg_left ysmall hy]
  have hs := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 3) h
  nlinarith only [hs, mul_nonneg (sq_nonneg y) (sq_nonneg (k-1)),
    congrArg (fun v : ℝ => v*(1+K)) ys, congrArg (fun v : ℝ => y^2*v) ks]

/-- The indicator bound works on the entire real line. -/
theorem pointBand (x L U : ℝ) (hL : 0 ≤ L) (hU : 0 < U) :
    x ≤ L + x^2/U + (Set.Icc L U).indicator (fun _ => U) x := by
  by_cases hx : x ∈ Set.Icc L U
  · rw [Set.indicator_of_mem hx]
    linarith only [hx.2, div_nonneg (sq_nonneg x) hU.le, hL]
  · rw [Set.indicator_of_not_mem hx, add_zero]
    by_cases lo : x ≤ L
    · linarith only [lo, div_nonneg (sq_nonneg x) hU.le]
    · have hi : U < x := lt_of_not_ge (fun h => hx ⟨(lt_of_not_ge lo).le,h⟩)
      have hs : x ≤ x^2/U := (le_div_iff₀ hU).mpr (by
        nlinarith only [mul_nonneg (hU.le.trans hi.le) (sub_nonneg.mpr hi.le)])
      linarith only [hs,hL]

theorem momentWindow (μ : Measure ℝ) [IsFiniteMeasure μ] {L U : ℝ}
    (hL : 0 ≤ L) (hU : 0 < U) (h1 : Integrable (fun x : ℝ => x) μ)
    (h2 : Integrable (fun x : ℝ => x^2) μ) :
    (∫ x, x ∂μ) ≤ L*μ.real Set.univ + (∫ x : ℝ, x^2 ∂μ)/U
      + U*μ.real (Set.Icc L U) := by
  have ha := (integrable_const L (μ := μ)).add (h2.div_const U)
  have hb := (integrable_const U (μ := μ)).indicator (measurableSet_Icc (a := L) (b := U))
  have h := integral_mono h1 (ha.add hb) (fun x => pointBand x L U hL hU)
  have step := integral_add ha hb
  have step' := integral_add (integrable_const L (μ := μ)) (h2.div_const U)
  simp only [Pi.add_apply] at step step' h
  rw [step, step',
      integral_const, integral_div, integral_indicator_const _ measurableSet_Icc,
      smul_eq_mul, mul_comm (μ.real Set.univ) L] at h
  simpa only [smul_eq_mul, mul_comm (μ.real (Set.Icc L U)) U] using h

theorem windowWeight {A L U V S W : ℝ} (hu : 0 < U)
    (moment : A ≤ L*V + S/U + U*W)
    (low : L*V ≤ A/4) (high : S/U ≤ A/4) : A/(2*U) ≤ W := by
  apply (div_le_iff₀ (by linarith : 0 < 2*U)).mpr
  linarith only [moment,low,high]

/-- Positive time differences test mass away from the entire zero eigenspace. -/
theorem differenceKernel {s t L U E : ℝ} (hs : 0 ≤ s) (ht : 0 ≤ t)
    (hl : 0 ≤ L) (he : E ∈ Set.Icc L U) :
    Real.exp (-t*U)*(1-Real.exp (-s*L))^2 ≤
      Real.exp (-t*E)*(1-Real.exp (-s*E))^2 := by
  have hb := Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left he.2 (neg_nonpos.mpr ht))
  have hc := Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left he.1 (neg_nonpos.mpr hs))
  have hp : 0 ≤ 1-Real.exp (-s*L) := by
    have := Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hs) hl)
    linarith
  exact mul_le_mul hb (by
    simpa only [← sq] using (mul_self_le_mul_self hp (sub_le_sub_left hc 1)))
    (sq_nonneg _) (Real.exp_pos _).le

theorem integratedDifference (μ : Measure ℝ) [IsFiniteMeasure μ] {s t L U : ℝ}
    (hs : 0 ≤ s) (ht : 0 ≤ t) (hl : 0 ≤ L)
    (hi : Integrable (fun E : ℝ => Real.exp (-t*E)*(1-Real.exp (-s*E))^2) μ) :
    (Real.exp (-t*U)*(1-Real.exp (-s*L))^2)*μ.real (Set.Icc L U) ≤
      ∫ E : ℝ, Real.exp (-t*E)*(1-Real.exp (-s*E))^2 ∂μ := by
  have hw := setIntegral_ge_of_const_le (μ := μ) measurableSet_Icc
    (measure_ne_top μ (Set.Icc L U)) (fun E hE => differenceKernel hs ht hl hE) hi.integrableOn
  have up := setIntegral_le_integral (s := Set.Icc L U) hi (Eventually.of_forall
    fun E => mul_nonneg (Real.exp_pos _).le (sq_nonneg _))
  linarith only [hw,up]

end YangMills.ExcitedBand
#print axioms YangMills.ExcitedBand.scoreFloor
#print axioms YangMills.ExcitedBand.pointBand
#print axioms YangMills.ExcitedBand.momentWindow
#print axioms YangMills.ExcitedBand.windowWeight
#print axioms YangMills.ExcitedBand.differenceKernel
#print axioms YangMills.ExcitedBand.integratedDifference
