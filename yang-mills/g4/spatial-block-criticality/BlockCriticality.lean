import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

noncomputable section
open MeasureTheory
namespace Millennium.G4.BlockCriticality
open scoped InnerProductSpace

open scoped BigOperators

theorem path_multiplicity {P E : Type*} [Fintype P] [Fintype E]
    (occ : P → E → ℝ)
    (test w : P → ℝ) (amp : E → ℝ) (cap : ℝ)
    (hocc : ∀ p e, 0 ≤ occ p e) (ht : ∀ p, 0 ≤ test p)
    (hc : 0 ≤ cap) (ha : ∀ e, amp e ≤ cap)
    (hlen : ∀ p, (∑ e, occ p e) ≤ w p) :
    (∑ p, test p * (∑ e, occ p e * amp e)) ≤ (∑ p, test p * (w p * cap)) := by
  apply Finset.sum_le_sum
  intro p _
  apply mul_le_mul_of_nonneg_left _ (ht p)
  calc
    (∑ e, occ p e * amp e) ≤ ∑ e, occ p e * cap := by
      apply Finset.sum_le_sum
      intro e _
      exact mul_le_mul_of_nonneg_left (ha e) (hocc p e)
    _ = (∑ e, occ p e) * cap := by rw [← Finset.sum_mul]
    _ ≤ w p * cap := mul_le_mul_of_nonneg_right (hlen p) hc

/-- The derivative of conjugating a rooted face is bounded without requiring
the two colors to commute. -/
theorem commutator_bound {A : Type*} [NormedRing A] (a b : A) :
    ‖a*b - b*a‖ ≤ 2*‖a‖*‖b‖ := by
  calc
    ‖a*b-b*a‖ ≤ ‖a*b‖+‖b*a‖ := norm_sub_le _ _
    _ ≤ ‖a‖*‖b‖+‖b‖*‖a‖ := add_le_add (norm_mul_le _ _) (norm_mul_le _ _)
    _ = 2*‖a‖*‖b‖ := by ring

/-- Summation by parts for the absolute first moment of a first difference
of a symmetric nonincreasing probability profile. -/
theorem symmetric_weighted_difference (p : ℕ → ℝ) (N : ℕ) :
    (∑ j ∈ Finset.range (N+1), (2*(j:ℝ)+1)*(p j-p (j+1))) =
      p 0+2*(∑ j ∈ Finset.range N, p (j+1))-(2*(N:ℝ)+1)*p (N+1) := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]
    push_cast
    ring

-- NATIVE CHILD 1
/-- After charging each spatial traversal, the two phase errors cost at most
a third power of R. The action and closure cost a fourth power. -/
theorem ward_orders (R Y : ℝ) (hR : 1 ≤ R) :
    2*Y*R^4 + 2*Y^2*R^3 ≤ 2*Y*R^4+2*Y^2*R^4 := by
  have h : 0 ≤ R^3 := pow_nonneg (by linarith) _
  nlinarith only [mul_nonneg (sq_nonneg Y) (mul_nonneg h (sub_nonneg.mpr hR))]

theorem cutoff_scale (R c b : ℝ) (hb : 0 < b) (hbnd : R^8 ≤ c^8*b^2) :
    R^4/b ≤ c^4 := by
  apply (div_le_iff₀ hb).2
  apply (sq_le_sq₀ (by positivity) (by positivity)).mp
  calc
    (R^4)^2 = R^8 := by ring
    _ ≤ c^8*b^2 := hbnd
    _ = (c^4*b)^2 := by ring

/-- A spectral measure supported above m has a decaying Laplace reading. -/
theorem spectral_reading (μ : Measure ℝ) [IsProbabilityMeasure μ]
    (R m : ℝ) (hR : 0 ≤ R) (hm : ∀ᵐ E ∂μ, m ≤ E) :
    (∫ E, Real.exp (-R*E) ∂μ) ≤ Real.exp (-R*m) := by
  calc
    (∫ E, Real.exp (-R*E) ∂μ) ≤ ∫ _, Real.exp (-R*m) ∂μ := by
      apply integral_mono_of_nonneg (Filter.Eventually.of_forall (fun _ => (Real.exp_pos _).le))
        (integrable_const _)
      exact hm.mono fun E hE => Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left hE (neg_nonpos.mpr hR))
    _ = Real.exp (-R*m) := by simp

