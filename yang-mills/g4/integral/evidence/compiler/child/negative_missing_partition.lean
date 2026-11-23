import ComplexReflectionPositivity
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Function.LocallyIntegrable
import Mathlib.MeasureTheory.Measure.Tilted
import Mathlib.MeasureTheory.Constructions.Pi
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.MeasureTheory.Integral.Prod

namespace Millennium.G4.IntegralRP

universe vtest

noncomputable section

open Filter MeasureTheory
open scoped BigOperators Topology ComplexConjugate



variable {X Y A ι : Type*}

def reflectedIntegral [MeasurableSpace X] (μ : Measure X)
    (theta : X → X) (F G : X → ℂ) : ℂ :=
  ∫ x, (starRingEnd ℂ) (F (theta x)) * G x ∂μ

def integralKernel [MeasurableSpace X] (μ : Measure X)
    (theta : X → X) (f : A → X → ℂ) (a b : A) : ℂ :=
  reflectedIntegral μ theta (f a) (f b)

def finiteTest [Fintype ι] (f : A → X → ℂ)
    (idx : ι → A) (c : ι → ℂ) (x : X) : ℂ :=
  ∑ i, c i * f (idx i) x

theorem finiteTest_reflected_product [Fintype ι]
    (theta : X → X) (f : A → X → ℂ)
    (idx : ι → A) (c d : ι → ℂ) (x : X) :
    (starRingEnd ℂ) (finiteTest f idx c (theta x)) * finiteTest f idx d x =
      ∑ i, ∑ j, ((starRingEnd ℂ) (c i) * d j) *
        ((starRingEnd ℂ) (f (idx i) (theta x)) * f (idx j) x) := by
  classical
  unfold finiteTest
  rw [map_sum, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro i hi
  rw [map_mul, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  ac_rfl

theorem integrable_finiteTest_reflected_product
    [MeasurableSpace X] [Fintype ι] (μ : Measure X)
    (theta : X → X) (f : A → X → ℂ)
    (idx : ι → A) (c d : ι → ℂ)
    (hpair : ∀ i j, Integrable
      (fun x => (starRingEnd ℂ) (f (idx i) (theta x)) * f (idx j) x) μ) :
    Integrable (fun x =>
      (starRingEnd ℂ) (finiteTest f idx c (theta x)) * finiteTest f idx d x) μ := by
  classical
  simp only [finiteTest_reflected_product]
  apply integrable_finset_sum
  intro i hi
  apply integrable_finset_sum
  intro j hj
  exact (hpair i j).const_mul ((starRingEnd ℂ) (c i) * d j)

theorem reflectedIntegral_finiteTest
    [MeasurableSpace X] [Fintype ι] (μ : Measure X)
    (theta : X → X) (f : A → X → ℂ)
    (idx : ι → A) (c d : ι → ℂ)
    (hpair : ∀ i j, Integrable
      (fun x => (starRingEnd ℂ) (f (idx i) (theta x)) * f (idx j) x) μ) :
    reflectedIntegral μ theta (finiteTest f idx c) (finiteTest f idx d) =
      Millennium.G4.ComplexRP.pairing (integralKernel μ theta f) idx c d := by
  classical
  let g : ι → ι → X → ℂ := fun i j x =>
    ((starRingEnd ℂ) (c i) * d j) *
      ((starRingEnd ℂ) (f (idx i) (theta x)) * f (idx j) x)
  have hg (i j : ι) : Integrable (g i j) μ :=
    (hpair i j).const_mul ((starRingEnd ℂ) (c i) * d j)
  have hrow (i : ι) : Integrable (fun x => ∑ j, g i j x) μ :=
    integrable_finset_sum Finset.univ (fun j _ => hg i j)
  calc
    reflectedIntegral μ theta (finiteTest f idx c) (finiteTest f idx d) =
        ∫ x, (∑ i, ∑ j, g i j x) ∂μ := by
          simp only [reflectedIntegral, finiteTest_reflected_product, g]
    _ = ∑ i, ∫ x, (∑ j, g i j x) ∂μ :=
      integral_finset_sum Finset.univ (fun i _ => hrow i)
    _ = ∑ i, ∑ j, ∫ x, g i j x ∂μ := by
      apply Finset.sum_congr rfl
      intro i hi
      exact integral_finset_sum Finset.univ (fun j _ => hg i j)
    _ = Millennium.G4.ComplexRP.pairing (integralKernel μ theta f) idx c d := by
      unfold Millennium.G4.ComplexRP.pairing
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      exact integral_const_mul _ _

-- NATIVE CHILD 1

/-- Configuration spaces and measures may vary; the finite test labels are common. -/
theorem integral_regulator_limit {I : Type*} {Ω : ℕ → Type*}
    [∀ n, MeasurableSpace (Ω n)] (μ : ∀ n, Measure (Ω n))
    (theta : ∀ n, Ω n → Ω n) (f : ∀ n, I → Ω n → ℂ) (L : I → I → ℂ)
    (hpair : ∀ n a b, Integrable
      (fun x => (starRingEnd ℂ) (f n a (theta n x)) * f n b x) (μ n))
    (hK : ∀ a b, Tendsto
      (fun n => integralKernel (μ n) (theta n) (f n) a b) atTop (𝓝 (L a b)))
    (hpos : ∀ (J : Type vtest) [Fintype J] (idx : J → I) (c : J → ℂ),
      ∀ᶠ n in atTop, Millennium.G4.ComplexRP.NonnegativeComplex
        (reflectedIntegral (μ n) (theta n)
          (finiteTest (f n) idx c) (finiteTest (f n) idx c))) :
    ∀ (J : Type vtest) [Fintype J] (idx : J → I) (c : J → ℂ),
      Millennium.G4.ComplexRP.NonnegativeComplex (Millennium.G4.ComplexRP.Q L idx c) := by
  intro J _ idx c
  apply Millennium.G4.ComplexRP.Q_nonnegative_of_entrywise_tendsto hK idx c
  filter_upwards [hpos J idx c] with n hn
  simpa only [reflectedIntegral_finiteTest (μ n) (theta n) (f n) idx c c
    (fun i j => hpair n (idx i) (idx j)), Millennium.G4.ComplexRP.Q] using hn

theorem reflectedIntegral_map [MeasurableSpace X] [MeasurableSpace Y]
    (μ : Measure X) (q : X → Y) (thetaX : X → X) (thetaY : Y → Y)
    (F G : Y → ℂ) (hq : Measurable q)
    (hcomm : ∀ x, q (thetaX x) = thetaY (q x))
    (hprod : AEStronglyMeasurable
      (fun y => (starRingEnd ℂ) (F (thetaY y)) * G y) (Measure.map q μ)) :
    reflectedIntegral (Measure.map q μ) thetaY F G =
      reflectedIntegral μ thetaX (F ∘ q) (G ∘ q) := by
  simpa only [reflectedIntegral, Function.comp_apply, hcomm] using
    (integral_map hq.aemeasurable hprod)

theorem integrable_reflectedProduct_map_iff
    [MeasurableSpace X] [MeasurableSpace Y]
    (μ : Measure X) (q : X → Y) (thetaX : X → X) (thetaY : Y → Y)
    (F G : Y → ℂ) (hq : Measurable q)
    (hcomm : ∀ x, q (thetaX x) = thetaY (q x))
    (hprod : AEStronglyMeasurable
      (fun y => (starRingEnd ℂ) (F (thetaY y)) * G y) (Measure.map q μ)) :
    Integrable (fun y => (starRingEnd ℂ) (F (thetaY y)) * G y)
        (Measure.map q μ) ↔
      Integrable (fun x => (starRingEnd ℂ) (F (q (thetaX x))) * G (q x)) μ := by
  simpa only [Function.comp_apply, hcomm] using
    (integrable_map_measure hprod hq.aemeasurable)

theorem reflectedIntegral_map_nonnegative
    [MeasurableSpace X] [MeasurableSpace Y]
    (μ : Measure X) (q : X → Y) (thetaX : X → X) (thetaY : Y → Y)
    (F : Y → ℂ) (hq : Measurable q)
    (hcomm : ∀ x, q (thetaX x) = thetaY (q x))
    (hprod : Integrable
      (fun y => (starRingEnd ℂ) (F (thetaY y)) * F y) (Measure.map q μ))
    (hpull : Millennium.G4.ComplexRP.NonnegativeComplex
      (reflectedIntegral μ thetaX (F ∘ q) (F ∘ q))) :
    Millennium.G4.ComplexRP.NonnegativeComplex (reflectedIntegral (Measure.map q μ) thetaY F F) := by
  rw [reflectedIntegral_map μ q thetaX thetaY F F hq hcomm
    hprod.aestronglyMeasurable]
  exact hpull

theorem integrable_continuous_compact
    {V : Type*} [NormedAddCommGroup V]
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] (g : X → V) (hg : Continuous g) :
    Integrable g μ := by
  have h : IntegrableOn g (Set.univ : Set X) μ :=
    hg.continuousOn.integrableOn_compact' isCompact_univ MeasurableSet.univ
  simpa only [IntegrableOn, Measure.restrict_univ] using h

theorem integrable_reflectedProduct_continuous
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] (theta : X → X) (F G : X → ℂ)
    (htheta : Continuous theta) (hF : Continuous F) (hG : Continuous G) :
    Integrable (fun x => (starRingEnd ℂ) (F (theta x)) * G x) μ :=
  integrable_continuous_compact μ _
    ((Complex.continuous_conj.comp (hF.comp htheta)).mul hG)

