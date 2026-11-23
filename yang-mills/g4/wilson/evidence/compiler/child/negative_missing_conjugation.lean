import IntegralReflectionPositivity
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.Tactic.Group
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Algebra.BigOperators.Ring.Finset

noncomputable section

open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate

namespace Millennium.G4.WilsonRP

def partialExp (N : ℕ) (z : ℝ) : ℝ := ∑ k ∈ Finset.range N, z ^ k / (k.factorial : ℝ)

def dotKernel {D X : Type*} [Fintype D] (v : D → X → ℝ) (x y : X) : ℝ := ∑ r, v r x * v r y

def splitExponent {D X : Type*} [Fintype D] (s : X → ℝ) (v : D → X → ℝ) (p : X × X) : ℝ := s p.1 + s p.2 + dotKernel v p.1 p.2

def taylorWeight {D X : Type*} [Fintype D] (s : X → ℝ) (v : D → X → ℝ) (N : ℕ) (p : X × X) : ℝ := Real.exp (s p.1 + s p.2) * partialExp N (dotKernel v p.1 p.2)

def testedTaylor {D X : Type*} [Fintype D] (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ) (N : ℕ) (p : X × X) : ℂ := (taylorWeight s v N p : ℂ) * (F p.1 * F p.2)

def testedWilson {D X : Type*} [Fintype D] (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ) (p : X × X) : ℂ := (Real.exp (splitExponent s v p) : ℂ) * (conj (F p.1) * F p.2)

theorem hasSum_real_exp_terms (z : ℝ) :
    HasSum (fun k : ℕ => z ^ k / (k.factorial : ℝ)) (Real.exp z) := by
  have h := NormedSpace.expSeries_div_hasSum_exp ℝ z
  simpa only [Real.exp_eq_exp_ℝ] using h

theorem tendsto_partialExp (z : ℝ) :
    Tendsto (fun N => partialExp N z) atTop (nhds (Real.exp z)) := by
  simpa only [partialExp] using (hasSum_real_exp_terms z).tendsto_sum_nat

theorem abs_partialExp_le (N : ℕ) (z : ℝ) :
    |partialExp N z| ≤ Real.exp |z| := by
  have hterm (k : ℕ) :
      |z ^ k / (k.factorial : ℝ)| = |z| ^ k / (k.factorial : ℝ) := by
    have hk : 0 ≤ (k.factorial : ℝ) := by positivity
    rw [abs_div, abs_pow, abs_of_nonneg hk]
  have hfinite (n : ℕ) : |partialExp n z| ≤ partialExp n |z| := by
    induction n with
    | zero => simp [partialExp]
    | succ n ih =>
        simp only [partialExp, Finset.sum_range_succ]
        exact (abs_add_le _ _).trans (add_le_add ih (hterm n).le)
  have hsum := hasSum_real_exp_terms |z|
  have hnonneg (k : ℕ) : 0 ≤ |z| ^ k / (k.factorial : ℝ) := by
    positivity
  have hle : partialExp N |z| ≤
      ∑' k : ℕ, |z| ^ k / (k.factorial : ℝ) := by
    unfold partialExp
    exact Summable.sum_le_tsum (Finset.range N)
      (fun k _ => hnonneg k) hsum.summable
  exact (hfinite N).trans (hsum.tsum_eq ▸ hle)

section Continuity

variable {D X : Type*} [Fintype D] [TopologicalSpace X]
variable {s : X → ℝ} {v : D → X → ℝ} {F : X → ℂ}

theorem continuous_dotKernel (hv : ∀ r, Continuous (v r)) :
    Continuous (fun p : X × X => dotKernel v p.1 p.2) := by
  unfold dotKernel
  exact continuous_finset_sum _ fun r _ =>
    ((hv r).comp continuous_fst).mul ((hv r).comp continuous_snd)

theorem continuous_splitExponent (hs : Continuous s)
    (hv : ∀ r, Continuous (v r)) : Continuous (splitExponent s v) := by
  exact ((hs.comp continuous_fst).add (hs.comp continuous_snd)).add
    (continuous_dotKernel hv)

theorem continuous_partialExp (N : ℕ) : Continuous (partialExp N) := by
  unfold partialExp
  exact continuous_finset_sum _ fun k _ =>
    (continuous_id.pow k).div_const (k.factorial : ℝ)

theorem continuous_testFactor (hF : Continuous F) :
    Continuous (fun p : X × X => conj (F p.1) * F p.2) := by
  have hconj : Continuous (fun z : ℂ => conj z) := by
    exact Complex.continuous_conj
  exact (hconj.comp (hF.comp continuous_fst)).mul (hF.comp continuous_snd)

theorem continuous_testedTaylor (hs : Continuous s)
    (hv : ∀ r, Continuous (v r)) (hF : Continuous F) (N : ℕ) :
    Continuous (testedTaylor s v F N) := by
  have hweight : Continuous (taylorWeight s v N) := by
    exact (Real.continuous_exp.comp
      ((hs.comp continuous_fst).add (hs.comp continuous_snd))).mul
      ((continuous_partialExp N).comp (continuous_dotKernel hv))
  exact (Complex.continuous_ofReal.comp hweight).mul (continuous_testFactor hF)

theorem continuous_testedWilson (hs : Continuous s)
    (hv : ∀ r, Continuous (v r)) (hF : Continuous F) :
    Continuous (testedWilson s v F) := by
  exact (Complex.continuous_ofReal.comp
    (Real.continuous_exp.comp (continuous_splitExponent hs hv))).mul
    (continuous_testFactor hF)

end Continuity

section Convergence

variable {D X : Type*} [Fintype D]

theorem tendsto_testedTaylor (s : X → ℝ) (v : D → X → ℝ)
    (F : X → ℂ) (p : X × X) :
    Tendsto (fun N => testedTaylor s v F N p) atTop
      (nhds (testedWilson s v F p)) := by
  have hweight :
      Tendsto (fun N => taylorWeight s v N p) atTop
        (nhds (Real.exp (splitExponent s v p))) := by
    rw [splitExponent, Real.exp_add]
    exact tendsto_const_nhds.mul (tendsto_partialExp (dotKernel v p.1 p.2))
  have hcast :
      Tendsto (fun N => (taylorWeight s v N p : ℂ)) atTop
        (nhds (Real.exp (splitExponent s v p) : ℂ)) :=
    (Complex.continuous_ofReal.tendsto _).comp hweight
  simpa only [testedTaylor, testedWilson] using hcast.mul tendsto_const_nhds

theorem norm_testedTaylor_le (s : X → ℝ) (v : D → X → ℝ)
    (F : X → ℂ) (N : ℕ) (p : X × X) :
    ‖testedTaylor s v F N p‖ ≤
      Real.exp (s p.1 + s p.2) * Real.exp |dotKernel v p.1 p.2| *
        ‖F p.1‖ * ‖F p.2‖ := by
  have hconj : ‖conj (F p.1)‖ = ‖F p.1‖ := by
    exact Complex.norm_conj _
  have hweight :
      |taylorWeight s v N p| ≤
        Real.exp (s p.1 + s p.2) * Real.exp |dotKernel v p.1 p.2| := by
    rw [taylorWeight, abs_mul, abs_of_pos (Real.exp_pos _)]
    exact mul_le_mul_of_nonneg_left (abs_partialExp_le N _) (Real.exp_nonneg _)
  rw [testedTaylor, norm_mul, norm_mul, hconj, Complex.norm_real, Real.norm_eq_abs]
  rw [← mul_assoc]
  exact mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_right hweight (norm_nonneg _)) (norm_nonneg _)