-- NATIVE CHILD 2
theorem gap_upper (R m b : ℝ) (hR : 0 < R) (hb : 0 < b)
    (reading : b ≤ Real.exp (-R*m)) : m ≤ -Real.log b/R := by
  have hl := Real.log_le_log hb reading
  rw [Real.log_exp] at hl
  exact (le_div_iff₀ hR).2 (by linarith)

theorem band_kernel_cap (y : ℝ) : y*(1-y) ≤ 1/4 := by
  nlinarith only [sq_nonneg (y-1/2)]

/-- An observed difference of two normalized lags certifies mass in a
measurable spectral window when its kernel is small outside the window. -/
theorem band_mass (μ : Measure ℝ) [IsProbabilityMeasure μ] (S : Set ℝ)
    (hs : MeasurableSet S) (k : ℝ → ℝ) (δ : ℝ) (hi : Integrable k μ)
    (h : ∀ x, k x ≤ δ + S.indicator (fun _ => (1/4 : ℝ)) x) :
    4*((∫ x, k x ∂μ)-δ) ≤ μ.real S := by
  have hind : Integrable (S.indicator (fun _ => (1/4 : ℝ))) μ :=
    (integrable_const _).indicator hs
  have hle := integral_mono hi ((integrable_const δ).add hind) h
  simp only [Pi.add_apply] at hle
  rw [integral_add (integrable_const δ) hind, integral_indicator hs, setIntegral_const] at hle
  simp only [integral_const, measureReal_univ_eq_one, one_smul, smul_eq_mul] at hle
  linarith

open scoped BigOperators RealInnerProductSpace

theorem harmonic_neighbors_constant {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    {n : ℕ} (center : H) (v : Fin n → H)
    (hmean : (∑ i, v i) = (n : ℝ) • center)
    (hstation : ∀ i, ‖v i‖ ^ 2 = ‖center‖ ^ 2) (i : Fin n) :
    v i = center := by
  have hinner : (∑ j, ⟪v j, center⟫_ℝ) = (n : ℝ) * ‖center‖ ^ 2 := by
    rw [← sum_inner, hmean, real_inner_smul_left, real_inner_self_eq_norm_sq]
  have hconst : (∑ _j : Fin n, ‖center‖ ^ 2) = (n : ℝ) * ‖center‖ ^ 2 := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have hzero : (∑ j, ‖v j - center‖ ^ 2) = 0 := by
    calc
      (∑ j, ‖v j - center‖ ^ 2) =
          ∑ j, 2 * (‖center‖ ^ 2 - ⟪v j, center⟫_ℝ) := by
            apply Finset.sum_congr rfl
            intro j _
            rw [norm_sub_sq_real, hstation j]
            ring
      _ = 0 := by
        rw [← Finset.mul_sum, Finset.sum_sub_distrib, hconst, hinner, sub_self, mul_zero]
  have hle : ‖v i - center‖ ^ 2 ≤ ∑ j, ‖v j - center‖ ^ 2 :=
    Finset.single_le_sum (fun j _ => sq_nonneg ‖v j - center‖) (Finset.mem_univ i)
  rw [hzero] at hle
  have hnorm : ‖v i - center‖ = 0 := by
    nlinarith [norm_nonneg (v i - center)]
  exact sub_eq_zero.mp (norm_eq_zero.mp hnorm)

#print axioms harmonic_neighbors_constant
#print axioms path_multiplicity
#print axioms commutator_bound
#print axioms symmetric_weighted_difference
#print axioms ward_orders
#print axioms cutoff_scale
#print axioms spectral_reading
#print axioms gap_upper
#print axioms band_kernel_cap
#print axioms band_mass

end Millennium.G4.BlockCriticality