theorem reflectedIntegral_finiteTest_continuous
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    [Fintype ι] (μ : Measure X) [IsFiniteMeasure μ]
    (theta : X → X) (f : A → X → ℂ) (idx : ι → A) (c d : ι → ℂ)
    (htheta : Continuous theta) (hf : ∀ i, Continuous (f (idx i))) :
    reflectedIntegral μ theta (finiteTest f idx c) (finiteTest f idx d) =
      Millennium.G4.ComplexRP.pairing (integralKernel μ theta f) idx c d :=
  reflectedIntegral_finiteTest μ theta f idx c d (fun i j =>
    integrable_reflectedProduct_continuous μ theta (f (idx i)) (f (idx j))
      htheta (hf i) (hf j))

-- NATIVE CHILD 2

theorem integrable_wilson_exp
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] (S : X → ℝ) (hS : Continuous S) :
    Integrable (fun x => Real.exp (S x)) μ :=
  integrable_continuous_compact μ _ (Real.continuous_exp.comp hS)

theorem wilson_partition_pos
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S) :
    0 < ∫ x, Real.exp (S x) ∂μ :=
  integral_exp_pos (integrable_wilson_exp μ S hS)

theorem wilson_tilt_probability
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S) :
    IsProbabilityMeasure (μ.tilted S) :=
  isProbabilityMeasure_tilted (integrable_wilson_exp μ S hS)