theorem tendsto_testedTaylor_integral
    [TopologicalSpace X] [CompactSpace X] [SecondCountableTopology X]
    [MeasurableSpace X] [BorelSpace X]
    (μ : Measure (X × X)) [IsFiniteMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r)) (hF : Continuous F) :
    Tendsto (fun N => ∫ p, testedTaylor s v F N p ∂μ) atTop
      (nhds (∫ p, testedWilson s v F p ∂μ)) := by
  let bound : X × X → ℝ := fun p =>
    Real.exp (s p.1 + s p.2) * Real.exp |dotKernel v p.1 p.2| *
      ‖F p.1‖ * ‖F p.2‖
  have houter : Continuous (fun p : X × X => Real.exp (s p.1 + s p.2)) :=
    Real.continuous_exp.comp ((hs.comp continuous_fst).add (hs.comp continuous_snd))
  have hinner : Continuous (fun p : X × X => Real.exp |dotKernel v p.1 p.2|) :=
    Real.continuous_exp.comp ((continuous_dotKernel hv).abs)
  have hbound_continuous : Continuous bound :=
    ((houter.mul hinner).mul (hF.comp continuous_fst).norm).mul
      (hF.comp continuous_snd).norm
  have hbound_integrable : Integrable bound μ :=
    Millennium.G4.IntegralRP.integrable_continuous_compact μ bound hbound_continuous
  exact MeasureTheory.tendsto_integral_of_dominated_convergence bound
    (fun N => (continuous_testedTaylor hs hv hF N).aestronglyMeasurable)
    hbound_integrable
    (fun N => Filter.Eventually.of_forall (norm_testedTaylor_le s v F N))
    (Filter.Eventually.of_forall (tendsto_testedTaylor s v F))

end Convergence

#print axioms partialExp
#print axioms dotKernel
#print axioms splitExponent
#print axioms taylorWeight
#print axioms testedTaylor
#print axioms testedWilson
#print axioms hasSum_real_exp_terms
#print axioms tendsto_partialExp
#print axioms abs_partialExp_le
#print axioms continuous_dotKernel
#print axioms continuous_splitExponent
#print axioms continuous_partialExp
#print axioms continuous_testFactor
#print axioms continuous_testedTaylor
#print axioms continuous_testedWilson
#print axioms tendsto_testedTaylor
#print axioms norm_testedTaylor_le
#print axioms tendsto_testedTaylor_integral

end Millennium.G4.WilsonRP

end

namespace Millennium.G4.WilsonRP
noncomputable section
open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate

theorem integral_tilted_complex_normalized {X : Type*} [MeasurableSpace X]
    (μ : Measure X) (S : X → ℝ) (P : X → ℂ) :
    (∫ x, P x ∂μ.tilted S) =
      (((∫ x, Real.exp (S x) ∂μ)⁻¹ : ℝ) : ℂ) *
        (∫ x, (Real.exp (S x) : ℂ) * P x ∂μ) := by
  rw [integral_tilted, ← integral_const_mul]
  apply integral_congr_ae
  apply Filter.Eventually.of_forall
  intro x
  change ((Real.exp (S x) / (∫ y, Real.exp (S y) ∂μ) : ℝ) : ℂ) * P x =
    (((∫ y, Real.exp (S y) ∂μ)⁻¹ : ℝ) : ℂ) * ((Real.exp (S x) : ℂ) * P x)
  rw [Complex.ofReal_div, Complex.ofReal_inv]
  ring

#print axioms integral_tilted_complex_normalized
end
end Millennium.G4.WilsonRP

-- NATIVE CHILD 1

namespace Millennium.G4.WilsonRP

noncomputable section

open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate

variable {X D : Type*} [Fintype D]

def wordMode (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (k : ℕ) (w : Fin k → D) (x : X) : ℂ :=
  (Real.exp (s x) : ℂ) * F x * ∏ i, (v (w i) x : ℂ)

def wordGramDegree (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (k : ℕ) (p : X × X) : ℂ :=
  ∑ w : Fin k → D,
    ((1 / (k.factorial : ℝ) : ℝ) : ℂ) *
      conj (wordMode s v F k w p.1) * wordMode s v F k w p.2

theorem testedTaylor_degree_eq_wordGramDegree
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (k : ℕ) (p : X × X) :
    (Real.exp (s p.1 + s p.2) : ℂ) *
        ((dotKernel v p.1 p.2 : ℂ) ^ k / (k.factorial : ℂ)) *
        (conj (F p.1) * F p.2) =
      wordGramDegree s v F k p := by
  classical
  have hdot :
      (dotKernel v p.1 p.2 : ℂ) =
        ∑ r : D, (v r p.1 : ℂ) * (v r p.2 : ℂ) := by
    unfold dotKernel
    push_cast
    rfl
  rw [hdot, Fintype.sum_pow]
  simp only [div_eq_mul_inv, Finset.sum_mul, Finset.mul_sum, wordGramDegree]
  apply Finset.sum_congr rfl
  intro w _
  rw [Real.exp_add, Finset.prod_mul_distrib]
  simp only [wordMode, map_mul, map_prod, Complex.conj_ofReal]
  push_cast <;> ring

theorem testedTaylor_eq_sum_wordGramDegree
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (N : ℕ) (p : X × X) :
    testedTaylor s v F N p =
      ∑ k ∈ Finset.range N, wordGramDegree s v F k p := by
  unfold testedTaylor taylorWeight partialExp
  push_cast
  simp only [Finset.mul_sum, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro k hk
  simpa only [Complex.ofReal_exp, Complex.ofReal_add] using
    testedTaylor_degree_eq_wordGramDegree s v F k p

variable [TopologicalSpace X]

theorem continuous_wordMode
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F) (k : ℕ) (w : Fin k → D) :
    Continuous (wordMode s v F k w) := by
  have hprod : Continuous (fun x : X => ∏ i, (v (w i) x : ℂ)) :=
    continuous_finset_prod _ (fun i _ =>
      Complex.continuous_ofReal.comp (hv (w i)))
  exact ((Complex.continuous_ofReal.comp (Real.continuous_exp.comp hs)).mul
    hF).mul hprod

theorem continuous_wordGramDegree
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F) (k : ℕ) :
    Continuous (wordGramDegree s v F k) := by
  unfold wordGramDegree
  apply continuous_finset_sum
  intro w _
  have hw := continuous_wordMode s v F hs hv hF k w
  have hc : Continuous (fun z : ℂ => conj z) := continuous_star
  exact (continuous_const.mul (hc.comp (hw.comp continuous_fst))).mul
    (hw.comp continuous_snd)

open Millennium.G4.ComplexRP (NonnegativeComplex)
open Millennium.G4.IntegralRP
  (integrable_continuous_compact integral_prod_gram_nonnegative)

variable [CompactSpace X] [SecondCountableTopology X]
  [MeasurableSpace X] [BorelSpace X]

theorem nonnegative_wordGramDegree_integral
    (μ : Measure X) [IsProbabilityMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F) (k : ℕ) :
    NonnegativeComplex
      (∫ p : X × X, wordGramDegree s v F k p ∂((μ).prod μ)) := by
  exact integral_prod_gram_nonnegative μ
    (fun _ : Fin k → D => (1 / (k.factorial : ℝ)))
    (wordMode s v F k)
    (fun _ => div_nonneg zero_le_one (Nat.cast_nonneg _))
    (fun w => integrable_continuous_compact μ _
      (continuous_wordMode s v F hs hv hF k w))
    (integrable_continuous_compact ((μ).prod μ) _
      (continuous_wordGramDegree s v F hs hv hF k))

theorem nonnegativeComplex_finset_sum
    {ι : Type*} (t : Finset ι) (f : ι → ℂ)
    (hf : ∀ i ∈ t, NonnegativeComplex (f i)) :
    NonnegativeComplex (∑ i ∈ t, f i) := by
  classical
  induction t using Finset.induction_on with
  | empty =>
      simp [NonnegativeComplex]
  | @insert i t hi ih =>
      have hhead := hf i (Finset.mem_insert_self i t)
      have htail := ih (fun j hj => hf j (Finset.mem_insert_of_mem hj))
      rw [Finset.sum_insert hi]
      exact ⟨by rw [Complex.add_im, hhead.1, htail.1, add_zero],
        by rw [Complex.add_re]; exact add_nonneg hhead.2 htail.2⟩

theorem nonnegative_testedTaylor_integral
    (μ : Measure X) [IsProbabilityMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F) (N : ℕ) :
    NonnegativeComplex
      (∫ p : X × X, testedTaylor s v F N p ∂((μ).prod μ)) := by
  have heq : testedTaylor s v F N =
      (fun p => ∑ k ∈ Finset.range N, wordGramDegree s v F k p) :=
    funext (testedTaylor_eq_sum_wordGramDegree s v F N)
  rw [heq, integral_finset_sum]
  · exact nonnegativeComplex_finset_sum _ _ (fun k _ =>
      nonnegative_wordGramDegree_integral μ s v F hs hv hF k)
  · intro k _
    exact integrable_continuous_compact ((μ).prod μ) _
      (continuous_wordGramDegree s v F hs hv hF k)

theorem nonnegative_testedWilson_integral
    (μ : Measure X) [IsProbabilityMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F) :
    NonnegativeComplex
      (∫ p : X × X, testedWilson s v F p ∂((μ).prod μ)) := by
  exact Millennium.G4.ComplexRP.nonnegativeComplex_of_tendsto
    (tendsto_testedTaylor_integral ((μ).prod μ) s v F hs hv hF)
    (Filter.Eventually.of_forall
      (fun N => nonnegative_testedTaylor_integral μ s v F hs hv hF N))

theorem normalized_testedWilson_of_integral_eq
    (μ : Measure X) [IsProbabilityMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r))
    (hF : Continuous F)
    (ν : Measure (X × X)) (Z : ℝ) (hZ : 0 < Z)
    (hidentity :
      (∫ p : X × X, conj (F (Prod.swap p).2) * F p.2 ∂ν) =
        (↑(Z⁻¹) : ℂ) *
          (∫ p : X × X, testedWilson s v F p ∂((μ).prod μ)))
    (hintegrable :
      Integrable (fun p : X × X => conj (F (Prod.swap p).2) * F p.2) ν) :
    NonnegativeComplex
        (∫ p : X × X, conj (F (Prod.swap p).2) * F p.2 ∂ν) ∧
      Integrable (fun p : X × X => conj (F (Prod.swap p).2) * F p.2) ν := by
  refine ⟨?_, hintegrable⟩
  rw [hidentity]
  obtain ⟨him, hre⟩ := nonnegative_testedWilson_integral μ s v F hs hv hF
  constructor
  · simp [Complex.mul_im, him]
  · simpa [Complex.mul_re] using mul_nonneg (inv_nonneg.mpr hZ.le) hre

