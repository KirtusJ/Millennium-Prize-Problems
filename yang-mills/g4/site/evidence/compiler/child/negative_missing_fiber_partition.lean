import WilsonReflectionPositivity
import Mathlib.MeasureTheory.Integral.Prod

noncomputable section
open MeasureTheory
open scoped Topology ComplexConjugate

namespace Millennium.G4.SiteRP

variable {Y Q : Type*}
variable [TopologicalSpace Y] [CompactSpace Y] [SecondCountableTopology Y]
variable [MeasurableSpace Y] [BorelSpace Y]
variable [TopologicalSpace Q] [CompactSpace Q] [SecondCountableTopology Q]
variable [MeasurableSpace Q] [BorelSpace Q]

def fiberPartition (μ : Measure Q) (S : Y × Q → ℝ) (y : Y) : ℝ :=
  ∫ q, Real.exp (S (y, q)) ∂μ

def totalPartition (η : Measure Y) (μ : Measure Q) (S : Y × Q → ℝ) : ℝ :=
  ∫ z, Real.exp (S z) ∂(η.prod μ)

def boundaryDensity (η : Measure Y) (μ : Measure Q) (S : Y × Q → ℝ) (y : Y) : ℝ :=
  1 / totalPartition η μ S

def fiberExpectation (μ : Measure Q) (S : Y × Q → ℝ) (P : Y × Q → ℂ) (y : Y) : ℂ :=
  ∫ q, P (y, q) ∂μ.tilted (fun q => S (y, q))

variable (η : Measure Y) (μ : Measure Q)
variable [IsProbabilityMeasure η] [IsProbabilityMeasure μ]
variable (S : Y × Q → ℝ) (hS : Continuous S)
include hS

theorem fiberPartition_pos (y : Y) : 0 < fiberPartition μ S y :=
  Millennium.G4.IntegralRP.wilson_partition_pos μ _
    (hS.comp (continuous_const.prodMk continuous_id))

theorem totalPartition_pos : 0 < totalPartition η μ S :=
  Millennium.G4.IntegralRP.wilson_partition_pos (η.prod μ) S hS

theorem boundaryDensity_pos (y : Y) : 0 < boundaryDensity η μ S y :=
  div_pos (fiberPartition_pos μ S hS y) (totalPartition_pos η μ S hS)

theorem integral_fiberPartition : (∫ y, fiberPartition μ S y ∂η) = totalPartition η μ S := by
  exact (integral_prod _ (Millennium.G4.IntegralRP.integrable_continuous_compact
    (η.prod μ) _ (Real.continuous_exp.comp hS))).symm

theorem boundaryDensity_integrable : Integrable (boundaryDensity η μ S) η := by
  exact (Millennium.G4.IntegralRP.integrable_continuous_compact
    (η.prod μ) _ (Real.continuous_exp.comp hS)).integral_prod_left.div_const _

theorem integral_boundaryDensity : (∫ y, boundaryDensity η μ S y ∂η) = 1 := by
  simp only [boundaryDensity, integral_div, integral_fiberPartition η μ S hS]
  exact div_self (ne_of_gt (totalPartition_pos η μ S hS))

-- NATIVE CHILD 1