theorem integrable_reflectedProduct_wilson_tilt
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S)
    (theta : X → X) (F G : X → ℂ)
    (htheta : Continuous theta) (hF : Continuous F) (hG : Continuous G) :
    Integrable (fun x => (starRingEnd ℂ) (F (theta x)) * G x) (μ.tilted S) := by
  letI : IsProbabilityMeasure (μ.tilted S) := wilson_tilt_probability μ S hS
  exact integrable_reflectedProduct_continuous (μ.tilted S) theta F G htheta hF hG

theorem reflectedIntegral_tilted_density
    [MeasurableSpace X] (μ : Measure X)
    (S : X → ℝ) (theta : X → X) (F G : X → ℂ) :
    reflectedIntegral (μ.tilted S) theta F G =
      ∫ x, Real.exp (S x) •
        ((starRingEnd ℂ) (F (theta x)) * G x) ∂μ := by
  unfold reflectedIntegral
  exact integral_tilted S _

theorem reflectedIntegral_wilson_one
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S) (theta : X → X) :
    reflectedIntegral (μ.tilted S) theta (fun _ => 1) (fun _ => 1) = 1 := by
  letI : IsProbabilityMeasure (μ.tilted S) := wilson_tilt_probability μ S hS
  simp [reflectedIntegral, integral_const]

theorem wilson_action_continuous
    {P : Type*} [TopologicalSpace X] (plaquettes : Finset P)
    (β : P → ℝ) (φ : P → X → ℝ)
    (hφ : ∀ p ∈ plaquettes, Continuous (φ p)) :
    Continuous (fun x => ∑ p ∈ plaquettes, β p * φ p x) := by
  exact continuous_finset_sum _ (fun p hp => continuous_const.mul (hφ p hp))

