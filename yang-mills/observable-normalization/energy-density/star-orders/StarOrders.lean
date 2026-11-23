import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Algebra.Polynomial.Degree.Domain
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

open Polynomial Filter
open scoped Topology

namespace YangMills.StarOrders

/-- Four geometric steps leave a nonnegative controlled error in the
one local Fourier integral which separates the covariance eigenvalues. -/
theorem geomFour {x A : ℝ} (hx : 0 ≤ x) (h : x ≤ A) (hA : A ≤ 16) (ha : 0 < A) :
    let u := 1-A/16
    let p := x^2*(1+u+u^2+u^3)/16
    p ≤ x^2/A ∧ x^2/A ≤ p+x*u^4 := by
  dsimp
  have id : x^2/A=x^2*(1+(1-A/16)+(1-A/16)^2+(1-A/16)^3)/16+
      x^2/A*(1-A/16)^4 := by field_simp; ring
  have sm : x^2/A ≤ x := (div_le_iff₀ ha).2 (by nlinarith [mul_nonneg hx (sub_nonneg.mpr h)])
  constructor
  · linarith only [id,mul_nonneg (div_nonneg (sq_nonneg x) ha.le) (pow_nonneg (by linarith : 0 ≤ 1-A/16) 4)]
  · linarith only [id,mul_le_mul_of_nonneg_right sm (by positivity : 0 ≤ (1-A/16)^4)]

theorem separateModes {d : ℝ} (hl : (5285:ℝ)/8192 ≤ d) (hu : d ≤ (6439:ℝ)/8192) :
    0 < d/2 ∧ d/2 < (2-d)/3 ∧ (2-d)/3 < 1 := by
  constructor
  · linarith
  constructor <;> linarith

/-- A nonzero numerator with the three required factors must have enough
degree. The Wilson application supplies divisibility by their product. -/
theorem poleBudget {P : Polynomial ℝ} (hp : P ≠ 0) {a b : ℝ} {k m : ℕ}
    (h : ((X-C (1:ℝ))*(X-C a)*(X-C b))^k ∣ P) (hm : P.natDegree < m) :
    3*k < m := by
  have deg := Polynomial.natDegree_le_of_dvd h hp
  have h₁ := Polynomial.X_sub_C_ne_zero (1:ℝ)
  have h₂ := Polynomial.X_sub_C_ne_zero a
  have h₃ := Polynomial.X_sub_C_ne_zero b
  rw [Polynomial.natDegree_pow, Polynomial.natDegree_mul (mul_ne_zero h₁ h₂) h₃,
    Polynomial.natDegree_mul h₁ h₂] at deg
  simp only [Polynomial.natDegree_X_sub_C] at deg
  omega

/-- Moment expansion for the symmetric Fourier cell variable 1-A/16.
The supplied integrals are finite raw moments; this checks both endpoints
after expanding the geometric series. -/
theorem momentBounds {lo gap : ℝ}
    (hlo : lo = ((6:ℝ) + (6-56/16) + (6-2*56/16+562/16^2)
      + (6-3*56/16+3*562/16^2-5976/16^3))/16)
    (hg : gap = (2:ℝ)-4*18/16+6*176/16^2-4*1834/16^3+20112/16^4) :
    lo = 5285/8192 ∧ lo+gap = 6439/8192 := by
  rw [hlo,hg]
  norm_num

/-- Difference of two single-pole responses lowers the total denominator order. -/
theorem mixedStep {ι : Type*} (s : Finset ι) (w r : ι → ℝ) (a b : ℝ)
    (ha : ∀ t ∈ s, r t+a ≠ 0) (hb : ∀ t ∈ s, r t+b ≠ 0) (i j : ℕ) :
    (b-a)*(∑ t ∈ s, w t/((r t+a)^(i+1)*(r t+b)^(j+1))) =
    (∑ t ∈ s, w t/((r t+a)^(i+1)*(r t+b)^j))-
    (∑ t ∈ s, w t/((r t+a)^i*(r t+b)^(j+1))) := by
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro t ht
  rw [pow_succ, pow_succ]
  field_simp [ha t ht, hb t ht]
  ring

/-- Pure cancellations along the two axes imply all mixed cancellations in
the rectangle, including mixed terms of the first surviving total order. -/
theorem mixedVanish (M : ℕ → ℕ → ℝ) {a b : ℝ} (hab : b ≠ a) (p q : ℕ)
    (step : ∀ i j, (b-a)*M (i+1) (j+1)=M (i+1) j-M i (j+1))
    (left : ∀ i, 0 < i → i ≤ p → M i 0=0)
    (right : ∀ j, 0 < j → j ≤ q → M 0 j=0) :
    ∀ i j, i ≤ p → j ≤ q → 0 < i+j → M i j=0 := by
  intro i
  induction i with
  | zero => intro j _ hj hpos; exact right j (by omega) hj
  | succ i ih =>
    intro j
    induction j with
    | zero => intro hi _ _; exact left (i+1) (by omega) hi
    | succ j jh =>
      intro hi hj _
      have h := step i j
      rw [jh hi (by omega) (by omega), ih _ (by omega) hj (by omega),sub_self] at h
      exact (mul_eq_zero.mp h).resolve_left (sub_ne_zero.mpr hab)

