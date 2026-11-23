import Mathlib.Algebra.QuadraticDiscriminant
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Topology.MetricSpace.IsometricSMul
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.CoarseHolonomies
open Finset MeasureTheory

/-- Net displacement by k repeated isometries. -/
theorem powerDisplacement {G X : Type*} [Monoid G] [PseudoMetricSpace X]
    [MulAction G X] [IsIsometricSMul G X] (h : G) (v : X) (k : ℕ) :
    dist v (h^k • v) ≤ (k : ℝ) * dist v (h • v) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, mul_smul]
    refine (dist_triangle v (h^k • v) _).trans ?_
    rw [dist_smul, Nat.cast_succ, add_mul, one_mul]
    exact add_le_add_right ih _

/-- Mixed changes factor exactly when each action face misses at least one of the two links. -/
theorem faceFactorization {ι : Type*} (s : Finset ι) (a b ab z : ι → ℝ)
    (miss : ∀ i ∈ s, (ab i = a i ∧ b i = z i) ∨ (ab i = b i ∧ a i = z i)) :
    Real.exp (∑ i ∈ s, ab i) * Real.exp (∑ i ∈ s, z i) =
      Real.exp (∑ i ∈ s, a i) * Real.exp (∑ i ∈ s, b i) := by
  rw [← Real.exp_add, ← Real.exp_add, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  apply congrArg Real.exp
  apply Finset.sum_congr rfl
  intro i hi
  rcases miss i hi with ⟨h,j⟩ | ⟨h,j⟩
  · rw [h,j]
  · rw [h,j,add_comm]

/-- The overlap argument for actual integrals, for an arbitrary metric-valued orbit. -/
theorem overlapVariance {ι X : Type*} [MeasurableSpace ι] [PseudoMetricSpace X]
    (μ : Measure ι) (r p q : ι → ℝ) (u w : ι → X) (z : X) (a : ℝ)
    (hr : ∀ i, 0 ≤ r i) (hp : ∀ i, r i ≤ p i) (hq : ∀ i, r i ≤ q i)
    (ir : Integrable r μ) (ip : Integrable (fun i => p i * dist (u i) z ^ 2) μ)
    (iq : Integrable (fun i => q i * dist (w i) z ^ 2) μ)
    (step : ∀ i, dist (u i) (w i) = a) :
    (∫ i, r i ∂μ) * a^2 ≤
      2 * ((∫ i, p i * dist (u i) z ^ 2 ∂μ) + ∫ i, q i * dist (w i) z ^ 2 ∂μ) := by
  rw [← integral_mul_const, ← integral_add ip iq, ← integral_const_mul]
  apply integral_mono (ir.mul_const _) ((ip.add iq).const_mul _)
  intro i
  have triangle := dist_triangle_right (u i) (w i) z
  rw [step i] at triangle
  have ha : 0 ≤ a := step i ▸ dist_nonneg
  have square := mul_self_le_mul_self ha triangle
  have bound : a^2 ≤ 2*(dist (u i) z ^2 + dist (w i) z ^2) := by
    nlinarith only [square, sq_nonneg (dist (u i) z - dist (w i) z)]
  have one := mul_le_mul_of_nonneg_left bound (hr i)
  have two := mul_le_mul_of_nonneg_right (hp i) (sq_nonneg (dist (u i) z))
  have three := mul_le_mul_of_nonneg_right (hq i) (sq_nonneg (dist (w i) z))
  dsimp
  linarith only [one,two,three]

/-- Weighted Fisher inequality along a finite normalized law. -/
theorem shiftScore {ι : Type*} (s : Finset ι) (p d : ι → ℝ)
    (hp : ∀ i ∈ s, 0 ≤ p i) (norm : ∑ i ∈ s, p i = 1) :
    (∑ i ∈ s, p i * |d i|)^2 ≤ ∑ i ∈ s, p i * (d i)^2 := by
  let m := ∑ i ∈ s, p i * |d i|
  have each : 0 ≤ ∑ i ∈ s, p i * (|d i| - m)^2 :=
    Finset.sum_nonneg fun i hi => mul_nonneg (hp i hi) (sq_nonneg _)
  have rewriteSummand (i : ι) : p i * (|d i| - m)^2 =
      p i*(d i)^2 - (p i*|d i|)*(2*m) + p i*m^2 := by
    rw [sub_sq, sq_abs]; ring
  simp_rw [rewriteSummand] at each
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.sum_mul, ← Finset.sum_mul, norm] at each
  change m^2 ≤ _
  change 0 ≤ _ - m*(2*m) + 1*m^2 at each
  linarith only [each]

/-- Small-shift overlap propagates through k equal steps to a variance floor. -/
-- PCP begin certificate
theorem displacementFloor {D s k : ℝ} (propagate : 2 ≤ k^2*s)
    (overlap : s ≤ 8*D) : 1 ≤ 4*k^2*D := by
  have h := mul_le_mul_of_nonneg_left overlap (sq_nonneg k)
  linarith only [propagate, h]
