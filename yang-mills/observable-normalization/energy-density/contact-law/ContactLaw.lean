import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open Filter MeasureTheory
open scoped Topology

namespace YangMills.ContactLaw

/-- The radial Wilson density is a decreasing tilt of a gamma density. -/
theorem radialTilt (R y : ℝ) (hR : 0 < R) (hy : 0 ≤ y) :
    1-Real.sqrt (max 0 (1-y/(2*R))) ≤ y/(2*R) := by
  let z := 1-y/(2*R)
  have hz : z ≤ 1 := by dsimp [z]; linarith [div_nonneg hy (by positivity : 0 ≤ 2*R)]
  by_cases h : 0 ≤ z
  · have s := Real.sq_sqrt h
    have m := Real.sqrt_nonneg z
    have s₁ : Real.sqrt z ≤ 1 := by nlinarith
    have j := mul_nonneg m (sub_nonneg.mpr s₁)
    change 1-Real.sqrt (max 0 z) ≤ _
    rw [max_eq_right h]
    dsimp [z] at *
    nlinarith only [s,j]
  · change 1-Real.sqrt (max 0 z) ≤ _
    rw [max_eq_left (le_of_not_ge h),Real.sqrt_zero]
    dsimp [z] at h
    linarith

theorem orderedSquaredError {a g : ℝ} (ha : 0 ≤ a) (order : a ≤ g) :
    (g-a)^2 ≤ g^2-a^2 := by nlinarith [mul_nonneg ha (sub_nonneg.mpr order)]