theorem squaredCoefficient {ι : Type*} (s : Finset ι) (w f : ι → ℝ) :
    (∑ i ∈ s, ∑ j ∈ s, (w i*f i)*(w j*f j))=(∑ i ∈ s, w i*f i)^2 := by
  rw [pow_two, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.mul_sum]

noncomputable def cubic (a b z : ℝ) := (z-1)*(z-a)*(z-b)

/-- Barycentric identity with the four actual source radii in the quartic
experiment. Clearing the common denominator makes signs and scale explicit. -/
theorem fourSources (a b z : ℝ) :
    cubic a b (-1/2)*(8/21)*(z+1)*(z+2)*(z+4)
    + cubic a b (-1)*(-2/3)*(z+1/2)*(z+2)*(z+4)
    + cubic a b (-2)/3*(z+1/2)*(z+1)*(z+4)
    - cubic a b (-4)/21*(z+1/2)*(z+1)*(z+2) = cubic a b z := by
  unfold cubic
  ring

theorem resolventFour {a b z : ℝ} (hz : 0 ≤ z) :
    cubic a b (-1/2)*(8/21)/(z+1/2) + cubic a b (-1)*(-2/3)/(z+1)
    + cubic a b (-2)/3/(z+2) - cubic a b (-4)/21/(z+4) =
    cubic a b z/((z+1/2)*(z+1)*(z+2)*(z+4)) := by
  unfold cubic
  field_simp
  ring

theorem quarticTail {v : ℕ → ℝ} (h : Tendsto (fun n : ℕ => (n:ℝ)^4*v n)
    atTop (𝓝 (-2/Real.pi^2))) (z : ℝ) :
    Tendsto (fun n : ℕ => (n:ℝ)^16*(99/8*v n^4*z^2)) atTop
      (𝓝 (198*z^2/Real.pi^8)) := by
  have t := ((h.pow 4).const_mul (99/8:ℝ)).mul_const (z^2)
  convert t using 1
  · ext n
    dsimp
    ring
  · ring

theorem slowerLeak (u v : ℝ) (a b : ℝ) :
    (9/2)*v^2*b^2 ≤ 3*u^2*a^2+(9/2)*v^2*b^2 := by nlinarith [sq_nonneg (u*a)]

/-- Gaussian averaging of a pointwise characteristic-function estimate.
Only the displayed integrable weight is needed of the mixing measure. -/
theorem integratedError {Ω : Type*} [MeasurableSpace Ω] (μ : MeasureTheory.Measure Ω)
    (f : Ω → ℂ) (w : Ω → ℝ) (ε : ℝ) (hf : MeasureTheory.Integrable f μ)
    (hw : MeasureTheory.Integrable w μ) (bound : ∀ᵐ x ∂μ, ‖f x‖ ≤ ε*w x) :
    ‖∫ x, f x ∂μ‖ ≤ ε * ∫ x, w x ∂μ := by
  rw [← MeasureTheory.integral_const_mul]
  exact (MeasureTheory.norm_integral_le_integral_norm _).trans
    (MeasureTheory.integral_mono_ae hf.norm (hw.const_mul _) bound)

theorem exponentError {s S Q : ℝ} (hs : 0 ≤ s) (hQ : 0 ≤ Q) (ord : Q ≤ S) :
    0 ≤ Real.exp (-s*Q)-Real.exp (-s*S) ∧
      Real.exp (-s*Q)-Real.exp (-s*S) ≤ s*(S-Q) := by
  have hd := mul_nonneg hs (sub_nonneg.mpr ord)
  have hq := Real.exp_le_one_iff.mpr (by nlinarith [mul_nonneg hs hQ] : -s*Q ≤ 0)
  have h₁ := Real.exp_le_one_iff.mpr (neg_nonpos.mpr hd)
  have h₂ := Real.add_one_le_exp (-(s*(S-Q)))
  have he : Real.exp (-s*S) = Real.exp (-s*Q)*Real.exp (-(s*(S-Q))) := by
    rw [← Real.exp_add]; congr 1; ring
  rw [he]
  constructor
  · nlinarith [mul_nonneg (Real.exp_pos (-s*Q)).le (sub_nonneg.mpr h₁)]
  · nlinarith only [h₂,mul_nonneg (sub_nonneg.mpr hq) (sub_nonneg.mpr h₁)]

end YangMills.StarOrders
#print axioms YangMills.StarOrders.geomFour
#print axioms YangMills.StarOrders.separateModes
#print axioms YangMills.StarOrders.poleBudget
#print axioms YangMills.StarOrders.mixedStep
#print axioms YangMills.StarOrders.mixedVanish
#print axioms YangMills.StarOrders.squaredCoefficient
#print axioms YangMills.StarOrders.quarticTail
#print axioms YangMills.StarOrders.slowerLeak
#print axioms YangMills.StarOrders.fourSources
#print axioms YangMills.StarOrders.resolventFour
#print axioms YangMills.StarOrders.momentBounds
#print axioms YangMills.StarOrders.integratedError
#print axioms YangMills.StarOrders.exponentError
