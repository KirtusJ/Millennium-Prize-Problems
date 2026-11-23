import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open MeasureTheory
namespace YangMills.GapWeight

/-- Sharp first/second moment bound from a lower bound on the probability
of an event on which x is at least one. The probability space is arbitrary. -/
theorem lowMassBound {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] {A : Set Ω} (hA : MeasurableSet A)
    (x : Ω → ℝ) (hx : Integrable x μ)
    (hx2 : Integrable (fun i => (x i)^2) μ) {s : ℝ} (hs : 0 ≤ s)
    (hp : s^2 ≤ μ.real A) (hfloor : ∀ i ∈ A, 1 ≤ x i) :
    2*s*(∫ i, x i ∂μ) ≤ (1+s)*(∫ i, (x i)^2 ∂μ) := by
  let g := fun i => (1+s)*((1+s)*(x i)^2-2*s*x i)
  have hg : Integrable g μ := ((hx2.const_mul (1+s)).sub (hx.const_mul (2*s))).const_mul _
  have hdom (i : Ω) : A.indicator (1 : Ω → ℝ) i ≤ g i + s^2 := by
    have hsq : g i + s^2 = ((1+s)*x i-s)^2 := by dsimp [g]; ring
    rw [hsq]
    by_cases hi : i ∈ A
    · rw [Set.indicator_of_mem hi]
      change 1 ≤ _
      have ht : 1 ≤ (1+s)*x i-s := by
        nlinarith [mul_nonneg hs (sub_nonneg.mpr (hfloor i hi)), hfloor i hi]
      nlinarith [sq_nonneg ((1+s)*x i-s-1)]
    · rw [Set.indicator_of_not_mem hi]
      exact sq_nonneg _
  have h := integral_mono ((integrable_const (1 : ℝ)).indicator hA)
    (hg.add (integrable_const (s^2))) hdom
  change (∫ i, A.indicator 1 i ∂μ) ≤ ∫ i, g i + s^2 ∂μ at h
  rw [integral_indicator_one hA, integral_add hg (integrable_const _)] at h
  simp only [g, integral_const_mul, integral_sub (hx2.const_mul _) (hx.const_mul _),
    integral_const, measureReal_univ_eq_one, one_smul] at h
  by_contra hn
  have hg' := mul_pos (a := 1+s) (by linarith)
    (sub_pos.mpr (lt_of_not_ge hn))
  nlinarith

/-- Equality for the two-atom law at x=1 and x=s/(1+s). -/
theorem twoAtomEquality (s : ℝ) (hs : 0 ≤ s) :
    2*s*(s^2+(1-s^2)*(s/(1+s))) =
    (1+s)*(s^2+(1-s^2)*(s/(1+s))^2) := by
  have h : 1+s ≠ 0 := by linarith
  field_simp
  ring

/-- The cutoff event under the half-time measure, from bounds on its
conditional contributions to the mean transfer weight. -/
theorem halfTimeFloor {p a b r : ℝ} (hab : a < b)
    (hmean : r ≤ p*b+(1-p)*a) :
    (r-a)/(b-a) ≤ p := by
  apply (div_le_iff₀ (sub_pos.mpr hab)).mpr
  linarith

/-- Reweighting by an increasing function raises the mean of a comonotone
test. Only the three stated integrability hypotheses are used. -/
theorem monotoneTilt {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (a b : Ω → ℝ) (ha : Integrable a μ)
    (hb : Integrable b μ) (hab : Integrable (fun i => a i*b i) μ)
    (h : ∀ i j, 0 ≤ (a i-a j)*(b i-b j)) :
    (∫ i, a i ∂μ)*(∫ i, b i ∂μ) ≤ ∫ i, a i*b i ∂μ := by
  have hr (i : Ω) : a i*(∫ j, b j ∂μ) + b i*(∫ j, a j ∂μ) ≤
      a i*b i + ∫ j, a j*b j ∂μ := by
    have H := integral_mono ((hb.const_mul (a i)).add (ha.const_mul (b i)))
      ((integrable_const (a i*b i)).add hab) (fun j => by
        change a i*b j + b i*a j ≤ a i*b i + a j*b j
        nlinarith [h i j])
    simp only [Pi.add_apply] at H
    simpa only [integral_add (hb.const_mul _) (ha.const_mul _),
      integral_add (integrable_const _) hab, integral_const_mul, integral_const,
      measureReal_univ_eq_one, one_smul] using H
  have H := integral_mono ((ha.mul_const _).add (hb.mul_const _))
    (hab.add (integrable_const _)) hr
  simp only [Pi.add_apply] at H
  simp only [integral_add (ha.mul_const _) (hb.mul_const _),
    integral_add hab (integrable_const _), integral_mul_const, integral_const,
    measureReal_univ_eq_one, one_smul] at H
  linarith

end YangMills.GapWeight
#print axioms YangMills.GapWeight.lowMassBound
#print axioms YangMills.GapWeight.twoAtomEquality
#print axioms YangMills.GapWeight.halfTimeFloor
#print axioms YangMills.GapWeight.monotoneTilt
