import WilsonReflectionPositivity
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.MeasureTheory.Integral.Prod

noncomputable section

open MeasureTheory
open scoped Topology

namespace Millennium.G4.PeriodicRP

variable {X H K : Type*}
variable [TopologicalSpace X] [CompactSpace X] [SecondCountableTopology X]
variable [MeasurableSpace X] [BorelSpace X]
variable [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
variable [CompactSpace H] [SecondCountableTopology H]
variable [MeasurableSpace H] [BorelSpace H]
variable [NormedAddCommGroup K] [NormedSpace ℝ K] [CompleteSpace K]

def relativeMap (z : (X × H) × (X × H)) : (X × X) × H :=
  ((z.1.1, z.2.1), z.1.2⁻¹ * z.2.2)

theorem continuous_relativeMap :
    Continuous (relativeMap : (X × H) × (X × H) → (X × X) × H) := by
  unfold relativeMap
  exact
    (continuous_fst.fst.prodMk continuous_snd.fst).prodMk
      (continuous_fst.snd.inv.mul continuous_snd.snd)

theorem integral_prod_continuous
    {A B : Type*}
    [TopologicalSpace A] [CompactSpace A] [SecondCountableTopology A]
    [MeasurableSpace A] [BorelSpace A]
    [TopologicalSpace B] [CompactSpace B] [SecondCountableTopology B]
    [MeasurableSpace B] [BorelSpace B]
    (α : Measure A) (β : Measure B)
    [IsFiniteMeasure α] [IsFiniteMeasure β]
    (f : A × B → K) (hf : Continuous f) :
    (∫ z, f z ∂(α.prod β)) = ∫ a, (∫ b, f (a, b) ∂β) ∂α := by
  exact integral_prod f
    (Millennium.G4.IntegralRP.integrable_continuous_compact
      (α.prod β) f hf)

theorem integral_relativeMap
    (μ : Measure X) (η : Measure H)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure η]
    [Measure.IsMulLeftInvariant η]
    (Φ : (X × X) × H → K) (hΦ : Continuous Φ) :
    (∫ z, Φ (relativeMap z) ∂((μ.prod η).prod (μ.prod η))) =
      ∫ z, Φ z ∂((μ.prod μ).prod η) := by
  have hleft (x y : X) (p : H) :
      (∫ q, Φ ((x, y), p⁻¹ * q) ∂η) =
        ∫ h, Φ ((x, y), h) ∂η := by
    let e : H ≃ᵐ H := MeasurableEquiv.mulLeft p⁻¹
    have he : MeasurePreserving e η η := measurePreserving_mul_left η p⁻¹
    change (∫ q, Φ ((x, y), e q) ∂η) = ∫ h, Φ ((x, y), h) ∂η
    exact he.integral_comp' (fun h => Φ ((x, y), h))
  have hfiber (a : X × H) :
      (∫ b, Φ (relativeMap (a, b)) ∂(μ.prod η)) =
        ∫ y, (∫ h, Φ ((a.1, y), h) ∂η) ∂μ := by
    rw [integral_prod_continuous μ η
      (fun b => Φ (relativeMap (a, b)))
      ((hΦ.comp continuous_relativeMap).comp
        (continuous_const.prodMk continuous_id))]
    exact integral_congr_ae (Filter.Eventually.of_forall
      (fun y => hleft a.1 y a.2))
  rw [integral_prod_continuous (μ.prod η) (μ.prod η)
    (fun z => Φ (relativeMap z)) (hΦ.comp continuous_relativeMap)]
  calc
    (∫ a, (∫ b, Φ (relativeMap (a, b)) ∂(μ.prod η)) ∂(μ.prod η)) =
        ∫ a, (∫ y, (∫ h, Φ ((a.1, y), h) ∂η) ∂μ) ∂(μ.prod η) :=
      integral_congr_ae (Filter.Eventually.of_forall hfiber)
    _ = ∫ xy, (∫ h, Φ (xy, h) ∂η) ∂(μ.prod μ) := by
      have hf : Integrable (fun xy : X × X => ∫ h, Φ (xy, h) ∂η)
          (μ.prod μ) :=
        (Millennium.G4.IntegralRP.integrable_continuous_compact
          ((μ.prod μ).prod η) Φ hΦ).integral_prod_left
      rw [integral_fun_fst (μ := μ) (ν := η)
        (fun x : X => ∫ y, (∫ h, Φ ((x,y),h) ∂η) ∂μ), integral_prod _ hf]
      simp
    _ = ∫ z, Φ z ∂((μ.prod μ).prod η) :=
      (integral_prod_continuous (μ.prod μ) η Φ hΦ).symm