theorem wilson_link_tilt_probability
    {E G : Type*} [Fintype E] [TopologicalSpace G] [CompactSpace G]
    [SecondCountableTopology G] [MeasurableSpace G] [BorelSpace G]
    (baseLaw : Measure G) [IsProbabilityMeasure baseLaw]
    (S : (E → G) → ℝ) (hS : Continuous S) :
    IsProbabilityMeasure ((Measure.pi (fun _ : E => baseLaw)).tilted S) := by
  classical
  letI : IsProbabilityMeasure (Measure.pi (fun _ : E => baseLaw)) := inferInstance
  exact wilson_tilt_probability (Measure.pi (fun _ : E => baseLaw)) S hS

theorem tilted_vacuity
    [MeasurableSpace X] (μ : Measure X) (S : X → ℝ)
    (h : ¬ Integrable (fun x => Real.exp (S x)) μ) :
    μ.tilted S = 0 :=
  tilted_of_not_integrable h

theorem reflectedIntegral_tilted_vacuity
    [MeasurableSpace X] (μ : Measure X) (S : X → ℝ)
    (theta : X → X) (F G : X → ℂ)
    (h : ¬ Integrable (fun x => Real.exp (S x)) μ) :
    reflectedIntegral (μ.tilted S) theta F G = 0 := by
  rw [tilted_vacuity μ S h]
  simp [reflectedIntegral]

theorem reflectedIntegral_wilson_const_I
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S) (theta : X → X) :
    reflectedIntegral (μ.tilted S) theta
      (fun _ => Complex.I) (fun _ => Complex.I) = 1 := by
  letI : IsProbabilityMeasure (μ.tilted S) := wilson_tilt_probability μ S hS
  have hI : (starRingEnd ℂ) Complex.I * Complex.I = (1 : ℂ) := by
    apply Complex.ext <;> simp [Complex.mul_re, Complex.mul_im]
  simp [reflectedIntegral, hI, integral_const]

theorem wilson_const_I_without_conjugation
    [TopologicalSpace X] [CompactSpace X] [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsFiniteMeasure μ] [NeZero μ]
    (S : X → ℝ) (hS : Continuous S) :
    (∫ _ : X, Complex.I * Complex.I ∂(μ.tilted S)) = (-1 : ℂ) := by
  letI : IsProbabilityMeasure (μ.tilted S) := wilson_tilt_probability μ S hS
  simp [Complex.I_mul_I, integral_const]

variable {X R : Type*} [MeasurableSpace X] [Fintype R]

theorem integral_gram_rank_one
    (μ : Measure X) (a : ℝ) (u : X → ℂ) (hu : Integrable u μ) :
    (∫ x, (∫ y, (a : ℂ) * conj (u x) * u y ∂μ) ∂μ) =
      ((a * Complex.normSq (∫ x, u x ∂μ) : ℝ) : ℂ) := by
  calc
    (∫ x, (∫ y, (a : ℂ) * conj (u x) * u y ∂μ) ∂μ) =
        ∫ x, ((a : ℂ) * conj (u x)) * (∫ y, u y ∂μ) ∂μ := by
          apply integral_congr_ae
          exact Filter.Eventually.of_forall fun x =>
            integral_const_mul ((a : ℂ) * conj (u x)) u
    _ = (a : ℂ) * conj (∫ x, u x ∂μ) * (∫ x, u x ∂μ) := by
          rw [integral_mul_const, integral_const_mul, integral_conj]
    _ = ((a * Complex.normSq (∫ x, u x ∂μ) : ℝ) : ℂ) := by
          rw [Complex.ofReal_mul, Complex.normSq_eq_conj_mul_self, mul_assoc]