#print axioms wordMode
#print axioms wordGramDegree
#print axioms testedTaylor_degree_eq_wordGramDegree
#print axioms testedTaylor_eq_sum_wordGramDegree
#print axioms continuous_wordMode
#print axioms continuous_wordGramDegree
#print axioms nonnegative_wordGramDegree_integral
#print axioms nonnegativeComplex_finset_sum
#print axioms nonnegative_testedTaylor_integral
#print axioms nonnegative_testedWilson_integral
#print axioms normalized_testedWilson_of_integral_eq

end

end Millennium.G4.WilsonRP

-- NATIVE CHILD 2


open MeasureTheory

namespace Millennium.G4.WilsonRP

noncomputable section

section GaugeAlgebra

variable {V G : Type*} [Group G]

def temporalGauge (h : V → ℕ → G) (x : V) : ℕ → G
  | 0 => 1
  | t + 1 => temporalGauge h x t * h x t

theorem temporalGauge_cancel (h : V → ℕ → G) (x : V) (t : ℕ) :
    temporalGauge h x t * h x t * (temporalGauge h x (t + 1))⁻¹ = 1 := by
  change
    (temporalGauge h x t * h x t) *
      (temporalGauge h x t * h x t)⁻¹ = 1
  exact mul_inv_cancel _

theorem spatialGauge_inverse (a u b : G) :
    (a * u * b⁻¹)⁻¹ = b * u⁻¹ * a⁻¹ := by
  group

theorem plaquette_covariance (g₀ g₁ k₀ k₁ u h₁ v h₀ : G) :
    (g₀ * u * g₁⁻¹) * (g₁ * h₁ * k₁⁻¹) *
        (k₁ * v⁻¹ * k₀⁻¹) * (k₀ * h₀⁻¹ * g₀⁻¹) =
      g₀ * (u * h₁ * v⁻¹ * h₀⁻¹) * g₀⁻¹ := by
  group

end GaugeAlgebra

section HaarCoordinates

variable {E G : Type*} [Group G] [MeasurableSpace G]
  [MeasurableMul G] [MeasurableInv G]

def gaugeMap (l r : E → G) (U : E → G) : E → G :=
  fun e => l e * U e * r e

def gaugeEquiv (l r : E → G) : (E → G) ≃ᵐ (E → G) where
  toFun := gaugeMap l r
  invFun := gaugeMap (fun e => (l e)⁻¹) (fun e => (r e)⁻¹)
  left_inv U := by
    funext e
    simp only [gaugeMap]
    group
  right_inv U := by
    funext e
    simp only [gaugeMap]
    group
  measurable_toFun := by
    apply measurable_pi_lambda
    intro e
    exact (measurable_mul_const (r e)).comp
      ((measurable_const_mul (l e)).comp (measurable_pi_apply e))
  measurable_invFun := by
    apply measurable_pi_lambda
    intro e
    exact (measurable_mul_const ((r e)⁻¹)).comp
      ((measurable_const_mul ((l e)⁻¹)).comp (measurable_pi_apply e))

variable [Fintype E]
variable (m : Measure G) [IsProbabilityMeasure m]
  [Measure.IsMulLeftInvariant m] [Measure.IsMulRightInvariant m]

theorem measurePreserving_gaugeMap (l r : E → G) :
    MeasurePreserving (gaugeMap l r)
      (Measure.pi (fun _ : E => m)) (Measure.pi (fun _ : E => m)) := by
  have hcoord (e : E) :
      MeasurePreserving (fun u : G => l e * u * r e) m m :=
    (measurePreserving_mul_right m (r e)).comp
      (measurePreserving_mul_left m (l e))
  exact measurePreserving_pi (fun _ : E => m) (fun _ : E => m) hcoord

variable {B : Type*} [NormedAddCommGroup B] [NormedSpace ℝ B] [CompleteSpace B]

theorem integral_gaugeMap (l r : E → G) (φ : (E → G) → B) :
    (∫ U, φ (gaugeMap l r U) ∂(Measure.pi (fun _ : E => m))) =
      ∫ U, φ U ∂(Measure.pi (fun _ : E => m)) := by
  have hpres :
      MeasurePreserving (gaugeEquiv l r)
        (Measure.pi (fun _ : E => m)) (Measure.pi (fun _ : E => m)) :=
    measurePreserving_gaugeMap m l r
  exact hpres.integral_comp' φ

section TemporalIntegration

variable {H : Type*} [MeasurableSpace H]
variable (η : Measure H) [IsProbabilityMeasure η]
variable (l r : H → E → G)

local notation "μ" => Measure.pi (fun _ : E => m)