theorem weighted_fiberExpectation (P : Y × Q → ℂ) (y : Y) :
    (boundaryDensity η μ S y : ℂ) * fiberExpectation μ S P y =
      ((totalPartition η μ S)⁻¹ : ℝ) *
        (∫ q, (Real.exp (S (y, q)) : ℂ) * P (y, q) ∂μ) := by
  unfold boundaryDensity fiberExpectation
  rw [Millennium.G4.WilsonRP.integral_tilted_complex_normalized]
  change ((fiberPartition μ S y / totalPartition η μ S : ℝ) : ℂ) *
    (((fiberPartition μ S y)⁻¹ : ℝ) * _) = _
  have hz : (fiberPartition μ S y : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (ne_of_gt (fiberPartition_pos μ S hS y))
  have ht : (totalPartition η μ S : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (ne_of_gt (totalPartition_pos η μ S hS))
  rw [Complex.ofReal_div, Complex.ofReal_inv, Complex.ofReal_inv]
  field_simp [hz, ht]
  <;> ring

theorem weighted_fiberExpectation_integrable
    (P : Y × Q → ℂ) (hP : Continuous P) :
    Integrable (fun y => (boundaryDensity η μ S y : ℂ) * fiberExpectation μ S P y) η := by
  have hi := (Millennium.G4.IntegralRP.integrable_continuous_compact
    (η.prod μ) (fun z => (Real.exp (S z) : ℂ) * P z)
    ((Complex.continuous_ofReal.comp (Real.continuous_exp.comp hS)).mul hP)).integral_prod_left
  have he : (fun y => (boundaryDensity η μ S y : ℂ) * fiberExpectation μ S P y) =
      (fun y => (((totalPartition η μ S)⁻¹ : ℝ) : ℂ) *
        (∫ q, (Real.exp (S (y, q)) : ℂ) * P (y, q) ∂μ)) :=
    funext (weighted_fiberExpectation η μ S hS P)
  rw [he]
  exact hi.const_mul _

theorem normalized_boundary_mixture
    (P : Y × Q → ℂ) (hP : Continuous P) :
    (∫ z, P z ∂(η.prod μ).tilted S) =
      ∫ y, (boundaryDensity η μ S y : ℂ) * fiberExpectation μ S P y ∂η := by
  rw [Millennium.G4.WilsonRP.integral_tilted_complex_normalized]
  rw [integral_prod (fun z => (Real.exp (S z) : ℂ) * P z)
    (Millennium.G4.IntegralRP.integrable_continuous_compact
      (η.prod μ) _ ((Complex.continuous_ofReal.comp (Real.continuous_exp.comp hS)).mul hP))]
  rw [← integral_const_mul]
  exact integral_congr_ae (Filter.Eventually.of_forall
    (fun y => (weighted_fiberExpectation η μ S hS P y).symm))

omit hS in
theorem nonnegativeComplex_integral {A : Type*} [MeasurableSpace A]
    (ν : Measure A) (f : A → ℂ) (hf : Integrable f ν)
    (h : ∀ a, Millennium.G4.ComplexRP.NonnegativeComplex (f a)) :
    Millennium.G4.ComplexRP.NonnegativeComplex (∫ a, f a ∂ν) := by
  constructor
  · have hi := integral_im hf
    change (∫ a, (f a).im ∂ν) = (∫ a, f a ∂ν).im at hi
    rw [← hi]
    have hz : (fun a => (f a).im) = (fun _ => (0 : ℝ)) := funext (fun a => (h a).1)
    rw [hz, integral_zero]
  · have hr := integral_re hf
    change (∫ a, (f a).re ∂ν) = (∫ a, f a ∂ν).re at hr
    rw [← hr]
    exact integral_nonneg (fun a => (h a).2)

-- NATIVE CHILD 2

theorem shared_boundary_nonnegative
    (P : Y × Q → ℂ) (hP : Continuous P)
    (hfiber : ∀ y, Millennium.G4.ComplexRP.NonnegativeComplex (fiberExpectation μ S P y)) :
    Millennium.G4.ComplexRP.NonnegativeComplex (∫ z, P z ∂(η.prod μ).tilted S) := by
  rw [normalized_boundary_mixture η μ S hS P hP]
  apply nonnegativeComplex_integral η _ (weighted_fiberExpectation_integrable η μ S hS P hP)
  intro y
  constructor
  · simp [Complex.mul_im, (hfiber y).1]
  · simpa [Complex.mul_re] using
      mul_nonneg (boundaryDensity_pos η μ S hS y).le (hfiber y).2

def sharedReflection (θ : Y → Q → Q) (z : Y × Q) : Y × Q := (z.1, θ z.1 z.2)

theorem shared_boundary_reflection_positive
    (θ : Y → Q → Q) (hθ : Continuous (sharedReflection θ))
    (F : Y × Q → ℂ) (hF : Continuous F)
    (hfiber : ∀ y, Millennium.G4.ComplexRP.NonnegativeComplex
      (Millennium.G4.IntegralRP.reflectedIntegral
        (μ.tilted (fun q => S (y, q))) (θ y) (fun q => F (y, q)) (fun q => F (y, q)))) :
    IsProbabilityMeasure ((η.prod μ).tilted S) ∧
      Integrable (fun z => conj (F (sharedReflection θ z)) * F z) ((η.prod μ).tilted S) ∧
      Millennium.G4.ComplexRP.NonnegativeComplex
        (Millennium.G4.IntegralRP.reflectedIntegral ((η.prod μ).tilted S)
          (sharedReflection θ) F F) := by
  have hP : Continuous (fun z => conj (F (sharedReflection θ z)) * F z) :=
    (Complex.continuous_conj.comp (hF.comp hθ)).mul hF
  letI : IsProbabilityMeasure ((η.prod μ).tilted S) :=
    Millennium.G4.IntegralRP.wilson_tilt_probability (η.prod μ) S hS
  refine ⟨inferInstance, Millennium.G4.IntegralRP.integrable_continuous_compact _ _ hP, ?_⟩
  exact shared_boundary_nonnegative η μ S hS _ hP hfiber

omit hS in
theorem rooted_reversal {G : Type*} [Group G] (r e p : G) :
    r * (e⁻¹ * p⁻¹ * e) * r⁻¹ = ((r * e⁻¹) * p * (r * e⁻¹)⁻¹)⁻¹ := by
  group

#print axioms fiberPartition
#print axioms totalPartition
#print axioms boundaryDensity
#print axioms fiberExpectation
#print axioms fiberPartition_pos
#print axioms totalPartition_pos
#print axioms boundaryDensity_pos
#print axioms integral_fiberPartition
#print axioms boundaryDensity_integrable
#print axioms integral_boundaryDensity
#print axioms weighted_fiberExpectation
#print axioms weighted_fiberExpectation_integrable
#print axioms normalized_boundary_mixture
#print axioms nonnegativeComplex_integral
#print axioms shared_boundary_nonnegative
#print axioms sharedReflection
#print axioms shared_boundary_reflection_positive
#print axioms rooted_reversal

end Millennium.G4.SiteRP
