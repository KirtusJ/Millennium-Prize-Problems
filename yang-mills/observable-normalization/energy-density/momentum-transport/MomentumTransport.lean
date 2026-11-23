import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith

open Real Set MeasureTheory
open scoped ENNReal

namespace YangMills.MomentumTransport

noncomputable def shell (s u t : ℝ) : ℝ := exp (-t*sqrt (s+u))/(2*sqrt (s+u))

theorem timeDerivative {s u : ℝ} (h : 0 < s+u) (t : ℝ) :
    HasDerivAt (shell s u) (-exp (-t*sqrt (s+u))/2) t := by
  have hv := sqrt_pos.mpr h
  unfold shell
  convert ((((hasDerivAt_id t).neg.mul_const (sqrt (s+u))).exp).div_const
    (2*sqrt (s+u))) using 1
  simp
  field_simp
  ring

/-- For one Lorentz shell, differentiating first in physical time then
in squared spatial momentum gives t/2 times the original shell. -/
theorem mixedDerivative {s u : ℝ} (h : 0 < s+u) (t : ℝ) :
    HasDerivAt (fun v : ℝ => -exp (-t*sqrt (s+v))/2) (t/2*shell s u t) u := by
  have hd := ((hasDerivAt_id u).const_add s).sqrt h.ne'
  convert (((hd.const_mul (-t)).exp).neg.div_const 2) using 1
  unfold shell
  simp
  ring

/-- The integrated shell equation also applies to the derivative of a
finite positive spectral sum by linearity. -/
theorem atomSum {ι : Type*} (S : Finset ι) (mass wt : ι → ℝ) {u : ℝ}
    (pos : ∀ i ∈ S, 0 < mass i + u) (t : ℝ) :
    HasDerivAt (fun v : ℝ => ∑ i ∈ S, wt i * (-exp (-t*sqrt (mass i+v))/2))
      (t/2 * ∑ i ∈ S, wt i*shell (mass i) u t) u := by
  rw [Finset.mul_sum]
  apply HasDerivAt.sum
  intro i hi
  convert (mixedDerivative (pos i hi) t).const_mul (wt i) using 1
  ring

/-- The positive heat-parameter expansion shifts the squared momentum under
an arbitrary nonnegative measure, even when the target integral is infinite. -/
theorem heatShiftSeries (μ : Measure ℝ) (support : ∀ᵐ z ∂μ, 0 ≤ z)
    {a : ℝ} (ha : 0 ≤ a) (u : ℝ) :
    (∑' n : ℕ, ∫⁻ z : ℝ, ENNReal.ofReal (exp (-u*z)) *
      ENNReal.ofReal ((a*z)^n/(n.factorial : ℝ)) ∂μ) =
    ∫⁻ z : ℝ, ENNReal.ofReal (exp (-(u-a)*z)) ∂μ := by
  have hm (n : ℕ) : Measurable (fun z : ℝ => ENNReal.ofReal (exp (-u*z)) *
      ENNReal.ofReal ((a*z)^n/(n.factorial : ℝ))) := by fun_prop
  rw [← lintegral_tsum (fun n => (hm n).aemeasurable)]
  apply lintegral_congr_ae
  filter_upwards [support] with z hz
  have hs : HasSum (fun n : ℕ => (a*z)^n/(n.factorial : ℝ)) (Real.exp (a*z)) :=
    by simpa only [Real.exp_eq_exp_ℝ] using NormedSpace.expSeries_div_hasSum_exp ℝ (a*z)
  rw [ENNReal.tsum_mul_left, ← ENNReal.ofReal_tsum_of_nonneg (fun n => by positivity)
    hs.summable, hs.tsum_eq, ← ENNReal.ofReal_mul (exp_pos _).le, ← exp_add]
  ring_nf

/-- A measured time cell is integrated against a positive polynomial weight. -/
theorem cellPrimitive (a b t : ℝ) (n : ℕ) :
    (∫ x in a..b, x/2*((x^2-t^2)/4)^n) =
    ((((b^2-t^2)/4)^(n+1))-(((a^2-t^2)/4)^(n+1)))/(n+1) := by
  let f := fun x : ℝ => ((x^2-t^2)/4)^(n+1)/((n:ℝ)+1)
  have dn : (n:ℝ)+1 ≠ 0 := by positivity
  have hd (x : ℝ) : HasDerivAt f (x/2*((x^2-t^2)/4)^n) x := by
    unfold f
    convert (((((hasDerivAt_pow 2 x).sub_const (t^2)).div_const 4).pow (n+1)).div_const
      ((n:ℝ)+1)) using 1
    simp
    field_simp
    ring
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hd x)
    ((by fun_prop : Continuous (fun x : ℝ => x/2*((x^2-t^2)/4)^n)).intervalIntegrable _ _)]
  dsimp [f]
  ring