theorem integral_temporalGauge
    (Φ : (E → G) × H → B) (φ : (E → G) → B)
    (hΦ : Integrable Φ ((μ).prod η))
    (hpoint : ∀ U h, Φ (U, h) = φ (gaugeMap (l h) (r h) U)) :
    (∫ z, Φ z ∂((μ).prod η)) = ∫ U, φ U ∂μ := by
  have hfiber (h : H) :
      (∫ U, Φ (U, h) ∂μ) = ∫ U, φ U ∂μ := by
    calc
      (∫ U, Φ (U, h) ∂μ) =
          ∫ U, φ (gaugeMap (l h) (r h) U) ∂μ :=
        integral_congr_ae (Filter.Eventually.of_forall (fun U => hpoint U h))
      _ = ∫ U, φ U ∂μ := integral_gaugeMap m (l h) (r h) φ
  calc
    (∫ z, Φ z ∂((μ).prod η)) =
        ∫ h, (∫ U, Φ (U, h) ∂μ) ∂η :=
      integral_prod_symm Φ hΦ
    _ = ∫ _ : H, (∫ U, φ U ∂μ) ∂η :=
      integral_congr_ae (Filter.Eventually.of_forall hfiber)
    _ = ∫ U, φ U ∂μ := by simp

/-- Transport of the partition and the normalized weighted expectation
for the density convention `exp S`. -/
theorem normalized_weighted_temporalGauge
    (S : (E → G) × H → ℝ) (S₀ : (E → G) → ℝ)
    (P : (E → G) × H → B) (P₀ : (E → G) → B)
    (hS : ∀ U h, S (U, h) = S₀ (gaugeMap (l h) (r h) U))
    (hP : ∀ U h, P (U, h) = P₀ (gaugeMap (l h) (r h) U))
    (hDensity : Integrable (fun z => Real.exp (S z)) ((μ).prod η))
    (hWeighted : Integrable (fun z => Real.exp (S z) • P z) ((μ).prod η))
    (hDensity₀ : Integrable (fun U => Real.exp (S₀ U)) μ)
    (hWeighted₀ : Integrable (fun U => Real.exp (S₀ U) • P₀ U) μ)
    (hPositive₀ : 0 < ∫ U, Real.exp (S₀ U) ∂μ) :
    (∫ z, Real.exp (S z) ∂((μ).prod η)) =
        (∫ U, Real.exp (S₀ U) ∂μ) ∧
    0 < (∫ z, Real.exp (S z) ∂((μ).prod η)) ∧
    (∫ z, Real.exp (S z) • P z ∂((μ).prod η)) =
        (∫ U, Real.exp (S₀ U) • P₀ U ∂μ) ∧
    (∫ z, Real.exp (S z) ∂((μ).prod η))⁻¹ •
        (∫ z, Real.exp (S z) • P z ∂((μ).prod η)) =
      (∫ U, Real.exp (S₀ U) ∂μ)⁻¹ •
        (∫ U, Real.exp (S₀ U) • P₀ U ∂μ) := by
  have hPartition :
      (∫ z, Real.exp (S z) ∂((μ).prod η)) =
        ∫ U, Real.exp (S₀ U) ∂μ :=
    integral_temporalGauge m η l r
      (fun z => Real.exp (S z)) (fun U => Real.exp (S₀ U))
      hDensity (fun U h => congrArg Real.exp (hS U h))
  have hNumerator :
      (∫ z, Real.exp (S z) • P z ∂((μ).prod η)) =
        ∫ U, Real.exp (S₀ U) • P₀ U ∂μ :=
    integral_temporalGauge m η l r
      (fun z => Real.exp (S z) • P z)
      (fun U => Real.exp (S₀ U) • P₀ U) hWeighted (by
        intro U h
        dsimp only
        rw [hS U h, hP U h])
  refine ⟨hPartition, hPartition.symm ▸ hPositive₀, hNumerator, ?_⟩
  rw [hPartition, hNumerator]

end TemporalIntegration
end HaarCoordinates
end

#print axioms temporalGauge
#print axioms temporalGauge_cancel
#print axioms spatialGauge_inverse
#print axioms plaquette_covariance
#print axioms gaugeMap
#print axioms gaugeEquiv
#print axioms measurePreserving_gaugeMap
#print axioms integral_gaugeMap
#print axioms integral_temporalGauge
#print axioms normalized_weighted_temporalGauge

end Millennium.G4.WilsonRP


noncomputable section
open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate

namespace Millennium.G4.WilsonRP

variable {V E C G K : Type*} [DecidableEq V] [Group G]

def vertexGauge (src dst : E → V) (g : V → G) (U : E → G) : E → G :=
  fun e => g (src e) * U e * (g (dst e))⁻¹

def boundaryGauge (B : Finset V) (h : ↥B → G) (v : V) : G :=
  if hv : v ∈ B then h ⟨v, hv⟩ else 1

theorem boundaryGauge_at (B : Finset V) (h : ↥B → G) (b : ↥B) :
    boundaryGauge B h b.val = h b := by
  rcases b with ⟨v, hv⟩
  simp [boundaryGauge, hv]

def GaugeInvariant (src dst : E → V) (f : (E → G) → K) : Prop :=
  ∀ (g : V → G) (U : E → G), f (vertexGauge src dst g U) = f U

/-- The coordinate left and right translations used by the parent Haar theorem. -/
theorem vertexGauge_eq_coordinateTranslations
    (src dst : E → V) (g : V → G) :
    vertexGauge src dst g =
      (fun (U : E → G) e => g (src e) * U e * (g (dst e))⁻¹) :=
  rfl

def crossingWord (edge : C → E) {B : Finset V} (bsrc bdst : C → ↥B)
    (U0 U1 : E → G) (h : ↥B → G) (c : C) : G :=
  U0 (edge c) * h (bdst c) * (U1 (edge c))⁻¹ * (h (bsrc c))⁻¹

theorem crossingWord_eq_gauged
    (src dst : E → V) (edge : C → E) {B : Finset V}
    (bsrc bdst : C → ↥B)
    (hsrc : ∀ c, src (edge c) = (bsrc c).val)
    (hdst : ∀ c, dst (edge c) = (bdst c).val)
    (U0 U1 : E → G) (h : ↥B → G) (c : C) :
    crossingWord edge bsrc bdst U0 U1 h c =
      U0 (edge c) * (vertexGauge src dst (boundaryGauge B h) U1 (edge c))⁻¹ := by
  unfold crossingWord vertexGauge
  rw [hsrc c, hdst c, boundaryGauge_at, boundaryGauge_at]
  simp [mul_inv_rev, mul_assoc]

def slabExponent [Fintype C]
    (edge : C → E) {B : Finset V} (bsrc bdst : C → ↥B)
    (χ : G → ℝ) (β : C → ℝ) (s : (E → G) → ℝ)
    (x : ((E → G) × (E → G)) × (↥B → G)) : ℝ :=
  s x.1.1 + s x.1.2 +
    ∑ c, β c * χ (crossingWord edge bsrc bdst x.1.1 x.1.2 x.2 c)

def reducedSlabExponent [Fintype C]
    (edge : C → E) (χ : G → ℝ) (β : C → ℝ) (s : (E → G) → ℝ)
    (x : (E → G) × (E → G)) : ℝ :=
  s x.1 + s x.2 + ∑ c, β c * χ ((x.1 (edge c))⁻¹ * x.2 (edge c))

