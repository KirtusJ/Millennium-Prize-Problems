import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

open MeasureTheory Filter
open scoped Topology

namespace YangMills.StapleResponse

/-- Squared innovations on two distinct product fibers have the same mixed
moment as their exterior second moments, even when the fiber laws vary. -/
theorem squaredFiber {E A B : Type*} [MeasurableSpace E] [MeasurableSpace A]
    [MeasurableSpace B] (ρ : Measure E) (μ : E → Measure A) (ν : E → Measure B)
    [∀ e, SFinite (μ e)] [∀ e, SFinite (ν e)] (f : E → A → ℝ) (g : E → B → ℝ) :
    (∫ e, ∫ z : A × B, f e z.1 ^ 2 * g e z.2 ^ 2 ∂(μ e).prod (ν e) ∂ρ) =
      ∫ e, (∫ u, (f e u)^2 ∂(μ e))*(∫ v, (g e v)^2 ∂(ν e)) ∂ρ := by
  apply integral_congr_ae
  filter_upwards with e
  exact integral_prod_mul (fun u => (f e u)^2) (fun v => (g e v)^2)

/-- Multiplication by an arbitrary boundary or spectator weight commutes with
integrating out the one temporal link at fixed remaining links. -/
theorem boundaryInsertion {E A : Type*} [MeasurableSpace E] [MeasurableSpace A]
    (ρ : Measure E) (μ : E → Measure A) (w : E → ℝ) (f : E → A → ℝ) :
    (∫ e, ∫ a, w e * f e a ∂(μ e) ∂ρ) = ∫ e, w e * (∫ a, f e a ∂(μ e)) ∂ρ := by
  apply integral_congr_ae
  filter_upwards with e
  exact integral_const_mul (w e) (f e)

/-- Multiply through by the squared normalizer to compare the three Taylor
polynomials for the raw tilted-gamma moments. -/
theorem tiltedVariance (x : ℝ) :
    let a := 1-3*x/8-15*x^2/128
    let b := 3/2-15*x/16-105*x^2/256
    let c := 15/4-105*x/32-945*x^2/512
    c*a-b^2-(3/2-3*x/4-9*x^2/8)*a^2 =
      x^3*(2025*x^3/131072+7155*x^2/65536-99*x/8192-189/256) := by
  dsimp
  ring

theorem reciprocalRemainder (β R : ℝ) (h : R ≠ 0) :
    β^2/R-β/6-(6*β-R)/36=(6*β-R)^2/(36*R) := by
  field_simp
  ring

theorem reciprocalSquare (β R : ℝ) (h : R ≠ 0) :
    β^2/R^2-1/36=(6*β-R)*(6*β+R)/(36*R^2) := by
  field_simp
  ring

theorem environmentExpansion (β R : ℝ) (h : R ≠ 0) :
    β^2*(-3/(4*R)-9/(8*R^2))+β/8+(6*β-R)/48+1/32 =
      -(6*β-R)^2/(48*R)-(6*β-R)*(6*β+R)/(32*R^2) := by
  field_simp
  ring

theorem secondMean : -(3:ℝ)/48-1/32 = -3/32 := by norm_num

/-- Covariance of two centered quadratic energies in three independent colors
after the Gaussian fourth-moment contraction has been supplied. -/
theorem wickContraction {ι : Type*} (s : Finset ι) (K : ι → ℝ) (cov : ℝ)
    (wick : cov = (3/2)*∑ i ∈ s, (K i)^2) :
    cov / 48^2 = (∑ i ∈ s, (K i)^2)/1536 := by rw [wick]; ring

theorem projectedSignal {ι : Type*} (s : Finset ι) (K : ι → ℝ)
    {j : ι} (hj : j ∈ s) (h : K j ≠ 0) : 0 < (∑ i ∈ s, (K i)^2)/1536 := by
  have h₁ := Finset.single_le_sum (f := fun i => (K i)^2)
    (fun i (_ : i ∈ s) => sq_nonneg (K i)) hj
  exact div_pos ((sq_pos_of_ne_zero h).trans_le h₁) (by norm_num)

/-- Pass from convergence of each rescaled projected cross entry to convergence
of the rescaled squared Frobenius reading. -/
theorem transferTail {ι : Type*} (s : Finset ι) (K : ℕ → ι → ℝ) (c : ι → ℝ)
    (h : ∀ i ∈ s, Tendsto (fun n : ℕ => (n:ℝ)^4*K n i) atTop (𝓝 (c i))) :
    Tendsto (fun n : ℕ => (n:ℝ)^8*(∑ i ∈ s, (K n i)^2)/1536) atTop
      (𝓝 ((∑ i ∈ s, (c i)^2)/1536)) := by
  have z := tendsto_finset_sum s (fun i hi => (h i hi).pow 2)
  convert z.div_const 1536 using 1
  ext n
  rw [Finset.mul_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem spatialCoefficient (p : ℝ) (hp : p ≠ 0) :
    12*(1/p^2)^2/1536=1/(128*p^4) := by field_simp; ring

end YangMills.StapleResponse

#print axioms YangMills.StapleResponse.boundaryInsertion
#print axioms YangMills.StapleResponse.squaredFiber
#print axioms YangMills.StapleResponse.tiltedVariance
#print axioms YangMills.StapleResponse.reciprocalRemainder
#print axioms YangMills.StapleResponse.reciprocalSquare
#print axioms YangMills.StapleResponse.environmentExpansion
#print axioms YangMills.StapleResponse.secondMean
#print axioms YangMills.StapleResponse.wickContraction
#print axioms YangMills.StapleResponse.projectedSignal
#print axioms YangMills.StapleResponse.transferTail
#print axioms YangMills.StapleResponse.spatialCoefficient