theorem integral_gram_sum
    (μ : Measure X) (a : R → ℝ) (u : R → X → ℂ)
    (hu : ∀ r, Integrable (u r) μ) :
    (∫ x, (∫ y, ∑ r, (a r : ℂ) * conj (u r x) * u r y ∂μ) ∂μ) =
      ∑ r, ((a r * Complex.normSq (∫ x, u r x ∂μ) : ℝ) : ℂ) := by
  classical
  have hconj (r : R) : Integrable (fun x => conj (u r x)) μ := by
    refine (hu r).norm.mono' ?_ ?_
    · exact Complex.continuous_conj.comp_aestronglyMeasurable
        (hu r).aestronglyMeasurable
    · exact Filter.Eventually.of_forall fun x => by simp
  have hinner (x : X) (r : R) :
      Integrable (fun y => (a r : ℂ) * conj (u r x) * u r y) μ :=
    (hu r).const_mul ((a r : ℂ) * conj (u r x))
  have houter (r : R) :
      Integrable (fun x => ∫ y, (a r : ℂ) * conj (u r x) * u r y ∂μ) μ := by
    have h :
        Integrable
          (fun x => ((a r : ℂ) * conj (u r x)) * (∫ y, u r y ∂μ)) μ :=
      ((hconj r).const_mul (a r : ℂ)).mul_const (∫ y, u r y ∂μ)
    convert h using 1
    funext x
    exact integral_const_mul ((a r : ℂ) * conj (u r x)) (u r)
  calc
    (∫ x, (∫ y, ∑ r, (a r : ℂ) * conj (u r x) * u r y ∂μ) ∂μ) =
        ∫ x, ∑ r, (∫ y, (a r : ℂ) * conj (u r x) * u r y ∂μ) ∂μ := by
          apply integral_congr_ae
          exact Filter.Eventually.of_forall fun x =>
            integral_finset_sum Finset.univ (fun r _ => hinner x r)
    _ = ∑ r, (∫ x, (∫ y, (a r : ℂ) * conj (u r x) * u r y ∂μ) ∂μ) :=
          integral_finset_sum Finset.univ (fun r _ => houter r)
    _ = ∑ r, ((a r * Complex.normSq (∫ x, u r x ∂μ) : ℝ) : ℂ) := by
          exact Finset.sum_congr rfl fun r _ =>
            integral_gram_rank_one μ (a r) (u r) (hu r)

theorem integral_gram_nonnegative
    (μ : Measure X) (a : R → ℝ) (u : R → X → ℂ)
    (ha : ∀ r, 0 ≤ a r) (hu : ∀ r, Integrable (u r) μ) :
    Millennium.G4.ComplexRP.NonnegativeComplex
      (∫ x, (∫ y, ∑ r, (a r : ℂ) * conj (u r x) * u r y ∂μ) ∂μ) := by
  classical
  rw [integral_gram_sum μ a u hu, ← Complex.ofReal_sum]
  constructor
  · exact Complex.ofReal_im _
  · rw [Complex.ofReal_re]
    exact Finset.sum_nonneg fun r _ =>
      mul_nonneg (ha r) (Complex.normSq_nonneg _)

theorem integral_prod_gram_nonnegative
    (μ : Measure X) [SFinite μ] (a : R → ℝ) (u : R → X → ℂ)
    (ha : ∀ r, 0 ≤ a r) (hu : ∀ r, Integrable (u r) μ)
    (hjoint : Integrable
      (fun p : X × X => ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2)
      (μ.prod μ)) :
    Millennium.G4.ComplexRP.NonnegativeComplex
      (∫ p : X × X, ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2
        ∂(μ.prod μ)) := by
  rw [integral_prod _ hjoint]
  exact integral_gram_nonnegative μ a u ha hu


#print axioms integral_gram_rank_one
/-- Positive normalization is additional to Gram positivity. -/
theorem normalized_integral_gram_nonnegative
    (μ : Measure X) [SFinite μ] (Z : ℝ) (hZ : 0 < Z)
    (a : R → ℝ) (u : R → X → ℂ)
    (ha : ∀ r, 0 ≤ a r) (hu : ∀ r, Integrable (u r) μ)
    (hjoint : Integrable
      (fun p : X × X => ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2)
      (μ.prod μ)) :
    Millennium.G4.ComplexRP.NonnegativeComplex
      (((Z⁻¹ : ℝ) : ℂ) * (∫ p : X × X,
        ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2 ∂(μ.prod μ))) := by
  obtain ⟨hi, hr⟩ := integral_prod_gram_nonnegative μ a u ha hu hjoint
  constructor
  · simp [Complex.mul_im, hi]
  · simpa [Complex.mul_re] using mul_nonneg (inv_nonneg.mpr (le_of_lt hZ)) hr