theorem slabExponent_gauge [Fintype C]
    (src dst : E → V) (edge : C → E) {B : Finset V}
    (bsrc bdst : C → ↥B)
    (hsrc : ∀ c, src (edge c) = (bsrc c).val)
    (hdst : ∀ c, dst (edge c) = (bdst c).val)
    (χ : G → ℝ) (β : C → ℝ) (s : (E → G) → ℝ)
    (hs : GaugeInvariant src dst s)
    (χrelative : ∀ a b : G, χ (a * b⁻¹) = χ (a⁻¹ * b))
    (U0 U1 : E → G) (h : ↥B → G) :
    slabExponent edge bsrc bdst χ β s ((U0, U1), h) =
      reducedSlabExponent edge χ β s
        (U0, vertexGauge src dst (boundaryGauge B h) U1) := by
  simp only [slabExponent, reducedSlabExponent, hs (boundaryGauge B h) U1]
  congr 1
  apply Finset.sum_congr rfl
  intro c _
  rw [crossingWord_eq_gauged src dst edge bsrc bdst hsrc hdst, χrelative]

def positiveHalfTest {B : Finset V} (F : (E → G) → K)
    (x : ((E → G) × (E → G)) × (↥B → G)) : K :=
  F x.1.2

def slabReflection (B : Finset V)
    (x : ((E → G) × (E → G)) × (↥B → G)) :
    ((E → G) × (E → G)) × (↥B → G) :=
  ((x.1.2, x.1.1), fun b => (x.2 b)⁻¹)

theorem slabReflection_involutive (B : Finset V) :
    Function.Involutive (slabReflection (E := E) (G := G) B) := by
  rintro ⟨⟨U0, U1⟩, h⟩
  simp [slabReflection]

/-- On complex scalars, `star` is complex conjugation. -/
def reflectedProduct {B : Finset V} (F : (E → G) → ℂ)
    (x : ((E → G) × (E → G)) × (↥B → G)) : ℂ :=
  star (positiveHalfTest F (slabReflection B x)) * positiveHalfTest F x

theorem reflectedProduct_eq {B : Finset V} (F : (E → G) → ℂ)
    (U0 U1 : E → G) (h : ↥B → G) :
    reflectedProduct F ((U0, U1), h) = star (F U0) * F U1 :=
  rfl

theorem reflectedProduct_gauge
    (src dst : E → V) {B : Finset V} (F : (E → G) → ℂ)
    (hF : GaugeInvariant src dst F)
    (U0 U1 : E → G) (h : ↥B → G) :
    reflectedProduct F ((U0, U1), h) =
      star (F U0) * F (vertexGauge src dst (boundaryGauge B h) U1) := by
  rw [reflectedProduct_eq, hF (boundaryGauge B h) U1]

section Topology

variable [TopologicalSpace G] [IsTopologicalGroup G]

theorem continuous_slabExponent [Fintype C]
    (edge : C → E) {B : Finset V} (bsrc bdst : C → ↥B)
    (χ : G → ℝ) (β : C → ℝ) (s : (E → G) → ℝ)
    (hχ : Continuous χ) (hs : Continuous s) :
    Continuous (slabExponent edge bsrc bdst χ β s) := by
  let X := ((E → G) × (E → G)) × (↥B → G)
  have h0 : Continuous (fun x : X => x.1.1) :=
    continuous_fst.comp continuous_fst
  have h1 : Continuous (fun x : X => x.1.2) :=
    continuous_snd.comp continuous_fst
  have hb : Continuous (fun x : X => x.2) := continuous_snd
  unfold slabExponent
  apply ((hs.comp h0).add (hs.comp h1)).add
  apply continuous_finset_sum
  intro c _
  have hu0 := (continuous_apply (edge c)).comp h0
  have hu1 := (continuous_apply (edge c)).comp h1
  have hdst := (continuous_apply (bdst c)).comp hb
  have hsrc := (continuous_apply (bsrc c)).comp hb
  have hw : Continuous (fun x : X =>
      crossingWord edge bsrc bdst x.1.1 x.1.2 x.2 c) := by
    unfold crossingWord
    exact ((hu0.mul hdst).mul hu1.inv).mul hsrc.inv
  exact continuous_const.mul (hχ.comp hw)

theorem continuous_reducedSlabExponent [Fintype C]
    (edge : C → E) (χ : G → ℝ) (β : C → ℝ) (s : (E → G) → ℝ)
    (hχ : Continuous χ) (hs : Continuous s) :
    Continuous (reducedSlabExponent edge χ β s) := by
  let X := (E → G) × (E → G)
  have h0 : Continuous (fun x : X => x.1) := continuous_fst
  have h1 : Continuous (fun x : X => x.2) := continuous_snd
  unfold reducedSlabExponent
  apply ((hs.comp h0).add (hs.comp h1)).add
  apply continuous_finset_sum
  intro c _
  have hu0 := (continuous_apply (edge c)).comp h0
  have hu1 := (continuous_apply (edge c)).comp h1
  exact continuous_const.mul (hχ.comp (hu0.inv.mul hu1))

end Topology

theorem continuous_positiveHalfTest [TopologicalSpace G] [TopologicalSpace K]
    {B : Finset V} (F : (E → G) → K) (hF : Continuous F) :
    Continuous (positiveHalfTest (B := B) F) :=
  hF.comp (continuous_snd.comp continuous_fst)

theorem gaugeInvariant_finset_sum {I : Type*} [AddCommMonoid K]
    (src dst : E → V) (S : Finset I) (f : I → (E → G) → K)
    (hf : ∀ i ∈ S, GaugeInvariant src dst (f i)) :
    GaugeInvariant src dst (fun U => ∑ i ∈ S, f i U) := by
  intro g U
  exact Finset.sum_congr rfl (fun i hi => hf i hi g U)

def plaquetteWord (e1 e2 e3 e4 : E) (U : E → G) : G :=
  U e1 * U e2 * (U e3)⁻¹ * (U e4)⁻¹

theorem gaugeInvariant_plaquette
    (src dst : E → V) (e1 e2 e3 e4 : E)
    (h12 : dst e1 = src e2)
    (h23 : dst e2 = dst e3)
    (h34 : src e3 = dst e4)
    (h41 : src e4 = src e1)
    (χ : G → K) (hχ : ∀ a x : G, χ (a * x * a⁻¹) = χ x) :
    GaugeInvariant src dst (fun U => χ (plaquetteWord e1 e2 e3 e4 U)) := by
  intro g U
  change χ (plaquetteWord e1 e2 e3 e4 (vertexGauge src dst g U)) =
    χ (plaquetteWord e1 e2 e3 e4 U)
  have hcov :
      plaquetteWord e1 e2 e3 e4 (vertexGauge src dst g U) =
        g (src e1) * plaquetteWord e1 e2 e3 e4 U * (g (src e1))⁻¹ := by
    simp only [plaquetteWord, vertexGauge, h12, h23, h34, h41]
    group
  rw [hcov, hχ]

#print axioms vertexGauge
#print axioms boundaryGauge
#print axioms boundaryGauge_at
#print axioms GaugeInvariant
#print axioms vertexGauge_eq_coordinateTranslations
#print axioms crossingWord
#print axioms crossingWord_eq_gauged
#print axioms slabExponent
#print axioms reducedSlabExponent
#print axioms slabExponent_gauge
#print axioms positiveHalfTest
#print axioms slabReflection
#print axioms slabReflection_involutive
#print axioms reflectedProduct
#print axioms reflectedProduct_eq
#print axioms reflectedProduct_gauge
#print axioms continuous_slabExponent
#print axioms continuous_reducedSlabExponent
#print axioms continuous_positiveHalfTest
#print axioms gaugeInvariant_finset_sum
#print axioms plaquetteWord
#print axioms gaugeInvariant_plaquette

end Millennium.G4.WilsonRP

end

namespace Millennium.G4.WilsonRP
noncomputable section
open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate Matrix

