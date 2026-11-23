import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

open MeasureTheory Set
open scoped BigOperators
namespace YangMills.ElectricDisorder

theorem twistConjugation {R : Type*} [Ring R] {d v h w : R}
    (hinv : d*v=1) (hw : v*h*d=h+w) : h*d-d*h=d*w := by
  have t := congrArg (d*·) hw
  change d*(v*h*d)=d*(h+w) at t
  rw [← mul_assoc, ← mul_assoc, hinv, one_mul, mul_add] at t
  rw [t]
  abel

/-- Unit-disk trace deficit controls squared distance from one. -/
theorem diskDefect {x y : ℝ} (hd : x^2+y^2 ≤ 1) :
    (1-x)^2+y^2 ≤ 2*(1-x) := by nlinarith

/-- A normalized nonnegative average of bounded SU(2) plaquette defects. -/
theorem meanSquare (s : Finset ℕ) (p d : ℕ → ℝ)
    (hp : ∀ i ∈ s, 0 ≤ p i) (hn : ∑ i ∈ s, p i = 1)
    (hd : ∀ i ∈ s, 0 ≤ d i ∧ d i ≤ 2) :
    (∑ i ∈ s, p i*d i)^2 ≤ 2*(∑ i ∈ s, p i*d i) := by
  have lo : 0 ≤ ∑ i ∈ s, p i*d i :=
    Finset.sum_nonneg fun i hi => mul_nonneg (hp i hi) (hd i hi).1
  have hi : (∑ i ∈ s, p i*d i) ≤ 2 := calc
    _ ≤ ∑ i ∈ s, p i*2 := Finset.sum_le_sum fun i hi =>
      mul_le_mul_of_nonneg_left (hd i hi).2 (hp i hi)
    _ = 2 := by rw [← Finset.sum_mul, hn, one_mul]
  nlinarith [mul_nonneg lo (sub_nonneg.mpr hi)]

private def shiftSite (n site axis : ℕ) : ℕ :=
  let stride := n^axis
  let digit := site / stride % n
  site - stride*digit + stride*((digit+1)%n)

private def corners (n p : ℕ) : List ℕ :=
  let s := p/3
  let i := (p%3+1)%3
  let j := (p%3+2)%3
  [3*s+i,3*shiftSite n s i+j,3*shiftSite n s j+i,3*s+j]

private def flipped (n e : ℕ) := (List.range (3*n^3)).filter fun p => (corners n p).contains e

theorem sideThreeFixture : (flipped 3 0).length = 4 ∧
    ((flipped 3 0).filter fun p => (flipped 3 1).contains p).length = 1 := by decide +kernel

theorem residualTail (μ : Measure ℝ) [IsFiniteMeasure μ] (δ : ℝ) (hδ : 0 < δ)
    (hi : Integrable (fun x : ℝ => (x-1)^2) μ) :
    δ^2 * μ.real {x : ℝ | δ ≤ |x-1|} ≤ ∫ x, (x-1)^2 ∂μ := by
  let S := {x : ℝ | δ ≤ |x-1|}
  have hs : MeasurableSet S := measurableSet_le measurable_const
    ((continuous_id.sub continuous_const).abs.measurable)
  have h := integral_mono_ae ((integrable_const (μ := μ) (δ^2)).indicator hs) hi
    (Filter.Eventually.of_forall (fun x => show S.indicator (fun _ => δ^2) x ≤ (x-1)^2 by
      by_cases hx : x ∈ S
      · rw [indicator_of_mem hx]
        have hh : δ ≤ |x-1| := hx
        nlinarith [sq_abs (x-1), mul_nonneg (sub_nonneg.mpr hh)
          (add_nonneg (abs_nonneg (x-1)) hδ.le)]
      · rw [indicator_of_not_mem hx]
        positivity))
  rw [integral_indicator hs] at h
  simpa [S, mul_comm] using h

theorem vacuumBound (μ : Measure ℝ) [IsFiniteMeasure μ]
    (hi : Integrable (fun x : ℝ => (x-1)^2) μ) :
    μ.real {0} ≤ ∫ x, (x-1)^2 ∂μ := by
  have hset : ({0} : Set ℝ) ⊆ {x | 1 ≤ |x-1|} := by
    intro x hx
    simp only [mem_singleton_iff] at hx
    subst x
    norm_num
  exact (measureReal_mono (μ := μ) hset).trans (by simpa using residualTail μ 1 (by norm_num) hi)

theorem twoStepSquare {x c : ℝ} : (x-c)^2=x^2-2*c*x+c^2 := by ring

theorem transferBudget {ham wilson normStep vacuum err : ℝ} (h1 : wilson ≤ ham+normStep+vacuum)
    (hn : 0 ≤ wilson) (h : ham ≤ err) :
    wilson^2 ≤ (err+normStep+vacuum)^2 := by
  have hb : wilson ≤ err+normStep+vacuum := by linarith
  nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ err+normStep+vacuum+wilson by linarith)]

