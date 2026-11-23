import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open MeasureTheory
open scoped BigOperators
namespace YangMills.SmearedMoments

/-- Convert the integrated divergence estimate to a shift-independent spread. -/
theorem vectorSpread {k y : ℝ} (score : 2 ≤ (3+4*k)*y) :
    4 ≤ 25*(1+k^2)*y^2 := by
  have h := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 2) score
  nlinarith only [h,mul_nonneg (sq_nonneg (4-3*k)) (sq_nonneg y)]

/-- Sum the four private-link estimates for one electric link. -/
theorem edgeBound (u v w z e τ : ℝ)
    (hu : τ*u^2 ≤ e) (hv : τ*v^2 ≤ e)
    (hw : τ*w^2 ≤ e) (hz : τ*z^2 ≤ e) :
    τ*(u^2+v^2+w^2+z^2) ≤ 4*e := by
  linarith only [hu,hv,hw,hz]

/-- Symmetric nonnegative majorants with bounded row sums act boundedly on ℓ². -/
theorem rowBound {ι : Type*} [Fintype ι] (w : ι → ι → ℝ) (c : ι → ℝ) (D : ℝ)
    (hw : ∀ i j, 0 ≤ w i j) (sym : ∀ i j, w j i = w i j)
    (rows : ∀ i, ∑ j, w i j ≤ D) :
    ∑ i, ∑ j, w i j*c i*c j ≤ D * ∑ i, (c i)^2 := by
  have single (i j : ι) : w i j*c i*c j ≤
      (w i j*(c i)^2 + w i j*(c j)^2)/2 := by
    nlinarith only [mul_nonneg (hw i j) (sq_nonneg (c i-c j))]
  have hs := Finset.sum_le_sum (s := Finset.univ) (fun i _ =>
    Finset.sum_le_sum (s := Finset.univ) (fun j _ => single i j))
  have swap : (∑ i, ∑ j, w i j*(c j)^2) = ∑ i, ∑ j, w i j*(c i)^2 := by
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by rw [sym j i]))
  have side : (∑ i, ∑ j, w i j*(c i)^2) ≤ D*∑ i,(c i)^2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (rows i) (sq_nonneg _)
  simp only [← Finset.sum_div, Finset.sum_add_distrib] at hs
  linarith only [hs,swap,side]

theorem secondCeiling {m₂ m₁ m₃ S B κ n : ℝ}
    (hn : 0 ≤ n) (hk : 0 ≤ κ) (hs : 0 ≤ S)
    (h₃ : 0 ≤ m₃) (loss : S*(1+B) ≤ 18)
    (first : m₁ ≤ 16*κ*S*n) (third : m₃ ≤ 145*103681537*κ^3*(1+B)*n)
    (interp : m₂^2 ≤ m₁*m₃) : m₂ ≤ 2100000*κ^2*n := by
  have hp : 0 ≤ 16*κ*S*n := by positivity
  have ha := mul_le_mul_of_nonneg_right first h₃
  have hb := mul_le_mul_of_nonneg_left third hp
  have hx := mul_le_mul_of_nonneg_right loss
    (mul_nonneg (pow_nonneg hk 4) (sq_nonneg n))
  by_contra! bad
  have upper : 0 ≤ 2100000*κ^2*n := by positivity
  have hc := mul_self_lt_mul_self upper bad
  nlinarith only [ha,hb,hx,interp,hc,mul_nonneg (pow_nonneg hk 4) (sq_nonneg n)]

/-- The moments of a finite measure bound its mass through a genuine integral. -/
theorem massInterpolation (μ : Measure ℝ) [IsFiniteMeasure μ] (a v d : ℝ)
    (hv : v=μ.real Set.univ) (ha : a=∫ x : ℝ, x ∂μ)
    (hd : d=∫ x : ℝ, x^2 ∂μ) (hp : 0 < v)
    (h1 : Integrable (fun x : ℝ => x) μ) (h2 : Integrable (fun x : ℝ => x^2) μ) :
    a^2 ≤ v*d := by
  have H := integral_nonneg (μ := μ) (fun x : ℝ => sq_nonneg (v*x-a))
  have eq (x : ℝ) : (v*x-a)^2=v^2*x^2-(2*v*a)*x+a^2 := by ring
  simp only [eq] at H
  have step := integral_add ((h2.const_mul (v^2)).sub (h1.const_mul (2*v*a)))
    (integrable_const (μ := μ) (a^2))
  simp only [Pi.sub_apply] at step
  rw [step,integral_sub (h2.const_mul _) (h1.const_mul _),integral_const_mul,
    integral_const_mul,integral_const,smul_eq_mul,← hv,← ha,← hd] at H
  exact le_of_mul_le_mul_left (a := v) (by nlinarith only [H]) hp

