import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
open MeasureTheory

namespace YangMills.ActionCurvature

/-- I is the inverse moment; u is the action per face. -/
theorem curvatureBudget {A B : ℝ} (u I du : ℝ → ℝ)
    (h : ∀ x ∈ Set.uIcc A B, HasDerivAt u (du x) x)
    (hI : ∀ x ∈ Set.uIcc A B, I x = -2 * du x)
    (hi : IntervalIntegrable du volume A B) :
    (∫ x in A..B, I x) = 2*(u A-u B) := by
  rw [intervalIntegral.integral_congr hI, intervalIntegral.integral_const_mul,
    intervalIntegral.integral_eq_sub_of_hasDerivAt h hi]
  ring

theorem budgetCeiling {r total start finish : ℝ} (hr : 0 < r)
    (h : total=2*(start-finish)) (upper : r*start ≤ 5/2) (lower : 0 ≤ finish) :
    r*total ≤ 5 := by
  rw [h]
  nlinarith only [upper,mul_nonneg hr.le lower]

/-- Cauchy–Schwarz between the inverse and first moments of a finite measure. -/
theorem inverseInterpolation (μ : Measure ℝ) [IsFiniteMeasure μ]
    (hp : ∀ᵐ x ∂μ, 0 < x) (h1 : Integrable (fun x : ℝ => x) μ)
    (hinv : Integrable (fun x : ℝ => x⁻¹) μ) (m v j : ℝ)
    (hm : (∫ x : ℝ, x ∂μ)=m) (hv : μ.real Set.univ=v)
    (hj : (∫ x : ℝ, x⁻¹ ∂μ)=j) (hpos : 0 < m) : v^2 ≤ m*j := by
  have hn : 0 ≤ ∫ x : ℝ, (v*x-m)^2/x ∂μ := integral_nonneg_of_ae
    (hp.mono fun x hx => div_nonneg (sq_nonneg _) hx.le)
  have eq := integral_congr_ae (hp.mono fun x hx => show
      (v*x-m)^2/x = v^2*x - 2*v*m + m^2*x⁻¹ by field_simp [hx.ne']; ring)
  rw [eq] at hn
  have step := integral_add ((h1.const_mul (v^2)).sub (integrable_const (μ := μ) (2*v*m)))
    (hinv.const_mul (m^2))
  simp only [Pi.sub_apply] at step
  rw [step,integral_sub (h1.const_mul _) (integrable_const _),integral_const_mul (v^2),
    integral_const_mul (m^2),integral_const,smul_eq_mul,hm,hv,hj] at hn
  exact le_of_mul_le_mul_left (a := m) (by nlinarith only [hn]) hpos

theorem lowMass (μ : Measure ℝ) [IsFiniteMeasure μ] (hp : ∀ᵐ x ∂μ, 0 < x)
    (hi : Integrable (fun x : ℝ => x⁻¹) μ) {E : ℝ} (he : 0 ≤ E) :
    μ.real (Set.Ioc 0 E) ≤ E*(∫ x : ℝ, x⁻¹ ∂μ) := by
  let s := Set.Ioc 0 E
  have hind := (integrable_const (μ := μ) (1:ℝ)).indicator (measurableSet_Ioc (a := 0) (b := E))
  have h := integral_mono_ae hind (hi.const_mul E) (hp.mono fun x hx => by
    by_cases h : x ∈ s
    · rw [Set.indicator_of_mem h]
      exact (by simpa [div_eq_mul_inv] using (one_le_div hx).mpr h.2 : 1 ≤ E*x⁻¹)
    · rw [Set.indicator_of_not_mem h]
      exact mul_nonneg he (inv_nonneg.mpr hx.le))
  simpa only [integral_indicator_const _ measurableSet_Ioc, smul_eq_mul, mul_one, integral_const_mul] using h

/-- Dominate a window integral by a constant multiple of its curvature budget. -/
theorem windowAverage {A B c : ℝ} (P I : ℝ → ℝ) (hab : A ≤ B)
    (hp : IntervalIntegrable P volume A B) (hi : IntervalIntegrable I volume A B)
    (bound : ∀ x ∈ Set.Icc A B, P x ≤ c*I x) :
    (∫ x in A..B, P x) ≤ c*(∫ x in A..B, I x) := by
  have h := intervalIntegral.integral_mono_on hab hp (hi.const_mul c) bound
  simpa only [intervalIntegral.integral_const_mul] using h

theorem rmsBound {G r total sqAvg : ℝ} (hr : 0 < r) (hG : G=r^2)
    (budget : r*total ≤ 5) (interpolated : sqAvg ≤ G*(80/r)*total) :
    sqAvg ≤ 400 := by
  have h : G*(80/r)=80*r := by rw [hG]; field_simp; ring
  rw [h] at interpolated
  linarith only [interpolated,budget]

theorem scaledTail {r v V J ε m : ℝ} (hr : 0 < r) (hv : 0 < v)
    (hV : 0 < V) (hJ : 0 ≤ J) (he : 0 ≤ ε)
    (floor : v ≤ r^2*V) (low : m ≤ ε*r*J) :
    m/V ≤ ε*r^3*J/v := by
  apply (div_le_div_iff₀ hV hv).mpr
  nlinarith only [mul_le_mul_of_nonneg_left floor (mul_nonneg (mul_nonneg he hr.le) hJ),
     mul_le_mul_of_nonneg_right low hv.le]

/-- Raw probabilities of a measurable family of finite spectral laws on a dyadic window. -/
theorem dyadicRawLow (μ : ℝ → Measure ℝ) [∀ g, IsFiniteMeasure (μ g)]
    (J : ℝ → ℝ) {G r v ε : ℝ} (hr : 0 < r) (hg : G=r^2) (hv : 0 < v) (he : 0 ≤ ε)
    (posEnergy : ∀ g ∈ Set.Icc G (2*G), ∀ᵐ x ∂(μ g), 0 < x)
    (inverse : ∀ g ∈ Set.Icc G (2*G), Integrable (fun x : ℝ => x⁻¹) (μ g))
    (moment : ∀ g ∈ Set.Icc G (2*G), (∫ x : ℝ, x⁻¹ ∂(μ g)) = J g)
    (floor : ∀ g ∈ Set.Icc G (2*G), v ≤ r^2*(μ g).real Set.univ)
    (hi : IntervalIntegrable J volume G (2*G))
    (hprob : IntervalIntegrable (fun g => (μ g).real (Set.Ioc 0 (ε*r)) /
      (μ g).real Set.univ) volume G (2*G))
    (budget : r*(∫ g in G..2*G, J g) ≤ 5) :
    (∫ g in G..2*G, (μ g).real (Set.Ioc 0 (ε*r))/(μ g).real Set.univ)/G ≤ 5*ε/v := by
  have hG : 0 < G := hg ▸ sq_pos_of_pos hr
  have hab : G ≤ 2*G := by linarith
  have bound (g : ℝ) (hx : g ∈ Set.Icc G (2*G)) :
      (μ g).real (Set.Ioc 0 (ε*r))/(μ g).real Set.univ ≤ (ε*r^3/v)*J g := by
    have h := lowMass (μ g) (posEnergy g hx) (inverse g hx) (mul_nonneg he hr.le)
    rw [moment g hx] at h
    have hV : 0 < (μ g).real Set.univ := by
      by_contra! z
      linarith only [floor g hx,hv,mul_nonpos_of_nonneg_of_nonpos (sq_nonneg r) z]
    have hJ : 0 ≤ J g := by
      rw [← moment g hx]
      exact integral_nonneg_of_ae ((posEnergy g hx).mono fun x h => (inv_pos.mpr h).le)
    have res := scaledTail hr hv hV hJ he (floor g hx) h
    convert res using 1
    ring
  have HW := windowAverage _ J hab hprob hi bound
  apply (div_le_iff₀ hG).mpr
  rw [div_mul_eq_mul_div]
  apply (le_div_iff₀ hv).mpr
  have H := mul_le_mul_of_nonneg_right HW hv.le
  have id : ((ε*r^3/v)*(∫ g in G..2*G, J g))*v = (ε*r^3)*(∫ g in G..2*G, J g) := by
    field_simp
  rw [id] at H
  rw [hg] at H budget ⊢
  nlinarith only [H,mul_le_mul_of_nonneg_left budget (mul_nonneg he (sq_nonneg r))]

end YangMills.ActionCurvature
#print axioms YangMills.ActionCurvature.curvatureBudget
#print axioms YangMills.ActionCurvature.budgetCeiling
#print axioms YangMills.ActionCurvature.inverseInterpolation
#print axioms YangMills.ActionCurvature.lowMass
#print axioms YangMills.ActionCurvature.windowAverage
#print axioms YangMills.ActionCurvature.rmsBound
#print axioms YangMills.ActionCurvature.scaledTail
#print axioms YangMills.ActionCurvature.dyadicRawLow
