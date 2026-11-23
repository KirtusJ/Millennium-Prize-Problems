import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
open MeasureTheory Filter
namespace YangMills.CubicMoment

theorem kineticDouble {d p r a : ℝ} (h : r ≤ a) (h' : p ≤ a)
    (term : ℝ) (ht : term ≤ r + d + 2*p) : term ≤ 3*a+d := by
  linarith only [ht,h,h']

theorem localThird {κ B lam S C M : ℝ} (hk : 0 ≤ κ) (hb : 0 ≤ B) (hc : 0 ≤ C)
    (magnetic : lam*S ≤ 2*κ*B)
    (form : M ≤ κ^2/8*(κ/4*C*(1+16*B)+6144*lam*S)) :
    M ≤ (C+1536)*κ^3*(1+B) := by
  have h := mul_le_mul_of_nonneg_left magnetic (sq_nonneg κ)
  nlinarith only [form,h,mul_nonneg (pow_nonneg hk 3) hc,
    mul_nonneg (mul_nonneg (pow_nonneg hk 3) hc) hb, pow_nonneg hk 3]

/-- Nonnegative energy makes the weighted square nonnegative. -/
theorem momentInterpolation (μ : Measure ℝ) (hs : ∀ᵐ x ∂μ, 0 ≤ x)
    (h1 : Integrable (fun x : ℝ => x) μ) (h2 : Integrable (fun x : ℝ => x^2) μ)
    (h3 : Integrable (fun x : ℝ => x^3) μ)
    (a b c : ℝ) (ha : a=∫ x : ℝ, x ∂μ) (hb : b=∫ x : ℝ, x^2 ∂μ)
    (hc : c=∫ x : ℝ, x^3 ∂μ) (pos : 0 < a) :
    b^2 ≤ a*c := by
  have eq (x : ℝ) : x*(a*x-b)^2 = a^2*x^3-(2*a*b)*x^2+b^2*x := by ring
  have hp : 0 ≤ ∫ x : ℝ, x*(a*x-b)^2 ∂μ :=
    integral_nonneg_of_ae (hs.mono fun x hx => mul_nonneg hx (sq_nonneg _))
  simp only [eq] at hp
  have addstep := integral_add ((h3.const_mul (a^2)).sub (h2.const_mul (2*a*b))) (h1.const_mul (b^2))
  have substep := integral_sub (h3.const_mul (a^2)) (h2.const_mul (2*a*b))
  simp only [Pi.sub_apply] at addstep
  rw [addstep,substep, integral_const_mul,
    integral_const_mul, integral_const_mul, ← ha, ← hb, ← hc] at hp
  apply (le_of_mul_le_mul_left (a := a) (by nlinarith only [hp]) pos)

theorem smallLoss {S B : ℝ} (hS : S ≤ 1) (hb : 0 ≤ B) (hB : B ≤ 1) :
    S*(1+B) ≤ 18 := by
  nlinarith only [hS,hB,mul_le_mul_of_nonneg_right hS hb]

theorem largeLoss {S B u : ℝ} (hu : 1 ≤ u) (hS : 0 ≤ S)
    (hB : B ≤ 5*u/2) (loss : S*u^2 ≤ 2*B) : S*(1+B) ≤ 18 := by
  have hu' : 0 < u := by linarith only [hu]
  have hsu : S*u ≤ 5 := le_of_mul_le_mul_right
    (a := u) (by nlinarith only [hB,loss]) hu'
  have hb' : 1+B ≤ 7*u/2 := by linarith only [hu,hB]
  nlinarith only [mul_le_mul_of_nonneg_left hb' hS, hsu]

theorem uniformSecond {M₁ M₂ M₃ C κ S B : ℝ} (hc : 0 ≤ C) (hk : 0 ≤ κ)
    (hm : M₁=4*κ*S) (hS : 0 ≤ S) (h3 : M₃ ≤ C*κ^3*(1+B))
    (hi : M₂^2 ≤ M₁*M₃) (h : S*(1+B) ≤ 18) :
    M₂^2 ≤ 72*C*κ^4 := by
  rw [hm] at hi
  have hp : 0 ≤ 4*κ*S := mul_nonneg (by linarith only [hk]) hS
  have hx := mul_le_mul_of_nonneg_left h (mul_nonneg hc (pow_nonneg hk 4))
  nlinarith only [hi,mul_le_mul_of_nonneg_left h3 hp,hx]

theorem numericCeiling {M κ : ℝ} (h : M^2 ≤ 72*((72*1200^2+1)+1536)*κ^4) :
    M ≤ 86401*κ^2 := by
  by_contra! bad
  have hs := mul_self_lt_mul_self (a := 86401*κ^2)
    (mul_nonneg (by norm_num) (sq_nonneg κ)) bad
  nlinarith only [hs,h,sq_nonneg (κ^2)]

end YangMills.CubicMoment
#print axioms YangMills.CubicMoment.kineticDouble
#print axioms YangMills.CubicMoment.localThird
#print axioms YangMills.CubicMoment.momentInterpolation
#print axioms YangMills.CubicMoment.smallLoss
#print axioms YangMills.CubicMoment.largeLoss
#print axioms YangMills.CubicMoment.uniformSecond
#print axioms YangMills.CubicMoment.numericCeiling
