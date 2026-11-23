import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

noncomputable section
open MeasureTheory
open scoped ComplexConjugate

namespace Millennium.G4.Exterior

variable {X Y Z : Type*} [MeasurableSpace X] [MeasurableSpace Y] [MeasurableSpace Z]

/-- Conditional fibre laws may differ on the two sides of the plane. -/
theorem pairing_of_product (μ : Measure X) (ν : Measure Y) [IsProbabilityMeasure μ]
    [IsProbabilityMeasure ν] (f : X → ℂ) (g : Y → ℂ) :
    (∫ p, conj (f p.1) * g p.2 ∂μ.prod ν) =
      conj (∫ x, f x ∂μ) * (∫ y, g y ∂ν) := by
  rw [integral_prod_mul (fun x => conj (f x)) g, integral_conj]

theorem mean_centered (μ : Measure X) [IsProbabilityMeasure μ]
    (f : X → ℂ) (hf : Integrable f μ) :
    (∫ x, (f x - ∫ u, f u ∂μ) ∂μ) = 0 := by
  rw [integral_sub hf (integrable_const _)]
  simp

theorem centered_pairing_zero (μ : Measure X) (ν : Measure Y) [IsProbabilityMeasure μ]
    [IsProbabilityMeasure ν] (f : X → ℂ) (g : Y → ℂ) (hg : Integrable g ν) :
    (∫ p, conj (f p.1) * (g p.2 - ∫ v, g v ∂ν) ∂μ.prod ν) = 0 := by
  rw [pairing_of_product μ ν f (fun y => g y - ∫ v, g v ∂ν), mean_centered ν g hg,
    mul_zero]

/-- The exterior is reflected as well. Its configuration need not be fixed pointwise. -/
theorem exterior_pairing (η : Measure Z) (μ : Z → Measure X) (ν : Z → Measure Y)
    [∀ z, IsProbabilityMeasure (μ z)] [∀ z, IsProbabilityMeasure (ν z)]
    (r : Z → Z) (f : Z → X → ℂ) (g : Z → Y → ℂ) :
    (∫ z, (∫ p, conj (f (r z) p.1) * g z p.2 ∂(μ z).prod (ν z)) ∂η) =
      ∫ z, conj (∫ x, f (r z) x ∂μ z) * (∫ y, g z y ∂ν z) ∂η := by
  apply integral_congr_ae
  exact Filter.Eventually.of_forall (fun z => pairing_of_product (μ z) (ν z) _ _)

-- NATIVE CHILD 1
/-- A centered Haar reading has a variance floor under any density bounded
below by c. The choice of center m includes the tilted mean. -/
theorem tilted_square_floor (μ : Measure X) [IsProbabilityMeasure μ]
    (f w : X → ℝ) (c m : ℝ) (hc : 0 ≤ c) (hw : ∀ x, c ≤ w x)
    (hf : Integrable f μ) (h2 : Integrable (fun x => f x ^ 2) μ)
    (h0 : (∫ x, f x ∂μ) = 0)
    (ht : Integrable (fun x => w x * (f x - m)^2) μ) :
    c * (∫ x, f x^2 ∂μ) ≤ ∫ x, w x * (f x - m)^2 ∂μ := by
  have hex : (fun x => (f x-m)^2) = fun x => f x^2 - (2*m)*f x + m^2 := by
    funext x
    ring
  have hs : Integrable (fun x => (f x-m)^2) μ := by
    rw [hex]
    exact (h2.sub (hf.const_mul _)).add (integrable_const _)
  have he : (∫ x, (f x-m)^2 ∂μ) = (∫ x, f x^2 ∂μ) + m^2 := by
    have hlin : Integrable (fun x => (2*m)*f x) μ := hf.const_mul _
    have hdiff : Integrable (fun x => f x^2 - (2*m)*f x) μ := h2.sub hlin
    rw [hex, integral_add hdiff (integrable_const (m^2)),
      integral_sub h2 hlin, integral_const_mul, h0]
    simp
  calc
    _ ≤ c * (∫ x, (f x-m)^2 ∂μ) := by rw [he]; nlinarith [mul_nonneg hc (sq_nonneg m)]
    _ = ∫ x, c * (f x-m)^2 ∂μ := (integral_const_mul _ _).symm
    _ ≤ _ := integral_mono (hs.const_mul _) ht
      (fun x => mul_le_mul_of_nonneg_right (hw x) (sq_nonneg _))