theorem varianceAndRate {a d n m₁ m₂ v : ℝ} (hn : 0 < n) (ha : 0 < a) (hd : 0 < d)
    (hv : 0 ≤ v) (first : a*n ≤ m₁) (second : m₂ ≤ d*n)
    (interp : m₁^2 ≤ v*m₂) :
    a^2*n/d ≤ v ∧ m₁ ≤ (d/a)*v := by
  have h := mul_le_mul_of_nonneg_left second hv
  have mx := mul_self_le_mul_self (mul_nonneg ha.le hn.le) first
  have mpos := (mul_pos ha hn).trans_le first
  have scale : a*m₁*n ≤ v*d*n := by
    nlinarith only [mul_le_mul_of_nonneg_right first mpos.le,interp,h]
  constructor
  · apply (div_le_iff₀ hd).mpr
    apply le_of_mul_le_mul_right (a := n) _ hn
    nlinarith only [mx,interp,h]
  · have g := le_of_mul_le_mul_right scale hn
    rw [div_mul_eq_mul_div,(le_div_iff₀ ha)]
    linarith only [g]

/-- Low energies of the energy-weighted law are bounded by the unweighted mass. -/
theorem lowFirst (μ : Measure ℝ) [IsFiniteMeasure μ] {E : ℝ} (hE : 0 ≤ E)
    (h1 : Integrable (fun x : ℝ => x) μ) :
    (∫ x in Set.Icc 0 E, x ∂μ) ≤ E*μ.real Set.univ := by
  let s := Set.Icc 0 E
  have h := integral_mono_ae (h1.restrict (s := s)) (integrable_const E)
    ((ae_restrict_mem (μ := μ) (s := s) measurableSet_Icc).mono (fun x hx => hx.2))
  rw [integral_const, Measure.real, Measure.restrict_apply_univ, smul_eq_mul] at h
  have m := measureReal_mono (μ := μ) (Set.subset_univ s)
  exact h.trans (by change (μ.real s)*E ≤ E*μ.real Set.univ
                    linarith only [mul_le_mul_of_nonneg_right m hE])

theorem weightedEscape {ell m n k B E u Z : ℝ} (he : 0 ≤ E) (hu : 0 ≤ u)
    (hB : 0 ≤ B) (hZ : 0 ≤ Z) (hn : 0 < n) (hk : 0 < k)
    (mass : ell ≤ 8*E*u*Z) (first : 4*k*n ≤ 25*(1+B)*m)
    (bounded : u*(1+B) ≤ 9) :
    ell*(k*n) ≤ 450*E*Z*m := by
  have hm : 0 ≤ m := by
    by_contra! bad
    nlinarith only [first,mul_pos hk hn,mul_nonpos_of_nonneg_of_nonpos hB bad.le,bad]
  have hp : 0 ≤ 8*E*u*Z := by positivity
  have H := mul_le_mul_of_nonneg_left first hp
  have H' := mul_le_mul_of_nonneg_right mass (mul_nonneg hk.le hn.le)
  have K := mul_le_mul_of_nonneg_right bounded (mul_nonneg (mul_nonneg he hZ) hm)
  nlinarith only [H,H',K]

end YangMills.SmearedMoments
#print axioms YangMills.SmearedMoments.vectorSpread
#print axioms YangMills.SmearedMoments.edgeBound
#print axioms YangMills.SmearedMoments.rowBound
#print axioms YangMills.SmearedMoments.secondCeiling
#print axioms YangMills.SmearedMoments.massInterpolation
#print axioms YangMills.SmearedMoments.varianceAndRate
#print axioms YangMills.SmearedMoments.lowFirst
#print axioms YangMills.SmearedMoments.weightedEscape