theorem integral_relativeMap_tilted
    (μ : Measure X) (η : Measure H)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure η]
    [Measure.IsMulLeftInvariant η]
    (S : (X × X) × H → ℝ) (hS : Continuous S)
    (P : (X × X) × H → ℂ) (hP : Continuous P) :
    (∫ z, P z ∂((μ.prod μ).prod η).tilted S) =
      ∫ z, P (relativeMap z) ∂
        ((μ.prod η).prod (μ.prod η)).tilted (S ∘ relativeMap) := by
  have hweight : Continuous (fun z => Real.exp (S z)) :=
    Real.continuous_exp.comp hS
  have hpartition := integral_relativeMap μ η
    (fun z => Real.exp (S z)) hweight
  have hnum := integral_relativeMap μ η
    (fun z => (Real.exp (S z) : ℂ) * P z)
    ((Complex.continuous_ofReal.comp hweight).mul hP)
  rw [Millennium.G4.WilsonRP.integral_tilted_complex_normalized,
    Millennium.G4.WilsonRP.integral_tilted_complex_normalized]
  change (((∫ z, Real.exp (S z) ∂(μ.prod μ).prod η)⁻¹ : ℝ) : ℂ) *
    (∫ z, (Real.exp (S z) : ℂ) * P z ∂(μ.prod μ).prod η) =
      (((∫ z, Real.exp (S (relativeMap z)) ∂(μ.prod η).prod (μ.prod η))⁻¹ : ℝ) : ℂ) *
        (∫ z, (Real.exp (S (relativeMap z)) : ℂ) * P (relativeMap z)
          ∂(μ.prod η).prod (μ.prod η))
  rw [hpartition, hnum]

#print axioms relativeMap
#print axioms continuous_relativeMap
#print axioms integral_prod_continuous
#print axioms integral_relativeMap
#print axioms integral_relativeMap_tilted

end Millennium.G4.PeriodicRP

end

-- NATIVE CHILD 1
noncomputable section

open scoped BigOperators

namespace Millennium.G4.PeriodicRP

variable {G B C X n : Type*}
variable [Group G] [Fintype C] [Fintype n] [DecidableEq n]

def gaugedBoundary (src dst : C → B) (U : C → X → G)
    (c : C) (z : X × (B → G)) : G :=
  z.2 (src c) * U c z.1 * (z.2 (dst c))⁻¹

def crossingBoundary (src dst : C → B) (U : C → X → G)
    (c : C) (z : (X × X) × (B → G)) : G :=
  U c z.1.1 * z.2 (dst c) * (U c z.1.2)⁻¹ * (z.2 (src c))⁻¹

def crossingExponent (src dst : C → B) (U : C → X → G)
    (β : C → ℝ) (ρ : G →* Matrix.unitaryGroup n ℂ)
    (z : (X × X) × (B → G)) : ℝ :=
  ∑ c, β c * Millennium.G4.WilsonRP.unitaryCharacter ρ
    (crossingBoundary src dst U c z)

