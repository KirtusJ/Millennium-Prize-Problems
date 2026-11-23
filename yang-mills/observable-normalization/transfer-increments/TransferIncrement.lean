import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Ring

open Filter Topology

namespace YangMills.Observable

/-- Iterating a positive contraction loses at most k times its one-step defect. -/
theorem powerLoss (x : ℝ) (hx : 0 ≤ x) (h1 : x ≤ 1) (k : ℕ) :
    1 - x ^ k ≤ k * (1 - x) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hp : x ^ k ≤ 1 := pow_le_one₀ hx h1
    have h := mul_le_mul_of_nonneg_right hp (sub_nonneg.mpr h1)
    rw [pow_succ, Nat.cast_succ]
    linarith

/-- The cutoff input is the one-step Dirichlet form of this same observable. -/
theorem spectralPowerLoss {ι : Type*} (s : Finset ι) (w x : ι → ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hx : ∀ i ∈ s, 0 ≤ x i ∧ x i ≤ 1) (k : ℕ) :
    (∑ i ∈ s, w i) - (∑ i ∈ s, w i * x i ^ k) ≤
      k * (∑ i ∈ s, w i * (1 - x i)) := by
  rw [← Finset.sum_sub_distrib, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have h := mul_le_mul_of_nonneg_left (powerLoss (x i) (hx i hi).1 (hx i hi).2 k) (hw i hi)
  linarith only [h]

/-- Apply a separate one-step defect bound to each factor in a Bessel ratio. -/
theorem productLoss (xs : List ℝ) (unit : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ 1) :
    1 - xs.prod ≤ (xs.map (fun x => 1 - x)).sum := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hx := unit x (List.mem_cons_self ..)
    have ht : ∀ y ∈ xs, 0 ≤ y ∧ y ≤ 1 :=
      fun y hy => unit y (List.mem_cons_of_mem _ hy)
    have tail := ih ht
    have nonneg : 0 ≤ (xs.map (fun y => 1 - y)).sum := by
      apply List.sum_nonneg
      intro z hz
      obtain ⟨y, hy, rfl⟩ := List.mem_map.mp hz
      exact sub_nonneg.mpr (ht y hy).2
    have hscale := mul_le_mul_of_nonneg_left tail hx.1
    have hcap := mul_le_mul_of_nonneg_right hx.2 nonneg
    simp only [List.prod_cons, List.map_cons, List.sum_cons]
    linarith

/-- This interface allows different cutoffs and step counts, with a shared time budget. -/
theorem positiveTransferLimit {C V D a : ℕ → ℝ} {k : ℕ → ℕ} {c v M t : ℝ}
    (lim : Tendsto C atTop (𝓝 c)) (margin : 0 < v - t * M) (hM : 0 ≤ M)
    (controls : ∀ᶠ n in atTop, v ≤ V n ∧ V n - C n ≤ k n * D n ∧
      D n ≤ a n * M ∧ k n * a n ≤ t) :
    v - t * M ≤ c ∧ 0 < c := by
  have hl : v - t * M ≤ c := by
    apply ge_of_tendsto lim
    filter_upwards [controls] with n hn
    rcases hn with ⟨hv, hdrop, hdef, htime⟩
    have hk : 0 ≤ (k n : ℝ) := Nat.cast_nonneg _
    have hbound : (k n : ℝ) * D n ≤ t * M := calc
      _ ≤ (k n : ℝ) * (a n * M) := mul_le_mul_of_nonneg_left hdef hk
      _ = ((k n : ℝ) * a n) * M := (mul_assoc _ _ _).symm
      _ ≤ t * M := mul_le_mul_of_nonneg_right htime hM
    linarith
  exact ⟨hl, margin.trans_le hl⟩

/-- B4's proposed tangent at q works at every nonnegative separation. -/
theorem tangentMomentBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ)
    {v q t : ℝ} (hq : 0 ≤ q) (ht : 0 ≤ t) (hw : ∀ i ∈ s, 0 ≤ w i)
    (mass : v ≤ ∑ i ∈ s, w i) (moment : (∑ i ∈ s, w i * E i) ≤ v * q) :
    v * Real.exp (-t * q) ≤ ∑ i ∈ s, w i * Real.exp (-t * E i) := by
  let b := Real.exp (-t * q)
  have hb : 0 ≤ b := (Real.exp_pos _).le
  have hcoef : 0 ≤ 1 + t * q := by linarith [mul_nonneg ht hq]
  have hmass := mul_le_mul_of_nonneg_left mass hcoef
  have hmom := mul_le_mul_of_nonneg_left moment ht
  have hmin : v ≤ (1+t*q) * (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i) := by
    linarith only [hmass, hmom]
  calc
    v * b ≤ ((1+t*q) * (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i)) * b :=
      mul_le_mul_of_nonneg_right hmin hb
    _ = ∑ i ∈ s, w i * (b * ((t*q - t*E i) + 1)) := by
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib, Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro i hi
      apply mul_le_mul_of_nonneg_left _ (hw i hi)
      calc
        b * ((t*q - t*E i) + 1) ≤ b * Real.exp (t*q - t*E i) :=
          mul_le_mul_of_nonneg_left (Real.add_one_le_exp _) hb
        _ = Real.exp (-t*E i) := by
          dsimp [b]
          rw [← Real.exp_add]
          congr 1
          ring

theorem sharpMomentBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ)
    {v M t : ℝ} (hv : 0 < v) (hM : 0 ≤ M) (ht : 0 ≤ t)
    (hw : ∀ i ∈ s, 0 ≤ w i) (mass : v ≤ ∑ i ∈ s, w i)
    (moment : (∑ i ∈ s, w i * E i) ≤ M) :
    v * Real.exp (-t * (M / v)) ≤ ∑ i ∈ s, w i * Real.exp (-t * E i) := by
  apply tangentMomentBound s w E (div_nonneg hM hv.le) ht hw mass
  simpa [mul_div_cancel₀ M hv.ne', mul_comm v (M / v)] using moment

end YangMills.Observable
#print axioms YangMills.Observable.powerLoss
#print axioms YangMills.Observable.spectralPowerLoss
#print axioms YangMills.Observable.positiveTransferLimit
#print axioms YangMills.Observable.productLoss
#print axioms YangMills.Observable.tangentMomentBound
#print axioms YangMills.Observable.sharpMomentBound