-- PCP end certificate

/-- The sum of squared step counts for diffusion at the inverse Hessian scale. -/
theorem heatSteps {r L : ℝ} : (1+r*L)^2 ≤ 2+2*r^2*L^2 := by
  nlinarith only [sq_nonneg (1-r*L)]

/-- Multiplying nonidentical contractions, including two smoothing endpoints. -/
theorem iterateBound {u : ℕ → ℝ} {q A : ℝ} (hq : 0 ≤ q) (start : u 0 ≤ A)
    (step : ∀ n, u (n+1) ≤ q*u n) (n : ℕ) : u n ≤ A*q^n := by
  induction n with
  | zero => simpa using start
  | succ n ih =>
    calc
      u (n+1) ≤ q*u n := step n
      _ ≤ q*(A*q^n) := mul_le_mul_of_nonneg_left ih hq
      _ = _ := by rw [pow_succ]; ring

/-- A relative density bound survives products with an explicit accumulated error. -/
theorem productDensity (p e : ℕ → ℝ) (n : ℕ)
    (bounds : ∀ i, |p i-1| ≤ e i) :
    |(∏ i ∈ range n, p i)-1| ≤ (∏ i ∈ range n, (1+e i))-1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    let P := ∏ i ∈ range n, p i
    let E := ∏ i ∈ range n, (1+e i)
    have hp : |p n| ≤ 1+e n := by
      have h := abs_add_le (p n - 1) 1
      rw [sub_add_cancel, abs_one] at h
      linarith [bounds n]
    have h := mul_le_mul ih hp (abs_nonneg (p n)) (le_trans (abs_nonneg _) ih)
    change |P-1| * |p n| ≤ (E-1)*(1+e n) at h
    rw [Finset.prod_range_succ, Finset.prod_range_succ]
    change |P*p n-1| ≤ E*(1+e n)-1
    have id : P*p n-1 = (P-1)*p n + (p n-1) := by ring
    rw [id]
    refine (abs_add_le _ _).trans ?_
    rw [abs_mul]
    linarith only [h, bounds n]

/-- Tensorization for the actual likelihood-ratio second moments. -/
theorem productSecondMoment {ι κ : Type*} [MeasurableSpace ι] [MeasurableSpace κ]
    (μ : Measure ι) (ν : Measure κ) [SFinite μ] [SFinite ν] (f : ι → ℝ) (g : κ → ℝ) :
    (∫ z, (f z.1*g z.2)^2 ∂μ.prod ν) =
    (∫ i, (f i)^2 ∂μ)*(∫ j, (g j)^2 ∂ν) := by
  simp_rw [mul_pow]
  exact integral_prod_mul (μ := μ) (ν := ν) (fun i => (f i)^2) (fun j => (g j)^2)