theorem gauge_covariance (pₛ p_d qₛ q_d a b : G) :
    (pₛ * a * p_d⁻¹)⁻¹ * (qₛ * b * q_d⁻¹) =
      p_d * (a⁻¹ * ((pₛ⁻¹ * qₛ) * b * (p_d⁻¹ * q_d)⁻¹)) * p_d⁻¹ := by
  group

theorem character_gauged_relative
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (pₛ p_d qₛ q_d a b : G) :
    Millennium.G4.WilsonRP.unitaryCharacter ρ
        ((pₛ * a * p_d⁻¹)⁻¹ * (qₛ * b * q_d⁻¹)) =
      Millennium.G4.WilsonRP.unitaryCharacter ρ
        (a * (p_d⁻¹ * q_d) * b⁻¹ * (pₛ⁻¹ * qₛ)⁻¹) := by
  have hcross :
      a * ((pₛ⁻¹ * qₛ) * b * (p_d⁻¹ * q_d)⁻¹)⁻¹ =
        a * (p_d⁻¹ * q_d) * b⁻¹ * (pₛ⁻¹ * qₛ)⁻¹ := by
    group
  rw [gauge_covariance]
  rw [Millennium.G4.WilsonRP.unitaryCharacter_conjugate]
  rw [← Millennium.G4.WilsonRP.unitaryCharacter_relative ρ
    a ((pₛ⁻¹ * qₛ) * b * (p_d⁻¹ * q_d)⁻¹)]
  rw [hcross]

open Matrix in
theorem trace_relative (ρ : G →* Matrix.unitaryGroup n ℂ)
    (a b : G) :
    (Matrix.trace
      ((ρ a : Matrix n n ℂ)ᴴ * (ρ b : Matrix n n ℂ))).re =
      Millennium.G4.WilsonRP.unitaryCharacter ρ (a⁻¹ * b) := by
  unfold Millennium.G4.WilsonRP.unitaryCharacter
  simp only [map_mul, map_inv, Matrix.UnitaryGroup.mul_val,
    Matrix.UnitaryGroup.inv_val, Matrix.star_eq_conjTranspose]

theorem dot_gaugedBoundary
    (src dst : C → B) (U : C → X → G)
    (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (x y : X) (p q : B → G) :
    let v := Millennium.G4.WilsonRP.matrixFeatures β
      (fun c z => (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ))
    Millennium.G4.WilsonRP.dotKernel v (x, p) (y, q) =
      ∑ c, β c * Millennium.G4.WilsonRP.unitaryCharacter ρ
        (crossingBoundary src dst U c ((x, y), p⁻¹ * q)) := by
  dsimp only
  rw [Millennium.G4.WilsonRP.dot_matrixFeatures β hβ
    (fun c z => (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ))
    (x, p) (y, q)]
  refine Finset.sum_congr rfl ?_
  intro c _
  rw [trace_relative]
  exact congrArg (fun t : ℝ => β c * t)
    (character_gauged_relative ρ
      (p (src c)) (p (dst c)) (q (src c)) (q (dst c))
      (U c x) (U c y))

section Continuity

variable [TopologicalSpace G] [IsTopologicalGroup G] [TopologicalSpace X]

theorem continuous_gaugedBoundary
    (src dst : C → B) (U : C → X → G)
    (hU : ∀ c, Continuous (U c)) (c : C) :
    Continuous (gaugedBoundary src dst U c) := by
  have hs : Continuous (fun z : X × (B → G) => z.2 (src c)) :=
    (continuous_apply (src c)).comp continuous_snd
  have hd : Continuous (fun z : X × (B → G) => z.2 (dst c)) :=
    (continuous_apply (dst c)).comp continuous_snd
  exact (hs.mul ((hU c).comp continuous_fst)).mul hd.inv

theorem continuous_crossingBoundary
    (src dst : C → B) (U : C → X → G)
    (hU : ∀ c, Continuous (U c)) (c : C) :
    Continuous (crossingBoundary src dst U c) := by
  have hs : Continuous (fun z : (X × X) × (B → G) => z.2 (src c)) :=
    (continuous_apply (src c)).comp continuous_snd
  have hd : Continuous (fun z : (X × X) × (B → G) => z.2 (dst c)) :=
    (continuous_apply (dst c)).comp continuous_snd
  have hx : Continuous (fun z : (X × X) × (B → G) => U c z.1.1) :=
    (hU c).comp (continuous_fst.comp continuous_fst)
  have hy : Continuous (fun z : (X × X) × (B → G) => U c z.1.2) :=
    (hU c).comp (continuous_snd.comp continuous_fst)
  exact ((hx.mul hd).mul hy.inv).mul hs.inv

theorem continuous_crossingExponent
    (src dst : C → B) (U : C → X → G)
    (hU : ∀ c, Continuous (U c))
    (β : C → ℝ) (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g : G => (ρ g : Matrix n n ℂ) i j)) :
    Continuous (crossingExponent src dst U β ρ) := by
  have hχ := Millennium.G4.WilsonRP.continuous_unitaryCharacter ρ hρ
  unfold crossingExponent
  refine continuous_finset_sum Finset.univ ?_
  intro c _
  exact continuous_const.mul
    (hχ.comp (continuous_crossingBoundary src dst U hU c))