def quadratic (A X B u : ℝ) : ℝ := u^2*A+2*u*X+B

theorem recoverTensor (A X B u h : ℝ) (hh : h ≠ 0) :
    (quadratic A X B (u+2*h)-2*quadratic A X B (u+h)+quadratic A X B u)/
      (2*h^2) = A := by unfold quadratic; field_simp; ring

theorem recoverCross (A X B u h : ℝ) (hh : h ≠ 0) :
    (quadratic A X B (u+h)-quadratic A X B u-(2*u*h+h^2)*A)/(2*h)=X := by
  unfold quadratic
  field_simp
  ring

theorem recoverScalar (A X B u : ℝ) : quadratic A X B u-u^2*A-2*u*X=B := by
  unfold quadratic
  ring

/-- Perturbing a polynomial by a multiple of (v-u)(v-w) preserves
its readings at u and w. -/
theorem twoMomentumAmbiguity (A X B u w d v : ℝ) :
    quadratic (A+d) (X-d*(u+w)/2) (B+d*u*w) v =
    quadratic A X B v+d*(v-u)*(v-w) := by unfold quadratic; ring

theorem tensorError {e₀ e₁ e₂ η h : ℝ} (hh : h ≠ 0)
    (h₀ : |e₀| ≤ η) (h₁ : |e₁| ≤ η) (h₂ : |e₂| ≤ η) :
    |(e₂-2*e₁+e₀)/(2*h^2)| ≤ 2*η/h^2 := by
  have hp : 0 < 2*h^2 := by positivity
  obtain ⟨lo₀,hi₀⟩ := abs_le.mp h₀
  obtain ⟨lo₁,hi₁⟩ := abs_le.mp h₁
  obtain ⟨lo₂,hi₂⟩ := abs_le.mp h₂
  rw [abs_div, abs_of_pos hp, div_le_div_iff₀ hp (sq_pos_of_ne_zero hh)]
  have bound : |e₂-2*e₁+e₀| ≤ 4*η := by
    apply abs_le.mpr
    constructor <;> linarith
  nlinarith [mul_nonneg (sub_nonneg.mpr bound) (sq_nonneg h)]

theorem scalarAbsent {A X B : ℝ} (gram : X^2 ≤ A*B) (h : B=0) : X=0 := by
  subst B
  nlinarith only [gram, sq_nonneg X]

/-- Expanding each bin before integrating shows why the packet method needs
first and second powers of the base squared momentum. -/
theorem packetShift (A X B v d : ℝ) :
    quadratic A X B (v+d)=quadratic A X B v+2*d*(v*A+X)+d^2*A := by
  unfold quadratic
  ring

theorem packetRecovery (A₁ A₂ X₀ X₁ B₀ : ℝ) :
    (A₁+X₀)-A₁=X₀ ∧ (A₂+2*X₁+B₀)-2*(A₂+X₁)+A₂=B₀ := by
  constructor <;> ring

/-- A strict excess over a trial mass threshold forces finite below-threshold
weight in the regularized measure of the tested channel. -/
theorem lowMassWeight {total low next fast slow : ℝ} (gap : fast < slow)
    (split : next ≤ slow*low+fast*(total-low)) :
    (next-fast*total)/(slow-fast) ≤ low := by
  apply (div_le_iff₀ (sub_pos.mpr gap)).2
  linarith only [split]

end YangMills.MomentumTransport
#print axioms YangMills.MomentumTransport.timeDerivative
#print axioms YangMills.MomentumTransport.mixedDerivative
#print axioms YangMills.MomentumTransport.atomSum
#print axioms YangMills.MomentumTransport.cellPrimitive
#print axioms YangMills.MomentumTransport.recoverTensor
#print axioms YangMills.MomentumTransport.recoverCross
#print axioms YangMills.MomentumTransport.recoverScalar
#print axioms YangMills.MomentumTransport.twoMomentumAmbiguity
#print axioms YangMills.MomentumTransport.tensorError
#print axioms YangMills.MomentumTransport.scalarAbsent
#print axioms YangMills.MomentumTransport.packetShift
#print axioms YangMills.MomentumTransport.packetRecovery
#print axioms YangMills.MomentumTransport.heatShiftSeries
#print axioms YangMills.MomentumTransport.lowMassWeight