/-- This estimate holds on an arbitrary probability coupling with ordered quantiles. -/
theorem integratedQuantileLoss {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    {d g : Ω → ℝ} (h : ∀ᵐ x ∂μ, 0 ≤ d x ∧ d x ≤ g x)
    (i₁ : Integrable (fun x => (g x-d x)^2) μ)
    (i₂ : Integrable (fun x => (g x)^2) μ) (i₃ : Integrable (fun x => (d x)^2) μ) :
    (∫ x, (g x-d x)^2 ∂μ) ≤ (∫ x, (g x)^2 ∂μ)-(∫ x, (d x)^2 ∂μ) := by
  rw [← integral_sub i₂ i₃]
  exact integral_mono_ae i₁ (i₂.sub i₃) (h.mono (fun _ h => orderedSquaredError h.1 h.2))

/-- A product of conditional characteristic functions can be replaced a factor
at a time, even with a different number of factors in each row. -/
theorem contractionProduct {ι : Type*} (s : Finset ι) (a b : ι → ℂ)
    (ha : ∀ i ∈ s, ‖a i‖ ≤ 1) (hb : ∀ i ∈ s, ‖b i‖ ≤ 1) :
    ‖(∏ i ∈ s, a i)-(∏ i ∈ s, b i)‖ ≤ ∑ i ∈ s, ‖a i-b i‖ := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert j s hj ih =>
    have aa : ∀ i ∈ s, ‖a i‖ ≤ 1 := fun i hi => ha i (Finset.mem_insert_of_mem hi)
    have bb : ∀ i ∈ s, ‖b i‖ ≤ 1 := fun i hi => hb i (Finset.mem_insert_of_mem hi)
    have bp : ‖∏ i ∈ s, b i‖ ≤ 1 := (Finset.norm_prod_le _ _).trans
      (Finset.prod_le_one (fun i _ => norm_nonneg (b i)) bb)
    rw [Finset.prod_insert hj, Finset.prod_insert hj, Finset.sum_insert hj]
    set A := ∏ i ∈ s, a i
    set B := ∏ i ∈ s, b i
    calc
      ‖a j*A-b j*B‖ = ‖(a j-b j)*B+a j*(A-B)‖ := by congr 1; ring
      _ ≤ ‖(a j-b j)*B‖+‖a j*(A-B)‖ := norm_add_le _ _
      _ ≤ ‖a j-b j‖+‖A-B‖ := by
        rw [norm_mul,norm_mul]
        exact add_le_add (mul_le_of_le_one_right (norm_nonneg _) bp)
          (mul_le_of_le_one_left (norm_nonneg _) (ha j (Finset.mem_insert_self _ _)))
      _ ≤ _ := add_le_add_left (ih aa bb) _

theorem triangularLimit {ι : Type*} (rows : ℕ → Finset ι) (a b : ℕ → ι → ℂ)
    (ha : ∀ n, ∀ i ∈ rows n, ‖a n i‖ ≤ 1) (hb : ∀ n, ∀ i ∈ rows n, ‖b n i‖ ≤ 1)
    (err : Tendsto (fun n => ∑ i ∈ rows n, ‖a n i-b n i‖) atTop (𝓝 0)) :
    Tendsto (fun n => ‖(∏ i ∈ rows n, a n i)-(∏ i ∈ rows n, b n i)‖) atTop (𝓝 0) :=
  squeeze_zero (fun _ => norm_nonneg _) (fun n => contractionProduct _ _ _ (ha n) (hb n)) err

/-- A global third-order bound for the one-link characteristic-function
expansion. The constant is deliberately nonoptimal. -/
theorem cubicTaylor (x : ℝ) :
    let z : ℂ := (x:ℂ)*Complex.I
    ‖Complex.exp z-(1+z+z^2/2)‖ ≤ (Real.exp 1+4)*|x|^3 := by
  dsimp only
  set z : ℂ := (x:ℂ)*Complex.I
  have hn : ‖z‖ = |x| := by simp [z]
  have hzero : 0 ≤ |x| := abs_nonneg _
  by_cases hx : |x| ≤ 1
  · have h := Complex.norm_exp_sub_sum_le_norm_mul_exp z 3
    have e : Real.exp |x| ≤ Real.exp 1 := Real.exp_le_exp.mpr hx
    have hs : (∑ m ∈ Finset.range 3, z^m/(m.factorial : ℂ))=1+z+z^2/2 := by
      norm_num [Finset.sum_range_succ, Nat.factorial]
    rw [hs, hn] at h
    exact h.trans (by
      nlinarith only [mul_nonneg (pow_nonneg hzero 3) (sub_nonneg.mpr e), pow_nonneg hzero 3])
  · have he : ‖Complex.exp z‖=1 := Complex.norm_exp_ofReal_mul_I x
    have h := norm_sub_le (Complex.exp z) (1+z+z^2/2)
    have h₁ := norm_add_le (1:ℂ) z
    have h₂ := norm_add_le (1+z) (z^2/2)
    rw [he] at h
    rw [norm_one, hn] at h₁
    rw [norm_div, norm_pow, hn] at h₂
    norm_num at h₂
    have hx₁ : 1 ≤ |x| := le_of_not_ge hx
    have hx₂ := mul_nonneg hzero (sub_nonneg.mpr hx₁)
    have hx₃ := mul_nonneg (sq_nonneg |x|) (sub_nonneg.mpr hx₁)
    have habs := sq_abs x
    nlinarith only [h,h₁,h₂,hx₁,hx₂,hx₃,habs,
      mul_nonneg (Real.exp_pos 1).le (pow_nonneg hzero 3)]

theorem integratedTaylor {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    (x : Ω → ℝ) (z : Ω → ℂ) (hz : ∀ a, z a=(x a:ℂ)*Complex.I)
    (hi : Integrable (fun a => Complex.exp (z a)-(1+z a+(z a)^2/2)) μ)
    (h₃ : Integrable (fun a => |x a|^3) μ) :
    ‖∫ a, Complex.exp (z a)-(1+z a+(z a)^2/2) ∂μ‖ ≤
    (Real.exp 1+4)*∫ a, |x a|^3 ∂μ := by
  rw [← integral_const_mul]
  apply (norm_integral_le_integral_norm _).trans
  apply integral_mono hi.norm (h₃.const_mul _)
  intro a
  dsimp only
  rw [hz a]
  exact cubicTaylor _

theorem perpendicularGram (a b c : ℝ) :
    let m := (a+b+c)/3
    (a-m)^2+(b-m)^2+(c-m)^2=a^2+b^2+c^2-(a+b+c)^2/3 := by dsimp; ring

theorem localGram (a b c v : ℝ) :
    let m := (a+b+c)/3
    (a+b+c)^2/48+v/16*((a-m)^2+(b-m)^2+(c-m)^2) =
    v/16*(a^2+b^2+c^2)+(1-v)/48*(a+b+c)^2 := by dsimp; ring

theorem rowFloor {d : ℝ} (hd : 1/2 ≤ d) (a b c : ℝ) :
    (a^2+b^2+c^2)/32 ≤
      (a+b+c)^2/48+d/16*((a-(a+b+c)/3)^2+(b-(a+b+c)/3)^2+(c-(a+b+c)/3)^2) := by
  have h := mul_nonneg (sub_nonneg.mpr hd)
    (add_nonneg (add_nonneg (sq_nonneg (a-(a+b+c)/3)) (sq_nonneg (b-(a+b+c)/3)))
      (sq_nonneg (c-(a+b+c)/3)))
  nlinarith only [h,sq_nonneg (a+b+c)]

theorem equalWeights (x : ℝ) :
    (x+x+x)^2/12=3*x^2/4 := by ring

theorem gammaThird : (3/2:ℝ)*(5/2)*(7/2)/2=105/16 := by norm_num

end YangMills.ContactLaw
#print axioms YangMills.ContactLaw.radialTilt
#print axioms YangMills.ContactLaw.orderedSquaredError
#print axioms YangMills.ContactLaw.integratedQuantileLoss
#print axioms YangMills.ContactLaw.contractionProduct
#print axioms YangMills.ContactLaw.triangularLimit
#print axioms YangMills.ContactLaw.perpendicularGram
#print axioms YangMills.ContactLaw.localGram
#print axioms YangMills.ContactLaw.rowFloor
#print axioms YangMills.ContactLaw.equalWeights
#print axioms YangMills.ContactLaw.gammaThird
#print axioms YangMills.ContactLaw.cubicTaylor
#print axioms YangMills.ContactLaw.integratedTaylor