theorem continuous_gaugedFeatures
    (src dst : C → B) (U : C → X → G)
    (hU : ∀ c, Continuous (U c))
    (β : C → ℝ) (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g : G => (ρ g : Matrix n n ℂ) i j)) :
    ∀ r, Continuous (fun z =>
      Millennium.G4.WilsonRP.matrixFeatures β
        (fun c z => (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ))
        r z) := by
  have hentry (c : C) (i j : n) :
      Continuous (fun z : X × (B → G) =>
        (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ) i j) :=
    (hρ i j).comp (continuous_gaugedBoundary src dst U hU c)
  intro r
  refine Millennium.G4.WilsonRP.continuous_matrixFeatures β
    (fun c z => (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ)) ?_ r
  exact hentry

end Continuity


#print axioms gaugedBoundary
#print axioms crossingBoundary
#print axioms crossingExponent
#print axioms gauge_covariance
#print axioms character_gauged_relative
#print axioms trace_relative
#print axioms dot_gaugedBoundary
#print axioms continuous_gaugedBoundary
#print axioms continuous_crossingBoundary
#print axioms continuous_crossingExponent
#print axioms continuous_gaugedFeatures

end Millennium.G4.PeriodicRP

end

-- NATIVE CHILD 2

namespace Millennium.G4.PeriodicRP
noncomputable section
open MeasureTheory
open scoped BigOperators ComplexConjugate

def seamReflection {X H : Type*} [Group H] (z : (X × X) × H) : (X × X) × H :=
  ((z.1.2,z.1.1),z.2⁻¹)

theorem seamReflection_involutive {X H : Type*} [Group H] :
    Function.Involutive (seamReflection : (X × X) × H → (X × X) × H) := by
  rintro ⟨⟨x,y⟩,h⟩
  simp [seamReflection]

def halfTest {X H : Type*} (F : X → ℂ) (z : (X × X) × H) : ℂ := F z.1.2

def fullExponent {G B C X n : Type*} [Group G] [Fintype C] [Fintype n] [DecidableEq n]
    (src dst : C → B) (U : C → X → G) (β : C → ℝ)
    (ρ : G →* Matrix.unitaryGroup n ℂ) (s : X → ℝ) (z : (X × X) × (B → G)) : ℝ :=
  s z.1.1 + s z.1.2 + crossingExponent src dst U β ρ z