/-- Reverse chi-square relative to an arbitrary reference probability. -/
theorem inverseDensity {ι : Type*} [MeasurableSpace ι] (μ : Measure ι) [IsProbabilityMeasure μ]
    (p : ι → ℝ) (pos : ∀ i, 0 < p i) (ip : Integrable p μ)
    (ir : Integrable (fun i => 1/p i) μ) (norm : ∫ i, p i ∂μ = 1) :
    (∫ i, 1/p i ∂μ)-1 = ∫ i, (p i-1)^2/p i ∂μ := by
  have term (i : ι) : (p i-1)^2/p i = 1/p i + p i - 2 := by
    field_simp [(pos i).ne']
    ring
  simp_rw [term]
  have j : Integrable (fun i => 1/p i+p i) μ := ir.add ip
  rw [integral_sub j (integrable_const (2:ℝ)), integral_add ir ip, norm]
  simp
  ring

/-- Reverse likelihood weighting controls actual conditional expectations in their own L² norm. -/
theorem reverseBias {ι : Type*} [MeasurableSpace ι] (μ : Measure ι)
    (f r : ι → ℝ) (ff : Integrable (fun i => f i ^ 2) μ)
    (rr : Integrable (fun i => (1-r i)^2) μ) (fr : Integrable (fun i => f i*(1-r i)) μ)
    (u v K : ℝ) (density : u-v = ∫ i, f i*(1-r i) ∂μ)
    (divergence : (∫ i, (1-r i)^2 ∂μ) ≤ K) :
    (u-v)^2 ≤ (∫ i, f i^2 ∂μ)*K := by
  let A := ∫ i, f i^2 ∂μ
  let B := ∫ i, f i*(1-r i) ∂μ
  let C := ∫ i, (1-r i)^2 ∂μ
  have pos : ∀ t : ℝ, 0 ≤ A*(t*t)+(2*B)*t+C := by
    intro t
    have j : Integrable (fun i => f i^2*(t*t) + f i*(1-r i)*(2*t)) μ :=
      (ff.mul_const _).add (fr.mul_const _)
    have h : 0 ≤ ∫ i, ((f i)^2*(t*t) + (f i*(1-r i))*(2*t) + (1-r i)^2) ∂μ := by
      apply integral_nonneg
      intro i
      change 0 ≤ f i^2*(t*t) + f i*(1-r i)*(2*t) + (1-r i)^2
      nlinarith only [sq_nonneg (f i*t+(1-r i))]
    rw [integral_add j rr, integral_add (ff.mul_const (t*t)) (fr.mul_const (2*t)),
        integral_mul_const, integral_mul_const] at h
    change 0 ≤ A*(t*t)+B*(2*t)+C at h
    linarith only [h]
  have h := discrim_le_zero pos
  have ha : 0 ≤ A := integral_nonneg fun _ => sq_nonneg _
  have hd : A*C ≤ A*K := mul_le_mul_of_nonneg_left divergence ha
  change (u-v)^2 ≤ A*K
  rw [density]
  change B^2 ≤ A*K
  unfold discrim at h
  linarith only [h,hd]

/-- Turn a Haar-centered density error into a conditional squared-norm estimate. -/
theorem exteriorBound {A F V d : ℝ} (small : d < 1)
    (bias : |A| ≤ d*|F|) (norm : (1-d)*F^2 ≤ V) :
    (1-d)*A^2 ≤ d^2*V := by
  have s := mul_self_le_mul_self (abs_nonneg A) bias
  have ss : A^2 ≤ d^2*F^2 := by
    rw [← sq_abs A, ← sq_abs F]; nlinarith only [s]
  have h := mul_le_mul_of_nonneg_left ss (sub_nonneg.mpr small.le)
  have j := mul_le_mul_of_nonneg_left norm (sq_nonneg d)
  linarith only [h,j]

/-- The two-step transfer norm controls a spectral interval. -/
theorem spectralWindow {ι : Type*} (s : Finset ι) (p v : ι → ℝ) {t : ℝ}
    (ht : 0 ≤ t) (hv : ∀ i ∈ s, t ≤ v i) (hp : ∀ i ∈ s, 0 ≤ p i) :
    t^2*(∑ i ∈ s, p i) ≤ ∑ i ∈ s, p i*(v i)^2 := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have h := mul_self_le_mul_self ht (hv i hi)
  nlinarith only [mul_le_mul_of_nonneg_left h (hp i hi)]

/-- Conditional first two moments of the trace score for either central sign. -/
theorem scoreMoments {s c : ℝ} :
    (4*s)*(2*s) = 8*s^2 ∧
      (4*s)^2*(1+3*c-(2*s)^2) = 16*s^2 + 48*s^2*c-64*s^4 := by
  constructor <;> ring

/-- Positive insertions keep a relative bound after multiplication by any positive exterior test. -/
theorem positiveInsertion {ι : Type*} [MeasurableSpace ι] (μ : Measure ι)
    (g a : ι → ℝ) (q l u : ℝ) (hg : ∀ i, 0 ≤ g i)
    (ig : Integrable g μ) (iga : Integrable (fun i => g i*a i) μ)
    (lo : ∀ i, l*q ≤ a i) (hi : ∀ i, a i ≤ u*q) :
    (∫ i, g i ∂μ)*(l*q) ≤ (∫ i, g i*a i ∂μ) ∧
      (∫ i, g i*a i ∂μ) ≤ (∫ i, g i ∂μ)*(u*q) := by
  rw [← integral_mul_const, ← integral_mul_const]
  exact ⟨integral_mono (ig.mul_const _) iga fun i => mul_le_mul_of_nonneg_left (lo i) (hg i),
         integral_mono iga (ig.mul_const _) fun i => mul_le_mul_of_nonneg_left (hi i) (hg i)⟩

/-- Exact cancellation of the even part before the binary log-likelihood expansion. -/
theorem centerParity {a e o : ℝ} :
    ((1+e)+(a+o))-((1+e)-(a+o)) = 2*a+2*o := by ring

-- PCP begin geometry
theorem interiorLinks (m : ℕ) (h : 2 ≤ m) : (m-2)+2 = m := by omega
-- PCP end geometry

#print axioms positiveInsertion
#print axioms reverseBias
#print axioms scoreMoments
#print axioms centerParity
#print axioms faceFactorization
#print axioms inverseDensity
#print axioms powerDisplacement
#print axioms overlapVariance
#print axioms shiftScore
#print axioms displacementFloor
#print axioms heatSteps
#print axioms iterateBound
#print axioms productDensity
#print axioms productSecondMoment
#print axioms exteriorBound
#print axioms spectralWindow
#print axioms interiorLinks

end Millennium.YangMills.CoarseHolonomies
