import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

open MeasureTheory Set Filter
namespace YangMills.Clustering

/-- Real part of the rectangular contour phase on its upper side. -/
theorem topPhase {m x u y : ℝ} (hm : 0 ≤ m) (hx : m ≤ x) (hu : 0 ≤ u)
    (hu' : u ≤ 1) (hy : 0 ≤ y) :
    u*(m*Real.cosh y-x*Real.sinh y) ≤ m*Real.exp (-y) := by
  have hs := Real.sinh_nonneg_iff.mpr hy
  have h : m*Real.cosh y - x*Real.sinh y ≤ m*(Real.cosh y-Real.sinh y) := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hx) hs]
  rw [Real.cosh_sub_sinh] at h
  calc
    _ ≤ u*(m*Real.exp (-y)) := mul_le_mul_of_nonneg_left h hu
    _ ≤ _ := by nlinarith [mul_nonneg (sub_nonneg.mpr hu') (mul_nonneg hm (Real.exp_pos (-y)).le)]

/-- Zeroth cyclic coefficient of (a*z+b/z)^n, computed as a Laurent walk. -/
private def coeff (a b : ℕ) : ℕ → ℤ → ℕ
  | 0, j => if j = 0 then 1 else 0
  | n+1, j => a*coeff a b n (j-1) + b*coeff a b n (j+1)

theorem circleFixture : (coeff 4 2 5 0, coeff 4 2 6 0) = (0,10240) := by decide

/-- The low branch is increasing and its value at the threshold has tail error at most q. -/
theorem lowResidual {f : ℝ → ℝ} {m x q : ℝ} (h : MonotoneOn f (Icc 0 m))
    (h0 : f 0 = 0) (hx : 0 ≤ x) (hm : x ≤ m)
    (hq : q ≤ 1) (hend : |1-f m| ≤ q) : |1-f x| ≤ 1 := by
  have hfirst := h (show 0 ∈ Icc 0 m from ⟨le_rfl,hx.trans hm⟩) ⟨hx,hm⟩ hx
  have hlast := h (show x ∈ Icc 0 m from ⟨hx,hm⟩) ⟨hx.trans hm,le_rfl⟩ hm
  rw [h0] at hfirst
  rw [abs_le] at hend ⊢
  constructor <;> linarith

/-- The absolute residual on a signed cross spectrum, integrated against a
positive dominating measure, costs one below the threshold and q above. -/
theorem residualIntegral (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f s : ℝ → ℝ) (m q : ℝ)
    (hs : ∀ x, |s x| ≤ 1) (hl : ∀ x < m, |1-f x| ≤ 1)
    (hh : ∀ x, m ≤ x → |1-f x| ≤ q) :
    |∫ x, (1-f x)*s x ∂μ| ≤ μ.real (Iio m) + q * μ.real (Ici m) := by
  let g : ℝ → ℝ := fun x => (Iio m).indicator (fun _ => (1:ℝ)) x +
                             (Ici m).indicator (fun _ => q) x
  have hg : Integrable g μ :=
    ((integrable_const _).indicator measurableSet_Iio).add
      ((integrable_const _).indicator measurableSet_Ici)
  have bound : ∀ x, ‖(1-f x)*s x‖ ≤ g x := by
    intro x
    simp only [Real.norm_eq_abs, abs_mul]
    have hs' := mul_le_mul_of_nonneg_left (hs x) (abs_nonneg (1-f x))
    by_cases hm : x < m
    · simpa [g, hm, not_le.mpr hm, Set.indicator, mul_one] using (hs'.trans (by simpa using hl x hm))
    · have hm' := le_of_not_gt hm
      simpa [g, hm, hm', Set.indicator, mul_one] using (hs'.trans (by simpa using hh x hm'))
  have H := norm_integral_le_of_norm_le hg (Filter.Eventually.of_forall bound)
  rw [Real.norm_eq_abs] at H
  calc
    _ ≤ _ := H
    _ = _ := by
      rw [show g = _ from rfl, integral_add ((integrable_const _).indicator measurableSet_Iio)
        ((integrable_const _).indicator measurableSet_Ici),
        integral_indicator measurableSet_Iio, integral_indicator measurableSet_Ici]
      simp [mul_comm]

theorem translatedBudget {c v w d q : ℝ} (hq : q < 1)
    (h : c ≤ d + w + q*(v-w)) : (c-d-q*v)/(1-q) ≤ w := by
  apply (div_le_iff₀ (by linarith)).mpr
  linarith

theorem guardedBand {mass low band u ell v : ℝ}
    (h : mass ≤ low+band) (hg : low ≤ ell^2*u^2*v) :
    mass-ell^2*u^2*v ≤ band := by linarith

private def atoms : List (ℕ × ℕ) := [(0,81),(1,6),(2,10),(3,7),(7,4)]
private def mass (p : ℕ → Bool) := ((atoms.filter fun em => p em.1).map Prod.snd).sum
theorem thresholdFixture : (mass (fun e => 0 < e && e < 3), mass (fun e => 3 ≤ e)) = (16,11) := by decide

/-- Keeping the filter damping yields the Euclidean norm of (h,m) in the exponent. -/
theorem angularBalance {h m t a c s : ℝ} (ht : 0 ≤ t) (ha : 0 ≤ a)
    (hunit : c^2+s^2=1) (ha2 : a^2=h^2+m^2) :
    t*(h*s-m*(1-c)) ≤ t*(a-m) := by
  have hs : (h*s+m*c)^2 ≤ a^2 := by
    have id : (h*s+m*c)^2+(h*c-m*s)^2=(h^2+m^2)*(c^2+s^2) := by ring
    rw [hunit, mul_one, ← ha2] at id
    nlinarith [sq_nonneg (h*c-m*s)]
  have hle : h*s+m*c ≤ a := by nlinarith [sq_nonneg (h*s+m*c-a)]
  apply mul_le_mul_of_nonneg_left _ ht
  linarith

theorem balancedTime {t a m d : ℝ} (h : t*a=d) :
    -d+t*(a-m) = -m*t := by linarith

theorem strongExponent {a : ℝ} (ha : 0 < a) (h : a^2 ≤ 292) :
    (7:ℝ)/10 < 12/a := by
  apply (lt_div_iff₀ ha).mpr
  nlinarith [sq_nonneg (a-120/7)]

theorem optimizedRate {w : ℝ} (hw : 0 < w) :
    ((w+2)^2)/(1+2/w) = w*(w+2) := by
  field_simp
  ring

theorem translatedExample {w : ℝ} (h : 3/4 ≤ 1/16+w+(1/4)*(1-w)) :
    7/12 ≤ w := by linarith

private def squaredNorm (h m : ℕ) := h*h+m*m
theorem clockFixture : squaredNorm 16 6 = 292 := by decide

/-- The imaginary-time contour kernel is dominated by the static kernel. -/
theorem lagKernel {b a u : ℝ} (hb : 1 ≤ b) (hba : b^2=1+a^2)
    (hu : u^2 ≤ 1) : b*u^2 ≤ u^2+a^2 := by
  have := mul_nonneg (sub_nonneg.mpr hb) (sub_nonneg.mpr hu)
  nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ b by linarith)]

theorem poleResidue {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    b*a/(2*a*b)=1/2 := by field_simp; ring

/-- One nonzero reading can force mass bounded away from zero and infinity. -/
theorem threeReadingBand {read err v small upper multiplier mass : ℝ}
    (h : read ≤ err+small*v+upper*v+multiplier*mass) (hm : 0 < multiplier) :
    (read-err-(small+upper)*v)/multiplier ≤ mass := by
  apply (div_le_iff₀ hm).mpr
  linarith

#print axioms lagKernel
#print axioms poleResidue
#print axioms threeReadingBand
#print axioms topPhase
#print axioms circleFixture
#print axioms lowResidual
#print axioms residualIntegral
#print axioms translatedBudget
#print axioms guardedBand
#print axioms thresholdFixture
#print axioms angularBalance
#print axioms balancedTime
#print axioms strongExponent
#print axioms optimizedRate
#print axioms translatedExample
#print axioms clockFixture
end YangMills.Clustering