theorem fullExponent_relative_eq_split {G B C X n : Type*} [Group G]
    [Fintype C] [Fintype n] [DecidableEq n]
    (src dst : C → B) (U : C → X → G) (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c)
    (ρ : G →* Matrix.unitaryGroup n ℂ) (s : X → ℝ) :
    fullExponent src dst U β ρ s ∘ relativeMap =
      Millennium.G4.WilsonRP.splitExponent (fun z : X × (B → G) => s z.1)
        (Millennium.G4.WilsonRP.matrixFeatures β
          (fun c z => (ρ (gaugedBoundary src dst U c z) : Matrix n n ℂ))) := by
  funext z
  change s z.1.1 + s z.2.1 + crossingExponent src dst U β ρ (relativeMap z) = _
  unfold Millennium.G4.WilsonRP.splitExponent
  rw [dot_gaugedBoundary src dst U β hβ ρ z.1.1 z.2.1 z.1.2 z.2.2]
  rfl

theorem opposite_seam_character {G n : Type*} [Group G] [Fintype n] [DecidableEq n]
    (ρ : G →* Matrix.unitaryGroup n ℂ) (a b hs hd : G) :
    Millennium.G4.WilsonRP.unitaryCharacter ρ (b * hd⁻¹ * a⁻¹ * hs) =
      Millennium.G4.WilsonRP.unitaryCharacter ρ (a * hd * b⁻¹ * hs⁻¹) := by
  have hgroup : b * hd⁻¹ * a⁻¹ * hs =
      hs⁻¹ * (a * hd * b⁻¹ * hs⁻¹)⁻¹ * (hs⁻¹)⁻¹ := by group
  rw [hgroup, Millennium.G4.WilsonRP.unitaryCharacter_conjugate]
  simpa using Millennium.G4.WilsonRP.unitaryCharacter_relative ρ 1
    (a * hd * b⁻¹ * hs⁻¹)

section Compact
variable {G B C X n : Type*} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [SecondCountableTopology G] [MeasurableSpace G] [BorelSpace G]
  [TopologicalSpace X] [CompactSpace X] [SecondCountableTopology X]
  [MeasurableSpace X] [BorelSpace X]
  [Fintype B] [Fintype C] [Fintype n] [DecidableEq n]

theorem continuous_fullExponent
    (src dst : C → B) (U : C → X → G) (hU : ∀ c, Continuous (U c))
    (β : C → ℝ) (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j))
    (s : X → ℝ) (hs : Continuous s) : Continuous (fullExponent src dst U β ρ s) :=
  ((hs.comp (continuous_fst.comp continuous_fst)).add
    (hs.comp (continuous_snd.comp continuous_fst))).add
      (continuous_crossingExponent src dst U hU β ρ hρ)

/-- Haar averaging retains every boundary variable. No gauge-invariance assumption
is placed on the half action or the half test. -/
theorem boundary_wilson_reflection_positive
    (μ : Measure X) [IsProbabilityMeasure μ]
    (m : Measure G) [IsProbabilityMeasure m] [Measure.IsMulLeftInvariant m]
    (src dst : C → B) (U : C → X → G) (hU : ∀ c, Continuous (U c))
    (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j))
    (s : X → ℝ) (hs : Continuous s) (F : X → ℂ) (hF : Continuous F) :
    let ν := ((μ.prod μ).prod (Measure.pi (fun _ : B => m))).tilted
      (fullExponent src dst U β ρ s)
    IsProbabilityMeasure ν ∧
      Integrable (fun z : (X × X) × (B → G) => conj (F z.1.1) * F z.1.2) ν ∧
      Millennium.G4.ComplexRP.NonnegativeComplex
        (Millennium.G4.IntegralRP.reflectedIntegral ν seamReflection (halfTest F) (halfTest F)) := by
  dsimp only
  let η := Measure.pi (fun _ : B => m)
  let S := fullExponent src dst U β ρ s
  have hS : Continuous S := continuous_fullExponent src dst U hU β ρ hρ s hs
  have hprob := Millennium.G4.IntegralRP.wilson_tilt_probability ((μ.prod μ).prod η) S hS
  have hP : Continuous (fun z : (X × X) × (B → G) => conj (F z.1.1) * F z.1.2) :=
    (Complex.continuous_conj.comp (hF.comp (continuous_fst.comp continuous_fst))).mul
      (hF.comp (continuous_snd.comp continuous_fst))
  refine ⟨hprob, ?_, ?_⟩
  · letI := hprob
    exact Millennium.G4.IntegralRP.integrable_continuous_compact _ _ hP
  · change Millennium.G4.ComplexRP.NonnegativeComplex
      (∫ z, conj (F z.1.1) * F z.1.2 ∂((μ.prod μ).prod η).tilted S)
    rw [integral_relativeMap_tilted μ η S hS _ hP]
    change Millennium.G4.ComplexRP.NonnegativeComplex
      (∫ z, conj (F z.1.1) * F z.2.1 ∂
        ((μ.prod η).prod (μ.prod η)).tilted (fullExponent src dst U β ρ s ∘ relativeMap))
    rw [fullExponent_relative_eq_split src dst U β hβ ρ s]
    exact (Millennium.G4.WilsonRP.split_wilson_reflection_positive (μ.prod η)
      (fun z => s z.1) _ (fun z => F z.1) (hs.comp continuous_fst)
      (continuous_gaugedFeatures src dst U hU β ρ hρ) (hF.comp continuous_fst)).2