theorem split_wilson_reflection_positive {D X : Type*} [Fintype D]
    [TopologicalSpace X] [CompactSpace X] [SecondCountableTopology X]
    [MeasurableSpace X] [BorelSpace X]
    (μ : Measure X) [IsProbabilityMeasure μ]
    (s : X → ℝ) (v : D → X → ℝ) (F : X → ℂ)
    (hs : Continuous s) (hv : ∀ r, Continuous (v r)) (hF : Continuous F) :
    Integrable (fun p : X × X => conj (F p.1) * F p.2)
        ((μ.prod μ).tilted (splitExponent s v)) ∧
    Millennium.G4.ComplexRP.NonnegativeComplex
      (Millennium.G4.IntegralRP.reflectedIntegral
        ((μ.prod μ).tilted (splitExponent s v)) Prod.swap
        (fun p => F p.2) (fun p => F p.2)) := by
  have hS := continuous_splitExponent hs hv
  constructor
  · exact Millennium.G4.IntegralRP.integrable_reflectedProduct_wilson_tilt
      (μ.prod μ) _ hS Prod.swap (fun p => F p.2) (fun p => F p.2)
      continuous_swap (hF.comp continuous_snd) (hF.comp continuous_snd)
  · unfold Millennium.G4.IntegralRP.reflectedIntegral
    rw [integral_tilted_complex_normalized]
    obtain ⟨him, hre⟩ := nonnegative_testedWilson_integral μ s v F hs hv hF
    have hZ := Millennium.G4.IntegralRP.wilson_partition_pos (μ.prod μ) _ hS
    change Millennium.G4.ComplexRP.NonnegativeComplex
      ((((∫ p, Real.exp (splitExponent s v p) ∂μ.prod μ)⁻¹ : ℝ) : ℂ) *
        (∫ p, testedWilson s v F p ∂μ.prod μ))
    constructor
    · simp [Complex.mul_im, him]
    · simpa [Complex.mul_re] using mul_nonneg (inv_nonneg.mpr hZ.le) hre

def realFeatures {I X : Type*} (w : I → ℝ) (a : I → X → ℂ)
    (r : I × Bool) (x : X) : ℝ :=
  Real.sqrt (w r.1) * (if r.2 then (a r.1 x).re else (a r.1 x).im)