/-- Conditional Wilson RP: the tested Boltzmann density must have this Gram form.
Compact continuity supplies a real finite positive partition, but not the factorization. -/
theorem reflectedIntegral_wilson_of_gram
    [TopologicalSpace X] [CompactSpace X] [SecondCountableTopology X] [BorelSpace X]
    (μ : Measure X) [IsProbabilityMeasure μ]
    (S : (X × X) → ℝ) (hS : Continuous S) (F : X → ℂ) (hF : Continuous F)
    (a : R → ℝ) (u : R → X → ℂ)
    (ha : ∀ r, 0 ≤ a r) (hu : ∀ r, Integrable (u r) μ)
    (hjoint : Integrable
      (fun p : X × X => ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2)
      (μ.prod μ))
    (hfactor : ∀ p : X × X,
      (Real.exp (S p) : ℂ) * (conj (F p.1) * F p.2) =
        ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2) :
    Integrable (fun p : X × X => conj (F p.1) * F p.2) ((μ.prod μ).tilted S) ∧
    Millennium.G4.ComplexRP.NonnegativeComplex
      (reflectedIntegral ((μ.prod μ).tilted S) Prod.swap
        (fun p => F p.2) (fun p => F p.2)) := by
  have heq : reflectedIntegral ((μ.prod μ).tilted S) Prod.swap
        (fun p => F p.2) (fun p => F p.2) =
      ((((∫ p, Real.exp (S p) ∂(μ.prod μ))⁻¹ : ℝ) : ℂ) *
        (∫ p : X × X, ∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2 ∂(μ.prod μ))) := by
    rw [reflectedIntegral_tilted_density, ← integral_const_mul]
    apply integral_congr_ae
    apply Filter.Eventually.of_forall
    intro p
    change ((Real.exp (S p) / (∫ y, Real.exp (S y) ∂(μ.prod μ)) : ℝ) : ℂ) *
      (conj (F p.1) * F p.2) =
      (((∫ y, Real.exp (S y) ∂(μ.prod μ))⁻¹ : ℝ) : ℂ) *
        (∑ r, (a r : ℂ) * conj (u r p.1) * u r p.2)
    rw [← hfactor p]
    rw [Complex.ofReal_div, Complex.ofReal_inv]
    ring
  constructor
  · exact integrable_reflectedProduct_wilson_tilt (μ.prod μ) S hS Prod.swap
      (fun p => F p.2) (fun p => F p.2) continuous_swap
      (hF.comp continuous_snd) (hF.comp continuous_snd)
  · rw [heq]
    exact normalized_integral_gram_nonnegative μ _
      (wilson_partition_pos (μ.prod μ) S hS) a u ha hu hjoint

#print axioms normalized_integral_gram_nonnegative
#print axioms reflectedIntegral_wilson_of_gram
#print axioms integral_regulator_limit
#print axioms integral_gram_sum
#print axioms integral_gram_nonnegative
#print axioms integral_prod_gram_nonnegative
#print axioms reflectedIntegral
#print axioms integralKernel
#print axioms finiteTest
#print axioms finiteTest_reflected_product
#print axioms integrable_finiteTest_reflected_product
#print axioms reflectedIntegral_finiteTest
#print axioms reflectedIntegral_map
#print axioms integrable_reflectedProduct_map_iff
#print axioms reflectedIntegral_map_nonnegative
#print axioms integrable_continuous_compact
#print axioms integrable_reflectedProduct_continuous
#print axioms reflectedIntegral_finiteTest_continuous
#print axioms integrable_wilson_exp
#print axioms wilson_partition_pos
#print axioms wilson_tilt_probability
#print axioms integrable_reflectedProduct_wilson_tilt
#print axioms reflectedIntegral_tilted_density
#print axioms reflectedIntegral_wilson_one
#print axioms wilson_action_continuous
#print axioms wilson_link_tilt_probability
#print axioms tilted_vacuity
#print axioms reflectedIntegral_tilted_vacuity
#print axioms reflectedIntegral_wilson_const_I
#print axioms wilson_const_I_without_conjugation

end

end Millennium.G4.IntegralRP