end Compact

def twoSeamEndpoint {E V : Type*} (src : E → V) (c : Bool × E) : Bool × V :=
  (c.1,src c.2)

theorem twoSeamEndpoint_distinct {E V : Type*} (src : E → V) (e : E) :
    twoSeamEndpoint src (false,e) ≠ twoSeamEndpoint src (true,e) := by
  simp [twoSeamEndpoint]

/-- At period two both boundary evaluations coincide, while the two tagged
collections of temporal links remain independent under the reference law. -/
theorem periodTwo_reflection_positive {G E V n : Type*} [Group G]
    [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
    [SecondCountableTopology G] [MeasurableSpace G] [BorelSpace G]
    [Fintype E] [Fintype V] [Fintype n] [DecidableEq n]
    (m : Measure G) [IsProbabilityMeasure m] [Measure.IsMulLeftInvariant m]
    (src dst : E → V) (β : Bool × E → ℝ) (hβ : ∀ c, 0 ≤ β c)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j))
    (s : (E → G) → ℝ) (hs : Continuous s) (F : (E → G) → ℂ) (hF : Continuous F) :
    let μ := Measure.pi (fun _ : E => m)
    let ν := ((μ.prod μ).prod (Measure.pi (fun _ : Bool × V => m))).tilted
      (fullExponent (twoSeamEndpoint src) (twoSeamEndpoint dst)
        (fun c U => U c.2) β ρ s)
    IsProbabilityMeasure ν ∧
      Integrable (fun z : ((E → G) × (E → G)) × ((Bool × V) → G) =>
        conj (F z.1.1) * F z.1.2) ν ∧
      Millennium.G4.ComplexRP.NonnegativeComplex
        (Millennium.G4.IntegralRP.reflectedIntegral ν seamReflection (halfTest F) (halfTest F)) := by
  exact boundary_wilson_reflection_positive (Measure.pi (fun _ : E => m)) m
    (twoSeamEndpoint src) (twoSeamEndpoint dst) (fun c U => U c.2)
    (fun c => continuous_apply c.2) β hβ ρ hρ s hs F hF

#print axioms seamReflection
#print axioms seamReflection_involutive
#print axioms halfTest
#print axioms fullExponent
#print axioms fullExponent_relative_eq_split
#print axioms opposite_seam_character
#print axioms continuous_fullExponent
#print axioms boundary_wilson_reflection_positive
#print axioms twoSeamEndpoint
#print axioms twoSeamEndpoint_distinct
#print axioms periodTwo_reflection_positive
end
end Millennium.G4.PeriodicRP