theorem dot_realFeatures {I X : Type*} [Fintype I]
    (w : I → ℝ) (hw : ∀ i, 0 ≤ w i) (a : I → X → ℂ) (x y : X) :
    dotKernel (realFeatures w a) x y =
      ∑ i, w i * (conj (a i x) * a i y).re := by
  classical
  unfold dotKernel
  rw [Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro i hi
  simp only [realFeatures, Fintype.sum_bool, Bool.false_eq_true, ite_true, ite_false]
  rw [Complex.mul_re, Complex.conj_re, Complex.conj_im]
  calc
    _ = (Real.sqrt (w i)) ^ 2 *
        ((a i x).re * (a i y).re + (a i x).im * (a i y).im) := by ring
    _ = _ := by rw [Real.sq_sqrt (hw i)]; ring

theorem continuous_realFeatures {I X : Type*} [TopologicalSpace X]
    (w : I → ℝ) (a : I → X → ℂ) (ha : ∀ i, Continuous (a i)) (r : I × Bool) :
    Continuous (realFeatures w a r) := by
  rcases r with ⟨i,b⟩
  cases b
  · change Continuous (fun x => Real.sqrt (w i) * (a i x).im)
    exact continuous_const.mul (Complex.continuous_im.comp (ha i))
  · change Continuous (fun x => Real.sqrt (w i) * (a i x).re)
    exact continuous_const.mul (Complex.continuous_re.comp (ha i))

theorem trace_conjTranspose_mul_sum {n : Type*} [Fintype n] [DecidableEq n]
    (A B : Matrix n n ℂ) :
    Matrix.trace (Aᴴ * B) = ∑ p : n × n, conj (A p.1 p.2) * B p.1 p.2 := by
  classical
  simp only [Matrix.trace, Matrix.diag, Matrix.mul_apply, Matrix.conjTranspose_apply,
    Fintype.sum_prod_type]
  exact Finset.sum_comm

theorem real_trace_crossing {n : Type*} [Fintype n] [DecidableEq n]
    (A B : Matrix n n ℂ) :
    (Matrix.trace (A * Bᴴ)).re = (Matrix.trace (Aᴴ * B)).re := by
  have h : Matrix.trace (A * Bᴴ) = conj (Matrix.trace (Aᴴ * B)) := by
    change Matrix.trace (A * Bᴴ) = star (Matrix.trace (Aᴴ * B))
    rw [← Matrix.trace_conjTranspose]
    simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
    exact Matrix.trace_mul_comm _ _
  rw [h]
  exact Complex.conj_re _

def unitaryCharacter {G n : Type*} [Group G] [Fintype n] [DecidableEq n]
    (ρ : G →* Matrix.unitaryGroup n ℂ) (g : G) : ℝ :=
  (Matrix.trace (ρ g : Matrix n n ℂ)).re

theorem unitaryCharacter_relative {G n : Type*} [Group G] [Fintype n] [DecidableEq n]
    (ρ : G →* Matrix.unitaryGroup n ℂ) (a b : G) :
    unitaryCharacter ρ (a * b⁻¹) = unitaryCharacter ρ (a⁻¹ * b) := by
  simp only [unitaryCharacter, map_mul, map_inv, Matrix.UnitaryGroup.mul_val,
    Matrix.UnitaryGroup.inv_val, Matrix.star_eq_conjTranspose]
  exact real_trace_crossing _ _

theorem unitaryCharacter_conjugate {G n : Type*} [Group G] [Fintype n] [DecidableEq n]
    (ρ : G →* Matrix.unitaryGroup n ℂ) (a b : G) :
    unitaryCharacter ρ (a * b * a⁻¹) = unitaryCharacter ρ b := by
  have hm : (ρ a : Matrix n n ℂ)ᴴ * (ρ a : Matrix n n ℂ) = 1 :=
    Matrix.UnitaryGroup.star_mul_self (ρ a)
  simp only [unitaryCharacter, map_mul, map_inv, Matrix.UnitaryGroup.mul_val,
    Matrix.UnitaryGroup.inv_val, Matrix.star_eq_conjTranspose]
  rw [Matrix.trace_mul_cycle, hm, Matrix.one_mul]

#print axioms split_wilson_reflection_positive
#print axioms realFeatures
#print axioms dot_realFeatures
#print axioms continuous_realFeatures
#print axioms trace_conjTranspose_mul_sum
#print axioms real_trace_crossing
#print axioms unitaryCharacter
#print axioms unitaryCharacter_relative
#print axioms unitaryCharacter_conjugate
end
end Millennium.G4.WilsonRP

namespace Millennium.G4.WilsonRP
noncomputable section
open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate Matrix

theorem integral_remove_gauge {Y H K : Type*}
    [MeasurableSpace Y] [MeasurableSpace H]
    [NormedAddCommGroup K] [NormedSpace ℝ K] [CompleteSpace K]
    (μ : Measure Y) [IsProbabilityMeasure μ] (η : Measure H) [IsProbabilityMeasure η]
    (T : H → Y ≃ᵐ Y) (hT : ∀ h, MeasurePreserving (T h) μ μ)
    (Φ : Y × H → K) (φ : Y → K) (hΦ : Integrable Φ (μ.prod η))
    (hpoint : ∀ U h, Φ (U,h) = φ (T h U)) :
    (∫ z, Φ z ∂μ.prod η) = ∫ U, φ U ∂μ := by
  rw [integral_prod_symm _ hΦ]
  have hfiber (h : H) : (∫ U, Φ (U,h) ∂μ) = ∫ U, φ U ∂μ := by
    calc
      _ = ∫ U, φ (T h U) ∂μ :=
        integral_congr_ae (Filter.Eventually.of_forall (fun U => hpoint U h))
      _ = _ := (hT h).integral_comp' φ
  simp_rw [hfiber]
  simp

theorem integral_tilted_equiv_transport {Y H : Type*}
    [MeasurableSpace Y] [MeasurableSpace H]
    (μ : Measure Y) [IsProbabilityMeasure μ] (η : Measure H) [IsProbabilityMeasure η]
    (T : H → Y ≃ᵐ Y) (hT : ∀ h, MeasurePreserving (T h) μ μ)
    (S : Y × H → ℝ) (S₀ : Y → ℝ) (P : Y × H → ℂ) (P₀ : Y → ℂ)
    (hS : ∀ U h, S (U,h) = S₀ (T h U))
    (hP : ∀ U h, P (U,h) = P₀ (T h U))
    (hDensity : Integrable (fun z => Real.exp (S z)) (μ.prod η))
    (hWeighted : Integrable (fun z => (Real.exp (S z) : ℂ) * P z) (μ.prod η)) :
    (∫ z, P z ∂(μ.prod η).tilted S) = ∫ U, P₀ U ∂μ.tilted S₀ := by
  have hZ : (∫ z, Real.exp (S z) ∂μ.prod η) = ∫ U, Real.exp (S₀ U) ∂μ :=
    integral_remove_gauge μ η T hT _ _ hDensity (fun U h => congrArg Real.exp (hS U h))
  have hN : (∫ z, (Real.exp (S z) : ℂ) * P z ∂μ.prod η) =
      ∫ U, (Real.exp (S₀ U) : ℂ) * P₀ U ∂μ :=
    integral_remove_gauge μ η T hT _ _ hWeighted (by
      intro U h
      rw [hS U h, hP U h])
  rw [integral_tilted_complex_normalized, integral_tilted_complex_normalized, hZ, hN]

def matrixFeatures {C n X : Type*} (β : C → ℝ) (A : C → X → Matrix n n ℂ) :=
  realFeatures (fun q : C × (n × n) => β q.1)
    (fun q x => A q.1 x q.2.1 q.2.2)

theorem dot_matrixFeatures {C n X : Type*} [Fintype C] [Fintype n] [DecidableEq n]
    (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c) (A : C → X → Matrix n n ℂ) (x y : X) :
    dotKernel (matrixFeatures β A) x y =
      ∑ c, β c * (Matrix.trace ((A c x)ᴴ * A c y)).re := by
  classical
  rw [matrixFeatures, dot_realFeatures (fun q : C × (n × n) => β q.1)
    (fun q => hβ q.1)]
  simp only [Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro c hc
  rw [trace_conjTranspose_mul_sum, Complex.re_sum, Fintype.sum_prod_type, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Finset.mul_sum]

theorem continuous_matrixFeatures {C n X : Type*} [TopologicalSpace X]
    (β : C → ℝ) (A : C → X → Matrix n n ℂ)
    (hA : ∀ c i j, Continuous (fun x => A c x i j)) (r : (C × (n × n)) × Bool) :
    Continuous (matrixFeatures β A r) :=
  continuous_realFeatures (fun q : C × (n × n) => β q.1)
    (fun q x => A q.1 x q.2.1 q.2.2) (fun q => hA q.1 q.2.1 q.2.2) r

theorem continuous_unitaryCharacter {G n : Type*} [Group G] [TopologicalSpace G]
    [Fintype n] [DecidableEq n] (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j)) :
    Continuous (unitaryCharacter ρ) := by
  unfold unitaryCharacter Matrix.trace Matrix.diag
  exact Complex.continuous_re.comp (continuous_finset_sum _ (fun i _ => hρ i i))

theorem reducedSlabExponent_eq_split {E C G n : Type*} [Group G]
    [Fintype C] [Fintype n] [DecidableEq n]
    (edge : C → E) (ρ : G →* Matrix.unitaryGroup n ℂ)
    (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c) (s : (E → G) → ℝ) :
    reducedSlabExponent edge (unitaryCharacter ρ) β s =
      splitExponent s (matrixFeatures β (fun c U => (ρ (U (edge c)) : Matrix n n ℂ))) := by
  funext p
  unfold reducedSlabExponent splitExponent
  rw [dot_matrixFeatures β hβ]
  congr 1
  apply Finset.sum_congr rfl
  intro c hc
  congr 1
  simp only [unitaryCharacter, map_mul, map_inv, Matrix.UnitaryGroup.mul_val,
    Matrix.UnitaryGroup.inv_val, Matrix.star_eq_conjTranspose]

#print axioms integral_remove_gauge
#print axioms integral_tilted_equiv_transport
#print axioms matrixFeatures
#print axioms dot_matrixFeatures
#print axioms continuous_matrixFeatures
#print axioms continuous_unitaryCharacter
#print axioms reducedSlabExponent_eq_split
end
end Millennium.G4.WilsonRP

namespace Millennium.G4.WilsonRP
noncomputable section
open MeasureTheory Filter
open scoped BigOperators Topology ComplexConjugate Matrix

section OpenSlab
variable {V E C G n : Type*} [DecidableEq V] [Fintype E] [Fintype C]
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [SecondCountableTopology G] [MeasurableSpace G] [BorelSpace G]
  [Fintype n] [DecidableEq n]

def positiveBoundaryEquiv (src dst : E → V) (B : Finset V) (h : ↥B → G) :
    ((E → G) × (E → G)) ≃ᵐ ((E → G) × (E → G)) :=
  (MeasurableEquiv.refl (E → G)).prodCongr
    (gaugeEquiv (fun e => boundaryGauge B h (src e))
      (fun e => (boundaryGauge B h (dst e))⁻¹))

theorem positiveBoundaryEquiv_apply (src dst : E → V) (B : Finset V)
    (h : ↥B → G) (U : (E → G) × (E → G)) :
    positiveBoundaryEquiv src dst B h U =
      (U.1, vertexGauge src dst (boundaryGauge B h) U.2) := rfl

theorem measurePreserving_positiveBoundaryEquiv
    (m : Measure G) [IsProbabilityMeasure m]
    [Measure.IsMulLeftInvariant m] [Measure.IsMulRightInvariant m]
    (src dst : E → V) (B : Finset V) (h : ↥B → G) :
    MeasurePreserving (positiveBoundaryEquiv src dst B h)
      ((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m)))
      ((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m))) := by
  have hid : MeasurePreserving (id : (E → G) → (E → G))
      (Measure.pi (fun _ : E => m)) (Measure.pi (fun _ : E => m)) :=
    ⟨measurable_id, Measure.map_id⟩
  exact hid.prod (measurePreserving_gaugeMap m
    (fun e => boundaryGauge B h (src e)) (fun e => (boundaryGauge B h (dst e))⁻¹))

theorem continuous_slabReflection (B : Finset V) :
    Continuous (slabReflection (E := E) (G := G) B) := by
  apply Continuous.prodMk
  · exact (continuous_snd.comp continuous_fst).prodMk
      (continuous_fst.comp continuous_fst)
  · apply continuous_pi
    intro b
    exact ((continuous_apply b).comp continuous_snd).inv

theorem continuous_reflectedProduct {B : Finset V} (F : (E → G) → ℂ)
    (hF : Continuous F) : Continuous (reflectedProduct (B := B) F) := by
  change Continuous (fun x : ((E → G) × (E → G)) × (↥B → G) =>
    conj (F x.1.1) * F x.1.2)
  exact (Complex.continuous_conj.comp (hF.comp (continuous_fst.comp continuous_fst))).mul
    (hF.comp (continuous_snd.comp continuous_fst))