private def shiftEnergy (n : ℕ) : ℕ := (flipped 3 n).length*2
theorem fourFacesEnergy : shiftEnergy 0 = 8 := by decide +kernel

/-- Effective rank from a trace lower bound and a Hilbert-Schmidt budget. -/
theorem rankBudget {k allowed rank tr hs : ℝ}
    (hk : 0 ≤ k) (hr : 0 ≤ rank) (ha : 0 < allowed)
    (htr : k ≤ tr) (hcs : tr^2 ≤ rank*hs) (hhs : hs ≤ allowed) :
    k^2/allowed ≤ rank := by
  apply (div_le_iff₀ ha).mpr
  nlinarith [mul_nonneg (sub_nonneg.mpr htr) (show 0 ≤ tr+k by linarith),
    mul_nonneg hr (sub_nonneg.mpr hhs)]

theorem exactBandFraction : 1 - 16*((2:ℚ)*(17*1024/8+3/16)/2^20) = 489469/524288 := by norm_num

theorem sideFourRank : (93:ℚ) <
    192*(489469/524288)^2/(1+191*(34819/8388608)) := by norm_num

theorem threeRank : (52:ℚ) <
    81*(489469/524288)^2/(1+80*(34819/8388608)) := by norm_num

private def numLinks (n : ℕ) := 3*n^3
theorem rankCount : (numLinks 3,numLinks 4)=(81,192) := by decide

/-- Averaging all rotations/translations of a defect pattern uses each face
with the same total weight. This identity permits arbitrary input states. -/
theorem orbitAverage {ι κ : Type*} (s : Finset ι) (f : Finset κ)
    (w : ι → κ → ℝ) (cost : κ → ℝ) (c : ℝ)
    (uniform : ∀ p ∈ f, ∑ i ∈ s, w i p = c) :
    (∑ i ∈ s, ∑ p ∈ f, w i p * cost p) = c * ∑ p ∈ f, cost p := by
  rw [Finset.sum_comm, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p hp
  rw [← Finset.sum_mul, uniform p hp]

theorem subspaceFraction {err : ℝ} (he : 0 ≤ err) (h : err ≤ 7/100) :
    (92:ℝ)/100 ≤ 1-16*err^2 := by
  nlinarith [mul_nonneg (sub_nonneg.mpr h) (show 0 ≤ 7/100+err by linarith)]


/-- Cancellation of the electric timeline and the spatial trial width. -/
theorem trialClock (beta b a A : ℝ) (hbeta : 0 < beta) (hb : 0 < b) (ha : 0 < a) (hA : 0 < A) :
    (1 / ((beta*b/a)*(A^2/beta))) / (a*beta/b) = 1/(A^2*beta) := by
  field_simp
  ring

/-- Cost of the two potential factors in the one-step residual. -/
theorem stepFactors {j step bound : ℝ} (hj : 0 < j) (h : step ≤ (j⁻¹+j)*bound) :
    step*j ≤ (1+j^2)*bound := by
  have hb := mul_le_mul_of_nonneg_right h hj.le
  have eq : (j⁻¹+j)*bound*j = (1+j^2)*bound := calc
    _ = (j⁻¹*j+j^2)*bound := by ring
    _ = _ := by simp [ne_of_gt hj]
  rwa [eq] at hb

theorem projectedBadPart (μ : Measure ℝ) [IsFiniteMeasure μ] (eta : ℝ)
    (hn : ∀ᵐ x ∂μ, 0 ≤ x) (hi : Integrable (fun x : ℝ => x) μ) :
    eta * μ.real (Ici eta) ≤ ∫ x, x ∂μ := by
  have hs := measurableSet_Ici (a := eta)
  have H := integral_mono_ae ((integrable_const (μ := μ) eta).indicator hs) hi
    (by
      filter_upwards [hn] with x hx
      by_cases hmem : x ∈ Ici eta
      · rw [indicator_of_mem hmem]
        exact hmem
      · rwa [indicator_of_not_mem hmem])
  rw [integral_indicator hs] at H
  simpa [mul_comm] using H


#print axioms trialClock
#print axioms stepFactors
#print axioms projectedBadPart
#print axioms orbitAverage
#print axioms subspaceFraction
#print axioms twistConjugation
#print axioms diskDefect
#print axioms meanSquare
#print axioms sideThreeFixture
#print axioms residualTail
#print axioms vacuumBound
#print axioms twoStepSquare
#print axioms transferBudget
#print axioms fourFacesEnergy
#print axioms rankBudget
#print axioms exactBandFraction
#print axioms sideFourRank
#print axioms threeRank
#print axioms rankCount
end YangMills.ElectricDisorder