/-- Externally equivalent representatives yield the same one-step state when
the original shift respects the quotient. No commutation of shift and P is used. -/
theorem compressed_step {A H : Type*} (q : A → H) (P S : A → A)
    (project : ∀ a, q (P a) = q a)
    (shift : ∀ a b, q a = q b → q (S a) = q (S b)) (a : A) :
    q (P (S (P a))) = q (S a) := by
  rw [project]
  exact shift _ _ (project a)

theorem compressed_steps {A H : Type*} (q : A → H) (P S : A → A)
    (project : ∀ a, q (P a) = q a)
    (shift : ∀ a b, q a = q b → q (S a) = q (S b)) (a : A) (n : ℕ) :
    q (((P ∘ S)^[n]) (P a)) = q ((S^[n]) a) := by
  induction n with
  | zero => exact project a
  | succ n ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
    exact (project _).trans (shift _ _ ih)

-- NATIVE CHILD 2
/-- The reflected norm is bounded below by overlap with a normalized boundary
witness. Inputs can already include the physical normalization and vacuum subtraction. -/
theorem boundary_witness {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (h v : H) (hh : 0 < ‖h‖) :
    ‖@inner ℂ H _ h v‖^2 / ‖h‖^2 ≤ ‖v‖^2 := by
  apply (div_le_iff₀ (sq_pos_of_pos hh)).2
  have bound : ‖@inner ℂ H _ h v‖ ≤ ‖h‖ * ‖v‖ := norm_inner_le_norm h v
  calc
    ‖@inner ℂ H _ h v‖^2 ≤ (‖h‖ * ‖v‖)^2 :=
      pow_le_pow_left₀ (norm_nonneg _) bound 2
    _ = ‖v‖^2 * ‖h‖^2 := by rw [mul_pow, mul_comm]

/-- If spectral weights of total mass M are tested by a contraction bounded
by a < 1 above a window, the two region estimates give a lower window weight. -/
theorem low_window_weight (M inside lo hi a witness : ℝ)
    (ha : a < 1) (hlo : lo ≤ inside) (hhi : hi ≤ a * (M - inside))
    (hw : witness ≤ lo + hi) :
    (witness - a*M) / (1-a) ≤ inside := by
  apply (div_le_iff₀ (sub_pos.mpr ha)).2
  nlinarith

/-- Convert the observed integral of a bounded filter into mass on a
measurable energy window. This works also for measures with an atom at zero. -/
theorem window_mass_of_integral (μ : Measure X) [IsFiniteMeasure μ]
    (s : Set X) (hs : MeasurableSet s) (f : X → ℝ) (hf : Integrable f μ)
    (a W : ℝ) (ha : a < 1) (h1 : ∀ x ∈ s, f x ≤ 1)
    (hrest : ∀ x ∈ sᶜ, f x ≤ a) (hw : W ≤ ∫ x, f x ∂μ) :
    (W - a * μ.real Set.univ) / (1-a) ≤ μ.real s := by
  apply low_window_weight _ _ (∫ x in s, f x ∂μ) (∫ x in sᶜ, f x ∂μ) _ _ ha
  · have h := setIntegral_mono_on hf.integrableOn (integrable_const (1:ℝ)).integrableOn hs h1
    simpa [setIntegral_const] using h
  · have h := setIntegral_mono_on hf.integrableOn (integrable_const a).integrableOn hs.compl hrest
    simpa [setIntegral_const, smul_eq_mul, measureReal_compl hs, mul_comm] using h
  · rwa [integral_add_compl hs hf]

#print axioms pairing_of_product
#print axioms mean_centered
#print axioms centered_pairing_zero
#print axioms exterior_pairing
#print axioms tilted_square_floor
#print axioms compressed_step
#print axioms compressed_steps
#print axioms boundary_witness
#print axioms low_window_weight
#print axioms window_mass_of_integral

end Millennium.G4.Exterior