/-- Exact equality of normalized integrals for the original boundary links.
The equality is derived from coordinate Haar preservation and Fubini. -/
theorem openSlab_integral_eq_reduced
    (m : Measure G) [IsProbabilityMeasure m]
    [Measure.IsMulLeftInvariant m] [Measure.IsMulRightInvariant m]
    (src dst : E → V) (edge : C → E) {B : Finset V}
    (bsrc bdst : C → ↥B)
    (hsrc : ∀ c, src (edge c) = (bsrc c).val)
    (hdst : ∀ c, dst (edge c) = (bdst c).val)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j))
    (β : C → ℝ) (s : (E → G) → ℝ) (F : (E → G) → ℂ)
    (hs : Continuous s) (hsGauge : GaugeInvariant src dst s)
    (hF : Continuous F) (hFGauge : GaugeInvariant src dst F) :
    (∫ x, reflectedProduct F x ∂
      (((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m))).prod
        (Measure.pi (fun _ : ↥B => m))).tilted
          (slabExponent edge bsrc bdst (unitaryCharacter ρ) β s)) =
    ∫ U : (E → G) × (E → G), conj (F U.1) * F U.2 ∂
      ((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m))).tilted
        (reducedSlabExponent edge (unitaryCharacter ρ) β s) := by
  let μ := Measure.pi (fun _ : E => m)
  let η := Measure.pi (fun _ : ↥B => m)
  let S := slabExponent edge bsrc bdst (unitaryCharacter ρ) β s
  have hS : Continuous S := continuous_slabExponent edge bsrc bdst _ β s
    (continuous_unitaryCharacter ρ hρ) hs
  apply integral_tilted_equiv_transport (μ.prod μ) η
    (positiveBoundaryEquiv src dst B)
    (measurePreserving_positiveBoundaryEquiv m src dst B)
  · intro U h
    exact slabExponent_gauge src dst edge bsrc bdst hsrc hdst _ β s hsGauge
      (unitaryCharacter_relative ρ) U.1 U.2 h
  · intro U h
    exact reflectedProduct_gauge src dst F hFGauge U.1 U.2 h
  · exact Millennium.G4.IntegralRP.integrable_continuous_compact _ _ (Real.continuous_exp.comp hS)
  · exact Millennium.G4.IntegralRP.integrable_continuous_compact _ _
      ((Complex.continuous_ofReal.comp (Real.continuous_exp.comp hS)).mul
        (continuous_reflectedProduct F hF))

/-- Finite open-slab reflection positivity for an actual compact-group Wilson density.
The base law is supplied as normalized bi-invariant Haar. No continuum limit is asserted. -/
theorem openSlab_wilson_reflection_positive
    (m : Measure G) [IsProbabilityMeasure m]
    [Measure.IsMulLeftInvariant m] [Measure.IsMulRightInvariant m]
    (src dst : E → V) (edge : C → E) {B : Finset V}
    (bsrc bdst : C → ↥B)
    (hsrc : ∀ c, src (edge c) = (bsrc c).val)
    (hdst : ∀ c, dst (edge c) = (bdst c).val)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j))
    (β : C → ℝ) (hβ : ∀ c, 0 ≤ β c)
    (s : (E → G) → ℝ) (F : (E → G) → ℂ)
    (hs : Continuous s) (hsGauge : GaugeInvariant src dst s)
    (hF : Continuous F) (hFGauge : GaugeInvariant src dst F) :
    let ν := (((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m))).prod
        (Measure.pi (fun _ : ↥B => m))).tilted
          (slabExponent edge bsrc bdst (unitaryCharacter ρ) β s)
    IsProbabilityMeasure ν ∧ Integrable (reflectedProduct (B := B) F) ν ∧
      Millennium.G4.ComplexRP.NonnegativeComplex
        (Millennium.G4.IntegralRP.reflectedIntegral ν (slabReflection B)
          (positiveHalfTest F) (positiveHalfTest F)) := by
  dsimp only
  have hS := continuous_slabExponent edge bsrc bdst _ β s
    (continuous_unitaryCharacter ρ hρ) hs
  have hprob := Millennium.G4.IntegralRP.wilson_tilt_probability
    (((Measure.pi (fun _ : E => m)).prod (Measure.pi (fun _ : E => m))).prod
      (Measure.pi (fun _ : ↥B => m))) _ hS
  refine ⟨hprob, ?_, ?_⟩
  · letI := hprob
    exact Millennium.G4.IntegralRP.integrable_continuous_compact _ _
      (continuous_reflectedProduct F hF)
  · change Millennium.G4.ComplexRP.NonnegativeComplex (∫ x, reflectedProduct F x ∂_)
    rw [openSlab_integral_eq_reduced m src dst edge bsrc bdst hsrc hdst ρ hρ β s F
      hs hsGauge hF hFGauge, reducedSlabExponent_eq_split edge ρ β hβ s]
    exact (split_wilson_reflection_positive (Measure.pi (fun _ : E => m)) s
      (matrixFeatures β (fun c U => (ρ (U (edge c)) : Matrix n n ℂ))) F hs
      (continuous_matrixFeatures β _ (fun c i j => (hρ i j).comp (continuous_apply (edge c))))
      hF).2

/-- Weighted Wilson plaquettes supply the invariant half-action required above. -/
theorem gaugeInvariant_wilsonHalfAction {P : Type*} [Fintype P]
    (src dst : E → V) (e1 e2 e3 e4 : P → E)
    (h12 : ∀ p, dst (e1 p) = src (e2 p))
    (h23 : ∀ p, dst (e2 p) = dst (e3 p))
    (h34 : ∀ p, src (e3 p) = dst (e4 p))
    (h41 : ∀ p, src (e4 p) = src (e1 p))
    (ρ : G →* Matrix.unitaryGroup n ℂ) (w : P → ℝ) :
    GaugeInvariant src dst (fun U => ∑ p, w p *
      unitaryCharacter ρ (plaquetteWord (e1 p) (e2 p) (e3 p) (e4 p) U)) := by
  intro g U
  apply Finset.sum_congr rfl
  intro p hp
  exact congrArg (fun z => w p * z)
    (gaugeInvariant_plaquette src dst (e1 p) (e2 p) (e3 p) (e4 p)
      (h12 p) (h23 p) (h34 p) (h41 p) _ (unitaryCharacter_conjugate ρ) g U)

theorem continuous_wilsonHalfAction {P : Type*} [Fintype P]
    (e1 e2 e3 e4 : P → E)
    (ρ : G →* Matrix.unitaryGroup n ℂ)
    (hρ : ∀ i j, Continuous (fun g => (ρ g : Matrix n n ℂ) i j)) (w : P → ℝ) :
    Continuous (fun U => ∑ p, w p *
      unitaryCharacter ρ (plaquetteWord (e1 p) (e2 p) (e3 p) (e4 p) U)) := by
  apply continuous_finset_sum
  intro p hp
  exact continuous_const.mul ((continuous_unitaryCharacter ρ hρ).comp
    ((((continuous_apply (e1 p)).mul (continuous_apply (e2 p))).mul
      (continuous_apply (e3 p)).inv).mul (continuous_apply (e4 p)).inv))

#print axioms positiveBoundaryEquiv
#print axioms positiveBoundaryEquiv_apply
#print axioms measurePreserving_positiveBoundaryEquiv
#print axioms continuous_slabReflection
#print axioms continuous_reflectedProduct
#print axioms openSlab_integral_eq_reduced
#print axioms openSlab_wilson_reflection_positive
#print axioms gaugeInvariant_wilsonHalfAction
#print axioms continuous_wilsonHalfAction
end OpenSlab
end
end Millennium.G4.WilsonRP
